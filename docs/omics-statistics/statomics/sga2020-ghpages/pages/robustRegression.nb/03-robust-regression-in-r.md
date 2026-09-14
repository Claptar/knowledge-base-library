---
title: Robust regression in R
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/robustRegression.nb.html
source_file: sources/statomics-sga2020-ghpages/pages/robustRegression.nb.html
licence: CC0-1.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Robust regression in R

**Source:** [`pages/robustRegression.nb.html`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/robustRegression.nb.html) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.html` (good)

## simulate 20 observations from a linear model with errors that follow a normal distribution

``` r
set.seed=112358
nobs<-20
sdy<-1
x<-seq(0,1,length=nobs)
y<-10+5*x+rnorm(nobs,sd=sdy)
```

---

[← Robust Regression {#robust-regression .title .toc-ignore}](02-robust-regression-robust-regression-title-toc-ignore.md) · [Up: contents](index.md) · [add outlier at high leverage point →](04-add-outlier-at-high-leverage-point.md)
