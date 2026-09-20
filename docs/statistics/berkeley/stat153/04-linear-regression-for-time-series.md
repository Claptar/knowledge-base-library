---
title: "4. Linear Regression for Time Series"
course: "Berkeley Stat 153 Fall 2024"
chapter: 4
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 4. Linear Regression for Time Series

## What this covers

This chapter covers ordinary least squares (OLS) as a way to fit a straight line relating a response
variable to a covariate, and the two ways that specializes when the covariate is time or the series
itself. It assumes the autocovariance and autocorrelation function (ACF) from the previous lecture,
since checking whether a regression's residuals behave like noise is exactly a residual-ACF check.

## Regression: response, covariate, and two roles for time

Given two variables $y$ and $x$, the goal of regression is to predict $y$ from $x$. $y$ is the
**response** (or dependent) variable, $x$ is the **covariate** (or independent) variable. A standard
example: predicting the height of an adult man ($y$) from the height of his father ($x$). With a
single covariate this is **simple linear regression**:

$$y = \beta_0 + \beta_1 x + \epsilon$$

$\beta_0$ is the intercept — the value of $y$ when $x=0$ — and $\beta_1$ is the change in $y$ for a
one-unit change in $x$. (With several covariates $x_1,\dots,x_p$ this is **multiple regression**,
not covered here.) Given paired data $(x_1,y_1),\dots,(x_n,y_n)$,

$$y_i = \beta_0 + \beta_1 x_i + \epsilon_i,$$

and estimates $\hat\beta_0,\hat\beta_1$ from the data are used to predict $\hat y$ for a new $x$.

For a time series $y_1,\dots,y_n$ — a single observed variable, not a set of pairs — there are two
natural ways to turn this into a regression problem, by choosing what plays the role of $x$:

1. **Time itself as the covariate**: $x_i = i$. This is what a linear trend line is — the DJIA,
   fMRI, and population-over-time examples from earlier in the course all fit this pattern.
2. **A lagged version of $y$ as the covariate**: $x_i = y_{i-1}$, predicting the current value from
   the previous one. This is called **lagged regression**, or **autoregression**.

This chapter works through the first case in detail.

## Estimating the coefficients

Software such as `statsmodels` fits $\hat\beta_0,\hat\beta_1$ by **least squares**: minimizing the
error sum of squares

$$Q(\beta_0,\beta_1) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2.$$

It is worth keeping two versions of this problem apart. At the **population level**, we ask for the
line minimizing $\mathbb E[(y-\beta_0-\beta_1 x)^2]$ — the best-fitting line for the underlying joint
distribution of $(x,y)$. At the **sample level**, we minimize $Q$ over the $n$ observations we
actually have; this is what a fitting routine does, and $\hat\beta_0,\hat\beta_1$ is only an estimate
of the population quantities.

The sample-level minimizer is found the usual way: set the partial derivatives of $Q$ to zero.

$$\frac{\partial Q}{\partial \beta_0} = -2\sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i) = 0
\quad\Longrightarrow\quad \hat\beta_0 = \bar y - \hat\beta_1 \bar x,$$

$$\frac{\partial Q}{\partial \beta_1} = -2\sum_{i=1}^n x_i(y_i - \beta_0 - \beta_1 x_i) = 0.$$

Substituting the first equation into the second and solving gives

$$\hat\beta_1 = \frac{\sum_{i=1}^n (x_i - \bar x)(y_i - \bar y)}{\sum_{i=1}^n (x_i - \bar x)^2},
\qquad \bar x = \frac{x_1+\cdots+x_n}{n},\quad \bar y = \frac{y_1+\cdots+y_n}{n}.$$

So $\hat\beta_1$ is (up to normalization) the sample covariance between $x$ and $y$ divided by the
sample variance of $x$, and $\hat\beta_0$ is whatever forces the fitted line through the point of
averages $(\bar x,\bar y)$.

## Fitting with statsmodels, and the intercept trap

Take a simulated example: $t = 1,\dots,100$, and

$$y_t = 2 + 0.5t + 4w_t,\qquad w_t \sim \text{i.i.d. noise}.$$

Fitting `sm.OLS(y, t)` — passing $t$ alone — gives a slope estimate of $0.525$, close to the true
$\beta_1 = 0.5$. But nothing in that call told `statsmodels` to estimate an intercept: `OLS` fits
exactly the columns you hand it, so this really fits $y_i = \beta_1 t_i + \epsilon_i$, a line forced
through the origin. Since the data don't sit near $(0,0)$ (at $t=0$ the true line is at $y=2$), the
forced-through-origin fit sits below the cluster of points even though its slope looks reasonable.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="A scatter of points offset from the origin, with a line forced through the origin sitting below the cluster and a line with a free intercept fitting through it">
  <line x1="40" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="205" text-anchor="middle" font-size="12" fill="currentColor">t</text>
  <text x="22" y="30" text-anchor="middle" font-size="12" fill="currentColor">y</text>
  <text x="34" y="192" text-anchor="end" font-size="11" fill="currentColor">0</text>
  <g fill="currentColor">
    <circle cx="80" cy="150" r="3"/>
    <circle cx="100" cy="145" r="3"/>
    <circle cx="120" cy="138" r="3"/>
    <circle cx="140" cy="130" r="3"/>
    <circle cx="160" cy="122" r="3"/>
    <circle cx="180" cy="110" r="3"/>
    <circle cx="200" cy="100" r="3"/>
    <circle cx="220" cy="90" r="3"/>
    <circle cx="240" cy="78" r="3"/>
    <circle cx="260" cy="65" r="3"/>
    <circle cx="280" cy="55" r="3"/>
  </g>
  <line x1="40" y1="180" x2="300" y2="95" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="215" y="112" font-size="11" fill="currentColor">no intercept</text>
  <line x1="45" y1="158" x2="295" y2="52" stroke="currentColor" stroke-width="2"/>
  <text x="190" y="60" font-size="11" fill="currentColor">with intercept</text>
</svg>
<figcaption>Forcing the fitted line through the origin (dashed) undershoots data that does not
start near $(0,0)$; adding a free intercept (solid) lets the line sit on the cluster.</figcaption>
</figure>

To estimate an intercept, add a column of ones to the covariate matrix — `sm.add_constant(t)` — then
fit `sm.OLS(y, T)`. On the same data this recovers $\hat\beta_0 = 1.303$ (95% CI $[-0.155, 2.762]$,
consistent with the true $\beta_0=2$) and $\hat\beta_1 = 0.506$ (95% CI $[0.480, 0.531]$, tight
around the true $\beta_1=0.5$). The lesson generalizes beyond this one example: an OLS call fits
only the columns you give it, and a model without an explicit constant column is a claim that the
line passes through the origin — rarely something you actually want.

## Checking the fit: do the residuals look like noise?

Because this is a *time series* regression, fitting the line is not the end of the check. The model
assumes the error term $\epsilon_t$ is weakly stationary, and the residuals $y_t - \hat y_t$ are the
only handle on $\epsilon_t$ available. Two diagnostics from the previous lecture's toolkit reappear
here:

- plot the residuals against time and look for any remaining trend or pattern;
- plot the residuals' autocorrelation function (ACF) and check that it looks like white noise — no
  significant autocorrelation at any lag.

If either shows structure, the model is missing something systematic that a straight line in time
cannot capture.

## A messier real example: chicken prices

The chicken-price series from `astsa` (monthly, 2001–2016) makes the point concrete. Fitting
`sm.OLS(yvec, xvec)` with $x_i = i$ but no constant again returns only a slope — the fit is again
forced through the origin, and is not really the model $y_i=\beta_0+\beta_1 x_i+\epsilon_i$ that was
intended. Adding the constant with `sm.add_constant` gives

$$\hat\beta_0 = 58.58,\qquad \hat\beta_1 = 0.2993 \quad (95\%\ \text{CI } [0.29, 0.31]),$$

read as: chicken price started around 58.6 cents/lb and rose by about 0.30 cents/lb per month over
the sample.

But the series visibly has more structure than a straight trend — there appear to be seasonal
fluctuations riding on top of it, the kind of feature commodity prices are known to show. So the
question the lecture poses of the residuals is the diagnostic from the previous section applied for
real: do the residuals show any strong or unmodeled dependence on time? Since the trend is clearly
not the whole story here, the expectation is that the residual plot and its ACF surface exactly the
leftover structure a single straight line cannot absorb — the reason a time series course does not
stop at ordinary linear regression, and goes on to autoregression and other models for that leftover
dependence (the second of the two covariate choices above).

## Sources

- Lecture notes: `05_linear_regression_notes.md` (*Lecture 5 Notes — Simple Linear Regression*,
  Liberty Hamilton, 3 Feb 2026) — the regression setup, the two time-series covariate choices, the
  OLS minimization problem, and the closed-form $\hat\beta_0,\hat\beta_1$. Cross-checked against the
  lower-fidelity PDF reconstruction `Lec05_Notes.md`, which covers the same material (through its
  §2.1) with no discrepancy in the parts it reconstructs.
- Worked notebook `Lecture5.ipynb`, split into three parts:
  - `Lecture5/01-introduction.md` — the simulated linear-trend-plus-noise example, the
    without-intercept vs. with-intercept fits, their coefficient estimates and confidence
    intervals, and the residual/ACF diagnostic.
  - `Lecture5/02-another-messier-example.md` — loading and plotting the `astsa` chicken-price data.
  - `Lecture5/03-chicken-price-regression.md` — fitting the trend line to chicken prices, without
    and with an intercept, the coefficient estimates and confidence interval, and the residual
    diagnostic question.
- The assigned reading, Chapter 2 of Shumway and Stoffer, is referred to by the lecture notes but
  not contained in the supplied material.
- No transcript, separate written notes, or problem set were supplied for this lecture.

---

[← 3. Autocovariance and Stationarity](03-autocovariance-and-stationarity.md) · [Contents](index.md) · [5. OLS and MLE in Regression →](05-ols-and-mle-in-regression.md)
