---
title: 6) Code chunks
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/01/introGitKnitr.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/01/introGitKnitr.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 6) Code chunks

**Source:** [`section/01/introGitKnitr.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/01/introGitKnitr.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

There are dozens of options available to control the executation of the code,
the formatting and display of both the commands and the output, the display
of images, graphs, and tables, and other fancy things. Here's a list of the
basic options you should become familiar with:

- `eval`: whether the code should be evaluated
    + `TRUE`
    + `FALSE`
- `echo`: whether the code should be displayed
    + `TRUE`
    + `FALSE`
    + numbers indicating lines in a chunk
- `error`: whether to stop execution if there is an error
    + `TRUE`
    + `FALSE`
- `results`: how to display the output
    + `markup`
    + `asis`
    + `hold`
    + `hide`
- `comment`: character used to indicate output lines
    + the default is a double hash `##`
    + `""` empty character (to have a cleaner display)

Additionally, you can include inline code within your work. If you're describing
results, you don't want to hard-code a number or the amount of repititions you ran.
Instead, include variables or short functions as **r 2 + 2**, which is rendered as `r 2+2`.

---

[← knitr and R Markdown Files](02-knitr-and-r-markdown-files.md) · [Up: contents](index.md) · [7) LaTeX →](04-7-latex.md)
