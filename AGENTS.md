# AGENTS.md

Instructions for any coding agent working in this repository — Claude Code, Codex, or otherwise.
This is the **one** instruction file. `CLAUDE.md` imports it; nothing is duplicated here by hand.

## What this repository is

**A shelf of course books.** One book per course — coherent lecture notes written from everything
that course provides, with the same structure for every course, so that moving between them costs
nothing.

**This is a change, and it was made for a reason.** The repository began as converted source
material and nothing else: slides in one directory, transcripts in another, problem sets in a
third, twelve course-years side by side. That is a *hoard*, not a library, and its owner said so
plainly — "instead of taking the best from each one and combining in one good book you keep all of
those separate as if the task is not to convert it into usable teaching material but to hoard all
books and courses in one place. For that I could have just kept them in PDF."

He was right. A converted artefact answers *what did page 19 say*; the original PDF already
answered that, and better. A book answers *teach me this subject*, and nothing else in the pipeline
was answering it.

So the conversion still happens — it is how the material becomes readable — but it is now an
intermediate step, not the product. `skills/normalise-materials/references/book-template.md` is the
specification for what ships.

```
knowledge-base            his questions, trajectories, notes and verdicts — small, curated, his
knowledge-base-library    everyone else's courses, rewritten as books — large, generated, theirs
```

**The split is by authorship, not by subject.** If a human wrote it about his own understanding —
his questions, his trajectories, what he derived himself — it belongs in the knowledge base. If it
is someone else's course, it belongs here.

**Note that "mechanically reformatted" no longer describes this repository**, and the distinction
between a rewrite here and an *adaptation* in the knowledge base's `adapted/` is now one of
purpose, not of process. A book here is a course taught well, for any reader. An adaptation there
is built around *his* anchors and his way in, and is a different document even when the source is
the same.

**Everything here is still generated, and still never edited by hand.** A book is regenerated from
its cached chapters; a chapter is regenerated from the converted material; the converted material
is regenerated from `sources/`. To change the text, fix the converter, the prompt or the template.

**This repository serves the knowledge base, and is judged by whether it does.** The knowledge base
is a route through ideas indexed by question, where completeness is the failure mode rather than
the goal — its `AGENTS.md` opens with the test every change there is judged by. Here the opposite
is true and deliberately so: breadth is the point, because the whole job is to be the place
exhaustive material can live *without* burying seventy pages of actual notes. So the test here is
narrower and mechanical — **is it converted faithfully, is it linkable, does it cite its
original?** — and anything that is a *judgement* about a source belongs next door, not here.

## Everything here is generated

**Never edit a converted file by hand.** It is regenerable output: a hand edit is lost on the next
run and, worse, silently diverges from the source it claims to reproduce. To change the text, fix
the converter — or make an *adaptation*, which is a different job and lives in the knowledge base's
`adapted/`.

The converter lives here, in `skills/`, beside the material it produces:

```bash
uv sync --group dev --group convert
uv run --group convert --group dev python \
    skills/normalise-materials/scripts/normalise_source.py sources/<slug>       # dry run
uv run ... normalise_source.py sources/<slug> --apply                           # write
uv run ... normalise_source.py --all                                            # plan the corpus
uv run ... normalise_source.py --summary-only --apply                           # nav + index only
```

`sources/<slug>` in, `docs/<slug>/` out, both in this repository. **Anything that touches
`sources/` lives where `sources/` lives** — which is why `collect-materials`, `normalise-materials`
and the four source-handling scripts are here rather than with the teaching skills next door.

## What is converted, and what is not

The rule is deliberately a single skip list rather than a tier system. Everything public is
converted and published; two categories are simply never converted at all:

| `material:` | Converted? |
| --- | --- |
| `course`, `notes`, `thesis` | yes |
| `paper` with `open_access: true` | yes |
| `paper` without it — assume paywalled | **no** |
| `book` | **no**, however obtained |
| `archive`, `data` | no — not document sources |

No source is currently classified `paper`, and `open_access:` appears nowhere in the lockfile, so
those two rows govern nothing today. They are kept because a paper is a first-class source kind
here and the next one collected will need them — not because they are in use.

`material:` is a hand-written field in `sources/sources.lock.yml`. It is never detected, because
guessing it guesses in the publishing direction. A source with no `material` is skipped and named
in the report.

### A licence must permit a derivative work, not merely redistribution

**A book here is a rewrite, so the question is not "may I copy this?" but "may I publish something
built from it?"** That is a higher bar, and it is an **allow-list with default deny** for the same
asymmetry as everything else on this page: a skipped source costs one lockfile edit, a published
derivative of someone's dissertation cannot be recalled. `may_adapt()` in `normalise_source.py` is
the implementation.

| `licence:` | Publish a book from it? | What the book must carry |
| --- | --- | --- |
| `CC0-1.0`, public domain | yes | nothing |
| `CC BY 4.0` / `3.0` | yes | attribution |
| `CC BY-SA 4.0` / `3.0` | yes | attribution, **and the same licence** — share-alike propagates |
| `CC BY-NC 4.0` / `3.0` | yes | attribution, non-commercial |
| `CC BY-NC-SA 4.0` / `3.0` | yes | attribution, non-commercial, **and the same licence** |
| `CC BY-ND`, `CC BY-NC-ND` | **no** | — **`ND` forbids distributing an adaptation.** It reads as permissive because it is Creative Commons, and it is the one CC family that rules a book out. Two Caltech theses here are CC BY-NC-ND: `NC` alone would have been fine, `ND` is what decides it |
| `unresolved` | **no** | — resolve it first; `unresolved` means *not found*, never *not licensed* |
| `all rights reserved` | **no** | — recorded when a check found *nothing*, which is a finding and not an open question |
| BSD / MIT / Apache | **no** | — see below |
| anything else | **no** | — add it to `MAY_ADAPT` deliberately, or leave it out |

**A software licence is not a content licence.** A BSD or MIT `LICENSE` in a course repository
almost always covers the scripts, and `AGENTS.md` already records the sharper form of this trap: a
`*.github.io` repo's MIT licence is the Jekyll theme's, with the template author in the copyright
line. Two sources here are BSD-only and are withheld for exactly that reason. Where a repository
genuinely licenses its *prose* this way — a `myst.yml` declaring `license: {code: MIT, content:
CC-BY-4.0}` — record the **content** licence in the lockfile and it passes.

**Third-party publications inside a course are excluded per file.** `material:` classifies the
source, and the source is a course; but courses ship a Wiley textbook chapter in `project/`, a
paywalled journal paper in `ps/`, a publisher's book-companion deck in `lectures/`. The
hand-written `exclude:` list in a lockfile entry names those, and they are reported as
*third-party publication — not redistributed*. This is the per-file half of a policy the
`material:` table above already states: a book is never converted "however obtained", and a paper
without `open_access` is assumed paywalled.

**Every page cites its source and links to the original.** That is generated rather than left to an
author to remember, because the whole arrangement of republishing other people's material rests on
it. A source with no recorded URL is skipped rather than published uncited.

**A real licence still governs.** Where a source carries CC BY-NC-SA or similar, share-alike
propagates and the converted pages carry the same licence — it is in each page's front matter. If a
rights-holder objects, remove the pages and record the reason in the knowledge base's catalogue
entry, which is why the source URL is never dropped.

## The rule that decides everything: convert the source, not the render

**Verified on this material, and the difference is not marginal.** The same lecture, two ways:

| From | Result |
| --- | --- |
| `.Rmd` / `.qmd` / `.tex` | `$\pm$`, `$(X_i, Y_i)$` — **the LaTeX the author typed** |
| the PDF built from it | `λ(t) = Sf((tt))becauseTiscontinuous` — the fraction destroyed |

Prose survives a PDF; **mathematics does not**. The converter enforces this automatically: where a
`.pdf` or `.html` sits beside a source file with the same stem, the render is dropped and reported.
The same rule now covers speech: a `.srt` beats a PDF of the same transcript, which OCW ships
alongside it.

**A PDF with nothing better beside it goes to a multimodal model**, not to `pymupdf4llm`. The
deterministic route produced 55% of the old corpus and almost none of it was readable — scrambled
two-column slides, equations destroyed, 3,519 figures reduced to unordered OCR fragments. It is
kept as the *cross-check* on the model rather than as the output. That route is inference, so it is
fenced: a labelled `route`/`fidelity`, a banner that says a model wrote the page and every equation
in it is unverified, a word-recall check against the parser wherever the parser's text is credible,
and a committed cache so regeneration does not re-roll the model. The rules are in
`skills/normalise-materials/references/quality-gates.md`.

## Traps, each of which cost real time

- **A scanned PDF has no text layer.** Stat 210A's handwritten lectures yield a couple of hundred
  characters of OCR fragments. They are skipped and listed, never turned into a near-empty page
  that looks like a conversion — the next reader cannot tell those apart.
- **A local path is not always an upstream path.** MIT OCW exports are renamed at ingest by
  `organise_course.py`, so building a per-file URL from the tidied path produces a confident 404:
  `…/worked-examples/x.srt` → 301 → `…/resources/x.srt` → 404. A files-kind source therefore links
  to its course page unless the lockfile asserts `mirrors_upstream: true`. Verified true for every
  Berkeley instructor-page source, false for all six OCW exports.
- **A PDF's biggest text is not its title.** Converted exam papers came out titled
  `**Student ID (NOT your name):**`. Titles are cleaned, and fall back to the filename.
- **A licence is rarely in a `LICENSE` file.** Course sites use `license.qmd`, `license.html`, or
  `myst.yml` declaring `license: {code: MIT, content: CC-BY-4.0}` — where the *content* licence
  governs and the code licence is a decoy. GitHub reports all of these as `NOASSERTION`.
- **A `*.github.io` repo's MIT licence is the Jekyll theme's**, with the template author in the
  copyright line. It says nothing about course content.

## Repairing mangled mathematics

A PDF conversion leaves equations broken in a way a parser cannot fix. Repairing them is worth
doing, but it is **inference about what was written**, and the discipline is not negotiable:

- **Mark every repaired expression `**Unverified.**`** unless confirmed against a source format.
- **Repair against the original page, not from context alone.** Guessing a plausible equation from
  surrounding prose is the worst available failure: undetectable, and confidently wrong.
- **Where the reading cannot be settled, give both** and say so.
- **Report the count of `**Unverified.**` marks.** That number is how much of the document is
  reconstruction rather than record.

Run it as a separate pass over already-converted files, never inline with the mechanical
conversion. A conversion that is merely lossy is honest; one silently improved by a model is not.

This is the one exception to *never edit a converted file by hand* — and it is not really an
exception, because a repair pass that cannot be re-run is a hand edit. Repairs belong in the
converter's repair step, so they survive regeneration.

## Source material is referenced, never vendored

`sources/` is **gitignored in full** except `README.md` and `sources.lock.yml`. The bytes are
someone else's material and mostly all-rights-reserved. What is committed is the durable half: the
lockfile that says how to get them back, and the conversion.

```bash
uv run python <kb>/skills/collect-materials/scripts/restore_sources.py --apply   # rebuild
uv run python <kb>/skills/collect-materials/scripts/restore_sources.py --check   # verify
uv run python <kb>/skills/collect-materials/scripts/lock_sources.py --apply      # re-record
```

`lock_sources.py` preserves hand-written fields across a rescan — `material`, `open_access`,
`mirrors_upstream`, `base`, `note`, `title`, `subject`, `provider` — and never downgrades a resolved licence to `unresolved`,
because several were settled by reading a course site rather than a file in the repo.

## The site

`docs/` is published to GitHub Pages at <https://claptar.github.io/knowledge-base-library/> on every
push to `main`. MkDocs Material, built with `uv`.

```bash
uv sync --group dev
uv run mkdocs serve
uv run mkdocs build --strict   # what CI runs
```

- **The nav is generated** into `docs/SUMMARY.md` and read by `mkdocs-literate-nav`. There is no
  hand-written `nav:` in `mkdocs.yml` and there should not be.
- **The build is `--strict`** even though nothing here is hand-written. A broken link means the
  converter has a bug, which is exactly what this catches.
- **`--strict` is not a quality check, and must never be mistaken for one.** It validates links and
  anchors, and it passed cleanly on a corpus where 373 pages showed the reader raw
  `<span class="math inline">`. `skills/normalise-materials/scripts/validate_pages.py` is the
  quality gate, it runs in CI beside the build, and it must report zero fatal findings.
- Maths is `pymdownx.arithmatex` with MathJax. `$…$` and `$$…$$`; never `\(…\)` or `\[…\]`.
- **MkDocs 1.x is pinned (`<2`) deliberately** — Material has announced 2.0 removes the plugin
  system with no migration path. Not a stale pin.

## Git

One long-lived branch, `main`, which is also the deploy branch. This repository holds generated
output: there is nothing to review on its own, and no releases to cut — the versioned artefact is
the skills, and they live in the knowledge base.

Commit per conversion run, with a message naming the source converted — not "update".
