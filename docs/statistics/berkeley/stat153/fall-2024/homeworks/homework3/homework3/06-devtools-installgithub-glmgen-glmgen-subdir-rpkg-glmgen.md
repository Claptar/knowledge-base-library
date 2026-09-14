---
title: devtools::installgithub("glmgen/glmgen", subdir = "Rpkg/glmgen")
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework3/homework3.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# devtools::installgithub("glmgen/glmgen", subdir = "Rpkg/glmgen")

**Source:** [`homeworks/homework3/homework3.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

library(glmgen)
library(fpp3)

boston = boston_marathon |>
  filter(Year >= 1924) |>
  filter(Event == "Men's open division") |>
  mutate(Minutes = as.numeric(Time)/60) |>
  select(Year, Minutes)

---

[← Trend filter](05-trend-filter.md) · [Up: contents](index.md) · [Fit trend filtering on the entire data in order to grab the lambda sequence →](07-fit-trend-filtering-on-the-entire-data-in-order-to-grab-the.md)
