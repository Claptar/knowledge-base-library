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
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pyyaml missing — run with `uv run --group dev python …`")

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
    ".pdf": ("pdf", "lossy"),
}
PREFERENCE = [".qmd", ".rmd", ".md", ".rst", ".ipynb", ".tex", ".srt", ".vtt", ".html", ".pdf"]

SKIP_DIRS = {
    ".git", ".github", ".quarto", "_freeze", "_site", "site_libs", "libs", "node_modules",
    "renv", "__pycache__", ".Rproj.user", "assets", "img", "images", "figures", "figure",
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
MD_LINK = re.compile(r"(!?)\[([^\]]*)\]\(\s*<?([^()>]*?)>?(\s+\"[^\"]*\")?\s*\)")
LATEX_INLINE = re.compile(r"\\\((.+?)\\\)", re.S)
LATEX_DISPLAY = re.compile(r"\\\[(.+?)\\\]", re.S)

SHORTCODE = re.compile(r"\{\{<\s*(\w+)\s+([^>]*?)\s*>\}\}")
HTML_TAG = re.compile(r"</?[a-zA-Z][^>]*>")
# A PDF's first bold line is often a form field, not a title: "Student ID (NOT your name):".
JUNK_TITLE = re.compile(
    r"^(student\s*id|name|signature|date|score|total|page\s*\d|do not|instructions?)\b", re.I)

MIN_SECTION_CHARS = 400        # below this a "section" is a stub; back off to a shallower level
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
    return docs, dropped


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
    import pypandoc
    # markdown_strict plus the extensions MkDocs actually renders. Dropping raw_html and the
    # native div/span extensions keeps Quarto's and MathJax's wrapper markup out of the output;
    # tex_math_dollars is what keeps the mathematics as $…$, which is the whole point.
    to = ("markdown_strict+pipe_tables+backtick_code_blocks+tex_math_dollars"
          "+fenced_code_attributes+header_attributes+footnotes+raw_tex")
    text = pypandoc.convert_file(
        str(path), to, format=fmt,
        extra_args=["--wrap=none", "--markdown-headings=atx", "--quiet"],
    )
    return text, None


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
    if doc.route == "transcript":
        return convert_transcript(doc.src)
    if doc.route == "pdf":
        return convert_pdf(doc.src)
    raise ValueError(doc.route)


# ---------------------------------------------------------------------------
# Splitting
# ---------------------------------------------------------------------------

def tidy(text):
    """Repo conventions that apply to every route, whatever it came from."""
    text = LATEX_DISPLAY.sub(lambda m: f"$${m.group(1)}$$", text)
    text = LATEX_INLINE.sub(lambda m: f"${m.group(1)}$", text)   # arithmatex needs $…$
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip() + "\n"


def split_sections(text):
    """Split on the shallowest heading level that yields real sections.

    Shallowest first, because a lecture's `##` subsections are parts of one argument and the
    `#` sections are the argument — and a level that produces a crowd of three-line stubs is
    the wrong level, so it backs off.
    """
    headings = [(m.start(), len(m.group(1)), m.group(2).strip()) for m in HEADING.finditer(text)]
    if not headings:
        return [(None, text)]

    for level in sorted({h[1] for h in headings}):
        at = [h for h in headings if h[1] == level]
        if len(at) < 2:
            continue
        cuts = [h[0] for h in at] + [len(text)]
        bodies = [text[cuts[i]:cuts[i + 1]].strip() for i in range(len(at))]
        if sum(len(b) for b in bodies) / len(bodies) < MIN_SECTION_CHARS:
            continue                                   # stubs — try a shallower level
        parts = []
        lead = text[:at[0][0]].strip()
        if len(lead) >= MIN_SECTION_CHARS:
            parts.append((None, lead))
        parts += [(at[i][2], bodies[i]) for i in range(len(at))]
        return parts
    return [(None, text)]


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

PDF_BANNER = ("!!! warning \"Converted from PDF — mathematics may be mangled\"\n"
              "    Prose survives a PDF; equations do not. Check anything symbolic against the\n"
              "    original before relying on it, and mark repairs `**Unverified.**`\n")


def provenance(entry, doc, url, exact):
    lic = entry.get("licence", "unresolved")
    if not url:
        src = f"`{doc.rel}`"
    elif exact:
        src = f"[`{doc.rel}`]({url})"
    else:
        src = f"`{doc.rel}` from [{entry['slug']}]({url})"
    return (f"**Source:** {src} · **Licence:** {lic} · "
            f"Converted {TODAY} from `{doc.src.suffix}` ({doc.fidelity})\n")


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
    out = [head, f"# {title}\n", provenance(entry, doc, url, exact)]
    if doc.fidelity == "lossy":
        out.append(PDF_BANNER)
    out.append(body.strip() + "\n")
    if nav_links:
        out.append("---\n\n" + nav_links + "\n")
    return "\n".join(out)


def source_index(entry, docs, published, reason, skipped):
    slug = entry["slug"]
    title = slug.replace("/", " · ").replace("-", " ")
    origin = entry.get("url") or entry.get("base")
    lines = [
        "---",
        f"title: {title}",
        f"source: {origin or ''}",
        f"licence: {entry.get('licence', 'unresolved')}",
        f"converted: {TODAY}",
        "---",
        "",
        f"# {title}",
        "",
    ]
    lines.append(
        f"Converted material from [{origin}]({origin})." if origin
        else "Converted material. **No upstream URL recorded** — see `sources.lock.yml`."
    )
    lines += [
        "",
        f"**Licence:** {entry.get('licence', 'unresolved')} · "
        f"**Material:** {entry.get('material') or 'unclassified'} · "
        f"**Converted:** {TODAY}",
        "",
        "> Converted, not adapted — the same text in markdown, split so every part has a URL.",
        "> It is regenerable output and is **never edited by hand**: a hand edit is lost on the",
        "> next run and silently diverges from the source it claims to reproduce. To change the",
        "> text, make an adaptation instead.",
        "",
        "## Contents",
        "",
    ]

    by_dir = {}
    for d in docs:
        by_dir.setdefault(str(Path(d.rel).parent), []).append(d)
    for folder in sorted(by_dir):
        if folder != ".":
            lines += [f"### {folder}", ""]
        for d in sorted(by_dir[folder], key=lambda d: d.rel):
            if len(d.parts) == 1:
                lines.append(f"- [{d.parts[0][0]}]({d.parts[0][1]})")
            else:
                lines.append(f"- **{Path(d.rel).stem}**")
                for t, href in d.parts:
                    lines.append(f"    - [{t}]({href})")
        lines.append("")
    if skipped:
        lines += ["## Not converted", "",
                  "Listed rather than dropped silently, because this is the material that needs a",
                  "different approach.", ""]
        by_reason = {}
        for rel, why in skipped:
            by_reason.setdefault(why, []).append(rel)
        for why in sorted(by_reason):
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

def process(entry, sources_dir, library, include_all, apply):
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
    docs, render_drops = group_documents(root, files)
    skipped = admin_skips + render_drops

    # ---- pass 1: convert, split, and decide where every page lands ------------------------
    plans, index_by_rel = [], {}
    for d in docs:
        if d.route == "pdf":
            ok, chars = pdf_has_text(d.src)
            if not ok:
                skipped.append((d.rel, f"no text layer (scan) — {chars} chars/page"))
                continue
        # `index.qmd` would be overwritten by the generated contents page at the same path, so
        # the source's own home page keeps its content under a name of its own.
        out = Path(d.rel).with_suffix("")
        if out.name == "index":
            out = out.with_name("home")
        d.out_rel = str(out)

        try:
            text, meta_title = convert(d)
        except Exception as exc:
            skipped.append((d.rel, f"conversion failed: {type(exc).__name__}: {exc}"))
            continue
        text = expand_shortcodes(tidy(text), d.src, root)
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
            rendered.append((target, page(title, entry, d, url, exact, body, nav)))

        if split:
            listing = "\n".join(f"{i}. [{t}]({_href(pt, landing)})"
                                 for i, (pt, t) in enumerate(targets, 1))
            rendered.append((landing, page(
                doc_title, entry, d, url, exact,
                f"Split into {len(targets)} sections.\n\n{listing}\n",
                f"[Up: contents]({_href(out_root / 'index.md', landing)})")))

        d.parts = [(t, _href(pt, out_root / "index.md")) for pt, t in targets]
        stats["converted"] += 1
        stats["parts"] += len(targets)
        if d.fidelity == "lossy":
            stats["lossy"] += 1
        stats["docs"].append(d)

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


def write_nav(reference_dir, apply):
    """Regenerate SUMMARY.md from what is on disk.

    Built by scanning rather than from this run's output, so the nav is correct whichever subset
    of sources has been converted so far. `mkdocs-literate-nav` reads it.

    **The nav stops at the document, never the section.** Material renders the navigation tree
    into every page it builds, so nav size multiplies across the site: listing all 9,967 section
    pages produced 5.8 MB of sidebar on *each* of 11,808 pages — a 68 GB site, against GitHub
    Pages' 1 GB limit, and a build that never finished. Listing documents instead costs ~2,100
    entries, and nothing becomes unreachable: a split document's index page lists its sections,
    and every section carries previous/next/up links and is indexed by search.
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
        pages = [p for p in entries if p.is_file() and p.suffix == ".md" and p.name != "index.md"]
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
            if is_split_document(sub):
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


def write_library_index(reference_dir, slugs, apply):
    """The landing page: one entry per source, not one per document.

    Built from the lockfile's slugs rather than by finding every `index.md` on disk — a split
    document has an index of its own, and listing those here turned the page into a flat list
    of four hundred lectures, which is the thing the nav exists to avoid.
    """
    if not reference_dir.is_dir():
        return
    entries = []
    for entry in sorted(slugs, key=lambda e: (e.get("subject") or "", e["slug"])):
        idx = output_path(entry, reference_dir.parent) / "index.md"
        if idx.exists():
            rel = idx.relative_to(reference_dir).as_posix()
            entries.append((entry.get("subject") or "unsorted", read_title(idx), rel))

    body = [
        "---", "title: Home", "---", "",
        "# Study reference library", "",
        "Course material, lecture notes, transcripts and papers converted to markdown and split",
        "by section, so that every part of them can be linked to. The companion to the",
        "[study knowledge base](https://github.com/Claptar/knowledge-base), which holds the notes",
        "themselves — the split is by authorship, not by subject.",
        "",
        "> **Converted, not adapted.** The text is its author's, reformatted. Every page cites its",
        "> source and links to the original, and says which route converted it — a page built from",
        "> a PDF carries a warning, because prose survives a PDF and mathematics does not. These",
        "> files are generated and are **never edited by hand**.",
        "",
        f"**{len(entries)} source{'s' if len(entries) != 1 else ''} converted**, by discipline. "
        "Books and paywalled papers are deliberately absent.",
        "",
        "## Sources", "",
    ]
    if entries:
        current = None
        for subject, title, href in entries:
            if subject != current:
                body += ["", f"### {prettify(subject)}", ""]
                current = subject
            body.append(f"- [{title}]({href})")
    else:
        body.append("*(none yet)*")
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
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    published_root = LIBRARY / "docs"
    lock = load_lock(a.sources)
    by_slug = {e["slug"]: e for e in lock.get("sources", [])}

    if a.summary_only:
        write_library_index(published_root, by_slug.values(), a.apply)
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

    results = [process(e, a.sources, LIBRARY, a.include_all, a.apply) for e in entries]

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

    if a.apply:
        write_library_index(published_root, by_slug.values(), True)
        n = write_nav(published_root, True)
        print(f"\nwrote {tot['parts']} pages; nav has {n} entries")
    else:
        print("\nDry run. Re-run with --apply to write.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
