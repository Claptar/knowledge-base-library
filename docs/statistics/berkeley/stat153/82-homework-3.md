---
title: "82. Homework 3"
course: "Berkeley Stat 153"
chapter: 82
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 82. Homework 3

## What this covers

This chapter is Homework 3 of Berkeley's STAT 153 (Introduction to Time Series, Fall 2024), the
problem set following the course's blocks on regression and prediction, regularization and
smoothing, and spectral analysis. Its eleven questions ask: what happens to a least-squares fit
once there are more predictors than data points; how ridge and lasso regressions of cardiovascular
mortality on lagged pollution and temperature should be validated on a time series; what the
Hodrick–Prescott (HP) filter's smoothing matrix looks like as a set of local weights; how to
cross-validate a trend filter; and how a sum of random sinusoids gives a stationary process with a
prescribed autocovariance. It assumes least squares, ridge and lasso, the HP filter, trend
filtering, and split-sample and time-series cross-validation have already been covered in lecture —
none of that exposition is supplied with this problem set, only the questions built on it.

## Regression troubles: least squares when $p > n$

Let $y \in \mathbb{R}^n$ be a response and $X \in \mathbb{R}^{n\times p}$ a predictor matrix with
$p > n$: more predictors than observations. The **null space** of $X$ is the subspace
$\mathrm{null}(X) = \{\eta \in \mathbb{R}^p : X\eta = 0\}$. If $\tilde\beta$ minimizes
$\|y - X\beta\|^2$ and $\eta \in \mathrm{null}(X)$, then $X(\tilde\beta + \eta) = X\tilde\beta$: the
fitted values, and hence the residual sum of squares, are unchanged by adding $\eta$ to
$\tilde\beta$. So once $\mathrm{null}(X)$ contains more than the zero vector, least squares does not
pick out a single $\beta$ but a whole affine set of them, $\tilde\beta + \mathrm{null}(X)$. The two
questions below ask when that happens and what it implies about the sign of an individual
coefficient — a first illustration of why a course on prediction turns to regularization, the
subject of the following section, once $p$ is not small compared to $n$.

## Validating ridge and lasso on a time series

The next block moves from the abstract $p > n$ pathology to a concrete high-dimensional regression:
daily cardiovascular mortality regressed on ten lags each (4, 8, ..., 40 days) of particulate matter
and temperature, twenty predictors in total. With that many correlated, lagged predictors, ordinary
least squares is exactly the kind of fit the previous section warns about, and ridge and lasso —
fit here with `glmnet` over its own grid of tuning parameters $\lambda$ — are the two standard
remedies, introduced in the regularization and smoothing lectures (not supplied with this problem
set). What differs from a textbook train/test split is that this is a time series: the assignment
first asks for a single split-sample validation (fit on the first half of the series, forecast the
second half, and choose $\lambda$ by the mean absolute error, MAE, of those forecasts), and then for
the sharper time-series cross-validation, refitting the model repeatedly as time moves forward using
a trailing window of 200 points and a $\lambda$-grid fixed in advance. The grid has to be fixed
because `glmnet`'s default behavior — recomputing its own $\lambda$ sequence from whatever data it
is passed at each refit — would otherwise leave no common grid over which to compare MAE across time
points. Both parts use 4-, 8-, ..., 40-day lags rather than the 0-, 4-, ..., 40-day lags used
elsewhere in the course, specifically so the fitted model makes a genuine four-week-ahead forecast
rather than a same-day fit.

## The HP filter's smoothing matrix as a kernel

Recall, as the assignment itself states, that the HP filter's fitted trend is a linear function of
the data,

$$\hat\theta = \underbrace{(I + \lambda D^TD)^{-1}}_{K}\,y, \qquad \hat\theta_i = \sum_{j=1}^n K_{ij}\,y_j,$$

where $D \in \mathbb{R}^{(n-2)\times n}$ is the second-difference matrix on $n$ points — so that
$D\theta$ measures the discrete curvature of $\theta$, and penalizing $\|D\theta\|^2$ is what makes
the HP filter smooth — and $K \in \mathbb{R}^{n\times n}$ is therefore an explicit smoothing matrix.
Any estimator of this form, a linear combination of all the data with weights read off a row of a
fixed matrix, is a **linear smoother**; if row $i$ of $K$, plotted against $j$, is concentrated near
$j = i$ and decays away from it, the smoother is acting like a **kernel smoother**, giving
$\hat\theta_i$ mostly as a weighted local average of $y$ near time $i$. The question below asks for
exactly that plot, at three positions in the series, as evidence for or against that description.

## Trend filtering, cross-validated

The trend-filtering question repeats the cross-validation problem for a different smoother — order
$k=1$ (piecewise-linear) trend filtering — applied to the Boston marathon men's winning times from
1924 on. The same difficulty as with `glmnet` recurs: the `glmgen` package's `trendfilter()`
function derives its own $\lambda$ sequence from whatever data it is given, so a $\lambda$-grid has
to be fixed in advance (taken from the fit to the full data set) before it can be reused consistently
across cross-validation folds. The assignment supplies code that computes predictions on one
held-out fold at a fixed $\lambda$; folds are meant to be assigned in the "structured" way described
near the end of the regularization and smoothing lecture notes for tuning smoothers, a description
not reproduced in this problem set.

## A harmonic process and its autocovariance

The final two questions turn to a process built by superposing sinusoids with random amplitudes:

$$x_t = \sum_{j=1}^p\Big(U_{j1}\cos(2\pi\omega_j t) + U_{j2}\sin(2\pi\omega_j t)\Big), \qquad t = 1,2,3,\dots,$$

for fixed frequencies $\omega_1,\dots,\omega_p$, where the $2p$ random variables $U_{j1}, U_{j2}$
($j = 1,\dots,p$) are uncorrelated, have mean zero, and $U_{j1}, U_{j2}$ share a variance
$\sigma_j^2$ for each $j$. A process is **(weakly) stationary** if its mean is constant in $t$ and
its autocovariance, $\mathrm{Cov}(x_t, x_{t+h})$, depends on the lag $h$ but not on $t$ itself. The
first question asks for a proof that this particular process is stationary and for its
autocovariance function, matching a form given in the spectral analysis lectures (not supplied
here); the second asks for a numerical check of that formula against the sample autocorrelation
function `acf()` computes from a simulated realization.

## Exercises

### Regression troubles

1. (5 points) Let $y \in \mathbb{R}^n$ and $X \in \mathbb{R}^{n\times p}$ with $p > n$. Show that
   $\mathrm{null}(X)$ contains a nonzero vector $\eta$. Then show that if $\tilde\beta$ is a least
   squares solution for the regression of $y$ on $X$, every vector of the form
   $\hat\beta = \tilde\beta + \eta$, for $\eta \in \mathrm{null}(X)$, is also a least squares
   solution.

2. (6 points) With $X, y$ as in Question 1, suppose $\tilde\beta$ is a least squares solution with
   $\tilde\beta_j > 0$ for some coordinate $j$, and suppose $\mathrm{null}(X)$ is not orthogonal to
   the standard basis vector $e_j$ (recall $S \perp v$ means $u^Tv = 0$ for every $u \in S$). Show
   that there is another least squares solution $\hat\beta$ with $\hat\beta_j < 0$.

### Ridge and lasso

3. (8 points) Using the cardiovascular mortality data, build twenty lagged features — lags
   $4, 8, \dots, 40$ of particulate matter and of temperature. Using `glmnet`, fit a ridge
   regression and (separately) a lasso regression of mortality on these twenty predictors, each over
   `glmnet`'s own grid of tuning parameters $\lambda$, with the following split-sample validation:
   fit on the first half of the series; predict the second half at every $\lambda$; record the MAE
   of each set of predictions; report the $\lambda$ with the smallest MAE for ridge and for lasso
   separately; and plot the mortality series together with the second-half predictions at the
   chosen $\lambda$, annotated with the MAE and $\lambda$. (Lags start at 4 rather than 0, so the
   forecasts are genuinely four-weeks-ahead.)

4. (1 point) Which lagged features appear in the MAE-optimal lasso model from Question 3?

5. (8 points) Repeat Question 3 with time-series cross-validation in place of the split-sample
   validation, starting the cross-validation at the beginning of the second half (the first half
   serves as a burn-in period) and refitting each model on a trailing window of 200 points. Fix the
   $\lambda$ sequence in advance — use the one `glmnet` derived for the first-half fit in Question 3
   — so that MAE is comparable across the grid, and produce the analogous plot.

6. (Bonus) Using the lasso solutions stored at every refit of the time-series cross-validation in
   Question 5, restrict attention to the MAE-optimal $\lambda$ and summarize which lagged features
   were consistently large in magnitude over time.

### HP filter

7. (5 points) For $n = 100$ and $\lambda = 100$, compute the HP filter's smoothing matrix
   $K = (I + \lambda D^TD)^{-1}$ explicitly, where $D$ is the second-difference matrix on $n$
   points. Plot rows $i = 25, 50, 75$ of $K$ — each as the curve of pairs $(j, K_{ij})$ for
   $j = 1,\dots,n$ — overlaid on one plot in different colors. What do the three curves look like,
   and what does that suggest about the HP filter as a kernel smoother?

8. (Bonus) Find, from the literature, the closed-form asymptotically equivalent kernel for the HP
   filter. Plot it and comment on whether the empirical rows of $K$ found in Question 7 agree with
   it.

### Trend filter

9. (Bonus) Tune $\lambda$ for order-1 trend filtering on the Boston marathon men's winning times
   (from 1924 on) by 5-fold cross-validation, assigning folds in the "structured" way described for
   tuning smoothers near the end of the regularization and smoothing lecture notes. Fix the
   $\lambda$ sequence in advance, using the one `trendfilter()` derives when fit to the full data
   set, so it can be reused consistently across folds. Report the cross-validated MAE-optimal
   $\lambda$, and plot the trend-filtered fit to the full data at that $\lambda$.

### Spectral analysis

10. (3 points) Let $\omega_1,\dots,\omega_p$ be fixed frequencies, and let $U_{j1}, U_{j2}$
    ($j=1,\dots,p$) be uncorrelated, mean-zero random variables, with $U_{j1}, U_{j2}$ sharing
    variance $\sigma_j^2$. Define

    $$x_t = \sum_{j=1}^p\Big(U_{j1}\cos(2\pi\omega_jt) + U_{j2}\sin(2\pi\omega_jt)\Big), \quad t=1,2,3,\dots.$$

    Show that $\{x_t\}$ is stationary, and derive its autocovariance function, matching the form
    given in lecture.

11. (2 points) Simulate a realization of such a process with at least $p = 2$ components, compute
    its sample autocorrelation with `acf()`, and compare it against the analytic autocovariance
    function derived in Question 10.

## Sources

- `homeworks/homework3/01-introduction.md` — Questions 1–2 ("Regression troubles").
- `homeworks/homework3/02-ridge-and-lasso.md` — Questions 3–6 ("Ridge and lasso") and 7–8 ("HP
  filter").
- `homeworks/homework3/03-trend-filter.md` — Question 9 ("Trend filter") and Questions 10–11
  ("Spectral analysis").

All three converted losslessly from `homeworks/homework3/homework3.Rmd` in
`berkeley-stat153/fall-2024` (CC BY 4.0, converted 2026-09-18); this problem set is the entire
material supplied for this chapter, worth 38 points across the non-bonus questions.

Referred to but not contained in the supplied material: the "Regression and prediction" lecture
(weeks 3–4), the "Regularization and smoothing" lecture (weeks 5–6) — including its description of
"structured" fold assignment for cross-validating smoothers — and the "Spectral analysis and
filtering" lecture (weeks 7–8), all cited by the assignment as background; the cardiovascular
mortality data set and the `boston_marathon` data set (from the `fpp3` package); the `glmnet` and
`glmgen` R packages; and the time-series cross-validation code from Homework 2, which Question 5
says can be reused.

---

[← 81. Regression: Estimation and Evaluation](81-regression-estimation-and-evaluation.md) · [Contents](index.md) · [83. Long-Range ARIMA and Cross-Validation →](83-long-range-arima-and-cross-validation.md)
