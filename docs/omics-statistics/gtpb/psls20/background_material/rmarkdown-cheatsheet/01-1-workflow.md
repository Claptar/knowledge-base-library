---
title: 1. Workflow
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/rmarkdown-cheatsheet.pdf
source_file: sources/gtpb-psls20/background_material/rmarkdown-cheatsheet.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`background_material/rmarkdown-cheatsheet.pdf`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/rmarkdown-cheatsheet.pdf) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1. Workflow

R Markdown Cheat Sheet — learn more at rmarkdown.rstudio.com

rmarkdown 0.2.50, Updated: 8/14

R Markdown is a format for writing reproducible, dynamic reports with R. Use it to embed R code
and results into slideshows, pdfs, html documents, Word files and more. To make a report:

- **i. Open** - Open a file that uses the .Rmd extension.
- **ii. Write** - Write content with the easy to use R Markdown syntax
- **iii. Embed** - Embed R code that creates output to include in the report
- **iv. Render** - Replace R code with its output and transform the report into a slideshow, pdf,
  html or ms Word file.

The diagram below the text shows the file progressing through these stages: a `.Rmd` file becomes
a document containing plain text ("A report. A plot:"), then gains an embedded code chunk:

````
A report.
A plot:

```{r}
hist(co2)
```
````

and is then rendered so the code chunk is replaced by its output (a histogram), producing one of:
a PDF (built via LaTeX), a Microsoft Word document, a Reveal.js/ioslides/Beamer slideshow, or an
HTML5 page.

## 2. Open File

Start by saving a text file with the extension .Rmd, or open an RStudio Rmd template

- In the menu bar, click **File ▶ New File ▶ R Markdown…**
- A window will open. Select the class of output you would like to make with your .Rmd file
- Select the specific type of output to make with the radio buttons (you can change this later)
- Click OK

A screenshot shows the resulting "New R Markdown" dialog: a list of Document / Presentation /
Shiny / From Template on the left; a Title field ("Untitled") and Author field ("Anonymous") on
the right; and a "Default Output Format" choice of:

- **HTML** (selected) — "Recommended format for authoring (you can switch to PDF or Word output
  anytime)."
- **PDF** — "PDF output requires TeX (MiKTeX on Windows, MacTeX 2013+ on OS X, TeX Live 2013+ on
  Linux)."
- **Word** — "Previewing Word documents requires an installation of MS Word (or Libre/Open Office
  on Linux)."

with OK and Cancel buttons.

---

[Up: contents](index.md) · [3. Markdown →](02-3-markdown.md)
