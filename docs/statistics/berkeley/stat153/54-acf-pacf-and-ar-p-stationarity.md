---
title: "54. ACF, PACF, and AR(p) Stationarity"
course: "Berkeley Stat 153"
chapter: 54
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 54. ACF, PACF, and AR(p) Stationarity

## What this covers

Two questions about fitted AR and MA models, worked through with real economic and geological data
rather than stated in the abstract. First: when is a fitted AR($p$) model *causal-stationary* — well
behaved enough that its forecasts settle down instead of exploding — and how does preprocessing a
trending series (logs, then differences) get you there. Second: given real data, how do you choose
the order $p$ of an AR($p$) model or $q$ of an MA($q$) model, using the sample autocorrelation
function (ACF) and the sample partial autocorrelation function (PACF). This assumes you already
know what an AR($p$) and an MA($q$) model are, and have seen them fit in `statsmodels`
(`AutoReg`, `ARIMA`).

## Causal stationarity of a fitted AR($p$) model

For an AR(1) model $y_t = c + \phi_1 y_{t-1} + \epsilon_t$, causal-stationarity holds exactly when
$|\phi_1| < 1$. For $p \geq 2$, the criterion is stated in terms of the **AR polynomial**

$$\phi(z) = 1 - \phi_1 z - \phi_2 z^2 - \cdots - \phi_p z^p,$$

built from the fitted coefficients. The AR($p$) model is causal-stationary exactly when *every*
root of $\phi(z)$ has modulus strictly larger than 1. For $p = 1$ this is the same $|\phi_1| < 1$
condition, since the single root of $1 - \phi_1 z$ is $z = 1/\phi_1$, which has modulus $> 1$
precisely when $|\phi_1| < 1$.

`AutoReg` reports the roots of the fitted AR polynomial (and their moduli) directly in its summary,
so checking this is a matter of reading off whether every modulus exceeds 1.

**Worked example.** Fitting AR(1) to raw quarterly GNP (FRED series GNP) gives $\hat\phi_1 =
1.0116$. Since $|\hat\phi_1| > 1$, this model is *not* causal-stationary. That is the expected
answer: GNP is a steadily growing series, so no stationary model should fit it well, and a model
with $\hat\phi_1 > 1$ produces forecasts that grow exponentially with the horizon — which is at
least consistent with the data even though the model itself is not stationary.

## Getting to a stationary series: logs and differences

If GNP itself won't support a stationary AR model, the fix is to preprocess it. Two steps:

1. **Take logarithms.** This tends to stabilize variance in a series whose fluctuations scale with
   its level.
2. **Take differences of the logarithms**, and multiply by 100. The quantity

$$100\big(\log \text{GNP}_t - \log \text{GNP}_{t-1}\big)$$

   is (approximately) the **percent change** in GNP from one quarter to the next — a standard trick,
   since $\log(1+x) \approx x$ for small $x$.

Fitting AR(1) to this log-differenced series gives $\hat\phi_1 = 0.2487$, with $|\hat\phi_1| < 1$:
this model *is* causal-stationary. Fitting AR(2) to the same percent-change series gives

$$y_t = 0.9181 + 0.1971\,y_{t-1} + 0.2077\,y_{t-2} + \epsilon_t,$$

whose AR polynomial has roots with moduli $1.7704$ and $2.7192$ — both strictly greater than 1, so
this AR(2) model is also causal-stationary.

## A subtlety: stationarity is a property of the model *and* the series

The AR(1) fitted to the percent-change series can be rewritten as a model for the *level* series
$G_t := 100\log\text{GNP}_t$, and the rewritten model is not stationary — which is worth working
through once, because it shows that "is this AR($p$) equation stationary" is not a free-standing
question about the coefficients alone.

Write $y_t = G_t - G_{t-1}$. The fitted AR(1) model $y_t = 1.1596 + 0.2487\,y_{t-1} + \epsilon_t$
becomes, substituting $y_{t-1} = G_{t-1} - G_{t-2}$:

$$G_t - G_{t-1} = 1.1596 + 0.2487\,(G_{t-1} - G_{t-2}) + \epsilon_t,$$

which rearranges to an AR(2) model for the level series itself:

$$G_t = 1.1596 + 1.2487\,G_{t-1} - 0.2487\,G_{t-2} + \epsilon_t.$$

Checking causal-stationarity means finding the roots of the corresponding AR polynomial, computed
in the lecture as $1 - 1.1487z - 0.2487z^2$, whose roots are $-5.3679$ and $0.74907$ — moduli
$5.3679$ and $0.74907$. One root has modulus above 1, the other below, so **this AR(2) model for
$G_t$ is not causal-stationary**, even though it was built out of a perfectly good stationary AR(1)
model for the differenced series. That makes sense: $G_t$ is (up to scaling) $\log\text{GNP}_t$,
"predominantly an increasing dataset," so no stationary model should be expected to fit it — the
stationarity lived in the *differenced* series, not in the level series that the differences came
from.

<figure>
<svg viewBox="0 0 420 220" role="img" aria-label="Roots of two fitted AR(2) polynomials placed relative to the unit circle in the complex plane">
  <circle cx="105" cy="110" r="50" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
  <circle cx="315" cy="110" r="50" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
  <line x1="20" y1="110" x2="190" y2="110" stroke="currentColor" stroke-width="0.6" opacity="0.5"/>
  <line x1="230" y1="110" x2="400" y2="110" stroke="currentColor" stroke-width="0.6" opacity="0.5"/>
  <text x="105" y="30" text-anchor="middle" font-size="12" fill="currentColor">AR(2) for level $G_t$</text>
  <text x="315" y="30" text-anchor="middle" font-size="12" fill="currentColor">AR(2) for change $y_t$</text>
  <circle cx="142" cy="110" r="4" fill="currentColor"/>
  <text x="142" y="132" text-anchor="middle" font-size="11" fill="currentColor">0.749</text>
  <circle cx="177" cy="110" r="4" fill="currentColor"/>
  <text x="177" y="132" text-anchor="middle" font-size="11" fill="currentColor">5.37</text>
  <circle cx="380" cy="110" r="4" fill="currentColor"/>
  <text x="380" y="132" text-anchor="middle" font-size="11" fill="currentColor">1.77</text>
  <circle cx="250" cy="110" r="4" fill="currentColor"/>
  <text x="250" y="132" text-anchor="middle" font-size="11" fill="currentColor">2.72</text>
  <text x="105" y="195" text-anchor="middle" font-size="12" fill="currentColor">one root inside — not stationary</text>
  <text x="315" y="195" text-anchor="middle" font-size="12" fill="currentColor">both roots outside — stationary</text>
</svg>
<figcaption>Roots of the fitted AR(2) polynomial for two representations of the same GNP data,
positioned schematically by whether their modulus is below or above 1 (dashed circle marks modulus
1; labels give the exact computed modulus, not to scale). Left: AR(2) fitted directly to the log
GNP level $G_t$ has one root inside the unit circle, so it is not causal-stationary — consistent
with $G_t$ being a trending series. Right: AR(2) fitted to the quarterly percent-change series
$y_t$ has both roots outside, so it is causal-stationary.</figcaption>
</figure>

## Choosing the order of an AR($p$) model: the sample PACF

Once you know how to check whether a *given* order is stationary, the remaining question is which
order to fit in the first place. The tool is the **sample partial autocorrelation function**:

$$\text{PACF}(h) := \text{the estimated coefficient } \hat\phi_h \text{ obtained by fitting an AR}(h) \text{ model to the data.}$$

That is, PACF(1) is $\hat\phi_1$ from fitting AR(1); PACF(2) is $\hat\phi_2$ from fitting AR(2)
(not the $\hat\phi_1$ from that same fit); and so on. The rule for choosing the order: compute
PACF($h$) for $h = 1, 2, 3, \dots$, and if the values become negligible after some $h = p$, use $p$
as the AR order.

Applied to the percent-change GNP series (up to $h_{\max} = 50$), PACF(1) $= 0.2487$ and PACF(2)
$= 0.2077$ stand out, while the values from $h = 3$ onward are small by comparison (a handful of
larger-looking values do turn up further out, e.g. around $h = 25$ or $h = 47$, but these are
scattered rather than a persisting pattern). On that basis, $p = 3$ is judged a reasonable order for
this series. `statsmodels`' built-in `pacf` function (with `method='ols'`) reproduces the same
values exactly, and its `plot_pacf` draws the same numbers with a shaded band for judging
negligibility, plus the (trivial) value $1$ plotted at lag 0.

## The sample ACF, and choosing the order of an MA($q$) model

The **sample autocorrelation function** plays the same role for MA($q$) models that the PACF plays
for AR($p$). Given data $y_1, \dots, y_n$ and a lag $h$, define

$$r_h := \frac{\sum_{t=1}^{n-h} (y_t - \bar y)(y_{t+h} - \bar y)}{\sum_{t=1}^n (y_t - \bar y)^2}, \qquad h = 0, 1, 2, \dots$$

with $\bar y$ the sample mean. By construction $r_0 = 1$ always, so the informative values start at
$h \geq 1$.

**Why this diagnoses MA order.** Simulating $n = 600$ points of Gaussian white noise and comparing
it to a simulated MA(1) series $y_t = \epsilon_t + \theta \epsilon_{t-1}$ makes the visual and ACF
signatures concrete:

- White noise: no visible structure, and the sample ACF is negligible at every lag $h \geq 1$.
- MA(1) with $\theta = 0.8$: the series looks smoother than white noise (positive lag-1
  correlation), and the sample ACF has a clear spike at lag 1, with the rest negligible.
- MA(1) with $\theta = -0.8$: the series looks more wiggly than white noise (negative lag-1
  correlation), again with a single spike — this time negative — at lag 1.

Fitting MA(1) to the $\theta = 0.8$ simulated series (via `ARIMA(..., order=(0,0,1))`, where the
general $(p, d, q)$ notation names an ARMA($p,q$) model after $d$ rounds of differencing) recovers
$\hat\theta = 0.8212$, $\hat\mu = -0.0272$, $\hat\sigma = 0.9732$ — all close to the true values
$0.8$, $0$, $1$ used to generate the data, which is the check that the ACF-based order choice and
the fitting procedure are doing what they should.

**Two real-data examples, same method.**

- *Glacial varve thickness* (Shumway & Stoffer, Example 2.6 in the 4th edition): yearly thickness of
  sedimentary deposits from melting glaciers, 634 years of data. The raw series does not have
  constant mean even after taking logs, so it is differenced; the sample ACF of the differenced log
  series shows exactly one non-negligible spike, negative, at lag 1. Fitting MA(1) to this
  differenced series gives $\hat\theta = -0.7710$.
- *GDP growth rate* (FRED series A191RP1Q027SBEA — the percent change in GDP from the preceding
  quarter, already the log-differenced-and-scaled form of raw GDP): the sample ACF shows two
  non-negligible spikes, at lags 1 and 2. Fitting MA(2) (`order=(0,0,2)`) gives $\hat\theta_1 =
  0.1927$, $\hat\theta_2 = 0.2267$.

In both cases the order is read off the same way: compute the sample ACF, and take $q$ to be the
lag after which the spikes stop.

## Sources

- Causal stationarity of AR($p$), the AR polynomial criterion, the raw-GNP AR(1) example, the
  logs-and-differences preprocessing, and the level-vs-difference AR(2) subtlety: Berkeley Stat 153,
  Fall 2025, `CodeLectureTwenty153248Fall2025` notebook —
  `01-ar-p-models-and-stationarity.md`
  and
  `02-preprocessing-using-logarithms-and-differences.md`.
  GNP data cited there to FRED, <https://fred.stlouisfed.org/series/GNP>.
- PACF definition and its use to choose the AR order for the percent-change GNP series: same
  notebook,
  `03-how-to-determine-the-order-of-for-ar-p.md`.
- Sample ACF definition, the white-noise-vs-MA(1) simulation ($\theta = \pm 0.8$) and its fitted
  recovery: Berkeley Stat 153, Spring 2025, `CodeLectureTwenty153248Spring2025` notebook —
  `01-introduction.md` and
  `02-sample-acf.md`.
- Varve dataset and GDP growth rate examples: same notebook,
  `03-varve-dataset.md` and
  `04-gdp-growth-rate-data.md`.
  Varve data referred to Shumway & Stoffer, *Time Series Analysis and Its Applications*, 4th
  edition, Example 2.6 (not itself supplied here). GDP growth rate series cited to FRED,
  <https://fred.stlouisfed.org/series/A191RP1Q027SBEA>.
- All figures in the original notebooks were omitted in conversion; the root diagram above is
  redrawn from the numeric roots reported in the fitted-model summaries, not a reproduction of a
  lecture image.

---

[← 53. Bayesian Regularization of Trends](53-bayesian-regularization-of-trends.md) · [Contents](index.md) · [55. Nonlinear Autoregression and Overfitting →](55-nonlinear-autoregression-and-overfitting.md)
