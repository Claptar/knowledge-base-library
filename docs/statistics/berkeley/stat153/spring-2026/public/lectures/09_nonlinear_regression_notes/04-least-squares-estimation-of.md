---
title: Least squares estimation of $\beta, f, \sigma$
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nonlinear_regression_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/09_nonlinear_regression_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Least squares estimation of $\beta, f, \sigma$

**Source:** [`public/lectures/09_nonlinear_regression_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nonlinear_regression_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

To estimate the parameters of this regression, we will use the same basic estimation as in prior lectures (least squares):

$S(\beta_0, \beta_1, \beta_2, f, \sigma) := \sum_{t=1}^n (y_t - \beta_0 - \beta_1 \cos 2\pi ft - \beta_2 \sin 2\pi ft)^2$

We have to minimize over all five variables $\beta_0, \beta_1, \beta_2, f, \sigma$. In practice, we will first start with estimating $f$ by taking a bunch of possible values of $f$, then calculating the goodness of fit $RSS(f)$ of that resulting linear regression model with fixed $f$. Then, with $f$ fixed at $\hat{f}$ we will calculate the remaining parameters.

1. Take a grid of possible values of $f$ in the range $[0, 1/2]$
2. For each frequency value $f$ in the grid:
    - Create a matrix $X_f$
    - Perform regression of $y$ on $X_f$ and compute the residual sum of squares $RSS(f)$
3. Take $\hat{f}$ to be the grid value that minimizes $RSS(f)$ over all values on the grid.
4. Take $\hat{\beta}$ and $\hat{\sigma}$ using the usual regression estimates of $\beta$ and $\sigma$ from typical linear regression of $y$ on $X_{\hat{f}}$.

---

[← A note on dealing with sampling](03-a-note-on-dealing-with-sampling.md) · [Up: contents](index.md)
