---
title: "61. Regression for Time Series Trends"
course: "Berkeley Stat 153 Fall 2024"
chapter: 61
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 61. Regression for Time Series Trends

## What this covers

How do you use ordinary least squares — a tool built for independent observations — on a series
that trends over time, and get a sensible forecast out of it? This chapter follows two worked
illustrations from the course, the monthly US Consumer Price Index (CPI) and the monthly US
population, through a sequence of regression models of increasing sophistication: a straight
line, a straight line in logarithms, a curved trend, a model built on the *growth rate* instead of
the level, and finally models that let the growth rate itself bend at one or two unknown points in
time. It assumes you can already fit and read an OLS regression (coefficients, fitted values,
residuals, confidence intervals) but nothing about time series specifically — that vocabulary is
built up as it is needed.

## The forecasting problem

Take a series $y_1, \dots, y_n$ observed at equally spaced times $t = 1, \dots, n$, and suppose it
trends: the monthly US population grows from about 176 million in 1959 to about 343 million by
2026, and the CPI has been climbing for as long as it has been measured. The question the course
poses concretely is: what will the US population be in July 2040, fourteen years past the last
observed month? The Census Bureau projects 355.309 million; the United Nations projects 370.209
million. The rest of this chapter builds several regression-based answers to that question and
compares them against these two external benchmarks, and does the same for the CPI series with a
different target quantity — the historical rate of inflation.

## Model 1: a straight line in the levels

The simplest model treats time itself as the covariate:
$$
y_t = \beta_0 + \beta_1 t + \epsilon_t .
$$
Here $\beta_0$ is the level at time $0$ (one period before the data starts) and $\beta_1$ is the
change in $y$ from one time step to the next. Fitted values are $\hat\beta_0 + \hat\beta_1 t$, and
residuals are $y_t - \hat\beta_0 - \hat\beta_1 t$ — the part of the series the straight line does
not explain.

Fitting this to the US population data (in `statsmodels`, `sm.OLS(y, X).fit()` with `X` the
two-column design matrix of ones and $t$) gives $\hat\beta_0 \approx 174{,}586$ thousand and
$\hat\beta_1 \approx 213.2$ thousand people per month, for an $R^2$ of 0.997 — a very high number,
but not a meaningful check of fit here, because *any* strongly trending series looks highly
"explained" by a trend line. The more informative diagnostic is the residual plot: every recent
residual is negative, meaning the fitted line runs above the actual recent data, and the residuals
have visible structure rather than looking like noise — a sign the straight line is missing
curvature that a better model should capture. Extrapolated 168 months forward, Model 1 predicts
**383.32 million** for July 2040, well above both external projections.

**A fitting trap worth flagging explicitly.** `sm.OLS(y, x)` in `statsmodels` does *not* add an
intercept by default — it silently fits $y_t = \beta_1 t + \epsilon_t$, the line through the
origin. On the CPI data this changes both the numbers and the story: with no constant, the
uncentered $R^2$ is 0.892; adding one via `sm.add_constant` before fitting raises it to 0.966 and
recovers a sensible intercept ($\hat\beta_0 \approx 2.986$ on the log scale, see below). Any
regression with time as covariate should be checked for this before the coefficients are trusted.

## Model 2: a straight line in the logarithm, and inflation as a slope

Raw dollar or count increases are not how growth is usually reported — inflation is quoted as a
percentage, and so is population growth. The fix is to regress the *logarithm* of the series
instead:
$$
\log y_t = \beta_0 + \beta_1 t + \epsilon_t .
$$
The reason $\beta_1$ becomes a percentage-change parameter is the standard log approximation:
$$
\log y_t - \log y_{t-1} = \log \frac{y_t}{y_{t-1}} \approx \frac{y_t - y_{t-1}}{y_{t-1}} ,
$$
so a one-unit increase in $t$ changes $\log y_t$ by $\beta_1$, which is approximately the
*fractional* change in $y_t$ from one period to the next. Hence $100 \beta_1$ is the percent change
per period, and $12 \times 100 \beta_1$ (for monthly data) annualizes it.

Applied to the CPI series, this gives $\hat\beta_1 = 0.0032$, i.e. a month-to-month rate of
$0.32\%$ and an annualized historical inflation rate of
$$
12 \times 100 \times 0.0032 = 3.794\%, \qquad \text{95\% CI: } [3.749\%,\ 3.840\%].
$$
Applied to the population series, the same regression gives $\hat\beta_1 = 0.0008$, an annual
population growth rate estimate of $0.96\%$. But the residuals again show structure: in recent
years actual log-population falls visibly below the fitted line, meaning growth has slowed below
what a *constant* rate can capture. Extrapolated forward, Model 2 predicts **412.76 million** for
July 2040 — the worst of all the models here, because a constant percentage growth rate compounds
the historical (higher) average rate forward for another fourteen years.

## Model 3: letting the growth rate curve

To let the rate of growth itself change over time, add a quadratic term on the log scale:
$$
\log y_t = \beta_0 + \beta_1 t + \beta_2 t^2 + \epsilon_t .
$$
Differentiating, the instantaneous growth rate is no longer constant but $\beta_1 + 2\beta_2 t$, so
a negative $\hat\beta_2$ produces a decelerating growth rate — exactly the pattern the data show,
and indeed $\hat\beta_2 \approx -2.5 \times 10^{-7}$ comes out negative. The residual scale shrinks
compared with Model 2, and the July 2040 prediction improves to **385.15 million** — still on the
high side, but less extreme.

## The jump problem

Models 1–3 share an awkward feature that only shows up once you extrapolate: the fitted trend line
at $t = n$ need not pass through the actual last observation $y_n$, since it is the best-fitting
line for *all* $n$ points, not a line pinned to the endpoint. Extending it into the future then
produces a visible discontinuity — a jump — between the last observed value and the first
prediction, which is implausible: there is no reason the US population in August 2026 should
suddenly be noticeably different from the observed July 2026 value. The next model is designed
specifically to remove this jump by construction.

## Model 4: modelling the growth rate directly

Instead of regressing the level or its logarithm on time, regress the *differenced* log series —
the growth rate itself:
$$
g_t = \log y_t - \log y_{t-1}, \qquad g_t = \beta_0 + \beta_1 t + \epsilon_t .
$$
The point of this reformulation is how forecasts get built back up. Since
$\log y_t = \log y_{t-1} + g_t$, once $\hat g_{n+1}, \hat g_{n+2}, \dots$ are predicted from the
fitted line, the population path is reconstructed by cumulating them starting from the *actual*
last observed value $y_n$:
$$
\log \hat y_{n+h} = \log y_n + \sum_{j=1}^h \hat g_{n+j},
\qquad
\hat y_{n+h} = y_n \exp\left( \sum_{j=1}^h \hat g_{n+j} \right).
$$
Every forecast is now anchored at $y_n$ by construction, so there is no jump: the forecast for
August 2026 is the observed July 2026 population times one month's predicted growth factor, which
is close to 1 since monthly growth rates are small.

Fitting this to the population growth rates gives a strongly negative slope
($\hat\beta_1 \approx -7.8\times 10^{-7}$, with $R^2 = 0.448$ — lower than the level models, because
growth rates are noisier than levels, but that noise is now honestly separated from the trend). The
July 2040 prediction is **369.28 million**, close to the United Nations projection of 370.21
million, and markedly better than any of Models 1–3.

## Models 5 and 6: letting the growth rate itself bend

The growth-rate series still shows more structure than a single straight line captures, so the
next step lets the line change slope at one or more unknown points in time. The building block is
the **hinge function** (also called ReLU, "Rectified Linear Unit," in the machine-learning
literature):
$$
(t - c)_+ = \max(t - c,\ 0) = \begin{cases} t - c & t \ge c \\ 0 & t < c \end{cases}.
$$
Adding this as a covariate,
$$
g_t = \beta_0 + \beta_1 t + \beta_2 (t - c)_+ + \epsilon_t,
$$
fits two straight-line segments joined continuously at $c$: slope $\beta_1$ before $c$, slope
$\beta_1 + \beta_2$ after it. If $c$ is *known*, this is ordinary multiple linear regression on the
covariates $1, t, (t-c)_+$. If $c$ is unknown — as here — it must be estimated, which makes the
problem nonlinear in $c$. The course's method (developed properly later) is a brute-force search:
try every candidate month $c$, fit the linear regression for that $c$, record the residual sum of
squares (RSS), and keep the $c$ that minimizes it.

On the population growth-rate series this gives $\hat c = 75$, corresponding to April 1965. Fixing
$c$ at that value and refitting by OLS gives slopes $\hat\beta_1 \approx -8.1\times 10^{-6}$ before
the break and $\hat\beta_1+\hat\beta_2 \approx -6\times 10^{-7}$ after it — a milder decline after
1965 than before. Because the post-break slope is slightly less negative than Model 4's single
overall slope, this model's July 2040 prediction is slightly higher: **373.12 million**.

The same idea extends to two change points:
$$
g_t = \beta_0 + \beta_1 t + \beta_2 (t - c_1)_+ + \beta_3 (t - c_2)_+ + \epsilon_t,
$$
a curve with three segments (for $c_1 < c_2$): slope $\beta_1$ before $c_1$, slope
$\beta_1 + \beta_2$ between $c_1$ and $c_2$, and slope $\beta_1 + \beta_2 + \beta_3$ after $c_2$.
Estimating both breakpoints means searching over the whole grid of pairs $c_1 < c_2$ and keeping
the pair with smallest RSS. On the population data this lands on $\hat c_1 = 108$ (January 1968)
and $\hat c_2 = 453$ (October 1996), with a fitted slope after October 1996 that is smaller than in
any earlier model — this is the model that most strongly captures the recent slowdown, and its
July 2040 prediction, **356.95 million**, comes closest of all six models to the Census Bureau's
355.31 million.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="A piecewise-linear growth-rate curve with two change points where the slope shifts">
  <line x1="30" y1="190" x2="380" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <text x="378" y="207" text-anchor="end" font-size="12" fill="currentColor">t (time)</text>
  <line x1="30" y1="190" x2="30" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="36" y="24" font-size="12" fill="currentColor">g_t</text>

  <line x1="150" y1="190" x2="150" y2="42" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <line x1="270" y1="190" x2="270" y2="42" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <text x="150" y="36" text-anchor="middle" font-size="12" fill="currentColor">c&#8321;</text>
  <text x="270" y="36" text-anchor="middle" font-size="12" fill="currentColor">c&#8322;</text>

  <polyline points="40,80 150,110 270,120 370,175" fill="none" stroke="currentColor" stroke-width="2"/>

  <text x="65" y="90" font-size="11" fill="currentColor">slope &#946;&#8321;</text>
  <text x="178" y="128" font-size="11" fill="currentColor">slope &#946;&#8321;+&#946;&#8322;</text>
  <text x="285" y="167" font-size="11" fill="currentColor">slope &#946;&#8321;+&#946;&#8322;+&#946;&#8323;</text>
</svg>
<figcaption>Adding hinge terms $(t-c_1)_+$ and $(t-c_2)_+$ to a linear regression fits three
straight segments that join continuously at $c_1$ and $c_2$; only the slope changes at a
breakpoint, never the level. Schematic — not the actual fitted population growth curve.</figcaption>
</figure>

## Comparing the six trend models for population

| Model | July 2040 prediction (millions) |
| --- | --- |
| 1. Linear trend, levels | 383.32 |
| 2. Log-linear trend | 412.76 |
| 3. Quadratic log trend | 385.15 |
| 4. Growth-rate trend | 369.28 |
| 5. Growth rate, one change point ($\hat c$ = Apr 1965) | 373.12 |
| 6. Growth rate, two change points ($\hat c_1$ = Jan 1968, $\hat c_2$ = Oct 1996) | 356.95 |
| Census Bureau projection | 355.31 |
| United Nations projection | 370.21 |

The spread across models this wide, on the same data, is itself the lesson: which trend
assumption you build in — constant level growth, constant log growth, one break, two breaks —
determines the forecast far more than any refinement within a fixed model class.

## A different strategy: lagged (autoregressive) regression

All the models above use *time* as the covariate. An entirely different choice, illustrated on the
CPI series, is to use the series' own previous value as the covariate — regress $\log \text{CPI}_t$
on $\log \text{CPI}_{t-1}$:
$$
\log \text{CPI}_t = \beta_0 + \beta_1 \log \text{CPI}_{t-1} + \epsilon_t .
$$
Fitting this gives $\hat\beta_0 = 0.0039$ and $\hat\beta_1 = 0.9998$, remarkably close to 1. That
is informative: if $\beta_1$ were exactly 1, the model would read
$$
\log \text{CPI}_t - \log \text{CPI}_{t-1} \approx \beta_0 + \epsilon_t,
$$
i.e. it would just be fitting a constant to the month-to-month log difference — the same quantity
underlying the log-linear trend model, approached from a completely different regression setup.
Reading off $\hat\beta_0 = 0.0039$ this way gives a monthly rate of $0.39\%$ and an annualized
estimate of $12 \times 100 \times 0.0039 = 4.645\%$ — noticeably higher than the $3.794\%$ from the
time-regression model. The gap is exactly the effect of the approximation $0.9998 \approx 1$: the
exact model is
$$
\log \text{CPI}_t - 0.9998 \log \text{CPI}_{t-1} = 0.0039 + \epsilon_t
\iff
\log \frac{\text{CPI}_t}{\text{CPI}_{t-1}} = 0.0039 - 0.0002 \log \text{CPI}_{t-1} + \epsilon_t,
$$
and the correction term $0.0002 \log \text{CPI}_{t-1}$ has mean about $0.0009$ over the sample —
not negligible, and it is what pulls $0.0039$ down toward the time-regression estimate once
accounted for.

The two CPI-based inflation estimates also carry very different uncertainty:

| Method | Annual inflation estimate | 95% CI |
| --- | --- | --- |
| Log-linear trend on time | 3.794% | [3.749%, 3.840%] |
| Lagged (AR-type) regression | 4.645% | [3.286%, 6.004%] |

The lagged model's interval is much wider. Plotting the individual month-to-month annualized rates
$100 \times 12 \times (\log \text{CPI}_t - \log \text{CPI}_{t-1})$ against time shows why: they
swing widely from month to month, and the lagged regression's precision is tied to that raw
variability, whereas the time-regression estimate effectively averages the whole trend over the
full span and so is much less sensitive to individual volatile months.

## Differencing, as a recurring idea

Two constructions in this chapter — the growth-rate series $g_t = \log y_t - \log y_{t-1}$ and the
lagged CPI regression, which reduces (once $\hat\beta_1 \approx 1$) to modelling the same
difference — both work with the series *differenced* rather than in levels. This turns out to be a
generally useful move in time series analysis: differencing a trending series often leaves
something closer to noise around a constant or slowly varying level, which is much easier to model
well. Both source lectures flag this as a theme the course returns to, alongside a fuller treatment
of autoregressive models.

## Sources

- Berkeley STAT 153, fall 2025, `CodeLectureTwo153248Fall2025.ipynb` (CC BY 4.0): "CPI Regression
  with Time as Covariate" (log-linear trend model, the `sm.add_constant` fitting trap, and the
  historical inflation-rate estimate with confidence interval) and "Lagged Regression for CPI"
  (the AR-type lagged regression, its coefficient near 1, the correction-term derivation, and the
  confidence-interval comparison).
- Berkeley STAT 153, fall 2026, `CodeLectureTwo153248Fall2026.ipynb` (CC BY 4.0): "Introduction"
  (the US population dataset and the forecasting question), "Model 1" through "Model 6" (the
  linear, log-linear, quadratic, growth-rate, and one- and two-change-point models, their fitted
  coefficients, residual diagnostics, and July 2040 predictions, plus the closing remark on
  differencing).
- The Census Bureau and United Nations population projections for July 2040, and the specific
  numerical estimation method for unknown change points, are referred to in the lecture as
  external/forthcoming material and are not derived within either notebook.

---

[← 60. ARMA and ARIMA Model Identification](60-arma-and-arima-model-identification.md) · [Contents](index.md) · [62. The Discrete Fourier Transform →](62-the-discrete-fourier-transform.md)
