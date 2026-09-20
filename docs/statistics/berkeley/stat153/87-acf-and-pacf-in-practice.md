---
title: "87. ACF and PACF in Practice"
course: "Berkeley Stat 153 Fall 2024"
chapter: 87
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 87. ACF and PACF in Practice

## What this covers

This chapter works a single real dataset — annual sunspot counts — through the autoregressive
model-building pipeline: read the sample ACF and PACF to propose an order, confirm computationally
what the sample PACF actually *is*, show why it is called a **partial** correlation by computing
one directly, and check that the resulting fitted models are causal and stationary. It assumes the
AR($p$) model, ordinary least squares, and the definitions of the sample autocorrelation function
(ACF) and partial autocorrelation function (PACF) already used for model identification.

## The sunspot series: reading the ACF and PACF plots

The data are annual sunspot counts starting in 1700 (`SN_y_tot_V2.0.csv`). Plotting the sample ACF
and PACF out to lag 50 gives two very different pictures.

The sample ACF oscillates and dies out slowly: the autocorrelations are still non-negligible past
lag 12, and even lags 15–17 look nontrivial. An MA($q$) process has autocorrelation *exactly* zero
past lag $q$ by construction, so an ACF that keeps oscillating and refuses to die out this slowly is
evidence against a low-order MA model, not for one.

The sample PACF is much more informative: two large spikes at lags 1 and 2, then values close to
zero — with one exception, a second, smaller cluster of non-negligible values at lags 7, 8 and 9.
Since the PACF of a true AR($p$) process is zero past lag $p$, this plot argues for two candidate
models at once: AR(2), from the dominant spikes, and AR(9), if the smaller cluster at 7–9 is taken
seriously too.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="Sample PACF of the sunspot series by lag, showing two large spikes at lags 1 and 2 and a smaller cluster at lags 7 to 9">
  <line x1="40" y1="110" x2="380" y2="110" stroke="currentColor" stroke-width="1"/>
  <line x1="55" y1="110" x2="55" y2="40.5" stroke="currentColor" stroke-width="2"/>
  <circle cx="55" cy="40.5" r="2.5" fill="currentColor"/>
  <line x1="82" y1="110" x2="82" y2="169.2" stroke="currentColor" stroke-width="2"/>
  <circle cx="82" cy="169.2" r="2.5" fill="currentColor"/>
  <line x1="109" y1="110" x2="109" y2="122.4" stroke="currentColor" stroke-width="2"/>
  <circle cx="109" cy="122.4" r="2.5" fill="currentColor"/>
  <line x1="136" y1="110" x2="136" y2="109.1" stroke="currentColor" stroke-width="2"/>
  <circle cx="136" cy="109.1" r="2.5" fill="currentColor"/>
  <line x1="163" y1="110" x2="163" y2="110.8" stroke="currentColor" stroke-width="2"/>
  <circle cx="163" cy="110.8" r="2.5" fill="currentColor"/>
  <line x1="190" y1="110" x2="190" y2="98.4" stroke="currentColor" stroke-width="2"/>
  <circle cx="190" cy="98.4" r="2.5" fill="currentColor"/>
  <line x1="217" y1="110" x2="217" y2="92.9" stroke="currentColor" stroke-width="2"/>
  <circle cx="217" cy="92.9" r="2.5" fill="currentColor"/>
  <line x1="244" y1="110" x2="244" y2="91.1" stroke="currentColor" stroke-width="2"/>
  <circle cx="244" cy="91.1" r="2.5" fill="currentColor"/>
  <line x1="271" y1="110" x2="271" y2="91.5" stroke="currentColor" stroke-width="2"/>
  <circle cx="271" cy="91.5" r="2.5" fill="currentColor"/>
  <line x1="298" y1="110" x2="298" y2="108.3" stroke="currentColor" stroke-width="2"/>
  <circle cx="298" cy="108.3" r="2.5" fill="currentColor"/>
  <line x1="325" y1="110" x2="325" y2="109.0" stroke="currentColor" stroke-width="2"/>
  <circle cx="325" cy="109.0" r="2.5" fill="currentColor"/>
  <line x1="352" y1="110" x2="352" y2="111.0" stroke="currentColor" stroke-width="2"/>
  <circle cx="352" cy="111.0" r="2.5" fill="currentColor"/>
  <text x="25" y="114" font-size="11" fill="currentColor">0</text>
  <text x="55" y="195" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="82" y="195" text-anchor="middle" font-size="11" fill="currentColor">2</text>
  <text x="217" y="195" text-anchor="middle" font-size="11" fill="currentColor">7</text>
  <text x="244" y="195" text-anchor="middle" font-size="11" fill="currentColor">8</text>
  <text x="271" y="195" text-anchor="middle" font-size="11" fill="currentColor">9</text>
  <text x="352" y="195" text-anchor="middle" font-size="11" fill="currentColor">12</text>
  <text x="210" y="212" text-anchor="middle" font-size="12" fill="currentColor">lag h</text>
</svg>
<figcaption>Sample PACF of the sunspot series by lag: two dominant spikes at lags 1 and 2, and a
smaller secondary cluster at lags 7–9 — the two candidate AR orders pursued below.</figcaption>
</figure>

## Calculating the sample PACF from an AR fit

Recall the operational definition: the sample PACF at lag $h$, $\widehat{\mathrm{PACF}}(h)$, is the
estimated coefficient $\hat\phi_h$ obtained by fitting an AR($h$) model — with lags $1$ through $h$
— to the data, and reading off the coefficient on the *last* lag, $y_{t-h}$.

This is exactly how the plotted values above were produced: fit AR(1) and take its one slope; fit
AR(2) and take the coefficient on $y_{t-2}$; and so on up to AR(50), each time discarding every
coefficient except the last. Doing this by hand for the sunspot series and comparing against
`statsmodels`'s built-in `pacf` routine gives identical numbers at every lag checked — $0.818$ at
lag 1, $-0.696$ at lag 2, ..., $0.218$ at lag 9, and so on through lag 50 — confirming that "fit
AR($h$), keep the last coefficient" *is* the sample PACF, not merely an approximation to it.

## Why "partial": the PACF as a partial correlation

The name promises something more specific than "a regression coefficient." In general, the
**partial correlation** between two variables $y$ and $x$, given a set of other variables
$z_1,\dots,z_k$, is defined as the ordinary correlation between the two *residuals* left over once
each of $y$ and $x$ has been regressed on $z_1,\dots,z_k$:
$$\mathrm{corr}\big(e^{\,y\mid z_1,\dots,z_k},\ e^{\,x\mid z_1,\dots,z_k}\big).$$
Both residuals are what remain of $y$ and $x$ once the information shared with the $z$'s has been
removed, so their correlation measures the association between $y$ and $x$ that is not explained by
$z_1,\dots,z_k$.

The claim is that $\widehat{\mathrm{PACF}}(p)$ is precisely the partial correlation between $y_t$
and $y_{t-p}$, given the intervening lags $y_{t-1},\dots,y_{t-p+1}$ — exactly the "in-between"
information that could otherwise explain away an apparent link between $y_t$ and $y_{t-p}$.

Take $p = 9$ on the sunspot series as a check. Fitting the full AR(9) regression — $y_t$ on a
constant and $y_{t-1},\dots,y_{t-9}$ — gives $\hat\phi_9 = 0.2177$, matching
$\widehat{\mathrm{PACF}}(9)$ computed above. Now compute the partial correlation directly:

- regress $y_t$ on the constant and $y_{t-1},\dots,y_{t-8}$ (everything **except** $y_{t-9}$), and
  keep the residual $e^{\,y_t \mid y_{t-1},\dots,y_{t-8}}$;
- regress $y_{t-9}$ on the same set $y_{t-1},\dots,y_{t-8}$, and keep its residual
  $e^{\,y_{t-9}\mid y_{t-1},\dots,y_{t-8}}$;
- correlate the two residuals.

That correlation comes out to $0.2195$ — extremely close to $\hat\phi_9 = 0.2177$, but not
identical.

## Reconciling the two numbers

The small gap is not noise; it has a precise algebraic source. In a multiple regression of $y$ on
covariates $x_1,\dots,x_k$, each fitted coefficient is related to a partial correlation by
$$\hat\beta_j = \mathrm{corr}\big(e^{\,y\mid x_k,\,k\neq j},\ e^{\,x_j\mid x_k,\,k\neq j}\big)
\sqrt{\dfrac{\mathrm{var}\big(e^{\,y\mid x_k,\,k\neq j}\big)}{\mathrm{var}\big(e^{\,x_j\mid x_k,\,k\neq j}\big)}}.$$
A regression coefficient is a partial correlation *rescaled* by the ratio of the two residual
standard deviations — and that ratio is 1 only when the two residuals happen to have equal
variance.

For the lag-9 example, the two residual variances are $570.4$ (for $e^{\,y_t\mid\cdots}$) and
$580.0$ (for $e^{\,y_{t-9}\mid\cdots}$) — close, but not equal, because regressing $y_t$ on the
intervening lags and regressing $y_{t-9}$ on the same intervening lags are two different
least-squares problems, with no reason to produce residuals of identical spread. Multiplying the
partial correlation by the square root of the variance ratio,
$$0.2195 \times \sqrt{\frac{570.4}{580.0}} = 0.2177,$$
recovers $\hat\phi_9$ exactly. So the sample PACF at lag $p$ genuinely *is* a partial correlation;
it only looks slightly different from the AR($p$) coefficient because a regression coefficient and
a partial correlation are two different rescalings of the same residual geometry, and they coincide
exactly only when the two residual variances match.

## Fitting AR(2) and AR(9), and checking they are usable models

The PACF plot proposed two candidate orders, so both get fit to the full series with `AutoReg`.
Forecasting 200 steps beyond the end of the observed data, the AR(9) forecast tracks the (unseen)
continuation of the series visibly better than AR(2) does, at least for the first several steps —
evidence that the smaller PACF spikes at lags 7–9 were carrying real information rather than noise.

Before trusting either fit, though, both need to be checked for **causal stationarity**. For an
AR($p$) model
$$y_t = \phi_0 + \phi_1 y_{t-1} + \cdots + \phi_p y_{t-p} + \varepsilon_t,$$
form the **characteristic polynomial** built from the fitted coefficients,
$$\phi(z) = 1 - \phi_1 z - \phi_2 z^2 - \cdots - \phi_p z^p.$$
This has degree $p$, so it has $p$ roots $z_1,\dots,z_p$ (possibly complex, even though the
$\phi_i$ are real — complex roots come in conjugate pairs). The fitted model is causal and
stationary exactly when **every** root has modulus strictly greater than $1$.

For the fitted AR(2), the characteristic polynomial has a complex-conjugate pair of roots, each of
modulus $\approx 1.198$ — both above 1, so the model is causal and stationary. For the fitted AR(9),
all nine roots (four conjugate pairs plus one real root) have modulus between about $1.02$ and
$1.31$ — again every one above 1, so this larger model is causal and stationary too. `AutoReg`'s
`.summary()` reports these roots and moduli directly; they can also be recovered by hand with
`np.roots` applied to the coefficient list $[-\phi_p,\dots,-\phi_1,1]$, and the two calculations
agree, up to the arbitrary order in which the roots are listed.

## Sources

- Sunspot ACF/PACF plots, the MA-vs-AR order-selection reasoning, and the "fit AR($h$), keep the
  last coefficient" definition of the sample PACF with its check against `statsmodels.tsa.stattools.pacf`:
  [`01-acf-and-pacf.md`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab11.ipynb)
  (Berkeley STAT 153, Spring 2025, Lab 11).
- The definition of partial correlation, the lag-9 worked example (direct AR(9) regression,
  residual construction, and reconciling regression-coefficient formula), the AR(2)/AR(9) fits and
  forecasts, and the causal-stationarity check via characteristic-polynomial roots:
  [`02-regression-and-partial-correlation.md`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab11.ipynb)
  (same lab).
- Both files are converted from `Lab11.ipynb` (berkeley-stat153, spring 2025), CC BY 4.0. Three
  figures from the original notebook — the raw series plot, the ACF/PACF plot, and the forecast
  plot — were omitted in the converted source and are not reproduced here (the PACF figure above is
  redrawn from the printed sample PACF values, not from the original plot). The underlying dataset,
  `SN_y_tot_V2.0.csv` (the world sunspot number series), is referenced by the notebook but not
  supplied as an input to this chapter.

---

[← 86. Fitting AR(p) Models to GNP](86-fitting-ar-p-models-to-gnp.md) · [Contents](index.md) · [88. ARIMA Fitting and Model Selection →](88-arima-fitting-and-model-selection.md)
