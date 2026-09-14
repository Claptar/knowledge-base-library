# Changelog

Releases of the `study-library` plugin — the `collect-materials` and `normalise-materials` skills
and their scripts. The converted material in `docs/` changes continuously and is not itemised here;
`git log` records it, and a tag per conversion run would make the tag list useless for the thing it
is actually for, which is telling someone which version of the skills they installed.

## Unreleased

### Structure

- **Split out of [knowledge-base](https://github.com/Claptar/knowledge-base).** A full dry run over
  the corpus plans **9,657 pages from 1,948 documents**, against roughly seventy files of his own
  writing in the knowledge base. Kept together, the notes become a rounding error inside their own
  library. The split is by authorship: what he wrote stays there, what someone else wrote is here.
- **Two skills and four scripts came with it.** `collect-materials`, `normalise-materials`, and the
  four source-handling scripts that used to live in `adapt-recordings/scripts/` — anything that
  touches `sources/` lives where `sources/` lives.

### Skills

- **`normalise_source.py`**, the converter. Prefers the source format over the render — a `.qmd`
  beside its `.pdf` converts from the `.qmd`, and the render is reported as dropped. Splits on the
  source's own headings, one page per logical section. Rewrites every relative link to a converted
  sibling, to the upstream original, or to plain text, because the site builds `--strict` and a
  dangling link fails CI. Dry run by default.
- **Two categories are never converted** — a book, and a paper without `open_access` — which
  replaces the publish-versus-private tiering the knowledge base used to carry. There is no private
  tree.
- **New recipe: CaltechTHESIS.** Record-page layout, the non-constant document slot in the PDF path
  (`/16062/03/`, `/16368/10/`), and the failure worth naming: the site began refusing automated
  requests partway through a harvest, with a timeout from `curl` and an `ECONNREFUSED` from an agent
  fetch, while other hosts answered normally in the same minute. Diagnose it by fetching an
  unrelated host.

### Tooling

- **`material:`, `open_access:` and `mirrors_upstream:` in `sources.lock.yml`** — hand-written,
  never detected, preserved across a rescan. `mirrors_upstream` exists because MIT OCW exports are
  renamed at ingest, so building a per-file URL from the tidied path produced a confident 404:
  `…/worked-examples/x.srt` → 301 → `…/resources/x.srt` → 404.
- **A licence rescan no longer downgrades a resolved licence.** Several were settled by reading a
  course site rather than a file in the repo, and `unresolved` means *not found*, not *not
  licensed*.

### Known issues

- **`normalise_names.py` is not idempotent.** A second `--apply` re-suffixes already-normalised
  files (`final-f09-exam.pdf` → `final-f09-exam-exam.pdf`) and rewrites `_manifest.csv` with the
  mangled names, destroying the mapping back to publisher filenames. The guard in `main()` compares
  `src != dest`, but `plan()` rebuilds `dest` from the current stem and appends the artefact type
  unconditionally, so it never fires. Deliberately unfixed — the repair touches the classifier.
- **1,016 of the converted pages came the lossy PDF route** and carry the mangled-mathematics
  banner. The repair pass in `normalise-materials` step 3a is specified but not built.
