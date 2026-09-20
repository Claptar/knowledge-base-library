---
title: "41. The R Markdown Workflow"
course: "GTPB Psls20"
chapter: 41
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 41. The R Markdown Workflow

## What this covers

This chapter covers the R Markdown workflow: how a single `.Rmd` file becomes a reproducible
report, slideshow, or interactive document that mixes prose, formatted text and live R code. It
assumes the reader already knows some R and wants a way to turn a script and its output into a
document without copying numbers and plots by hand. No statistics is introduced here — this is the
tool used to write up everything else in the course.

## The four-stage workflow

An R Markdown document moves through four stages: it is **opened** as a `.Rmd` file, **written**
in plain text with Markdown formatting, given **embedded** R code that produces output, and finally
**rendered** into a finished file.

<figure>
<svg viewBox="0 0 640 160" role="img" aria-label="The four-stage R Markdown workflow: open, write, embed, render">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="10" y="55" width="130" height="50" fill="none" stroke="currentColor"/>
  <text x="75" y="75" text-anchor="middle" font-size="12" fill="currentColor">i. Open</text>
  <text x="75" y="92" text-anchor="middle" font-size="11" fill="currentColor">.Rmd file</text>

  <line x1="140" y1="80" x2="168" y2="80" stroke="currentColor" marker-end="url(#arrow)"/>

  <rect x="170" y="55" width="130" height="50" fill="none" stroke="currentColor"/>
  <text x="235" y="75" text-anchor="middle" font-size="12" fill="currentColor">ii. Write</text>
  <text x="235" y="92" text-anchor="middle" font-size="11" fill="currentColor">Markdown text</text>

  <line x1="300" y1="80" x2="328" y2="80" stroke="currentColor" marker-end="url(#arrow)"/>

  <rect x="330" y="55" width="130" height="50" fill="none" stroke="currentColor"/>
  <text x="395" y="75" text-anchor="middle" font-size="12" fill="currentColor">iii. Embed</text>
  <text x="395" y="92" text-anchor="middle" font-size="11" fill="currentColor">R code chunk</text>

  <line x1="460" y1="80" x2="488" y2="80" stroke="currentColor" marker-end="url(#arrow)"/>

  <rect x="490" y="55" width="130" height="50" fill="none" stroke="currentColor"/>
  <text x="555" y="75" text-anchor="middle" font-size="12" fill="currentColor">iv. Render</text>
  <text x="555" y="92" text-anchor="middle" font-size="11" fill="currentColor">pdf / html / docx</text>
</svg>
<figcaption>An .Rmd file is opened, written as Markdown text, given an embedded code chunk, then
rendered: the chunk is replaced by its output (for example a histogram in place of
<code>hist(co2)</code>) and the whole thing is turned into a PDF, Word document, HTML page, or
slideshow.</figcaption>
</figure>

## i. Open

Start by saving a plain text file with the extension `.Rmd`, or let RStudio create one from a
template: **File > New File > R Markdown…**. A dialog asks which class of output to build
(Document, Presentation, Shiny, or From Template) and a default output format:

- **HTML** — the recommended format for authoring; it can be switched to PDF or Word later.
- **PDF** — requires a TeX installation (MiKTeX on Windows, MacTeX 2013+ on macOS, TeX Live 2013+
  on Linux).
- **Word** — previewing requires an installation of Microsoft Word, or LibreOffice/OpenOffice on
  Linux.

This choice is only a starting point: the output format is a setting in the file (see the YAML
header below), not a property of the `.Rmd` file itself, and can be changed at any time.

## ii. Write — Markdown syntax

The body of the report is written in **Markdown**, a lightweight syntax for describing formatting
in plain text. The table below gives the syntax next to what it produces.

| Write | Get |
| --- | --- |
| `*italics*` or `_italics_` | italic text |
| `**bold**` or `__bold__` | bold text |
| `superscript^2^` | a raised 2 |
| `~~strikethrough~~` | struck-through text |
| `link` | a hyperlink |
| `# Header 1` … `###### Header 6` | headings of decreasing size, levels 1–3 markedly larger than 4–6 |
| `` | an embedded image |
| `***` | a horizontal rule (or a slide break, in a slideshow output) |
| `> block quote` | an indented quotation with a vertical bar to its left |
| a line ending in two spaces | forces a new paragraph |
| `--`, `---`, `...` | en dash, em dash, ellipsis |

An inline mathematical expression is written between single dollar signs, for example the syntax
```
$A = \pi r^{2}$
```
is typeset as a proper equation rather than left as plain text.

Lists nest with indentation, and the marker used for an unordered sub-item does not matter:

```
* unordered list
* item 2
    + sub-item 1
    + sub-item 2

1. ordered list
2. item 2
    + sub-item 1
    + sub-item 2
```

Tables are written with a header row, a separator row of dashes, and pipe-separated cells:

```
Table Header  | Second Header
------------- | -------------
Table Cell    | Cell 2
Cell 3        | Cell 4
```

which becomes:

| Table Header | Second Header |
| --- | --- |
| Table Cell | Cell 2 |
| Cell 3 | Cell 4 |

## iii. Choose the output format — the YAML header

Before the body of the document, a **YAML header** — a block of `key: value` pairs opened and
closed by a line of three dashes — tells R Markdown what kind of file to build:

```yaml
---
title: "Untitled"
author: "Anonymous"
output: html_document
---

This is the start of my report. The above is metadata saved in a YAML header.
```

RStudio writes this header automatically from the "New R Markdown" dialog described above, but it
can be edited by hand at any time. The `output` field determines what `rmarkdown::render` (see
below) produces:

| `output` value | produces |
| --- | --- |
| `html_document` | an HTML web page |
| `pdf_document` | a PDF document |
| `word_document` | a Microsoft Word `.docx` |
| `beamer_presentation` | a Beamer slideshow (PDF) |
| `ioslides_presentation` | an ioslides slideshow (HTML) |

## iv. Embed code

This is the step that separates R Markdown from plain Markdown: R code is embedded directly in the
report, and R runs it and inserts the results when the report is rendered — the numbers in the
report are always the numbers R actually computed, not numbers typed in by hand.

**Inline code** is surrounded by single backticks with a leading `r`, and is replaced by its
value when rendered:

```
Two plus two equals `r 2 + 2`.
```

renders as "Two plus two equals 4."

**Code chunks** are a whole block of R code, opened with `` ```{r} `` and closed with `` ``` ``:

````
Here's some code
```{r}
dim(iris)
```
````

which renders as "Here's some code" followed by the printed result of the chunk:

```
dim(iris)

## [1] 150  5
```

**Chunk options**, placed inside the braces after `r`, control how a chunk's code and output are
displayed without changing what the code does. `eval=FALSE` shows the code but does not run it:

````
Here's some code
```{r eval=FALSE}
dim(iris)
```
````

renders as "Here's some code" followed only by the unevaluated code. `echo=FALSE` does the reverse
— it runs the code but hides it, showing only the result:

````
Here's some code
```{r echo=FALSE}
dim(iris)
```
````

renders as "Here's some code" followed only by:

```
## [1] 150  5
```

| option | default | effect |
| --- | --- | --- |
| `eval` | `TRUE` | whether to evaluate the code and include its results |
| `echo` | `TRUE` | whether to display the code along with its results |
| `warning` | `TRUE` | whether to display warnings |
| `error` | `FALSE` | whether to display errors |
| `message` | `TRUE` | whether to display messages |
| `tidy` | `FALSE` | whether to reformat the code neatly when displaying it |
| `results` | `"markup"` | one of `"markup"`, `"asis"`, `"hold"`, or `"hide"` |
| `cache` | `FALSE` | whether to cache results so future renders can skip re-running the chunk |
| `comment` | `"##"` | the character used to preface printed results |
| `fig.width` | `7` | width in inches for a plot produced in the chunk |
| `fig.height` | `7` | height in inches for a plot produced in the chunk |

(Full documentation of chunk options is at `yihui.name/knitr/`.)

## Render

Rendering is what turns the `.Rmd` blueprint into a finished report, in one of two ways:

1. run `rmarkdown::render("<file path>")`, or
2. click the **Knit HTML** button at the top of the RStudio script pane (a split button that also
   offers Knit PDF and Knit Word, and a choice of viewing the result in the pane or in a new
   window).

When a report is rendered, R:

- executes every embedded code chunk and inserts its results into the report,
- builds the report in whatever output file type the YAML header names,
- opens a preview of the finished file in the viewer, and
- saves the output file to the working directory.

Because the report is rebuilt from the `.Rmd` source and the current data every time, re-rendering
after the data changes is exactly as much work as the first render — nothing needs to be found and
retyped by hand.

## Interactive documents

A report can be turned into an interactive Shiny document in three steps.

**1.** Add `runtime: shiny` to the YAML header:

```yaml
---
title: "Line graph"
output: html_document
runtime: shiny
---
```

**2.** Inside code chunks, add Shiny **input** functions to create widgets, and Shiny **render**
functions to create output that reacts to them:

````
---
title: "Line graph"
output: html_document
runtime: shiny
---

Choose a time series:
```{r echo = FALSE}
selectInput("data", "",
  c("co2", "lh"))
```

See a plot:
```{r echo = FALSE}
renderPlot({
  d <- get(input\$data)
  plot(d)
})
```
````

Here `selectInput` creates a drop-down of time series to choose from, and `renderPlot` redraws the
plot every time the selection changes by reading the chosen series back out of `input`.

**3.** Render with `rmarkdown::run`, or click **Run Document** in RStudio.

Because the resulting document is a running Shiny app rather than a static file, it must use an
HTML output format — `html_document` for an interactive report, or `ioslides_presentation` for an
interactive slideshow.

## Publish

A finished report can be shared in two ways, depending on whether it needs to keep running R code
after it is published:

- **RPubs** (`rpubs.com`) — RStudio's free publishing site for **non-interactive** documents.
  Clicking the **Publish** button in the RStudio preview window (or Viewer pane) pushes the
  rendered document there in one click.
- **shinyapps.io** — hosts an **interactive** Shiny document on RStudio's server, with free and
  paid tiers, since a Shiny app needs a live R process behind it rather than a static file.

## Sources

All three sections are reconstructed by a model from `background_material/rmarkdown-cheatsheet.pdf`
in the GTPB PSLS20 course repository (CC BY 4.0; converted 2026-09-20). No transcript or slide deck
accompanies this material — it is the course's standalone R Markdown reference, laid out as:

- Stages "1. Workflow" and "2. Open File" —
  `background_material/rmarkdown-cheatsheet/01-1-workflow.md`.
- Stages "3. Markdown" and "4. Choose Output" —
  `background_material/rmarkdown-cheatsheet/02-3-markdown.md`.
- Stages "5. Embed Code" through "9. Learn More" —
  `background_material/rmarkdown-cheatsheet/03-5-embed-code.md`.

The original cheat sheet is a PDF with no text layer, so screenshots of the RStudio dialogs and the
"New R Markdown" window are described in prose in the source rather than reproduced; this chapter
keeps those descriptions where they explain a step, and otherwise omits them. No exercises were
supplied with this material. Further reference named in the source but not contained in it:
`rmarkdown.rstudio.com`, `shiny.rstudio.com/articles`, and `yihui.name/knitr/`.

---

[← 40. Base R Cheat Sheet](40-base-r-cheat-sheet.md) · [Contents](index.md) · [42. Statistics and Data Exploration Review →](42-statistics-and-data-exploration-review.md)
