---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework3/homework3.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`homeworks/homework3/homework3.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd) — berkeley-stat153 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

```r
knitr::opts_chunk$set(cache = TRUE, autodep = TRUE, cache.comments = TRUE)
```

\raggedright

The total number of points possible for this homework is 38. The number of
points for each question is written below, and questions marked as "bonus" are
optional (points awarded for bonus problems can be used to earn back points that
you may have lost on other parts of this homework but will not put you above
full credit). Submit the **knitted pdf file** from this Rmd to Gradescope.

## Regression troubles

1. (5 pts)
Suppose that $y \in \mathbb{R}^n$ is a response vector and $X \in \mathbb{R}^{n
\times p}$ is a predictor matrix, with $p > n$. Prove that there is at least
one $\eta \not= 0$ (not equal to the zero vector) that is in $\mathrm{null}(X)$,
the null space of $X$. Prove that if $\tilde\beta$ is a least squares solution
in the regression of $y$ on $X$, then any vector of the form

$$
\hat\beta = \tilde\beta + \eta, \quad \text{for $\eta \in \mathrm{null}(X)$}
$$

is also a solution.

2. (6 pts)
With $X, y$ as in Q1, suppose that $\tilde\beta$ is a least squares solution
with $\tilde\beta_j > 0$, and suppose that $\mathrm{null}(X) \not\perp e_j$,
where $e_j$ is the $j^{\text{th}}$ standard basis vector (i.e., $e_j$ is a
vector with all 0s except for a 1 in the $j^{\text{th}}$ component), and recall
we write $S \perp v$ for a set $S$ and vector $v$ provided $u^T v = 0$ for all
$u \in S$. Prove that there exists another least squares solution $\hat\beta$
such that $\hat\beta_j < 0$.

---

[Up: contents](index.md) · [Ridge and lasso →](02-ridge-and-lasso.md)
