---
title: Ridge regression solution
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/11_regularization_L1_L2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Ridge regression solution

**Source:** [`public/lectures/11_regularization_L1_L2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

The solution for the $\beta$ estimates is given by:

$$\hat{\beta^{ridge}} = (X^\intercal X + \lambda I )^{-1} X^\intercal y$$

We get this by minimizing the ridge objective (MAP estimation - what parameters make the data most probable, given our prior on the parameters):

$$L(\beta) = (y-X\beta)^\intercal (y-X\beta) + \lambda \beta^\intercal \beta$$

Take the derivative w.r.t $\beta$ and set to 0:

$$\frac{\delta L}{\delta \beta} = -2 X^\intercal (y-X\beta)+2\lambda\beta = 0$$
$$X^\intercal y - X^\intercal X \beta - \lambda\beta = 0$$
$$X^\intercal y = (X^\intercal X + \lambda I)\beta$$
$$\hat{\beta^{ridge}} = (X^\intercal X + \lambda I )^{-1} X^\intercal y$$


## Important considerations

* Ridge regression is strongly affected by the *scale* of the predictors
* In OLS, multiplying $X$ by a constant $c$ scales $\beta$ by $1/c$ - OLS is *scale equivariant*
* On the other hand, ridge estimates can vary substantially when multiplying a given predictor by a constant -- why?
  * Scaling a given $X$ in ridge changes $X^\intercal X$, the $j$-th diagonal grows by $c^2$, so the penalty $\lambda$ now has relatively less influence over that coefficient!
* Thus it is best practice to first rescale the predictors - usually by at least *scaling* (dividing by std), but also typically by *centering* (subtracting the mean) and *scaling*. - this is the same as Z-scoring the data

---

[← Ridge regression](03-ridge-regression.md) · [Up: contents](index.md) · [Advantages of ridge →](05-advantages-of-ridge.md)
