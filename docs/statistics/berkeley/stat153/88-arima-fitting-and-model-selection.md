---
title: "88. ARIMA Fitting and Model Selection"
course: "Berkeley Stat 153 Fall 2024"
chapter: 88
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 88. ARIMA Fitting and Model Selection

## What this covers

This chapter works through Lab 12: two independent pieces built around causal ARMA solutions and
ARIMA model selection. The first shows that a specific AR(2) recursion has a causal stationary
solution and derives its infinite-order moving-average (MA($\infty$)) representation by hand. The
second fits four different ARIMA specifications to a real monthly time series — total US
construction spending — and uses AIC and BIC to compare them. It assumes the reader already has AR,
MA and ARIMA models, the backshift operator $B$, the characteristic polynomial of an AR process,
and the definitions of causality and stationarity. (Lecture 22, referenced in this lab, is where
the four ARIMA models were first fit; that lecture is not among the inputs for this chapter.)

## Causal stationarity of an AR(2) process

Consider the equation
$$y_t - 0.5 y_{t-1} + 0.25 y_{t-2} = \epsilon_t.$$

In operator form this is $\phi(B) y_t = \epsilon_t$ with characteristic polynomial
$$\phi(z) = 1 - 0.5z + 0.25z^2.$$

Its roots are $2e^{\pm i\pi/3}$, both of modulus $2$. Because every root of $\phi$ lies strictly
outside the unit circle, the equation has a causal stationary solution — "causal" meaning $y_t$ can
be written as a one-sided function of present and past $\epsilon$'s only, $y_t = \sum_{j\ge 0}
\psi_j \epsilon_{t-j}$.

To find the $\psi_j$ explicitly, factor $\phi$ using its roots:
$$\phi(z) = \left(1 - 0.5e^{i\pi/3}z\right)\left(1 - 0.5e^{-i\pi/3}z\right),$$
and write $a_1 = 0.5e^{i\pi/3}$, $a_2 = 0.5e^{-i\pi/3}$, so $\phi(z) = (1-a_1z)(1-a_2z)$. A
partial-fraction split of $1/\phi(z)$,
$$\frac{1}{(1-a_1z)(1-a_2z)} = \frac{a_1}{a_1-a_2}\cdot\frac{1}{1-a_1z} + \frac{a_2}{a_2-a_1}\cdot\frac{1}{1-a_2z},$$
turns each factor into a geometric series (valid since $|a_1|,|a_2| < 1$), and collecting the
coefficient of $z^j$ gives
$$\psi_j = \frac{a_1^{j+1}-a_2^{j+1}}{a_1-a_2}.$$

Since $a_1,a_2$ are a complex-conjugate pair, this simplifies to a real, damped oscillation:
$$\psi_j = (0.5)^j\,\frac{\sin\big((j+1)\pi/3\big)}{\sin(\pi/3)} = \frac{2}{\sqrt3}(0.5)^j
\sin\!\left(\frac{(j+1)\pi}{3}\right).$$

The solution is then
$$y_t = \sum_{j=0}^{\infty}\psi_j\,\epsilon_{t-j} = \frac{2}{\sqrt3}\sum_{j=0}^{\infty}(0.5)^j
\sin\!\left(\frac{(j+1)\pi}{3}\right)\epsilon_{t-j},$$
an MA($\infty$) representation of the causal stationary AR(2) process. The lab checks this by
comparing the hand-computed $\psi_j$ against `ArmaProcess(ar, ma).arma2ma(lags=20)` — statsmodels'
built-in routine for converting any causal ARMA process to its MA($\infty$) form — and the two
columns agree to numerical precision. The general point: whenever every root of the characteristic
polynomial has modulus greater than $1$, software can produce the $\psi_j$ directly, but the
partial-fraction argument is what explains *why* they decay geometrically and oscillate at a
frequency set by the argument of the complex root.

## Fitting ARIMA models to a real series

The running example is TTLCONS, FRED's total construction spending series, monthly from January
1993, log-transformed to $y_t = \log(\mathrm{TTLCONS}_t)$, giving $n = 386$ observations. Four
models, previously fit in lecture, are revisited here for the fitting mechanics and for model
comparison:

1. **AR(3) on the first difference, with intercept:**
   $$y_t - y_{t-1} = \phi_0 + \phi_1(y_{t-1}-y_{t-2}) + \phi_2(y_{t-2}-y_{t-3}) + \phi_3(y_{t-3}-y_{t-4}) + \epsilon_t$$
2. **ARIMA(3,1,0), no intercept** — identical to Model One with $\phi_0$ dropped.
3. **ARIMA(0,2,1):**
   $$y_t - 2y_{t-1} + y_{t-2} = \epsilon_t + \theta\epsilon_{t-1}$$
4. **ARIMA(3,2,2)** — an ARMA(3,2) applied to the twice-differenced series, no intercept.

**Two ways to fit Model One.** Differencing $y$ once and fitting an AR(3) can be done with
`AutoReg`, which estimates by OLS — equivalently, *conditional* maximum likelihood, conditioning on
the first few observations — or with `ARIMA(3,0,0)`, which uses the *full* likelihood. The two give
nearly the same slope coefficients but noticeably different intercepts (0.0021 vs 0.0041, roughly a
factor of two); despite that, their forecasts for the original series, obtained by cumulatively
summing forecast differences back onto the last observed $y$, are essentially identical.

**Getting the intercept right when differencing inside ARIMA.** Model One can also be fit directly
on $y$ (undifferenced) via `ARIMA(y, order=(3,1,0))`, but by default this drops the intercept — it
silently fits Model Two instead. Recovering Model One's intercept requires `trend='t'` (a linear
trend in the *level*, which becomes a constant after one differencing) rather than the default. With
that argument, the fitted coefficients and log-likelihood match the by-hand differenced fit exactly.

**Why the intercept matters.** Fit as Model Two — `ARIMA(y, order=(3,1,0))` with no trend argument —
the model has no constant term at all, and its forecasts diverge visibly and badly from the other
models': dropping $\phi_0$ is not a minor simplification here, since the differenced series has a
genuine nonzero mean (spending trends upward over time) that the model needs to be told about
explicitly.

**Models Three and Four** are fit directly with `ARIMA(y, order=(0,2,1))` and
`ARIMA(y, order=(3,2,2))`. Model Three's forecasts resemble Model One's reasonably closely. Model
Four's forecasts are essentially indistinguishable from Model One's, which is worth pausing on:
Model One is "AR(3) with intercept on the first difference" and Model Four is "ARMA(3,2) with no
intercept on the second difference" — different differencing orders, different AR and MA orders,
and no shared intercept — yet nearly the same predictions. The lab poses this as a question, *why
do they agree?*, and the only clue given here is Model Four's fitted coefficients: several of them
are individually far from significant (`ar.L1`, `ar.L2` and `ma.L2` all have $p>0.1$), suggesting
the extra differencing and extra MA terms are absorbing structure that a well-chosen AR(3)-plus-
intercept model already captures on its own. The reconciliation is not carried further in this
material.

## Comparing models with AIC and BIC

Model selection between the four uses the standard information criteria:
$$\mathrm{AIC} = -2\times(\text{maximised log-likelihood}) + 2\times(\text{number of parameters}),$$
$$\mathrm{BIC} = -2\times(\text{maximised log-likelihood}) + (\log n)\times(\text{number of parameters}),$$
with a lower value indicating a better trade-off between fit and complexity — AIC penalising each
extra parameter by $2$, BIC by $\log n$.

The one subtlety in applying these by hand is *which* $n$ to use. A model fit to a $d$-times-
differenced series only has $n-d$ genuine data points to fit, since $d$ observations are consumed
by differencing. Recomputing BIC with $\log(n-1)$ for the once-differenced Models One and Two, and
$\log(n-2)$ for the twice-differenced Models Three and Four, reproduces statsmodels' own `.aic` and
`.bic` attributes to full numerical precision for all four models — confirming that this is exactly
how statsmodels counts effective sample size internally.

Reading the four results together (rounded to one decimal place):

| Model | Parameters | AIC | BIC |
|---|---|---|---|
| One (AR(3) + intercept, $d=1$) | 5 | $-2364.5$ | $-2344.7$ |
| Two (AR(3), no intercept, $d=1$) | 4 | $-2354.9$ | $-2339.1$ |
| Three (ARIMA(0,2,1)) | 2 | $-2357.3$ | $-2349.4$ |
| Four (ARIMA(3,2,2)) | 6 | $-2356.3$ | $-2332.6$ |

AIC ranks Model One best — its extra parameters buy enough extra log-likelihood to be worth the
(smaller) AIC penalty. BIC, which penalises parameters more heavily once $n$ is large, instead
ranks the much sparser Model Three best, despite its lower likelihood than Model One's. This is the
usual tension between the two criteria showing up in a real fit: AIC is willing to pay for
parameters that improve the likelihood enough, while BIC is stricter and here prefers the
two-parameter model over the five-parameter one that AIC prefers.

## Sources

All material in this chapter comes from Lab 12, Berkeley STAT153, Spring 2025 (`Lab12.ipynb`, CC BY
4.0), converted to markdown:

- Causal AR(2) example and MA($\infty$) derivation — `01-introduction.md`.
- TTLCONS data, Models One through Four, and their fitting/forecasting code and statsmodels
  output — `02-ttlcons-total-construction-spending-data.md`.
- AIC/BIC formulas and their by-hand verification against `.aic`/`.bic` — `03-aic-and-bic.md`.

The lab refers to "Lecture 22" as where the four ARIMA models were first fit; that lecture itself is
not among the inputs for this chapter. Time-series plots referenced in the notebook (the raw data,
and the four models' forecasts) were omitted in the conversion and are not reproduced here.

---

[← 87. ACF and PACF in Practice](87-acf-and-pacf-in-practice.md) · [Contents](index.md) · [89. Change-of-Slope Regression and Scaling →](89-change-of-slope-regression-and-scaling.md)
