---
name: normalise-materials
description: Converts collected source material — course repos, lecture notes, GitHub Pages sites, Quarto/Rmd/LaTeX sources, notebooks, caption files, PDFs — into uniform markdown split by lecture or section, so every part of it can be linked to. Use when he wants material made referenceable rather than fetched, judged or rewritten: "convert these to markdown", "split this course into sections", "make this linkable", "normalise the sources", "why can't I link to lecture 7". Produces a markdown tree beside the raw download, never in place of it. Use collect-materials to fetch a source first, adapt-material to rewrite one motivation-first, and study-mentor to work through it.
---

# Normalise Materials

## What this is for

A course arrives as a pile of formats — Quarto sources, rendered HTML, typeset PDFs, notebooks,
caption files — and none of it can be *linked to*. A topic file cannot say "the NPMLE derivation is
§3 of this lecture" when the lecture is page 19 of a PDF.

This skill converts a source into markdown split by section, so every part has a URL. It sits
between fetching and using:

```
collect-materials  ->  normalise-materials  ->  adapt-material  ->  study-mentor
   fetch it            make it linkable         rewrite it         work through it
```

**Conversion preserves; the book rewrites.** The two steps are deliberately separate and the
boundary matters: everything up to step 3a changes format only, and step 3b writes new prose from
what those steps produced. If you find yourself improving the text during conversion, stop — that
belongs in the book, where it is marked as a rewrite and carries its source's licence.

**It preserves; it does not rewrite.** An adapted document reorders the material motivation-first
and converts proofs to exercises — that is the `adapt-material` skill, in the knowledge base
repository, and it is a different job.
This one changes the *format* and nothing else. If you find yourself improving the prose, stop:
that is an adaptation, and it belongs in `adapted/` under its own rules.

## The rule that decides everything: convert the source, not the render

**Verified on this repository's own material, and the difference is not marginal.** The same
lecture, converted two ways:

| From | Result |
| --- | --- |
| `.Rmd` / `.qmd` / `.tex` | `$\pm$`, `$(X_i, Y_i)$` — **the LaTeX the author typed**, and clean headings to split on |
| the PDF built from it | `λ(t) = Sf((tt))becauseTiscontinuous` — the fraction destroyed, words run together |

Prose survives a PDF; **mathematics does not**. For a mathematics knowledge base that makes the
rendered artefact close to worthless for the equations, which are the part that matters.

So: **look for the source next to the render before converting anything.** Most course PDFs in
`sources/` were built from a `.qmd` or `.Rmd` sitting in the same repository — 1,027 source-format
files against 1,585 PDFs. Reach for the PDF only when nothing else exists, and mark the result.

### What cannot be converted at all

**Scanned or handwritten PDFs have no text layer.** Stat 210A's lectures are `handwritten/
lecture01-intro.pdf` — photographs of handwriting. Extraction yields a couple of hundred characters
of OCR fragments and nothing usable.

Say so and stop. Emit an index entry pointing at the original rather than a page of garbage: a
near-empty markdown file that looks like a conversion is worse than an honest absence, because the
next reader cannot tell which it is.

## Step 1 — decide whether it is converted at all

There is no private tree and no tier system. Two categories are simply never converted; everything
else public is converted, published, cited and linked to its original.

| `material:` | Converted? |
| --- | --- |
| `course`, `notes`, `thesis` | yes |
| `paper` with `open_access: true` | yes |
| `paper` without it — assume paywalled | **no** |
| `book` | **no**, however obtained, whatever its licence |
| `archive`, `data` | no — not document sources |
| missing, or no source URL to cite | **no**, and named in the report |

**`material:` lives in `sources/sources.lock.yml` and is written by hand.** It is never detected,
because guessing it guesses in the publishing direction. `open_access: true` is the one assertion
that admits a paper.

**Every page cites its source and links to the original**, generated rather than left to an author
to remember — the whole arrangement of republishing other people's material rests on it, which is
why a source with no recorded URL is skipped rather than published uncited. Where a source carries
a real licence, it goes in the front matter and its conditions hold: share-alike propagates.

## Step 2 — convert

`scripts/normalise_source.py` does the mechanical part. Formats, in the order to prefer them:

| Format | Route | Fidelity |
| --- | --- | --- |
| `.md` `.qmd` `.Rmd` | strip front matter and code chunks | lossless |
| `.tex` | pandoc, after rewriting knitr's `\KeywordTok{}` highlighting as `verbatim` | high — maths intact |
| `.rst` | pandoc | high |
| `.html` | pandoc, with the maths lifted out first — see below | good |
| `.ipynb` | read from the JSON, not nbconvert | lossless |
| `.srt` `.vtt` | `scripts/transcript_text.py` | speech, and **read `adapt-recordings` first** |
| `.pdf` | **a multimodal model** — `scripts/llm_pdf.py` | reconstructed |

Install the toolchain with `uv sync --group convert`.

**There is no plain PDF route any more.** `pymupdf4llm` produced 55% of the old corpus and almost
none of it was worth reading; it is now the *cross-check* rather than the output. A PDF that
survives re-routing goes to a model, under the four controls in
[`references/quality-gates.md`](references/quality-gates.md) § *The LLM route*.

**Two traps in the pandoc routes, both of which cost real time:**

- **Pandoc's HTML reader does not parse `<span class="math inline">\(x\)</span>` as mathematics.**
  It treats the payload as literal text and escapes the backslashes. A later `\[` → `$$`
  substitution over that escaped output is what turned `\EE\[\theta_i \mid X\]` into
  `\EE\[\theta_i \mid X$$` on 360 published pages. The maths is now lifted out *before* pandoc
  sees the file and put back afterwards, untouched.
- **knitr writes R code into LaTeX as `\begin{Shaded}` with every token in a `\NormalTok{}`
  macro**, which pandoc renders as bold prose: `m1 <- **lm**(lpsa ** ** 1, data = prostate)`.
  Those environments are rewritten as `verbatim` first.

Where a document exists in several formats the script keeps only the best, and reports the rest as
dropped renders. **A caption file beats a PDF of the same transcript**: OCW ships each lecture's
words up to four times, and converting the rest produced duplicate pages and, now, duplicate bills.

Course administrivia is skipped by default and listed; `--include-all` keeps it. A syllabus is
**not** administrivia.

## Step 3 — split it, and shape it

**Chapter-sized pages.** Split on the source's *top* heading level and no deeper, then merge any
part too thin to stand as a page into its neighbour — backwards, or forwards when it is the first
part, because an exam PDF opens with a letterhead that otherwise becomes a page of nothing.

The old rule tried each level shallowest-first and accepted one whose sections *averaged* over 400
characters. Averaging is the flaw: one long section drags a crowd of three-line stubs over the bar,
and it produced 11,918 pages of which 2,243 had no body at all.

**The shape of a page is not described here.** It is in
[`references/page-template.md`](references/page-template.md), which is the single authority, and
`scripts/body_rules.py` implements it. This file used to carry a front-matter block that had
already drifted out of step with the script — one copy, referenced, is the rule for skills as much
as for notes.

## Step 3a — repairing mangled mathematics

**This step is now mostly the LLM route, and that is the point.** The old instruction was to run a
separate manual pass over converted files, reading `λ(t) = Sf((tt))because...` against the original
and restoring `$\lambda(t) = f(t)/S(t)$` by hand, marking each repair `**Unverified.**`. It was
specified, never built, and the count of `**Unverified.**` marks in the corpus stayed at zero while
6,506 pages carried the mangled-mathematics banner.

A model reading the page does that job, at scale, and the honest bookkeeping moved with it: instead
of marking each repaired expression, the whole page declares itself reconstructed in its banner,
because a page written end-to-end by a model is not a record with repairs in it.

**The marking discipline still holds wherever a human or an agent edits a converted page by hand:**

- **Mark every repaired expression `**Unverified.**`** unless confirmed against a source format.
- **Repair against the original page, not from context alone.** Guessing a plausible equation from
  surrounding prose is the worst available failure: undetectable, and confidently wrong.
- **Where the reading cannot be settled, give both** and say so.

And the rule above it still holds hardest: **a source format beats any reconstruction.** A `.tex`
gives the LaTeX its author typed. No model improves on that, and none is asked to.

## Step 3b — write the book

**Conversion is not the product.** A converted page answers *what did page 19 say*, which the PDF
already answered. The library ships **one book per course**: coherent lecture notes written from
the slides and the transcript together, exercises from the course's own problem sets, solutions as
a linked appendix, and the same structure for every course.

`references/book-template.md` is the specification; `scripts/synthesise_book.py` implements it.

```bash
synthesise_book.py plan  <course>            # chapters it would write, from what, and the cost
synthesise_book.py submit <course>           # queue them (Batch API, half price)
synthesise_book.py submit <course> --sync    # or straight to the model, twice the price, no wait
synthesise_book.py collect                   # finished chapters into the cache
synthesise_book.py write <course> --apply    # write the book AND delete the artefacts it replaces
```

Three things about this that cost real time to learn:

- **Course years merge.** Stat 243 ran twelve times and Stat 150 seven. That is one book each, not
  twelve directories side by side.
- **Practice binds to its lecture.** Recitation 7 is the exercises for chapter 7, not a chapter
  between 7 and 8. Treating every recitation and worked example as its own chapter turned one
  course into 86 "chapters" — the same fragmentation wearing a different label.
- **A chapter is keyed on its input material**, so writing a book before its slides have finished
  converting means paying for every chapter twice. Wait for the conversion.

## Step 4 — file it

- **An `index.md` per source**, listing its parts in order with links. This is the page a topic
  file links to, and for a source that cannot be published it is the *only* page — structure and
  links, no body text.
- **The nav is generated into `docs/SUMMARY.md`**, which `mkdocs-literate-nav` reads. There is no
  hand-written `nav:` in `mkdocs.yml` and there should not be — several thousand entries do not
  belong in a config file. `--summary-only` rebuilds the nav and the landing page without
  converting anything.
- **Link it from the catalogue entry**, which lives in the *knowledge base* repository next door
  at `docs/resources/`, so the verdict on a source and its converted form are one click apart.
- **Never edit a converted file by hand.** It is regenerable output; a hand edit is lost on the next
  run and, worse, silently diverges from the source it claims to reproduce. Fix the converter, or
  make an adaptation instead.

## Step 5 — report

Say how many files converted, how many were **skipped as unconvertible** and why, and how many came
through the lossy PDF route. Those three numbers are the quality of the result, and the second is
the one worth acting on — it is the list of material that needs a different approach.

## Reference files

- [`references/page-template.md`](references/page-template.md) — **the authority on what a
  converted page looks like.** Front matter, banner, headings, maths, HTML, figures, footer.
- [`references/quality-gates.md`](references/quality-gates.md) — what is rejected and why, the
  measured baseline, and the rules fencing the LLM route.
- [`references/book-template.md`](references/book-template.md) — **what the library ships**: one
  book per course, and the motto every choice here is judged by.
- [`references/index-template.md`](references/index-template.md) — the per-source contents page.
- `scripts/normalise_source.py` — the converter. Dry run by default, and a dry run never calls a
  model.
- `scripts/body_rules.py` — the body pipeline.
- `scripts/validate_pages.py` — the gates, as code. Also CI.
- `scripts/llm_pdf.py` — the PDF route, its cross-check and its cache.
- `scripts/llm_batch.py` — the same route at half price, through the Batch API.
- `scripts/synthesise_book.py` — converted material to a course book.
- `scripts/transcript_text.py` — captions to timestamped prose.
- [`AGENTS.md`](../../AGENTS.md) — what is converted, what is not, and the traps.

In the **knowledge base** repository, not this one: `adapt-recordings` is the authority on
transcripts, `adapt-material` on rewriting (which this is not), and `study-mentor` on what a
verdict costs.
