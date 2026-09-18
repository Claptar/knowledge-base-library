# Changelog

Releases of the `study-library` plugin — the `collect-materials` and `normalise-materials` skills
and their scripts. The converted material in `docs/` changes continuously and is not itemised here;
`git log` records it, and a tag per conversion run would make the tag list useless for the thing it
is actually for, which is telling someone which version of the skills they installed.

## Unreleased

### A licence must permit a derivative work, and it is now checked

A book is a **rewrite**, so the question is not "may I copy this?" but "may I publish something
built from it?" That is a higher bar, and it was not being asked: 28 of 63 published sources had
`licence: unresolved` and were shipping derivative books anyway. `may_adapt()` is now an
**allow-list with default deny** — CC0, CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA pass; everything
else is withheld and named in the report.

Resolving the 28 against their upstream sites moved them in **both** directions, which is the
argument for the allow-list rather than a deny-list:

- **`statomics-sga2020-ghpages` was recorded CC0-1.0 and is not licensed at all.** Its
  `License.md` is Karl Broman's waiver for the *`simple_site` Jekyll theme*, byte-identical to
  `kbroman/simple_site`'s and listed in `_config.yml`'s `exclude:` so it never renders. A wrongly
  permissive record is the one direction that cannot be recalled.
- **`statomics-sga21` reports `license: null` and is CC BY-NC-SA 4.0.** The grant is in the course
  front page's prose, not in a `LICENSE` file. A metadata-only check misses it, and 44 chapters
  turned on getting it right.
- **`CC BY-NC-ND` is the trap worth naming.** It reads as permissive because it is Creative
  Commons, and `ND` forbids distributing an adaptation outright. Two Caltech theses are
  CC BY-NC-ND, where `NC` alone would have been fine. A deny-list would have published both.
- **A BSD or MIT `LICENSE` in a course repo is the code licence.** stat243's fall-2023 file was
  added at "Initial commit", referenced nowhere, and drafted for software; the same instructor
  picked CC0 in 2021 and CC BY in 2024-26. Recorded as unresolved, not as a green light.
- **Silence is a finding, not an open question.** Twelve Berkeley instructor pages carry no licence
  after checking the course page, the parent page and the source file; they are recorded
  `all rights reserved` so a later session does not re-resolve them.

### Third-party publications inside a course are excluded per file

`material:` classifies the *source*, and the source is a course — but courses ship a Wiley
textbook chapter in `project/`, a paywalled RSS paper in `ps/`, a publisher's book-companion deck
in `lectures/`. A hand-written `exclude:` list names them. They surfaced because an API content
filter refused to transcribe two of them, which was the correct answer to a question nobody had
asked.

### A chapter is a document, not a filename number

Chapter grouping read a section index off a split document's filename and treated it as a lecture
number, so stat153's chapter 1 merged **the first section of twenty-two different lectures** and
chapter 2 all the second sections — a book transposed, and one that would have read as plausible
prose. 70 of 726 chapters were built this way. Grouping now keys on the `source_file:` each page
records. Consequences:

- Course years merge even when the term is inside the *filename* rather than a directory
  (`CodeLectureTwentyOne153248Fall2025`), which is what inflated stat153 to 171 chapters.
- An exam is practice material, not a chapter: 6.041SC had grown `01-exam-quiz01-revi`,
  `02-exam` and `final-exam` as though a quiz were a lecture. It is now 25 lectures, each pairing
  its deck with its transcript, plus one stray recording.
- A single document over ~120k chars is a book rather than a lecture, and its own section pages
  become the chapters. Gorin's thesis was one chapter of 240k chars, silently truncated at the
  220k input cap.
- A course whose material is only a syllabus ships no book. Six Berkeley courses were producing a
  one-chapter book titled "Course Overview and Policies", 25 characters long.

### Fixes

- **A regeneration from cache no longer re-runs the PDF parser.** `convert_llm()` ran
  `pymupdf4llm` over every *cached* PDF purely to recompute a recall the cache already stores —
  29.5s for one 47-page deck. A full `--all --apply --clean` went from over an hour to under ten
  minutes.
- **`fig` added to `SKIP_DIRS`.** 72 plot PDFs under stat153's `lectures/*/fig/` were converted as
  documents and then grouped into chapters as though each were a slide deck.
- **A solutions page cites its source.** Without `source:` every one failed the fatal `uncited`
  gate — 14 of 6.041SC's 41 pages.
- **An SVG figure's labels are not prose.** `validate_pages.py` counted a `$1` price label in a
  diagram as an unmatched maths delimiter (fatal) and the numeric entities `tidy_svg` deliberately
  emits as debris to repair. The maths and entity gates now skip figures, as the raw-HTML gate
  already did. 6.041SC went from 15 rejected pages to 0.

### The library ships books, not artefacts

The repository's whole output changed. It was a pile of converted artefacts — slides in one
directory, transcripts in another, twelve course-years side by side, `recordings/recordings/` full
of pages titled by YouTube id. Its owner's verdict: *"for that I could have just kept them in PDF."*

It now ships **one book per course**: lecture notes written from the slides and the transcript
merged, exercises from the course's own problem sets, solutions as a linked appendix, identical
structure for every course. Conversion still happens and is unchanged in kind — it is now the
intermediate step rather than the product.

- **`references/book-template.md`** — the specification, and the motto it is judged by: *simpler
  and better*, both halves together.
- **`synthesise_book.py`** — plan / submit / collect / write, batched at half price. Idempotent:
  a manifest records which chapters a book is made of, so writing it again costs nothing.
- **Course years merge.** Stat 243's twelve become one book, Stat 150's seven become one.
- **Practice binds to its lecture.** Recitation 7 is chapter 7's exercises. Treating each
  recitation and worked example as its own chapter gave one course 86 of them.
- **Chapters are titled by the model**, from the content — `Probability Models and Axioms`, not
  `LECTURE 1`, `08 captions` or `12 slides lec 12 bonvid`.
- **Figures are inline SVG.** The model drew ASCII art in code fences unprompted; that is banned.
  Diagrams use `currentColor` so they are legible in both the light and dark themes — which is why
  they must be inline rather than `![](x.svg)`, since an external image cannot inherit the page's
  foreground. `body_rules.tidy_svg` makes them strict-XML clean deterministically, and turns `<=`
  into `≤` on the way past. 55 figures in the first book, 0 malformed, 0 ASCII.
- **Manim was considered and rejected** for figures: it renders `png|gif|mp4|webm|mov` and no
  vector format, so its output cannot follow the theme, and it needs LaTeX and ffmpeg to execute
  generated Python per figure. It remains the right tool for animation, which is a different
  artefact.


### Conversion quality — a rebuild, not a tidy-up

The library was uniform markdown in name only. Measured on the corpus as it stood: **4,613 of
11,917 pages failed a basic quality check**, 373 showed the reader raw
`<span class="math inline">\$\\tau^2\$</span>`, 652 had code fences split mid-block, 3,089 had no
body at all, 1,882 were duplicates, and `mkdocs build --strict` passed throughout — because it
checks links, not content.

- **The output shape now has one home.** `normalise-materials` had no `references/` at all: its
  page shape lived as hard-coded strings in the script and as prose in `SKILL.md`, and the two had
  already drifted (five documented front-matter keys against seven emitted). Three reference files
  now hold it — `page-template.md`, `quality-gates.md`, `index-template.md` — and `SKILL.md` points
  at them instead of restating them.
- **`validate_pages.py`** implements the gates, runs in CI beside the strict build, and is the
  publish decision for every page. A page that fails is listed under *Not converted* with its
  reason rather than published broken.
- **`body_rules.py`** is the stage the converter never had. `page()` used to interpolate the
  extractor's output verbatim between a banner and a footer, which is how 166,030 raw HTML tags,
  14,001 stray page numbers and 5,804 duplicate title levels reached the site.
- **Pandoc's HTML reader does not parse `<span class="math">` as mathematics.** It escapes the
  payload as text, and a later `\[` → `$$` substitution over that output turned
  `\EE\[\theta_i \mid X\]` into `\EE\[\theta_i \mid X$$`. The maths is now lifted out before
  pandoc sees the file. 360 pages fixed.
- **knitr's LaTeX highlighting** (`\begin{Shaded}` with `\NormalTok{}` macros) rendered R code as
  bold prose — `m1 <- **lm**(lpsa ** ** 1, ...)`. Rewritten as `verbatim` before conversion.
- **Chapter-sized pages.** The old splitter accepted a heading level whose sections *averaged* 400
  characters, so one long section dragged a crowd of stubs over the bar. It now splits on the top
  level only and merges thin parts into their neighbours — forwards as well as backwards, because
  an exam PDF opens with a letterhead that otherwise becomes a page of nothing.
- **Transcripts have their own subtree.** `recordings/` — a directory that alternated
  `01-captions`, `01-slides`, `01-transcript` told a reader nothing. A `.srt` now also beats a PDF
  of the same transcript: 118 duplicate documents dropped.
- **Currency is not mathematics.** `$50 million` in a problem set opened a maths span that never
  closed and swallowed the rest of the page. Unmatched dollars are escaped structurally, by
  locating the valid spans first.
- **`normalise_names.py` is idempotent**, so `-transcript-transcript` stops leaking into published
  URLs.

### The PDF route is now a model

`pymupdf4llm` produced 55% of the old corpus and almost none of it was readable. It is kept as the
**cross-check**, not the output: a PDF with no better source goes to a multimodal model, natively
rather than as rendered images (574 input tokens per page against 1,179, for equal quality).

It is inference, so it is fenced — a labelled `route`/`fidelity`, a banner saying every equation is
unverified, a word-recall check against the parser wherever the parser's text is credible, and a
committed cache so regeneration does not re-roll the model.

- **`llm_pdf.py`** — the route, the cross-check and the cache.
- **`llm_batch.py`** — the same at half price through the Batch API. Note: a batch request that
  *references* a Files API upload returns `code=7, 'The caller does not have permission'` for every
  response while the job still reports `SUCCEEDED`. The bytes must be inlined.
- **Neither a dry run nor `--apply` calls a model.** The corpus is converted from the batch cache;
  `--llm-sync` opts in. An `--apply` that quietly spent money on 172 PDFs is the accident this
  prevents.
- **Failures are never cached.** An empty answer is a rate limit or a 503, not a fact about the
  document, and caching it would make one bad minute permanent.
- **The cross-check does not run without a credible baseline.** On a scan the parser emits
  fragments a correct transcription will never contain, and scoring the model against them punishes
  it for being better than the parser — the handwritten Stat 210A lecture, transcribed cleanly,
  scored 80% and would have been thrown away.


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
