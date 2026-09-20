---
title: "31. Fitting Trends to Time Series"
course: "Berkeley Stat 153 Fall 2024"
chapter: 31
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 31. Fitting Trends to Time Series

## What this covers

This chapter works through the first computational lab of the course: fitting a trend function to a
time series by ordinary least squares, using the time index itself as the covariate. It derives the
least-squares formulas for simple linear regression from scratch, then follows two worked examples —
monthly US population and the Google Trends volume for the search term "amazon" — as the model for
the trend is made progressively richer (linear, quadratic, cubic, log-transformed, seasonal) and used
to forecast beyond the data. It assumes only the mechanics of fitting a line by least squares and
basic partial derivatives; everything about time series proper — trend, seasonality, forecasting
uncertainty — is built up here from that starting point.

## Fitting a line through a time index

A time series is a sequence of observations $y_1, \dots, y_n$, one per time step. The simplest
possible model treats the mean of $y_i$ as a straight-line function of the time index itself: let
$x_i = i$ and write
$$y_i = \beta_0 + \beta_1 x_i + \text{error}, \qquad i = 1, \dots, n.$$
Fitting this model means choosing $\beta_0$ and $\beta_1$ to minimize the sum of squared errors
$$S(\beta_0, \beta_1) := \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2.$$
The running example is the monthly US population series from FRED (POPTHM), in thousands, from
January 1959 ($i=1$) to July 2026 ($i = n = 811$).

## Deriving the least squares estimators

Setting the partial derivatives of $S$ to zero gives the two **normal equations**:
$$\frac{\partial S}{\partial \beta_0} = 0 \implies \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i) = 0,$$
$$\frac{\partial S}{\partial \beta_1} = 0 \implies \sum_{i=1}^n x_i(y_i - \beta_0 - \beta_1 x_i) = 0.$$
The first equation rearranges directly to $\beta_0 = \bar y - \beta_1 \bar x$. Substituting this into
the second equation and solving for $\beta_1$ gives
$$\hat\beta_1 = \frac{\sum_{i=1}^n (y_i - \bar y)(x_i - \bar x)}{\sum_{i=1}^n (x_i - \bar x)^2}, \qquad
\hat\beta_0 = \bar y - \hat\beta_1 \bar x.$$

The same two equations can be written in matrix form. Stack the observations into $y \in \mathbb{R}^n$
and set
$$X = \begin{pmatrix} 1 & x_1 \\ 1 & x_2 \\ \vdots & \vdots \\ 1 & x_n \end{pmatrix}, \qquad
\beta = \begin{pmatrix}\beta_0 \\ \beta_1\end{pmatrix}.$$
Then the normal equations are $X^T(y - X\beta) = 0$, i.e.
$$X^TX\beta = X^Ty \implies \hat\beta = (X^TX)^{-1}X^Ty.$$
Expanding $(X^TX)^{-1}X^Ty$ by hand reproduces the two explicit formulas above; this matrix form is
also exactly what `statsmodels.OLS` (or any least-squares routine) computes, which is why a by-hand
calculation and the library call agree to every reported digit.

For the population data, computing $\hat\beta_1$ and $\hat\beta_0$ directly from the formulas gives
$\hat\beta_0 = 174585.5$ and $\hat\beta_1 = 213.22$, and calling `sm.OLS(y, X).fit()` on the same data
returns the identical pair of coefficients.

## Reading the fitted line

$\hat\beta_0$ is the fitted value at $x=0$, one month before the series starts, i.e. December 1958:
about 174.585 million people. $\hat\beta_1 = 213.22$ is the fitted increase in population, in
thousands, per additional month — about $12 \times 213.2 \approx 2.56$ million people per year. The
regression reports $R^2 = 0.997$, but a high $R^2$ here mainly reflects that population is a smoothly
growing series; it is not by itself evidence that a straight line is the *right* long-run model, and
the lecture flags this directly: plain linear regression usually does not work well for time series,
which is why the rest of the course builds more structured models.

**Extrapolating far outside the data is where model choice starts to matter.** The last observation
is July 2026 ($i = 811$); July 2040 is 168 months later, $i = 979$. The line predicts
$$\hat\beta_0 + \hat\beta_1 \cdot 979 = 383{,}323.75 \text{ thousand} \approx 383.3 \text{ million}.$$
`get_prediction` also returns two different uncertainty intervals for this number: one for the mean
response, and one — wider — for a single future observation, which is the one normally quoted. For
July 2040 the interval for the observation is $[378.0, 388.6]$ million (the derivation of these
intervals is left for later in the course). For comparison, the US Census Bureau's own published
projection for July 2040 is about 355 million — noticeably below even the lower end of this interval,
from a straight line fit to the same historical population series.

## The same question, three more ways

Refitting the same 811 monthly observations with richer trend functions shows how much that gap
depends on functional form, not on the data.

**Quadratic.** Adding an $i^2$ term, $y_i = \beta_0 + \beta_1 i + \beta_2 i^2 + \text{error}$, barely
changes the fit inside the observed range ($R^2$ still $0.997$; the fitted curve is visually almost
indistinguishable from the line). The estimated $\hat\beta_2 = 0.0182$ is small but positive and
statistically significant — the curve is convex, bending gently upward. Extrapolated to July 2040 it
gives 388.3 million, *larger* than the straight line, because convexity compounds over 168 months of
extrapolation even though it is invisible over the roughly 67 years of data used to fit it.

**Logarithms.** Fitting a line to $\log y_i$ instead of $y_i$ treats population as growing at a
roughly constant *proportional* rate rather than a constant absolute one — an exponential trend on
the original scale. This fit tracks the data closely ($R^2 = 0.994$) but the plot of $\log y$ against
the fitted line shows the actual recent values sitting visibly below it: growth has slowed relative to
what a constant proportional rate would predict. Extrapolating anyway (predicting $\log y$ for July
2040, $i = 979$, and exponentiating) gives $e^{\widehat{\log y}} \approx 412.7$ million — larger
again, and now the furthest of the three from the Census Bureau's number.

So the three models — linear, quadratic, log-linear — agree almost perfectly on the data used to fit
them and disagree by tens of millions of people on a forecast 14 years past the end of that data: 383,
388 and 413 million respectively, against an outside projection of 355 million. The lesson is about
extrapolation rather than about any one functional form being "wrong": a trend curve is constrained by
the data only where there is data, and how it behaves once you leave that range is almost entirely a
property of the curve you chose, not of what you fit it to.

## Building a trend function by trial: Google search interest for "amazon"

A second dataset makes the same point from the fitting side rather than the forecasting side. Google
Trends gives a monthly index of search popularity for the query "amazon", January 2004 to September
2025 ($n = 261$). Unlike the population series this one is not close to a straight line, and it also
has a visible yearly wiggle.

Fitting successively higher-degree polynomials in the time index, purely by adding more columns to the
same $X$ matrix — still ordinary least squares throughout — traces out how much curve is needed:

- **Linear** ($x$): $R^2 = 0.776$. The line "does not capture the trend in the data well" — the series
  rises, falls and rises again, and one straight line can only average over that.
- **Quadratic** ($x, x^2$): $R^2 = 0.832$. Better, but the fit is still visibly poor.
- **Cubic** ($x, x^2, x^3$): $R^2 = 0.889$, and now "the fit is pretty good" — the cubic has enough
  flexibility to trace the broad rise-and-fall shape of the series. (Statsmodels flags a large
  condition number at both the quadratic and cubic stages — a warning that the powers of a large $x$
  are becoming highly correlated with each other, a numerical side effect of using raw time indices as
  high powers, not a comment on the model itself.)

Even the cubic misses something the polynomial terms cannot represent: a genuine *seasonal* pattern,
months of the year that are systematically higher or lower than the smooth trend. This is added the
same way — as more columns of the same regression, this time trigonometric rather than polynomial:
$$\cos\!\left(\frac{2\pi x}{12}\right), \quad \sin\!\left(\frac{2\pi x}{12}\right),$$
one full cycle every 12 months. Adding this pair to the cubic model improves the fit but "is not
enough to capture the actual oscillation present in the data" — the amplitude is still off. Adding a
second harmonic pair at twice the frequency,
$$\cos\!\left(\frac{2\pi \cdot 2x}{12}\right), \quad \sin\!\left(\frac{2\pi \cdot 2x}{12}\right),$$
gives a model with seven regressors ($x, x^2, x^3$ and the two harmonic pairs) whose fit is "much
improved," though still not perfect. This is the general recipe for seasonality by regression: any
periodic shape can be approximated as closely as needed by summing enough sine/cosine pairs at the
fundamental frequency and its harmonics, fit by the same least-squares machinery as the polynomial
terms.

## Where the polynomial trend breaks the extrapolation

Using the seven-regressor model to forecast 100 months beyond the data reveals the same danger seen in
the population example, in a sharper form. The forecast oscillates seasonally as expected, but the
underlying cubic term — fit to a portion of the series where it happens to be curving downward near
the right edge — keeps curving downward once extrapolated, and the predicted search-popularity index
eventually goes negative. A search-interest index cannot be negative, so this is not merely a poor
forecast, it is a nonsensical one, and the cause is structural: a cubic polynomial is flexible enough
to fit any local shape but has no way to "know" that the series should stay non-negative once pushed
outside the range it was fit to.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="A forecast from a model fit to the raw series eventually goes negative, while the same regressors fit to the log series and exponentiated stay positive">
  <line x1="40" y1="20" x2="40" y2="200" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <text x="40" y="212" text-anchor="middle" font-size="11" fill="currentColor">last observed month</text>
  <line x1="30" y1="140" x2="350" y2="140" stroke="currentColor" stroke-width="1"/>
  <text x="352" y="144" font-size="11" fill="currentColor">0</text>
  <polyline points="40,60 70,50 100,65 130,90 160,110 190,130 220,150 250,165 280,178 310,185 340,190" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="345" y="200" text-anchor="end" font-size="12" fill="currentColor">fit to y</text>
  <polyline points="40,60 70,52 100,68 130,85 160,95 190,102 220,108 250,113 280,117 310,120 340,122" fill="none" stroke="currentColor" stroke-width="2" opacity="0.55" stroke-dasharray="6 3"/>
  <text x="345" y="108" text-anchor="end" font-size="12" fill="currentColor">fit to log y, exponentiated</text>
</svg>
<figcaption>Forecasting beyond the fitted data: extending the cubic-plus-seasonal model fit to the raw
series carries it below zero, while the same model fit to the logarithm and exponentiated back stays
positive by construction.</figcaption>
</figure>

The fix is the same move used above for the population log model, now for a genuinely practical reason
rather than an interpretive one: fit the identical seven regressors to $\log y$ instead of $y$,
forecast on the log scale, and exponentiate the forecast to return to the original units. Since
$e^t > 0$ for every real $t$, the exponentiated forecast can never be negative, however the underlying
linear model behaves once extrapolated.

## The general lesson

Two points recur across both examples and are worth holding on to past this particular lab:

1. **A trend function is only pinned down where there is data.** Linear, quadratic and log-linear fits
   to the population series are close to indistinguishable on the roughly 67 years they were fit to,
   and diverge by tens of millions of people 14 years past the end of the data. The shape of a curve
   *outside* the observed range is a property of the curve, chosen in advance, not something the data
   can correct.
2. **Fitting on the log scale and exponentiating back is a cheap guard against predictions leaving a
   natural domain.** Whenever the response is inherently non-negative — a population count, a search
   interest index — a linear (or polynomial, or seasonal) model fit directly to $y$ has no mechanism to
   respect that constraint once extrapolated, while the same model fit to $\log y$ respects it
   automatically, at the cost of the coefficients now describing proportional rather than absolute
   change.

## Sources

- US population dataset, derivation of the least-squares formulas, matrix form, prediction and
  uncertainty intervals: `berkeley-stat153` fall-2026 `CodeLabOne153248Fall2026.ipynb`,
  `01-us-population-dataset.md`.
- Quadratic trend fit and its extrapolated prediction: same notebook,
  `02-fitting-a-quadratic-trend.md`.
- Log-transformed trend fit and its extrapolated prediction: same notebook,
  `03-modeling-logarithms.md`.
- Google Trends "amazon" example — linear/quadratic/cubic progression, seasonal (Fourier) terms, the
  negative-forecast problem and the log-scale fix: `berkeley-stat153` fall-2025
  `CodeLabOne153248Fall2025.ipynb`, `02-google-trends-dataset-for-the-query-amazon.md`.
- The fall-2025 notebook's own US population file (`01-us-population-dataset.md`) and its separate
  derivation file (`03-derivation-of-the-least-squares-estimators-in-simple-linear.md`) cover the same
  regression and the same derivation as the fall-2026 version and were not repeated here; the
  fall-2025 explanation of the two kinds of prediction interval (`get_prediction`'s interval for the
  mean versus for a single observation) is folded into the discussion above.
- The Census Bureau's July 2040 population projection is a figure the fall-2026 notebook looks up
  externally (census.gov, 2023 summary tables, Table 1) for comparison; it is not itself part of the
  supplied lab material.
- Original notebook figures are referenced in the source markdown as omitted; no plot images were
  available to reproduce, only the printed regression output and forecast values.

---

[← 30. AR(p): Levels, Logs, and Differences](30-ar-p-levels-logs-and-differences.md) · [Contents](index.md) · [32. Causal Stationary AR(2) Example →](32-causal-stationary-ar-2-example.md)
