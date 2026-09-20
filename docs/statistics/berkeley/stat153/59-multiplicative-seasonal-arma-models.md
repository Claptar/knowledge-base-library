---
title: "59. Multiplicative Seasonal ARMA Models"
course: "Berkeley Stat 153 Fall 2024"
chapter: 59
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 59. Multiplicative Seasonal ARMA Models

## What this covers

Ordinary ARMA models are built to describe short-range dependence: an observation is correlated
with the last few observations, and the correlation dies off. Monthly data with a strong yearly
cycle breaks that picture — an observation is *also* correlated with the observation twelve months
back, and with the ones near it. This chapter asks: how do you model that second kind of dependence
without simply throwing a huge number of extra parameters at the problem? The answer is the
seasonal and multiplicative seasonal ARMA model, motivated here by a real dataset (monthly CO$_2$
levels) and then applied, with varying degrees of success, to three more.

It assumes you already know how to read the ACF and PACF of an ordinary ARMA($p,q$) process, know
what differencing a series means and why it is used to reach stationarity, know the backshift
operator ($By_t = y_{t-1}$, so $B^sy_t = y_{t-s}$), and have seen `statsmodels`' `ARIMA` class used
to fit and forecast a model.

## Recap: what the ACF and PACF tell you

Three facts about the theoretical ACF and PACF of an ARMA($p,q$) process do essentially all the
work of guessing an order from a plot, and are worth restating because the rest of the chapter
leans on them repeatedly:

- For MA($q$), the ACF is exactly zero beyond lag $q$.
- For AR($p$), the PACF is exactly zero beyond lag $p$.
- For a genuine mixed ARMA($p,q$) with $p,q \geq 1$, *neither* the ACF nor the PACF cuts off at a
  finite lag. Guessing $p$ and $q$ from the plots alone is then hard.

One more thing worth holding in mind before looking at real data: the *sample* ACF and PACF
(computed from a finite simulated or observed series) look like noisier versions of the
*theoretical* ones. A model can be very easy to spot from its population ACF/PACF and considerably
harder to spot from four hundred simulated points of it.

## The CO$_2$ dataset: why a plain ARMA model will not do

The motivating dataset is monthly CO$_2$ levels measured in Alert, Canada, January 1994 to
December 2004 (132 observations), from the R package `TSA` that accompanies Cryer and Chan's *Time
Series Analysis with Applications in R*. The raw series both drifts upward (accumulating CO$_2$)
and swings within each year — an obvious seasonal pattern on top of a trend.

To get to something closer to stationary, first take a **seasonal difference** with period
$s = 12$,
$$\nabla_s y_t = y_t - y_{t-s},$$
comparing each month to the same month a year earlier. This removes the yearly cycle but the plot
of $\nabla_s y_t$ still drifts, so a second, **ordinary** difference is taken on top of it,
$\nabla \nabla_s y_t$.

The sample ACF and PACF of this twice-differenced series show a large negative spike at lag 1,
then a run of small, negligible autocorrelations, followed by non-negligible spikes again at lags
11, 12 and 13. Read literally with an ordinary MA($q$) model, this calls for $q = 13$ — an MA(13)
has thirteen free moving-average coefficients, almost all of which the data is saying should be
close to zero. What is wanted is a model with only two or three parameters whose ACF has exactly
this shape: a spike near lag 1, silence in between, and another cluster of spikes near lag 12. That
model is the multiplicative seasonal ARMA model, and reaching it takes two steps.

## Seasonal ARMA models

A **seasonal ARMA model** with period $s$ is
$$\phi(B^s)(y_t - \mu) = \theta(B^s)\epsilon_t,$$
i.e. an ordinary ARMA model written in powers of $B^s$ rather than $B$. Expanded out, this is a
special case of a regular ARMA model whose AR and MA coefficients are mostly zero, nonzero only at
multiples of $s$. For instance, the seasonal MA(1) model with period $s = 4$ is
$$y_t = \mu + \epsilon_t + \theta\epsilon_{t-4},$$
which is exactly a regular MA(4) model with $\theta_1 = \theta_2 = \theta_3 = 0$ and $\theta_4 =
\theta$.

Because almost all the coefficients are zero, the ACF and PACF of a seasonal ARMA model are
themselves zero except at the seasonal lags $h = 0, s, 2s, 3s, \dots$ — and *at* those lags they
equal exactly the ACF/PACF of the corresponding non-seasonal ARMA model. A seasonal AR(1) with
period 12 has a PACF that looks like an ordinary AR(1)'s PACF, but stretched out so its one nonzero
value sits at lag 12 instead of lag 1.

## Multiplicative seasonal ARMA models

A **multiplicative seasonal ARMA model**, written $ARMA(p,q)\times(P,Q)_s$, multiplies a regular
ARMA polynomial by a seasonal one:
$$\phi(B)\Phi(B^s)(y_t - \mu) = \theta(B)\Theta(B^s)\epsilon_t.$$
This captures short-range (month-to-month) dependence and a separate seasonal (year-to-year)
dependence at the same time, with only $p + q + P + Q$ parameters, even though multiplying the two
polynomials out produces a "regular" ARMA with many more nonzero coefficients than that.

Reading $p,q,P,Q$ off the ACF and PACF of such a process is harder than for a plain ARMA, because
the product of the two polynomials creates cross terms at lags that are neither purely seasonal nor
purely regular (exactly the lags 11 and 13 flanking the seasonal lag 12 in the CO$_2$ example
above). The lecture's heuristic strategy is to look at the two lag ranges separately:

1. Look at the ACF and PACF **only at the seasonal lags** $h = 0, s, 2s, 3s, \dots$, and apply the
   usual cutoff rule there to guess the seasonal orders $P$ and $Q$: if $ACF(hs)$ looks negligible
   for $h > Q$, the seasonal part could be MA($Q$); if $PACF(hs)$ looks negligible for $h > P$, the
   seasonal part could be AR($P$).
2. Then look **only at the first few non-seasonal lags** $h = 0, 1, \dots, s-1$, and apply the same
   rule to guess the regular orders $p$ and $q$.

It is a heuristic, not an exact recipe — the cross terms mean it can mislead — but it correctly
identifies the model in each of the four theoretical examples worked through in the lecture, all
simulated with period $s = 12$:

| Model | Parameters | What the seasonal lags (12, 24, …) show | What the small lags (1, 2, …) show |
| --- | --- | --- | --- |
| $MA(1)\times MA(1)_{12}$ | $\theta=-0.8,\ \Theta=0.7$ | one ACF spike, at 12 | one ACF spike, at 1 |
| $MA(1)\times AR(1)_{12}$ | $\theta=0.8,\ \phi=0.8$ | one PACF spike, at 12 | one ACF spike, at 1 |
| $MA(2)\times AR(1)_{12}$ | $\theta_1=0.8,\theta_2=0.6,\ \phi=0.8$ | one PACF spike, at 12 | two ACF spikes |
| $AR(1)\times AR(1)_{12}$ | $\phi=-0.8,\ \Phi=0.7$ | one PACF spike, at 12 | one PACF spike, at 1 |

The first row is worth working out explicitly, because it is exactly the shape the CO$_2$ data
showed. $MA(1)\times MA(1)_{12}$ means
$$y_t = \mu + \epsilon_t + \theta\epsilon_{t-1} + \Theta\epsilon_{t-12} + \theta\Theta\epsilon_{t-13},$$
an MA(13) with nonzero coefficients only at lags $0, 1, 12, 13$. Its autocorrelation can only be
nonzero at differences between members of $\{0,1,12,13\}$, i.e. at $h \in \{0, 1, 11, 12, 13\}$ —
nowhere else. Plugging in $\theta=-0.8,\ \Theta=0.7$ gives
$\rho(1)\approx-0.49$, $\rho(11)\approx-0.23$, $\rho(12)\approx0.47$, $\rho(13)\approx-0.23$, and
$\rho(h)=0$ for every other $h$:

<figure>
<svg viewBox="0 0 420 220" role="img" aria-label="Theoretical ACF of a multiplicative MA(1) times seasonal MA(1) model, showing spikes clustered near lag 1 and near the seasonal lag 12, with nothing in between">
  <line x1="30" y1="140" x2="390" y2="140" stroke="currentColor" stroke-width="1.5"/>
  <line x1="328" y1="40" x2="328" y2="140" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <text x="328" y="30" text-anchor="middle" font-size="12" fill="currentColor">seasonal period s = 12</text>
  <line x1="40" y1="140" x2="40" y2="70" stroke="currentColor" stroke-width="2.5"/>
  <circle cx="40" cy="70" r="3.5" fill="currentColor"/>
  <line x1="64" y1="140" x2="64" y2="174" stroke="currentColor" stroke-width="2.5"/>
  <circle cx="64" cy="174" r="3.5" fill="currentColor"/>
  <text x="150" y="132" text-anchor="middle" font-size="12" fill="currentColor">rho(h) approx 0 for h = 2, ..., 10</text>
  <line x1="304" y1="140" x2="304" y2="156" stroke="currentColor" stroke-width="2.5"/>
  <circle cx="304" cy="156" r="3.5" fill="currentColor"/>
  <line x1="328" y1="140" x2="328" y2="107" stroke="currentColor" stroke-width="2.5"/>
  <circle cx="328" cy="107" r="3.5" fill="currentColor"/>
  <line x1="352" y1="140" x2="352" y2="156" stroke="currentColor" stroke-width="2.5"/>
  <circle cx="352" cy="156" r="3.5" fill="currentColor"/>
  <text x="40" y="195" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <text x="64" y="195" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="304" y="195" text-anchor="middle" font-size="12" fill="currentColor">11</text>
  <text x="328" y="195" text-anchor="middle" font-size="12" fill="currentColor">12</text>
  <text x="352" y="195" text-anchor="middle" font-size="12" fill="currentColor">13</text>
  <text x="395" y="144" text-anchor="end" font-size="12" fill="currentColor">h</text>
</svg>
<figcaption>Theoretical ACF of MA(1) x MA(1)<sub>12</sub> with theta = -0.8, Theta = 0.7. The
nonzero autocorrelations cluster near the regular lag 1 and near the seasonal lag 12 (with small
side lobes at 11 and 13 from the product of the two polynomials) and vanish everywhere else — the
same shape the twice-differenced CO2 series' sample ACF showed, produced here with only two
parameters instead of the thirteen an unstructured MA(13) would need.</figcaption>
</figure>

The lecture is explicit that this heuristic gets noticeably harder once you replace the theoretical
ACF/PACF with the sample ACF/PACF of *simulated* data from these same four models: the same
qualitative pattern is there, but it is considerably harder to read off by eye through the extra
noise.

## Fitting a SARIMA model to the CO$_2$ data

The pattern found earlier for the CO$_2$ data — spike at lag 1, spikes at 11–12–13 — is exactly the
$MA(1)\times MA(1)_{12}$ signature just derived. In `statsmodels`' notation this is written as the
full SARIMA model $ARIMA(0,1,1)\times(0,1,1,12)$: the middle entry of each triple ($d=1$, $D=1$)
tells the `ARIMA` class to do the ordinary and seasonal differencing itself, so it can be handed the
raw (undifferenced) series directly:

```python
m1_co2 = ARIMA(y, order=(0, 1, 1), seasonal_order=(0, 1, 1, 12)).fit()
```

The fit gives $\hat\theta = -0.579$ (`ma.L1`), $\hat\Theta = -0.821$ (`ma.S.L12`), and
$\hat\sigma^2 = 0.545$. The Ljung–Box test on the residuals has $p \approx 0.94$, i.e. no evidence
of leftover autocorrelation — the two-parameter seasonal model has absorbed what an MA(13) would
otherwise have needed thirteen coefficients to describe. Forecasts (via `get_prediction`) extend
the rising, seasonally-wiggling series forward in the obvious way.

## Choosing a SARIMA model when the ACF and PACF are not so clean

The heuristic above works when the ACF/PACF has an unambiguous, low-order signature. Real data is
often messier, and the lecture demonstrates two fallbacks, applied to three further datasets.

**Guess a couple of plausible candidates and compare.** If the differenced ACF/PACF is ambiguous
between, say, an MA(1)-flavoured and an AR(1)-flavoured seasonal structure, fit both simple
candidates and see whether their forecasts agree.

**Brute-force search over $(p,d,q)\times(P,D,Q)_s$.** Loop over a grid of small orders (the lecture
uses $p,q \in \{0,1,2\}$, $d\in\{0,1\}$, $P,Q\in\{0,1,2\}$, $D=1$ fixed), fit each combination, and
keep whichever minimizes AIC and whichever minimizes BIC. Because BIC penalizes extra parameters
more heavily than AIC, the two criteria do not have to agree, and neither has to agree with the
model a human would have guessed from the plot.

### Airline passengers (monthly international air travel, 1949–1960)

As is routine whenever a series is positive and its seasonal swings grow with its level, the model
is fit to $\log y_t$ rather than $y_t$. After a seasonal and then a regular difference, the ACF/PACF
suggest two simple rival candidates, $MA(1)\times MA(1)_{12}$ and $AR(1)\times AR(1)_{12}$, i.e.
$ARIMA(0,1,1)\times(0,1,1,12)$ and $ARIMA(1,1,0)\times(1,1,0,12)$ on $\log y$:

| Model | Estimates | AIC |
| --- | --- | --- |
| $MA(1)\times MA(1)_{12}$ | $\hat\theta=-0.402,\ \hat\Theta=-0.557$ | $-483.4$ |
| $AR(1)\times AR(1)_{12}$ | $\hat\phi=-0.375,\ \hat\Phi=-0.464$ | $-474.8$ |

Their forecasts, on both the log scale and after exponentiating back to passenger counts, are
close to one another. A brute-force grid search over the full $(p,d,q)\times(P,D,Q)_{12}$ range
finds the AIC-best model to be $ARIMA(1,0,1)\times(1,1,2)_{12}$ and the BIC-best model to be
$ARIMA(0,1,1)\times(0,1,1,12)$ — the same $MA(1)\times MA(1)_{12}$ model guessed by hand (BIC's
heavier penalty on extra parameters favours the simpler match here). Forecasts from all three
models agree closely, especially in the near term.

### Retail sales of beer, wine and liquor (FRED series `MRTSSM4453USN`)

Here the sample ACF/PACF of the seasonally-and-regularly-differenced log series gives no clean
signature, so the analysis goes straight to the grid search. It picks $ARIMA(2,1,0)\times(2,1,2)_{12}$
by AIC and the more parsimonious $ARIMA(2,1,0)\times(0,1,2)_{12}$ by BIC; the two models' forecasts
agree well over a ten-year horizon. It is worth noting that a version of the same analysis run
*without* first taking logs of this series ran into repeated convergence failures during the grid
search (several candidate models failed to fit, and several others produced convergence warnings),
while the logged version fit cleanly across the whole grid — a concrete illustration of why fitting
to logarithms is the routine first step for a positive series with growing seasonal swings, rather
than a decoration.

### FRED industrial production index (monthly since 1919, 1280 observations)

An older version of this series is analyzed as Example 3.46 in Shumway and Stoffer. On the raw
series, the grid search picks $ARIMA(1,0,2)\times(1,1,2)_{12}$ by AIC and
$ARIMA(0,1,1)\times(0,1,1)_{12}$ by BIC; their forecasts are close in the near term and diverge
further out. Repeating the entire search after taking logs gives a *different* pair of winners,
$ARIMA(1,0,2)\times(0,1,2)_{12}$ (AIC) and $ARIMA(2,0,0)\times(0,1,1)_{12}$ (BIC) — and this time the
AIC-best and BIC-best forecasts disagree with each other more sharply than the corresponding pair
did on the raw scale. The lesson drawn in the lecture is that "the best model by AIC" is a property
of a particular transformation of the data, not an absolute statement about the series, and that
AIC and BIC need not agree — nor does that disagreement need to look the same on every scale.

## Estimating the parameters of an MA(1) model

As a coda, the lecture turns from choosing a model's order to the separate question of how software
actually estimates a model's coefficients. Parameter estimation for ARMA, ARIMA and SARIMA models
in general is harder than for pure AR models (which reduce to ordinary least squares) and is not
covered in detail — the course simply relies on `ARIMA(...).fit()`. But the MA(1) case is done by
hand, both to see the idea and to check the black box against it.

For $y_t = \mu + \epsilon_t + \theta\epsilon_{t-1}$, inverting the recursion expresses each
$\epsilon_t$ in terms of $y_1,\dots,y_t$, and the sum of squared implied innovations is
$$
S(\mu,\theta) = \left(y_1 - \tfrac{\mu}{1+\theta}\right)^2
+ \left(y_2 - \tfrac{\mu}{1+\theta} - \theta y_1\right)^2
+ \left(y_3 - \tfrac{\mu}{1+\theta} - \theta y_2 + \theta^2 y_1\right)^2
+ \cdots
$$
with the general term $\left(y_t - \tfrac{\mu}{1+\theta} - \theta y_{t-1} + \theta^2 y_{t-2} -
\cdots + (-1)^{t-1}\theta^{t-1}y_1\right)^2$. In code this is evaluated by the recursion $s_1 = y_1$,
$s_t = y_t - \theta s_{t-1}$, and then $S(\mu,\theta) = \sum_t \left(s_t - \tfrac{\mu}{1+\theta}\right)^2$,
minimized numerically (`scipy.optimize.minimize`, started from $\theta=0$ and $\mu$ at the sample
mean).

Two checks against `ARIMA(...).fit()` are given:

- **Simulated MA(1)**, true $\theta=-0.7$, $n=400$: least squares gives $\hat\mu=-0.004$,
  $\hat\theta=-0.747$, matching `ARIMA`'s $-0.003$ and $-0.746$ closely.
- **The (undifferenced-then-twice-differenced) alcohol sales series**, $n=383$: least squares gives
  $\hat\theta=-0.570$ against `ARIMA`'s $-0.570$ — the $\theta$ estimates agree well, though the
  lecture notes that the $\hat\mu$ estimate here (0.039 by least squares versus 0.171 from `ARIMA`)
  is "slightly off."

Standard errors for $\hat\mu,\hat\theta$ are obtained from the Hessian of $S$ at the minimum
(computed numerically, via `numdifftools`), using $\widehat{\mathrm{Var}} \approx
\hat\sigma^2(H/2)^{-1}$ with $\hat\sigma^2 = S(\hat\mu,\hat\theta)/(n-2)$; in both checks these come
out close to the standard errors `ARIMA` reports directly. The lecture attributes the standard-error
formula itself to "the notes for Lecture 23" — a written source referred to but not reproduced in
this material.

## Sources

- Berkeley STAT 153, fall 2025, `CodeLectureTwentyThree153248Fall2025.ipynb` — the core material
  (ACF/PACF recap is absent here; the lecture opens directly with the CO2 motivation):
  `01-co2-dataset-motivation-for-multiplicative-seasonal-arma-mode.md`,
  `02-seasonal-arma-models.md`, `03-multiplicative-seasonal-arma-models.md`,
  `04-back-to-co2-dataset.md`; and the extra worked examples,
  `05-airline-passengers-dataset.md` (airline passengers, and the log-transformed retail alcohol
  sales analysis embedded in the same file) and `06-fred-industrial-production-dataset.md`
  (industrial production index, raw and logged).
- Berkeley STAT 153, spring 2025, `CodeLectureTwentyThree153248Spring2025.ipynb` — the same core
  material (`02` through `05`, matching fall's `01` through `04` almost line for line, confirming
  it as one recurring lecture), plus `01-acf-and-pacf-of-arma-processes.md` (the ACF/PACF recap
  used above) and `06-ma-1-parameter-estimation.md` (the least-squares MA(1) section). Spring's own
  retail alcohol sales analysis, embedded in `05-back-to-co2-dataset.md`, was run without a log
  transform and is the source of the convergence-failure contrast noted above.
- Figures throughout both notebooks (time series plots, ACF/PACF plots, simulated-data plots,
  forecast plots) were omitted in conversion to markdown and are not reproduced here; where a
  figure's content is described, it is paraphrased from the surrounding text, except for the ACF
  diagram above, which is computed directly from the stated model parameters.
- The standard-error formula used for the MA(1) least-squares estimates is attributed by the
  lecture to "the notes for Lecture 23," a written source not included in the supplied material.
- Shumway and Stoffer's *Time Series Analysis and Its Examples* (Example 3.46, referenced for the
  industrial production index) and Cryer and Chan's *Time Series Analysis with Applications in R*
  (source of the `TSA` package and the CO2 dataset) are named by the lecture but not themselves
  supplied.

---

[← 58. LSTM Networks for Forecasting](58-lstm-networks-for-forecasting.md) · [Contents](index.md) · [60. ARMA and ARIMA Model Identification →](60-arma-and-arima-model-identification.md)
