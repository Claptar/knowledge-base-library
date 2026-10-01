---
title: "102. Ridge and LASSO Trend Filtering"
course: "Berkeley Stat 153"
chapter: 102
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 102. Ridge and LASSO Trend Filtering

## What this covers

The previous lecture introduced a very flexible model for the trend in a time series: instead of
fitting a single line, it lets the slope bend at every time point. That flexibility makes the model
**high-dimensional** — it has about as many parameters as there are data points — so fitting it by
ordinary least squares is not useful on its own. This chapter covers how ridge and LASSO
regularization tame that model, what the two penalties look like once translated back into "the
trend should be smooth," why LASSO produces trends with a handful of exact corners while ridge
produces uniformly curved ones, and how to choose the regularization strength $\lambda$ by
cross-validation. It assumes ordinary least squares, and ridge/LASSO penalized regression in the
usual (non-time-series) setting, from earlier in the course.

## A trend model with a parameter for (almost) every time point

For a time series $y_1, \dots, y_n$, consider

$$y_t = \beta_0 + \beta_1(t - 1) + \beta_2\,\mathrm{ReLU}(t - 2) + \dots + \beta_{n-1}\,\mathrm{ReLU}(t - (n-1)) + \epsilon_t, \qquad \epsilon_t \stackrel{\text{i.i.d.}}{\sim} N(0, \sigma^2), \tag{1}$$

where $\mathrm{ReLU}(t-c) = (t-c)_+$ is $0$ for $t \le c$ and $t - c$ for $t > c$. Each term after the
first two is a "hinge" that switches on at its own time point $c$ and then grows linearly — so the
model is a sum of an intercept, an overall linear ramp, and a hinge at every later time index.

The unknown parameters are $\beta_0, \beta_1, \dots, \beta_{n-1}$ together with $\sigma$: that is
$n + 1$ unknowns for $n$ observations. This is exactly why the lecture calls the model
**high-dimensional** — there are more parameters than data points, so the model cannot be fit the
way an ordinary regression is.

## Two views of the same model

### The trend view: $\mu_t$ and its differences

Write $y_t = \mu_t + \epsilon_t$ where

$$\mu_t = \beta_0 + \beta_1(t-1) + \beta_2\,\mathrm{ReLU}(t-2) + \dots + \beta_{n-1}\,\mathrm{ReLU}(t-(n-1)). \tag{2}$$

Here $\mu_t$ is the underlying trend the model is trying to capture. The $\beta$'s translate into
statements about $\mu_t$:

$$\beta_0 = \mu_1, \qquad \beta_1 = \mu_2 - \mu_1, \qquad \beta_t = (\mu_{t+1} - \mu_t) - (\mu_t - \mu_{t-1}) \ \text{ for } t = 2, \dots, n-1.$$

So $\beta_0$ is the starting level, $\beta_1$ is the initial slope, and every later $\beta_t$ is the
**change in slope at time $t$** — the discrete second difference of $\mu$. A hinge basis function is
exactly the device that lets $\mu$ pick up a new, independent slope-change at each time point:
$\beta_t \neq 0$ means the trend has a corner at $t$; $\beta_t = 0$ means it runs straight through.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Three consecutive trend points showing a change in slope, i.e. a kink, at the middle one">
  <line x1="30" y1="170" x2="320" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <line x1="60" y1="170" x2="60" y2="150" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="170" y1="170" x2="170" y2="150" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="280" y1="170" x2="280" y2="150" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="60" y="185" text-anchor="middle" font-size="12" fill="currentColor">t-1</text>
  <text x="170" y="185" text-anchor="middle" font-size="12" fill="currentColor">t</text>
  <text x="280" y="185" text-anchor="middle" font-size="12" fill="currentColor">t+1</text>
  <polyline points="60,140 170,55 280,95" fill="none" stroke="currentColor" stroke-width="2"/>
  <circle cx="60" cy="140" r="3" fill="currentColor"/>
  <circle cx="170" cy="55" r="3" fill="currentColor"/>
  <circle cx="280" cy="95" r="3" fill="currentColor"/>
  <text x="95" y="90" font-size="12" fill="currentColor">slope s1</text>
  <text x="225" y="65" font-size="12" fill="currentColor">slope s2</text>
  <text x="170" y="35" text-anchor="middle" font-size="12" fill="currentColor">kink = s2 - s1 = beta_t</text>
</svg>
<figcaption>The size of the corner at time t, s2 minus s1, is exactly the coefficient beta_t on the
hinge anchored at t. A zero coefficient means no corner: the trend runs straight through.</figcaption>
</figure>

### The regression view: a triangular design matrix

The same model in matrix form is $y = X\beta + \epsilon$, with

$$X = \begin{pmatrix} 1 & 0 & 0 & \cdots & 0 \\ 1 & 1 & 0 & \cdots & 0 \\ 1 & 2 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & n-1 & n-2 & \cdots & 1 \end{pmatrix}, \qquad \beta = \begin{pmatrix} \beta_0 \\ \beta_1 \\ \vdots \\ \beta_{n-1} \end{pmatrix}. \tag{3}$$

Row $t$ evaluates every basis function — the intercept, the ramp $(t-1)$, and each hinge
$\mathrm{ReLU}(t-j)$ — at that time point. Reading off the pattern: $X$ is $n \times n$, lower
triangular, with $1$'s on the diagonal. That is worth noticing before moving on, because it explains
why regularization is not optional here.

## Why the raw fit is useless

A square lower-triangular matrix with $1$'s on the diagonal is invertible. So the unregularized
least-squares fit of (1) does not estimate a trend in any useful sense — it exactly reproduces the
data, $\hat\mu_t = y_t$ for every $t$, because there are exactly enough free hinges to bend the
curve through every single point. A model with as many mean parameters as observations always has
this degenerate exact-interpolation solution available; regularization is what forces the fit to
prefer a *simple* curve through the data over an *arbitrary* one.

## Ridge and LASSO, in $\beta$ and in $\mu$

The ridge estimate $\hat\beta^{\mathrm{ridge}}(\lambda)$ minimizes

$$\sum_{t=1}^n \big(y_t - \beta_0 - \beta_1(t-1) - \cdots - \beta_{n-1}\mathrm{ReLU}(t-(n-1))\big)^2 + \lambda\big(\beta_2^2 + \beta_3^2 + \cdots + \beta_{n-1}^2\big), \tag{4}$$

and the LASSO estimate $\hat\beta^{\mathrm{lasso}}(\lambda)$ minimizes the same fit term plus
$\lambda(|\beta_2| + |\beta_3| + \cdots + |\beta_{n-1}|)$. Notice $\beta_0$ and $\beta_1$ — the level
and the overall linear trend — are not penalized; only the hinge coefficients, the ones that add
curvature, are.

Because $\beta_t$ for $t \ge 2$ is the change in slope at $t$, these penalties are, via the
identities above, penalties on how much the slope of $\mu$ is allowed to change from one step to the
next:

$$\sum_{t=1}^n (y_t - \mu_t)^2 + \lambda \sum_{t=2}^{n-1} \big((\mu_{t+1}-\mu_t) - (\mu_t - \mu_{t-1})\big)^2 \tag{5}$$

for ridge, and the same fit term plus $\lambda \sum_{t=2}^{n-1} \big|(\mu_{t+1}-\mu_t) - (\mu_t -
\mu_{t-1})\big|$ for LASSO. Both objectives trade off fit to the data against neighboring slopes
being close to each other, which is exactly what makes $\hat\mu_t$ look like a smooth trend rather
than an interpolant.

These estimators already have names in the literature (not derived in the lecture, only pointed to):
the ridge trend estimate $\hat\mu_t^{\mathrm{ridge}}(\lambda)$ is the **Hodrick–Prescott filter**
from econometrics, closely related to the cubic smoothing spline; the LASSO trend estimate
$\hat\mu_t^{\mathrm{lasso}}(\lambda)$ is the **$\ell_1$ trend filter**.

## The two extremes of $\lambda$

At $\lambda = 0$, both estimators reduce to the unregularized (interpolating) least-squares fit
described above. As $\lambda \to \infty$, both estimators converge to plain linear regression of
$y_t$ on $t$: the first two components ($\beta_0, \beta_1$) become the ordinary least-squares
intercept and slope, and every hinge coefficient $\beta_2, \dots, \beta_{n-1}$ is driven to exactly
zero. So $\lambda$ interpolates between "fit every point exactly" and "fit a single straight line,"
with everything in between being a trend that bends only where the data forces it to.

## Why LASSO gives exact zeros and ridge does not

Ridge coefficients shrink toward zero as $\lambda$ grows but are essentially never *exactly* zero;
LASSO coefficients are typically sparse — most of $\hat\beta_2^{\mathrm{lasso}}, \dots,
\hat\beta_{n-1}^{\mathrm{lasso}}$ land exactly at zero (up to numerical precision). The reason is
visible already in the single-coefficient case, where the multivariate problems above reduce to a
one-dimensional optimization.

**Fact (simple ridge).** For a real number $y$ and $\lambda > 0$, the minimizer of
$f(\beta) = (y-\beta)^2 + \lambda\beta^2$ is $\hat\beta = \dfrac{y}{1+\lambda}$.

*Proof.* $f'(\beta) = 2(\beta - y) + 2\lambda\beta = 0 \implies \beta = \dfrac{y}{1+\lambda}$. $\blacksquare$

**Fact (simple LASSO).** For a real number $y$ and $\lambda > 0$, the minimizer of
$f(\beta) = (y - \beta)^2 + \lambda|\beta|$ is

$$\hat\beta = \begin{cases} y - \lambda/2 & \text{if } y > \lambda/2 \\ y + \lambda/2 & \text{if } y < -\lambda/2 \\ 0 & \text{if } -\lambda/2 \le y \le \lambda/2. \end{cases}$$

*Proof.* Away from $0$, $f$ is differentiable: $f'(\beta) = 2(\beta - y) + \lambda$ for $\beta > 0$
and $f'(\beta) = 2(\beta-y) - \lambda$ for $\beta < 0$; $|\beta|$ itself is not differentiable at
$\beta = 0$. Setting the $\beta > 0$ branch to zero gives $\beta = y - \lambda/2$, valid only when
this is positive, i.e. $y > \lambda/2$. Setting the $\beta < 0$ branch to zero gives
$\beta = y + \lambda/2$, valid only when $y < -\lambda/2$. For $y$ in the remaining range
$[-\lambda/2, \lambda/2]$, neither branch's candidate is admissible; checking signs shows
$f'(\beta) < 0$ for $\beta < 0$ and $f'(\beta) > 0$ for $\beta > 0$ throughout that range, so $f$ is
decreasing then increasing and its minimum sits at $\beta = 0$. $\blacksquare$

The ridge minimizer $y/(1+\lambda)$ is zero only if $y$ itself is zero. The LASSO minimizer is
exactly zero for an entire *interval* of $y$-values, $[-\lambda/2, \lambda/2]$ — this is the
soft-thresholding behavior that gives LASSO its tendency to zero out coefficients, and ridge its
tendency merely to shrink them.

### What that means for the fitted trend

Translated back to the trend-filtering problem: a hinge coefficient pinned at exactly zero means the
fitted trend has **no corner** at that time point — it runs straight through. So a sparse
$\hat\beta^{\mathrm{lasso}}$ produces a trend $\hat\mu_t^{\mathrm{lasso}}$ that is **piecewise
linear**, with corners only at the handful of time points where a coefficient survived. A ridge fit,
with every hinge coefficient nonzero (even if tiny), bends a little at every single time point,
giving $\hat\mu_t^{\mathrm{ridge}}$ a uniformly smooth, continuously curving appearance rather than a
polyline with a few sharp joints.

## Choosing $\lambda$ by cross-validation

$\lambda$ can be tuned by eye — start at $\lambda = 1$ and move up or down by factors of $10$ until
the fitted trend looks appropriately simple without underfitting the data — or chosen by
cross-validation.

The cross-validation recipe: split the time indices $T = \{1, \dots, n\}$ into a training set
$T_{\mathrm{train}}$ and a test set $T_{\mathrm{test}}$ (e.g. an 80/20 split). Fit $\hat\beta^{\mathrm{ridge}}_{\mathrm{train}}(\lambda)$ and $\hat\beta^{\mathrm{lasso}}_{\mathrm{train}}(\lambda)$ using only
the training indices in the sums (4) above, use the fitted model to predict $\hat y_t$ for
$t \in T_{\mathrm{test}}$, and measure

$$\text{Test-Error}(\lambda) = \sum_{t \in T_{\mathrm{test}}} \big(y_t - \hat y_t(\lambda)\big)^2.$$

Repeating over several train/test splits and adding the test errors gives one number,
$\text{AllSplit-Test-Error}(\lambda)$, per candidate $\lambda$ (candidates might be a grid such as
$\lambda = 10^a$ for $a = -5, \dots, 5$); the chosen $\lambda$ is the one with the smallest total
test error — separately for ridge and for LASSO.

A common way to build the splits is **5-fold cross-validation**, but with folds built by taking
every fifth time index rather than a contiguous block:

1. Split 1: $T_{\mathrm{test}} = \{1, 6, 11, \dots\}$, everything else trains.
2. Split 2: $T_{\mathrm{test}} = \{2, 7, 12, \dots\}$, everything else trains.
3. Split 3: $T_{\mathrm{test}} = \{3, 8, 13, \dots\}$, everything else trains.
4. Split 4: $T_{\mathrm{test}} = \{4, 9, 14, \dots\}$, everything else trains.
5. Split 5: $T_{\mathrm{test}} = \{5, 10, 15, \dots\}$, everything else trains.

## Sources

- **Fall 2025, Lecture Eleven** (`statistics/berkeley/stat153/fall-2025/LectureEleven153248Fall2025.md`,
  Aditya Guntuboyina, October 2, 2025), §1 "High-dimensional Linear Model from last class" and §2
  "Two alternative representations of (1)": the model (1), the $\mu_t$ reparametrization and its
  $\beta$-to-$\mu$ identities, and the start of the design-matrix form (3). This converted file is
  itself truncated mid-equation (the definition of the $\beta$ vector cuts off); the completion used
  here, $\beta = (\beta_0, \dots, \beta_{n-1})^\top$, is read directly off §1 of the same document,
  not invented.
- **Spring 2025, Lecture Eleven**, §4 "Regularized Estimates"
  (`.../spring-2025/LectureEleven153248Spring2025/02-4-regularized-estimates.md`): the ridge and
  LASSO objectives in $\beta$, their translation into penalties on second differences of $\mu$, and
  the Hodrick–Prescott filter / $\ell_1$ trend filter naming, including both external links the
  lecture pointed to (Wikipedia's Hodrick–Prescott filter and smoothing spline pages, and Boyd's
  $\ell_1$ trend filter page) but did not reproduce.
- Same lecture, §5 "Ridge vs LASSO" (`03-5-ridge-vs-lasso.md`): the sparsity contrast, Facts 5.1 and
  5.2 with their proofs.
- Same lecture, §6 "Cross-validation for selecting $\lambda$" (`04-6-cross-validation-for-selecting.md`):
  the train/test recipe, the test-error formula, and the specific 5-fold interleaved split.
- Not in the supplied material: whatever the source PDF's §3 contained. §4 refers back to
  "objectives (9) and (10)," equation numbers that do not match anything in the supplied excerpts,
  so an intermediate section of the original lecture was not part of this conversion and is not
  reconstructed here.
- All four source files are model reconstructions of PDFs with no text layer and carry the note that
  every equation is unverified; the transcriptions above follow them as given.

---

[← 101. AR(p) Estimation and Forecasting (part 2)](101-ar-p-estimation-and-forecasting-part-2.md) · [Contents](index.md) · [103. Smoothing the Periodogram (part 3) →](103-smoothing-the-periodogram-part-3.md)
