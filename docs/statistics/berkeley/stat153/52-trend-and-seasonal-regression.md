---
title: "52. Trend and Seasonal Regression"
course: "Berkeley Stat 153"
chapter: 52
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 52. Trend and Seasonal Regression

## What this covers

How do you fit a trend to a time series, and what do you do once a straight line is visibly wrong?
This chapter works through the two examples of a Berkeley STAT153 code lecture: fitting a straight
line to monthly US population figures by ordinary least squares, then building up polynomial and
seasonal (harmonic) regressors for a Google Trends search-interest series until the fit is
reasonable, and confronting what happens when that fitted model is used to forecast. It assumes
only that the reader can read the output of an OLS regression — coefficients, standard errors,
$R^2$ — and does not assume any prior exposure to time series.

## Regression on time

The idea behind everything below is to treat elapsed time itself, or some function of it, as the
covariate in an ordinary regression. Index the $n$ observations $t = 1, \dots, n$ and posit

$$y_t = \beta_0 + \beta_1 t + \varepsilon_t,$$

then estimate $\beta_0, \beta_1$ exactly as in any other linear regression, by least squares.
Nothing about the regression machinery changes; what changes from one series to the next is which
functions of $t$ belong on the right-hand side — a first power for a straight-line trend, higher
powers for curvature, and sines and cosines for periodic (seasonal) behaviour.

## A straight-line trend: US population

The first series is the FRED series `POPTHM`: the monthly population of the United States, in
thousands, from January 1959 to November 2024 — $n = 791$ observations. Taking $t = 1, \dots, 791$
and fitting $y_t = \beta_0 + \beta_1 t + \varepsilon_t$ by ordinary least squares,

```python
x = np.arange(1, len(y) + 1)          # covariate: 1, 2, ..., n
X = sm.add_constant(x)
linmod = sm.OLS(y, X).fit()
```

gives

$$\hat\beta_0 = 174575.15, \qquad \hat\beta_1 = 213.235, \qquad R^2 = 0.997.$$

Because $y$ is recorded in thousands, $\hat\beta_1$ says the population grows by about 213,235
people every month. $\hat\beta_0$ is the fitted population at $t = 0$ — one month before the first
observation, i.e. December 1958. The standard errors attached to the two coefficients (about $198$
and $0.43$) quantify the uncertainty in $\hat\beta_0$ and $\hat\beta_1$ themselves, not in any one
prediction. The fitted line tracks the data closely, but the lecture notes that actual population
growth diverges from the straight line over some stretches of the series.

### Extrapolating the line

Because the fitted model is just a function of $t$, it can be evaluated beyond the observed range.
The last observation, November 2024, is $t = 791$; January 2025 is two months later, $t = 793$, and
the point forecast is

$$\hat\beta_0 + 793\,\hat\beta_1 = 343670.7 \text{ thousand} \approx 343.67 \text{ million}.$$

`statsmodels`' `get_prediction` returns two different intervals around this point forecast: a
narrow one for the *mean* of the population process at $t = 793$, $[343281.2,\ 344060.2]$ thousand,
and a wider one for a *single new observation* at $t = 793$, $[338194.8,\ 349146.6]$ thousand. The
wider interval is the one normally used in practice. How either interval is actually derived is
left by the lecture for a later class, and is not covered here.

## Beyond a straight line: polynomial trends

The second series is a monthly Google Trends index: relative search interest for the query
"amazon", from January 2004 to January 2025, $n = 253$ observations. As before the covariate is
$t = 1, \dots, 253$.

A purely linear fit,

```python
x = np.arange(1, len(y) + 1)
X = sm.add_constant(x)
linmod = sm.OLS(y, X).fit()
```

gives $R^2 = 0.856$ — a large number — but the fitted line visibly fails to track the shape of the
series. A high $R^2$ is compatible with a systematically wrong trend, if the discrepancy between fit
and data is itself smooth rather than noise-like.

Adding a quadratic term,

```python
x2 = x ** 2
X = sm.add_constant(np.column_stack([x, x2]))
quadmod = sm.OLS(y, X).fit()
```

raises $R^2$ only to $0.877$, and the fit is still judged "not good." `statsmodels` also flags the
regression's condition number as large ($8.7 \times 10^4$), warning of possible multicollinearity or
other numerical problems — a caution that recurs, more severely, once a cubic term is added:

```python
x3 = x ** 3
X = sm.add_constant(np.column_stack([x, x2, x3]))
cubmod = sm.OLS(y, X).fit()
```

The cubic fit reaches $R^2 = 0.921$ and is judged "pretty good," though the condition number has
grown further still, to $2.5 \times 10^7$, with the same warning attached.

## Capturing the season: harmonic regression

The Amazon search series is monthly and has a visible seasonal pattern: some months are
consistently higher or lower than others, year after year. A polynomial in $t$ has no way to
represent that — it cannot repeat. The fix is to add periodic functions of $t$ directly. For monthly
data the natural period is 12, and the simplest periodic regressors of that period are

$$\cos\!\left(\frac{2\pi t}{12}\right), \qquad \sin\!\left(\frac{2\pi t}{12}\right).$$

Added to the cubic trend, these two terms improve the fit, but the lecture notes it is "not enough
to capture the actual oscillation" in the data — the true seasonal shape is not a pure sine wave.
Adding a second pair at twice the frequency (period 6 months),

$$\cos\!\left(\frac{2\pi \cdot 2t}{12}\right), \qquad \sin\!\left(\frac{2\pi \cdot 2t}{12}\right),$$

improves the fit substantially further. In general, stacking $K$ such pairs at the fundamental
frequency and its harmonics,

$$y_t = \beta_0 + \beta_1 t + \beta_2 t^2 + \beta_3 t^3 + \sum_{k=1}^{K}\left[a_k \cos\!\left(\frac{2\pi k t}{12}\right) + b_k \sin\!\left(\frac{2\pi k t}{12}\right)\right] + \varepsilon_t,$$

lets the fitted seasonal shape depart increasingly from a single sine wave: $K = 1$ was the first
attempt above, $K = 2$ the improved one. Fitting either is still an ordinary OLS regression — the
design matrix just gets more columns:

```python
x4, x5 = np.cos(2 * np.pi * x * (1/12)), np.sin(2 * np.pi * x * (1/12))
x6, x7 = np.cos(2 * np.pi * x * (2/12)), np.sin(2 * np.pi * x * (2/12))
X = sm.add_constant(np.column_stack([x, x2, x3, x4, x5, x6, x7]))
seasmod = sm.OLS(y, X).fit()
```

## Extrapolation, and why the scale of the fit matters

The fitted $K = 2$ model can be used to forecast future months by evaluating the same functions of
$t$ beyond the observed range:

```python
nf = 100
xf = np.arange(len(x) + 1, len(x) + 1 + nf)
Xf = sm.add_constant(np.column_stack([
    xf, xf**2, xf**3,
    np.cos(2*np.pi*xf*(1/12)), np.sin(2*np.pi*xf*(1/12)),
    np.cos(2*np.pi*xf*(2/12)), np.sin(2*np.pi*xf*(2/12)),
]))
pred = Xf @ np.array(seasmod.params)
```

The forecast starts out reasonably — in the 50s and 60s, comparable to recent search interest — but
the cubic term's negative leading coefficient ($-1.749 \times 10^{-5}$) eventually dominates: around
60 months into the 100-month horizon the forecast crosses zero, and it keeps falling, reaching about
$-88$ by the end of the horizon. A negative value is meaningless for a search-popularity index, which
by construction cannot be negative.

The fix used in the lecture is to fit the same regression to $\log y$ instead of $y$:

```python
ylog = np.log(y)
seasmodlog = sm.OLS(ylog, X).fit()
predlog = Xf @ np.array(seasmodlog.params)
pred_positive = np.exp(predlog)
```

Because the forecast is now made on the log scale and only exponentiated afterwards, it is positive
regardless of what the underlying linear predictor does — $\exp$ of any real number is positive. The
two forecasts, on the original scale and on the exponentiated log scale, agree closely near the end
of the observed data and then diverge as the horizon lengthens.

<figure>
<svg viewBox="0 0 400 240" role="img" aria-label="Forecasts from a cubic-plus-seasonal trend model on the original scale run negative, while the same model fit on the log scale and exponentiated stays positive">
  <line x1="40" y1="160" x2="380" y2="160" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <text x="30" y="164" text-anchor="end" font-size="11" fill="currentColor">0</text>
  <line x1="230" y1="25" x2="230" y2="205" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2" opacity="0.5"/>
  <text x="230" y="218" text-anchor="middle" font-size="11" fill="currentColor">last observed month</text>
  <polyline points="40,150 60,128 80,140 100,108 120,126 140,98 160,116 180,92 200,106 220,114 230,120"
            fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M230,120 C260,116 300,132 380,145" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M230,120 C270,112 300,158 380,212" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5 3"/>
  <text x="300" y="95" text-anchor="middle" font-size="11" fill="currentColor">log scale, exponentiated</text>
  <text x="335" y="200" text-anchor="middle" font-size="11" fill="currentColor">original scale</text>
</svg>
<figcaption>Extending the fitted cubic-plus-harmonic model past the observed data (left of the
dashed line): on the original scale the negative leading cubic coefficient eventually drags the
forecast below zero, which is meaningless for a search-popularity index; fitting the same model to
$\log y$ and exponentiating the forecast keeps it positive by construction.</figcaption>
</figure>

## Sources

- Both worked examples are from the Berkeley STAT153 (Spring 2025) code lecture
  `CodeLectureThree153248Spring2025.ipynb`: the US Population Dataset section and the Google Trends
  Dataset for the query Amazon section, converted at
  `docs/statistics/berkeley/stat153/spring-2025/CodeLectureThree153248Spring2025/01-us-population-dataset.md`
  and `.../02-google-trends-dataset-for-the-query-amazon.md`. No slides or spoken transcript were
  supplied for this lecture; the notebook's own markdown commentary is the only exposition
  available.
- The US population series is the FRED series `POPTHM` (monthly, thousands), from
  https://fred.stlouisfed.org/; the search-interest series is from Google Trends,
  https://trends.google.com/trends/, for the query "amazon" (see also
  https://en.wikipedia.org/wiki/Google_Trends, cited in the notebook). Neither underlying CSV file
  was supplied — only the code and its printed output.
- Every plot referenced in the discussion (the fitted line against the data, the linear/quadratic/
  cubic/seasonal comparison plots, the forecast plot) was omitted from the converted notebook; the
  descriptions of fit quality here ("decent," "not good," "pretty good," "much improved") are the
  notebook's own words, not a reading of the missing images.
- How the confidence and prediction intervals produced by `get_prediction` are actually derived is
  explicitly deferred by the lecture ("We shall see how these predictions are obtained later") and
  is not covered here.

---

[← 51. Bayesian Regularization and Variance Models](51-bayesian-regularization-and-variance-models.md) · [Contents](index.md) · [53. Bayesian Regularization of Trends →](53-bayesian-regularization-of-trends.md)
