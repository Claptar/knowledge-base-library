---
title: "9. Cross-Validation and Regularization"
course: "Berkeley Stat 153 Fall 2024"
chapter: 9
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 9. Cross-Validation and Regularization

## What this covers

When a regression model has many predictors relative to the number of observations, minimizing
training error is not enough: the fitted coefficients chase noise as well as signal. This chapter
answers two connected questions: how do we *measure* whether a model generalizes (cross-validation),
and how do we *build* a model that generalizes better in the first place (ridge and lasso
regression). It assumes familiarity with ordinary least squares, the residual sum of squares, and
basic matrix calculus ($X^\intercal X$, derivatives of quadratic forms).

## Why hold out data: cross-validation

Overfitting happens when a model matches the training data too well, at the cost of predicting new
data badly. One way to guard against it is to prefer the model that minimizes error on *held-out*
data — data that played no role in fitting.

The general tool for this is **$k$-fold cross-validation**: split the data into $k$ chunks, train on
$k-1$ of them, and evaluate on the one that was left out. For time series, though, two things break
the standard recipe:

- We usually want to train on the past to predict the future, so **randomly permuting time doesn't
  make sense** — a fold cannot mix future observations into the training set for the past.
- Time series data has **autocorrelation structure** that a random subsample would destroy. Rather
  than randomly choosing some percentage of observations for each fold, we need to **chunk the data
  so that temporal order is preserved** within the fitting.

Cross-validation used to be avoided because testing many possible training/test splits was
computationally prohibitive; that is no longer true, and CV is now a very clean way to assess model
performance without requiring:

- normally distributed errors,
- homoscedasticity,
- correct model specification,
- a known number of parameters.

It works for essentially any model, without needing to know anything about the error distribution —
which is why it has become more popular than parametric alternatives such as AIC and BIC, both of
which assume Gaussian errors.

## The case for shrinking coefficients

Suppose we have potentially many parameters and comparatively few observations, but still want a
model that is both accurate and interpretable. One answer is to **constrain or shrink** the
coefficients: this reduces the variance of the coefficient estimates at the cost of a slight
increase in bias, and — by forcing some coefficients to be very small or exactly zero — makes the
model easier to interpret, since irrelevant covariates effectively drop out.

Two major ways of doing this:

1. **Ridge regression** ($\ell_2$ regularization).
2. **Lasso regression** ($\ell_1$ regularization).

## Ridge regression

Ordinary least squares chooses $\beta$ to minimize the residual sum of squares,

$$\text{RSS} = \sum_{i=1}^n \left(y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij}\right)^2.$$

Ridge regression adds a *penalty term* to this objective. The ridge estimates are the values of
$\beta$ that minimize

$$\sum_{i=1}^n \left(y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij}\right)^2 + \lambda \sum_{j=1}^p \beta_j^2 = \text{RSS} + \lambda \sum_{j=1}^p \beta_j^2,$$

equivalently written as $\text{RSS} + \lambda \| \hat\beta \|_2^2$, where
$\| \hat\beta \|_2 = \sqrt{\sum_{j=1}^p \beta_j^2}$ is the $\ell_2$ norm. Here $\lambda \ge 0$ is a
*tuning parameter* — also called the *ridge parameter* or *ridge regularization term* — which must
itself be fit (see the section on cross-validation for $\lambda$ below).

The penalty term $\lambda \sum_j \beta_j^2$ is small exactly when the coefficients are close to
zero, so minimizing the combined objective pulls the $\beta_j$ toward zero — though, as we'll see,
not usually all the way to zero. The size of $\lambda$ controls how much the penalty matters
relative to fitting the data:

- At $\lambda = 0$ there is no regularization at all: the ridge solution is the OLS solution.
- As $\lambda \to \infty$, the ridge coefficients shrink toward $0$.
- One can plot each $\beta_j$ as a function of $\lambda$ to see this shrinkage directly.
- The shrinkage penalty is **never applied to the intercept** $\beta_0$ — only the slope
  coefficients are penalized.

## Solving for the ridge estimate

The ridge estimate has a closed form:

$$\hat{\beta}^{\text{ridge}} = (X^\intercal X + \lambda I)^{-1} X^\intercal y.$$

This is also the **MAP estimate** — the parameter values that make the data most probable once a
prior has been placed on the parameters — obtained by minimizing

$$L(\beta) = (y - X\beta)^\intercal (y - X\beta) + \lambda \beta^\intercal \beta.$$

Differentiating with respect to $\beta$ and setting the result to zero:

$$\frac{\partial L}{\partial \beta} = -2X^\intercal(y - X\beta) + 2\lambda\beta = 0$$
$$X^\intercal y - X^\intercal X \beta - \lambda \beta = 0$$
$$X^\intercal y = (X^\intercal X + \lambda I)\beta$$
$$\hat{\beta}^{\text{ridge}} = (X^\intercal X + \lambda I)^{-1} X^\intercal y.$$

**A scale warning.** Ridge regression is strongly affected by the *scale* of the predictors, in a
way OLS is not. In OLS, multiplying a column of $X$ by a constant $c$ just rescales the
corresponding $\beta$ by $1/c$ — OLS is *scale equivariant*, so the fit doesn't really change. Ridge
estimates, by contrast, can change substantially when a predictor is rescaled. The reason: scaling a
column of $X$ by $c$ changes $X^\intercal X$, and the corresponding diagonal entry grows by $c^2$ —
so the fixed penalty $\lambda$ now has *relatively less* influence over that coefficient than before.
Because of this, best practice is to rescale the predictors before fitting — typically by centering
(subtracting the mean) and scaling (dividing by the standard deviation), i.e. Z-scoring the data.

**Why use ridge?**

- It works well precisely where best subset selection becomes computationally infeasible.
- It has a closed-form solution: fitting it means fitting a single model (aside from whatever
  refitting cross-validation requires to choose $\lambda$).
- It's useful when there are many parameters relative to the number of observations and the
  predictors are correlated, so that we don't want to arbitrarily throw any of them out.
- It embodies a clean **bias–variance trade-off**: when $p$ is large relative to $n$ (close to it,
  or $p > n$), the OLS solution is highly variable, or may not even be unique. As $\lambda$
  increases, the flexibility of the fit decreases — variance falls, at the cost of increased bias.

## Lasso: forcing coefficients to zero

Ridge's weakness is that it keeps every parameter in the model: coefficients shrink toward zero but
are not usually set exactly to zero (short of $\lambda = \infty$). The **lasso** (Least Absolute
Shrinkage and Selection Operator, or $\ell_1$ regularization) minimizes instead

$$\sum_{i=1}^n \left(y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij}\right)^2 + \lambda \sum_{j=1}^p |\beta_j| = \text{RSS} + \lambda \sum_{j=1}^p |\beta_j|,$$

where the $\ell_1$ norm of the coefficient vector is $|\beta| = \sum_j |\beta_j|$. The objective
looks almost identical to ridge's, with $\beta_j^2$ replaced by $|\beta_j|$ — but that single change
has a large consequence: lasso **forces some coefficients to exactly zero**. It performs variable
selection as a side effect of fitting, producing *sparse* models that use only a subset of the
available predictors.

## Why lasso zeroes coefficients: the geometric picture

Penalized least squares can be read as a constrained optimization problem: minimize the RSS subject
to the coefficient vector lying inside some region — a disc for ridge, a diamond for lasso, with the
size of the region shrinking as $\lambda$ grows. Thinking about the geometry of this constrained
problem explains why lasso, and not ridge, produces exact zeros.

<figure>
<svg viewBox="0 0 480 260" role="img" aria-label="Contours of the RSS around the OLS estimate meeting a diamond-shaped lasso constraint at a corner, versus a circular ridge constraint at a generic point">
  <line x1="120" y1="60" x2="120" y2="230" stroke="currentColor" stroke-width="1"/>
  <line x1="15" y1="150" x2="225" y2="150" stroke="currentColor" stroke-width="1"/>
  <text x="128" y="52" font-size="12" fill="currentColor">&#946;&#8322;</text>
  <text x="213" y="163" font-size="12" fill="currentColor">&#946;&#8321;</text>
  <polygon points="120,95 175,150 120,205 65,150" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="135" cy="45" r="18" fill="none" stroke="currentColor" stroke-opacity="0.85" stroke-width="1"/>
  <circle cx="135" cy="45" r="34" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="1"/>
  <circle cx="135" cy="45" r="52" fill="none" stroke="currentColor" stroke-opacity="0.9" stroke-width="1.5"/>
  <circle cx="135" cy="45" r="2.5" fill="currentColor"/>
  <text x="140" y="42" font-size="11" fill="currentColor">OLS</text>
  <circle cx="120" cy="95" r="3.5" fill="#d97706"/>
  <text x="15" y="50" font-size="11" fill="currentColor">touches a corner: &#946;&#8321; = 0</text>
  <text x="120" y="248" font-size="12" text-anchor="middle" fill="currentColor">Lasso (&#8467;&#8321; ball)</text>

  <line x1="360" y1="60" x2="360" y2="230" stroke="currentColor" stroke-width="1"/>
  <line x1="255" y1="150" x2="465" y2="150" stroke="currentColor" stroke-width="1"/>
  <text x="368" y="52" font-size="12" fill="currentColor">&#946;&#8322;</text>
  <text x="453" y="163" font-size="12" fill="currentColor">&#946;&#8321;</text>
  <circle cx="360" cy="150" r="55" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="410" cy="90" r="8" fill="none" stroke="currentColor" stroke-opacity="0.85" stroke-width="1"/>
  <circle cx="410" cy="90" r="15" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="1"/>
  <circle cx="410" cy="90" r="23" fill="none" stroke="currentColor" stroke-opacity="0.9" stroke-width="1.5"/>
  <circle cx="410" cy="90" r="2.5" fill="currentColor"/>
  <text x="414" y="87" font-size="11" fill="currentColor">OLS</text>
  <circle cx="395" cy="108" r="3.5" fill="#d97706"/>
  <text x="255" y="50" font-size="11" fill="currentColor">touches off-axis: no &#946; is 0</text>
  <text x="360" y="248" font-size="12" text-anchor="middle" fill="currentColor">Ridge (&#8467;&#8322; ball)</text>
</svg>
<figcaption>Each ring is a contour of constant RSS around the OLS estimate; the constraint region
(diamond for lasso, disc for ridge) shrinks as &#955; grows, and the fitted point is the smallest
RSS contour still touching the region. The diamond has corners sitting on the axes, so the
touching contour typically lands on a corner first &#8212; setting that coordinate to exactly zero.
The disc has no corners, so the touching point is generically off both axes, and no coefficient is
forced to zero.</figcaption>
</figure>

Reading the picture: the ellipses (drawn here as circles for simplicity) are contours of the RSS
centered on the OLS estimate $\hat\beta$ — every point on the same contour has the same RSS. If the
constraint region is large enough (small $\lambda$, near $\lambda = 0$), the OLS estimate itself lies
inside it and the constrained solution just *is* the OLS solution. In the more usual case the OLS
estimate lies outside both the diamond and the disc, and the constrained solution is wherever the
smallest RSS contour first touches the boundary of the region.

Because the ridge region is a circle with no sharp points, that first touch happens somewhere on the
smooth part of the boundary — generically off the coordinate axes, so no coefficient is exactly
zero. The lasso region has sharp corners sitting exactly on the axes, and — especially once there
are many coefficients — it becomes comparatively likely that the RSS contour first touches one of
those corners rather than a flat side. Touching a corner means one coordinate of $\beta$ is exactly
zero.

**Which is better?** It depends on the problem, not on one method dominating the other:

- **Ridge** tends to do better when the response genuinely depends on many predictors, or when the
  predictors are collinear, so that arbitrarily selecting one over another doesn't make sense — for
  instance, correlated time lags, where there's no principled reason to zero one lag but keep its
  neighbor.
- **Lasso** tends to do better when variable selection is actually wanted, or when many predictors
  are expected to be irrelevant. The resulting sparse models are easier to interpret.

## Choosing the tuning parameter by cross-validation

Both ridge and lasso need a value of $\lambda$, and cross-validation is how it's chosen: fit the
model across a range of candidate $\lambda$ values, compute the CV error for each, and select the
$\lambda$ that minimizes it.

As before, for time series this cross-validation **must preserve the time series structure** — the
autocorrelation in the data — rather than randomly shuffling observations across folds.

## Sources

- `docs/statistics/berkeley/stat153/spring-2026/public/lectures/11_regularization_L1_L2_notes/01-cross-validation.md`
  — cross-validation, the overfitting motivation, $k$-fold CV, and the time-series adaptations.
- `docs/statistics/berkeley/stat153/spring-2026/public/lectures/11_regularization_L1_L2_notes/02-ridge-regression.md`
  — the ridge objective and the behavior of $\lambda$.
- `docs/statistics/berkeley/stat153/spring-2026/public/lectures/11_regularization_L1_L2_notes/03-ridge-regression-solution.md`
  — the closed-form ridge solution and its derivation, the scale-dependence argument, ridge's
  advantages, and the lasso objective.
- `docs/statistics/berkeley/stat153/spring-2026/public/lectures/11_regularization_L1_L2_notes/04-a-geometric-comparison.md`
  — the geometric argument for why lasso zeroes coefficients and ridge doesn't, when each is
  preferable, and choosing $\lambda$ by CV. The lecture illustrated this with a static image
  (`lec11_ridge_lasso_constraint.png`, linked from that file); the SVG above is a redrawn schematic
  of the same argument, not a reproduction of that image.

The lecture's assigned reading — *An Introduction to Statistical Learning*, Chapter 6 (and §6.2) —
covers this material in full but was not supplied as an input and is not reproduced here. No
transcript, instructor notes, or exercise set was provided for this lecture; the lab exercise on
lasso/ridge cross-validation that the slides refer to ("You will see this in your lab!") is likewise
not part of the supplied material.

---

[← 8. Improving upon the linear model](08-improving-upon-the-linear-model.md) · [Contents](index.md) · [10. Periodic Signals and the Periodogram →](10-periodic-signals-and-the-periodogram.md)
