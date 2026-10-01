---
title: "27. AR Fitting: AutoReg vs ARIMA"
course: "Berkeley Stat 153"
chapter: 27
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 27. AR Fitting: AutoReg vs ARIMA

## What this covers

This chapter works through two practical questions that arise once you already know which AR or
ARIMA model you want and have to actually fit it in `statsmodels`: which of the two available
routines — `AutoReg` or `ARIMA` — to use, and what changes if you let `ARIMA`'s built-in
differencing order $d$ do the differencing rather than differencing the series yourself first. It
assumes the AR($p$) model, the stationarity (causality) condition on the AR coefficients, maximum
likelihood estimation, and ACF/PACF-based model identification from earlier lectures. Two datasets
carry the argument: quarterly GNP, used to fit and compare AR(1) two ways, and monthly total
construction spending (TTLCONS), used to build and compare several ARIMA specifications chosen from
ACF/PACF plots.

## AutoReg and ARIMA fit the same model differently

`statsmodels` has two routines for fitting an autoregression: `AutoReg`, and `ARIMA` called with a
$(p, d, q) = (p, 0, 0)$ order. Fit to the same AR(1) series — the percent change in log GNP,
$100 \times \Delta \log(\text{GNP}_t)$ — they do not return the same numbers, and the reason is that
they solve two different optimization problems.

**`AutoReg` uses conditional MLE.** It maximizes the likelihood of $y_2, \dots, y_n$ *conditional
on* $y_1$, parametrized by the intercept $\phi_0$ and the AR coefficient $\phi_1$:

$$
\left(\frac{1}{\sqrt{2\pi}\,\sigma}\right)^{n-1}
\exp\left(-\frac{1}{2\sigma^2}\sum_{t=2}^n (y_t - \phi_0 - \phi_1 y_{t-1})^2\right).
$$

This is just the density of $n-1$ Gaussian residuals from the regression of $y_t$ on $y_{t-1}$, so
maximizing it is ordinary least squares. On the GNP data, `AutoReg(ylogdiff, lags=1).fit()` gives
$\hat\phi_0 = 1.1596$, $\hat\phi_1 = 0.2487$, $\hat\sigma^2 = 1.5597$.

**`ARIMA` uses the full likelihood**, and parametrizes the AR(1) model around its mean instead of
its intercept:

$$
y_t - \mu = \phi_1(y_{t-1} - \mu) + \epsilon_t, \qquad \mu = \frac{\phi_0}{1-\phi_1}.
$$

There is no $\phi_0$ in this parametrization — it has been absorbed into $\mu$ — so comparing the
two fits means converting AutoReg's $(\phi_0, \phi_1)$ into $\mu = \phi_0/(1-\phi_1)$ first. Doing
that conversion and lining the two fits up side by side:

| | AutoReg, converted to $(\mu, \phi_1, \sigma^2)$ | ARIMA |
|---|---|---|
| $\mu$ | 1.5434 | 1.5415 |
| $\phi_1$ | 0.2487 | 0.2480 |
| $\sigma^2$ | 1.5597 | 1.5551 |

Close, but not equal — the two routines are genuinely maximizing different functions of the data.

## Conditional likelihood versus full likelihood

The full likelihood that `ARIMA` maximizes is the conditional likelihood above multiplied by the
*marginal* density of $y_1$ under the stationary AR(1) distribution:

$$
\frac{\sqrt{1-\phi_1^2}}{\sqrt{2\pi}\,\sigma}
\exp\left(-\frac{1-\phi_1^2}{2\sigma^2}(y_1-\mu)^2\right)
\left(\frac{1}{\sqrt{2\pi}\,\sigma}\right)^{n-1}
\exp\left(-\frac{1}{2\sigma^2}\sum_{t=2}^n\big((y_t-\mu)-\phi_1(y_{t-1}-\mu)\big)^2\right).
$$

The first factor is the extra piece: it uses the fact that a stationary AR(1) has
$y_1 \sim N\!\big(\mu, \sigma^2/(1-\phi_1^2)\big)$, whereas the conditional likelihood simply treats
$y_1$ as given and says nothing about where it came from. That single extra factor is the entire
difference between the two estimation methods.

Coding up this full log-likelihood directly and maximizing it numerically, starting from AutoReg's
estimates, reproduces `ARIMA`'s numbers almost exactly:

| | AutoReg | ARIMA | custom optimizer on the full likelihood |
|---|---|---|---|
| $\mu$ | 1.5434 | 1.5415 | 1.5415 |
| $\phi_1$ | 0.2487 | 0.2480 | 0.2480 |
| $\sigma^2$ | 1.5597 | 1.5551 | 1.5551 |
| log-likelihood | $-513.263$ | $-513.262$ | $-513.262$ |

This confirms the diagnosis: `ARIMA`'s estimates are not a different algorithm's approximation to
the same target, they are the exact maximizer of a different, well-defined function — the full
likelihood rather than the conditional one — and a general-purpose optimizer finds the same point.

## Stationarity: enforced by one routine, not the other

A second difference: when searching for the maximizer, `ARIMA` restricts the search to the causal
stationary region ($|\phi_1| < 1$ for AR(1)), while `AutoReg` places no such restriction. Fitting
AR(1) to the *raw*, undifferenced, unlogged GNP series — a series that is visibly trending, not
stationary — makes the difference concrete:

- `AutoReg` returns $\hat\phi_1 = 1.0116$, slightly *above* 1.
- `ARIMA` returns $\hat\phi_1 = 0.9999$, just *below* 1, and warns that "non-stationary starting
  autoregressive parameters" were found and replaced with zeros before it would proceed.

`ARIMA`'s bounded search is visible directly in code as the constraint passed to the optimizer:
`bounds = [(-np.inf, np.inf), (-0.99, 0.99), (1e-6, np.inf)]` — the middle bound on $\phi_1$ is what
keeps the search inside the stationary region.

## Differencing built into the model costs you the intercept

`ARIMA`'s order triplet $(p, d, q)$ lets you difference *inside* the model instead of differencing
the series yourself beforehand: $p$ is the AR order, $q$ the MA order, and $d$ the number of times
the series is differenced before the ARMA($p,q$) structure is applied to what remains. Fitting
`ARIMA(ylog*100, order=(1,1,0))` is mechanically almost the same as fitting `ARIMA(ylogdiff,
order=(1,0,0))`, since `ylogdiff` already is the once-differenced series — but not quite, because
whenever $d \geq 1$, `ARIMA` fits the model with **no intercept**:

$$
100\big(\log y_t - \log y_{t-1}\big) = \phi_1 \cdot 100\big(\log y_{t-1} - \log y_{t-2}\big) + \epsilon_t.
$$

There is no $\mu$ here at all, whereas the $(1,0,0)$ fit on `ylogdiff` estimated $\mu = 1.5415$ — a
nonzero average percent change per quarter. To get from a forecast on the differenced scale back to
a forecast on the level ($\log$ GNP) scale, you have to undo the differencing by hand: the
predicted differences $\widehat{y_{n+1}-y_n}, \widehat{y_{n+2}-y_{n+1}}, \dots$ are accumulated as a
telescoping sum on top of the last observed value,

```python
fcast_1[0] = last_observed_ylog + fcast_diff_1[0]
for i in range(1, k):
    fcast_1[i] = fcast_1[i-1] + fcast_diff_1[i]
```

Doing this with the intercept-carrying $(1,0,0)$ fit on `ylogdiff`, versus fitting $(1,1,0)$
directly on `ylog` with $d=1$ and no intercept, gives visibly different forecasts: the first keeps
drifting upward at roughly the historical average growth rate, the second flattens out toward the
last fitted level, because the model that produced it has no term that says the series should keep
increasing on average.

<figure>
<svg viewBox="0 0 460 230" role="img" aria-label="Two forecasts beyond the last observation: one continues the historical drift, the other flattens because the fitted model has no intercept">
  <line x1="40" y1="200" x2="440" y2="200" stroke="currentColor" stroke-width="1"/>
  <text x="440" y="216" text-anchor="end" font-size="12" fill="currentColor">time</text>
  <polyline points="40,175 90,160 140,138 190,118 240,100" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="55" y="150" font-size="12" fill="currentColor">observed data</text>
  <line x1="240" y1="20" x2="240" y2="200" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="245" y="32" font-size="12" fill="currentColor">now (t = n)</text>
  <polyline points="240,100 320,72 420,40" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="300" y="58" font-size="12" fill="currentColor">with intercept</text>
  <polyline points="240,100 420,100" fill="none" stroke="orange" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="280" y="120" font-size="12" fill="orange">no intercept (flat)</text>
</svg>
<figcaption>Fitting with $d \geq 1$ inside ARIMA drops the intercept, so the forecast flattens at the
last fitted level. Fitting the same AR/MA structure directly on the already-differenced series
keeps the intercept, and undoing the differencing by hand (telescoping the forecast differences
back onto the last observed level) lets the forecast keep drifting.</figcaption>
</figure>

## Choosing a specification by ACF/PACF: the TTLCONS example

The same fitting choices matter once you move from a single AR(1) to picking a full ARIMA
specification. For total construction spending (TTLCONS, monthly), the workflow is: take logs,
then read off candidate orders from the ACF and PACF of the differenced series.

Once-differenced $\log(\text{TTLCONS})$ (i.e. `ylogdiff`) suggests two candidate structures:

1. **AR(3)** for the differenced log data,
2. **MA(6)** for the differenced log data,

and, since either of these can be fit either by differencing the data first or by handing the
differencing to `ARIMA` via $d=1$, that gives two more candidates that use the *same* AR/MA order
but are fit differently and so, as the previous section showed, can forecast differently:

3. **ARIMA$(3,1,0)$** fit directly on $\log(\text{TTLCONS})$ — the same AR(3) structure as Model 1,
   but with no intercept, since $d=1$,
4. **ARIMA$(0,1,6)$** fit directly on $\log(\text{TTLCONS})$ — the same MA(6) structure as Model 2,
   again with no intercept.

Differencing a second time, `ylogdiff2` $= \operatorname{diff}(\operatorname{diff}(\log y))$, and
reading its ACF/PACF suggests one more candidate:

5. **ARIMA$(0,2,1)$** for the log data.

Finally, to see what an intercept would look like at $d=2$, an MA(1) is fit *directly on the
twice-differenced series* (so with an intercept, since here $d=0$ from `ARIMA`'s point of view):

6. **MA(1) on `ylogdiff2`**, with its forecasts telescoped back to the log scale in *two* stages —
   first undoing the second difference, then undoing the first.

## Why the six forecasts disagree

Laid out together, the same intercept story from the GNP example repeats, now over six models
instead of two:

- **Models 1 and 2** are both fit directly on the once-differenced series (so both carry an
  intercept — the estimated average percent change per month), and, once their forecasts are
  telescoped back to the log scale, they "lead to basically the same predictions."
- **Model 3**, fit as ARIMA$(3,1,0)$ with $d=1$ built in, has no intercept, and "the lack of
  intercept is leading to flat predictions" relative to Models 1 and 2, even though it is fitting
  the same AR(3) structure to (almost) the same differenced data.
- **Model 4** is fit the same way as Model 3 (direct fit, $d=1$, no intercept), and its forecasts
  are "largely similar" to Model 3's.
- **Model 5** pushes the same no-intercept logic one difference further ($d=2$), compounding the
  effect of having no drift term over two rounds of differencing.
- **Model 6** restores an intercept by fitting on `ylogdiff2` directly (as with Models 1 and 2) and
  telescoping the forecast back through both differences by hand, rather than letting `ARIMA` take
  $d=2$.

The lecture's own summary of the resulting plot is worth keeping as the closing observation, since
it is the point of the exercise: "All these models seem to give quite different predictions. Which
prediction do you like?" — the ACF/PACF plots alone do not settle which of six defensible-looking
specifications to trust; whether the fitting routine carries an intercept turns out to matter as
much as the AR/MA order itself.

## Sources

- `01-ar-model-fitting-autoreg-vs-arima.md` (GNP dataset: `AutoReg` vs `ARIMA`, conditional vs full
  likelihood for AR(1), the custom log-likelihood optimizer, the stationarity-region comparison on
  raw GNP, and the ARIMA$(1,1,0)$-vs-telescoped-ARIMA$(1,0,0)$ forecast comparison) — from
  `berkeley-stat153/fall-2025`, `CodeLabEleven153248Fall2025.ipynb`, CC BY 4.0.
- `02-ttlcons.md` (TTLCONS dataset: ACF/PACF-based model selection, the six candidate models, and
  their forecasts) — same notebook, `berkeley-stat153/fall-2025`, CC BY 4.0.
- The notes explicitly point to two earlier lectures not contained in this material: **Lecture 17**,
  for the derivation of the full AR(1) likelihood used here, and **Lecture 21**, where these ARIMA
  models were first fit to TTLCONS.

---

[← 26. From Sinusoid to AR(2)](26-from-sinusoid-to-ar-2.md) · [Contents](index.md) · [28. High-Dimensional Regression for Change-Points →](28-high-dimensional-regression-for-change-points.md)
