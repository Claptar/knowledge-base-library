---
title: to use the lambda sequence that we saved above
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework3/homework3.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# to use the lambda sequence that we saved above

**Source:** [`homeworks/homework3/homework3.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

tf_subset = trendfilter(x = boston$Year[inds != 1],
                        y = boston$Minutes[inds != 1],
                        k = 1, lambda = lambda)

---

[← Fit trend filtering on all points but those in first fold. We are forcing it](08-fit-trend-filtering-on-all-points-but-those-in-first-fold-we.md) · [Up: contents](index.md) · [Compute the predictions on the points in the first fold. Plot the predictions →](10-compute-the-predictions-on-the-points-in-the-first-fold-plot.md)
