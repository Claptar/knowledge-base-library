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
| `.tex` | pandoc | high — maths intact |
| `.html` | pandoc | good; MathJax output is uglier than source |
| `.ipynb` | nbconvert | good |
| `.srt` `.vtt` | `scripts/transcript_text.py` | speech, and **read that skill first** |
| `.pdf` | pymupdf4llm | **prose only — maths destroyed. Mark it** |

Install the toolchain with `uv sync --group convert`; it is declared in `pyproject.toml` and needs
no system packages.

Where a document exists in several formats the script keeps only the best: a lecture present as
`.qmd`, `.html` and `.pdf` converts once, from the `.qmd`, and the other two are reported as
dropped renders. Course administrivia — install guides, rubrics, codes of conduct — is skipped by
default and listed; `--include-all` keeps it. A syllabus is **not** administrivia.

A transcript is not a document, and converting one is not this skill's job beyond the mechanical
step. The `adapt-recordings` skill, in the knowledge base repository, owns what speech requires —
reconstructing mathematics spoken aloud and written on a board the transcript cannot see — and it
is the authority on it.

## Step 3 — split it

**One file per lecture, section or coherent block**, because the point of the exercise is a URL per
idea. Split on the source's own structure — `#`/`##` headings, or one file per lecture in a course
repo — rather than on length.

Keep the source's numbering where it has one (`lecture07`, `chapter03`): it is how he will refer to
it, and renumbering breaks the correspondence with the original. Where there is none, number in
document order.

Each output file carries, generated rather than hand-written:

```markdown
---
title: <section title, from the source>
source: <URL of the original>
source_file: sources/<slug>/<path>
licence: <the source's, and therefore this file's>
converted: YYYY-MM-DD from .qmd
---
```

Add `**Converted from PDF — mathematics may be mangled. Check against the original.**` when the
route was a PDF. That warning is the honest half of a lossy conversion and must not be omitted to
make the output look tidier.

## Step 3a — repairing mangled mathematics

A PDF conversion leaves equations broken in a way a parser cannot fix: `λ(t) = Sf((tt))because...`
is recoverable as $\lambda(t) = f(t)/S(t)$ only by *reading it and knowing what it must have said*.
That is a job for a model, not a regex, and it is worth doing — but it is **inference about what
was written**, and this repo already has a rule for that.

**The precedent is the `adapt-recordings` skill's step 3**, which reconstructs spoken mathematics
and
marks every reconstruction. The discipline is identical here and not negotiable:

- **Mark every repaired expression `**Unverified.**`** unless it is confirmed against a source
  format or a clean copy. Confirmation demotes it to plain text; nothing else does.
- **Repair against the original page, not from context alone.** Guessing a plausible equation from
  surrounding prose is the worst available failure: undetectable, and confidently wrong.
- **Where the reading genuinely cannot be settled, give both** and say so, exactly as for a
  transcript.
- **Report the count of `**Unverified.**` marks left in the file.** That number is how much of the
  document is reconstruction rather than record.

Run it as a separate pass over already-converted files, never inline with the mechanical
conversion — the two have different failure modes and should be reviewable apart. A conversion that
is merely lossy is honest; a conversion silently improved by a model is not, which is the whole
reason for the marking.

A dedicated lightweight skill for this pass is a reasonable thing to add; until one exists, it is
this step, with the rules above.

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

- `scripts/normalise_source.py` — the converter. Dry run by default.
- `scripts/transcript_text.py` — captions to timestamped prose.
- `../collect-materials/SKILL.md` — how material gets here in the first place.
- [`AGENTS.md`](../../AGENTS.md) — what is converted, what is not, and the traps.

In the **knowledge base** repository, not this one: `adapt-recordings` is the authority on
transcripts, `adapt-material` on rewriting (which this is not), and `study-mentor` on what a
verdict costs.
