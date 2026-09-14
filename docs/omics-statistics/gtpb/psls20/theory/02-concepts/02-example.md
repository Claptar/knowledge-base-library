---
title: Example
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/02-concepts.Rmd
source_file: sources/gtpb-psls20/theory/02-concepts.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Example

**Source:** [`theory/02-concepts.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/02-concepts.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- National Health and Nutrition Examination Survey (NHANES)
- American demografic study
- Large number of physical, demographic, nutritional, life style and health characteristics

```r
library(NHANES)
knitr::kable(  NHANES[c(1,4,5,6,7,8),c(1,3,20,23,34,72)]
,format = "markdown")
```

---

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Variables →](03-variables.md)
