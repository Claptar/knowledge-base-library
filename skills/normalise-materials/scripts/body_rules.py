#!/usr/bin/env python3
"""The body of a converted page, normalised.

`references/page-template.md` § *The body* is the specification; this is the implementation.

It is the stage the converter never had. `page()` used to interpolate `body.strip()` verbatim
between the banner and the footer, which is how 11,918 pages came to hold 166,030 raw HTML tags,
14,001 stray page numbers and 5,804 duplicate title levels. Every rule here is mechanical: none of
them requires understanding the mathematics, and none of them rewrites a sentence. Rewriting is
`adapt-material`'s job, next door, and the difference is the whole reason this repository exists.

Fenced and inline code is protected before anything else happens and restored last, so no rule can
reach inside a code block.

    from body_rules import normalise_body, protect_math_spans, restore_math
    body = normalise_body(raw, title="Lecture 7", route="pandoc-html")
"""

from __future__ import annotations

import re

# --- maths hidden inside rendered HTML ------------------------------------------------------------
# Pandoc's HTML reader does NOT parse <span class="math">\(x\)</span> as mathematics. It treats the
# payload as literal text and escapes the backslashes, so `\(n\to\infty\)` arrives as `\\(n\\to
# \\infty\\)`. The old converter then ran a blind \[ -> $$ substitution over that escaped output,
# which is precisely what turned \EE\[\theta_i \mid X\] into \EE\[\theta_i \mid X$$ on 360 pages.
#
# So the mathematics is lifted out before pandoc sees the document and put back afterwards,
# untouched. Verified on sources/berkeley-stat210a/fall-2025/homework.html.
MATH_SPAN = re.compile(
    r'<span class="math\s+(inline|display)"[^>]*>\s*(?:\\\(|\\\[)?(.*?)(?:\\\)|\\\])?\s*</span>',
    re.S)
MATH_TOKEN = re.compile(r"@@MATH(\d+)@@")


def protect_math_spans(html: str) -> tuple[str, list]:
    store: list[tuple[str, str]] = []

    def take(m):
        store.append((m.group(1), m.group(2).strip()))
        return f"@@MATH{len(store) - 1}@@"

    return MATH_SPAN.sub(take, html), store


def restore_math(md: str, store: list) -> str:
    def put(m):
        kind, tex = store[int(m.group(1))]
        return f"${tex}$" if kind == "inline" else f"\n\n$$\n{tex}\n$$\n\n"

    return MATH_TOKEN.sub(put, md)


# --- knitr's LaTeX code highlighting ---------------------------------------------------------------
# knitr writes R code into LaTeX as \begin{Shaded}\begin{Highlighting}[] with every token wrapped
# in a \NormalTok{...} / \KeywordTok{...} macro. Pandoc's LaTeX reader does not know those macros,
# so it renders the code as **bold prose**: `m1 <- **lm**(lpsa ** ** 1, data = prostate)`. Rewriting
# the environment as `verbatim`, which the reader does understand, recovers a real code block.
# 281 such blocks in one statomics deck alone.
SHADED = re.compile(r"\\begin\{Shaded\}\s*\\begin\{Highlighting\}(?:\[[^\]]*\])?\s*(.*?)"
                    r"\s*\\end\{Highlighting\}\s*\\end\{Shaded\}", re.S)
TOK = re.compile(r"\\[A-Za-z]+Tok\{([^{}]*)\}")
TEX_UNESCAPE = ((r"\\textbackslash(?:\{\})?", r"\\\\"),
                (r"\\textquotesingle(?:\{\})?", "'"),
                (r"\\textasciitilde(?:\{\})?", "~"),
                (r"\\textasciicircum(?:\{\})?", "^"),
                (r"\\textless(?:\{\})?", "<"),
                (r"\\textgreater(?:\{\})?", ">"),
                (r"\\ldots(?:\{\})?", "..."),
                (r"\\([_${}&%#])", r"\1"))


def _detokenise(block: str) -> str:
    prev = None
    while prev != block:                       # innermost first, so nested macros unwrap cleanly
        prev, block = block, TOK.sub(r"\1", block)
    for pat, rep in TEX_UNESCAPE:
        block = re.sub(pat, rep, block)
    return block


def pre_tex(tex: str) -> str:
    """Prepare a .tex file for pandoc. Mechanical, and applied before the reader sees it."""
    return SHADED.sub(
        lambda m: "\\begin{verbatim}\n" + _detokenise(m.group(1)) + "\n\\end{verbatim}", tex)


# --- protecting code ------------------------------------------------------------------------------

FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
CODE_TOKEN = re.compile(r"@@CODE(\d+)@@")


LIST_ITEM = re.compile(r"^\s*([-*+]|\d+[.)])\s")


def _fence_indented(text: str) -> str:
    """Turn pandoc's indented code blocks into fenced ones.

    Pandoc's markdown writer emits indented code however `backtick_code_blocks` is set, and an
    indented block is invisible to anything scanning for fences -- which is how `borstkanker$S100A8`
    (R's column accessor) was counted as an unclosed maths delimiter on twelve pages. Fencing it
    makes the code unambiguous to every later rule, and it is what page-template.md asks for.

    A run indented under a list marker is a list continuation, not code, and is left alone."""
    lines, out, i = text.splitlines(), [], 0
    while i < len(lines):
        blank_before = not out or not out[-1].strip()
        prev_real = next((l for l in reversed(out) if l.strip()), "")
        if (blank_before and lines[i].startswith("    ") and lines[i].strip()
                and not LIST_ITEM.match(prev_real) and not prev_real.startswith("    ")):
            j = i
            while j < len(lines) and (lines[j].startswith("    ") or not lines[j].strip()):
                j += 1
            while j > i and not lines[j - 1].strip():
                j -= 1
            out.append("```")
            out.extend(l[4:] for l in lines[i:j])
            out.append("```")
            i = j
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


SVG_BLOCK = re.compile(r"<figure\b.*?</figure>|<svg\b.*?</svg>", re.S | re.I)
SVG_TOKEN = re.compile(r"@@SVG(\d+)@@")


NAMED_ENTITY = re.compile(r"&([a-zA-Z][a-zA-Z0-9]*);")


def tidy_svg(text: str) -> str:
    """Make inline SVG figures strict-XML clean, and better to read while we are here.

    Nothing here is fixing a rendering bug: a browser parses SVG-in-HTML by HTML rules, so
    `&Omega;` and a `<=` inside an aria-label both render correctly today. They are fixed because
    they are fragile -- any strict-XML tool downstream chokes -- and because `\u2264` is simply the
    right character for "less than or equal" in a label. Deterministic, no model involved."""
    import html.entities

    def one(block: str) -> str:
        # `<=` and `>=` are comparisons in labels and comments, never tag syntax. As characters
        # they are unambiguous to every parser and read better than the ASCII digraph.
        block = block.replace("<=", "\u2264").replace(">=", "\u2265")

        def ent(m):
            name = m.group(1)
            cp = html.entities.name2codepoint.get(name)
            return f"&#{cp};" if cp else m.group(0)

        block = NAMED_ENTITY.sub(ent, block)
        # a bare & that is not already an entity
        return re.sub(r"&(?![a-zA-Z][a-zA-Z0-9]*;|#\d+;|#x[0-9a-fA-F]+;)", "&amp;", block)

    return SVG_BLOCK.sub(lambda m: one(m.group(0)), text)


def _protect_svg(text: str) -> tuple[str, list]:
    """Inline SVG figures survive the no-raw-HTML rule. Deliberately, and only these.

    The rule exists because extractor debris -- `<br>`, `<sup>`, `<span>` -- makes markdown
    unreadable as plain text. A diagram is the opposite: it is content that cannot be written any
    other way. It has to be INLINE rather than an `![](x.svg)` image because only inline SVG
    inherits the page's foreground through `currentColor`, and the site has a light/dark toggle --
    an external SVG with baked-in strokes is invisible in one of the two themes."""
    store = []

    def take(m):
        store.append(m.group(0))
        return f"@@SVG{len(store) - 1}@@"

    return SVG_BLOCK.sub(take, text), store


def _restore_svg(text: str, store: list) -> str:
    return SVG_TOKEN.sub(lambda m: store[int(m.group(1))], text)


def _protect_code(text: str) -> tuple[str, list]:
    store, out, buf, fence = [], [], None, None
    for line in text.splitlines():
        m = FENCE.match(line)
        if buf is None and m:
            fence, buf = m.group(1)[0], [line]
            continue
        if buf is not None:
            buf.append(line)
            if m and line.strip().startswith(fence * 3):
                store.append("\n".join(buf))
                out.append(f"@@CODE{len(store) - 1}@@")
                buf = None
            continue
        out.append(line)
    if buf is not None:                       # unterminated fence: close it rather than lose it
        store.append("\n".join(buf) + "\n```")
        out.append(f"@@CODE{len(store) - 1}@@")
    text = "\n".join(out)

    def take_inline(m):
        store.append(m.group(0))
        return f"@@CODE{len(store) - 1}@@"

    return re.sub(r"`[^`\n]+`", take_inline, text), store


def _restore_code(text: str, store: list) -> str:
    return CODE_TOKEN.sub(lambda m: store[int(m.group(1))], text)


# --- raw HTML -------------------------------------------------------------------------------------

PICTURE_TEXT = re.compile(
    r"<!--\s*Start of picture text\s*-->.*?<!--\s*End of picture text\s*-->\s*", re.S)
ENTITIES = {"&lt;": "<", "&gt;": ">", "&amp;": "&", "&quot;": '"', "&nbsp;": " ",
            "&#39;": "'", "&apos;": "'"}
SUPSUB = re.compile(r"<(sup|sub)>(.*?)</\1>", re.S)
ANCHOR = re.compile(r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.S | re.I)
FOOTNOTE_ANCHOR = re.compile(r'<a\s[^>]*href="#fn\d+"[^>]*>.*?</a>', re.S | re.I)
UNWRAP = re.compile(r"</?(span|div|section|p|em|strong|i|b|small|font|a|figure|figcaption)\b[^>]*>",
                    re.I)
ANY_TAG = re.compile(r"</?[a-zA-Z][^>]*>")
# detached accents and replacement characters: PDF glyph debris, never content
GLYPH_DEBRIS = {"ˆ", "\ufffd", "˜", "¨", "˙", "`", "´"}


def _supsub(m: re.Match) -> str:
    kind, inner = m.group(1).lower(), m.group(2).strip()
    inner = ANY_TAG.sub("", inner)
    if not inner or inner in GLYPH_DEBRIS or all(c in GLYPH_DEBRIS for c in inner):
        return ""
    if len(inner) > 12:
        return inner
    mark = "^" if kind == "sup" else "_"
    return f"${mark}{{{inner}}}$"


def _strip_html(text: str) -> str:
    text = PICTURE_TEXT.sub("", text)
    for ent, char in ENTITIES.items():
        text = text.replace(ent, char)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = SUPSUB.sub(_supsub, text)
    text = FOOTNOTE_ANCHOR.sub("", text)
    # Only absolute hrefs become links. This runs AFTER normalise_source.rewrite_links, so a
    # RELATIVE href turned into markdown here is never resolved against the source tree and lands
    # in the site as a dangling link -- `<a href="files/syllabus.pdf">` did exactly that, and the
    # strict build caught it. There is nothing to resolve it to at this stage, so it becomes text.
    text = ANCHOR.sub(
        lambda m: (f"[{ANY_TAG.sub('', m.group(2)).strip()}]({m.group(1)})"
                   if re.match(r"(https?:|mailto:)", m.group(1))
                   else ANY_TAG.sub('', m.group(2)).strip()), text)
    text = UNWRAP.sub("", text)
    text = re.sub(r"</?(table|thead|tbody|tr|th|td|ol|ul|li|h[1-6]|pre|code)\b[^>]*>", " ", text,
                  flags=re.I)
    return ANY_TAG.sub("", text)


# --- mathematics delimiters and escaping ------------------------------------------------------------

LATEX_INLINE = re.compile(r"\\+\((.+?)\\+\)", re.S)
TEXISH = re.compile(r"\\[a-zA-Z]{2,}|[_^]\{|\\frac|\\sum|\\int|\\mathbb|\\left|\\right")
ESCAPES = ((r"\\\$", "$"), (r"\\_", "_"), (r"\\\*", "*"),
           (r"\\\[", "["), (r"\\\]", "]"), (r"\\#", "#"), (r"\\&", "&"))


def _display_math(para: str) -> str:
    """Convert a paragraph's outer \\[ ... \\] to $$ ... $$.

    Matched first-open to LAST-close within the paragraph, never lazily. A lazy match stops at the
    first \\] it meets, which in `\\EE\\[\\theta_i \\mid X\\] = ...` is the closing bracket of
    \\EE[...], not the end of the equation -- the exact mistake that left 107 display blocks with no
    closing delimiter."""
    opens = [m.start() for m in re.finditer(r"\\\[", para)]
    closes = [m.start() for m in re.finditer(r"\\\]", para)]
    if not opens or not closes or closes[-1] <= opens[0]:
        return para
    inner = para[opens[0] + 2:closes[-1]]
    if not TEXISH.search(inner):
        return para
    return para[:opens[0]] + f"\n\n$$\n{inner.strip()}\n$$\n\n" + para[closes[-1] + 2:]


ESCAPED_PAIR = re.compile(r"\\\$(.+?)\\\$", re.S)
# A `\$` is an escaped dollar, not the start of mathematics. Excluding it from the opening
# lookbehind is what stops a price from opening a region that runs to the next real `$`.
MATH_REGION = re.compile(r"\$\$.*?\$\$|(?<![\$\\])\$(?!\$).+?(?<![\$\\])\$(?!\$)", re.S)


def _unescape_math(region: str) -> str:
    for esc, plain in ESCAPES:
        region = re.sub(esc, plain, region)
    return region


def _maths(text: str) -> str:
    out = []
    for para in text.split("\n\n"):
        para = _display_math(para)
        para = LATEX_INLINE.sub(lambda m: f"${m.group(1).strip()}$", para)
        # Pandoc escapes the delimiters of mathematics it failed to parse, so `\$x\$` is a mangled
        # `$x$`. A LONE `\$` is a price, and unescaping it would open a math span that never
        # closes -- so only balanced pairs around TeX-looking content are repaired.
        para = ESCAPED_PAIR.sub(
            lambda m: f"${m.group(1)}$" if TEXISH.search(m.group(1)) else m.group(0), para)
        # Everything else is unescaped only INSIDE mathematics, where `\theta\_i` is damage.
        # Outside it, `snake\_case` and `2 \* 3` are correct markdown and are left alone.
        para = MATH_REGION.sub(lambda m: _unescape_math(m.group(0)), para)
        # `\[91.9, 147\]mmHg` is a literal bracket pandoc escaped, not a display-maths delimiter.
        # It renders as a bracket either way, but leaving backslashes in the text makes the
        # markdown unreadable as plain text, which this repo is first. A `\](` is left alone in
        # case it is a link.
        para = re.sub(r"\\\[", "[", para)
        para = re.sub(r"\\\](?!\()", "]", para)
        out.append(para)
    return "\n\n".join(out)


CURRENCY_DOUBLED = re.compile(r"\$\$(\d[\d,.]*)\$")
VALID_MATH = re.compile(r"\$\$.*?\$\$|(?<![\$\\])\$(?!\$)(?:\\.|[^$\\])+?(?<![\$\\])\$(?!\$)",
                        re.S)


def unmatched_dollars(text: str) -> int:
    """Dollar signs that are neither escaped nor part of a valid maths span.

    Exported so that the converter's repair and the validator's gate agree by construction. They
    used to carry separate regexes that disagreed about whether `\\$` could close a span, so the
    repair fixed pages the gate still failed."""
    covered = bytearray(len(text))
    for m in VALID_MATH.finditer(text):
        for i in range(m.start(), m.end()):
            covered[i] = 1
    return sum(1 for i, ch in enumerate(text)
               if ch == "$" and not covered[i] and (i == 0 or text[i - 1] != "\\"))


def _fix_stray_dollars(text: str) -> str:
    """Escape dollar signs that are money, not mathematics.

    Statistics problem sets are full of prices, and a model transcribing one writes `$50 million`
    or `$$4$`. Both open a maths span that never closes, and an unclosed span swallows the rest of
    the page -- seventeen pages in one course before this rule existed.

    The test is structural rather than lexical: valid `$...$` and `$$...$$` spans are located
    first, and only the dollars left over are escaped. A `$` that is doing real work is never
    touched, whatever follows it."""
    text = CURRENCY_DOUBLED.sub(r"\\$\1", text)
    out, last = [], 0
    spans = [(m.start(), m.end()) for m in VALID_MATH.finditer(text)]
    covered = bytearray(len(text))
    for a, b in spans:
        for i in range(a, b):
            covered[i] = 1
    for i, ch in enumerate(text):
        if ch == "$" and not covered[i] and (i == 0 or text[i - 1] != "\\"):
            out.append(text[last:i] + "\\$")
            last = i + 1
    out.append(text[last:])
    return "".join(out)


# Pandoc renders a LaTeX \ref{} to a non-heading label as `[[eq:biasvar]](#eq:biasvar)` -- a
# nested-bracket link whose target is an equation label, not a heading. It cannot resolve once the
# document is split, and it never could: there is no such anchor on any page. The link markup is
# dropped and the label kept as text, which is what a reader can actually use. 25 strict-build
# failures, and the ordinary link regex never matched the form at all because of the inner bracket.
CROSSREF = re.compile(r"\[\[([^\]\[]+)\]\]\(#[^)\s]+\)")


def _crossrefs(text: str) -> str:
    return CROSSREF.sub(lambda m: m.group(1), text)


# --- extraction debris ------------------------------------------------------------------------------

BARE_NUMBER = re.compile(r"^\s*\(?\d{1,4}\)?\s*$")
PAGE_MARKER = re.compile(r"^\s*(page\s+\d+(\s+of\s+\d+)?|\d+\s+of\s+\d+|\d+\s*/\s*\d+)\s*$", re.I)
HYPHEN_BREAK = re.compile(r"([a-z])-\n([a-z])")


def _debris(text: str) -> str:
    keep = [l for l in text.splitlines()
            if not (BARE_NUMBER.match(l) or PAGE_MARKER.match(l))]
    text = "\n".join(keep)
    return HYPHEN_BREAK.sub(r"\1\2", text)


def _running_headers(text: str) -> str:
    """A line repeated many times at the top or bottom of a page is a running header, not content."""
    lines = text.splitlines()
    counts: dict[str, int] = {}
    for l in lines:
        s = l.strip()
        if 3 < len(s) < 80 and not s.startswith(("#", "|", ">", "-", "*", "!", "$")):
            counts[s] = counts.get(s, 0) + 1
    repeated = {s for s, n in counts.items() if n >= 5}
    if not repeated:
        return text
    return "\n".join(l for l in lines if l.strip() not in repeated)


# --- headings ---------------------------------------------------------------------------------------

HEADING = re.compile(r"^(#{1,6})[ \t]*(.*?)[ \t]*#*$")


def _headings(text: str, title: str | None) -> str:
    rows = []
    for i, line in enumerate(text.splitlines()):
        m = HEADING.match(line)
        rows.append((i, len(m.group(1)), m.group(2).strip()) if m else None)

    # Decide what goes before measuring what is left, or a dropped title level keeps its rung on
    # the ladder and every heading below it stays one level too deep.
    cleaned, drop = {}, set()
    for r in rows:
        if not r:
            continue
        i, lvl, txt = r
        txt = re.sub(r"^\*\*(.+?)\*\*$", r"\1", txt).strip()   # bold carrying structure
        txt = re.sub(r"^\*(.+?)\*$", r"\1", txt).strip()
        # `## 7.1 Inleiding {#inleiding}` is the title repeated, but the trailing attribute
        # carries an anchor other pages may link to -- so it is dropped only when there is no
        # anchor to lose. The strict build is the check on that.
        bare = re.sub(r"\s*\{[^}]*\}\s*$", "", txt).strip()
        if not bare:
            drop.add(i)
            continue
        if title and bare.casefold() == title.casefold() and bare == txt:
            drop.add(i)
            continue
        cleaned[i] = (lvl, txt)

    levels = sorted({lvl for lvl, _ in cleaned.values()})
    if not levels:
        return "\n".join(l for i, l in enumerate(text.splitlines()) if i not in drop)

    # Demote so the shallowest body heading is ##, closing any gap in the ladder, so that a source
    # rooted at # and one rooted at ## produce the same-looking page.
    ladder = {lvl: min(6, i + 2) for i, lvl in enumerate(levels)}

    out = text.splitlines()
    for i, (lvl, txt) in cleaned.items():
        out[i] = f"{'#' * ladder[lvl]} {txt}"
    return "\n".join(l for i, l in enumerate(out) if i not in drop)


# --- the pipeline -------------------------------------------------------------------------------------

BLANKS = re.compile(r"\n{3,}")
TRAILING_WS = re.compile(r"[ \t]+$", re.M)


def normalise_body(text: str, *, title: str | None = None, route: str = "") -> str:
    """Apply every rule in page-template.md § The body. Order matters.

    Code is protected first and restored last, so nothing below can reach into a code block."""
    text, svg = _protect_svg(text)
    text = _fence_indented(text)
    text, code = _protect_code(text)
    text = _strip_html(text)
    text = _maths(text)
    text = _crossrefs(text)
    text = _fix_stray_dollars(text)
    text = _debris(text)
    if route in ("pdf", "llm") or route.startswith("llm-"):
        text = _running_headers(text)
    text = _headings(text, title)
    text = TRAILING_WS.sub("", text)
    text = BLANKS.sub("\n\n", text)
    text = _restore_code(text, code)
    text = _restore_svg(text, svg)
    return text.strip() + "\n"


# --- titles ----------------------------------------------------------------------------------------

SCREAMING = re.compile(r"^[^a-z]{6,}$")


def normalise_title(raw: str) -> str:
    """`INTRODUCTION - PART I` -> `Introduction — Part I`. Screaming caps never ship."""
    t = ANY_TAG.sub("", raw).strip().strip("*_# ")
    t = re.sub(r"\s+", " ", t)
    if SCREAMING.match(t) and len(t) > 5:
        t = t.title()
    return re.sub(r"\s+[-–]\s+", " — ", t)


if __name__ == "__main__":
    sample = """# Lecture 7

### **2.1 The two perspectives**

4

Some prose with <br>a break and x<sup>2</sup> and a <span class="cite">span</span>.

Page 12

The estimator \\[ \\EE\\[\\theta\\_i \\mid X\\] = \\frac{\\tau^2}{1+\\tau^2} X\\_i \\] is Bayes.

<!-- Start of picture text -->Interpretations<br>of<br>Probability<!-- End of picture text -->

```python
x = 1  # <sup>not</sup> touched, page 12, 4
```

Inline \\(n \\to \\infty\\) and an escaped \\$5 price.
"""
    print(normalise_body(sample, title="Lecture 7", route="pdf"))
