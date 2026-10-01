#!/usr/bin/env python3
"""Convert a collected source into uniform markdown, split into linkable sections.

Usage:
    uv run --group convert --group dev python \
        skills/normalise-materials/scripts/normalise_source.py <slug> [more ...] [--apply]
    ... --all            every source in the lockfile
    ... --include-all    do not skip course administrivia
    ... --summary-only   regenerate SUMMARY.md and index.md, convert nothing

`sources/<slug>` in, `docs/<slug>/` out, both in this repository. The study knowledge base next
door holds notes and links here; nearly ten thousand converted pages would have buried seventy of
his own, which is why these are two repositories.

A course arrives as a pile of formats and none of it can be *linked to*. This produces one
markdown file per logical section, so a topic file can cite the NPMLE derivation rather than
"somewhere in lecture 7", and so the whole corpus is greppable regardless of what it started as.

It preserves; it does not rewrite. Changing the prose is `adapt-material`'s job.

Four rules it exists to enforce, each of which cost someone time to learn:

  * **Convert the source, not the render.** A `.qmd` keeps the author's LaTeX; the PDF built
    from the same file turns $\\lambda(t) = f(t)/S(t)$ into `Sf((tt))becauseTiscontinuous`. Where
    both exist the render is dropped. PDFs are converted only when nothing better is there, and
    the result is stamped as lossy.
  * **Two categories are never converted**, rather than converted somewhere private: a book, and
    a paper without `open_access`. `material:` in the lockfile says which is which, is written by
    hand, and is never detected — a source without it is skipped and named, because guessing it
    guesses in the publishing direction. So is a source with no URL to cite.
  * **Every published page cites its source and links to the original.** Generated, not left to
    an author to remember, because the whole republishing arrangement rests on it.
  * **Nothing links into the void.** Relative links in the source are rewritten — to the
    converted sibling where there is one, to the upstream original otherwise, and to plain text
    where there is no upstream. The site builds `--strict`, so a broken link fails CI.

Dry run by default: without --apply it reports the plan and writes nothing.
"""

import argparse
import json
import os
import re
import shutil
import sys
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pyyaml missing — run with `uv run --group dev python …`")

sys.path.insert(0, str(Path(__file__).resolve().parent))
import llm_pdf
import validate_pages
from body_rules import (normalise_body, normalise_title, pre_tex, protect_math_spans,
                        restore_math)

LIBRARY = Path(__file__).resolve().parents[3]   # skills/<name>/scripts/x.py -> repo root
TODAY = date.today().isoformat()

# ---------------------------------------------------------------------------
# What to publish
#
# AGENTS.md "What may be republished" decides by kind of source, not by licence. `material:` in
# sources.lock.yml carries that kind; it is distinct from `kind:` there, which is git-vs-files
# and is about restoring the download.
# ---------------------------------------------------------------------------
# Two categories are never converted at all, which is the whole of the policy. Everything else
# public is converted and published, cited and linked to its original.
NEVER = {"book"}                           # however obtained, whatever its licence
NOT_MATERIAL = {"archive", "data", "scaffolding"}
NEEDS_OPEN_ACCESS = {"paper"}              # assume paywalled unless the lockfile asserts otherwise

# A licence that permits a DERIVATIVE WORK, which is what a book here is. This is a stricter
# question than redistribution, and the reason it is an allow-list rather than a deny-list is the
# asymmetry the whole file turns on: a skipped source costs one lockfile edit, a wrongly published
# derivative of someone's dissertation cannot be recalled. The knowledge base's AGENTS.md already
# states the rule for its own adaptations -- "unclear -> never published, and say the licence is
# unresolved" -- and this is the same rule, enforced here rather than trusted to a reader.
#
# Deliberately NOT on this list:
#   * `unresolved` -- means *not found*, which is not *not licensed*. Resolve it, then publish.
#   * BSD / MIT / Apache -- software licences. On a course repository one of these almost always
#     covers the scripts, not the notes, and AGENTS.md records the trap: a `*.github.io` repo's
#     MIT licence is the Jekyll theme's. Where a repo genuinely licenses its CONTENT this way,
#     record the content licence explicitly and it passes.
MAY_ADAPT = {
    "CC0-1.0", "CC0 1.0", "public domain", "public-domain",
    "CC BY 4.0", "CC-BY-4.0", "CC BY-SA 4.0", "CC-BY-SA-4.0",
    "CC BY 3.0", "CC-BY-3.0", "CC BY-SA 3.0", "CC-BY-SA-3.0",
    "CC BY-NC 4.0", "CC-BY-NC-4.0", "CC BY-NC-SA 4.0", "CC-BY-NC-SA-4.0",
    "CC BY-NC 3.0", "CC-BY-NC-3.0", "CC BY-NC-SA 3.0", "CC-BY-NC-SA-3.0",
}


def may_adapt(licence: str) -> bool:
    """Whether this licence permits publishing a rewritten book built from the source."""
    return (licence or "").strip() in MAY_ADAPT

# docs/<subject>/<provider>/<rest of slug>/ — a library is browsed by what a thing is about, not
# by who published it, so the discipline is the top level. `subject:` is hand-written in the
# lockfile beside `material:`; the provider and the rest are mechanical, because the slug already
# encodes them. Berkeley alone is 45 of 57 sources, which is why provider cannot be the top level.
PROVIDERS = {"ocw": "mit-ocw", "berkeley": "berkeley", "statomics": "statomics",
             "gtpb": "gtpb", "pachter": "pachter-lab"}


def output_path(entry, library):
    """Where a source's converted pages go. One definition, used by the converter and the index."""
    slug = entry["slug"]
    subject = entry.get("subject") or "unsorted"
    if entry.get("material") == "paper":
        # The Papers shelf: one page per paper (its summary), with the full text beneath it where
        # the licence lets it be published.
        return library / "docs" / "papers" / subject / slug.split("/")[-1] / "full-text"
    head, _, tail = slug.partition("/")
    if entry.get("provider"):
        # Set by hand where the slug does not encode the publisher — a thesis is named for its
        # author, not for the repository it came from.
        provider, rest = entry["provider"], head
    else:
        for prefix, name in PROVIDERS.items():
            if head == prefix or head.startswith(prefix + "-"):
                provider, rest = name, head[len(prefix):].lstrip("-") or head
                break
        else:
            provider, rest = "other", head
    parts = [p for p in (rest, tail) if p]
    return library / "docs" / subject / provider / Path(*parts)

# ---------------------------------------------------------------------------
# Formats, best first. A document is whatever group of files shares a directory and a stem;
# only the best format in each group is converted, so a lecture present as .qmd, .html and .pdf
# converts once, from the .qmd.
# ---------------------------------------------------------------------------
ROUTES = {
    ".md": ("markdown", "lossless"),
    ".qmd": ("markdown", "lossless"),
    ".rmd": ("markdown", "lossless"),
    ".ipynb": ("notebook", "lossless"),
    ".tex": ("pandoc-latex", "high"),
    ".rst": ("pandoc-rst", "high"),      # Sphinx / readthedocs sources
    ".srt": ("transcript", "speech"),
    ".vtt": ("transcript", "speech"),
    ".html": ("pandoc-html", "good"),
    # JATS, the XML a journal or PubMed Central publishes an article in. Keyed on a `.jats`
    # extension rather than `.xml`, so a course's stray config or sitemap file is never
    # mistaken for an article. bioRxiv's JATS stores every formula as a GIF and loses all the
    # mathematics, so a preprint is read from its PDF instead.
    ".jats": ("pandoc-jats", "high"),
    # Not a "pdf" route any more. A PDF that survives re-routing is read by a multimodal model,
    # with pymupdf4llm kept as the cross-check rather than as the output. The deterministic route
    # produced 55% of the old corpus and almost none of it was worth reading; it is far more
    # useful as a control. See references/quality-gates.md, "The LLM route".
    ".pdf": ("llm", "reconstructed"),
}
PREFERENCE = [".qmd", ".rmd", ".md", ".rst", ".ipynb", ".tex", ".jats", ".srt", ".vtt", ".html",
              ".pdf"]

SKIP_DIRS = {
    ".git", ".github", ".quarto", "_freeze", "_site", "site_libs", "libs", "node_modules",
    "renv", "__pycache__", ".Rproj.user", "assets", "img", "images", "figures", "figure",
    # `fig` is the Quarto default, and missing it was not free: 72 plot PDFs under
    # stat153's `lectures/*/fig/` were converted as documents, and each one then grouped
    # into a lecture chapter as though it were a slide deck. A figure is not a document.
    "fig",
    "css", "js", "fonts", "data", "_extensions",
}

# Course administrivia. Real material for a study knowledge base is lectures, notes, problem
# sets and exams; how to install R on Windows is not, and several hundred such files would bury
# the material in both the nav and the search index. `--include-all` keeps them.
#
# Syllabus and index are deliberately NOT here: a syllabus is a navigational object and its
# bibliography is a source in its own right (AGENTS.md, "Papers are a source kind").
ADMIN = re.compile(
    r"(^|[-_/])("
    r"readme|license|licence|copying|code[-_]of[-_]conduct|contributing|changelog|citation|"
    r"install\w*|setup|config|requirements|environment|renv|makefile|"
    r"rubric|grading|submission|submit\w*|policy|policies|accommodation|"
    r"faq|calendar|staff|instructors|contact|announcement\w*|logistics|"
    r"access\w*|windows\w*|vscode|rstudio\w*|troubleshoot\w*|"
    r"test|scratch|sandbox|example|template|draft"
    r")([-_/.]|$)",
    re.I,
)

# Quarto/knitr chunk headers: ```{r, echo=FALSE} -> ```r. The code is material; the execution
# options are machinery.
CHUNK = re.compile(r"^(\s*```+)\{([a-zA-Z0-9_]+)[^}]*\}\s*$", re.M)
CALLOUT = re.compile(r"^:::+\s*\{?\.callout-(\w+)[^}]*\}?\s*$", re.M)
CALLOUT_END = re.compile(r"^:::+\s*$", re.M)
CALLOUT_MAP = {"note": "note", "tip": "tip", "warning": "warning",
               "important": "important", "caution": "danger"}
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
HEADING = re.compile(r"^(#{1,4})\s+(.+?)\s*#*\s*$", re.M)
REF_DEF = re.compile(r"^\[([^\]]+)\]:\s*\S+.*$", re.M)
# The label allows one level of nested brackets: `[Chapter 3 of [BZ]](BZ.pdf)` is what an
# HTML `<a>` with a citation in its text converts to, and a label pattern of `[^\]]*` skips
# it entirely -- so the link is never rewritten and dangles in the built site.
MD_LINK = re.compile(
    r"(!?)\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(\s*<?([^()>]*?)>?(\s+\"[^\"]*\")?\s*\)")
LATEX_INLINE = re.compile(r"\\\((.+?)\\\)", re.S)
LATEX_DISPLAY = re.compile(r"\\\[(.+?)\\\]", re.S)

SHORTCODE = re.compile(r"\{\{<\s*(\w+)\s+([^>]*?)\s*>\}\}")
HTML_TAG = re.compile(r"</?[a-zA-Z][^>]*>")
# A PDF's first bold line is often a form field, not a title: "Student ID (NOT your name):".
# A PDF's biggest text is not its title. On an exam paper it is the institution's letterhead, and
# on a slide deck it is often the course banner -- which is how eleven sibling pages all came to be
# called `Massachusetts Institute of Technology`. Boilerplate is rejected and the filename is used.
JUNK_TITLE = re.compile(
    r"^(student\s*id|name|signature|date|score|total|page\s*\d|do not|instructions?"
    r"|massachusetts institute|department of|university of|college of|school of"
    r"|faculty of|institute of technology|electrical engineering"
    r"|all rights reserved|copyright|creative commons|table of contents|contents"
    r"|introduction to probability|this work is licensed)\b", re.I)

# How a source's own name is written, where the slug is not good enough to show a reader.
SOURCE_TITLES = {
    "ocw": "MIT", "berkeley": "Berkeley", "statomics": "StatOmics", "gtpb": "GTPB",
    "pachter": "Pachter Lab", "caltech": "Caltech",
}
COURSE_CODE = re.compile(r"^(?:stat|math|cs|ee|ph|bio)?[-_]?(\d+[a-z]*)$", re.I)


def source_title(entry):
    """A readable name for a source.

    `title:` in the lockfile wins and is the right place to put a real course name; this is the
    fallback, and it exists because `ocw 6041sc` is a slug, not something to show a reader."""
    if entry.get("title"):
        return str(entry["title"])
    words, seen = [], set()
    for chunk in re.split(r"[/\-_]", entry["slug"]):
        if not chunk:
            continue
        low = chunk.lower()
        if low in SOURCE_TITLES:
            word = SOURCE_TITLES[low]
        elif re.fullmatch(r"\d{4}", chunk):
            word = chunk
        elif re.fullmatch(r"(fall|spring|summer|winter)", low):
            word = low.capitalize()
        elif re.match(r"^stat\d", low):
            word = "Stat " + chunk[4:].upper()
        elif re.fullmatch(r"\d{4}[a-z]{0,2}", low):
            # MIT numbers the slug flattened: 6041sc -> 6.041SC, 8591j -> 8.591J
            word = f"{chunk[0]}.{chunk[1:4]}{chunk[4:].upper()}"
        elif re.fullmatch(r"\d+[a-z]{0,3}", low):
            word = chunk.upper()
        else:
            word = chunk.capitalize()
        # `berkeley-stat243/stat243-fall-2018` repeats its own course code; say it once.
        if word.lower() in seen:
            continue
        seen.add(word.lower())
        words.append(word)
    return " ".join(words)

MIN_SECTION_CHARS = 400        # a lead-in shorter than this is a stray sentence, not an intro
MIN_PART_CHARS = 1200          # below this a part cannot stand as a page and is merged upward
MIN_PDF_CHARS_PER_PAGE = 60    # below this the PDF is a scan with no text layer


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def clean_title(raw, fallback):
    """A heading is not always a title.

    PDF extraction promotes whatever was biggest on page one, which on an exam paper is
    "**Student ID (NOT your name):**". A title that reads as a form field, or is long enough to
    be a sentence, is discarded for the filename — which is at least a real name for the thing.
    """
    t = (raw or "").strip()
    # Pandoc keeps the source's explicit anchor as an attribute block: `Foundations {#foundations}`.
    t = re.sub(r"\s*\{[^}]*\}\s*$", "", t)
    t = HTML_TAG.sub("", t)
    t = re.sub(r"[*_`]{1,3}", "", t)
    t = re.sub(r"^#+\s*", "", t)
    t = re.sub(r"\s+", " ", t).strip().rstrip(":").strip()
    if not t or len(t) > 90 or JUNK_TITLE.match(t) or not re.search(r"[A-Za-z]", t):
        return prettify(fallback)
    return t


def prettify(stem):
    """`lecture07-unbiased` -> `Lecture 07 — unbiased`: a filename is a usable title."""
    s = re.sub(r"[-_]+", " ", str(stem)).strip()
    s = re.sub(r"\b(lecture|lec|chapter|chap|unit|week|part|section|hw|ps)\s*0*(\d+)",
               lambda m: f"{m.group(1).title()} {int(m.group(2)):02d} —", s, flags=re.I)
    return (s[:1].upper() + s[1:]) if s else "Untitled"


def expand_shortcodes(text, path, root):
    """Quarto `{{< var name >}}` against the nearest `_variables.yml`; drop the rest.

    Left alone they surface as page titles like `{{< var department >}} {{< var number >}}`,
    which is the site advertising its own plumbing.
    """
    variables = {}
    d = path.parent
    while True:
        f = d / "_variables.yml"
        if f.is_file():
            try:
                variables = yaml.safe_load(read_text(f)) or {}
            except Exception:
                variables = {}
            break
        if d == root or d.parent == d:
            break
        d = d.parent

    def resolve(m):
        kind, arg = m.group(1), m.group(2).strip()
        if kind == "var":
            cur = variables
            for key in arg.split("."):
                cur = cur.get(key) if isinstance(cur, dict) else None
                if cur is None:
                    return ""
            return str(cur)
        if kind in {"meta", "env"}:
            return ""
        return ""                    # include/embed/video: the target is not converted here
    return SHORTCODE.sub(resolve, text)


def slugify(text, limit=60):
    s = re.sub(r"\$[^$]*\$", "", text)                     # drop maths from a heading slug
    s = re.sub(r"[^\w\s-]", " ", s.lower())
    s = re.sub(r"[\s_]+", "-", s.strip())
    return (s[:limit].rstrip("-") or "section")


def load_lock(sources_dir):
    lock = sources_dir / "sources.lock.yml"
    if not lock.exists():
        sys.exit(f"no lockfile at {lock} — run lock_sources.py first")
    return yaml.safe_load(lock.read_text(encoding="utf-8")) or {}


def upstream(entry, relpath, raw=False):
    """(url, exact) for one file in the original. `exact` means the URL is that file.

    A local path is only an upstream path when the download preserved the publisher's layout.
    A git clone always does. A pile of downloaded files usually does — but not when it was
    reorganised at ingest, which is exactly what happens to MIT OCW exports, whose four naming
    schemes are normalised by `organise_course.py`. Building a per-file URL from the tidied path
    produces a confident 404:

        .../6-041sc-…-fall-2013/worked-examples/normal-probability-calculation-captions.srt
        -> 301 -> .../resources/normal-probability-calculation-captions.srt -> 404

    So a files-kind source links to the course page unless the lockfile asserts
    `mirrors_upstream: true`. A citation that lands on the right page beats one that lands
    nowhere, and the whole republishing arrangement rests on the citation being good.
    """
    url, base = entry.get("url"), entry.get("base")
    if url and "github.com" in url:
        owner_repo = re.sub(r"^https?://github\.com/|\.git$", "", url).strip("/")
        commit = entry.get("commit") or entry.get("branch") or "HEAD"
        host = ("https://raw.githubusercontent.com/%s/%s/" % (owner_repo, commit) if raw
                else "https://github.com/%s/blob/%s/" % (owner_repo, commit))
        return host + relpath, True
    origin = base or url
    if not origin:
        return None, False
    if entry.get("mirrors_upstream"):
        return origin.rstrip("/") + "/" + relpath, True
    return origin.rstrip("/") + "/", False


def course_home(entry):
    """Where a book's citation lands: the course, never a file inside it.

    A book is written from a whole course, so citing one leaf of it -- the first page found on
    disk -- told a reader that Stat 156 was a homework PDF. `upstream` answers the per-file
    question; this answers the per-course one."""
    url = entry.get("url") or ""
    if "github.com" in url:
        return re.sub(r"\.git$", "", url.rstrip("/"))
    return entry.get("base") or url


def _licence_family(licence):
    """0 public domain, 1 BY, 2 BY-SA, 3 BY-NC, 4 BY-NC-SA: least to most restrictive."""
    words = licence.upper().replace("-", " ").split()
    if "CC0" in words or "PUBLIC" in words:
        return 0
    if "BY" not in words:
        raise ValueError(f"not a Creative Commons licence: {licence!r}")
    return {(False, False): 1, (False, True): 2, (True, False): 3, (True, True): 4}[
        ("NC" in words, "SA" in words)]


def book_licence(licences):
    """The licence a book written from several course years must carry.

    The book is a derivative of every year it merges, so it carries the most restrictive of their
    licences. Share-alike without NC cannot be combined with anything NC -- each forbids the
    other's terms on the derivative -- so that refuses rather than picking one."""
    found = sorted(set(licences), key=_licence_family)
    families = {_licence_family(l) for l in found}
    if 2 in families and families & {3, 4}:
        raise ValueError(f"share-alike and non-commercial cannot be combined: {found}")
    return found[-1]


def destination(entry, library):
    """(output_root, convert, reason). Never guess in the publishing direction.

    A single skip list rather than a tier system: there is no private tree, because material that
    may not be republished is simply not converted. Anything not positively known to be
    convertible is skipped and named in the report, which is the asymmetry that matters — a
    skipped source costs one lockfile edit, a wrongly published one cannot be recalled.
    """
    mat = entry.get("material")
    if mat in NOT_MATERIAL:
        return None, False, f"material: {mat} — not a document source"
    if mat is None:
        return None, False, "no `material:` in the lockfile"
    if mat in NEVER:
        return None, False, f"material: {mat} — never converted"
    if mat in NEEDS_OPEN_ACCESS and not entry.get("open_access"):
        return None, False, f"material: {mat} without `open_access` — assumed paywalled"
    if not (entry.get("url") or entry.get("base")):
        # Every page cites its original. One that cannot is not published.
        return None, False, "no source URL to cite"
    lic = entry.get("licence", "unresolved")
    if not may_adapt(lic):
        # Not "unconvertible" -- unlicensed for this use. The catalogue still names it and links
        # upstream, so the material is findable; what is withheld is the derivative.
        return None, False, (f"licence: {lic} — does not permit a published derivative"
                             if lic and lic != "unresolved"
                             else "licence unresolved — resolve it before publishing a derivative")
    return output_path(entry, library), True, ""


# ---------------------------------------------------------------------------
# Planning: which files, by which route
# ---------------------------------------------------------------------------

@dataclass
class Doc:
    src: Path                  # absolute path in sources/
    rel: str                   # path relative to the source root
    route: str
    fidelity: str
    out_rel: str = ""          # output path relative to the source's output root, no extension
    parts: list = field(default_factory=list)


def candidate_files(root, include_all):
    """Every convertible file under a source, minus scaffolding and administrivia."""
    keep, skipped = [], []
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        if any(part in SKIP_DIRS for part in p.relative_to(root).parts[:-1]):
            continue
        if p.suffix.lower() not in ROUTES:
            continue
        rel = p.relative_to(root).as_posix()
        if not include_all and ADMIN.search(rel):
            skipped.append((rel, "administrivia"))
            continue
        keep.append(p)
    return keep, skipped


def group_documents(root, files):
    """One document per (directory, stem); convert only the best format present.

    This is where "convert the source, not the render" is enforced: the .pdf and .html built
    from a .qmd sit beside it with the same stem, and lose.
    """
    groups = {}
    for p in files:
        key = (p.parent, p.stem)
        groups.setdefault(key, []).append(p)

    docs, dropped = [], []
    for (parent, stem), members in sorted(groups.items()):
        members.sort(key=lambda p: PREFERENCE.index(p.suffix.lower()))
        best = members[0]
        for loser in members[1:]:
            dropped.append((loser.relative_to(root).as_posix(),
                            f"render of {best.suffix} with the same stem"))
        route, fidelity = ROUTES[best.suffix.lower()]
        docs.append(Doc(src=best, rel=best.relative_to(root).as_posix(),
                        route=route, fidelity=fidelity))

    docs, more = drop_transcript_renders(docs, root)
    return docs, dropped + more


ARTEFACT = re.compile(r"^(.*?)[-_](captions?|transcripts?|subs?)(?:-\d+)?$", re.I)


def drop_transcript_renders(docs, root):
    """A caption file beats a PDF of the same transcript.

    OCW ships each lecture's words up to four times: the `.srt` the video was captioned with, a
    PDF of that same transcript, a `transcripts-pdf/` directory holding it again, and the odd
    `-transcript-2`. They are the same speech, and only the `.srt` carries timings. Converting the
    rest produced the duplicate pages that made `6041sc/lectures/` alternate `01-captions`,
    `01-slides`, `01-transcript` -- and, now that PDFs go out to a model, it would pay for the
    same words three times over.

    `-slides.pdf` is NOT a transcript render and is kept: a deck is different content."""
    have_captions = set()
    for d in docs:
        if d.route != "transcript":
            continue
        m = ARTEFACT.match(Path(d.rel).stem)
        have_captions.add((str(Path(d.rel).parent), m.group(1) if m else Path(d.rel).stem))

    # A whole directory of transcript PDFs is the same duplication as a single mismatched file.
    # OCW ships `transcripts-pdf/<youtube-id>-transcript.pdf` beside the `.srt` the video was
    # captioned with; the stems never match, so a per-file rule misses every one of them, and they
    # came back as thirteen extra "chapters" repeating lectures the book already had.
    transcript_dir = re.compile(r"(^|/)(transcripts?[-_]?pdf|transcripts?)(/|$)", re.I)

    keep, dropped = [], []
    for d in docs:
        stem = Path(d.rel).stem
        m = ARTEFACT.match(stem)
        in_transcript_dir = bool(transcript_dir.search(str(Path(d.rel).parent)))
        if d.route == "llm" and in_transcript_dir and have_captions:
            dropped.append((d.rel, "transcript already present as captions"))
            continue
        is_transcript_render = (
            d.route == "llm" and m and m.group(2).lower().startswith(("transcript", "sub")))
        base = m.group(1) if m else stem
        parent = str(Path(d.rel).parent)
        if is_transcript_render and (
                (parent, base) in have_captions
                or any(b == base for _, b in have_captions)):
            dropped.append((d.rel, "transcript already present as captions"))
            continue
        keep.append(d)
    return keep, dropped


def pdf_has_text(path):
    """A scanned PDF has no text layer, and a near-empty page that looks like a conversion is
    worse than an honest absence. Probe a few pages rather than converting the whole thing."""
    try:
        import pymupdf
    except ImportError:
        import fitz as pymupdf
    try:
        with pymupdf.open(path) as doc:
            n = min(len(doc), 5)
            if n == 0:
                return False, 0
            chars = sum(len(doc[i].get_text().strip()) for i in range(n))
            return chars / n >= MIN_PDF_CHARS_PER_PAGE, chars // max(n, 1)
    except Exception as exc:
        return False, f"unreadable: {exc}"


# ---------------------------------------------------------------------------
# Conversion, one route per format
# ---------------------------------------------------------------------------

def read_text(path):
    return path.read_text(encoding="utf-8", errors="replace")


def convert_markdown(path):
    """.md / .qmd / .Rmd — strip the front matter and normalise the machinery, keep everything
    else byte for byte. The code in a chunk is material; the chunk options are not."""
    text = read_text(path)
    meta = {}
    m = FRONTMATTER.match(text)
    if m:
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except Exception:
            meta = {}
        text = text[m.end():]
    text = CHUNK.sub(lambda m: f"{m.group(1)}{m.group(2)}", text)

    def callout(m):
        return f'!!! {CALLOUT_MAP.get(m.group(1).lower(), "note")} "{m.group(1).title()}"'
    text = CALLOUT.sub(callout, text)
    return text, (meta.get("title") if isinstance(meta, dict) else None)


def convert_notebook(path):
    """Hand-rolled rather than nbconvert, for one reason: nbconvert writes image outputs as
    links to files we do not emit, and the site build fails on a broken link. Figures are named
    as omitted instead of silently linking nowhere."""
    nb = json.loads(read_text(path))
    out = []
    for cell in nb.get("cells", []):
        src = "".join(cell.get("source", [])).rstrip()
        if not src and cell.get("cell_type") != "code":
            continue
        if cell["cell_type"] == "markdown":
            out.append(src)
        elif cell["cell_type"] == "code":
            lang = (nb.get("metadata", {}).get("kernelspec", {}).get("language") or "python")
            if src:
                out.append(f"```{lang}\n{src}\n```")
            texts, figures = [], 0
            for o in cell.get("outputs", []):
                data = o.get("data", {})
                if "text/plain" in data and "image/png" not in data:
                    texts.append("".join(data["text/plain"]).rstrip())
                elif "image/png" in data or "image/jpeg" in data:
                    figures += 1
                elif o.get("output_type") == "stream":
                    texts.append("".join(o.get("text", [])).rstrip())
            if texts:
                out.append("```\n" + "\n".join(texts).strip() + "\n```")
            if figures:
                out.append(f"*({figures} figure{'s' if figures > 1 else ''} omitted — "
                           "see the original notebook.)*")
    title = None
    for block in out:
        m = re.match(r"^#\s+(.+)", block)
        if m:
            title = m.group(1).strip()
            break
    return "\n\n".join(out), title


def convert_pandoc(path, fmt):
    """Pandoc, with the mathematics carried past it by hand when the input is rendered HTML.

    Pandoc's HTML reader does NOT parse `<span class="math inline">\\(x\\)</span>` as mathematics:
    it treats the payload as literal text and escapes the backslashes. Verified on
    sources/berkeley-stat210a/fall-2025/homework.html, and it is why 360 pages published raw
    `<span class="math inline">` to the reader. So the spans are lifted out before conversion and
    put back after, exactly as they were written.
    """
    import pypandoc
    to = ("markdown_strict+pipe_tables+backtick_code_blocks+tex_math_dollars"
          "+fenced_code_attributes+header_attributes+footnotes+raw_tex-raw_html")
    args = ["--wrap=none", "--markdown-headings=atx", "--quiet"]
    if fmt == "html":
        guarded, store = protect_math_spans(read_text(path))
        text = pypandoc.convert_text(guarded, to, format=fmt, extra_args=args)
        return restore_math(text, store), None
    if fmt == "latex":
        return pypandoc.convert_text(pre_tex(read_text(path)), to, format=fmt,
                                     extra_args=args), None
    text = pypandoc.convert_file(str(path), to, format=fmt, extra_args=args)
    return text, None


TEX_MATH = re.compile(r"(<tex-math\b[^>]*>)(.*?)(</tex-math>)", re.S)


def convert_jats(path):
    """A journal article's JATS, with each formula's TeX unwrapped first.

    PubMed Central ships every `<tex-math>` as a complete LaTeX document -- `\\documentclass`,
    a dozen `\\usepackage` lines, `\\begin{document}$...$\\end{document}` -- and pandoc copies the
    preamble into the output, so every equation in a Nature Communications paper came out as
    `$\\documentclass[12pt]{minimal}`. The gate caught four of them only because they happened to
    unbalance the dollars; the rest would have published as junk. The author's own TeX is the
    body of that document, so it is kept and the wrapper dropped; pandoc supplies the delimiters."""
    import pypandoc

    def body(m):
        t = re.sub(r"<\?[^>]*\?>", "", m.group(2))
        doc = re.search(r"\\begin\{document\}(.*?)\\end\{document\}", t, re.S)
        t = re.sub(r"^\$\$?|\$\$?$", "", (doc.group(1) if doc else t).strip()).strip()
        return m.group(1) + t.replace("&", "&amp;").replace("<", "&lt;") + m.group(3)

    to = ("markdown_strict+pipe_tables+backtick_code_blocks+tex_math_dollars"
          "+fenced_code_attributes+header_attributes+footnotes+raw_tex-raw_html")
    raw = read_text(path)
    text = pypandoc.convert_text(TEX_MATH.sub(body, raw), to, format="jats",
                                 extra_args=["--wrap=none", "--markdown-headings=atx", "--quiet"])
    # The article's own title, so the document is not named after its first section.
    t = re.search(r"<title-group>.*?<article-title[^>]*>(.*?)</article-title>", raw, re.S)
    return text, (re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t.group(1))).strip() if t else None)


def convert_transcript(path):
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import transcript_text
    md = transcript_text.convert(path)
    if md is None:
        return "", None
    # Its first line is a `# <stem>` title; the section machinery here supplies its own.
    return re.sub(r"\A#\s+\S+\n", "", md), None


# `N[ϵ, F, L²(P)]` in a PDF comes out as `[ϵ, F, L_<sup>2</sup>](P)` — markdown link syntax
# manufactured out of mathematical notation, pointing at nothing. A PDF conversion has no
# hyperlinks worth keeping anyway, so the brackets are escaped and the text is left readable.
FAKE_LINK = re.compile(r"\[([^\]\n]{0,120})\]\((?!https?:)")


def convert_pdf(path):
    import pymupdf4llm
    text = pymupdf4llm.to_markdown(str(path), show_progress=False)
    text = FAKE_LINK.sub(lambda m: f"\\[{m.group(1)}\\](", text)
    return text, None


def convert(doc):
    if doc.route == "markdown":
        return convert_markdown(doc.src)
    if doc.route == "notebook":
        return convert_notebook(doc.src)
    if doc.route == "pandoc-latex":
        return convert_pandoc(doc.src, "latex")
    if doc.route == "pandoc-rst":
        return convert_pandoc(doc.src, "rst")
    if doc.route == "pandoc-html":
        return convert_pandoc(doc.src, "html")
    if doc.route == "pandoc-jats":
        return convert_jats(doc.src)
    if doc.route == "transcript":
        return convert_transcript(doc.src)
    if doc.route == "pdf":
        return convert_pdf(doc.src)
    raise ValueError(doc.route)


FIGDIR = "FIGDIR"          # placeholder prefix; pass 2 knows where the page actually lands
MODEL_IN_USE = [llm_pdf.DEFAULT_MODEL]   # set once from the CLI; the cache key depends on it


def convert_llm(path, model, cache_dir):
    """A PDF, read by a model, cross-checked against the parser. Returns (text, figures, reason).

    The parser is run only when the cache is about to MISS. On a hit the blob already carries the
    recall the cross-check produced at conversion time, and llm_pdf.convert() re-applies policy to
    those stored numbers -- so parsing again yields the same verdict at the cost of running
    pymupdf4llm over the whole corpus. Measured at 29.5s for one 47-page deck, which is how a
    regeneration that should be free came to take an hour."""
    key = llm_pdf.cache_key(path, model)
    deterministic = ""
    if not (cache_dir / f"{key}.json").exists():
        import pymupdf4llm
        try:
            deterministic = pymupdf4llm.to_markdown(str(path), show_progress=False)
        except Exception:
            deterministic = ""
    figs = cache_dir / "figures" / key
    r = llm_pdf.convert(path, model=model, cache_dir=cache_dir, figures_dir=figs,
                        rel_figures=FIGDIR, deterministic=deterministic)
    if not r.ok:
        return None, [], r.reason
    return r.markdown, r.figures, r.reason


_QUOTA_GONE = []          # per worker process: stop calling once the day's quota is gone


def convert_one(job):
    """Convert a single document. Pure function of its input path — the unit of parallelism.

    Runs in a worker process, so it takes and returns only plain data and never touches the
    output tree or the shared link map. Failures come back as values rather than exceptions,
    because one unreadable PDF in 1,591 must not take the pool down with it.
    """
    rel, src, route, fidelity, model, cache, apply, sync = job
    path = Path(src)
    if route == "llm":
        # The cache is consulted BEFORE credentials are. Converting from the batch cache is the
        # normal path and needs no API key at all; requiring one made a perfectly good cached
        # corpus look unconvertible the moment the environment was not sourced.
        have_cached = (Path(cache) / f"{llm_pdf.cache_key(path, model)}.json").exists()
        if not have_cached and not (
                os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")):
            return rel, "noapi", "not converted yet, and no GEMINI_API_KEY to convert it", None, []
        # Neither a dry run nor an --apply calls the model by default. The corpus is converted
        # through llm_batch.py, which is half the price, and a stray --apply that quietly spent
        # money on 172 PDFs is exactly the accident this prevents. `--llm-sync` opts in.
        # Uncached documents fall back to the parser's text so that splitting and page counts stay
        # realistic, and the summary says how many are waiting on the batch.
        if (not sync or not apply) and not have_cached:
            try:
                import pymupdf4llm
                stand_in = pymupdf4llm.to_markdown(str(path), show_progress=False)
            except Exception as exc:
                return rel, "fail", f"{type(exc).__name__}: {exc}", None, []
            return rel, "planned", tidy(stand_in), None, []
        if _QUOTA_GONE:
            return rel, "quota", "daily model quota reached — re-run to continue", None, []
        try:
            text, figures, note = convert_llm(path, model, Path(cache))
        except llm_pdf.QuotaExhausted as exc:
            # Not a failure of the document: it is simply not converted yet. Saying so keeps it
            # out of the "unconvertible" list, which is meant to be the material that needs a
            # different approach rather than the material that needs tomorrow.
            _QUOTA_GONE.append(True)
            return rel, "quota", str(exc), None, []
        except Exception as exc:
            return rel, "fail", f"{type(exc).__name__}: {exc}", None, []
        if text is None:
            return rel, "reject", note, None, []
        return rel, "ok", tidy(text), None, figures
    try:
        text, meta_title = convert(Doc(src=path, rel=rel, route=route, fidelity=fidelity))
    except Exception as exc:
        return rel, "fail", f"{type(exc).__name__}: {exc}", None, []
    return rel, "ok", tidy(text), meta_title, []


def convert_all(docs, jobs, model=llm_pdf.DEFAULT_MODEL, cache=None, apply=False,
                sync=False):
    """Run convert_one over every document, in parallel where it is worth it.

    PDFs are ~90% of the corpus by bytes and now go out to a model, so this is where the wall
    clock goes -- network-bound rather than CPU-bound, which parallelises just as well. Pass 2 stays serial: it needs the finished map of which file became which page,
    and it is only string work and file writes.
    """
    work = [(d.rel, str(d.src), d.route, d.fidelity, model, str(cache), apply, sync)
            for d in docs]
    if jobs > 1 and len(work) > 1:
        with ProcessPoolExecutor(max_workers=jobs) as pool:
            return {r[0]: r[1:] for r in pool.map(convert_one, work, chunksize=1)}
    return {r[0]: r[1:] for r in map(convert_one, work)}


# ---------------------------------------------------------------------------
# Splitting
# ---------------------------------------------------------------------------

def tidy(text):
    """Whitespace only. Everything else belongs to body_rules.normalise_body().

    This function used to substitute \\[ -> $$ and \\( -> $ across the whole document, which is how
    `\\EE\\[\\theta_i \\mid X\\]` became `\\EE\\[\\theta_i \\mid X$$`: a lazy match closing on the
    inner bracket of \\EE[...]. Delimiters are now handled paragraph-wise, first-open to last-close,
    in body_rules._display_math(), and the maths in rendered HTML never reaches a regex at all -- it
    is lifted out before pandoc sees the file."""
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip() + "\n"


def _heading_positions(text):
    """Headings outside fenced code.

    The old splitter ran HEADING.finditer over the raw document, so a `# comment` inside a Python
    block counted as a section boundary and the cut landed in the middle of the fence. That is the
    whole of the 652 pages that render as one giant code block, or as none."""
    out, fence = [], None
    offset = 0
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        if fence is None and (stripped.startswith("```") or stripped.startswith("~~~")):
            fence = stripped[0]
        elif fence and stripped.startswith(fence * 3):
            fence = None
        elif fence is None:
            m = HEADING.match(line.rstrip("\n"))
            if m:
                out.append((offset, len(m.group(1)), m.group(2).strip()))
        offset += len(line)
    return out


def split_sections(text):
    """Split into chapter-sized parts: the source's TOP heading level, and no deeper.

    The old rule tried each level shallowest-first and accepted one whose sections averaged over
    400 characters. Averaging is the flaw -- a single long section drags a crowd of three-line
    stubs over the bar -- and it produced 11,918 pages of which 2,243 had no body at all.

    So: cut at the top level only, then merge any part that is too thin into the one before it. A
    section that cannot stand as a page is not a page; it is part of the section above it."""
    headings = _heading_positions(text)
    if not headings:
        return [(None, text)]

    top = min(h[1] for h in headings)
    at = [h for h in headings if h[1] == top]
    if len(at) < 2:
        # One top-level heading is a document title, not a division. Try the next level down
        # before giving up, which is what makes a thesis chapter split into its sections.
        deeper = sorted({h[1] for h in headings if h[1] > top})
        at = next(([h for h in headings if h[1] == lvl]
                   for lvl in deeper if len([h for h in headings if h[1] == lvl]) >= 2), [])
        if not at:
            return [(None, text)]

    cuts = [h[0] for h in at] + [len(text)]
    parts = [(at[i][2], text[cuts[i]:cuts[i + 1]].strip()) for i in range(len(at))]

    lead = text[:at[0][0]].strip()
    if lead:
        if len(lead) >= MIN_SECTION_CHARS:
            parts.insert(0, (None, lead))
        else:                                   # a stray sentence, not an introduction
            parts[0] = (parts[0][0], lead + "\n\n" + parts[0][1])

    merged = []
    for title, body in parts:
        if merged and len(body) < MIN_PART_CHARS:
            prev_title, prev_body = merged[-1]
            merged[-1] = (prev_title, prev_body + "\n\n" + body)
        else:
            merged.append((title, body))

    # A thin FIRST part has no predecessor to fold into, so it folds forward instead -- and it is
    # the common case, not an edge one: an exam PDF opens with a letterhead ("Department of
    # Electrical Engineering & Computer Science"), which became a page of nothing but its own
    # heading. Seventy-nine such pages in one course.
    while len(merged) > 1 and len(merged[0][1]) < MIN_PART_CHARS:
        (_, first_body), (second_title, second_body) = merged[0], merged[1]
        merged[1] = (second_title, first_body + "\n\n" + second_body)
        merged.pop(0)
    return merged if len(merged) > 1 else [(None, text)]


def split_footnote_defs(text):
    """Separate footnote definitions from the prose. Returns (text_without_defs, {id: block}).

    A definition is `[^id]: …` plus any lines indented under it.
    """
    out, defs, cur_id, cur = [], {}, None, []
    for line in text.split("\n"):
        m = re.match(r"^\[\^([^\]]+)\]:", line)
        if m:
            if cur_id is not None:
                defs[cur_id] = "\n".join(cur).rstrip()
            cur_id, cur = m.group(1), [line]
            continue
        if cur_id is not None and line.startswith(("    ", "\t")):
            cur.append(line)
            continue
        if cur_id is not None:
            defs[cur_id] = "\n".join(cur).rstrip()
            cur_id, cur = None, []
        out.append(line)
    if cur_id is not None:
        defs[cur_id] = "\n".join(cur).rstrip()
    return "\n".join(out), defs


def carry_footnotes(all_defs, part):
    """Give each part exactly the footnote definitions it actually references.

    Splitting separates a footnote from its marker, and both halves then break: a definition
    whose `[^id]` marker ended up on another page renders a back-link to `#fnref:id`, an anchor
    that no longer exists on this one — 124 strict-build failures in a single converted course.
    A marker whose definition went the other way renders as literal `[^id]`.

    So definitions are stripped from every part and re-attached to the parts that use them. A
    footnote referenced twice across a split legitimately appears in both.
    """
    part, _ = split_footnote_defs(part)
    # Test against what markdown will actually render. A marker inside an HTML comment is not a
    # reference, and attaching a definition for it produces a footnote nothing points at — which
    # the strict build reports as a back-link to a missing `#fnref:` anchor.
    visible = re.sub(r"<!--.*?-->", "", part, flags=re.S)
    used = [i for i in all_defs if re.search(r"\[\^%s\]" % re.escape(i), visible)]
    if not used:
        return part.rstrip() + "\n"
    blocks = "\n\n".join(all_defs[i] for i in used)
    return part.rstrip() + "\n\n" + blocks + "\n"


def carry_reference_defs(whole, part):
    """A part that uses [text][ref] needs the definition, which may have been in another part.
    Without this the split itself manufactures broken links."""
    defs = REF_DEF.findall(whole)
    if not defs:
        return part
    used = [d for d in defs if re.search(r"\]\[%s\]" % re.escape(d), part)
            or re.search(r"\[%s\]\[\]" % re.escape(d), part)]
    if not used:
        return part
    lines = [m.group(0) for m in REF_DEF.finditer(whole)
             if re.match(r"^\[([^\]]+)\]", m.group(0)).group(1) in used]
    return part.rstrip() + "\n\n" + "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Link rewriting
# ---------------------------------------------------------------------------

def rewrite_links(text, doc, out_page_dir, entry, index_by_rel, root, anchors=None):
    """Point every relative link somewhere real: at the converted sibling, or at the original.

    The last case — no upstream recorded — strips the link to plain text rather than leaving it
    dangling, because the strict build treats a dangling link as an error and it is right to.

    Two cases look like they need no work and do:

    * **A site-root-relative link** (`/data`, `/units/unit9-sim.html`) is relative to the *source
      site's* root, not to this one. Left alone it points into this site and resolves nowhere.
    * **A fragment-only link** (`#data-exploration`) was valid in the source document and stops
      being valid the moment that document is split, because the heading it names is now on a
      sibling page. `anchors` maps heading slug -> the part that ended up holding it.
    """
    src_dir = (root / doc.rel).parent

    def sub(m):
        bang, label, target, title = m.group(1), m.group(2), m.group(3), m.group(4) or ""
        if re.match(r"^(https?:|mailto:)", target):
            # An absolute target needs no work, but its LABEL might: `[![logo](x.png)](https://…)`
            # is an image nested in a link, and returning the match untouched leaves the inner
            # relative image dangling in the built site.
            if "](" in label:
                return f"{bang}[{MD_LINK.sub(sub, label)}]({target}{title})"
            return m.group(0)

        # A fragment-only link: valid before the split, and this is where it gets repaired.
        if target.startswith("#"):
            frag = target[1:]
            if anchors is None or frag in anchors.get("_here", ()):
                return m.group(0)                       # heading stayed on this page
            dest = anchors.get(frag)
            if dest:
                link = os.path.relpath(dest, Path(out_page_dir)).replace(os.sep, "/")
                return f"[{label}]({link}#{frag})"
            return label                                # heading did not survive the conversion

        # `/x` is relative to the source site's root, not to ours.
        target = target.lstrip("/") if target.startswith("/") else target
        path_part, _, frag = target.partition("#")
        if not path_part:
            return m.group(0)
        if " " in path_part.strip():
            return label            # "link TBD" and friends: a placeholder, not a path
        try:
            resolved = (src_dir / path_part).resolve()
            rel = resolved.relative_to(root.resolve()).as_posix()
        except (ValueError, OSError):
            return f"{label}" if not bang else ""

        # 1. a converted sibling — an internal link, which is the point of the exercise
        if not bang:
            hit = index_by_rel.get(rel) or index_by_rel.get(_swap_render(rel, index_by_rel))
            if hit:
                target_path = Path(hit)
                here = Path(out_page_dir)
                link = os.path.relpath(target_path, here).replace(os.sep, "/")
                return f"[{label}]({link})"       # fragment dropped: splitting moved the anchors

        # 2. the original upstream
        url, _ = upstream(entry, rel, raw=bool(bang))
        if url:
            return f"{bang}[{label}]({url}{('#' + frag) if frag and not bang else ''}{title})"

        # 3. nowhere to point
        return label if not bang else f"*({label or 'figure'} — see the original)*"

    return MD_LINK.sub(sub, text)


def _swap_render(rel, index_by_rel):
    """`lecture07.pdf` in a link, `lecture07.qmd` in the tree — same document."""
    stem = rel.rsplit(".", 1)[0]
    for ext in PREFERENCE:
        if (cand := stem + ext) in index_by_rel:
            return cand
    return rel


# ---------------------------------------------------------------------------
# Emitting
# ---------------------------------------------------------------------------

# The provenance banner, one blockquote per page, immediately after the front matter and before
# the H1 -- the shape docs/notes uses. It replaces the old two-part header (a `**Source:**` line
# plus an `!!! warning` admonition), which gave content pages and index pages two different
# formats for the same information. references/page-template.md is the specification.
BANNERS = {
    "lossless": ("**Converted source.**",
                 "The same text in markdown, split so that every part has a URL; nothing here is "
                 "rewritten."),
    "high": ("**Converted source.**",
             "The same text in markdown, split so that every part has a URL; nothing here is "
             "rewritten."),
    "good": ("**Converted source.**",
             "The same text in markdown, split so that every part has a URL; nothing here is "
             "rewritten."),
    "speech": ("**Converted recording.**",
               "This is a transcript of speech, timestamped. Mathematics spoken aloud is left as "
               "it was spoken, and whatever was written on the board is not in it."),
    "lossy": ("**Converted from PDF — check the mathematics.**",
              "Prose survives a PDF; equations do not. Verify anything symbolic against the "
              "original before relying on it."),
    "reconstructed": ("**Reconstructed by a model.**",
                      "The original is a PDF with no usable text layer. A model read the pages and "
                      "wrote this markdown: the prose is a paraphrase in places and **every "
                      "equation is unverified**. Treat it as a pointer into the original, never as "
                      "a citable source."),
}


def provenance(entry, doc, url, exact):
    lic = entry.get("licence", "unresolved")
    if not url:
        src = f"`{doc.rel}`"
    elif exact:
        src = f"[`{doc.rel}`]({url})"
    else:
        src = f"`{doc.rel}` from [{entry['slug']}]({url})"
    label, note = BANNERS.get(doc.fidelity, BANNERS["good"])
    who = entry["slug"].replace("/", " · ")
    return (f"> {label} {src} — {who}, licensed {lic}. Converted {TODAY} from "
            f"`{doc.src.suffix}`. {note}\n")


def page(title, entry, doc, url, exact, body, nav_links):
    fm = {
        "title": title,
        "source": url or "",
        "source_file": f"sources/{entry['slug']}/{doc.rel}",
        "licence": entry.get("licence", "unresolved"),
        "route": doc.route,
        "fidelity": doc.fidelity,
        "converted": TODAY,
    }
    head = "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip() + "\n---\n"
    out = [head, provenance(entry, doc, url, exact), f"# {title}\n",
           normalise_body(body, title=title, route=doc.route)]
    if nav_links:
        out.append("---\n\n" + nav_links + "\n")
    return "\n".join(out)


GROUP_NAMES = {"recordings": "Recordings", "lectures": "Lectures", "psets": "Problem sets",
               "solutions": "Solutions", "exams": "Exams", "recitations": "Recitations",
               "tutorials": "Tutorials", "worked-examples": "Worked examples",
               "sections": "Sections", "labs": "Labs", "slides": "Slides", "notes": "Notes",
               "handwritten": "Handwritten", "reader": "Reader", "units": "Units",
               "homework": "Homework", ".": "Contents"}


def _group_label(folder):
    head = folder.split("/")[0] if folder != "." else "."
    return GROUP_NAMES.get(head, head.replace("-", " ").replace("_", " ").strip().capitalize())


def source_index(entry, docs, published, reason, skipped):
    """The contents page for one source: what it is, what is in it, and what is NOT.

    references/index-template.md is the specification. The front matter and banner are the same
    shape as a content page's -- they were two different formats for the same information, which
    is precisely the inconsistency this rebuild exists to remove -- and the `Not converted`
    section is what makes dropping material honest rather than silent."""
    slug = entry["slug"]
    title = source_title(entry)   # already formatted; normalise_title would flatten MIT -> Mit
    origin = entry.get("url") or entry.get("base")
    licence = entry.get("licence", "unresolved")
    pages = sum(max(1, len(d.parts)) for d in docs)

    lines = [
        "---",
        f'title: "{title}"',
        f"source: {origin or ''}",
        f"licence: {licence}",
        f"material: {entry.get('material') or 'unclassified'}",
        f"converted: '{TODAY}'",
        "---",
        "",
    ]
    where = f"[{title}]({origin})" if origin else f"`{slug}`"
    lines += [
        f"> **Converted source.** {where} — licensed {licence}. Converted {TODAY}. The same "
        f"material in markdown, split so that every part has a URL; nothing here is rewritten. "
        f"It is regenerable output and is never edited by hand — to change the text, fix the "
        f"converter or make an adaptation.",
        "",
        f"# {title}",
        "",
    ]

    routes = {}
    for d in docs:
        routes[d.route] = routes.get(d.route, 0) + 1
    how = ", ".join(f"{n} from `{r}`" for r, n in sorted(routes.items(), key=lambda kv: -kv[1]))
    lines += [f"{len(docs)} documents, {pages} pages — {how}." if docs
              else "Nothing from this source could be converted.", ""]

    by_dir = {}
    for d in docs:
        by_dir.setdefault(str(Path(d.out_rel or d.rel).parent), []).append(d)

    # Recordings last: a transcript of speech is a different object from a set of notes, and
    # interleaving them is what made `lectures/` alternate captions, slides and transcript.
    def order(folder):
        return (1 if folder.startswith("recordings") else 0, folder)

    for folder in sorted(by_dir, key=order):
        lines += [f"## {_group_label(folder)}", ""] if folder != "." else ["## Contents", ""]
        for d in sorted(by_dir[folder], key=lambda d: d.rel):
            if len(d.parts) == 1:
                lines.append(f"- [{d.parts[0][0]}]({d.parts[0][1]})")
            elif d.parts:
                lines.append(f"- **{Path(d.rel).stem}**")
                for t_, href in d.parts:
                    lines.append(f"    - [{t_}]({href})")
        lines.append("")

    if skipped:
        lines += ["## Not converted", "",
                  "Listed rather than dropped silently: a reader cannot otherwise tell an absence",
                  "from an oversight, and this is the material that needs a different approach.",
                  ""]
        by_reason = {}
        for rel, why in skipped:
            by_reason.setdefault(why, []).append(rel)
        for why in sorted(by_reason, key=lambda w: -len(by_reason[w])):
            files = by_reason[why]
            shown = ", ".join(f"`{f}`" for f in sorted(files)[:8])
            more = f" … and {len(files) - 8} more" if len(files) > 8 else ""
            lines += [f"- **{why}** ({len(files)}) — {shown}{more}", ""]
    return "\n".join(lines).rstrip() + "\n"


def footer(prev, nxt, up):
    bits = []
    if prev:
        bits.append(f"[← {prev[0]}]({prev[1]})")
    bits.append(f"[Up: contents]({up})")
    if nxt:
        bits.append(f"[{nxt[0]} →]({nxt[1]})")
    return " · ".join(bits)


# ---------------------------------------------------------------------------
# One source, end to end
# ---------------------------------------------------------------------------

def process(entry, sources_dir, library, include_all, apply, jobs=1,
            model=llm_pdf.DEFAULT_MODEL, cache=None, sync=False):
    """Convert one source, in two passes.

    Converting first and rendering second is not an optimisation — it is the only way the
    internal links can be right. Whether a document becomes one page or a directory of them is
    only known after it has been split, and a link from lecture 3 to lecture 7 has to point at
    whichever of those lecture 7 turned out to be.
    """
    slug = entry["slug"]
    root = sources_dir / slug
    out_root, published, reason = destination(entry, library)
    stats = {"slug": slug, "published": published, "reason": reason,
             "converted": 0, "parts": 0, "lossy": 0, "skipped": [], "docs": []}
    if out_root is None:
        stats["skipped"].append(("(whole source)", reason))
        return stats
    if not root.is_dir():
        stats["skipped"].append(("(whole source)", "not on disk — restore_sources.py"))
        return stats

    files, admin_skips = candidate_files(root, include_all)
    # `exclude:` is hand-written, per file, and names third-party publications that a course
    # happens to ship inside itself: a Wiley textbook chapter in `project/`, a paywalled RSS
    # paper in `ps/`, a publisher's own book-companion deck in `lectures/`. `material:` cannot
    # catch these because it classifies the SOURCE, and the source is a course. The rule it
    # enforces is already in AGENTS.md -- a book is never converted "however obtained", and a
    # paper without `open_access` is assumed paywalled -- so this is the missing per-file half
    # of a policy that already exists. Never detected, for the same reason `material:` is not:
    # guessing here guesses in the publishing direction.
    excluded = set(entry.get("exclude") or [])
    if excluded:
        keep = []
        for f in files:
            rel = f.relative_to(root).as_posix()
            if rel in excluded:
                admin_skips.append((rel, "third-party publication — not redistributed"))
            else:
                keep.append(f)
        files = keep
    docs, render_drops = group_documents(root, files)
    skipped = admin_skips + render_drops

    # ---- pass 1: convert, split, and decide where every page lands ------------------------
    cache = Path(cache or LIBRARY / "conversion-cache")
    MODEL_IN_USE[0] = model
    converted = convert_all(docs, jobs, model, cache, apply, sync)

    plans, index_by_rel, figures_for = [], {}, {}
    for d in docs:
        status, payload, meta_title, figures = converted[d.rel]
        if status == "scan":
            skipped.append((d.rel, f"no text layer (scan) — {payload} chars/page"))
            continue
        if status == "fail":
            skipped.append((d.rel, f"conversion failed: {payload}"))
            continue
        if status == "reject":
            skipped.append((d.rel, payload))
            continue
        if status == "noapi":
            skipped.append((d.rel, payload))
            continue
        if status == "quota":
            stats["pending"] = stats.get("pending", 0) + 1
            continue
        if status == "planned":
            stats["to_model"] = stats.get("to_model", 0) + 1
        figures_for[d.rel] = figures
        # `index.qmd` would be overwritten by the generated contents page at the same path, so
        # the source's own home page keeps its content under a name of its own.
        out = Path(d.rel).with_suffix("")
        if out.name == "index":
            out = out.with_name("home")
        # A transcript of speech and a set of typeset notes are different objects, and a directory
        # that alternates `01-captions`, `01-slides`, `01-transcript` tells a reader nothing about
        # which to open. Recordings get their own subtree, keeping the source's own grouping
        # underneath it, so `lectures/01-captions.srt` lands at `recordings/lectures/01`.
        if d.route == "transcript":
            out = Path("recordings") / out
            if out.name.endswith(("-captions", "-transcript", "-subs")):
                out = out.with_name(out.name.rsplit("-", 1)[0])
        d.out_rel = str(out)

        text = expand_shortcodes(payload, d.src, root)
        if meta_title:
            meta_title = expand_shortcodes(str(meta_title), d.src, root)
        if len(text.strip()) < 80:
            skipped.append((d.rel, "converted to almost nothing"))
            continue

        sections = split_sections(text)
        # A document with a single top heading is not "unsectioned" — that heading is its title.
        # Without this the page is named after its file (`Packages monod`) while the real title
        # (`Monod: CME inference from seq data`) sits duplicated in the body as a second H1.
        if len(sections) == 1 and sections[0][0] is None:
            m = re.match(r"\A#{1,4}[ \t]+(.+?)[ \t]*#*[ \t]*$", sections[0][1], re.M)
            if m:
                sections = [(m.group(1).strip(), sections[0][1])]
        stem = Path(d.rel).stem
        doc_title = clean_title(meta_title or sections[0][0] or "", stem)

        if len(sections) == 1:
            targets = [(out_root / (d.out_rel + ".md"), doc_title)]
            landing = targets[0][0]
        else:
            targets = []
            for i, (heading, _) in enumerate(sections, start=1):
                t = clean_title(heading, f"{stem} part {i}") if heading else "Introduction"
                targets.append((out_root / d.out_rel / f"{i:02d}-{slugify(t)}.md", t))
            landing = out_root / d.out_rel / "index.md"
        index_by_rel[d.rel] = str(landing)
        plans.append((d, text, sections, doc_title, targets, landing))

    # A source's output is regenerable in full, so it is rebuilt rather than written over.
    # Writing over leaves orphans: rename a section and the old file survives, stays in the nav,
    # and is published alongside its replacement with nobody able to tell which is current.
    if apply and plans and out_root.exists():
        shutil.rmtree(out_root)

    # ---- pass 2: render, now that every link has somewhere to point ------------------------
    for d, text, sections, doc_title, targets, landing in plans:
        url, exact = upstream(entry, d.rel)
        split = len(targets) > 1
        rendered = []

        # Which part ended up holding each heading. A `#section` link inside the source was
        # valid until the document was split; this is what lets it be repaired rather than
        # dropped, so a table of contents in the source keeps working.
        part_slugs = []
        for (heading, body), (target, title) in zip(sections, targets):
            slugs = {slugify(t) for _, t in HEADING.findall(body)}
            slugs.add(slugify(title))
            part_slugs.append(slugs)
        anchor_home = {}
        for slugs, (target, _) in zip(part_slugs, targets):
            for slug in slugs:
                anchor_home.setdefault(slug, target)

        _, footnote_defs = split_footnote_defs(text)
        for i, ((heading, body), (target, title)) in enumerate(zip(sections, targets)):
            anchors = dict(anchor_home, _here=part_slugs[i])
            body = carry_footnotes(footnote_defs, body)
            body = carry_reference_defs(text, body)
            body = rewrite_links(body, d, target.parent, entry, index_by_rel, root, anchors)
            if heading:
                # The section heading becomes the page title; drop the duplicate from the body.
                body = re.sub(r"\A#{1,4}\s+.+?\n", "", body, count=1)
            prev = (targets[i - 1][1], _href(targets[i - 1][0], target)) if i else None
            nxt = ((targets[i + 1][1], _href(targets[i + 1][0], target))
                   if i + 1 < len(targets) else None)
            nav = footer(prev, nxt, _href(landing if split else out_root / "index.md", target))
            body = place_figures(body, d, target, out_root, figures_for.get(d.rel, []),
                                 cache, apply)
            rendered.append((target, page(title, entry, d, url, exact, body, nav)))

        # The gates decide what is PUBLISHED, not merely what is reported. This has to happen
        # before the contents listing is built, or a dropped page stays linked from it and the
        # strict build fails on the dangling link. references/quality-gates.md is the
        # specification and validate_pages.py the implementation, so CI and the converter cannot
        # disagree about what is acceptable.
        keep = []
        for target, content in rendered:
            report = validate_pages.check(target, content)
            if report.fatal:
                skipped.append((f"{d.rel} → {target.name}",
                                report.fatal[0].gate.replace("-", " ")))
                continue
            keep.append((target, content))
        if not keep:
            continue
        titles = dict(targets)
        targets = [(target, titles[target]) for target, _ in keep]
        rendered = keep
        split = len(targets) > 1

        figures_found = extract_document_figures(d, out_root, entry, apply)
        if split:
            listing = "\n".join(f"{i}. [{t}]({_href(pt, landing)})"
                                 for i, (pt, t) in enumerate(targets, 1))
            rendered.append((landing, page(
                doc_title, entry, d, url, exact,
                f"Split into {len(targets)} sections.\n\n{listing}\n"
                + figures_section(figures_found, landing, out_root, d),
                f"[Up: contents]({_href(out_root / 'index.md', landing)})")))
        elif figures_found:
            # Unsplit: the figures go on the one page there is, after its body.
            target, content = rendered[0]
            rendered[0] = (target, content.rstrip("\n") + "\n"
                           + figures_section(figures_found, target, out_root, d) + "\n")

        d.parts = [(t, _href(pt, out_root / "index.md")) for pt, t in targets]
        if not split and len(rendered) == 1 and rendered[0][0] == landing:
            landing = rendered[0][0]
        stats["converted"] += 1
        stats["parts"] += len(targets)
        if d.fidelity == "lossy":
            stats["lossy"] += 1
        stats["docs"].append(d)

        # The gates decide what is published, not just what is reported. A page that fails one is
        # named under "Not converted" on the source's contents page instead of being shipped
        # broken -- references/quality-gates.md is the specification and validate_pages.py is the
        # implementation, so CI and the converter cannot disagree about what is acceptable.
        if apply:
            for target, content in rendered:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")

    stats["skipped"] = skipped
    if apply and stats["docs"]:
        out_root.mkdir(parents=True, exist_ok=True)
        (out_root / "index.md").write_text(
            source_index(entry, stats["docs"], published, reason, skipped), encoding="utf-8")
    return stats


# An extracted figure is redistribution of source content in a way reformatted prose is not, so
# extraction is gated on the licence rather than attempted everywhere. `unresolved` is the default
# and costs nothing; a wrongly published figure cannot be recalled from a public site.
FIGURE_LICENCES = {"cc by 4.0", "cc by-nc 4.0", "cc by-nc-sa 4.0", "cc by-sa 4.0", "cc0-1.0",
                   "cc0 1.0", "bsd-2-clause", "bsd-3-clause", "mit", "public domain"}


def may_extract_figures(entry):
    return (entry.get("licence") or "unresolved").strip().lower() in FIGURE_LICENCES


def extract_document_figures(d, out_root, entry, apply):
    """Pull a PDF's figures out locally and list them on the document's landing page.

    Local, free and independent of the model: pymupdf reads the images straight out of the file.
    What it cannot do is place them where they belong in the prose -- the model was not told the
    filenames, so its markdown does not reference them -- so each figure is listed with the source
    page it came from rather than dropped into the text at a guessed position. Approximate
    placement, honestly labelled, beats 3,519 figures reduced to OCR fragments.
    """
    if d.route != "llm" or not may_extract_figures(entry):
        return []
    try:
        import pymupdf
    except ImportError:
        try:
            import fitz as pymupdf
        except ImportError:
            return []
    home = out_root / d.out_rel / "figures"
    found = []
    try:
        with pymupdf.open(d.src) as doc:
            for pno in range(len(doc)):
                for k, info in enumerate(doc[pno].get_images(full=True)):
                    try:
                        img = doc.extract_image(info[0])
                    except Exception:
                        continue
                    data, ext = img["image"], img["ext"]
                    if not (llm_pdf.MIN_FIGURE_BYTES <= len(data) <= llm_pdf.MAX_FIGURE_BYTES):
                        continue
                    name = f"p{pno + 1:03d}-{k + 1}.{ext}"
                    if apply:
                        home.mkdir(parents=True, exist_ok=True)
                        (home / name).write_bytes(data)
                    found.append((pno + 1, name))
    except Exception:
        return []
    return found


def figures_section(found, from_page, out_root, d):
    if not found:
        return ""
    prefix = _href(out_root / d.out_rel / "figures" / "X", from_page).rsplit("/", 1)[0]
    lines = ["", "## Figures", "",
             "Extracted from the original PDF. They are listed by the page they came from rather",
             "than placed in the text: the conversion does not record where on the page each one",
             "sat.", ""]
    for page_no, name in found:
        lines.append(f"![Figure from page {page_no} of the original]({prefix}/{name})")
        lines.append("")
    return "\n".join(lines)


def place_figures(body, d, target, out_root, figures, cache, apply):
    """Put extracted figures beside the page that references them.

    The model is given a `FIGDIR/` placeholder rather than a real path, because where a page ends
    up is only known after the document has been split -- a split document's pages sit one
    directory deeper than an unsplit one's, and a relative image path has to account for that.
    Figures nothing references are not copied: the model is the judge of which pages a figure
    belongs on, and an unreferenced one is usually a decorative rule the extractor picked up."""
    if FIGDIR + "/" not in body:
        return body
    home = out_root / d.out_rel / "figures"
    prefix = ("figures" if target.parent == out_root / d.out_rel
              else f"{Path(d.out_rel).name}/figures")
    wanted = set(re.findall(re.escape(FIGDIR) + r"/([\w.\-]+)", body))
    if apply and wanted:
        staged = Path(cache) / "figures" / llm_pdf.cache_key(d.src, MODEL_IN_USE[0])
        home.mkdir(parents=True, exist_ok=True)
        for name in wanted:
            src = staged / name
            if src.exists():
                shutil.copy2(src, home / name)
    return body.replace(FIGDIR + "/", prefix + "/")


def _href(target, from_page):
    """Relative markdown link from one page to another."""
    return os.path.relpath(Path(target), Path(from_page).parent).replace(os.sep, "/")


# ---------------------------------------------------------------------------
# Nav
# ---------------------------------------------------------------------------

def read_title(path):
    m = FRONTMATTER.match(read_text(path))
    if m:
        try:
            meta = yaml.safe_load(m.group(1)) or {}
            if meta.get("title"):
                return str(meta["title"])
        except Exception:
            pass
    return path.stem


def read_meta(path):
    m = FRONTMATTER.match(read_text(path))
    try:
        return (yaml.safe_load(m.group(1)) or {}) if m else {}
    except Exception:
        return {}


def is_written(course: Path) -> bool:
    """Whether this directory holds a written book.

    True by construction: synthesise_book's `write` emits every chapter with a `chapter:` field in
    its front matter, and nothing else in the tree carries one."""
    return course.is_dir() and any(
        "\nchapter:" in p.read_text(encoding="utf-8", errors="ignore")[:400]
        for p in course.glob("*.md"))


CHAPTER_FILE = re.compile(r"^(\d+)-")


def chapter_order(path: Path):
    """Sort key putting `100-…` after `99-…`, not between `10-` and `11-`."""
    m = CHAPTER_FILE.match(path.name)
    return (int(m.group(1)) if m else float("inf"), path.name)


def repair_dangling_links(published_root, apply):
    """Strip links whose target was not published, after the gates have decided.

    The link map is necessarily built in pass 1, before a page can be rendered and therefore
    before it can be judged -- so a page that later fails a gate leaves every link to it dangling,
    and the strict build fails on 215 of them. Rather than publish a broken page to keep a link
    alive, the link becomes plain text: the material is named on its source's contents page under
    "Not converted", which is where a reader should be sent anyway.
    """
    fixed = pages = 0
    for md in published_root.rglob("*.md"):
        text = md.read_text(encoding="utf-8")

        def sub(m):
            nonlocal fixed
            bang, label, target, title = m.group(1), m.group(2), m.group(3), m.group(4) or ""
            if re.match(r"^(https?:|mailto:|#)", target) or not target.strip():
                return m.group(0)
            path_part = target.partition("#")[0]
            if not path_part:
                return m.group(0)
            dest = (md.parent / path_part).resolve()
            if dest.exists() or dest.with_suffix(".md").exists() or (dest / "index.md").exists():
                return m.group(0)
            fixed += 1
            return label if not bang else ""

        out = MD_LINK.sub(sub, text)
        if out != text:
            pages += 1
            if apply:
                md.write_text(out, encoding="utf-8")
    return fixed, pages


def write_nav(reference_dir, apply):
    """Regenerate SUMMARY.md from what is on disk.

    Built by scanning rather than from this run's output, so the nav is correct whichever subset
    of sources has been converted so far. `mkdocs-literate-nav` reads it.

    **A book lists its chapters; a converted document stops at the document.** Material renders
    the navigation tree into every page it builds, so nav size multiplies across the site. When
    the library was ~12,000 converted section pages, listing them all produced 5.8 MB of sidebar
    on each page, a site far over GitHub Pages' 1 GB limit, so the nav stopped at the document.
    A book is a few dozen chapters a reader moves between, and with `navigation.prune` on a page
    renders only its own book's chapters: listing all 450 adds ~10 MB to the site and keeps the
    largest page under 90 KB. Converted split documents still collapse to their index, which
    lists their sections.
    """
    if not reference_dir.is_dir():
        return 0
    lines = ["<!-- Generated by normalise_source.py. Do not edit. -->", "",
             "- [Home](index.md)"]
    count = 1

    def is_split_document(d):
        """A directory holding one document's sections: an index plus NN-*.md parts."""
        return (d / "index.md").exists() and any(
            re.match(r"^\d{2}-", p.name) for p in d.iterdir() if p.suffix == ".md")

    def walk(d, depth):
        nonlocal count
        pad = "    " * depth
        idx = d / "index.md"
        entries = sorted(p for p in d.iterdir() if p.name != "SUMMARY.md")
        subdirs = [p for p in entries if p.is_dir()]
        pages = sorted((p for p in entries
                        if p.is_file() and p.suffix == ".md" and p.name != "index.md"),
                       key=chapter_order)
        if idx.exists():
            lines.append(f"{pad}- [{read_title(idx)}]({idx.relative_to(reference_dir).as_posix()})")
            count += 1
            pad += "    "
            depth += 1
        for p in pages:
            lines.append(f"{pad}- [{read_title(p)}]({p.relative_to(reference_dir).as_posix()})")
            count += 1
        for sub in subdirs:
            if not any(sub.rglob("*.md")):
                continue
            if is_split_document(sub) and not is_written(sub):
                # The document, not its sections. Its own index page lists those.
                target = (sub / "index.md").relative_to(reference_dir).as_posix()
                lines.append(f"{pad}- [{read_title(sub / 'index.md')}]({target})")
                count += 1
            elif not (sub / "index.md").exists():
                lines.append(f"{pad}- {prettify(sub.name)}:")
                walk(sub, depth + 1)
            else:
                walk(sub, depth)

    top = sorted(p for p in reference_dir.iterdir() if p.is_dir())
    for d in top:
        if any(d.rglob("*.md")):
            if (d / "index.md").exists():
                walk(d, 0)
            else:
                lines.append(f"- {prettify(d.name)}:")
                walk(d, 1)

    text = "\n".join(lines) + "\n"
    if apply:
        (reference_dir / "SUMMARY.md").write_text(text, encoding="utf-8")
    return count


def write_library_index(reference_dir, apply):
    """The landing page: one entry per course, read from the tree it describes.

    Not from the lockfile. Its slugs are course YEARS (`berkeley-stat243/fall-2024`), and a book
    merges the years into one directory, so looking each slug's index up by path missed every
    merged book: four books and 266 chapters, with a whole discipline, were absent from the page.
    The shelf is `docs/<discipline>/<provider>/<course>/`: a course with an index is one entry,
    and a course that is not a book lists the year directories it was converted into.
    """
    if not reference_dir.is_dir():
        return
    books, converted, papers = [], [], []
    shelf = reference_dir / "papers"
    for page in sorted(shelf.glob("*/*/index.md")) if shelf.is_dir() else []:
        # docs/papers/<subject>/<slug>/index.md -- a summary, with the full text beneath it where
        # the paper's licence lets it be published.
        papers.append((page.parent.parent.name, read_title(page),
                       page.relative_to(reference_dir).as_posix(),
                       (page.parent / "full-text" / "index.md").exists()))
    for discipline in sorted(p for p in reference_dir.iterdir() if p.is_dir() and p != shelf):
        for provider in sorted(p for p in discipline.iterdir() if p.is_dir()):
            for course in sorted(p for p in provider.iterdir() if p.is_dir()):
                units = ([course] if (course / "index.md").exists() else
                         sorted(d for d in course.iterdir() if (d / "index.md").exists()))
                for unit in units:
                    idx = unit / "index.md"
                    entry = (discipline.name, read_title(idx),
                             idx.relative_to(reference_dir).as_posix(),
                             read_meta(idx).get("licence", "unresolved"))
                    if is_written(unit):
                        n = sum(1 for p in unit.glob("*.md") if CHAPTER_FILE.match(p.name))
                        books.append(entry + (n,))
                    else:
                        n = sum(1 for p in unit.rglob("*.md") if p.name != "index.md")
                        converted.append(entry + (n,))

    def listing(rows, unit):
        out, current = [], None
        for discipline, title, href, licence, n in rows:
            if discipline != current:
                out += ["", f"### {prettify(discipline)}", ""]
                current = discipline
            out.append(f"- [{title}]({href}) — {n} {unit}{'s' if n != 1 else ''}, {licence}")
        return out

    chapters = sum(r[-1] for r in books)
    pages = sum(r[-1] for r in converted)
    body = [
        "---", "title: Home", "---", "",
        "# Study reference library", "",
        "Other people's courses, written up as one book per course from everything the course",
        "provides. The companion to the",
        "[study knowledge base](https://github.com/Claptar/knowledge-base), which holds the notes",
        "themselves — the split is by authorship, not by subject.",
        "",
        f"**{len(books)} course books, {chapters} chapters.** "
        + (f"{len(converted)} further sources are converted but not yet written as books — "
           f"{pages} pages. " if converted else "")
        + "Books and paywalled papers are deliberately absent.",
        "",
        "## Course books", "",
        "> **Rewritten, not reformatted.** Each book merges a course's slides, recordings, notes",
        "> and problem sets into chapters, names every course offering it was written from, and",
        "> carries the licence those offerings permit. The books are generated and are",
        "> **never edited by hand**.",
    ]
    body += listing(books, "chapter") if books else ["", "*(none yet)*"]
    if papers:
        body += [
            "", "## Papers", "",
            f"> **{len(papers)} papers and theses**, each summarised in our own words. The full "
            f"text is here too for the {sum(1 for p in papers if p[3])} whose licence allows it; "
            "the rest are summaries only and link to the original.",
        ]
        current = None
        for subject, title, href, full in papers:
            if subject != current:
                body += ["", f"### {prettify(subject)}", ""]
                current = subject
            body.append(f"- [{title}]({href}) — {'summary and full text' if full else 'summary'}")
    if converted:
        body += [
            "", "## Converted sources", "",
            "> **Converted, not adapted.** The text is its author's, reformatted and split so that",
            "> every part has a URL. A page built from a PDF carries a warning, because prose",
            "> survives a PDF and mathematics does not.",
        ]
        body += listing(converted, "page")
    text = "\n".join(body).rstrip() + "\n"
    if apply:
        (reference_dir / "index.md").write_text(text, encoding="utf-8")


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", type=Path, help="source directories under sources/")
    ap.add_argument("--sources", type=Path, default=LIBRARY / "sources")
    ap.add_argument("--all", action="store_true", help="every source in the lockfile")
    ap.add_argument("--include-all", action="store_true", help="keep course administrivia")
    ap.add_argument("--summary-only", action="store_true", help="regenerate nav only")
    ap.add_argument("--jobs", type=int, default=min(8, os.cpu_count() or 1),
                    help="parallel conversion workers (default: min(8, cores); 1 disables)")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--clean", action="store_true",
                    help="delete the published tree before converting. Use with --all: a source "
                         "whose documents are all pending never gets its directory rebuilt, so "
                         "output from a previous run survives as orphans -- 894 pages of the old "
                         "corpus, still carrying a route that no longer exists.")
    ap.add_argument("--llm-sync", action="store_true",
                    help="call the model directly instead of using the batch cache. Costs twice "
                         "as much; use llm_batch.py for the corpus.")
    ap.add_argument("--llm-model", default=llm_pdf.DEFAULT_MODEL,
                    help="model for the PDF route (default: %(default)s). The cache key depends "
                         "on it, so changing it re-converts every PDF.")
    a = ap.parse_args()

    published_root = LIBRARY / "docs"
    lock = load_lock(a.sources)
    by_slug = {e["slug"]: e for e in lock.get("sources", [])}

    if a.summary_only:
        write_library_index(published_root, a.apply)
        n = write_nav(published_root, a.apply)
        print(f"nav: {n} entries" + ("" if a.apply else "  (dry run)"))
        return 0

    if a.all:
        entries = list(by_slug.values())
    else:
        if not a.paths:
            sys.exit("give one or more source directories, or --all")
        entries = []
        for p in a.paths:
            slug = p.resolve().relative_to(a.sources.resolve()).as_posix()
            if slug not in by_slug:
                sys.exit(f"{slug} is not in the lockfile — run lock_sources.py first")
            entries.append(by_slug[slug])

    if a.clean and a.apply:
        # Everything under docs/ is generated except the MathJax config, which is hand-written.
        keep = {"javascripts"}
        for child in sorted(published_root.iterdir()):
            if child.name in keep:
                continue
            shutil.rmtree(child) if child.is_dir() else child.unlink()
        print(f"cleaned {published_root} (kept {', '.join(sorted(keep))})")

    results = [process(e, a.sources, LIBRARY, a.include_all, a.apply, a.jobs,
                       a.llm_model, None, a.llm_sync) for e in entries]

    print(f"{'source':45s} {'dest':8s} {'docs':>5s} {'pages':>6s} {'lossy':>6s} {'skipped':>8s}")
    print("-" * 84)
    tot = {"converted": 0, "parts": 0, "lossy": 0, "skipped": 0}
    for r in results:
        dest = "public" if r["published"] else "private"
        print(f"{r['slug']:45s} {dest:8s} {r['converted']:5d} {r['parts']:6d} "
              f"{r['lossy']:6d} {len(r['skipped']):8d}")
        for k in ("converted", "parts", "lossy"):
            tot[k] += r[k]
        tot["skipped"] += len(r["skipped"])
    print("-" * 84)
    print(f"{'TOTAL':45s} {'':8s} {tot['converted']:5d} {tot['parts']:6d} "
          f"{tot['lossy']:6d} {tot['skipped']:8d}")

    private = [r for r in results if not r["published"] and r["reason"]]
    if private:
        print("\nNot published:")
        for r in private:
            print(f"  {r['slug']:45s} {r['reason']}")

    reasons = {}
    for r in results:
        for _, why in r["skipped"]:
            key = re.sub(r"\d+", "N", why.split("—")[0].strip())
            reasons[key] = reasons.get(key, 0) + 1
    if reasons:
        print("\nSkipped, by reason:")
        for why, n in sorted(reasons.items(), key=lambda kv: -kv[1]):
            print(f"  {n:5d}  {why}")

    pending = sum(r.get("pending", 0) for r in results)
    to_model = sum(r.get("to_model", 0) for r in results)
    if pending:
        print(f"\n{pending} documents pending: the day's model quota is gone. Everything already "
              f"converted is cached,\nso re-running tomorrow resumes rather than starting over.")
    if to_model:
        print(f"\n{to_model} PDFs are not in the conversion cache yet. Queue them with\n"
              f"  llm_batch.py submit   (half price, results within 24h)\n"
              f"then re-run this with --apply. Nothing here called the model.")

    if a.apply:
        fixed, on_pages = repair_dangling_links(published_root, True)
        if fixed:
            print(f"\nstripped {fixed} links on {on_pages} pages whose target failed a gate")
        write_library_index(published_root, True)
        n = write_nav(published_root, True)
        print(f"\nwrote {tot['parts']} pages; nav has {n} entries")
    else:
        print("\nDry run. Re-run with --apply to write.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
