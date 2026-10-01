#!/usr/bin/env python3
"""Turn a converted course into a book.

`references/book-template.md` is the specification.

The library's first shape was a pile of converted artefacts -- slides in one directory, transcripts
in another, problem sets in a third, twelve course-years side by side. That is a hoard, not a
library: for reading page 19 of a PDF the PDF was already fine. A book merges those inputs into
chapters that teach the subject, with the same structure for every course.

    synthesise_book.py plan  <course>     what chapters it would write, from what
    synthesise_book.py submit <course>    queue the chapter prompts (Batch API, half price)
    synthesise_book.py collect            write the finished chapters, index and solutions

The inputs are the converted pages under docs/. The output replaces them.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import llm_pdf                                                        # noqa: E402
from body_rules import (_fix_stray_dollars, _protect_svg, fix_escaped_closer,   # noqa: E402
                        protect_code, restore_code,
                        _restore_svg, tidy_svg)

LIBRARY = Path(__file__).resolve().parents[3]
DOCS = LIBRARY / "docs"
CACHE = LIBRARY / "conversion-cache" / "books"
JOBS = CACHE / "batches"
MANIFESTS = CACHE / "manifests"
MODEL = "gemini-3.8-flash"
TODAY = __import__("datetime").date.today().isoformat()
REQUESTS_PER_JOB = 100
MAX_JOB_BYTES = 20_000_000
MAX_INPUT_CHARS = 220_000        # per chapter; well inside the context and keeps one bill small

# How a page's role is read off its path. Order matters: the first match wins.
ROLES = [
    ("solutions", re.compile(r"(^|/)(solutions?|sol|answers?)(/|-|$)", re.I)),
    # Recitations, tutorials and worked examples are PRACTICE, not chapters of their own. Treating
    # them as separate chapters turned 6.041SC into 86 "chapters" -- 25 lectures plus 24
    # recitations plus 43 worked examples, each a page. That is the same fragmentation the book
    # exists to remove, wearing a different label.
    # Exams sit here with the problem sets. Left out, they fell through to "notes" and became
    # chapters: 6.041SC grew `01-exam-quiz01-revi`, `02-exam` and `final-exam` as though a quiz
    # were a lecture. An exam is the course's own practice material, which is what this role means.
    ("exercises", re.compile(
        r"(^|/)(psets?|problem[-_]?sets?|homework|hw|exercises?|labs?|recitations?|tutorials?"
        r"|worked[-_]?examples?|drills?|exams?|quiz(?:zes)?|midterms?|finals?)(/|-|$)", re.I)),
    ("transcript", re.compile(r"(^|/)(recordings?|transcripts?|captions?)(/|-|$)", re.I)),
    ("slides", re.compile(r"(^|/)(lectures?|slides?|lec)(/|-|$)", re.I)),
]
TERM_DIR = re.compile(
    r"^(?:(?:fall|spring|summer|winter|autumn|au)[-_]?[a-z]?\d{2,4}|\d{4}(?:-\d{2,4})?"
    r"|[a-z0-9-]*(?:fall|spring|summer|winter)-\d{4}|aldous-legacy)$", re.I)
# A chapter key: a unit name, a lecture number, or failing both the containing directory.
UNIT = re.compile(r"(unit\s*\d+|week\s*\d+|chap(?:ter)?[-_ ]?\d+)", re.I)
LECTURE_NO = re.compile(r"(?:^|[/-])(?:lec(?:ture)?[-_ ]?)?(\d{1,2})(?:[-_./]|$)")
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
# Which source document a converted page is a section of. The converter records this on every
# page, and it is the only reliable answer: the OUTPUT path cannot distinguish section 1 of
# lecture 2 from lecture 1, because both are spelled `01-`.
SRC_FILE = re.compile(r"^source_file:\s*(.+?)\s*$", re.M)
# A term glued into a filename states the same fact as a term directory. Without this,
# `CodeLectureTwentyOne153248Fall2025` and `...Spring2025` are two chapters of the same lecture,
# which is how stat153 came to have 171: the hoarding the book removes, hidden in a filename.
TERM_IN_STEM = re.compile(r"[-_]?(?:fall|spring|summer|winter|autumn)[-_]?\d{2,4}\b", re.I)
# Above this, one document is a book rather than a lecture, and its own sections are the
# chapters. Gorin's thesis was one chapter of 240k chars, silently truncated to the 220k input
# cap -- the tail of every thesis dropped with nothing on the page saying so.
CHAPTER_BUDGET = 120_000
# A chapter that is the course's own front matter rather than its teaching.
ADMIN_CHAPTER = re.compile(
    r"^(index|home|syllabus|about|contents?|readme|calendar|schedule|overview)", re.I)
# Below this much real teaching material there is no book here. Six Berkeley courses are an
# instructor page and nothing else, and they were producing a one-chapter "book" called
# "Course Overview and Policies" -- 25 characters long, and a fatal `thin-body` finding. The
# converted syllabus still ships as a cited page; it just is not a book.
BOOK_FLOOR = 30_000
BANNER = re.compile(r"^>.*$", re.M)


@dataclass
class Chapter:
    key: str
    number: int
    title: str = ""
    slides: list = field(default_factory=list)
    transcript: list = field(default_factory=list)
    notes: list = field(default_factory=list)
    exercises: list = field(default_factory=list)
    solutions: list = field(default_factory=list)

    @property
    def inputs(self):
        return self.slides + self.transcript + self.notes

    def chars(self):
        return sum(p.stat().st_size for p in self.inputs + self.exercises)


def role_of(rel: str) -> str:
    for name, pattern in ROLES:
        if pattern.search(rel):
            return name
    return "notes"


def strip_page(path: Path) -> tuple[str, str]:
    """A converted page's title and body, with front matter and banner removed."""
    text = path.read_text(encoding="utf-8", errors="replace")
    meta = {}
    m = FRONTMATTER.match(text)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith((" ", "\t", "-")):
                k, _, v = line.partition(":")
                meta[k.strip()] = v.strip().strip("'\"")
        text = text[m.end():]
    text = BANNER.sub("", text)
    text = re.sub(r"^#\s+.*$", "", text, count=1, flags=re.M)
    # the prev/up/next footer
    text = re.sub(r"\n---\s*\n[^\n]*(?:Up:|←|→)[^\n]*\n?\Z", "\n", text)
    return meta.get("title", path.stem), text.strip()


def source_document(page: Path) -> str:
    """The source document this page is a section of, term directories stripped.

    Read from the page's own `source_file:`, not inferred from where it landed. The output path
    lies about this: the converter splits one document into `01-…`, `02-…` section pages, and a
    key built from those numbers read section 1 of twenty-two different lectures as "lecture 1".
    stat153's first chapter was the opening section of all twenty-two, and its second chapter all
    the second sections -- a book transposed, and one that would have read as plausible prose."""
    m = SRC_FILE.search(page.read_text(encoding="utf-8", errors="replace")[:1600])
    if not m:
        return ""
    parts = m.group(1).strip().strip("'\"").split("/")[2:]      # drop `sources/<slug-head>`
    return "/".join(p for p in parts if not TERM_DIR.match(p))


def chapter_key(rel: str, doc: str = "") -> tuple[str, int]:
    """Which chapter a page belongs to, and where it sorts.

    `doc` is the source document the page came from (see source_document). Three shapes appear
    across the corpus and all three have to work: a lecture-numbered course
    (`lectures/07-slides.pdf`), a unit-based one (`units/unit5-programming/…`), and a plain
    document split into sections. Keying on the document rather than the page is what makes the
    third work without breaking the first -- `07-slides.pdf` and `07-captions.srt` are two formats
    of one lecture and still merge, because the number is read off the DOCUMENT's stem."""
    role = role_of(rel)
    unit = UNIT.search(doc or rel)
    if unit:
        return re.sub(r"\s+", "", unit.group(1).lower()), 0
    if doc:
        stem = TERM_IN_STEM.sub("", Path(doc).stem).strip("-_").lower()
    else:
        parts = [p for p in rel.split("/") if not TERM_DIR.match(p)]
        stem = Path(parts[-1]).stem.lower() if parts else rel
    m = LECTURE_NO.search("/" + stem)
    if m and role in ("slides", "transcript", "exercises", "solutions"):
        # Practice numbered like a lecture belongs WITH that lecture: recitation 7 is the
        # exercises for chapter 7, not a chapter between 7 and 8.
        return f"lecture{int(m.group(1)):02d}", int(m.group(1))
    if role in ("exercises", "solutions"):
        # Unnumbered practice -- OCW's worked examples are named by topic -- gathers into one
        # closing chapter rather than 43 pages of its own.
        return "practice", 999
    return (stem or "book"), 0


def is_written(course: Path) -> bool:
    """Whether this course's book has already been written. One definition, shared with the nav
    and the landing page, which ask the same question."""
    import normalise_source as ns
    return ns.is_written(course)


def is_book(chapters: list) -> bool:
    """Whether a course has enough teaching material to be a book at all.

    Measured over the chapters that are not the course's own front matter, because a 16k-char
    syllabus is not 16k of a subject being taught."""
    return sum(c.chars() for c in chapters
               if not ADMIN_CHAPTER.match(c.key)) >= BOOK_FLOOR


def course_root(slug_dir: Path) -> list:
    return [p for p in slug_dir.rglob("*.md") if p.name != "index.md"]


def _split_long_document(ch: Chapter, docs: dict) -> list:
    """One chapter per section, for a document that is a book rather than a lecture.

    A thesis and a set of full lecture notes arrive as ONE source document, so they group into one
    chapter -- Gorin's thesis at 240k chars against a 220k input cap, its last sections dropped in
    silence. Where the converter has already split such a document into numbered section pages
    that match its real chapters, those are the book's chapters.

    Only a SINGLE-document chapter is split. A lecture chapter is legitimately large because it
    merges a deck, a transcript and several years of the same lecture, and splitting that by page
    would undo the merge that is the whole point of a book."""
    pages = ch.inputs + ch.exercises
    if len(pages) < 2 or len({docs.get(p, "") for p in pages}) != 1:
        return [ch]
    # Split by SECTION, not by page. stat243 carries the same project paper in four years, so
    # four copies of `01-abstract.md` reach here; keyed by path they became four chapters called
    # "Abstract", which is the year duplication the merge exists to remove, one level down.
    parts: dict = {}
    for page in pages:
        stem = TERM_IN_STEM.sub("", page.stem).strip("-_").lower()
        part = parts.setdefault(stem, Chapter(key=f"{ch.key}-{stem}", number=0))
        getattr(part, role_of(page.as_posix())).append(page)
    # Sections carry a zero-padded index from the converter, so the key sorts them into the
    # document's own order; number 0 keeps the whole run together, after the numbered lectures.
    return list(parts.values())


def plan_course(course_dir: Path) -> list:
    """Group a course's converted pages into chapters."""
    buckets: dict[str, Chapter] = {}
    docs: dict[Path, str] = {}
    for page in sorted(course_root(course_dir)):
        rel = page.relative_to(course_dir).as_posix()
        docs[page] = doc = source_document(page)
        key, order = chapter_key(rel, doc)
        ch = buckets.setdefault(key, Chapter(key=key, number=order))
        ch.number = ch.number or order
        getattr(ch, role_of(rel)).append(page)

    chapters = []
    for c in buckets.values():
        if not c.inputs:
            continue
        chapters += (_split_long_document(c, docs) if c.chars() > CHAPTER_BUDGET else [c])
    # a course's own order: lecture number where it has one, then alphabetically by key
    chapters.sort(key=lambda c: (c.number or 999, c.key))
    for i, c in enumerate(chapters, 1):
        c.number = i
        if not c.title:
            c.title = strip_page(c.inputs[0])[0] if c.inputs else c.key
    return chapters


PROMPT = """You are writing one chapter of a set of lecture notes for the course below.

You are given the raw converted material for this chapter: some combination of slide text, a
transcript of what the lecturer said, and written notes. Your job is to turn it into a chapter a
student can actually learn from.

COURSE: {course}
CHAPTER {number}: {title}

Rules:
- Write lecture notes, not a summary and not a transcript. Full prose that teaches the material.
- The slides give the skeleton and the equations; the transcript gives the motivation and the
  reasoning that the slides leave out. Merge them. Where the same topic appears more than once
  (a course taught in several years), take the clearest treatment rather than repeating it.
- NEVER invent material. If the source does not cover something, leave it out. Do not add examples,
  results or history that are not in the material you were given.
- Start at heading level 2 (`##`). Do NOT write a level-1 `#` heading, and do not repeat the
  chapter title.
- Open with `## What this covers` -- two or three sentences saying what question the chapter
  answers and what it assumes.
- Then the exposition, in `##` sections. Define terms properly. State results with the argument
  that makes them plausible. Keep the worked examples from the lecture.
- Mathematics in LaTeX: `$...$` inline, `$$...$$` on its own lines. Never `\\(` or `\\[`.
- No raw HTML. No `<br>`, `<span>`, `<sup>`. The ONE exception is a diagram, below.
- NEVER draw with ASCII or box-drawing characters. A picture made of `┌─┐` and `╲` in a code
  fence is not a diagram; it is an apology for one.
- Where the lecture showed a picture that genuinely carries the argument -- a region of a sample
  space, a tree of outcomes, a distribution being shaded, a process moving between states -- draw
  it as an inline SVG figure:

  <figure>
  <svg viewBox="0 0 320 220" role="img" aria-label="one sentence saying what the picture shows">
    <line x1="40" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1.5"/>
    <text x="170" y="205" text-anchor="middle" font-size="12" fill="currentColor">x</text>
  </svg>
  <figcaption>What the picture shows.</figcaption>
  </figure>

  Rules for it, which are not optional:
  * Strokes, text and arrowheads use `fill="currentColor"` / `stroke="currentColor"` so the figure
    is legible in BOTH the light and dark themes. Baked-in black or white is invisible in one of
    them. At most one literal colour, for the single element carrying the meaning, and it must read
    on a white and a dark ground alike.
  * Size with `viewBox`; no `width`/`height` attributes.
  * Shade a region with `fill="currentColor" fill-opacity="0.15"`, never with a solid fill.
  * Text 11-13px, short labels. Explanation goes in the `<figcaption>`, not inside the drawing.
  * Arrowheads as a `<defs><marker>` or a small `<polygon>`; never an image.
  * No `<script>`, `<style>` or `<foreignObject>`. Nothing loaded from outside the figure.
  * Draw the mechanism the argument turns on, and leave out what it does not. If a sentence says
    it faster, write the sentence and no figure.
- Remove lecture boilerplate: donation notices, "the following content is provided under a Creative
  Commons license", administrative announcements, "see you Thursday".
{exercises}
- End with `## Sources`, a short bullet list saying exactly which supplied material each part came
  from, and naming anything the lecture referred to but did not contain.

Begin your answer with a single line:

TITLE: <a short topic title for this chapter, five words or fewer>

The title names what the chapter is ABOUT. `Probability Models and Axioms`, not `Lecture 1`, not a
filename, not a video id. Then write the chapter, starting with `## What this covers`.

---- MATERIAL ----

{material}"""

EXERCISES_RULE = """- After the exposition, add `## Exercises` containing the problems supplied
  below, rewritten cleanly but NOT solved. Do not include solutions."""


TITLE_LINE = re.compile(r"\A\s*TITLE:\s*(.+?)\s*$", re.M)


def split_title(text: str, fallback: str) -> tuple[str, str]:
    """Pull the model's `TITLE:` line off the front of a chapter.

    Chapter titles came from the first input file's own title, which gave a book with chapters
    called `LECTURE 1`, `08 captions` and `12 slides lec 12 bonvid`. A book's contents page has to
    name topics; only something that has read the chapter can supply that."""
    m = TITLE_LINE.match(text)
    if not m:
        return fallback, text.strip()
    title = re.sub(r"^[\d.\s]+", "", m.group(1)).strip(" *#`")
    return (title or fallback), text[m.end():].strip()


def build_material(ch: Chapter) -> str:
    out, budget = [], MAX_INPUT_CHARS
    for label, pages in (("SLIDES", ch.slides), ("TRANSCRIPT", ch.transcript),
                         ("NOTES", ch.notes), ("PROBLEMS", ch.exercises)):
        for page in pages:
            if budget <= 0:
                break
            title, body = strip_page(page)
            if not body.strip():
                continue
            chunk = f"\n=== {label}: {title} ===\n{body}\n"
            out.append(chunk[:budget])
            budget -= len(chunk)
    return "".join(out)


def chapter_key_hash(course: str, ch: Chapter, material: str) -> str:
    h = hashlib.sha256()
    h.update(course.encode())
    h.update(str(ch.number).encode())
    h.update(material.encode())
    h.update(PROMPT.encode())
    return h.hexdigest()[:32]


def courses() -> list:
    """Every course directory: docs/<discipline>/<provider>/<course>.

    Defined by DEPTH, not by the presence of an index.md. Every split document has an index.md of
    its own, so keying on that made `psls20/theory/01-intro` look like a course in its own right --
    and a course made of one section of one chapter is not a book."""
    out = []
    for discipline in sorted(p for p in DOCS.iterdir() if p.is_dir()):
        if discipline.name in {"javascripts"}:
            continue
        for provider in sorted(p for p in discipline.iterdir() if p.is_dir()):
            for course in sorted(p for p in provider.iterdir() if p.is_dir()):
                out.append(course)
    return out


def cmd_plan(a):
    total_ch = total_chars = 0
    for course in courses():
        if a.course and a.course not in str(course):
            continue
        chapters = plan_course(course)
        if not chapters:
            continue
        if not is_book(chapters):
            print(f"{course.relative_to(DOCS)}: not a book — "
                  f"{sum(c.chars() for c in chapters)/1000:.0f}k chars, "
                  f"{', '.join(c.key for c in chapters[:4])}")
            continue
        chars = sum(c.chars() for c in chapters)
        total_ch += len(chapters); total_chars += chars
        print(f"{course.relative_to(DOCS)}: {len(chapters)} chapters, {chars/1000:.0f}k chars")
        if a.verbose:
            for c in chapters[:a.verbose]:
                print(f"    {c.number:2}. {c.title[:44]:46} "
                      f"slides={len(c.slides)} transcript={len(c.transcript)} "
                      f"notes={len(c.notes)} ex={len(c.exercises)}")
    inp = total_chars / 4
    out = total_ch * 3000
    print(f"\n{total_ch} chapters, {total_chars/1e6:.1f}M chars in")
    print(f"estimate: ${inp/1e6*0.75 + out/1e6*3.75:.2f} standard, "
          f"${(inp/1e6*0.75 + out/1e6*3.75)/2:.2f} batched")


def cmd_tasks(a):
    """Emit the work list as JSON, one row per chapter still to write.

    This is the hand-off to subagents. Each row carries everything an agent needs -- the input
    files to read, where to write the result, and the key that ties it back to the cache -- so the
    orchestrator never has to recompute a plan or pass material through its own context. The
    material stays on disk and only a filename crosses the boundary."""
    rows = []
    # A course whose book is already written has had its artefacts deleted and replaced by the
    # chapters, so plan_course() now reads the BOOK and proposes rewriting it from its own
    # output -- a chapter written from a chapter, with the source material gone. That is asked
    # of the tree rather than of the manifest: the manifest is a file that can be absent, and
    # when it was, this guard silently passed and the work list offered 44 tasks that would have
    # rewritten two finished books from their own chapters. A written chapter, by contrast,
    # always says so in its front matter.
    for course in courses():
        name = course.relative_to(DOCS).as_posix()
        if a.course and a.course not in name:
            continue
        if is_written(course):
            continue
        chapters = plan_course(course)
        if not is_book(chapters):
            continue
        for ch in chapters:
            material = build_material(ch)
            if len(material) < 800:
                continue
            key = chapter_key_hash(name, ch, material)
            if (CACHE / f"{key}.json").exists():
                continue
            rows.append({
                "key": key, "course": name, "number": ch.number, "title": ch.title,
                "out": str(CACHE / f"{key}.json"),
                "chars": len(material),
                "slides": [str(p) for p in ch.slides],
                "transcript": [str(p) for p in ch.transcript],
                "notes": [str(p) for p in ch.notes],
                "exercises": [str(p) for p in ch.exercises],
            })
    rows.sort(key=lambda r: (r["course"], r["number"]))
    out = LIBRARY / "conversion-cache" / "book-tasks.json"
    out.write_text(json.dumps(rows, indent=1))
    by_course = {}
    for r in rows:
        by_course[r["course"]] = by_course.get(r["course"], 0) + 1
    for c, n in sorted(by_course.items()):
        print(f"  {n:4} chapters  {c}")
    print(f"\n{len(rows)} chapters to write, {sum(r['chars'] for r in rows)/1e6:.1f}M chars")
    print(f"written to {out}")
    return 0


def cmd_submit(a):
    from google import genai
    from google.genai import types
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        print("GEMINI_API_KEY is not set", file=sys.stderr)
        return 2
    client = genai.Client(api_key=key)
    JOBS.mkdir(parents=True, exist_ok=True)
    done = {p.stem for p in CACHE.glob("*.json")}
    queued = set()
    for man in JOBS.glob("*.json"):
        for row in json.loads(man.read_text()).get("index", []):
            queued.add(row["key"])

    requests, index, sizes = [], [], []
    for course in courses():
        if a.course and a.course not in str(course):
            continue
        name = course.relative_to(DOCS).as_posix()
        for ch in plan_course(course):
            material = build_material(ch)
            if len(material) < 800:
                continue
            k = chapter_key_hash(name, ch, material)
            if k in done or k in queued:
                continue
            prompt = PROMPT.format(
                course=name, number=ch.number, title=ch.title, material=material,
                exercises=EXERCISES_RULE if ch.exercises else "")
            parts = [types.Part.from_text(text=prompt)]
            requests.append({"contents": [types.Content(role="user", parts=parts).model_dump(
                exclude_none=True)], "config": {"thinking_config": {"thinking_level": "low"}}})
            sizes.append(len(prompt))
            index.append({"key": k, "course": name, "number": ch.number, "title": ch.title,
                          "solutions": [str(p) for p in ch.solutions]})
    if not requests:
        print("nothing to write: every chapter is cached or already queued")
        return 0

    if a.sync:
        # Straight to the model, at twice the batched price, for when a finished book is wanted
        # now rather than within 24 hours. Threaded because each chapter is an independent call
        # and the wall clock is otherwise dominated by waiting on the network.
        from concurrent.futures import ThreadPoolExecutor
        cfg = types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_level="low"))

        def one(pair):
            i, req = pair
            meta = index[i]
            text = req["contents"][0]["parts"][-1]["text"]
            for attempt in range(4):
                try:
                    r = client.models.generate_content(model=a.model, contents=text, config=cfg)
                    out = llm_pdf.FENCE_WRAPPED.sub(r"\1", (r.text or "").strip()).strip()
                    if not out:
                        raise RuntimeError("empty")
                    title, out = split_title(out, meta["title"])
                    (CACHE / f"{meta['key']}.json").write_text(
                        json.dumps({**meta, "title": title, "markdown": out}, indent=1))
                    return True
                except Exception as exc:
                    if attempt == 3:
                        print(f"  failed: {meta['course']} ch{meta['number']} "
                              f"({type(exc).__name__})")
                        return False
                    import time as _t
                    _t.sleep(2 ** attempt * 3)
            return False

        CACHE.mkdir(parents=True, exist_ok=True)
        with ThreadPoolExecutor(max_workers=4) as pool:
            ok = sum(1 for r in pool.map(one, list(enumerate(requests))) if r)
        print(f"wrote {ok}/{len(requests)} chapters")
        return 0

    submitted, start = [], 0
    while start < len(requests):
        end, size = start, 0
        while end < len(requests) and end - start < REQUESTS_PER_JOB:
            if end > start and size + sizes[end] > MAX_JOB_BYTES:
                break
            size += sizes[end]; end += 1
        job = client.batches.create(model=a.model, src=requests[start:end],
                                    config={"display_name": f"book-{start:05d}"})
        submitted.append({"job": job.name, "first": start, "count": end - start})
        print(f"  queued {job.name} ({end - start} chapters)")
        start = end

    import time
    stamp = time.strftime("%Y%m%dT%H%M%S")
    (JOBS / f"{stamp}.json").write_text(json.dumps(
        {"model": a.model, "submitted": submitted, "index": index}, indent=1))
    print(f"\n{len(requests)} chapters queued; collect when they land")
    return 0


def _get_job(client, name, attempts=5):
    """Fetch a job, riding out transient server errors.

    A single 503 used to abort the whole collect, losing the results of every job already walked.
    The service was returning them intermittently on the day 545 of 920 requests also came back
    "Internal error encountered" -- so resilience here is not hypothetical."""
    import time
    for attempt in range(attempts):
        try:
            return client.batches.get(name=name)
        except Exception as exc:
            transient = any(s in str(exc) for s in ("503", "UNAVAILABLE", "500", "Internal"))
            if not transient or attempt == attempts - 1:
                raise
            time.sleep(2 ** attempt * 3)
    return None


def cmd_status(a):
    from google import genai
    import collections
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    states = collections.Counter()
    for man in sorted(JOBS.glob("*.json")):
        for e in json.loads(man.read_text())["submitted"]:
            try:
                j = _get_job(client, e["job"])
                st = j.state.name if hasattr(j.state, "name") else str(j.state)
            except Exception:
                st = "ERR"
            states[st] += 1
    for s, n in states.most_common():
        print(f"  {s:30} {n} jobs")
    return 0


def cmd_collect(a):
    from google import genai
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    CACHE.mkdir(parents=True, exist_ok=True)
    written = pending = 0
    failed = {}
    for man in sorted(JOBS.glob("*.json")):
        blob = json.loads(man.read_text())
        index = blob["index"]
        for e in blob["submitted"]:
            j = _get_job(client, e["job"])
            st = j.state.name if hasattr(j.state, "name") else str(j.state)
            if "SUCCEEDED" not in st:
                pending += e["count"]
                continue
            for offset, resp in enumerate(getattr(j.dest, "inlined_responses", None) or []):
                meta = index[e["first"] + offset]
                err = getattr(resp, "error", None)
                if err:
                    msg = str(getattr(err, "message", err))
                    failed[msg] = failed.get(msg, 0) + 1
                    continue
                try:
                    text = (resp.response.candidates[0].content.parts[0].text or "").strip()
                except Exception:
                    text = ""
                text = llm_pdf.FENCE_WRAPPED.sub(r"\1", text).strip()
                if not text:
                    continue
                title, text = split_title(text, meta["title"])
                (CACHE / f"{meta['key']}.json").write_text(json.dumps(
                    {**meta, "title": title, "markdown": text}, indent=1))
                written += 1
    print(f"wrote {written} chapters to the cache; {pending} still pending")
    for why, n in sorted(failed.items(), key=lambda kv: -kv[1]):
        print(f"  {n:5d}  {why}")
    return 0


BOOK_BANNER = ("> **Lecture notes.** Written from the material of [{course}]({url}), "
               "licensed {licence}. These are notes, not a transcript: the material has "
               "been reorganised and rewritten. This adaptation carries the same licence, and the "
               "original is linked above.")


def _slug(text, limit=60):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return (s[:limit].rstrip("-") or "chapter")


TERM = re.compile(r"(fall|spring|summer|winter)-(\d{4})", re.I)


def _course_provenance(course_name: str) -> dict:
    """Title, citation, licence and the course offerings a book was written from.

    Read from the LOCKFILE, never from a surviving page. `write` deletes the artefacts, so the only
    `source:` left in the tree afterwards is the one this function wrote, and reading it back
    would launder a wrong citation through every re-emit -- which is how Stat 156 came to cite
    one homework PDF. The tree says which books exist (`is_written`); the lockfile says where they
    came from."""
    import normalise_source as ns
    parts = tuple(course_name.split("/"))
    entries = []
    for e in ns.load_lock(LIBRARY / "sources").get("sources", []):
        dest, ok, _ = ns.destination(e, LIBRARY)
        if ok and Path(dest).relative_to(DOCS).parts[:3] == parts:
            entries.append(e)
    if not entries:
        raise SystemExit(f"{course_name}: no publishable lockfile source -- refusing to write a "
                         "book that cannot cite its original")
    # Chronological, not by slug: `stat243-fall-2021` sorts after `fall-2026` alphabetically.
    def when(e):
        m = TERM.search(e["slug"])
        season = ["winter", "spring", "summer", "fall"].index(m.group(1).lower()) if m else 0
        return (int(m.group(2)) if m else 0, season, e["slug"])
    entries.sort(key=when)
    head = entries[0]["slug"].partition("/")[0]
    # The book is the course, so the year belongs in `years`, not in the title.
    title = (entries[0].get("title") if len(entries) == 1 else None) \
        or ns.source_title({"slug": head})
    homes = [ns.course_home(e) for e in entries]
    owners = {re.match(r"https://github\.com/[^/]+", h).group(0)
              for h in homes if h.startswith("https://github.com/")}
    url = homes[0] if len(entries) == 1 else (owners.pop() if len(owners) == 1 else homes[0])
    licences = [e.get("licence", "unresolved") for e in entries]
    licence = ns.book_licence(licences)
    if len(set(licences)) > 1:
        print(f"  {course_name}: licences differ across years, the book carries {licence}: "
              + ", ".join(f"{e['slug']}={e.get('licence')}" for e in entries))
    offerings = []
    for e, home in zip(entries, homes):
        m = TERM.search(e["slug"].partition("/")[2])
        offerings.append({"term": f"{m.group(1).capitalize()} {m.group(2)}" if m
                          else ns.source_title(e),
                          "home": home, "commit": str(e.get("commit") or "")[:7],
                          "licence": e.get("licence", "unresolved")})
    return {"title": title, "url": url, "licence": licence, "offerings": offerings}


def _written_on(page: Path) -> str:
    """The date a page was first written, kept across re-emits; today for a new page.

    Re-emitting a book to fix its citation does not rewrite its chapters, and stamping all of
    them with today's date would say it did."""
    if page.exists():
        m = re.search(r"^written: ['\"]?([\d-]+)", page.read_text(encoding="utf-8")[:600], re.M)
        if m:
            return m.group(1)
    return TODAY


def _published_solution(page: Path) -> str:
    """The body of a solutions page this command wrote on an earlier run.

    A re-emitted book's solution sources are artefacts that the first write deleted, so the
    published page is the only copy left. Without this a re-emit dropped every solutions page --
    all 14 of 6.041SC's."""
    if not page.exists():
        return ""
    text = page.read_text(encoding="utf-8")
    body = text.split("\n# ", 1)[1].split("\n", 1)[1] if "\n# " in text else ""
    return body.rsplit("\n---\n\n[← back to chapter", 1)[0].strip()


def cmd_write(a):
    """Write the books and remove the artefact layer they replace."""
    # Plan-driven, not cache-driven. The cache accumulates every chapter ever generated, including
    # ones whose inputs have since been removed -- dropping 13 duplicate transcript PDFs left their
    # chapters behind, and a cache-driven write put them back into the book.
    cached = {}
    for course in courses():
        name = course.relative_to(DOCS).as_posix()
        if a.course and a.course not in name:
            continue
        chapters_planned = plan_course(course)
        if not is_book(chapters_planned):
            continue
        for ch in chapters_planned:
            material = build_material(ch)
            if len(material) < 800:
                continue
            f = CACHE / f"{chapter_key_hash(name, ch, material)}.json"
            if f.exists():
                cached.setdefault(name, []).append(json.loads(f.read_text()))

    # Writing a book deletes the artefacts it was built from, so a second `write` finds nothing to
    # plan and would silently do nothing -- or worse, rebuild the book out of its own chapters.
    # The manifest records which cached chapters a course's book is made of, so the step is
    # idempotent and a book can be re-emitted (after a template change, say) without re-paying.
    for man in MANIFESTS.glob("*.json"):
        blob = json.loads(man.read_text())
        name = blob["course"]
        if a.course and a.course not in name:
            continue
        if name in cached:
            continue
        chapters = [json.loads((CACHE / f"{k}.json").read_text())
                    for k in blob["keys"] if (CACHE / f"{k}.json").exists()]
        if chapters:
            cached[name] = chapters

    if not cached:
        print("no chapters for these courses yet — run submit, then collect")
        return 1

    for course_name, chapters in sorted(cached.items()):
        course = DOCS / course_name
        if a.course and a.course not in course_name:
            continue
        chapters.sort(key=lambda c: c["number"])
        # Each chapter is titled by the agent that wrote it, which cannot see its neighbours. A
        # course that spends three lectures on one topic therefore yields three chapters called
        # "Local Excitation, Global Inhibition" -- correct, honest, and useless on a contents
        # page. A run like that really is parts of one treatment, so number them as such.
        seen = collections.Counter(c["title"] for c in chapters)
        run = collections.Counter()
        for ch in chapters:
            if seen[ch["title"]] > 1:
                run[ch["title"]] += 1
                ch["title"] = f"{ch['title']} (part {run[ch['title']]})"
        prov = _course_provenance(course_name)
        url, licence, title = prov["url"], prov["licence"], prov["title"]
        index_written = _written_on(course / "index.md")   # read before the course is cleared

        # solutions are carried over as an appendix, not left as loose artefacts
        solutions = {}
        for ch in chapters:
            for src in ch.get("solutions", []):
                src = Path(src)
                if src.exists():
                    solutions.setdefault(ch["number"], []).append(strip_page(src))
            if ch.get("solutions") and ch["number"] not in solutions:
                kept = _published_solution(
                    course / "solutions" / f"{ch['number']:02d}-{_slug(ch['title'])}.md")
                if kept:
                    solutions[ch["number"]] = [("", kept)]

        pages = []
        for i, ch in enumerate(chapters):
            name = f"{ch['number']:02d}-{_slug(ch['title'])}.md"
            # Money, not mathematics: a chapter's price table (`$500,000`) leaves an
            # unmatched `$` that opens a maths span and swallows the rest of the page.
            # The converter has always repaired this for converted pages; a written
            # chapter has to go through the same repair, not just the SVG tidy.
            #
            # SVG is lifted out first, exactly as normalise_body() does it. A figure's `$1`
            # price label is neither money to escape nor maths to leave alone -- it is a
            # drawing's text, and escaping it there put a stray `\$` inside the diagram and
            # broke the very page this repair was added to fix.
            body, _svg = _protect_svg(tidy_svg(ch["markdown"].strip()))
            # fix_escaped_closer runs AFTER the escaper, not before: the damage it repairs is the
            # escaper's own. One stray dollar earlier in the page shifts every pairing, so a
            # legitimate closer is left over and escaped -- `$\chi^2\$` -- which then swallows
            # the page the escaper was protecting.
            _code_body, _code = protect_code(body)
            _code_body = fix_escaped_closer(_fix_stray_dollars(_code_body))
            body = _restore_svg(restore_code(_code_body, _code), _svg)
            if solutions.get(ch["number"]):
                body += (f"\n\nSolutions: [chapter {ch['number']}]"
                         f"(solutions/{name})\n")
            # `chapter:` must stay inside the first 400 bytes: is_written() reads only that far.
            front = {"title": f"{ch['number']}. {ch['title']}", "course": title,
                     "chapter": ch["number"], "source": url, "licence": licence,
                     "written": _written_on(course / name)}
            fm = "---\n" + "\n".join(f"{k}: {json.dumps(v) if isinstance(v, str) else v}"
                                     for k, v in front.items()) + "\n---\n"
            banner = BOOK_BANNER.format(course=title, url=url, licence=licence)
            nav = []
            if i:
                prev = chapters[i - 1]
                nav.append(f"[← {prev['number']}. {prev['title']}]"
                           f"({prev['number']:02d}-{_slug(prev['title'])}.md)")
            nav.append("[Contents](index.md)")
            if i + 1 < len(chapters):
                nxt = chapters[i + 1]
                nav.append(f"[{nxt['number']}. {nxt['title']} →]"
                           f"({nxt['number']:02d}-{_slug(nxt['title'])}.md)")
            page = (f"{fm}\n{banner}\n\n# {ch['number']}. {ch['title']}\n\n{body}\n\n"
                    f"---\n\n{' · '.join(nav)}\n")
            pages.append((name, page, ch))

        if a.apply:
            # The artefacts are what the book replaces. Removing them is the point: keeping both
            # would leave the hoard in place with a book on top of it.
            for child in list(course.iterdir()):
                shutil.rmtree(child) if child.is_dir() else child.unlink()
            course.mkdir(parents=True, exist_ok=True)
            for name, page, ch in pages:
                (course / name).write_text(page, encoding="utf-8")
                if solutions.get(ch["number"]):
                    sol_dir = course / "solutions"
                    sol_dir.mkdir(exist_ok=True)
                    parts = "\n\n".join(b for _, b in solutions[ch["number"]])
                    ch_title = ch["title"]
                    (sol_dir / name).write_text(
                        "---\n"
                        + f'title: "Solutions — {ch_title}"\n'
                        # Without `source:` every solutions page failed the fatal `uncited`
                        # gate -- 14 of 6.041SC's 41 pages -- and a page that cannot cite its
                        # original is exactly what that gate exists to stop.
                        + f"source: {url}\n"
                        + f"licence: {licence}\n---\n\n"
                        + "> **Worked solutions.** From the course's own solution sets, "
                        + f"licensed {licence}.\n\n"
                        + f"# Solutions — {ch_title}\n\n{parts}\n\n"
                        + f"---\n\n[← back to chapter {ch['number']}](../{name})\n",
                        encoding="utf-8")
            contents = "\n".join(
                f"{ch['number']}. [{ch['title']}]({name})" for name, _, ch in pages)
            offs = prov["offerings"]
            # The artefact layer is gone, so this table is the only route back to the originals.
            # `source:` above stays a scalar: the validator skips list lines, and a list there
            # would read as uncited.
            rows = "\n".join(
                f"| {o['term']} | [{o['home'].split('://', 1)[1]}]({o['home']}) | "
                f"{('`' + o['commit'] + '`') if o['commit'] else '—'} | {o['licence']} |"
                for o in offs)
            merged = (f"{len(offs)} course offerings were merged. " if len(offs) > 1 else "")
            carries = (f"The book carries {licence}, the most restrictive licence among them."
                       if len({o['licence'] for o in offs}) > 1
                       else f"The book carries {licence}.")
            years = ", ".join(o["term"] for o in offs)
            (course / "index.md").write_text(
                f'---\ntitle: "{title}"\nsource: {url}\nlicence: {licence}\n'
                + (f'years: "{years}"\n' if TERM.search(years.replace(" ", "-")) else "")
                + f"written: '{index_written}'\n---\n\n"
                f"> **Lecture notes.** Written from the material of [{title}]({url}), licensed "
                f"{licence}. Notes, not a transcript — reorganised and rewritten, carrying the "
                f"same licence.\n\n# {title}\n\n{len(pages)} chapters, written from the "
                f"course's material.\n\n## Contents\n\n{contents}\n\n"
                f"## Sources\n\n{merged}{carries}\n\n"
                f"| Offering | Original | Commit | Licence |\n| --- | --- | --- | --- |\n{rows}\n",
                encoding="utf-8")
        if a.apply:
            MANIFESTS.mkdir(parents=True, exist_ok=True)
            (MANIFESTS / f"{course_name.replace('/', '__')}.json").write_text(json.dumps(
                {"course": course_name, "keys": [c["key"] for c in chapters]}, indent=1))
        print(f"{course_name}: {len(pages)} chapters"
              + ("" if a.apply else "  (dry run)"))

    if a.apply:
        # The nav is generated from the tree, and the tree just changed out from under it. Without
        # this every deleted artefact stays in SUMMARY.md and the strict build fails on all of
        # them -- 472 warnings the first time.
        import normalise_source as ns
        # Solutions carry over from converted pages and can reference figures that did not come
        # with them. Same repair as the converter uses: a link whose target is not published
        # becomes plain text rather than a dangling reference the strict build rejects.
        fixed, on_pages = ns.repair_dangling_links(DOCS, True)
        if fixed:
            print(f"stripped {fixed} links on {on_pages} pages with no published target")
        ns.write_library_index(DOCS, True)
        n = ns.write_nav(DOCS, True)
        print(f"nav rebuilt: {n} entries")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["plan", "tasks", "submit", "status", "collect", "write"])
    ap.add_argument("--apply", action="store_true", help="write the books and delete the artefacts")
    ap.add_argument("--sync", action="store_true", help="call the model directly instead of batching: twice the price, no wait")
    ap.add_argument("course", nargs="?", default="")
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--verbose", type=int, default=0, help="show the first N chapters per course")
    a = ap.parse_args()
    return {"plan": cmd_plan, "tasks": cmd_tasks, "submit": cmd_submit, "status": cmd_status,
            "collect": cmd_collect, "write": cmd_write}[a.command](a) or 0


if __name__ == "__main__":
    raise SystemExit(main())
