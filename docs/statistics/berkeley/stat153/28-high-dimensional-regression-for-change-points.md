---
title: "28. High-Dimensional Regression for Change-Points"
course: "Berkeley Stat 153"
chapter: 28
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 28. High-Dimensional Regression for Change-Points

## What this covers

This chapter works through a lab exercise on recovering a piecewise-constant signal from noisy
data by regression. It answers: how do you turn "the true function jumps around but is flat in
between" into a regression model, what does the unregularized least-squares fit for that model
look like, and how do ridge and LASSO penalties change the answer? It assumes the earlier course
material on fitting a *piecewise-linear* trend with a basis of ReLU functions and choosing a
penalty by cross-validation — that material is used here for comparison but is not itself
reproduced.

## A signal that jumps instead of bending

The running example is a simulated dataset built from a fixed "blocks" function on $2048$ points:
a function that is constant except for eleven jumps of specified sizes at specified locations,
rescaled so its jumps have a definite scale. Noise $\epsilon_t \sim N(0, \sigma^2)$ with $\sigma =
5$ is added to the true values to produce the observed series $y_t$. The point of the lab is to
recover the jumps from the noisy series.

This is deliberately a different shape of signal from the one used earlier in the course. The
earlier model fit a piecewise-*linear* trend — a function with kinks, built from a basis of ReLU
functions $(t-c)_+$, each of which is zero up to a changepoint $c$ and then rises linearly. That
basis is the right one when the underlying trend bends. It is the wrong one when the underlying
trend jumps and is flat everywhere else, because reproducing a vertical jump out of ramps that
start at slope zero and increase gradually is exactly the wrong task for that basis.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="An indicator basis function jumping at a changepoint, contrasted with a ReLU basis function ramping up from the same changepoint">
  <line x1="30" y1="170" x2="300" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <text x="302" y="175" font-size="12" fill="currentColor">t</text>
  <line x1="170" y1="170" x2="170" y2="80" stroke="currentColor" stroke-width="1" stroke-dasharray="2,3" opacity="0.6"/>
  <text x="166" y="185" font-size="12" fill="currentColor" text-anchor="middle">c</text>

  <path d="M 30 150 L 170 150 L 170 90 L 300 90" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="240" y="80" font-size="12" fill="currentColor">I{t &#8805; c}</text>

  <path d="M 30 150 L 170 150 L 300 90" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="230" y="128" font-size="12" fill="currentColor">(t &#8722; c)&#8314;</text>
</svg>
<figcaption>The indicator basis function jumps from 0 to 1 at the changepoint c; the ReLU basis
function used for the piecewise-linear model instead ramps up gradually after c. Regression on the
indicator basis can reproduce a true jump exactly; regression on the ReLU basis can only
approximate one with a steep slope.</figcaption>
</figure>

## The indicator-basis model

The model used for this dataset is

$$
y_t = \beta_0 + \beta_1 I\{t \geq 2\} + \beta_2 I\{t \geq 3\} + \dots + \beta_{n-1} I\{t \ge n\} + \epsilon_t,
$$

one indicator per possible changepoint, rather than one ReLU per possible changepoint. Written as
$y = X\beta + \epsilon$, the design matrix is the lower-triangular matrix of ones,

$$
X = \begin{pmatrix}
1 & 0 & 0 & \cdots & 0 \\
1 & 1 & 0 & \cdots & 0 \\
1 & 1 & 1 & \cdots & 0 \\
\vdots & & & \ddots & \vdots \\
1 & 1 & 1 & \cdots & 1
\end{pmatrix},
$$

with $n$ rows and $n$ columns (`np.tril(np.ones((n, n)))` builds it directly). Row $t$ of $X\beta$
sums $\beta_0, \dots, \beta_{t-1}$: multiplying by $X$ turns a vector of coefficients into its
running cumulative sum.

## The unregularized fit is an exact inversion

With $n$ observations and $n$ parameters, this model is saturated, and $X$ is square and
invertible — so the unregularized least-squares problem is not really a fitting problem at all,
it is the linear system $y = X\beta$ solved exactly for $\beta$. Since $X$ turns $\beta$ into a
cumulative sum, solving for $\beta$ means undoing a cumulative sum, i.e. differencing:

$$
\hat\beta_0 = y_1, \qquad \hat\beta_t = y_{t+1} - y_t \quad (t = 1, \dots, n-1).
$$

This is confirmed by comparing `sm.OLS(y, X).fit().params` against `np.diff(y)` and `y[0]`
directly on the simulated data — the two agree to machine precision. The unregularized fit is
useless as an estimate of the true jump locations (it simply reproduces the noisy data point for
point, since $\hat\beta_t$ is nonzero at every $t$), but it sets up why a penalty is needed: any
usable estimate has to force most of the $\hat\beta_t$ to be exactly or nearly zero, leaving
nonzero coefficients only near the true changepoints.

## Ridge and LASSO on the jump sizes

Both penalized estimators leave the intercept $\beta_0$ unpenalized and shrink the jump
coefficients $\beta_1, \dots, \beta_{n-1}$. The ridge estimator minimizes

$$
\sum_{t=1}^n \Big(y_t - \beta_0 - \beta_1 I\{t\geq 2\} - \dots - \beta_{n-1}I\{t \ge n\}\Big)^2 + \lambda \sum_{t=1}^{n-1}\beta_t^2,
$$

and the LASSO estimator minimizes the same squared error plus $\lambda \sum_{t=1}^{n-1}
|\beta_t|$. Both are solved as generic convex programs (via `cvxpy`), not in closed form, since the
penalty destroys the simple invertibility that made the unregularized problem trivial.

At $\lambda = 100$, the qualitative difference between the two penalties is visible directly in
the fitted curves: the LASSO fit is piecewise constant, while the ridge fit is smoother (unless
$\lambda$ is made very large). This is the $\ell_1$ vs. $\ell_2$ distinction acting on the jump
sizes themselves — the $\ell_1$ penalty drives most $\hat\beta_t$ to exactly zero, leaving a
sparse set of nonzero jumps and hence a genuinely flat reconstruction between them; the $\ell_2$
penalty shrinks every $\hat\beta_t$ toward zero without making many of them exactly zero, so the
reconstruction keeps a small amount of drift everywhere. Since the true function is itself
piecewise constant, the LASSO fit matches its structure and gives the better estimate here.

## Choosing $\lambda$ by cross-validation

The cross-validation procedure used earlier in the course for this kind of trend-fitting problem
did not work well on this dataset. Instead, $5$-fold cross-validation with **random** splits is
used: on each of $5$ folds, a random $20\%$ of the $n = 2048$ points is held out as the test set
and the LASSO or ridge estimator is fit on the rest, for each candidate $\lambda$; the squared
error on the held-out points is summed across folds, divided by $n$, and the $\lambda$ with the
smallest average error is chosen.

For ridge, over candidates $\lambda \in \{0.1, 1, 10, 100, 1000, 10000, 100000\}$:

| $\lambda$ | CV error |
|---|---|
| 0.1 | 35.04 |
| 1 | 30.74 |
| **10** | **28.24** |
| 100 | 29.61 |
| 1000 | 36.71 |
| 10000 | 48.74 |
| 100000 | 67.01 |

The chosen $\lambda = 10$ is small enough to let the ridge estimate pick up the jumps reasonably
well, but a ridge fit at this $\lambda$ is still too wiggly on the constant stretches — the
$\ell_2$ penalty cannot simultaneously suppress noise on flat segments and stay responsive enough
to track a jump, because it never sets a coefficient to exactly zero.

For LASSO, over candidates $\lambda \in \{0.1, 1, 10, 100, 1000\}$:

| $\lambda$ | CV error |
|---|---|
| 0.1 | 36.58 |
| 1 | 35.25 |
| 10 | 28.78 |
| **100** | **27.22** |
| 1000 | 45.65 |

Here $\lambda = 100$ is both the cross-validated choice and, from the earlier visual comparison,
a good fit to the true jump structure — a case where the two ways of choosing $\lambda$ (by eye,
by CV) agree.

## The same dataset under the earlier ReLU model

The lab closes by returning to the piecewise-linear model from the earlier part of the course —
intercept, linear trend, and a ReLU feature $(t-c)_+$ for every candidate changepoint $c$ — and
fitting *this* dataset with LASSO on that basis instead (intercept and linear-trend columns left
unpenalized). At $\lambda = 100$ the fit is visibly too wiggly on the flat stretches; at $\lambda =
1000$ it is smoother but can no longer track the jumps sharply — the fit blurs a jump into a short
steep ramp rather than reproducing a step, because every basis function in this model is a ramp,
not a step. This is the same bias–variance tension seen with ridge above, but here it cannot be
resolved by any choice of $\lambda$ at all: the ReLU basis is the wrong shape for a purely
piecewise-constant truth, no matter how it is regularized. The moral of the lab is that the choice
of basis has to match the shape of the signal — indicator functions for a signal that jumps and
holds, ReLU functions for a signal that bends — and only once that choice is right does tuning the
penalty strength do the rest of the work.

## Sources

- Notebook: `docs/statistics/berkeley/stat153/fall-2025/CodeLabFive153248Fall2025.md` (STAT 153,
  UC Berkeley, Fall 2025, Code Lab Five, "High-dimensional regression for change-points";
  converted from `CodeLabFive153248Fall2025.ipynb`, CC BY 4.0). All formulas, code behaviour, and
  numerical results (the `blocks` function, the design matrix, the closed-form unregularized
  estimate, the ridge/LASSO objectives, and both cross-validation tables) are taken directly from
  this notebook.
- The lab explicitly refers to, but does not itself contain, two pieces of earlier course
  material used only for comparison: the ReLU-basis piecewise-linear trend model "used in class,"
  and "the CV method discussed in class," which the lab notes does not work well on this dataset.
  Neither is reproduced here beyond what the lab states about them.
- No slide deck, transcript, or separate problem set was supplied for this chapter.

---

[← 27. AR Fitting: AutoReg vs ARIMA](27-ar-fitting-autoreg-vs-arima.md) · [Contents](index.md) · [29. Change-Point Detection and Estimation →](29-change-point-detection-and-estimation.md)
