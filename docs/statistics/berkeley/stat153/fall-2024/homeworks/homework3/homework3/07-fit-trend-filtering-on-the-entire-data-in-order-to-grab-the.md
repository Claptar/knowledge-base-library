---
title: Fit trend filtering on the entire data in order to grab the lambda sequence
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework3/homework3.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Fit trend filtering on the entire data in order to grab the lambda sequence

**Source:** [`homeworks/homework3/homework3.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

tf = trendfilter(x = boston$Year, y = boston$Minutes, k = 1)
lambda = tf$lambda

n = nrow(boston)       # Number of points
k = 5                  # Number of folds
inds = rep_len(1:k, n) # Folds indices

---

[← devtools::installgithub("glmgen/glmgen", subdir = "Rpkg/glmgen")](06-devtools-installgithub-glmgen-glmgen-subdir-rpkg-glmgen.md) · [Up: contents](index.md) · [Fit trend filtering on all points but those in first fold. We are forcing it →](08-fit-trend-filtering-on-all-points-but-those-in-first-fold-we.md)
