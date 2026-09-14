---
title: (as a sanity check) at a particular value of lambda in the middle of the grid
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework3/homework3.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# (as a sanity check) at a particular value of lambda in the middle of the grid

**Source:** [`homeworks/homework3/homework3.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

yhat = predict(tf_subset, x.new = boston$Year[inds == 1])
plot(boston$Year, boston$Minutes, col = 8)
points(boston$Year[inds == 1], yhat[, 25], col = 2, pch = 19, type = "o")
```

---

[← Compute the predictions on the points in the first fold. Plot the predictions](10-compute-the-predictions-on-the-points-in-the-first-fold-plot.md) · [Up: contents](index.md) · [Spectral analysis →](12-spectral-analysis.md)
