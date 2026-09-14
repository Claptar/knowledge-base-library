---
title: R Sweave
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/01/intro_git_knitr.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/01/intro_git_knitr.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# R Sweave

**Source:** [`sections/01/intro_git_knitr.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/01/intro_git_knitr.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

An alternative to R Markdown is R Sweave.  R Sweave knits R code together in the form of a LaTeX document.  There is an example R Sweave document `example_sweave.Rnw` included in this folder.  This can serve as a template for you if you choose to use this format for your problem sets.

The options for code chunks listed in the Rmd section above are the same as the options used in Rnw code chunks.  As you can see in the `example_sweave.Rnw` document the syntax to designate code chunks is different.  In Sweave documents you will use <<>>= to start the chunk and @ to end the chunk.

To compile the PDF click the __Compile PDF__ button.

### Updating Preferences to knit using knitr
Sweave is older way to knit together code and text, while knitr is more updated and
allows for better formatting.  By default R Studio sets R Sweave documents to be run using
Sweave to switch to knitr open the __RStudio__ menu in the menu bar, and choose __Preferences__. In __Preferences__ go to the __Sweave__ tab and change the PDF generation to Weave Rnw
files using knitr.

### Opening an R Sweave
In the menu bar of RStudio, click on __File__, then __New File__,
and choose __R Sweave__. Select the default option (Document),
and click __Ok__. RStudio will open a new `.Rnw` file in the source pane.
And you should be able to see a file with some default content.

If you opened an Rnw file before changing the from Sweave to knitr, the default content will contain `\SweaveOpts{concordance=TRUE}` you will need to remove this line of code if you have changed the preferences to generate the PDF
using knitr.

---

[← knitr and R Markdown Files](02-knitr-and-r-markdown-files.md) · [Up: contents](index.md) · [Rtex →](04-rtex.md)
