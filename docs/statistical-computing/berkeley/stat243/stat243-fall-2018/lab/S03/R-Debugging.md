---
title: Debugging In R
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S03/R-Debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S03/R-Debugging.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Debugging In R

**Source:** [`lab/S03/R-Debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S03/R-Debugging.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```r
knitr::opts_chunk$set(echo = TRUE)
```

## Debugging `gamma_jackknife()`

Material is based on [Chris's tutorial on debugging](https://github.com/berkeley-scf/tutorial-R-debugging) along with an example.

Let's walk through the debugging procedure of the function `gamma_jackknife()` in `debuggingJackKnifeEst.R`.

## A More Involved Example: `logitBoot()`

  - Load `data.csv`
  - Fit a logistic regression model `y~x` called `mod` in the script provided.
  - What is the std of the coefficient of `x` from `summary(mod)`?
  - Now find the estimate of the same parameter now using bootstrap by simply calling `logitBoot()` as provided in the script.
  - Why is this estimate so much larger?
  - Use debugging tools to figure out the bug.

---

[Up: contents](../../index.md)
