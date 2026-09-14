---
title: Trend filter
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework3/homework3.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Trend filter

**Source:** [`homeworks/homework3/homework3.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

9. (Bonus)
Implement 5-fold cross-validation in order to tune $\lambda$ in trend filtering
applied to the Boston marathon men's data set. Recall the description of how to
set folds in a special "structured" way, for tuning smoothers, given near the
end of the lecture notes (weeks 5-6: "Regularization and smoothing"). The code
below shows how to run trend filtering and derive estimates at the held-out
points for one fold. You can build off this code for your solution. You will
need to install the `glmgen` package from GitHub, which you can do using the
code that has been commented out.

    Important note: just like `glmnet()`, the `trendfilter()`  function (in the
`glmnet` package) computes its own `lambda` sequence. So you will need to define
an initial `lambda` sequence to pass to each subsequent call to `trendfilter()`,
so that you can have a consistent grid of tuning parameter values over which to
perform cross-validation. We do this below by using the `lambda` sequence that
`trendfilter()` itself derived when the trend filtering model is fit on the full
data set.

    After implementing cross-validation, compute and report the $\lambda$ value
with the smallest cross-validated MAE. Then, lastly, plot the solution at this
value of $\lambda$ when the model is fit to the full data set (this is already
available in the `tf` object below.)

```r

---

[← HP filter](04-hp-filter.md) · [Up: contents](index.md) · [devtools::installgithub("glmgen/glmgen", subdir = "Rpkg/glmgen") →](06-devtools-installgithub-glmgen-glmgen-subdir-rpkg-glmgen.md)
