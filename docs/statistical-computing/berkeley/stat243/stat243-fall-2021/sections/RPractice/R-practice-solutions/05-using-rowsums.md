---
title: using rowSums
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice-solutions.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/RPractice/R-practice-solutions.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# using rowSums

**Source:** [`sections/RPractice/R-practice-solutions.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice-solutions.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

m2 <- m1 / rowSums(x = m1)
```

#### d.
```r
m2 <- apply(X = m1, MARGIN = 2, FUN = function(x){x/sum(x)})

---

[← check that the rows sum to 1](04-check-that-the-rows-sum-to-1.md) · [Up: contents](index.md) · [dimensions are the same →](06-dimensions-are-the-same.md)
