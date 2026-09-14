---
title: Ridge regression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/11_regularization_L1_L2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Ridge regression

**Source:** [`public/lectures/11_regularization_L1_L2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Recall that least squares estimates our $\beta$ parameters by minimizing the residual sum of squares:

$$\text{RSS} = \displaystyle\sum_{i=1}^n \left(y_i - \beta_0 - \displaystyle\sum_{j=1}^p \beta_j x_{ij}\right)^2$$


Ridge regression is very similar, but we add a *penalty term* $\lambda$ for our minimization function. For ridge esimates, we take the values that minimize:

$$\displaystyle\sum_{i=1}^n \left(y_i - \beta_0 - \displaystyle\sum_{j=1}^p \beta_j x_{ij}\right)^2 + \lambda \displaystyle\sum_{j=1}^p \beta_j^2 = \text{RSS} + \lambda \displaystyle\sum_{j=1}^p \beta_j^2$$

$\lambda \ge 0$ is a *tuning parameter*, also called the *ridge parameter* or *ridge regularization term*, which we must also fit separately.

This can also be written as:

$$\text{RSS} + \lambda \| \hat{\beta} \|_2^2$$

Where $$\| \hat{\beta} \|_2 = \sqrt{\sum_{j=1}^p \beta_j^2}$$ is the $\ell 2$ norm.

$\lambda \displaystyle\sum_{j=1}^p \beta_j^2$ is the second term, which is small when $\beta_1, \dots, \beta_p$ are close to zero. The effect of this penalty is that the $\beta$ coefficients will tend to shrink towards zero (but they are not usually exactly zero). The value of $\lambda$ determines the impact of the two terms on the $\beta$ estimates.

* $\lambda = 0$ = no regularization, same as OLS
* As $\lambda \longrightarrow \infty$, the ridge regression coefficients will approach 0
* Can plot $\beta$ values as a function of $\lambda$
* Note that we don't apply the shrinkage penalty to $\beta_0$

---

[← Alternative fitting procedures](02-alternative-fitting-procedures.md) · [Up: contents](index.md) · [Ridge regression solution →](04-ridge-regression-solution.md)
