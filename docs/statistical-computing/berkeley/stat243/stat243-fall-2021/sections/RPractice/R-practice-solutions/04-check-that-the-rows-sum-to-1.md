---
title: check that the rows sum to 1
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice-solutions.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/RPractice/R-practice-solutions.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# check that the rows sum to 1

**Source:** [`sections/RPractice/R-practice-solutions.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice-solutions.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

apply(X = m2, MARGIN = 1, FUN = function(x){sum(x) == 1})

---

[← can set rownames as well](03-can-set-rownames-as-well.md) · [Up: contents](index.md) · [using rowSums →](05-using-rowsums.md)
