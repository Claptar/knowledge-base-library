---
title: "49. Autoregressive Models in Practice"
course: "Berkeley Stat 153"
chapter: 49
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 49. Autoregressive Models in Practice

## What this covers

This is a lab-style lecture: it works a single practical question across three real time series —
given actual data, how do you fit an autoregressive model to it, and how do you turn the fit into a
forecast? Along the way it tells the origin story of the AR model itself, because the lecture uses
that history — Yule's 1927 analysis of the sunspot record — to motivate why the model has the form
it does. The chapter assumes the reader already knows what an AR(p) process is, can fit and read an
ordinary least-squares regression, and has seen the single-sinusoid regression model
$y_t=\beta_0+\beta_1\cos(2\pi ft)+\beta_2\sin(2\pi ft)+\epsilon_t$ from an earlier lecture in the
course.

## Fitting an AR(p) model as an ordinary regression

An AR(p) model is
$$y_t = \phi_0 + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \cdots + \phi_p y_{t-p} + \epsilon_t.$$
The point of this lecture is that, given data $y_1,\dots,y_n$, fitting it is nothing more than an
ordinary multiple regression. Treat $y_{p+1},\dots,y_n$ as the response vector, and for each of
these build a row of predictors out of the $p$ values immediately before it: the row belonging to
response $y_{p+i}$ holds $(1,\,y_{p+i-1},\,y_{p+i-2},\,\dots,\,y_{p+i-p})$. Sliding this window one
time step at a time down the series turns the single sequence $y_1,\dots,y_n$ into an
$(n-p)\times(p+1)$ regression table, which is then fit by ordinary least squares exactly like any
other regression — this is literally what the code does: one column of the design matrix per lag,
built by slicing overlapping windows of the series.

<figure>
<svg viewBox="0 0 340 170" role="img" aria-label="A sliding window of p lagged values along a time series becomes one row of the regression design matrix">
  <line x1="20" y1="30" x2="310" y2="30" stroke="currentColor" stroke-width="1"/>
  <g font-size="11" fill="currentColor" text-anchor="middle">
    <circle cx="40" cy="30" r="3.5" fill="currentColor"/>
    <text x="40" y="18">y1</text>
    <circle cx="80" cy="30" r="3.5" fill="currentColor"/>
    <text x="80" y="18">y2</text>
    <circle cx="120" cy="30" r="3.5" fill="currentColor"/>
    <text x="120" y="18">y3</text>
    <circle cx="160" cy="30" r="3.5" fill="currentColor"/>
    <text x="160" y="18">y4</text>
    <circle cx="200" cy="30" r="3.5" fill="currentColor"/>
    <text x="200" y="18">y5</text>
    <circle cx="240" cy="30" r="3.5" fill="currentColor"/>
    <text x="240" y="18">y6</text>
    <circle cx="280" cy="30" r="3.5" fill="currentColor"/>
    <text x="280" y="18">y7</text>
  </g>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="32" y="55" width="96" height="18" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="80" y="67" text-anchor="middle" font-size="11" fill="currentColor">row 1: predictors</text>
  <line x1="128" y1="64" x2="157" y2="33" stroke="currentColor" stroke-width="1" marker-end="url(#arrow)"/>
  <rect x="72" y="90" width="96" height="18" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="120" y="102" text-anchor="middle" font-size="11" fill="currentColor">row 2: predictors</text>
  <line x1="168" y1="99" x2="197" y2="33" stroke="currentColor" stroke-width="1" marker-end="url(#arrow)"/>
  <rect x="112" y="125" width="96" height="18" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="160" y="137" text-anchor="middle" font-size="11" fill="currentColor">row 3: predictors</text>
  <line x1="208" y1="134" x2="237" y2="33" stroke="currentColor" stroke-width="1" marker-end="url(#arrow)"/>
  <text x="285" y="150" font-size="14" fill="currentColor">…</text>
</svg>
<figcaption>Each row of the AR(p) design matrix is a window of p consecutive values (shaded) used
to predict the value right after it (arrow); sliding the window forward one step at a time turns a
single series into a regression table. Shown here for p = 3.</figcaption>
</figure>

## Choosing the order p: liquor store sales

The first dataset is FRED's monthly retail sales figures for beer, wine and liquor stores, January
1992 to October 2025 ($n=403$). The series has an unmistakable seasonal spike every December —
values roughly 1.3–1.5 times the surrounding months (for example 2354 in one December against
values around 1650–1800 in the neighbouring months).

Fitting AR(12) — $n-p=391$ observations, 13 columns including the intercept — gives $R^2=0.988$.
The coefficient on lag 12 dominates the fit: $\hat\phi_{12}=0.974$ (s.e. $0.019$, $t=52.2$),
essentially saying "next month's sales are close to the same month last year, adjusted by small
corrections from the intervening months." A handful of the shorter lags (1, 2, 3, 5) are also
mildly significant with small positive coefficients around $0.03$–$0.05$, and lags 9–10 come out
negative and significant; most others are not distinguishable from zero. The regression also flags
a large condition number ($3.36\times10^4$), a symptom of multicollinearity that is unsurprising
here — consecutive months of the same series are highly correlated with each other.

The central lesson the lecture draws from this example: **the order $p$ has to be large enough to
see the periodicity you're trying to capture.** "The predictions depend crucially on the order $p$
of the model. If $p\geq 12$, we get reasonable predictions. However for smaller values of $p$, the
predictions look very unnatural." Because the series has a strong annual (12-month) seasonal
component, an AR model needs at least one lag reaching back a full year to have any chance of
reproducing next December's jump; with fewer lags the model can only extrapolate a smooth local
trend and misses the seasonal spike entirely.

## Forecasting: feeding predictions back into the model

To forecast $k$ steps beyond the observed data, the lecture extends the series with $k$ placeholder
slots and fills them in one at a time using the fitted coefficients:
$$\hat y_{n+i} = \hat\phi_0 + \sum_{j=1}^{p} \hat\phi_j\, \tilde y_{n+i-j}, \qquad i=1,\dots,k,$$
where $\tilde y_{n+i-j}$ is the *actual* observed value $y_{n+i-j}$ when $n+i-j\le n$, and the
already-computed forecast $\hat y_{n+i-j}$ otherwise. In other words: as soon as the lag window runs
off the end of the observed data, the recursion starts feeding its own forecasts back in as if they
were data, and this is what lets it extend arbitrarily far into the future. Every forecast plot in
this lecture — for the liquor sales, the house prices, and the sunspots — is generated by this same
plug-in loop, only the fitted coefficients and the lag structure change.

## A trending series, and working on the log scale: house prices

The second dataset is FRED's average sales price of houses sold in the US, quarterly from 1963 to
2025 ($n=250$), a series that trends upward throughout. Fitting AR(30) — 30 quarters, about
7.5 years of lags — gives $R^2=0.998$, but with a very large condition number ($2.29\times10^6$):
heavy multicollinearity among 30 correlated lags of a smoothly trending series. Many individual lag
coefficients are not significant on their own even though the joint fit is excellent — the expected
symptom of multicollinearity, where the lags predict well together but no single lag's contribution
is well identified.

The lecture then reruns the identical procedure on $\log y_t$ instead of $y_t$: same order $p=30$,
same lag-regression construction. The fit is slightly better ($R^2=0.999$), and, more strikingly,
the condition number drops to $6.47\times10^3$ — three orders of magnitude smaller than on the raw
scale. A natural reading of that drop: raw house prices range from about \$19,300 to \$525,100 over
the sample, and taking logs compresses that huge range into a narrow numeric band, which is kinder
to the conditioning of a design matrix built from many correlated lags of the same series. Forecasts
are generated by the same plug-in recursion, now on the log scale, and the lecture compares them
back on the original scale — either by exponentiating the log-scale forecast or by using the
raw-scale AR(30) forecast directly — without drawing a further conclusion about which is better in
the text.

## Where the AR model came from: sunspots and Yule (1927)

The third dataset is the annual sunspot record ($n=325$ years, from `SN_y_tot_V2.0.csv`), and it is
not just another example — autoregressive models were originally invented in the context of this
data, by Yule, in 1927. The series shows a roughly 11-year cycle, but an irregular one: cycles vary
in both length and peak height, unlike a perfect sinusoid.

### The single-sinusoid model, and the check that broke it

The lecture first recalls a model used in an earlier lecture, the single sinusoid plus noise,
$$y_t = \beta_0 + \beta_1\cos(2\pi f t) + \beta_2 \sin(2\pi ft) + \epsilon_t, \qquad
\epsilon_t \overset{\text{iid}}{\sim} N(0,\sigma^2).$$
Given $f$, this is linear in $\beta_0,\beta_1,\beta_2$ and fit by OLS; $f$ itself is estimated by a
grid search, computing the residual sum of squares $RSS(f)$ of the best-fitting regression at each
of $10{,}000$ candidate values of $f$ over $(0, 0.5)$ and taking $\hat f=\arg\min_f RSS(f)$. Here
$\hat f = 1/11 \approx 0.0909$, matching the well-known 11-year solar cycle. With $\hat f$ fixed,
the remaining parameters are estimated by OLS as usual: $\hat\beta_0=78.88$, $\hat\beta_1=-38.28$,
$\hat\beta_2=-29.28$, with two close variance estimates $\hat\sigma_{\text{MLE}}=51.62$ ($RSS/n$)
and $\hat\sigma_{\text{unbiased}}=51.86$ ($RSS/(n-3)$).

Yule's objection to this model wasn't about the fit — by these numbers it fits reasonably — it was
about whether the model is a plausible account of *how the data was generated*. The check: simulate
a synthetic series from the fitted model (same $\hat f$, $\hat\beta$, $\hat\sigma$, fresh i.i.d.
Gaussian noise), and compare it by eye against the real series — plotting several simulated
datasets alongside the real one in a grid of panels and asking whether the real data can be spotted
as the odd one out. It can be: the simulated series look "too wiggly and irregular," lacking the
smooth, well-defined peaks the real sunspot record has. The model gets the frequency content right
on average but not the *texture* of the data — evidence that the noise in the real process is not
simply additive on top of a fixed deterministic curve.

### Yule's recursive model

Yule's alternative replaces the additive sinusoid with a recursion:
$$y_t = \phi_0 + \phi_1 y_{t-1} - y_{t-2} + \epsilon_t,$$
which is an AR(2) model with the second coefficient pinned at $\phi_2=-1$, and $\phi_1$ tied to
frequency by $\phi_1 = 2\cos(2\pi f)$.

That relation is plausible already in the noise-free case: if $\epsilon_t\equiv 0$, $\phi_0=0$, and
$y_t=\cos(\theta t)$ with $\theta = 2\pi f$, the trigonometric identity
$\cos(\theta t)+\cos(\theta(t-2)) = 2\cos\theta\cos(\theta(t-1))$ rearranges to exactly
$y_t = 2\cos\theta\, y_{t-1} - y_{t-2}$ — so a pure, noise-free sinusoid of frequency $f$ satisfies
Yule's recursion precisely when $\phi_1=2\cos(2\pi f)$. Injecting the noise *inside* the recursion,
rather than adding it on top of a fixed sinusoid afterward, is the substantive change from the
earlier model.

Estimation exploits the fixed $\phi_2=-1$: rearranging to
$y_t + y_{t-2} = \phi_0 + \phi_1 y_{t-1} + \epsilon_t$ turns the fit into an ordinary simple
regression of $y_t+y_{t-2}$ on $y_{t-1}$ — there is no need to fit $\phi_2$ separately once it is
fixed by assumption. On $n-2=323$ observations this gives $\hat\phi_0=28.68$,
$\hat\phi_1=1.6365$ ($R^2=0.930$). Inverting $\hat\phi_1=2\cos(2\pi\hat f)$ gives
$\hat f = \arccos(\hat\phi_1/2)/(2\pi)$ and an estimated period of about $10.26$ years — a little
shorter than the 11-year period the single-sinusoid model gave. The two models, fit to the same
data, disagree slightly on the cycle length, because neither is "the" true generating process and
each is estimating $f$ through a different lens.

Forecasting with the plug-in recursion produces a *perfectly* sinusoidal forecast that continues
forever at the fixed estimated period — a direct consequence of $\phi_2$ being pinned exactly at
$-1$ (the noise-free argument above says the recursion, run forward with the noise switched off,
retraces an exact sinusoid indefinitely). The lecture flags this as a liability: because real
sunspot cycles vary in length, a forecast locked to one exact period will eventually drift out of
phase with the real cycle, degrading its accuracy over a long horizon.

Simulating from the fitted Yule model — fresh $N(0,\hat\sigma^2)$ noise at each step, with
$\hat\sigma\approx 27.78$, fed recursively through $y_t=\hat\phi_0+\hat\phi_1y_{t-1}-y_{t-2}+\epsilon_t$
— and comparing to the real data again: the real series can probably still be picked out, but the
simulated series are now qualitatively right — "quite smooth, just like the actual sunspots data."
Feeding the noise into the recursion, instead of adding it on top of a fixed curve, is what recovers
the smooth, cycle-like texture the additive model couldn't reproduce. The lecture's conclusion is
that the two "sinusoid + noise" constructions — additive noise on a fixed curve, versus noise
injected into a recursion — are fundamentally different generative processes, even though both
nominally describe an oscillation at roughly the same frequency.

### The general AR(2) model

Yule's model is the special case $\phi_2=-1$ of the ordinary AR(2) model
$y_t=\phi_0+\phi_1y_{t-1}+\phi_2y_{t-2}+\epsilon_t$. Fitting all three coefficients freely — the
same lag-regression construction used for the liquor-sales and house-price examples, now with
$p=2$ — on the same 325 years of sunspot data ($n-p=323$) gives
$\hat\phi_0=24.46$, $\hat\phi_1=1.388$, $\hat\phi_2=-0.696$ ($R^2=0.829$, innovation standard
deviation $\hat\sigma\approx 25.59$).

Two things stand out against Yule's model. First, the data does not actually want $\phi_2=-1$:
freely estimated it comes out around $-0.70$, well inside $(-1,1)$, and the fitted innovation
standard deviation ($\approx 25.6$) is a little smaller than Yule's ($\approx 27.8$) — the freer
model fits marginally better, as it must with an extra free parameter, but the gap is modest.
Second, and more important, the *behaviour* of the two models' forecasts is very different: Yule's
forecasts oscillate forever at fixed amplitude, while the freely-fit AR(2)'s forecasts are, in the
lecture's words, "given by a damped sinusoid" — one that oscillates with shrinking amplitude and
flattens out to roughly a constant after only a few steps. (The lecture notes this is proved
properly "in the coming lectures"; here it is simply read off the forecast plot.) The practical
trade-off drawn from this: because the real sunspot cycles are irregular in period, a model whose
long-range forecast eventually flattens to a constant can do better than one whose forecast keeps
oscillating at a fixed — and possibly wrong — period, since a flat forecast can't go as badly out of
phase as a perpetual sinusoid can.

Simulations from the freely-fit AR(2) are again smooth — "much smoother" than simulations from the
original single-sinusoid model — consistent with the earlier finding that injecting noise
recursively, rather than additively, is what reproduces the qualitative texture of the sunspot
series.

## Sources

- Fitting AR(p) as regression, the liquor-sales example, and the plug-in forecasting recursion:
  `docs/statistics/berkeley/stat153/fall-2025/CodeLectureSixteen153248Fall2025/01-dataset-one-liquor-sales-data-from-fred.md`
  (Fall 2025 Code Lecture 16, converted from `CodeLectureSixteen153248Fall2025.ipynb`, CC BY 4.0),
  cross-checked against the Spring 2025 equivalent,
  `docs/statistics/berkeley/stat153/spring-2025/CodeLectureSixteen153248Spring2025/01-dataset-one-liquor-sales-data-from-fred.md`
  (same lecture, earlier data vintage; numbers quoted here are from the Fall 2025 pull).
- The house-price example and the log-scale refit: fall-2025 part 02,
  `.../CodeLectureSixteen153248Fall2025/02-dataset-two-house-price-data-from-fred.md`. Spring 2025
  does not include this dataset.
- The sunspots narrative (single-sinusoid model, Yule's model, the simulation-based model checks):
  fall-2025 part 03, `.../CodeLectureSixteen153248Fall2025/03-sunspots-data.md`, cross-checked
  against spring-2025 part 03 (`.../CodeLectureSixteen153248Spring2025/03-sunspots-data.md`), which
  covers the Yule model but omits the single-sinusoid model and its simulation check.
- The general AR(2) fit to sunspots: fall-2025 part 04,
  `.../CodeLectureSixteen153248Fall2025/04-ar-2-model.md`, matching numbers in spring-2025 part 04,
  `.../CodeLectureSixteen153248Spring2025/04-ar-2-model.md`.
- No slides or transcript were supplied for this lecture; both source files are converted Jupyter
  notebooks (code and prose cells only), and all figures in them are omitted from the converted
  text ("figure omitted — see the original notebook"), so descriptions of plot shapes above ("too
  wiggly," "quite smooth," "damped sinusoid") are the lecture's own words about what the omitted
  figures show, not independently verified here.
- The single-sinusoid regression model and its frequency-by-grid-search fitting procedure are
  referenced as material from an earlier lecture ("we previously used this model") not included in
  these files. The claim that AR(2) forecasts are exactly a damped sinusoid is likewise flagged in
  the source as a result proved "in the coming lectures," not derived in this one.
- No problem set was supplied with this lecture.

---

[← 48. Profile RSS: Changepoints and the Periodogram](48-profile-rss-changepoints-and-the-periodogram.md) · [Contents](index.md) · [50. Broken-Stick Regression and Regularization →](50-broken-stick-regression-and-regularization.md)
