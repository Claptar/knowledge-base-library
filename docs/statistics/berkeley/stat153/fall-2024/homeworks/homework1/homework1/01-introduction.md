---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework1/homework1.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework1/homework1.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`homeworks/homework1/homework1.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework1/homework1.Rmd) — berkeley-stat153 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

```r
knitr::opts_chunk$set(cache = TRUE, autodep = TRUE, cache.comments = TRUE)
```

\raggedright

The total number of points possible for this homework is 42. The number of
points for each question is written below, and questions marked as "bonus" are
optional (points awarded for bonus problems can be used to earn back points that
you may have lost on other parts of this homework but will not put you above
full credit). Submit the **knitted pdf file** from this Rmd to Gradescope.

If you collaborated with anybody for this homework, put their names here:

## Correlation and independence

1. (3 pts)
Give an example to show that two random variables can be uncorrelated but not
independent. You must explicitly prove that they are uncorrelated but not
independent (for the latter, you may invoke any property that you know is
equivalent to independence).

2. (2 pts)
If $(X,Y)$ has a multivariate Gaussian distribution, and $X,Y$ are uncorrelated:
$\mathrm{Cov}(X,Y) = 0$, then show that $X,Y$ are independent.

3. (3 pts)
Give an example to show that two random variables $X,Y$ can be marginally
Gaussian (meaning, $X$ is Gaussian, and $Y$ is Gaussian) and uncorrelated but
*not* independent. Hint: $(X,Y)$ cannot be multivariate Gaussian in this case.

---

[Up: contents](index.md) · [Random walks →](02-random-walks.md)
