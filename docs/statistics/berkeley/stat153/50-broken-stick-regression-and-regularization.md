---
title: "50. Broken-Stick Regression and Regularization"
course: "Berkeley Stat 153 Fall 2024"
chapter: 50
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 50. Broken-Stick Regression and Regularization

## What this covers

The previous lecture introduced nonlinear regression models; this one asks a concrete version of
that question: how do you fit a trend whose growth rate itself changes over time, and what happens
if you let it change at *every* time point? Working through one dataset — the log of California's
population, 1900–2024 — the lecture moves from a single change of slope, to several, to a knot at
every observation, and lands on ridge and lasso as the fix for the last case. It assumes ordinary
least squares (fitting, $R^2$, reading a regression summary table) and some comfort with nonlinear
regression as a modelling idea, but develops the specific tools — profiling, joint nonlinear
optimization, and penalized least squares — from scratch.

## A trend that will not stay straight

The running example is FRED's estimate of California's resident population, in thousands of
persons, from 1900 to 2024 ($n = 125$ years). Fitting is done on the logarithm of the population
rather than the level, because a straight line in $\log(\text{population})$ has a clean reading:
if
$$y_t = \log(\text{pop}_t) = \beta_0 + \beta_1 t + \epsilon_t,$$
then $\beta_1$ is (approximately) the annual growth rate — population is multiplied by
$e^{\beta_1}$ each year, and $e^{\beta_1} - 1 \approx \beta_1$ when $\beta_1$ is small.

Fitting this by ordinary least squares gives $\hat\beta_1 = 0.0269$: a population growing at 2.69%
a year, with $R^2 = 0.950$. But the fit is visibly wrong — the growth rate was not constant over
125 years, and a single straight line cannot represent a rate that itself trends downward over the
century. The rest of the lecture is about letting the slope change.

## The single change-of-slope (broken-stick) model

The natural fix is a model with one *knot*: a point $c$ at which the slope is allowed to jump.
Writing $(x)_+ = \max(0, x)$ for the positive part,
$$y_t = \beta_0 + \beta_1 t + \beta_2 (t - c)_+ + \epsilon_t.$$
Before $c$ the slope is $\beta_1$; from $c$ onward it is $\beta_1 + \beta_2$, and the two segments
join continuously at $c$ (nothing jumps in level, only in slope) — hence "broken stick".

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="A piecewise linear curve with one kink at the knot c, showing the slope changing from beta_1 to beta_1 plus beta_2">
  <line x1="40" y1="190" x2="330" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="335" y="195" font-size="12" fill="currentColor">t</text>
  <text x="25" y="18" font-size="12" fill="currentColor">y</text>
  <polyline points="45,160 180,108" fill="none" stroke="currentColor" stroke-width="2"/>
  <polyline points="180,108 320,42" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="180" y1="190" x2="180" y2="108" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <circle cx="180" cy="108" r="2.5" fill="currentColor"/>
  <text x="170" y="205" font-size="12" fill="currentColor">c</text>
  <text x="70" y="145" font-size="12" fill="currentColor">slope &#946;&#8321;</text>
  <text x="215" y="80" font-size="12" fill="currentColor">slope &#946;&#8321;+&#946;&#8322;</text>
</svg>
<figcaption>The broken-stick model: a straight line up to the knot c, another straight line
(continuous with the first) from c onward; &#946;<sub>2</sub> is the change in slope.</figcaption>
</figure>

**Estimating $c$.** For a *fixed* value of $c$, the model is linear in $\beta_0, \beta_1, \beta_2$
(the column $(t-c)_+$ is just another known covariate once $c$ is fixed), so it can be fit by
ordinary least squares and its residual sum of squares $\mathrm{RSS}(c)$ computed. The estimate of
$c$ is then the value that makes this smallest:

1. For each candidate $c$ on a grid, fit OLS and record $\mathrm{RSS}(c)$.
2. Take $\hat c = \arg\min_c \mathrm{RSS}(c)$.

This works because the hard, nonlinear part of the problem — where is the knot — has been reduced
to a one-dimensional search, with the easy linear regression solved exactly at each grid point.

On the California data, searching $c$ over 1000 points from $t=1$ to $t=n$ gives
$\hat c \approx 66.29$, corresponding to the year $1965.3$, with $\mathrm{RSS}(\hat c) \approx
0.349$. Refitting OLS with $c$ fixed at $\hat c$ gives $\hat\beta_1 = 0.038$ and
$\hat\beta_2 = -0.024$: a growth rate of 3.8% a year before 1965, falling to $3.8 - 2.4 = 1.4\%$
after.

## More than one change of slope

Nothing stops the same idea from using several knots. With $k$ knots $c_1, \dots, c_k$,
$$y_t = \beta_0 + \beta_1 t + \beta_2 (t-c_1)_+ + \beta_3 (t-c_2)_+ + \cdots + \epsilon_t.$$
As before, for *fixed* knot locations the model is linear, so the concentrated objective
$$\mathrm{RSS}(c_1,\dots,c_k) := \min_{\beta_0,\dots,\beta_{k+1}} \sum_{t=1}^n \left(y_t - \beta_0 -
\beta_1 t - \sum_{j=1}^k \beta_{j+1}(t-c_j)_+\right)^2$$
can be evaluated at any candidate knot vector by an OLS fit, and the knots chosen to minimize it.

**Grid search does not scale.** With two knots, a $200 \times 200$ grid over $(c_1, c_2)$ already
means 40,000 OLS fits; the cost of a grid grows like $m^k$ in the number of knots $k$; for $k=2$
this grid found $\hat c_1 \approx 62.1$ (year 1961), $\hat c_2 \approx 101.3$ (year 2000), with
$\mathrm{RSS} \approx 0.199$ — down from $0.349$ with one knot. The corresponding growth rates are
3.82% before 1961, $3.82 - 1.23 = 2.59\%$ between 1961 and 2000, and $2.59 - 1.98 = 0.61\%$ after
2000. But a grid search is not going to be practical once $k$ gets much past 2 or 3.

**Joint gradient-based optimization is the alternative.** Rather than profiling out the $\beta$'s
and gridding over the knots, treat *everything* — the coefficients and the knot locations — as
parameters of one nonlinear, nonconvex objective
$$L(\beta_0,\dots,\beta_{k+1}, c_1,\dots,c_k) = \sum_{t=1}^n \left(y_t - \beta_0 - \beta_1 t -
\sum_{j=1}^k \beta_{j+1}(t-c_j)_+\right)^2,$$
and minimize it directly with a black-box optimizer. The lecture builds this as a small PyTorch
module: the knots and coefficients are both `nn.Parameter`s, and the forward pass sorts the knots
and evaluates $\beta_0 + \beta_1 x + \sum_j \beta_{j+1}\,\mathrm{ReLU}(x - c_j)$ — `ReLU` being
exactly the positive-part function $(\cdot)_+$. This is then trained with a standard optimizer
(Adam) minimizing mean squared error over many epochs, exactly as a neural network would be.

Two practical points matter for making this converge:

- **Scale the data first.** $y$ and $t$ are each standardized (mean 0, standard deviation 1) before
  optimization; gradient-based training on the raw scale (with $t$ running into the hundreds)
  converges far less reliably. Parameter estimates are converted back to the original scale
  afterward.
- **Start from a good initial guess.** Because the objective is nonconvex, a poor starting point
  can land in a bad local optimum. Initial knots are placed at evenly spaced quantiles of the
  (scaled) covariate, and initial coefficients come from an ordinary OLS fit with the knots held
  fixed at those quantiles — the same trick as the profiled grid search, just used once to
  initialize rather than repeatedly to search.

On the two-knot case, the trained model recovers essentially the same fit as the grid search —
knots at $\approx 62.4$ and $101.4$ (matching $61.1, 101.3$ up to which knot is which), and a
slightly *lower* RSS ($\approx 0.1987$ against the grid search's $0.1989$), because it searches a
continuum of knot positions rather than a finite grid. The coefficient estimates agree closely too.
The real payoff is that this method scales: fitting $k=3$ knots costs about the same as $k=2$, and
gives $\mathrm{RSS} \approx 0.101$, a further improvement (though a small one — the fitted curve
for $k=3$ looks close to the $k=2$ fit, i.e. adding a third knot buys diminishing returns here).
Pushing $k$ much higher starts to overfit: with enough knots the piecewise-linear curve can track
essentially every wiggle in the data rather than the underlying trend.

## The limit: a knot at every point

Push the idea to its extreme and put a knot at *every* interior time index, $c = 2, 3, \dots,
n-1$:
$$y_t = \beta_0 + \beta_1 (t-1) + \beta_2 (t-2)_+ + \beta_3 (t-3)_+ + \cdots + \beta_{n-1}(t-(n-1))_+
+ \epsilon_t.$$
Counting parameters: one intercept, one slope, and $n-2$ knot coefficients make exactly $n$
parameters for $n$ observations. Fitting this by ordinary least squares on the California data
(with $n=125$) gives $R^2 = 1.000$ and zero residual degrees of freedom — the model does not
approximate the data, it *interpolates* it exactly, and the regression output shows the tell-tale
signs of a degenerate fit: standard errors of `inf`, an undefined adjusted $R^2$, and a condition
number of $1.78 \times 10^4$.

The unregularized coefficients have a strikingly simple closed form:
$$\hat\beta_0 = y_1, \qquad \hat\beta_1 = y_2 - y_1, \qquad \hat\beta_j = y_{j+1} - 2y_j + y_{j-1}
\ \ (j = 2, \dots, n-1),$$
i.e. the intercept and first slope are just the first two observations, and every other
coefficient is the *second difference* of the series at that point. This checks out numerically
against the fitted regression: $y_1 = 7.3065$, $y_2 - y_1 = 0.0395$, and $y_3 - 2y_2 + y_1 =
0.0065$ match the printed $\hat\beta_0, \hat\beta_1, \hat\beta_2$ exactly. This is the sense in
which "a knot everywhere" is not really a regression model any more — it is a re-encoding of the
raw data itself, with as many free parameters as data points.

## Reining it in: ridge and lasso regularization

A fit with zero residual degrees of freedom is useless for anything except reproducing the
training data, so the fix is to penalize the coefficients that make the model flexible — the knot
coefficients $\beta_2, \dots, \beta_{n-1}$ — while leaving the trend coefficients $\beta_0,
\beta_1$ unpenalized. Writing $X_{\text{full}}$ for the design matrix of the full model, two
penalized least-squares problems are solved (both convex, both handled directly by a general
convex optimizer):

**Ridge** shrinks the knot coefficients toward zero smoothly:
$$\min_{\beta} \ \lVert y - X_{\text{full}}\beta \rVert_2^2 + \lambda \sum_{j \geq 2} \beta_j^2.$$
With a large penalty ($\lambda = 100{,}000$ in the example), every knot coefficient becomes tiny —
none is driven to *exactly* zero, but the fitted curve becomes smooth again, close to a plain
straight-line trend.

**Lasso** penalizes the same coefficients by their absolute value instead:
$$\min_{\beta} \ \lVert y - X_{\text{full}}\beta \rVert_2^2 + \lambda \sum_{j \geq 2} |\beta_j|.$$
The $\ell_1$ penalty behaves qualitatively differently: with $\lambda = 0.01$, the great majority of
the 123 knot coefficients come out *exactly* (or numerically indistinguishable from) zero, and only
a modest subset survive above a small threshold. This is the connection back to the start of the
lecture: instead of deciding in advance how many knots to use and searching for their locations —
by grid or by gradient descent — the lasso solution automatically selects a sparse set of "active"
knots from the full candidate set of every observed time point, with $\lambda$ controlling how many
survive. It turns the change-of-slope model from something you specify (how many knots, roughly
where) into something the fit chooses for you.

## Sources

- California population data, the log-linear trend model, and its OLS fit: fall 2025 lecture 10,
  [`01-introduction.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTen153248Fall2025.ipynb).
- The single-knot broken-stick model and grid-search estimation of $c$: fall 2025 lecture 10,
  [`02-broken-stick-regression-or-change-of-slope-model.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTen153248Fall2025.ipynb).
- Multiple knots by grid search, the PyTorch `BrokenStickRegression` module and joint gradient
  optimization, the full (knot-at-every-point) model and its interpolation/second-difference
  result: fall 2025 lecture 10,
  [`03-models-with-more-changes-of-slope.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTen153248Fall2025.ipynb)
  (this file ends by deferring regularization to "the next lecture").
- The same full model, and the ridge and lasso regularized fits via `cvxpy`: spring 2025 lecture
  10, [`CodeLectureTen153248Spring2025.md`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTen153248Spring2025.ipynb).

Both notebooks are converted lecture code (Berkeley STAT 153, CC BY 4.0); numbers quoted above are
the values printed in their outputs. Figures referenced in the original notebooks (the raw
population plot, the fitted curves, the $\mathrm{RSS}(c)$ profile) were omitted in conversion and
are not reproduced here — only the single change-of-slope figure above was added to make the model
shape explicit. No slides or transcript were supplied for this lecture; the two notebooks (fall
2025 and spring 2025 offerings of the same lecture) are complementary rather than a slide/transcript
pair, and are merged here rather than repeated.

---

[← 49. Autoregressive Models in Practice](49-autoregressive-models-in-practice.md) · [Contents](index.md) · [51. Bayesian Regularization and Variance Models →](51-bayesian-regularization-and-variance-models.md)
