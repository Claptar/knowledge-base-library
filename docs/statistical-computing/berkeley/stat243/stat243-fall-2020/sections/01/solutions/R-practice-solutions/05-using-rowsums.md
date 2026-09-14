---
title: using rowSums
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/01/solutions/R-practice-solutions.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/01/solutions/R-practice-solutions.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# using rowSums

**Source:** [`sections/01/solutions/R-practice-solutions.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/01/solutions/R-practice-solutions.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

m2 <- m1 / rowSums(x = m1)
```

#### d.
```r
m2 <- apply(X = m1, MARGIN = 2, FUN = function(x){x/sum(x)})

---

[← check that the rows sum to 1](04-check-that-the-rows-sum-to-1.md) · [Up: contents](index.md) · [dimensions are the same →](06-dimensions-are-the-same.md)
