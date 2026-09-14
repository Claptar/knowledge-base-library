---
title: check that the rows sum to 1
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/01/solutions/R-practice-solutions.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/01/solutions/R-practice-solutions.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# check that the rows sum to 1

**Source:** [`sections/01/solutions/R-practice-solutions.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/01/solutions/R-practice-solutions.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

apply(X = m2, MARGIN = 1, FUN = function(x){sum(x) == 1})

---

[← can set rownames as well](03-can-set-rownames-as-well.md) · [Up: contents](index.md) · [using rowSums →](05-using-rowsums.md)
