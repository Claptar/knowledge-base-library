# Quality gates

**A page that fails a gate is not published.** It is named in its source's index with a link to the
original, under *Not converted* — which is the honest outcome, because a near-empty or garbled page
that looks like a conversion is worse than an absence: the next reader cannot tell the two apart.

`scripts/validate_pages.py` implements this file. It runs in two places, and they are the same code:

- **inside the converter**, as the publish decision for each candidate page;
- **over `docs/` in CI**, beside `mkdocs build --strict`, where it must report zero failures.

`mkdocs build --strict` is not a quality check. It validates links and anchors, and it passed
cleanly on a corpus where 373 pages displayed raw `<span class="math inline">\$\\tau^2\$</span>` to
the reader. That is exactly the hole this file closes.

## The two kinds of finding

**Repair** — the converter fixes it and the page ships. If a repair is not implemented yet, the
finding is fatal until it is; a known-broken page is never published on the grounds that the fix is
coming.

**Fatal** — the page does not ship, at any count above the threshold. These are conditions where the
content is not recoverable mechanically and there is nothing honest to publish.

## The gates

Counts in the right-hand column are the **baseline** measured on `main` at `b6766d7`, over 11,918
pages. They are what the rebuild is scored against, and they are all expected to reach zero.

### Fatal

| gate | why it is fatal | baseline |
| --- | --- | --- |
| `extraction-debris` — over 20% of body lines are page numbers, OCR fragments or picture text | scanned or column-scrambled beyond mechanical recovery | 1,012 pages |
| `math-span` — `<span class="math` in the body | MathJax scaffolding reaching markdown means the HTML route failed; the equations are unrecoverable without re-converting | 360 pages |
| `duplicate-body` — body hash matches another page | the same document converted twice under two paths, or a directory copied | 473 pages |
| `picture-text` — `<!-- Start of picture text -->` present | a figure destroyed into unordered OCR fragments; extract the figure instead | 932 pages |
| `thin-body` — under 400 characters of prose | there is no page here: banner, title, footer, nothing | 2,243 pages |
| `unbalanced-fences` — odd number of ``` | the page renders as one giant code block, or as none | 652 pages |
| `unbalanced-dollars` — odd `$` outside code | the rest of the page renders as mathematics | 359 pages |
| `uncited` — no `source` URL | cannot be published uncited | 1 page |
| `route: pdf` where a text-format sibling exists | the render was converted instead of the source | see `SKILL.md` |

**4,613 of 11,917 pages fail one of these.** That is the number the rebuild is scored against.

### Repair

| gate | repair | baseline |
| --- | --- | --- |
| `raw-html` — `<br>` `<sup>` `<sub>` `<span>` `<div>` `<td>` | convert or unwrap per `page-template.md` | 166,030 in 3,160 pages |
| `escaped-dollar` — `\$` | unescape; the maths never opens | 19,952 in 373 pages |
| `page-number-line` — a line that is only a number, or `Page N` / `N of M` | delete | 14,001 in 3,889 pages |
| `escaped-underscore` — `\_` | unescape; `\theta\_i` is not a subscript | 9,308 in 314 pages |
| `bold-heading` — `### **2.1 Foo**` | unwrap, recover the level the extractor lost | 6,856 in 1,244 pages |
| `extra-h1` — the body re-states a title level | demote so the shallowest body heading is `##` | 5,804 in 1,011 pages |
| `html-entity` — `&lt;` `&gt;` `&amp;` | unescape | 1,001 in 153 pages |
| `latex-bracket` / `latex-paren` — `\[ \]` / `\( \)` | convert **at the converter's input**, never by substituting delimiters afterwards | 732 in 155 pages |
| `escaped-star` — `\*` | unescape | 591 in 109 pages |
| `empty-heading` | delete, with its blank line | 249 in 122 pages |
| `hyphen-break` — a word split across a line break | rejoin | 77 in 60 pages |
| `orphan-footnote` — a reference whose definition did not survive the split | re-attach the definition, or drop the reference | 41 in 27 pages |
| `doubled-suffix` — `-transcript-transcript` | fix `normalise_names.py` idempotency and re-run | 26 paths |
| `not-an-image` — a `.pdf` or `.html` used as an image source | drop, or replace with a link | 8 in 6 pages |

The repair counts are over the 7,304 pages that pass the fatal gates — so even the survivors of the
old corpus are not publishable as they stand.

### The route census at baseline

| route | pages |
| --- | --- |
| `pdf` | **6,506** |
| `markdown` | 2,882 |
| `notebook` | 1,191 |
| `pandoc-html` | 789 |
| `pandoc-latex` | **349** |
| `transcript` | 118 |
| `pandoc-rst` | 20 |

`pandoc-latex` is the only route that produces correct mathematics, and it is 3% of the corpus.
That one line is the whole argument for the rebuild.

## Calibration — what these gates learned by being wrong

A gate that rejects correct work is worse than no gate, because it throws away the material it was
built to protect. Each of these fired on good pages before being narrowed, and each narrowing is
recorded so it is not quietly undone:

- **`extraction-debris` exempts anything short by design.** A multiple-choice question is a run of
  four-character options, and the short-fragment test condemned eight pages of a probability exam
  as OCR noise. List items, table rows, and any line carrying `$…$` are content however short.
- **`thin-body` and `duplicate-body` skip `index.md`.** A contents page is navigation: little prose
  by design, and two generated ones can legitimately coincide. Holding them to the prose floor
  rejected exactly the pages whose job is to help a reader find the others.
- **`escaped-dollar` only fires next to TeX.** `\$` is *correct* for a price, and the body pipeline
  deliberately produces it so `$50 million` cannot open a maths span. It is suspicious only where a
  TeX command sits on the same line, which suggests an escaped delimiter rather than money.
- **`page-number-line` and `hyphen-break` are measured outside code.** A bare `4` in R output is a
  result, and a trailing hyphen in code is an operator.
- **`extra-h1` is measured outside code.** `#dosis wordt als continue covariaat ingelezen` is an R
  comment, not a heading; counting those reported 5,804 phantom duplicate title levels.
- **The numeral cross-check is advisory.** See *The LLM route* below.

The pattern is the same every time: the gate measured a *shape* and assumed the shape implied
damage. Where the shape is also what correct content looks like, the gate has to look at context
instead.

## Figures

Extraction is **licence-gated**, because an extracted figure is redistribution of source content in
a way a paragraph of reformatted prose is not.

| source `licence` | figures |
| --- | --- |
| `CC BY 4.0`, `CC BY-NC 4.0`, `CC BY-NC-SA 4.0`, `CC0-1.0`, `BSD-2-Clause`, `BSD-3-Clause` | extracted, committed, referenced relatively |
| `unresolved`, or anything not on that list | **not extracted.** A marked placeholder links to the original page of the original file |

Never guess in the publishing direction. `unresolved` is the default and costs nothing; a wrongly
published figure cannot be recalled from a public site. 4,306 pages currently carry
`licence: unresolved`, including all five Caltech theses — that is 36% of the corpus, and resolving
those licences is worth more than any converter change.

Also skipped, regardless of licence: images under 4 KB (rules, bullets, logos) and anything that
would put a single file over 2 MB.

## The report

`validate_pages.py --report` prints, and a conversion run repeats in its own summary:

- pages published, and pages **rejected with the gate that rejected them**
- the route census — how many pages came by each route, which is the real quality distribution
- `**Unverified.**` count, and pages carrying a `reconstructed` banner
- figures extracted, and figures suppressed by licence

The rejected list is the useful half. It is the material that needs a different approach — a better
source format, a licence resolved, or an adaptation — and it is invisible unless something prints it.

## The LLM route, and how it is kept honest

A multimodal model reading page images is the only thing that recovers a two-column slide deck, a
typeset equation or a scanned page — the material `pymupdf4llm` turns into word salad. It is also
**inference about what was written**, which this repository has a standing rule about: a conversion
that is merely lossy is honest; one silently improved by a model is not.

Both are true, so the route exists and is fenced.

### Where it runs

| the source has | route |
| --- | --- |
| `.tex` `.qmd` `.Rmd` `.md` `.rst` `.ipynb` | **never the model.** Pandoc gives the LaTeX the author typed; a model can only paraphrase it |
| `.srt` `.vtt` | never the model. Timestamped speech is already faithful |
| `.html` | pandoc, with the MathJax pre-pass. The model only if pandoc's output fails a fatal gate |
| **`.pdf`, and nothing better exists** | **the model, always** — with `pymupdf4llm` run alongside as the cross-check, not as the output |

That last row is the deliberate change. The deterministic PDF route produced 55% of the old corpus
and essentially none of it was worth reading; keeping it as the *published* output in order to feel
rigorous was rigour about the wrong thing. It is far more useful as a control.

### The cross-check

The model's markdown and `pymupdf4llm`'s extraction of the same pages are compared before anything
is published:

- **token recall** — what fraction of the deterministic text's content words appear in the model's
  output. Low recall means the model dropped or summarised sections. Threshold **0.80**.
- **no invention** — content words in the model's output that appear nowhere in the deterministic
  text, excluding mathematics and normal connective tissue. A spike here is fabrication.
- **numerals and identifiers** — **advisory, never fatal.** Measured and demoted: on
  `ocw-6041sc/lectures/01-slides.pdf` the model produced a conversion that was plainly better than
  the parser's — it unscrambled a two-column reading order the parser had jumbled — and still
  scored 67%, because the parser's "numbers" are mostly slide numbers, running footers and
  fragments split across columns. A check that rejects correct work two times in three is not a
  check. It is reported and watched, not enforced.

A document failing the **word-recall** floor is **not published**; it is listed under *Not
converted* with the reason. The point of the control is that it can say no.

### When the cross-check does not apply

**The check runs only where the parser's output is credible** — at least 400 characters per page of
real text. On a scan the parser emits fragments (`of nterpretations Probability come from 2 Where
does prior`) that a *correct* transcription will never contain, so scoring the model against them
punishes it for being better than the parser: the handwritten Stat 210A lecture, which the model
transcribed cleanly and legibly, scored 80% and would have been thrown away.

Where there is no credible baseline, the control is the banner, not a number. The page says a model
wrote it and that every equation is unverified, and that is the honest position.

**The verdict is recomputed on every read of the cache, never stored in it.** The cache holds what
the model wrote; whether that is publishable is policy, and a threshold change must take effect on
everything already converted rather than only on what is converted next.

This is the check both circulating Gemini-to-markdown recipes omit entirely, and it is the whole
difference between a conversion and a plausible-looking replacement for one.

### Reproducibility

**Model output is cached and committed**, keyed by source file hash + model id + prompt hash, under
`sources/.llm-cache/` (committed by exception to the `sources/*` gitignore, because it is derived
output rather than someone else's bytes).

Without this, *everything here is generated* quietly stops being true: a regeneration would re-roll
the model and produce different text for an unchanged source, and no diff would ever be reviewable.
A cache miss is the only time the API is called, so a full regenerate after the first run is free
and deterministic.

### What the reader is told

`route: llm-<model-id>`, `fidelity: reconstructed`, and the banner from `page-template.md` that says
in plain words that a model wrote the markdown and every equation in it is unverified. No page
pretends otherwise, and no `**Unverified.**` marks are sprinkled through the body — the banner
covers the whole page, which is the truth.

### Credentials

The API key is read from `GEMINI_API_KEY` in the environment and from nowhere else. It is never
written to a file in this repository, never committed, and never printed in a report or a log.
