# Conventions

*Draft v2, from the owner interview of 2026-10-02.* These are the numbered rules behind
[PHILOSOPHY.md](PHILOSOPHY.md). Cite rules by ID in every agent prompt, validator message, commit and
decision-log entry, for example "per L-06".

**How to read a rule.** Each rule gives what must hold, a **default** for the cases it leaves open, an
**example** where the shape isn't obvious, and how it is **checked**:

- **V**: the validator enforces it (`validate_pages.py`; the gate is named after the rule ID).
- **R**: the independent review agent checks it.
- **H**: the owner checks it at a gate (G-04).

**When no rule covers a case,** apply G-01.

**Vocabulary.**

| Term | Meaning |
| --- | --- |
| *spine* | the one set of notes whose text forms a course's core |
| *supplement* | any other source attached to the course |
| *core* | the spine converted faithfully |
| *study layer* | every block we write |
| *key result* | a definition or theorem used later in the course or named in a hub |
| *anchor* | the stable id of a numbered block |

---

## S — Sources and rights

**S-01 What is published in full.** Material that its **author posted online** is converted and
published whatever its licence. That covers lecture notes, slides, homework, solutions, scribe notes,
theses (any CC variant, ND included) and free book drafts. The licence is recorded *as found*, for
attribution only. Being somewhere on the internet is not enough: the copy has to come from the author
(S-05). *Default:* if a file's class or its poster is unclear, classify it per file in the lockfile and
open a question. *Check:* V `S-01-publish-basis`: the front matter carries `basis:` and `posted_by:`.

**S-02 What is never published.** Commercially published books, and any copy of a book not posted by its
author, are never converted. A paper is published in full only under an open licence; otherwise it gets
a summary (G-06). A third-party publication shipped inside a course is excluded per file with `exclude:`.
*Check:* V. `publish_decision()` returns `full | summary | never`, and no `never` source has a page.

**S-03 Attribution.** Every page records, in its front matter and in a one-line banner: the author(s),
institution, course and term, original URL, retrieval date, licence as found, and the takedown link.
*Check:* V `S-03-attribution`.

**S-04 Takedown.** `TAKEDOWN.md` says how to ask. `takedowns.yml` records each removal with its date and
reason, and a source listed there is never collected or emitted again. *Check:* V.

**S-05 Posted by the author.** Under S-01, the source must be fetched from a place its author
controls or chose:

- the author's own page;
- the official page or repository of a course the author teaches;
- the author's institution, including thesis repositories;
- arXiv.

Scribe notes count when the course instructor posts them on the course page, or the scribe posts them on
their own page. A mirror, an aggregator, or a copy on someone else's course page does not count: find the
author's copy, or open a question. *Example:* `~aldous/205B/bmbook.pdf` is the Mörters–Peres draft
posted by Aldous, not by its authors, so it qualifies only if fetched from Mörters's or Peres's own page.
The Stanford 310 notes linked from Aldous's page must be fetched from the Stanford author's page.
*Check:* V (`posted_by:` is set and names the author, instructor or institution); R (that it is true).

## C — Collection

**C-01 Source census.** Every course in scope has `courses/<id>.yml`, listing every candidate source:

- every offering in the last 10 years;
- every instructor's personal page;
- the course's GitHub organisation;
- scribe notes;
- notes the course pages link to, followed one hop out.

Each candidate has a status: `spine`, `supplement:<role>`, `rejected:<reason>` or `not-found`. A search
that found nothing is recorded too. *Check:* V (the census exists and every source has a status).

**C-02 Search recipe.** The recipe lives in `skills/collect-materials/references/discovery.md`. Run every
step, and log the queries in the census:

1. Search `site:<dept domain> "<course number>" lecture notes`.
2. Search each instructor's name with "lecture notes".
3. Check every instructor's `~user` page.
4. Follow every link on the course pages one hop out.
5. Check arXiv and GitHub for a `.tex` source of each candidate.

*Example of what a skipped step costs:* Zhivotovskiy's 210B notes and the Stanford 310 notes were missed
in 2026-09. *Check:* R.

**C-03 Gap fill.** When a hub's courses are done, any hub topic still without a treatment gets the best
free notes from any university, Russian ones included (G-05). They are recorded in the hub file with the
reason they were chosen. *Check:* R.

**C-04 Upstream updates.** A monthly CI job compares checksums for every spine source. A changed source
is re-converted, and study records re-anchor through their fingerprints (L-10). The run is logged. Any
record that no longer anchors goes stale and becomes an open question. *Check:* V.

**C-05 Lockfile safety.** `lock_sources.py` may overwrite only the keys the scanner owns: `files`,
`bytes`, `contents`, `commit`, `branch`, and a licence that came from the scan. Every other field,
including a licence resolved by hand, is preserved. An entry the scan can't find is kept and marked
`missing_locally: true`. *Check:* V (test).

## P — Spine and course structure

**P-01 Choosing the spine.** Score the candidates on these criteria, in order:

1. coverage of the course syllabus;
2. completeness (no missing lectures);
3. a source format exists (`.tex`/`.qmd` beats PDF);
4. recency;
5. clarity.

Record the scores in the census. *Default:* the top score wins, and the choice is logged. A tie, or a
best candidate covering under 70% of the syllabus, becomes an open question.
*Check:* V (exactly one spine per course); R (the scores).

**P-02 Supplements never interleave with the core.** A supplement contributes only through placement
records, and its verbatim blocks are labelled `kb-course` with their source:

- the course's own exercises;
- alternative proofs;
- extra examples.

A supplement can also be a book of its own (e.g. Stanford 310). *Check:* V `P-02-provenance`.

**P-03 Chapter order follows the spine.** The spine's order (its PDF outline, or its sections) is the
chapter order. Syllabi, admin pages, exam papers and lorem ipsum never become chapters. Exams and
homework go into the exercise pool. *Check:* V `P-03-book-shape`.

**P-04 Stable URLs.** Course paths are fixed in the manifest (`path:`) and never move. Hub pages live at
the existing discipline directories. When a chapter URL changes, `redirects.yml` maps old to new; it is
generated and served by a build hook. The snapshot of inbound knowledge-base URLs must always resolve.
*Check:* V `P-04-url-stability`.

## F — Faithful core

**F-01 Convert the source, not the render.** Use `.tex`, `.qmd` or `.Rmd` whenever one exists. Before
transcribing a PDF, look for its source (C-02 step 5). *Check:* V.

**F-02 Transcription is measured, page by page.** Transcribe a PDF in chunks of 4–8 pages. A
transcription is `ok` only when all of these hold:

- every chunk finished normally, with all output parts joined;
- `<!-- page N -->` markers are present once each, in order;
- on credible pages (≥ 400 characters of extractable text), the character ratio against the
  extracted text is ≥ 0.6 and word recall is ≥ 0.85, and ≥ 0.90 over the whole document;
- 100% label recall: every `Theorem/Lemma/Definition/Example/Exercise N.M` in the extracted text
  appears as a numbered block;
- non-credible pages have ≥ 150 characters, unless the page is marked `figure-only` or `blank`.

Failing chunks are re-split (8 → 4 → 1 pages) and redone. A page that still fails becomes an open
question. Paraphrase is never accepted. *Check:* V. Every cache record carries `measured: true`;
`audit_cache.py` re-measures legacy records.

**F-03 The core is never edited by hand.** Repairs run as a re-runnable pass, and every repaired
expression is marked. The study pass never receives a writable copy of the core. *Check:* V
`F-03-core-drift`: strip study blocks, wrappers and `[x](#anchor)` links from the emitted page, re-hash,
and compare with `core_sha`.

**F-04 Author numbering is kept and anchored.** Numbered environments become `pymdownx.blocks` with the
author's number and a stable id:

- numbered: `thm-2-3`, `def-3-1`, `lem-4-2`, `eq-4-7`;
- unnumbered (as in scribe notes): `thm-c3-u2`.

No visible number is ever invented. *Example:*

```
/// kb-theorem | Theorem 2.3 (Bernstein's inequality)
    attrs: {id: thm-2-3, class: kb-core, data-kb-src: "p14"}
Let $X_1,\dots,X_n$ be independent …
///
```

*Check:* V `F-04-anchor-grammar` (ids unique page-wide, raw-HTML ids included).

**F-05 Proofs are collapsed.** Every author proof is reproduced verbatim inside a closed `kb-proof`
details block, behind a "try it first" prompt and at least two hints (see L-06). *Check:* V
`F-05-proof-wrapped`.

**F-06 Author figures.** A figure in the notes is cropped from the original page region and captioned
"from the original, p. N". The crop is inverted in dark mode by CSS. A figure that cannot be cropped
cleanly is redrawn as one of ours, captioned "redrawn from Fig. X of the notes". *Check:* V (every
figure reference resolves); R.

**F-07 Mark only real doubts.** "Unverified" marks go only where a check failed. There are no blanket
banners. *Check:* V.

**F-08 Disclosure.** The front matter names the route and model and stores the per-page check results.
The banner says either "transcribed by a model from the author's PDF, checked page by page" or
"converted from the author's source". *Check:* V.

## L — Study layer

**L-01 Written for the owner.** Build on the anchors in the knowledge base's `profile.md`:

- spectral and Gram geometry, and PCA;
- HMMs and filtering;
- birth–death processes and the CME;
- 10x count data and its artefacts.

Write in the second person, and directly. Leave out introductory filler, and don't explain what the
reader already holds. The study layer is always in English (G-05). *Check:* R.

**L-02 Every block we add is typed and labelled.** The types are `kb-roadmap`, `kb-intuition`,
`kb-example`, `kb-exercise`, `kb-hint`, `kb-solution`, `kb-connection`, `kb-note`, `kb-recap` and
`kb-figure`. Each carries `kb-study` and a `data-kb-rec` record id, and shows a badge reading "Study
note — written by M, checked by M′". No prose sits outside a block, except the core and generated
headings. *Check:* V `L-02-unlabelled-study`.

**L-03 Roadmap first.** Every chapter opens with `## Roadmap`, which covers:

1. the prerequisites, linked through the hub's `needs`;
2. the question the chapter answers;
3. where it leads: the next chapter and the hub topic;
4. the generated "In your knowledge base" links (K-02).

*Check:* V `L-03-roadmap`.

**L-04 Motivation before every key result.** A `kb-intuition` block sits immediately before each key
anchor. It gives the problem that forces the result and how someone could have come up with it, using an
L-01 anchor where one fits. Minor lemmas get none. *Check:* V `L-04-intuition` (every anchor with
`key: true` has one); R (quality).

**L-05 Pictures where they carry the argument.** Each key result has a figure (V-rules) or `figure: none`
with a reason, and each chapter has at least one figure. *Check:* V; R.

**L-06 Practice with hint ladders.** Each chapter has 4–8 exercises in its `## Practice` section:

- The course's own exercises come first, from any offering, verbatim through placement.
- We write exercises only to fill the gap.
- Every exercise has at least two collapsed hints (the idea, then the key step) before its collapsed
  solution.
- A solution never appears above its exercise.

*Check:* V `L-06-practice`.

**L-07 Connections.** Each chapter has a `## Connections` section of 3–10 items, using at least two
tags. Every link resolves.

| Tag | Points to |
| --- | --- |
| `same-course` | another chapter of this course |
| `other-course` | a library anchor |
| `external` | Wikipedia, a DOI, arXiv, or other notes |
| `application` | computational biology or single-cell, only where the application is real |

*Check:* V `L-07-connections`.

**L-08 Recap is optional.** If present, it is a table of results with their anchors. *Check:* V (format).

**L-09 Accuracy.** Everything we add is checked before it ships:

- **Numbers.** Every number in our prose is computed, written as `{{kbnum:<figure>.<key>}}` and
  resolved from committed figure code.
- **Arguments.** Every solution, worked example, derivation and intuition argument is verified by a
  checker agent. The checker is a different model from the writer, and it never sees the writer's
  reasoning.
- **Verdicts.** Verdicts live in `conversion-cache/verify/`, keyed by record id and record hash.
  Editing a record invalidates its verdict.
- **Gate.** Unverified records are not emitted.

*Check:* V `L-09-unverified`.

**L-10 Records point at anchors.** A study record stores `anchor` and `anchor_fp`, a fingerprint of the
normalised statement. If the fingerprint no longer matches after re-transcription, the record is stale.
It is reported and withheld, never silently re-attached. *Check:* V `L-10-stale-record`.

## V — Visuals

House style is the Cellanome kit, ported to `docs/stylesheets/kb.css`. Its tokens, `--kb-ink`,
`--kb-muted`, `--kb-accent`, `--kb-c1…c6`, `--kb-grid` and `--kb-fill-soft`, are defined on
`[data-md-color-scheme="default"]`, with dark pairs on `[data-md-color-scheme="slate"]`. The fonts are
IBM Plex Sans and IBM Plex Mono.

**V-01 Three kinds of figure, one frame.** The kinds are `plot` (computed), `diagram` (hand-authored) and
`widget` (interactive). Each sits in the same frame:

```
figure.kb-panel > figcaption.kb-cap > div.kb-art > svg
```

The caption is "Figure N.M" plus what to see, and an `aside.kb-note` may follow. *Check:* V `V-01-frame`.

**V-02 Plots come from code.** Each plot is `figures/src/<hub>/<id>.py`, which defines
`render() -> (svg, numbers)`.

- **Drawing.** Plots are seeded, deterministic, and drawn with the in-house `kbfig` primitives in kit
  classes. `kbfig.from_matplotlib()` is the escape hatch for heatmaps and contours.
- **Provenance.** The emitter inlines each plot with `data-kb-src` and `data-kb-sha`.
- **CI.** CI re-renders every plot and fails on any drift.

*Check:* V `V-02-plot-provenance`.

**V-03 Diagram rules.** A diagram uses kit classes only:

- no fill or stroke colour literals (only `none` or `currentColor`);
- no `<style>`, `<script>` or `<foreignObject>`;
- `viewBox` is `0 0 320 180` or `0 0 640 180`;
- `role="img"` plus an `aria-label`;
- ids are prefixed with the figure id;
- arrows use the per-page `kb-arr` sprite marker.

*Check:* V `V-03-figure-kit`.

**V-04 Widgets: sliders and simulators only.** Two kinds are allowed:

- **Parameter slider:** change n, σ or t and watch a bound, density or rate move.
- **Simulator:** run a random walk, Poisson arrivals, Gillespie or martingale paths, with resampling
  and an empirical-against-theory overlay.

Do not build step-through constructions or quizzes. Use at most two widgets per chapter, and only for
key results.

How widgets are built:

- The default is the in-house `kb-svg.js`, the JavaScript twin of `kbfig`, so a static fallback and its
  live widget look the same. Vendor Observable Plot only when a widget needs scales or binning.
- Mount from `document$.subscribe`, so widgets survive instant navigation.
- The static fallback, rendered by the Python twin at the default parameters, is what you see without
  JavaScript.
- Use native `<input type=range>` with labels, and announce changes through `aria-live`.
- Widget maths is pure functions, tested in CI against the Python twin.

*Check:* V (a fallback exists, and `node --test` passes); R.

**V-05 Maths in figures renders or is forbidden.** Captions and notes are rendered at emit time with
arithmatex, so `$…$` becomes a typeset span. SVG `<text>` holds Unicode only (θ, ‖x‖², Σ, via
`unicodeit`). Heavier notation goes in a `div.kb-legend` below the art. *Check:* V `V-05-svg-maths`: no
`$` or `\cmd` in `<text>` or `<tspan>`, and no raw `$` in a built `figcaption`.

## H — Hubs and navigation

**H-01 Hub files.** `hubs/<id>.yml` holds:

- an overview;
- 20–40 `nodes`, each a syllabus section, not a single theorem, with `needs` (prerequisite edges) and
  `covered_by` (course anchors, best treatment first);
- the `route` overlay of knowledge-base `path.md` nodes;
- `gaps`, which is the C-03 queue.

Every chapter belongs to at least one node. *Check:* V `H-01-hub-shape`.

**H-02 Hub pages are generated.** Each hub page shows:

- the overview;
- a computed prerequisite graph, with nodes as links and the route highlighted;
- a topologically ordered list, which is also the version without JavaScript;
- the courses and the gaps.

*Check:* V.

**H-03 Landing page.** Hubs first, then courses, then papers. *Check:* V.

**H-04 Level never excludes a course.** Whether a course is included depends on its substance, never on
its level. A full course labelled "introductory", such as MIT 6.041SC, gets the full treatment. *Check:*
R.

**H-05 Starting taxonomy.** This list is revisable only through an open question:

1. Measure-theoretic probability
2. Conditioning & martingales
3. Markov chains & processes
4. Brownian motion & stochastic calculus
5. Concentration & high-dimensional probability
6. Mathematical statistics
7. Asymptotics & empirical processes
8. Time series
9. Causal inference
10. Experimental design
11. Statistical computing
12. Stochastic gene expression & chemical kinetics
13. Computational-biology algorithms
14. Omics statistics
15. Probability (non-measure-theoretic)

## G — Governance

**G-01 When the rules run out.** A cheap, reversible call follows the nearest default and is appended to
`decisions/log.md` as `date · rule ID extended · decision · why`. Anything about publication, deletion,
restructuring, a spine tie or a hub change becomes a GitHub issue:

- labelled `open-question`, with the rule ID in its title;
- the item is skipped until the issue is answered;
- the answer is copied into the log.

*Check:* V (the log is append-only and well-formed; no page exists for an item blocked by an open
question).

**G-02 Generated only.** `docs/` is emitted from the cache and is never edited by hand. Commit once per
run, naming the course and the rule IDs exercised. *Check:* V.

**G-03 Cite rules.** Every agent prompt and validator message cites rule IDs. A rule that can't be cited
is split or removed. *Check:* R.

**G-04 Pilot gate.** A new or changed rule is applied to the pilot first, and spreads only after the
owner signs off in `decisions/log.md`. *Check:* H.

**G-05 One language per block.** A Russian spine stays in Russian and is not translated. The study layer
is always in English. *Check:* V.

**G-06 Paper summaries.** A paper summary follows the chapter kit, scaled down:

- a roadmap;
- key equations, written by us;
- one figure of ours, where it helps;
- 3–10 typed connections.

The paper's text and figures are never reproduced unless its licence is open. *Check:* V
`G-06-paper-shape`.

**G-07 Who does what.** Claude does all of it. Each agent's prompt cites the rules it applies.

| Agent | Job | Rules |
| --- | --- | --- |
| `source-census` | builds the census | C-01, C-02 |
| `pdf-to-markdown` | transcribes PDFs | F-02, F-04, F-06 |
| `study-writer` | writes `study/` records only | L |
| `figure-author` | plots, diagrams, widgets | V |
| `study-verifier` | checks study records; a different model from the writer | L-09 |
| `paper-summary-writer` | paper summaries | G-06 |

*Check:* R.

## K — Knowledge-base boundary

**K-01 Split by authorship.** The library holds the author's text plus our study layer. The knowledge
base holds what its owner produces: questions, trajectories, derivations, logs and verdicts. Its
`adapt-material` skill and `adapted/` folder are retired. `path.md` nodes and catalogue entries link to
hub nodes and chapter anchors. *Check:* R.

**K-02 Backlinks are generated.** A build step reads the knowledge base's outbound library links and
writes the "In your knowledge base" line in each chapter's roadmap. Neither side is hand-edited. The
knowledge base's weekly link check stays. *Check:* V.
