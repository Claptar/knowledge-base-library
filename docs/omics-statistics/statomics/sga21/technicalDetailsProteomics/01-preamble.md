---
title: Preamble
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/technicalDetailsProteomics.Rmd
source_file: sources/statomics-sga21/technicalDetailsProteomics.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Preamble

**Source:** [`technicalDetailsProteomics.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/technicalDetailsProteomics.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Read stored results for heart data

```r
library(tidyverse)
library(limma)
library(QFeatures)
library(msqrob2)
pe <- readRDS(
  url(
    "https://raw.githubusercontent.com/statOmics/SGA2020/gh-pages/assets/peHeart.rds",
    "rb")
  )
```

---

[Up: contents](index.md) · [Linear regression →](02-linear-regression.md)
