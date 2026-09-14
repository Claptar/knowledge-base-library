---
title: Another flavor - lasso regularization
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/11_regularization_L1_L2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Another flavor - lasso regularization

**Source:** [`public/lectures/11_regularization_L1_L2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

One disadvantage of ridge is that it includes all parameters in the model - while they shrink toward zero, the ridge solution won't set any parameters to exactly zero (unless $\lambda = \infty$). Instead, we can use an alternative to ridge, with is the Lasso (Least Absolute Shrinkage and Selection Operator) or L1 regularization. This minimizes:

$$\displaystyle\sum_{i=1}^n \left( y_i -\beta_0 - \displaystyle\sum_{j=1}^{p} \beta_j x_{ij}\right)^2 + \lambda \displaystyle\sum_{j=1}^p |\beta_j| = \text{RSS} + \lambda \displaystyle\sum_{j=1}^p |\beta_j|$$

Note the similarities here between ridge and lasso, but the difference is that the $\beta_j^2$ term has been replaced by $|\beta_j|$. This uses an $\ell_1$ penalty instead of an $\ell_2$ penalty. The $\ell_1$ norm of a coefficient vector $\beta$ is $\left|\beta \right| = \sum |\beta_j|$

A big difference here is that lasso *forces some coefficients to exactly zero*. This results in performing variable selection and yields *sparse models* - models that contain only a subset of the variables.

---

[← Advantages of ridge](05-advantages-of-ridge.md) · [Up: contents](index.md) · [A geometric comparison →](07-a-geometric-comparison.md)
