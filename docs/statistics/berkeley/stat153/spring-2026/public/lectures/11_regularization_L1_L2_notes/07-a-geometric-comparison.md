---
title: A geometric comparison
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/11_regularization_L1_L2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# A geometric comparison

**Source:** [`public/lectures/11_regularization_L1_L2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Lasso, unlike ridge, results in coefficients that are exactly equal to zero. To show geometric intuition for this, we can think about the contours of the error and constraint functions for lasso and ridge regularization.

![Contours of the error and constraint functions for lasso and ridge regression](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/lec11_ridge_lasso_constraint.png)

The ellipses here around $\hat{\beta}$ represent a contour for the error function (think of a paraboloid or bowl shaped function, where the minimum is the OLS solution). All points on a particular red ellipse will have the same RSS value.

If the constraint regions are sufficiently large (corresponding to the smallest $\lambda=0$), then the estimates are the same as OLS. However, in most cases ridge and lasso will be different from OLS since the OLS estimate lies outside of the diamond and the circle.

Since ridge regression has a circular constraint with no sharp points, the error surface will intersect with the circle outside of the axes. On the other hand, lasso has sharp corners, and especially in even higher dimensions, it is more likely that our error surface will intersect with one of these sharp corners (where one of the variables is zero) compared to the sides.

## Which is better?

It depends! Ridge tends to be better in scenarios where the response is a function of many predictors, or where predictors have some degree of collinearity, so it doesn't make sense to choose one over the other (for example - time lags may be correlated and it might not make sense to arbitrarily choose one).

Lasso tends to be better when variable selection is required or when it is expected that many of the predictors are not useful. This can result in models that are easier to interpret.

---

[← Another flavor - lasso regularization](06-another-flavor---lasso-regularization.md) · [Up: contents](index.md) · [How do we find $\lambda$? →](08-how-do-we-find.md)
