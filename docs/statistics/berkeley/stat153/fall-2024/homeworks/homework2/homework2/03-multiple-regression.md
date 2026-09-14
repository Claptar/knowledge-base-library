---
title: Multiple regression
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework2/homework2.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Multiple regression

**Source:** [`homeworks/homework2/homework2.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

5. (2 pts)
In class, we claimed that the multiple regression coefficients, with respect to
responses $y_i$ and feature vectors $x_i \in \mathbb{R}^p$, $i = 1,\dots,n$, can
be written in two ways: the first is
$$
\hat\beta = \bigg( \sum_{i=1}^n x_i x_i^T \bigg)^{-1} \sum_{i=1}^n x_i y_i.
$$
The second is
$$
\hat\beta = (X^T X)^{-1} X^T y,
$$
where $X \in \mathbb{R}^{n \times p}$ is a feature matrix, with $i^{\text{th}}$
row $x_i$, and $y \in \mathbb{R}^n$ is a response vector, with $i^{\text{th}}$
component $y_i$. Prove that these two expressions are equivalent.

6. (Bonus)
Derive the population and sample multiple regression coefficients by solving the
corresponding least squares problem (differentiating the criterion with respect
to each $\beta_j$, setting equal to zero, and solving). For the sample least
squares coefficient, deriving either representation in Q5 will be fine.

---

[← Simple regression](02-simple-regression.md) · [Up: contents](index.md) · [Covariance calculations →](04-covariance-calculations.md)
