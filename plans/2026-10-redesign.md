# Library redesign: plan (2026-10)

The rules this plan carries out are in [PHILOSOPHY.md](../PHILOSOPHY.md) and
[CONVENTIONS.md](../CONVENTIONS.md). Rule IDs below, such as F-02, refer to them.

## Why

As a study resource, the library fails in four ways.

### Material is missing

STAT 210B is a syllabus page, although Zhivotovskiy's 134-page LaTeX notes are posted on his own page
(<https://www.stat.berkeley.edu/~zhivotovskiy/Stat210BLectureNotes.pdf>). 201A, 205A, 205B, 206A/B,
150, 158, 201B and 230A are syllabus pages or lorem ipsum. There are three causes:

- **Sources were found only by a one-off manual pass.** It never found `~zhivotovskiy` or the Stanford
  310 notes linked from Aldous's page.
- **A default-deny licence gate** (`may_adapt()` and `destination()`, `normalise_source.py:91-102` and
  `:417-444`) blocked every instructor page.
- **Transcriptions were silently truncated.**
  - 151 tracked and 115 withheld cache records of 3 or more pages have fewer than 400 characters per
    page, yet are marked `ok, recall 1.0`.
  - The worst cases: Guntuboyina 210B, 158 pages → 126 characters; Chewi 205A, 105 pages → 1,064
    characters.
  - Probable cause: `parts[0]` only (`llm_batch.py:267`), and an unchecked `finish_reason`.

### The books are broken

- stat153 (128 chapters) and stat210a (83 chapters) concatenate five course offerings. Duplicate
  lectures appear several times, the course opener is chapter 108, exams count as chapters, and some
  pages are lorem ipsum.
- Across 473 chapters there are 0 cross-links and a single admonition.
- Only 124 chapters have exercises.
- Only 6.041SC has solutions, and those are raw OCR.

### The figures are disappointing

- All 460 figures are schematics drawn by a model; the original plots were lost.
- 141 captions and 182 SVG labels show raw `$…$`.
- `body_rules.tidy_svg` corrupts `>=`. The damage is live in stat153 chapter 22.

### Agents have to guess

The rules lived in a long narrative `AGENTS.md`, so each agent had to work out what applied.

## Decisions (owner interview, 2026-10-02)

| # | Decision |
|---|---|
| D1 | **Rights.** Material its author posted online is published, whatever its licence: lecture notes, slides, homework and solutions, scribe notes, theses, and free book drafts (S-01, S-05). Commercially published books are never converted. A paper's full text is published only under an open licence; any paper may be summarised. |
| D2 | **Structure.** Subject hubs (standard map plus a `path.md` overlay) over per-course books. |
| D3 | **Book model.** Faithful core plus a study layer that is clearly marked as ours. |
| D4 | **Spine.** The best author notes form the spine. Other offerings supply the study layer. |
| D5 | **Every chapter** has a roadmap, intuition and figures before key results, exercises, and connections. A recap is optional. |
| D6 | **Proofs** are collapsed behind a try-first prompt and a hint ladder. |
| D7 | **Density.** Every key result gets a study block. Each chapter has 4–8 exercises and 3–10 connections. |
| D8 | **Accuracy.** Everything we add is labelled. Numbers are computed by code. Arguments are checked by an independent agent. |
| D9 | **Visuals.** Computed plots, widgets, and kit diagrams. The Cellanome kit is the house style. |
| D10 | **Gaps in the rules.** Cheap calls: take the default and log it. Calls with high stakes: ask and wait (G-01). |
| D11 | **Rules are documented** as PHILOSOPHY plus numbered CONVENTIONS. AGENTS.md becomes an index. |
| D12 | **The study layer is written for the owner**, using the anchors in `profile.md`. |
| D13 | **The library absorbs adaptation.** The KB's `adapt-material` skill and `adapted/` folder are retired. |
| D14 | **Sourcing.** Courses first, then hub gaps from any university. |
| D15 | **Order.** Pilot the probability ladder, then 210B, then rebuild the 12 existing books worst-first. |
| D16 | **Execution happens on the Mac.** |
| D17 | **A Russian spine stays in Russian.** The study layer is in English. |
| D18 | **Paper summaries become study-style** (G-06). |
| D19 | **Open questions are GitHub issues** labelled `open-question`. |
| D20 | **Widgets** are sliders and simulators only. **6.041SC gets the full treatment** (H-04). |
| D21 | **Claude does everything:** transcription, writing, figures and checking. The verifier is a different Claude model from the writer. Gemini routes become legacy cache readers only. |
| D22 | **Backlinks.** The library gets generated backlinks into the KB, and spine updates are detected monthly. |

### Rights note

Author-posted is still not a licence. These rules reverse the 2026-10-02 Track-A containment for
author-posted material, and the owner has accepted that. The safeguards:

- S-03: attribution on every page.
- S-04: a working takedown process.
- S-05: the source must be fetched from the author's own copy.

## Architecture

### Three programs, three layers

The core can never be rewritten by the study pass, because each layer has its own writer:

- `build_core.py` writes `conversion-cache/core/<course>/<NN-key>.md` and `.anchors.json`. It is
  deterministic and committed.
- The study agents write only `conversion-cache/study/<course>/<NN-key>.json`. These are records that
  point at anchors.
- `emit_book.py` merges the two into `docs/` and stamps `core_sha`. The F-03 gate re-hashes the core
  after stripping every study block, so any drift is caught.

Books are built from the cache, never from `docs/`. That removes the v1 coupling where `write --apply`
deleted the converted pages its own planner read (`synthesise_book.py:233`, `:866-870`).

### New files

```
courses/<id>.yml                 census, spine, supplements, roles, pinned path (C-01, P-01..04)
hubs/<id>.yml                    nodes (syllabus sections), needs, covered_by, route overlay, gaps (H-01)
conversion-cache/core/…          faithful core and anchor table (F-02..08)
conversion-cache/study/…         typed study and placement records (L-02..10)
conversion-cache/verify/…        verdicts keyed by record id and record hash (L-09)
conversion-cache/audit/<date>.tsv   truncation audit (audit_cache.py)
figures/kbfig/  figures/src/<hub>/<id>.py  figures/build/   plot toolchain (V-02)
docs/stylesheets/kb.css  docs/javascripts/kb/{index.js,kb-svg.js,widgets/}   kit and widgets
hooks/redirects.py  redirects.yml  site-urls.lock  kb-inbound-urls.txt   URL stability (P-04)
decisions/log.md  TAKEDOWN.md  takedowns.yml   (G-01, S-04)
```

### Markdown

`pymdownx` 11.0.2 is already pinned. Its `pymdownx.blocks.admonition` and `.details` accept custom
`types:` and `attrs:` (ids, classes, `data-*`). Fenced `///` blocks keep display maths and lists safe
from LLM indentation errors.

The transcription prompt emits pandoc fenced divs:

```
::: {.theorem number="2.3" title="Bernstein"}
```

`build_core.py` turns these into `/// kb-theorem` blocks with `attrs: {id: thm-2-3, …}`. For `.tex`
sources, add `+fenced_divs` to the pandoc target at `normalise_source.py:648`.

Emitted chapter skeleton:

1. Front matter and banner (S-03, F-08).
2. `## Roadmap`
3. The author's sections. Each key anchor is preceded by a `kb-intuition` block. Each proof is a
   closed `kb-proof` block containing hints and then the verbatim `kb-proof-full`.
4. `## Practice`
5. `## Connections`
6. `## Recap` (optional)
7. `## Sources`, generated, with `#page=` links per anchor.

### Figures

- **Maths in captions.** Rendered at emit time with Python-Markdown and arithmatex, which yields typeset
  spans with no `md_in_html` dependency.
- **SVG text.** Unicode only, produced by `kbfig.label()` through `unicodeit`.
- **Crops.** Author figures are crops taken with pymupdf `get_pixmap(clip=…)` at the `[[figure pN #k]]`
  markers in the transcription.
- **Widgets.** In-house `kb-svg.js`, the JS twin of `kbfig`, mounted from `document$.subscribe` with an
  AbortController. Observable Plot is vendored and pinned only if a widget needs it.
- **CI.** `figures/build.py --check` and `node --test tests/widgets`.

### `mkdocs.yml`

- `theme.font`: IBM Plex Sans and IBM Plex Mono.
- `pymdownx.blocks.admonition`, with types `kb-definition`, `kb-theorem`, `kb-lemma`,
  `kb-proposition`, `kb-corollary`, `kb-example`, `kb-remark`, `kb-exercise`, `kb-roadmap`,
  `kb-intuition`, `kb-note`, `kb-recap`.
- `pymdownx.blocks.details`, with types `kb-proof`, `kb-proof-full`, `kb-alt-proof`, `kb-hint`,
  `kb-solution`.
- `pymdownx.blocks.html` and `md_in_html`.
- `extra_css: stylesheets/kb.css`.
- `extra_javascript`: `javascripts/kb/index.js` (a module), alongside the existing MathJax setup.
- `hooks: [hooks/redirects.py]`. The redirect map is generated, so it stays out of the hand-written
  config.

### Publishing gate

Replace `may_adapt()` and `destination()` with `publish_decision(entry, file) -> full | summary | never`,
per S-01, S-02 and S-05:

- **Lockfile fields.** `basis:` and `posted_by:`, plus per-file `material` overrides.
- **Takedowns.** `takedowns.yml` always wins.
- **Same gate everywhere.** It applies to `llm_batch.pdfs_to_convert` (`:79`) and to figure extraction
  (`FIGURE_LICENCES`, `:1460`).
- **What `MAY_ADAPT` still does.** It survives only for share-alike propagation (`book_licence`,
  `:404`).

## Phases (all on the Mac)

**Phase 0: safety fixes, before anything else.** No model spend. Each fix gets a regression test under
`tests/`.

1. Fix `body_rules.tidy_svg` (`:135-158`). Substitute only in text nodes and attribute values, then
   re-emit stat153 chapter 22.
2. Add a `join_base()` helper and use it in `restore_sources.py:88` and `normalise_source.upstream()`
   (`:376-377`). The bug produces wrong *published citations*, not only failed restores.
3. Fix `lock_sources.py` (C-05).
   - Detect ND licences first (`:117-127`).
   - Invert `merge()` (`:211-235`) so the scanner owns only its own keys.
   - Keep entries that are missing locally.

   This must land before Dembo or Zhivotovskiy is locked.
4. Fix `llm_pdf` and `llm_batch`.
   - Join all output parts and record `finish_reason`.
   - Never cache output that did not stop normally.
   - Re-measure on a cache hit when `measured` is absent (`llm_pdf.py:278-289`).
   - Apply `exclude:` in `pdfs_to_convert` (`:63-100`).
   - Use 8-page chunks: `PAGES_PER_CALL = 8` is currently unused; `:300` and `:121` both use 40.

   These fixes stop bad legacy records from publishing.
5. Guard `normalise_source.py`.
   - Scope `--clean` (`:1843-1850`).
   - Refuse `rmtree` on a written book (`:1357-1358`).
6. In `synthesise_book.cmd_submit` (`:471-505`), add the `cmd_tasks` guards (`:437`), and refuse any
   course that has a `courses/<id>.yml`.
7. Write the new `audit_cache.py` (F-02), which re-measures the tracked and withheld caches and writes
   the TSV.
8. Interim fix for the live site, at no model cost: emit-time caption rendering plus the `tidy_svg` fix,
   applied in the current write path (`synthesise_book.py:816`).

**Phase A: rules in force.**

1. Commit PHILOSOPHY.md and CONVENTIONS.md.
2. Reduce `AGENTS.md` to an index of rule groups.
3. Retire `book-template.md` and `page-template.md` in favour of rule references.
4. Add `decisions/log.md`, `TAKEDOWN.md`, `takedowns.yml` and the `open-question` label.
5. Implement `publish_decision()`.
6. Restore withheld records only if they pass the audit and the publishing gate.
7. Add a CHANGELOG entry.

**Phase B: toolchain.**

1. Scripts in `skills/normalise-materials/scripts/`. Each new script reuses existing code:

   | New script | Reuses |
   | --- | --- |
   | `kb_model.py` | — |
   | `transcribe.py` | `llm_pdf.cache_key`, `pdf_slice`; `group_documents`/`candidate_files` (`normalise_source.py:479/461`) |
   | `build_core.py` | `convert_one` (`:766`), `normalise_body` (`body_rules.py:501`), `split_sections` (`:873`), pymupdf `get_toc()`, adapted `extract_document_figures` (`:1468`) |
   | `study.py` | the `cmd_tasks` hand-off pattern (`synthesise_book.py:418-468`) |
   | `emit_book.py` | `_course_provenance` (`:658-702`), `_written_on`, the dollar repair (`:816-823`), the offerings table (`:892-917`), `repair_dangling_links` (`:1595`), `write_nav` (`:1630`), `write_library_index` (`:1702`, plus a hubs section) |
   | `emit_hubs.py` | — |

2. Figures, widgets and the kit CSS.
3. The `mkdocs.yml` changes.
4. `validate_pages.py` v2, with one gate per V rule. v1 books keep the current `book-shape` gate until
   they are rebuilt.
5. CI: figures `--check`, `node --test`, validator v2, then the build.
6. Agents (G-07), each prompt citing rule IDs.
7. A demo page that exercises every block type, in both themes.

**Phase C: pilot, the probability ladder.**

1. **Census** for 205A, 205B and 150 (C-01, C-02), plus Stanford 310 fetched from its author's page
   (S-05).
2. **Classify every file** in the instructor-page sources, per file.
   - Likely papers, which get summaries only: `511.pdf`, `austin_arrays.pdf`, `pitman_yor_guide_bm.pdf`,
     `me134_monthly.pdf`.
   - Open questions: `BZ.pdf`; `bmbook.pdf` (S-05: needs the authors' copy); `takis_exercises.pdf`,
     `coincidence_chapter.pdf`, `entropy_chapter.pdf`.
   - `205A/notes.pdf` is byte-identical to `205B/kernel.pdf`.
3. **Manifests.** Likely spines:

   | Course | Likely spine (confirm with P-01 scores) |
   | --- | --- |
   | stat205a | `sinho_chewi_notes.pdf` (105 pages, pdfTeX) |
   | stat205b | `chewi_notes.pdf` (104 pages; the current record is suspect at about 388 characters per page) |
   | stat150 | Aldous's 30 `lecture_*_post.pdf` vs Au's five offerings vs Gorin's 2026 site. 12 of Aldous's are truncated in the cache. Likely an open question. |
   | stanford-stat310 | its own book |

4. **Transcribe** the spines, honouring F-02.
5. **Build the core.** Each chapter plan goes to the owner as an open question.
6. **Port the kit** and build three widgets: Markov-chain convergence, Poisson process / birth–death, and
   LLN/CLT.
7. **Study layer.** Write, verify and emit each chapter.
8. **Hubs 1–4** with the `path.md` overlay, nodes 1–7.
9. **Acceptance test** (below), run on 205A before 205B, 150 and 310. This is the G-04 sign-off.

**Phase D: STAT 210B.**

- **Census:** Zhivotovskiy 2026, Guntuboyina 2018 (re-transcribe; the cached copy is 126 characters),
  van der Laan, Song Mei 2025 (bCourses only).
- **Spine:** probably Zhivotovskiy. Split it by the PDF outline, and ask the author for the `.tex`.
- **Hub:** hub 5.

**Phase E: rebuild the 12 existing books, worst first.**

1. stat153: `.qmd` sources, so a lossless core.
2. stat210a.
3. 8.591J-2014: no notes, so the spine is an open question.
4. The remaining books, 6.041SC included.

Each rebuild gets a manifest, `replaces_urls` and redirects. Then convert the 41 paper summaries to
G-06, then fill each hub's gaps (C-03).

**Phase F: knowledge-base side** (`Claptar/knowledge-base`).

1. K-01 in its `AGENTS.md`.
2. Retire `adapt-material` and `adapted/`.
3. Link `path.md` nodes and catalogue entries to hub nodes and chapter anchors.
4. Add Zhivotovskiy and Stanford 310 to `resources/berkeley-statistics.md`.
5. Fix the stale licence lines the audit found.

## Risks

- **Refusals.** A model may refuse to transcribe full texts it treats as all-rights-reserved.
  - Mitigations: per-page chunks, the `basis`/`posted_by` stated in the task, and gates that reject
    paraphrase.
  - Persistent refusals become open questions.
- **Rights exposure.** Third-party files sit inside instructor pages, and git history still holds text
  that was previously withheld.
  - Mitigations: per-file classification (S-01, S-05) and the takedown process (S-04).
- **Anchor drift on re-transcription.** Mitigation: fingerprints and stale records (L-10). A record is
  never silently re-attached.
- **A core built from a PDF is still a reconstruction.** Mitigations: disclosure (F-08), with label recall
  as the strongest mechanical check.
- **Cost.** Density × 473 chapters, doubled by verification.
  - Measure the cost per chapter in the pilot before starting Phase E.
- **Over-built hubs.** Keep them at syllabus-section granularity (20–40 nodes), derived from syllabi.
- **Platform.** Ids inside raw HTML escape `--strict`, so the validator must cover them. MkDocs is pinned
  below 2.
  - Page weight: keep the largest page under about 300 KB.

## Verification and pilot acceptance test

Run on 205A, the Probability hubs and one widget:

1. `validate_pages.py` reports zero fatal v2 findings, and `mkdocs build --strict` passes.
2. Every spine chunk stopped normally with complete page markers. Credible pages meet ratio ≥ 0.6 and
   recall ≥ 0.85, and label recall is 100% (F-02).
3. F-03 holds on every chapter: the emitted page minus the study layer equals `core_sha`.
4. Every chapter has all of these (L-03 to L-07):
   - a roadmap with a resolving prerequisite;
   - intuition before every key anchor;
   - every proof wrapped, with at least two hints;
   - 4–8 exercises with hint ladders;
   - 3–10 tagged connections.
5. Every solution and derivation record has a verified verdict with a matching hash, from a different
   model (L-09).
6. Figures (V-02, V-05):
   - `figures/build.py --check` is byte-identical;
   - no `$` or `\` appears in SVG text;
   - captions in the built site contain no literal `$`.
7. The widget:
   - shows its static fallback with JavaScript off;
   - re-mounts after instant navigation;
   - recolours on a theme toggle;
   - can be operated from the keyboard.
8. Every hub node is covered or listed as a gap, and the overlay for `path.md` nodes 1–7 links into
   anchors.
9. The KB's inbound URLs and every entry in `site-urls.lock` resolve.
10. The owner reads two chapters, one measure-theoretic and one on Markov chains, and signs off in
    `decisions/log.md` (G-04).
