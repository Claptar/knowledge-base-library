---
title: Regression troubles
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework3/homework3.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Regression troubles

**Source:** [`homeworks/homework3/homework3.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

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

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Ridge and lasso →](03-ridge-and-lasso.md)
