# AGENTS.md

Instructions for any coding agent working in this repository — Claude Code, Codex, or otherwise.
This is the **one** instruction file. `CLAUDE.md` imports it; nothing is duplicated here by hand.

## What this repository is

**Converted source material, and nothing else.** Course notes, lecture transcripts, problem sets
and papers, turned into uniform markdown and split by section so that every part of them has a URL.

It exists because a PDF has no addressable parts. A topic file in the knowledge base cannot cite
"§3 of lecture 7" when lecture 7 is a page range — and once there are nearly ten thousand converted
pages, they cannot live in the knowledge base either, or the knowledge base becomes a rounding
error inside its own library.

```
knowledge-base            his questions, trajectories, notes and verdicts — small, curated, his
knowledge-base-library    everyone else's material, converted — large, generated, theirs
```

**The split is by authorship, not by subject.** If a human wrote it about his own understanding it
belongs in the knowledge base. If it is someone else's text mechanically reformatted, it belongs
here.

## Everything here is generated

**Never edit a converted file by hand.** It is regenerable output: a hand edit is lost on the next
run and, worse, silently diverges from the source it claims to reproduce. To change the text, fix
the converter — or make an *adaptation*, which is a different job and lives in the knowledge base's
`adapted/`.

The converter is **not in this repository**. It lives with the skills, in the knowledge base:

```bash
export KB_LIBRARY=/path/to/knowledge-base-library
cd /path/to/knowledge-base
uv run --group convert --group dev python \
    skills/normalise-materials/scripts/normalise_source.py sources/<slug>            # dry run
uv run ... normalise_source.py sources/<slug> --apply                                # write
uv run ... normalise_source.py --all                                                 # plan the corpus
uv run ... normalise_source.py --summary-only --apply                                # nav + index only
```

`sources/` lives **here**, beside the output it produces. The script resolves it from `--library`,
then `$KB_LIBRARY`, then a sibling `../knowledge-base-library`.

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

`material:` is a hand-written field in `sources/sources.lock.yml`. It is never detected, because
guessing it guesses in the publishing direction. A source with no `material` is skipped and named
in the report.

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
PDFs are converted only when nothing better exists, and every such page carries a banner saying so.

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
`mirrors_upstream`, `base`, `note` — and never downgrades a resolved licence to `unresolved`,
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
- Maths is `pymdownx.arithmatex` with MathJax. `$…$` and `$$…$$`; never `\(…\)` or `\[…\]`.
- **MkDocs 1.x is pinned (`<2`) deliberately** — Material has announced 2.0 removes the plugin
  system with no migration path. Not a stale pin.

## Git

One long-lived branch, `main`, which is also the deploy branch. This repository holds generated
output: there is nothing to review on its own, and no releases to cut — the versioned artefact is
the skills, and they live in the knowledge base.

Commit per conversion run, with a message naming the source converted — not "update".
