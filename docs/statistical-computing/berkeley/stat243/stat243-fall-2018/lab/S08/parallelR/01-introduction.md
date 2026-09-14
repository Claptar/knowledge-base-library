---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/parallelR.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S08/parallelR.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`lab/S08/parallelR.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S08/parallelR.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Many tasks that are computationally expensive are embarrassingly parallel. Here are a few common tasks that fit the description:

  - Bootstrapping
  - Cross-validation
  - Multivariate Imputation by Chained Equations (MICE)
  - Fitting multiple regression models


## `lapply` Refresher

`lapply` takes one parameter (a vector/list), feeds that variable into the function, and returns a list:

```r
lapply(1:3, function(x) c(x, x^2, x^3))
```

You can feed it additional values by adding named parameters:

```r
lapply(1:3/3, round, digits=3)
```

These tasks are embarrassingly parallel as the elements are calculated independently, i.e. second element is independent of the result from the first element. After learning to code using `lapply` parallelizing your code is simple.

## `parallel` Package

The `parallel` package is basically about doing the above in parallel. The main difference is that we need to start with setting up a cluster, a collection of "workers"" that will be doing the job. The suggested upper limit on the number of clusters is the numbers of  `cores - 1`. Using all cores on my machine will cause the machine to come to a standstill until the R task has finished. One therefore may set up the cluster as follows:

```r
library(parallel)

---

[Up: contents](index.md) · [Calculate the number of cores →](02-calculate-the-number-of-cores.md)
