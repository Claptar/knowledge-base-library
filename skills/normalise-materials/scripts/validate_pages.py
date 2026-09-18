#!/usr/bin/env python3
"""Quality gates for converted pages.

`references/quality-gates.md` is the specification; this is the implementation, and the two are
meant to be read together. It runs in two places, and they are deliberately the same code:

    - inside normalise_source.py, as the publish decision for a candidate page;
    - over docs/ in CI, beside `mkdocs build --strict`, where it must report zero fatal findings.

The strict build is not a quality check. It validates links and anchors, and it passed cleanly on a
corpus where 373 pages showed the reader raw `<span class="math inline">\\$\\\\tau^2\\$</span>`.
That is the hole this closes.

    python3 validate_pages.py docs/ --report
    python3 validate_pages.py docs/probability --report --verbose
    python3 validate_pages.py docs/ --json findings.json

Exit status is 1 if any fatal finding survives, so CI can gate on it.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

# --- what counts as a page ----------------------------------------------------------------------

SUBSTANCE_FLOOR = 400          # characters of real body text; below this there is no page here
DEBRIS_LINE_RATIO = 0.20       # above this the document is scanned or column-scrambled past saving
HTML_TAG_BUDGET = 0            # raw HTML in a body is always a repair, never tolerated

FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})", re.M)
HEADING = re.compile(r"^(#{1,6})[ \t]*(.*?)[ \t]*#*\s*$", re.M)
BARE_NUMBER = re.compile(r"^\s*\(?\d{1,4}\)?\s*$")
PAGE_MARKER = re.compile(r"^\s*(page\s+\d+|\d+\s+of\s+\d+|\d+\s*/\s*\d+)\s*$", re.I)
PICTURE_TEXT = re.compile(r"<!--\s*Start of picture text\s*-->")
MATH_SPAN = re.compile(r"<span class=\"math")
LATEX_PAREN = re.compile(r"\\\(|\\\)")
LATEX_BRACKET = re.compile(r"\\\[|\\\]")
ESCAPED_DOLLAR = re.compile(r"\\\$")
TEX_COMMAND = re.compile(r"\\(?:frac|sum|int|mathbb|theta|tau|alpha|beta|sigma|mu|left|right|begin|cdot|times|leq|geq|infty)\b")
ESCAPED_UNDERSCORE = re.compile(r"\\_")
ESCAPED_STAR = re.compile(r"\\\*")
ENTITY = re.compile(r"&(lt|gt|amp|quot|#\d+);")
SVG_FIGURE = re.compile(r"<figure\b.*?</figure>|<svg\b.*?</svg>", re.S | re.I)
HTML_TAG = re.compile(r"</?(br|sup|sub|span|div|td|tr|table|section|a|img|p|ol|ul|li|i|b|em|strong)\b[^>]*>", re.I)
FOOTNOTE_REF = re.compile(r"\[\^([^\]]+)\]")
FOOTNOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:", re.M)
NOT_AN_IMAGE = re.compile(r"!\[[^\]]*\]\(\s*<?[^)]*\.(pdf|html?|docx?)\b", re.I)
DOUBLED_SUFFIX = re.compile(r"-(transcript|slides|solutions|questions|exam|compiled)-\1\b")
DISPLAY_MATH = re.compile(r"\$\$.*?\$\$", re.S)
INLINE_MATH = re.compile(r"(?<!\$)\$(?!\$)(?:\\.|[^$\\])+?\$(?!\$)", re.S)

# Severity
FATAL = "fatal"
REPAIR = "repair"


@dataclass
class Finding:
    gate: str
    severity: str
    count: int
    sample: str = ""

    def __str__(self) -> str:
        s = f"  {self.severity:6} {self.gate:34} x{self.count}"
        return s + (f"   {self.sample}" if self.sample else "")


@dataclass
class PageReport:
    path: Path
    findings: list[Finding] = field(default_factory=list)
    route: str = ""
    body_hash: str = ""
    body_chars: int = 0

    @property
    def fatal(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == FATAL]

    @property
    def ok(self) -> bool:
        return not self.fatal


# --- decomposing a page -------------------------------------------------------------------------

def split_frontmatter(text: str) -> tuple[dict, str]:
    """Front matter as a flat dict of strings, and the rest. Deliberately not yaml: this script is
    a CI gate and should not need the convert dependency group installed to run."""
    m = FRONTMATTER.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#", "-")):
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip("'\"")
    return meta, text[m.end():]


def strip_code(text: str) -> str:
    """Blank out fenced blocks and inline spans, preserving line count so offsets stay usable."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        if in_fence or (line.startswith("    ") and line.strip()):
            out.append("")                     # fenced or indented: both are code
            continue
        out.append(re.sub(r"`[^`\n]+`", "", line))
    return "\n".join(out)


def body_of(text: str) -> str:
    """The body: front matter, provenance banner, H1 and footer removed.

    This is what a reader actually reads, and it is what the substance floor and the duplicate hash
    are computed over. Counting the banner would make every empty page look substantial -- which is
    exactly how 3,089 pages with no content passed for conversions."""
    _, rest = split_frontmatter(text)
    lines = rest.splitlines()

    # leading blockquote banner(s) and blank lines
    i = 0
    while i < len(lines) and (not lines[i].strip() or lines[i].lstrip().startswith(">")):
        i += 1
    # the old two-part header: a "**Source:**" line and/or an admonition block
    while i < len(lines) and (lines[i].startswith("**Source:**") or lines[i].startswith("!!! ")
                              or (lines[i].startswith("    ") and i and lines[i - 1].strip())
                              or not lines[i].strip()):
        if lines[i].startswith("!!! ") or lines[i].startswith("**Source:**"):
            i += 1
            while i < len(lines) and (lines[i].startswith("    ") or not lines[i].strip()):
                i += 1
        elif not lines[i].strip():
            i += 1
        else:
            break
    # the H1
    if i < len(lines) and lines[i].startswith("# "):
        i += 1
    lines = lines[i:]

    # trailing footer: a `---` rule followed by a nav line
    for j in range(len(lines) - 1, max(len(lines) - 8, -1), -1):
        if lines[j].strip() == "---":
            tail = "\n".join(lines[j + 1:])
            if "Up:" in tail or "←" in tail or "→" in tail:
                lines = lines[:j]
                break
    return "\n".join(lines).strip()


def substance(body: str) -> int:
    """Characters of prose: headings, images, tables and code excluded."""
    text = strip_code(body)
    keep = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("![") or s.startswith("|") or s == "---":
            continue
        if BARE_NUMBER.match(s) or PAGE_MARKER.match(s):
            continue
        keep.append(s)
    return len("".join(keep))


DEBRIS_EXEMPT = re.compile(r"^\s*(?:[-*+>#|!\[`]|\(?[a-zA-Z0-9]{1,3}[.)]\s)")


def is_debris(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if BARE_NUMBER.match(s) or PAGE_MARKER.match(s):
        return True
    if PICTURE_TEXT.search(s) or s.startswith("<!-- End of picture text"):
        return True
    # Anything short BY DESIGN is content, not wreckage. Without this the rule condemns exactly
    # the material worth keeping: a multiple-choice question is a run of four-character options,
    # and it rejected eight pages of a probability exam as OCR noise.
    if "$" in s or DEBRIS_EXEMPT.match(s):
        return False
    # a short fragment with no verb-like structure, typical of column-scrambled OCR
    if len(s) < 25 and " " in s:
        return s.count(" ") <= 3 and not s.endswith((".", ":", "?", "!", ";", ","))
    return False


# --- the gates ----------------------------------------------------------------------------------

def unbalanced_dollars(clean: str) -> bool:
    # One implementation, shared with the converter's repair. See body_rules.unmatched_dollars.
    from body_rules import unmatched_dollars
    return unmatched_dollars(clean) > 0


def unbalanced_fences(text: str) -> bool:
    return len([1 for line in text.splitlines() if FENCE.match(line)]) % 2 == 1


def check(path: Path, text: str) -> PageReport:
    meta, _ = split_frontmatter(text)
    body = body_of(text)
    clean = strip_code(body)
    # An inline SVG figure is a drawing, and its labels are not prose. A `$1` price in a diagram
    # is not an unmatched maths delimiter, and the numeric entities tidy_svg deliberately produces
    # inside one are not debris to repair -- counting them rejected a correct chapter as FATAL.
    prose = SVG_FIGURE.sub("", clean)
    rep = PageReport(path=path, route=meta.get("route", ""),
                     body_hash=hashlib.sha256(body.encode()).hexdigest(),
                     body_chars=substance(body))

    def add(gate, severity, count, sample=""):
        if count:
            rep.findings.append(Finding(gate, severity, count, sample))

    # fatal -- nothing publishable here
    add("math-span", FATAL, len(MATH_SPAN.findall(clean)), "MathJax scaffolding reached markdown")
    add("picture-text", FATAL, len(PICTURE_TEXT.findall(text)), "figure destroyed into OCR fragments")
    if unbalanced_dollars(prose):
        add("unbalanced-dollars", FATAL, 1, "an odd $ swallows the rest of the page")
    if unbalanced_fences(body):
        add("unbalanced-fences", FATAL, 1, "code fence opened and not closed")
    # A contents page is navigation: links and headings, little prose by design. Holding it to the
    # substance floor rejects exactly the pages whose job is to help a reader find the others.
    is_index = path.name == "index.md"
    if not is_index and rep.body_chars < SUBSTANCE_FLOOR:
        add("thin-body", FATAL, 1, f"{rep.body_chars} chars of prose, floor is {SUBSTANCE_FLOOR}")
    # The library's own front page is navigation it generated, not someone else's material, so
    # there is no original for it to link to. Every SOURCE's contents page is still held to this.
    is_library_root = path.parent.name == "docs" and path.name == "index.md"
    if not meta.get("source") and not is_library_root:
        add("uncited", FATAL, 1, "no source URL in front matter")
    lines = [l for l in body.splitlines() if l.strip()]
    if lines:
        ratio = sum(1 for l in lines if is_debris(l)) / len(lines)
        if ratio > DEBRIS_LINE_RATIO:
            add("extraction-debris", FATAL, int(ratio * 100), f"{ratio:.0%} of lines are debris")

    # repair -- the converter fixes these and the page ships
    add("latex-paren", REPAIR, len(LATEX_PAREN.findall(prose)), r"\( \) instead of $ $")
    add("latex-bracket", REPAIR, len(LATEX_BRACKET.findall(prose)), r"\[ \] instead of $$ $$")
    # `\$` is CORRECT for a price, and the body pipeline deliberately produces it so that a
    # `$50 million` cannot open a maths span. It is only suspicious next to TeX, where it suggests
    # a delimiter the extractor escaped rather than a currency symbol.
    add("escaped-dollar", REPAIR,
        sum(1 for line in clean.splitlines()
            for _ in ESCAPED_DOLLAR.findall(line) if TEX_COMMAND.search(line)))
    add("escaped-underscore", REPAIR, len(ESCAPED_UNDERSCORE.findall(clean)))
    add("escaped-star", REPAIR, len(ESCAPED_STAR.findall(clean)))
    add("html-entity", REPAIR, len(ENTITY.findall(prose)))
    # An inline SVG figure is a diagram, which is content; the no-raw-HTML rule is about
    # extractor debris. See body_rules._protect_svg for why it must be inline rather than an image.
    tags = HTML_TAG.findall(SVG_FIGURE.sub("", clean))
    if len(tags) > HTML_TAG_BUDGET:
        add("raw-html", REPAIR, len(tags), ", ".join(f"<{t}>" for t, _ in Counter(tags).most_common(3)))
    # from `clean`, not `body`: a `#dosis wordt...` comment inside an R block is not a heading,
    # and counting it as one reported 5,804 phantom duplicate title levels.
    heads = HEADING.findall(clean)
    h1 = [h for h in heads if h[0] == "#"]
    add("extra-h1", REPAIR, len(h1), "body re-states a title level")
    add("empty-heading", REPAIR, sum(1 for h in heads if not h[1].strip()))
    add("bold-heading", REPAIR, sum(1 for h in heads if h[1].startswith("**")))
    # over `clean`: a bare `4` inside an R block is output, not a page number, and a trailing
    # hyphen inside code is an operator.
    add("page-number-line", REPAIR,
        sum(1 for l in clean.splitlines() if BARE_NUMBER.match(l) or PAGE_MARKER.match(l)))
    add("hyphen-break", REPAIR, sum(1 for l in clean.splitlines() if re.search(r"[a-z]-$", l)))
    add("not-an-image", REPAIR, len(NOT_AN_IMAGE.findall(body)))
    add("doubled-suffix", REPAIR, len(DOUBLED_SUFFIX.findall(str(path))))
    defs = set(FOOTNOTE_DEF.findall(body))
    orphans = [r for r in FOOTNOTE_REF.findall(body) if r not in defs]
    add("orphan-footnote", REPAIR, len(orphans))
    return rep


# --- running over a tree ------------------------------------------------------------------------

def walk(root: Path):
    if root.is_file():
        yield root
        return
    for p in sorted(root.rglob("*.md")):
        if p.name == "SUMMARY.md":
            continue
        yield p


TERM_DIR = re.compile(
    r"^(?:(?:fall|spring|summer|winter|autumn|au)[-_]?[a-z]?\d{2,4}|\d{4}(?:-\d{2,4})?"
    r"|[a-z0-9-]*(?:fall|spring|summer|winter)-\d{4})$", re.I)


def _source_of(path: Path, root: Path) -> str:
    """The source a page belongs to — discipline/provider/course, plus the term if there is one.

    The term matters: the lockfile treats `berkeley-stat210a/fall-2025` and `.../fall-2024` as
    separate sources, so a homework reprinted in both is two courses assigning the same sheet, not
    one document converted twice. Stopping at three components called 125 of those a defect."""
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        parts = path.parts
    depth = 4 if len(parts) > 3 and TERM_DIR.match(parts[3]) else 3
    return "/".join(parts[:depth])


def run(root: Path) -> list[PageReport]:
    reports, by_hash = [], defaultdict(list)
    for p in walk(root):
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            rep = PageReport(path=p)
            rep.findings.append(Finding("unreadable", FATAL, 1, "not valid utf-8"))
            reports.append(rep)
            continue
        rep = check(p, text)
        # Index pages are generated navigation and two of them can legitimately coincide; only
        # content pages are compared for duplication.
        if rep.body_chars and p.name != "index.md":
            by_hash[rep.body_hash].append(rep)
        reports.append(rep)
    for group in by_hash.values():
        if len(group) <= 1:
            continue
        keeper = group[0].path
        for dup in group[1:]:
            where = keeper.relative_to(root) if root in keeper.parents else keeper
            # Fatal only WITHIN one source, where it means the same document was converted twice
            # under two paths -- `reader/` and `units/reader/` of the same course. Across sources
            # it is usually correct: Stat 243 assigns the same two papers in eleven course years,
            # and deleting the reading from ten of them would misrepresent those courses.
            same_source = _source_of(dup.path, root) == _source_of(keeper, root)
            dup.findings.append(Finding(
                "duplicate-body", FATAL if same_source else REPAIR, len(group),
                f"same body as {where}" + ("" if same_source else " (another source — expected)")))
    return reports


def report(reports: list[PageReport], root: Path, verbose: bool) -> None:
    fatal_pages = [r for r in reports if not r.ok]
    gates, by_dir = Counter(), Counter()
    routes = Counter(r.route or "(none)" for r in reports)
    for r in reports:
        for f in r.findings:
            gates[(f.severity, f.gate)] += f.count
        if not r.ok:
            try:
                rel = r.path.relative_to(root)
                by_dir["/".join(rel.parts[:3])] += 1
            except ValueError:
                by_dir[str(r.path.parent)] += 1

    print(f"\n{len(reports)} pages under {root}")
    print(f"{len(reports) - len(fatal_pages)} would publish, {len(fatal_pages)} rejected\n")

    print("Gates")
    for severity in (FATAL, REPAIR):
        rows = sorted(((g, c) for (s, g), c in gates.items() if s == severity),
                      key=lambda kv: -kv[1])
        if not rows:
            continue
        print(f"  {severity}")
        for gate, count in rows:
            pages = sum(1 for r in reports for f in r.findings
                        if f.gate == gate and f.severity == severity)
            print(f"    {gate:24} {count:>8,}  in {pages:>6,} pages")

    print("\nRoutes")
    for route, n in routes.most_common():
        print(f"    {route:24} {n:>8,}")

    if by_dir:
        print("\nRejections by source")
        for d, n in by_dir.most_common(15):
            print(f"    {d:56} {n:>7,}")

    if verbose:
        print("\nRejected pages")
        for r in fatal_pages[:200]:
            print(f"\n{r.path}")
            for f in r.fatal:
                print(f)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root", type=Path, nargs="?", default=Path("docs"))
    ap.add_argument("--report", action="store_true", help="print the summary")
    ap.add_argument("--verbose", action="store_true", help="list every rejected page")
    ap.add_argument("--json", type=Path, help="write findings as json")
    args = ap.parse_args()

    if not args.root.exists():
        print(f"no such path: {args.root}", file=sys.stderr)
        return 2

    reports = run(args.root)
    if args.report or args.verbose:
        report(reports, args.root, args.verbose)
    if args.json:
        args.json.write_text(json.dumps([
            {"path": str(r.path), "route": r.route, "body_chars": r.body_chars,
             "findings": [{"gate": f.gate, "severity": f.severity, "count": f.count} for f in r.findings]}
            for r in reports], indent=2))
    return 1 if any(not r.ok for r in reports) else 0


if __name__ == "__main__":
    raise SystemExit(main())
