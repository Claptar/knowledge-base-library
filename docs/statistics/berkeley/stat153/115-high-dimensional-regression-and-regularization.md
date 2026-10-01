---
title: "115. High-Dimensional Regression and Regularization"
course: "Berkeley Stat 153"
chapter: 115
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 115. High-Dimensional Regression and Regularization

## What this covers

This chapter builds a *high-dimensional* linear regression model for the trend in a time series,
by pushing the piecewise-linear "change-of-slope" (broken-stick) model to its limit: a possible
change point at every single time index. It assumes ordinary linear regression, least squares and
maximum likelihood from earlier in the course, plus the change-of-slope model itself. The point of
the chapter is a cautionary one — this saturated model turns out to reproduce the data exactly and
tells you nothing — which is exactly what motivates the fix: penalizing the fit, first as ridge
regression, then as the lasso.

## From one change point to many

Recall the change-of-slope model for a time series $y_1,\dots,y_n$:
$$
y_t = \beta_0 + \beta_1 t + \beta_2 (t-c)_+ + \epsilon_t, \qquad \epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2). \tag{1}
$$
Here $(t-c)_+$, also written $\mathrm{ReLU}(t-c)$, is $0$ for $t\le c$ and $t-c$ for $t> c$. The
model says the trend is a straight line with slope $\beta_1$ up to time $c$, after which the slope
becomes $\beta_1+\beta_2$: $\beta_2$ is exactly the *change in slope* at the break point.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A broken-stick trend that changes slope at the break point c, illustrating what beta_2 measures in the change-of-slope model">
  <line x1="40" y1="180" x2="310" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <polygon points="310,180 300,175 300,185" fill="currentColor"/>
  <text x="313" y="178" font-size="12" fill="currentColor">t</text>
  <polyline points="40,150 170,105" fill="none" stroke="currentColor" stroke-width="2"/>
  <polyline points="170,105 300,35" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="170" y1="105" x2="170" y2="180" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="163" y="196" font-size="12" fill="currentColor">c</text>
  <text x="63" y="150" font-size="12" fill="currentColor">slope β₁</text>
  <text x="198" y="63" font-size="12" fill="currentColor">slope β₁+β₂</text>
</svg>
<figcaption>The change-of-slope model (1): linear with slope β₁ before the break, linear with slope
β₁+β₂ after it, so β₂ is the change in slope.</figcaption>
</figure>

Allowing $k$ break points instead of one generalizes (1) to
$$
y_t = \beta_0 + \beta_1 t + \beta_2\,\mathrm{ReLU}(t-c_1) + \beta_3\,\mathrm{ReLU}(t-c_2) + \dots + \beta_{k+1}\,\mathrm{ReLU}(t-c_k) + \epsilon_t. \tag{2}
$$
Fitting (2) means estimating both the break points $c_1,\dots,c_k$ and the coefficients
$\beta_0,\dots,\beta_{k+1}$ by least squares. One approach, used in earlier lectures, *profiles
out* the linear coefficients: for fixed candidate break points, minimizing over the $\beta$'s is
an ordinary linear regression, giving a residual sum of squares that depends only on the break
points,
$$
RSS(c_1,\dots,c_k) := \min_{\beta_0,\dots,\beta_{k+1}} \sum_{t=1}^n \big(y_t - \beta_0 - \beta_1 t - \beta_2\,\mathrm{ReLU}(t-c_1) - \dots - \beta_{k+1}\,\mathrm{ReLU}(t-c_k)\big)^2. \tag{3}
$$
$RSS(c_1,\dots,c_k)$ is then minimized over the break points by a grid search, and the fitted
$\hat c_1,\dots,\hat c_k$ are plugged back in to get the $\beta$'s. This is fine for $k=1$ but the
grid to search grows with $k$, and the method becomes computationally inefficient once $k$ is not
small — even $k\ge 3$ is already a problem. The alternative is to minimize the full least-squares
objective jointly over everything at once,
$$
\min_{\beta_0,\dots,\beta_{k+1},\,c_1,\dots,c_k} \sum_{t=1}^n \big(y_t - \beta_0 - \beta_1 t - \beta_2\,\mathrm{ReLU}(t-c_1) - \dots - \beta_{k+1}\,\mathrm{ReLU}(t-c_k)\big)^2, \tag{4}
$$
which is a non-trivial (non-convex, because of the $c_j$'s) optimization problem, but one that
general-purpose libraries can attack with first-order methods — gradient descent and its
relatives, as implemented in PyTorch, for instance. These methods need a reasonable starting
point: a natural initialization takes the $c_j$'s to be equally spaced quantiles of $t$, then
fits $\beta_0,\dots,\beta_{k+1}$ by ordinary least squares with those $c_j$'s held fixed.

Either way, once $k$ is not small, (4) starts to overfit — which is exactly the phenomenon the
rest of the chapter isolates, in the cleanest case there is: letting $k$ be as large as possible.

## Every time point becomes a change point

Because $t$ only ever takes the values $1,\dots,n$, a break point $c_j$ outside $(1,n)$ is
redundant: if $c_j\le 1$ then $\mathrm{ReLU}(t-c_j)$ agrees with the linear term $t-c_j$ on
$\{1,\dots,n\}$, which can be absorbed into $\beta_0+\beta_1 t$; if $c_j\ge n$ then
$\mathrm{ReLU}(t-c_j)$ is identically zero there. So nothing is lost by restricting each $c_j$ to
the open interval $(1,n)$.

It is enough, further, to take each $c_j$ to be an integer in $\{2,\dots,n-1\}$: on the integers
$t=1,\dots,n$, $\mathrm{ReLU}(t-c)$ for a non-integer $c$ is a linear combination of
$\mathrm{ReLU}(t-c)$ at the two neighbouring integers. For example,
$$
\mathrm{ReLU}(t-5.7) = 0.3\,\mathrm{ReLU}(t-5) + 0.7\,\mathrm{ReLU}(t-6) \quad \text{for all } t\le 5 \text{ and } t\ge 6,
$$
so a fractional break point buys nothing that an integer one, in linear combination, doesn't
already give. Taking *every* integer in $\{2,\dots,n-1\}$ as a break point — i.e. $k=n-2$ — turns
(2) into the saturated model
$$
y_t = \beta_0 + \beta_1(t-1) + \beta_2\,\mathrm{ReLU}(t-2) + \dots + \beta_{n-1}\,\mathrm{ReLU}(t-(n-1)) + \epsilon_t, \qquad \epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2). \tag{5}
$$
(The term is written $\beta_1(t-1)$ rather than $\beta_1 t$ purely so the pattern of indices lines
up; it changes nothing about the model.) The unknown parameters are now $\beta_0,\dots,\beta_{n-1}$
together with $\sigma$.

Models (2) and (5) differ in two ways that matter:

1. **Dimension.** Model (2) is used with a small $k$ — say $1,2,3,4$ — so it has few parameters. Model (5) has $n+1$ parameters, one for essentially every data point: it is *high-dimensional*.
2. **Linearity.** The break points $c_1,\dots,c_k$ in (2) are themselves parameters to estimate, which makes it a nonlinear regression model. In (5) the break points are fixed at every integer, so there are no nonlinear parameters left — it is an ordinary linear regression model.

So (2) is a low-dimensional *nonlinear* regression model, and (5) is a high-dimensional *linear*
one. Trading nonlinearity for dimension is exactly the point: (5) is no longer a hard optimization
problem, but as the next two sections show, that convenience is not free.

## Reading off the parameters

Write $\mu_t$ for the deterministic (trend) part of (5),
$$
\mu_t = \beta_0 + \beta_1(t-1) + \beta_2\,\mathrm{ReLU}(t-2) + \dots + \beta_{n-1}\,\mathrm{ReLU}(t-(n-1)), \tag{6}
$$
so that $y_t = \mu_t + \epsilon_t$. Depending on the application, $\mu_t$ is either the systematic
pattern being estimated (with $\epsilon_t$ genuine noise around it) or the "actual" quantity, with
$\epsilon_t$ a measurement error that makes $\mu_t$ show up as $y_t$.

Take $y_t$ to be the log of California's population in year $t$, so $\mu_t$ is the (log) trend in
population and $\epsilon_t$ measurement noise. Plugging $t=1,2,3,\dots$ into (6) one at a time and
solving recursively gives the $\beta$'s in terms of $\mu$:
$$
\beta_0=\mu_1,\qquad \beta_1=\mu_2-\mu_1,\qquad \beta_2=(\mu_3-\mu_2)-(\mu_2-\mu_1),
$$
and in general, for $j=2,\dots,n-1$,
$$
\beta_j = (\mu_{j+1}-\mu_j) - (\mu_j - \mu_{j-1}).
$$
So $\beta_0$ is just the trend's starting value. If $P_t=\exp(\mu_t)$ is the population on the
original scale, then $\beta_1 = \log(P_2/P_1) \approx (P_2-P_1)/P_1$ using $\log x \approx x-1$
for $x$ near $1$ — so $100\beta_1$ is (approximately) the percentage growth from year 1 to year 2.
Each subsequent $\beta_j$ is a *second difference* of the trend, so $100\beta_j$ is approximately
the change in percentage growth rate from one year to the next: $100\beta_2$ is how much the
growth rate in year 2–3 differs from the growth rate in year 1–2, and so on.

For example, if $\beta_0=7.3$, $\beta_1=0.04$, $\beta_2=-0.001$, $\beta_3=-0.0005$, then
$\mu_1=\exp(7.3)\approx 1480$ (in whatever units $y$ is measured, e.g. 1.48 million if the units
are thousands of people); the population grew $4\%$ from year 1 to 2, then $4-0.1=3.9\%$ from
year 2 to 3, then $3.9-0.05=3.85\%$ from year 3 to 4.

The important point to take from this is that the $\beta_j$'s are **not on a common scale**:
$\beta_0$ is in the units of the data itself, $100\beta_1$ is a percentage growth rate, and
$100\beta_j$ for $j\ge 2$ is a *change* in percentage growth rate — typically much smaller. This
comes back directly when deciding what to penalize in the next section.

## Least squares interpolates the data

Model (5) is a linear regression model, so its coefficients can be estimated the usual way, by
least squares — equivalently, by maximum likelihood — minimizing
$$
\sum_{t=1}^n \big(y_t - \beta_0 - \beta_1(t-1) - \beta_2\,\mathrm{ReLU}(t-2) - \dots - \beta_{n-1}\,\mathrm{ReLU}(t-(n-1))\big)^2 \tag{7}
$$
over $\beta_0,\dots,\beta_{n-1}$; call the minimum value $RSS$. The MLE of $\sigma$ is then
$\hat\sigma_{\mathrm{MLE}}=\sqrt{RSS/n}$.

Because (5) has exactly as many coefficients as there are data points, this fit is *perfect*:
for any $y_1,\dots,y_n$ whatsoever there is a choice of $\beta_0,\dots,\beta_{n-1}$ making
$$
y_t = \beta_0 + \beta_1(t-1) + \beta_2\,\mathrm{ReLU}(t-2) + \dots + \beta_{n-1}\,\mathrm{ReLU}(t-(n-1))
$$
hold exactly for every $t=1,\dots,n$ — and the same recursion as above (with $y$ in place of
$\mu$) exhibits it directly:
$$
\beta_0 = y_1, \qquad \beta_1 = y_2-y_1, \qquad \beta_j = (y_{j+1}-y_j)-(y_j-y_{j-1}) \quad (j=2,\dots,n-1).
$$
The fitted trend is then $\hat\mu_t = y_t$ for every $t$: the estimate simply *is* the data.
Consequently $RSS=0$ and $\hat\sigma_{\mathrm{MLE}}=0$, and the usual unbiased estimate of
$\sigma$, $\sqrt{RSS/(n-p)}$, does not even exist, since here $p=n$.

So the saturated model's least-squares fit overfits completely: it produces no simplification of
the data and no useful trend estimate at all. The fix, as in other overparametrized settings, is
regularization.

## Ridge and lasso: taming the fit

Two standard penalties turn the useless interpolating fit into something informative. The **ridge**
estimate $\hat\beta_{\mathrm{ridge}}(\lambda)$ minimizes (7) plus a penalty on the sum of squares
of the higher-order coefficients,
$$
\sum_{t=1}^n \big(y_t - \beta_0 - \beta_1(t-1) - \dots - \beta_{n-1}\,\mathrm{ReLU}(t-(n-1))\big)^2 \; + \; \lambda\big(\beta_2^2+\beta_3^2+\dots+\beta_{n-1}^2\big), \tag{8}
$$
and the **lasso** estimate $\hat\beta_{\mathrm{lasso}}(\lambda)$ minimizes (7) plus the
corresponding penalty on absolute values,
$$
\sum_{t=1}^n \big(y_t - \beta_0 - \beta_1(t-1) - \dots - \beta_{n-1}\,\mathrm{ReLU}(t-(n-1))\big)^2 \; + \; \lambda\big(|\beta_2|+|\beta_3|+\dots+|\beta_{n-1}|\big). \tag{9}
$$
In both, $\lambda\ge 0$ is a tuning parameter interpolating between two extremes. At $\lambda=0$
the penalty vanishes and both estimators reduce to the unregularized least-squares fit of the
previous section — the interpolating, useless one. As $\lambda\to\infty$ the penalty dominates,
forcing $\beta_2,\dots,\beta_{n-1}$ to zero, and what remains is exactly ordinary linear
regression of $y_t$ on $t$ using only $\beta_0$ and $\beta_1$ — a single straight line, no kinks
at all. Every value of $\lambda$ in between produces a trend somewhere between these two: a
straight line lightly perturbed by a few surviving change points.

The only difference between the two penalties is $\sum_j\beta_j^2$ versus $\sum_j|\beta_j|$; how
that difference plays out in computation and in which coefficients survive is left for the next
lecture, as is understanding regularization from a Bayesian point of view.

One more detail is deliberate rather than an oversight: the usual convention is to penalize every
coefficient except the intercept, but here the penalty in (8) and (9) also spares $\beta_1$. That
follows directly from the previous section — $\beta_0$ is on the scale of the data, $\beta_1$ is
a percentage growth rate, and only $\beta_2,\dots,\beta_{n-1}$, the second differences, are
commensurate with each other and genuinely small when the trend is close to a straight line.
Penalizing $\beta_1$ alongside them would not make sense.

## Sources

- **Fall 2025, Lecture Ten** (Aditya Guntuboyina, October 1, 2025), section *1 Background*: the
  change-of-slope model recap, the general $k$-break-point model (2), the profiled $RSS(c_1,\dots,c_k)$
  (3), the grid-search-then-refit method, its inefficiency for larger $k$, and the joint
  optimization (4) with the PyTorch/gradient-descent remark and quantile initialization. —
  `docs/statistics/berkeley/stat153/fall-2025/LectureTen153248Fall2025/01-1-background.md`
- **Fall 2025, Lecture Ten**, section *2 High-dimensional Version of (2)*: the argument for
  restricting break points to $(1,n)$ and then to integers, the $\mathrm{ReLU}(t-5.7)$ identity,
  the saturated model (5), the dimension/linearity comparison with (2), and the interpolation
  derivation. — `docs/statistics/berkeley/stat153/fall-2025/LectureTen153248Fall2025/02-2-high-dimensional-version-of-2.md`
- **Spring 2025, Lecture Ten** (Aditya Guntuboyina, February 20, 2025), section *STAT 153 & 248 -
  Time Series*: the same saturated model and low/high-dimensional comparison, used here only to
  cross-check the Fall treatment. — `docs/statistics/berkeley/stat153/spring-2025/LectureTen153248Spring2025/01-stat-153-248---time-series.md`
- **Spring 2025, Lecture Ten**, section *1 Parameter Interpretation in (1)*: the trend function
  $\mu_t$, the recursive derivation of $\beta_0,\beta_1,\beta_j$ in terms of $\mu$, and the
  California log-population example with its numeric illustration. —
  `docs/statistics/berkeley/stat153/spring-2025/LectureTen153248Spring2025/02-1-parameter-interpretation-in-1.md`
- **Spring 2025, Lecture Ten**, section *2 (Unregularized) MLE*: the least-squares/MLE derivation
  showing exact interpolation, $\hat\sigma_{\mathrm{MLE}}=0$, and the non-existence of the
  unbiased $\sigma$ estimate. — `docs/statistics/berkeley/stat153/spring-2025/LectureTen153248Spring2025/03-2-unregularized-mle.md`
- **Spring 2025, Lecture Ten**, section *3 Regularization*: the ridge objective (8) and lasso
  objective (9), the behaviour at $\lambda=0$ and $\lambda\to\infty$, and the remark on excluding
  $\beta_1$ from the penalty. — `docs/statistics/berkeley/stat153/spring-2025/LectureTen153248Spring2025/04-3-regularization.md`
- No slides or transcript were supplied for this lecture; the above notes are themselves model
  reconstructions from a PDF with no text layer (each source file carries a "reconstructed by a
  model, every equation unverified" notice), so they are the only record used here and should be
  checked against the original slides where precision matters.
- The lecture explicitly defers two things this chapter does not cover: how ridge and lasso are
  actually computed and how they differ in which coefficients they zero out, and the Bayesian
  interpretation of regularization — both promised for "the next lecture" in the Fall notes.

---

[← 114. AR Models and Sunspots](114-ar-models-and-sunspots.md) · [Contents](index.md) · [116. Sinusoidal Models for Sunspots →](116-sinusoidal-models-for-sunspots.md)
