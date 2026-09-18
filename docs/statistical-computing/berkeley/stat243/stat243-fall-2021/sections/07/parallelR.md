---
title: Parallel R
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/parallelR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/parallelR.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`sections/07/parallelR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/parallelR.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Parallel R

Andrew Vaughn

18 October, 2021

Many tasks that are computationally expensive are embarrassingly parallel. A few common tasks that fit the description:

* Simulations with independent replicates
* Bootstrapping
* Cross-validation
* Multivariate Imputation by Chained Equations (MICE)
* Fitting multiple regression models
* cross-validation

## lapply Refresher

lapply takes one parameter (a vector/list), feeds that variable into the function, and returns a list:

```r
lapply(1:3, function(x) c(x, x^2, x^3))
```

```
## [[1]]
## [1] 1 1 1
##
## [[2]]
## [1] 2 4 8
```

---

[Up: contents](../../index.md)
