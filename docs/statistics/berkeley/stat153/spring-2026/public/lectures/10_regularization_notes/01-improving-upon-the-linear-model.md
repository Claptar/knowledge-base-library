---
title: Improving upon the linear model
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/10_regularization_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/10_regularization_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Improving upon the linear model

**Source:** [`public/lectures/10_regularization_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/10_regularization_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

For multiple linear regression we have seen $Y = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p + \epsilon$. If the true relationship between the response and predictors is approximately linear, then the least squares estimates will have low bias. In addition, if $n >> p$ (we have many more time points than parameters), then the least squares estimates will tend to have low variance and should perform well on test observations.

If $n$ is not much larger than $p$, we can have a lot of variability in the least squares fit, which will result in overfitting. This generally means that we will not be able to predict future observations well.

If $p > n$, then there are more coefficients $\beta_j$ to estimate than there are observations from which to estimate them. This means we cannot and should not fit multiple linear regression using least squares. We will have to take into consideration other methods for high dimensional data. In this case, there is no longer a unique least squares estimate, and there are infinitely many solutions. These least squares solutions can give zero error on the training data, but will be very poorly performing on new data due to high variance. Again, this is overfitting.

---

[Up: contents](index.md) · [What is overfitting? →](02-what-is-overfitting.md)
