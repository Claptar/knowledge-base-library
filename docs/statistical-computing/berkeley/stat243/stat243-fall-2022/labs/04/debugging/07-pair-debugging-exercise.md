---
title: Pair debugging exercise
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/04/debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/04/debugging.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Pair debugging exercise

**Source:** [`labs/04/debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/04/debugging.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

For the group work this week we will step through debugging the `logitBoot()`
function. This is a function that computes a bootstrapped estimate of the
standard error of the coefficient on a logistic regression model. From R's
implementation of logistic regression, stored in the `mod` variable below, we
can see that the estimated standard error is around 3.

```r
my_data <- read.csv('./data.csv')

---

[← Getting help online](06-getting-help-online.md) · [Up: contents](index.md) · [fit model in R →](08-fit-model-in-r.md)
