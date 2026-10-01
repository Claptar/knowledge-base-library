# The shape of a converted page

**This file is the single authority on what a converted page looks like** — the intermediate a book
is written from, and what still ships for a course not yet written as one. A book's chapters and
index are specified in `book-template.md`; this file governs their markdown, not their structure.
`SKILL.md` points here
rather than restating it, and `scripts/normalise_source.py` implements it. When the three disagree,
this file wins and the other two are wrong.

It exists because they *did* disagree: `SKILL.md` documented five front-matter keys while the script
emitted seven, and the body — the part a reader actually reads — was never specified at all. The
converter interpolated whatever the extractor produced between a banner and a footer, which is how
11,918 pages came to have 488 duplicate H1s, 49,666 raw `<br>` tags and 13,225 stray page numbers.

The model for the shape is the knowledge base's own `docs/notes/`, which is the standard he reads
comfortably. What is *not* borrowed from it is the editorial voice — guiding questions, motivation,
summaries. Those are authored, and authoring is `adapt-material`'s job. **This skill preserves; it
does not rewrite.**

## The skeleton

Every converted page, without exception:

```markdown
---
title: "Lecture 7 — Conditional Expectation"
source: https://github.com/berkeley-stat205a/…/lecture07.tex
source_file: sources/berkeley-stat205a/lectures/lecture07.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

> **Converted source.** [`lectures/lecture07.tex`](https://…) — Berkeley Stat 205A, licensed
> CC BY 4.0. Converted 2026-09-14 from `.tex`. The same text in markdown, split so that every part
> has a URL; nothing here is rewritten.

# Lecture 7 — Conditional Expectation

<body>

---

[← Lecture 6](../06-…/) · [Up: contents](../) · [Lecture 8 →](../08-…/)
```

Four parts, in this order, all generated: **front matter**, **provenance banner**, **H1**, **body**,
**footer**. Nothing else may appear above the body.

### Front matter

Exactly these seven keys, in this order, always present:

| key | value |
| --- | --- |
| `title` | the page title, quoted. Cleaned — see *Titles* below |
| `source` | URL of the original **file** where one can be built, else the source's landing page |
| `source_file` | path under `sources/`, so the original is findable locally |
| `licence` | the source's, and therefore this page's. Share-alike propagates |
| `route` | which converter produced it — `markdown`, `pandoc-latex`, `pandoc-html`, `pandoc-rst`, `notebook`, `transcript`, `llm-<model-id>`. Note there is no plain `pdf` route: a PDF that survives re-routing goes through the model, with the deterministic extraction kept as a cross-check. See `quality-gates.md` § *The LLM route* |
| `fidelity` | `lossless`, `high`, `good`, `speech`, `reconstructed` |
| `converted` | ISO date, quoted |

A page with no `source` URL is not published. That is not a formatting rule — the whole arrangement
of republishing other people's material rests on every page citing its original.

### The provenance banner

**One blockquote, immediately after the front matter, before the H1.** It replaces the old
`**Source:** … ·` line *and* the `!!! warning` admonition — one object, not two, and a blockquote
rather than an admonition because that is what `docs/notes/` uses and admonitions are visually loud
enough to compete with the content.

The first sentence is a bolded label naming the route's honesty:

| fidelity | label and what follows |
| --- | --- |
| `lossless`, `high`, `good` | `> **Converted source.** <link> — <provider>, licensed <licence>. Converted <date> from `.<ext>`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.` |
| `speech` | `> **Converted recording.** … This is a transcript of speech, timestamped. Mathematics spoken aloud is left as it was spoken, and whatever was written on the board is not in it.` |
| `lossy` | `> **Converted from PDF — check the mathematics.** … Prose survives a PDF; equations do not. Verify anything symbolic against the original.` |
| `reconstructed` | `> **Reconstructed by a model.** … The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.` |

The `lossy` and `reconstructed` banners are not optional and are never softened to make output look
tidier. A conversion that is merely lossy is honest; one silently improved is not.

### Titles

The title is a short noun phrase, and it is what the nav shows. Rules, in order:

1. Take the source's own heading or document title.
2. Reject junk: form fields (`Student ID (NOT your name):`), anything over 90 characters, anything
   with no letters, anything that is a bare filename or a code fragment.
3. On rejection, fall back to the file stem, prettified.
4. Normalise case: `INTRODUCTION – PART I` → `Introduction — Part I`. Screaming caps never ship.
5. Keep the source's own numbering where it has one — `lecture07`, `chapter03`. It is how he refers
   to the material, and renumbering breaks correspondence with the original.

## The body

**This is the part that was never specified, and every rule here is enforced by the converter rather
than requested of an author.** All of it is mechanical: no rule below requires understanding the
mathematics, and none of them rewrite a sentence.

### Headings

- **Exactly one H1 per page**, and it is the title. Every heading the source carried is demoted so
  that the shallowest body heading is `##`. A source rooted at `#` and one rooted at `##` must
  produce the same-looking page.
- **No empty headings.** A `##` with no text is deleted along with its blank line.
- **No markup carrying structure.** `### **2.1 Introduction**` → `### 2.1 Introduction`. Bold inside
  a heading means the extractor lost a level; recover the level, drop the bold.
- **No heading-level jumps** of more than one on the way down. `##` followed by `####` becomes `##`
  followed by `###`.
- A heading identical to the page title is dropped — it is the title repeated.

### Mathematics

- **`$…$` and `$$…$$` only.** Never `\(…\)`, never `\[…\]`: `pymdownx.arithmatex` does not pick
  those up from source, so they render as literal backslashes on the site.
- Display maths has its `$$` fences on their own lines, and is indented three spaces when it sits
  inside a list item so that it stays in the item.
- **No escaped delimiters.** `\$`, `\_`, `\*` and `\[` inside mathematics are extractor damage, not
  content — `\theta\_i` is not a subscript. They are unescaped before the page is written.
- **No MathJax scaffolding.** `<span class="math inline">`, `<span class="math display">` and the
  `\(`-wrapped payload inside them are converted to `$…$` / `$$…$$` before pandoc sees the document,
  never patched afterwards by substituting delimiters — that is what turned `\EE\[\theta_i \mid X\]`
  into `\EE\[\theta_i \mid X$$`.
- Every `$` and every `$$` is balanced within the page. An odd count means the rest of the page is
  swallowed into mathematics, and the page does not ship.

### Raw HTML

**The body contains no raw HTML.** The site enables neither `md_in_html` nor `pymdownx.caret`, so
most of it does not render as intended anyway, and it makes the markdown unreadable as plain text —
which this repo is first.

| found | becomes |
| --- | --- |
| `<br>` | a real line break, or a space where it was splitting a sentence |
| `<sup>2</sup>`, `<sub>i</sub>` | `$^2$`, `$_i$` where the context is mathematical; otherwise the bare character |
| `<span …>text</span>` | `text` |
| `<div>`, `<section>` | dropped, contents kept |
| `<tr>`/`<td>` tables | pipe tables |
| `<a href="#fn38" …>` | a real footnote reference, or dropped if the definition did not survive the split |
| `&lt;` `&gt;` `&amp;` | `<` `>` `&` |
| `<!-- Start of picture text -->…<!-- End of picture text -->` | **deleted.** This is OCR of the text inside a figure, `<br>`-joined and unordered. It is not content; it is the wreckage of a figure that should have been extracted |

### Extraction debris

Deleted wherever it appears:

- **bare page-number lines** — a line whose entire content is a number, and `Page 7`, `7 of 31`
- **running headers and footers** — a line repeated at the same position across more than half the
  pages of the source document
- **line-ending hyphens** joining a word split across a line break
- **orphaned code fences.** Every ``` opened in a page is closed in the same page. The splitter
  must not cut inside a fenced block; where a section boundary falls inside one, the split moves to
  the end of the block

### Figures

```markdown
![Two planes in R^3 sharing a line, with the same vector decomposed two ways](figures/03-sum-not-direct.png)
```

- on its own line, blank line above and below, immediately after the paragraph it illustrates
- a **relative** path into a `figures/` directory beside the page, matching `docs/notes/*/figures/`
- alt text describes the figure in words, ASCII only, no LaTeX
- **extraction is licence-gated.** See `quality-gates.md` § *Figures*. Where the licence does not
  permit redistribution, the figure becomes an explicit marked placeholder linking to the original,
  never a silent omission and never an apology in italics

### Length and wrapping

- Prose is **not** hard-wrapped: one paragraph per physical line, as in `docs/notes/`. Only this
  repo's own hand-written files (`AGENTS.md`, `README.md`, these references) wrap at ~100.
- A blank line between every block — paragraph, heading, display equation, image, table, blockquote.
- `---` between top-level sections on a page longer than ~250 lines; none on a short page.

## The footer

```markdown
---

[← Lecture 6](../06-…/) · [Up: contents](../) · [Lecture 8 →](../08-…/)
```

Unchanged from the existing converter, and relative so it survives `use_directory_urls: true`. A
page that is not part of a split document gets only `[Up: contents]`.

## What is never in a converted page

Anything that would make it look like *his* material rather than someone else's:

- **No `Status:`**, no `**Derived unaided.**`, no `**Not yet derived.**`. Those are knowledge-base
  vocabulary and mean things about his understanding. A converted page is not evidence of anything.
- **No supplied motivation**, no guiding question, no summary, no "what this covers". If a source
  needs those to be worth reading, it needs *adapting*, and that happens next door.
- **No `**Unverified.**` on a page that was not repaired.** The marker means a specific expression
  was reconstructed. A whole-page reconstruction says so in its banner instead — see the
  `reconstructed` row above — because marking every line would make the marker meaningless.
- **No editorial opinion.** Verdicts on a source live in the knowledge base's `docs/resources/`.
