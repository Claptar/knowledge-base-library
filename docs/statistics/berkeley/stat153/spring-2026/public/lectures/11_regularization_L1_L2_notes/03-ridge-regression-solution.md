---
title: Ridge regression solution
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/11_regularization_L1_L2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/11_regularization_L1_L2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.md`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Ridge regression solution

The solution for the $\beta$ estimates is given by:

$$\hat{\beta^{ridge}} = (X^\intercal X + \lambda I )^{-1} X^\intercal y$$

We get this by minimizing the ridge objective (MAP estimation - what parameters make the data most probable, given our prior on the parameters):

$$L(\beta) = (y-X\beta)^\intercal (y-X\beta) + \lambda \beta^\intercal \beta$$

Take the derivative w.r.t $\beta$ and set to 0:

$$\frac{\delta L}{\delta \beta} = -2 X^\intercal (y-X\beta)+2\lambda\beta = 0$$
$$X^\intercal y - X^\intercal X \beta - \lambda\beta = 0$$
$$X^\intercal y = (X^\intercal X + \lambda I)\beta$$
$$\hat{\beta^{ridge}} = (X^\intercal X + \lambda I )^{-1} X^\intercal y$$

### Important considerations

* Ridge regression is strongly affected by the *scale* of the predictors
* In OLS, multiplying $X$ by a constant $c$ scales $\beta$ by $1/c$ - OLS is *scale equivariant*
* On the other hand, ridge estimates can vary substantially when multiplying a given predictor by a constant -- why?
  * Scaling a given $X$ in ridge changes $X^\intercal X$, the $j$-th diagonal grows by $c^2$, so the penalty $\lambda$ now has relatively less influence over that coefficient!
* Thus it is best practice to first rescale the predictors - usually by at least *scaling* (dividing by std), but also typically by *centering* (subtracting the mean) and *scaling*. - this is the same as Z-scoring the data

## Advantages of ridge

* Works well when best subset selection is computationally infeasible
* Closed-form solution - fit only a single model (aside from CV repetitions)
* Helpful in situations where there are many parameters and few time points, and where predictors are correlated so we don't necessarily want to get rid of them
* *bias-variance* trade-off: In the case of large $p$ compared to $n$ (either they are close or $p>n$), the OLS solution will be highly variable or won't have a unique solution. As $\lambda$ increases, the flexibility of the ridge regression fit decreases, so we have decreased variance but increased bias.

## Another flavor - lasso regularization

One disadvantage of ridge is that it includes all parameters in the model - while they shrink toward zero, the ridge solution won't set any parameters to exactly zero (unless $\lambda = \infty$). Instead, we can use an alternative to ridge, with is the Lasso (Least Absolute Shrinkage and Selection Operator) or L1 regularization. This minimizes:

$$\displaystyle\sum_{i=1}^n \left( y_i -\beta_0 - \displaystyle\sum_{j=1}^{p} \beta_j x_{ij}\right)^2 + \lambda \displaystyle\sum_{j=1}^p |\beta_j| = \text{RSS} + \lambda \displaystyle\sum_{j=1}^p |\beta_j|$$

Note the similarities here between ridge and lasso, but the difference is that the $\beta_j^2$ term has been replaced by $|\beta_j|$. This uses an $\ell_1$ penalty instead of an $\ell_2$ penalty. The $\ell_1$ norm of a coefficient vector $\beta$ is $\left|\beta \right| = \sum |\beta_j|$

A big difference here is that lasso *forces some coefficients to exactly zero*. This results in performing variable selection and yields *sparse models* - models that contain only a subset of the variables.

---

[← Ridge regression](02-ridge-regression.md) · [Up: contents](index.md) · [A geometric comparison →](04-a-geometric-comparison.md)
