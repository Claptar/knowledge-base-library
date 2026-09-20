---
title: "39. Ridge and LASSO Trend Estimation"
course: "Berkeley Stat 153 Fall 2024"
chapter: 39
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 39. Ridge and LASSO Trend Estimation

## What this covers

This chapter answers a practical question that shows up as soon as a regression model is made
flexible enough to fit *anything* in a time series: once the model is that flexible, it also fits
the noise, so how do you make it fit only the trend? Starting from a basis of piecewise-linear
pieces with one kink at every observed time point — a model rich enough to interpolate the data
exactly — it develops two ways of constraining the fit, ridge ($\ell_2$) and LASSO ($\ell_1$)
regularization, shows why they produce qualitatively different curves, and covers how to pick the
regularization strength $\lambda$ by cross-validation instead of by eye. It assumes ordinary least
squares regression and the idea, introduced in the preceding lecture, of building a regression
model out of a basis of functions rather than a single fixed polynomial.

## The saturated trend model

The motivating example is the annual resident population of California (in thousands of people),
1900–2024. Working with $y_t = \log(\text{population}_t)$ so that proportional changes become
additive ones, the model fit to the $n = 125$ points is

$$
y_t = \beta_0 + \beta_1(t-1) + \beta_2(t-2)_+ + \beta_3(t-3)_+ + \cdots + \beta_{n-1}\bigl(t-(n-1)\bigr)_+ + \epsilon_t ,
$$

where $(z)_+ = \max(z, 0)$. Each term $(t - c)_+$ is a *hinge*: it is exactly zero up to time $c$
and rises linearly afterward, so it lets the fitted trend bend at $c$ without disturbing the fit
before it.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="The hinge basis function (t minus c) positive part: flat before the knot c, then a linear ramp">
  <line x1="40" y1="160" x2="300" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="160" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <polyline points="40,150 180,150 280,40" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="180" y1="160" x2="180" y2="150" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="180" y="178" text-anchor="middle" font-size="12" fill="currentColor">c</text>
  <text x="300" y="178" text-anchor="middle" font-size="12" fill="currentColor">t</text>
  <text x="55" y="35" font-size="12" fill="currentColor">(t - c)&#8314;</text>
</svg>
<figcaption>One basis function of the full model. The unregularized fit places one such hinge at
every time point; LASSO's penalty keeps only a handful of them active, so the fitted trend is
straight except at a few kinks, while ridge keeps a little of every hinge and bends slightly
everywhere.</figcaption>
</figure>

Stacked into a design matrix, this is one column of 1s, one column $t - 1$, and one hinge column
for every interior time point $c = 2, \dots, n-1$ — $n$ columns for $n$ observations.

### Fitting the full model is interpolation, not estimation

Because the design matrix is square and invertible, the ordinary-least-squares fit reproduces the
data exactly. Fitting it to the California series gives $R^2 = 1$ and 0 residual degrees of
freedom; correspondingly `statsmodels` reports every standard error as `inf` and every $t$-statistic
as `nan` — there is no residual left from which to estimate a noise variance.

The fitted coefficients have a clean closed form, checked numerically against the data in the
lecture: $\hat\beta_0 = y_1$, $\hat\beta_1 = y_2 - y_1$, and for $j = 2, \dots, n-1$,

$$
\hat\beta_j = y_{j+1} - 2y_j + y_{j-1} .
$$

Each hinge coefficient is exactly the discrete second difference of the series at that point — the
amount of extra bend the interpolating curve needs at time $j$, having already matched $y_{j-1}$
and $y_j$, in order to also hit $y_{j+1}$. So the unregularized fit is not doing estimation at all:
it threads a piecewise-linear curve through every point using one degree of curvature per
observation, and it reproduces noise exactly as faithfully as it reproduces trend.

That is the reason to regularize: penalizing $\beta_2, \dots, \beta_{n-1}$ pushes the discrete
curvature of the fitted curve toward zero without touching $\beta_0$ and $\beta_1$ — the overall
level and linear slope. Both estimators below start their penalty at index 2 for exactly this
reason (`penalty_start = 2` in the code).

## Ridge regularized estimation

Given $y$, a design matrix $X$, and a penalty strength $\lambda \ge 0$, ridge estimation solves

$$
\hat\beta^{\text{ridge}}(\lambda) = \arg\min_{\beta} \left[\, \|y - X\beta\|^2 + \lambda \sum_{j \ge 2} \beta_j^2 \,\right],
$$

solved numerically with the convex-optimization library `cvxpy` (a general tool for formulating
and solving convex optimization problems, used widely in statistics, machine learning and
engineering) rather than via ridge regression's closed form, since the same solver is reused for
LASSO below. At $\lambda = 0$ this is the interpolating fit above; as $\lambda$ grows, the fit is
pulled toward a smoother curve, and $\hat\mu^{\text{ridge}}_t(\lambda) = \bigl(X\hat\beta^{\text{ridge}}(\lambda)\bigr)_t$
traces out the estimated trend. The lecture's rule of thumb for choosing $\lambda$ by eye: start
around $\lambda = 1$ and move up or down by factors of ten until the fitted curve looks "smooth
while capturing the patterns in the data" — for the NOAA January and June temperature-anomaly
series (1850–2025), $\lambda = 1000$ gave a visually good fit.

Comparing the unregularized coefficients $\hat\beta(0)$ to the ridge coefficients
$\hat\beta^{\text{ridge}}(1000)$ (January anomalies) shows the effect directly: plotted against
each other, the ridge coefficients sit in a much tighter range around zero than the unregularized
ones. Even the two coefficients that are never penalized move: $\hat\beta_0$ goes from $-0.46$ to
$-0.18$ and $\hat\beta_1$ from $0.29$ to $0.0036$, because all coefficients are fit jointly and
shrinking the curvature terms changes how the level and slope have to compensate. This is
**shrinkage**: ridge rarely sets a coefficient to exactly zero, it pulls all of them toward zero,
more so the larger $\lambda$ is.

## LASSO regularized estimation

LASSO replaces the squared penalty with an absolute-value one:

$$
\hat\beta^{\text{lasso}}(\lambda) = \arg\min_{\beta} \left[\, \|y - X\beta\|^2 + \lambda \sum_{j \ge 2} |\beta_j| \,\right].
$$

Fit to the log California population series with $\lambda = 25$: of the 123 hinge coefficients,
only five exceed $10^{-6}$ in absolute value (at the hinges indexed 29, 30, 64, 65 and 91).
Everywhere else the fitted curve is *exactly* linear.

That is **sparsity**: instead of shrinking every coefficient a little, the $\ell_1$ penalty drives
almost all of them to exactly zero. Since each surviving coefficient is a kink in the fitted curve,
the LASSO trend is genuinely piecewise linear — a handful of straight segments joined at a few
kinks — while the ridge trend for the same data bends a little at every time point and has no
exact kinks anywhere ("the LASSO fit is piecewise linear while the ridge fit is smoother, without
any kinks," as the lecture puts it). Plotted together, the two fits end up visually similar despite
this structural difference, because most of the coefficients LASSO zeroes out were already small
under ridge.

Ridge estimation results in shrinkage; LASSO estimation results in sparsity.

## Choosing $\lambda$ by cross-validation

Trial and error — "try $\lambda = 1$, then 10, then 100" — is fine for one series but not
systematic. The fix is $k$-fold cross-validation with $k = 5$: for $i = 0, \dots, 4$, fold $i$'s
test set is every fifth observation starting at $i$ (indices $i, i+5, i+10, \dots$), and the
training set is everything else. For each candidate $\lambda$, and each fold, $\hat\beta(\lambda)$
is fit on the training indices, used to predict the held-out points, and the squared prediction
errors are accumulated; the chosen $\lambda$ minimizes the total error, summed over all five folds.

Applied to the January temperature anomalies, over $\lambda \in \{0.1, 1, 10, 10^2, 10^3, 10^4, 10^5\}$:

| $\lambda$ | Ridge CV error | LASSO CV error |
|---:|---:|---:|
| 0.1 | 0.0386 | 0.0343 |
| 1 | 0.0342 | 0.0312 |
| 10 | 0.0308 | **0.0306** |
| 100 | **0.0306** | 0.0346 |
| 1,000 | 0.0306 | 0.0666 |
| 10,000 | 0.0310 | 0.0666 |
| 100,000 | 0.0334 | 0.0666 |

Both columns are U-shaped in $\log\lambda$: too small a $\lambda$ leaves the fit close to the
noisy interpolant, too large a $\lambda$ flattens it past the point of following the data, and the
minimum sits in between — ridge's minimum lands at $\lambda = 100$, LASSO's at $\lambda = 10$, with
essentially the same minimum error. This automates the "adjust by factors of ten until it looks
right" heuristic above by replacing "looks right" with a number.

## Trend estimation as denoising

The same procedure is a way of separating signal from noise in simulated data where the true
trend is known, which makes it possible to check that the regularized fit is actually recovering
it. One example generates $n = 400$ points from a smooth function combining a sine, a Gaussian
bump, a quadratic and a logarithm, with Gaussian noise of standard deviation $2$ added on top.
Cross-validating $\lambda$ over $\{10, 10^2, \dots, 10^6\}$ for ridge picks $\lambda = 10^5$ (CV
error $3.772$, against $4.221$ at $\lambda=10$ and $3.970$ at $\lambda=10^6$ — again U-shaped);
cross-validating LASSO over $\{1, 10, \dots, 10^4\}$ picks $\lambda = 100$ (CV error $3.810$).

A second example builds the truth as a genuinely piecewise-linear function of four segments,
with noise of standard deviation $4$. Here ridge's cross-validated choice is $\lambda = 10^4$ (CV
error $15.224$), and LASSO's is $\lambda = 1000$ (CV error $15.181$) — LASSO's best fit is
fractionally better than ridge's here, where the true trend is exactly the kind of object LASSO's
sparsity is built to recover, though the margin is small and both track the true segments closely.
On the smooth-truth example above the comparison runs the other way (ridge $3.772$ against LASSO's
$3.810$), consistent with each penalty being best matched to the shape of trend it is suited to.

A further use of the same idea: two noisy series of length $n = 1000$ are generated from related
but different smooth trends (the second is $0.8$ times the first, with more noise added). The
lecture notes that the two underlying trends are clearly different, but that difference is not
easy to see in the raw, noisy data. Denoising each series with its own cross-validated ridge or
LASSO fit recovers trend estimates that are comparable in a way the raw data are not — cross
validation picked the same $\lambda$ for both series in this case, so the two smoothed curves
differ only because the underlying trends genuinely do.

## Sources

- Berkeley STAT 153, fall 2025, Lecture 11 code notebook (`CodeLectureEleven153248Fall2025.ipynb`,
  CC BY 4.0), converted pages:
  [01-introduction.md](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEleven153248Fall2025.ipynb)
  (the full model, its design matrix, and the closed-form interpolation coefficients),
  02-ridge-and-lasso-regularized-estimation.md (the `solve_ridge`/`solve_lasso` `cvxpy` code and
  the shrinkage/sparsity numbers on the California population series),
  03-fitting-smooth-trend-functions-to-data.md (the NOAA January/June temperature-anomaly example
  and the by-eye choice of $\lambda$),
  05-shrinkage-and-sparsity.md (the shrinkage vs. sparsity scatter comparison and its numbers),
  06-simulated-data.md (the two-related-series denoising example). The intervening page on
  cross-validation, linked from both 03 and 05 as "Cross-validation for picking $\lambda$," was not
  among the supplied files.
- Berkeley STAT 153, spring 2025, the same code lecture given in an earlier offering
  (`CodeLectureEleven153248Spring2025.ipynb`, CC BY 4.0, single converted page). Used here for the
  `ridge_cv`/`lasso_cv` cross-validation code and results (missing from the fall conversion) and
  for the smooth-truth and piecewise-linear-truth simulated examples, which this offering covers
  in more complete form than the fall version's single two-series example.

---

[← 38. AR(p) Forecasting and Prediction Uncertainty](38-ar-p-forecasting-and-prediction-uncertainty.md) · [Contents](index.md) · [40. Applying the Spectrum Smoother →](40-applying-the-spectrum-smoother.md)
