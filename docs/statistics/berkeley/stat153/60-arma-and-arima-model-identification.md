---
title: "60. ARMA and ARIMA Model Identification"
course: "Berkeley Stat 153"
chapter: 60
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 60. ARMA and ARIMA Model Identification

## What this covers

This chapter answers the question that follows immediately from having AR($p$), MA($q$) and
ARMA($p,q$) models in hand: given a real, plainly non-stationary series, how do you decide which
orders to fit, and how do you check the fit is any good? It assumes the reader already has the
definitions of AR($p$), MA($q$) and ARMA($p,q$) processes, what causal stationarity means for such
a process, and what the autocorrelation function (ACF) and partial autocorrelation function (PACF)
are. What is new here is: the two cutoff facts that make order identification possible for a pure
AR or pure MA model, and why they fail for a mixed ARMA; the root parametrization used to check
whether a fitted AR(2) is causal; the Box–Jenkins recipe of differencing, reading the ACF/PACF, and
refitting, worked through in full on a real economic series; and the use of AIC and BIC to
automate — and sometimes fail to automate correctly — the search over orders.

## Reading orders off the ACF and PACF

For a pure AR or pure MA process, the theoretical ACF and PACF carry a sharp signature:

- For an **MA($q$)** process, the ACF is exactly zero beyond lag $q$: $\rho(h) = 0$ for $h > q$.
- For an **AR($p$)** process, the PACF is exactly zero beyond lag $p$: $\alpha(h) = 0$ for $h > p$.
- For a genuine **ARMA($p,q$)** process with *both* $p \geq 1$ and $q \geq 1$, neither function
  becomes zero after any finite lag.

The first two facts are what make order identification from a plot possible at all: count how many
lags the ACF (respectively PACF) stays away from zero, and that count is $q$ (respectively $p$).
The third fact is the reason this trick stops working the moment the model has both an AR and an MA
part — there is no finite lag past which you can point and say "this is where it becomes zero," so
eyeballing the ACF and PACF no longer pins down $p$ and $q$. This is exactly the situation that
motivates the automatic, likelihood-based search later in the chapter.

<figure>
<svg viewBox="0 0 480 210" role="img" aria-label="Stem plots showing the ACF of an MA(2) process cutting off after lag 2, and the PACF of an AR(2) process cutting off after lag 2">
  <text x="120" y="16" text-anchor="middle" font-size="12" fill="currentColor">ACF of MA(2)</text>
  <line x1="40" y1="150" x2="205" y2="150" stroke="currentColor" stroke-width="1"/>
  <line x1="110" y1="30" x2="110" y2="160" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="112" y="26" font-size="10" fill="currentColor">zero beyond lag q</text>
  <g stroke="currentColor" stroke-width="1.5">
    <line x1="50" y1="150" x2="50" y2="70"/>
    <line x1="74" y1="150" x2="74" y2="106"/>
    <line x1="98" y1="150" x2="98" y2="122"/>
    <line x1="122" y1="150" x2="122" y2="150"/>
    <line x1="146" y1="150" x2="146" y2="150"/>
    <line x1="170" y1="150" x2="170" y2="150"/>
    <line x1="194" y1="150" x2="194" y2="150"/>
  </g>
  <g fill="currentColor">
    <circle cx="50" cy="70" r="2.5"/>
    <circle cx="74" cy="106" r="2.5"/>
    <circle cx="98" cy="122" r="2.5"/>
    <circle cx="122" cy="150" r="2.5"/>
    <circle cx="146" cy="150" r="2.5"/>
    <circle cx="170" cy="150" r="2.5"/>
    <circle cx="194" cy="150" r="2.5"/>
  </g>
  <g font-size="10" fill="currentColor" text-anchor="middle">
    <text x="50" y="165">0</text><text x="74" y="165">1</text><text x="98" y="165">2</text>
    <text x="122" y="165">3</text><text x="146" y="165">4</text><text x="170" y="165">5</text>
    <text x="194" y="165">6</text>
  </g>
  <text x="120" y="195" text-anchor="middle" font-size="12" fill="currentColor">lag h</text>

  <text x="352" y="16" text-anchor="middle" font-size="12" fill="currentColor">PACF of AR(2)</text>
  <line x1="270" y1="150" x2="435" y2="150" stroke="currentColor" stroke-width="1"/>
  <line x1="340" y1="30" x2="340" y2="160" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="342" y="26" font-size="10" fill="currentColor">zero beyond lag p</text>
  <g stroke="currentColor" stroke-width="1.5">
    <line x1="280" y1="150" x2="280" y2="70"/>
    <line x1="304" y1="150" x2="304" y2="102"/>
    <line x1="328" y1="150" x2="328" y2="126"/>
    <line x1="352" y1="150" x2="352" y2="150"/>
    <line x1="376" y1="150" x2="376" y2="150"/>
    <line x1="400" y1="150" x2="400" y2="150"/>
    <line x1="424" y1="150" x2="424" y2="150"/>
  </g>
  <g fill="currentColor">
    <circle cx="280" cy="70" r="2.5"/>
    <circle cx="304" cy="102" r="2.5"/>
    <circle cx="328" cy="126" r="2.5"/>
    <circle cx="352" cy="150" r="2.5"/>
    <circle cx="376" cy="150" r="2.5"/>
    <circle cx="400" cy="150" r="2.5"/>
    <circle cx="424" cy="150" r="2.5"/>
  </g>
  <g font-size="10" fill="currentColor" text-anchor="middle">
    <text x="280" y="165">0</text><text x="304" y="165">1</text><text x="328" y="165">2</text>
    <text x="352" y="165">3</text><text x="376" y="165">4</text><text x="400" y="165">5</text>
    <text x="424" y="165">6</text>
  </g>
  <text x="350" y="195" text-anchor="middle" font-size="12" fill="currentColor">lag h</text>
</svg>
<figcaption>The identification rule: an MA(2)'s ACF is nonzero only up to lag 2, an AR(2)'s PACF is
nonzero only up to lag 2. For a mixed ARMA($p,q$) with $p,q\geq 1$, both plots keep producing
nonzero values forever, so there is no lag at which either one visibly "stops."</figcaption>
</figure>

`statsmodels` provides `arma_acf` and `arma_pacf`, which compute these theoretical (not sampled)
functions directly from a chosen set of AR and MA coefficients, so the shapes above can be
reproduced for any specific MA($q$), AR($p$), or mixed ARMA($p,q$) by simply changing the
coefficient lists fed into `ArmaProcess`.

## Checking causal stationarity of a fitted AR(2): the root parametrization

Before trusting any fitted AR model, it is worth having a quick way to check that it is causal and
stationary — otherwise none of the model's implied ACF, forecasts, or the identification rules
above are meaningful. For AR(2), $y_t = \phi_0 + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \epsilon_t$, this
is done through the roots of the characteristic polynomial $1 - \phi_1 z - \phi_2 z^2$.

Write $a_1, a_2$ for the **reciprocals** of these two roots. Then

$$
\phi_1 = a_1 + a_2, \qquad \phi_2 = -a_1 a_2,
$$

and the causal, stationary regime is exactly $|a_1| < 1$ and $|a_2| < 1$ — equivalently, the roots
of the characteristic polynomial themselves must lie strictly *outside* the unit circle (modulus
$> 1$).

**Real roots.** Take $a_1 = 0.4$, $a_2 = 0.5$; then $\phi_1 = a_1+a_2 = 0.9$ and
$\phi_2 = -a_1 a_2 = -0.2$. Simulating $y_t = \phi_1 y_{t-1} + \phi_2 y_{t-2} + \epsilon_t$ forward
from $y_1=y_2=0$ with Gaussian innovations of scale $\sigma=0.5$ produces an ordinary, mean-reverting
series — both reciprocal roots are inside the unit disk, so this is in the causal region.

**Complex roots.** Take $a_1 = \tfrac{1+i}{2}$, $a_2 = \tfrac{1-i}{2}$ (a conjugate pair). Then
$\phi_1 = \mathrm{Re}(a_1+a_2) = 1$ and $\phi_2 = -\mathrm{Re}(a_1a_2) = -\tfrac12$, since
$a_1a_2 = \tfrac{1-i^2}{4} = \tfrac12$. Here $|a_1|=|a_2| = \tfrac{\sqrt2}{2}\approx 0.707 < 1$, so
this AR(2) is still causal and stationary, but with complex reciprocal roots the simulated series
shows the pseudo-periodic, oscillating behavior characteristic of AR(2) processes with complex
characteristic roots. If instead $a_1$ is rescaled so that $|a_1|=|a_2|=1$ exactly (in the lecture's
example, changing a $\sqrt4$ in the denominator to $\sqrt2$), the reciprocal roots land exactly on
the unit circle and the simulated series is no longer stationary — this is the boundary case, a
unit root.

<figure>
<svg viewBox="0 0 300 260" role="img" aria-label="Unit circle with a causal root outside it and a boundary root sitting on it">
  <line x1="30" y1="140" x2="270" y2="140" stroke="currentColor" stroke-width="0.75" opacity="0.6"/>
  <line x1="150" y1="20" x2="150" y2="260" stroke="currentColor" stroke-width="0.75" opacity="0.6"/>
  <circle cx="150" cy="140" r="100" fill="none" stroke="currentColor" stroke-width="1.3"/>
  <text x="150" y="245" text-anchor="middle" font-size="11" fill="currentColor">unit circle (modulus = 1)</text>

  <circle cx="278" cy="80" r="3.2" fill="currentColor"/>
  <text x="196" y="70" font-size="11" fill="currentColor">root, modulus &#8776; 1.4</text>
  <text x="196" y="84" font-size="11" fill="currentColor">outside &#8594; causal, stationary</text>

  <circle cx="184" cy="46" r="3.6" fill="#d9534f"/>
  <text x="188" y="40" font-size="11" fill="#d9534f">root, modulus = 1</text>
  <text x="188" y="54" font-size="11" fill="#d9534f">on the circle &#8594; non-stationary</text>
</svg>
<figcaption>Causality of a fitted AR(2) is read off the moduli of the roots of its characteristic
polynomial: strictly outside the unit circle is causal and stationary; on the circle is a unit
root, the boundary of non-stationarity.</figcaption>
</figure>

This check is not only for hand-built simulations. When an AR($p$) model is fit with `AutoReg`,
its summary table reports the roots of the fitted AR polynomial together with their moduli, so the
same causality check applies directly to an estimated model: all moduli greater than 1 confirms the
fit is causal and stationary. Fitting `AutoReg(lags=2)` to a series simulated from the complex-root
example above recovers roots with real part $\approx 0.99$ and imaginary part $\approx \mp 0.99$,
modulus $\approx 1.40$ — matching the reciprocal of $|a_1|=|a_2|\approx0.707$, and comfortably
outside the unit circle.

## The Box–Jenkins recipe on a real series

The Box–Jenkins approach to a non-stationary series is: difference until the series looks
stationary, identify AR/MA orders for the differenced series from its ACF/PACF, fit, check
causality, and forecast — translating forecasts for the differenced series back into forecasts for
the original one. An ARIMA($p,d,q$) model packages exactly this: $p$ is the AR order, $q$ the MA
order, and $d$ the number of times the series is differenced before an ARMA($p,q$) is fit to what
remains.

**The data.** TTLCONS is a FRED series, total construction spending in the United States, monthly.
Its log, $y_t = \log(\text{TTLCONS}_t)$, trends upward and is plainly not stationary, so the first
differences $w_t = y_t - y_{t-1}$ are examined instead.

**Identification.** The sample PACF of $w_t$ is negligible beyond lag 3, which suggests an AR(3)
model for the differenced series.

**Fitting and checking.** Fitting AR(3) with an intercept (`AutoReg(lags=3)`) to $w_t$ gives

$$
\hat\phi_0 = 0.0021,\quad \hat\phi_1 = 0.2148,\quad \hat\phi_2 = 0.0636,\quad \hat\phi_3 = 0.2014,
$$

with $\hat\phi_2$ not significant ($p=0.211$). The reported roots of the fitted AR(3) polynomial
have moduli $1.41$ and (a complex pair) $1.87$, all comfortably greater than 1: the fit is causal
and stationary.

**Converting back to the original scale, by hand.** The fitted equation for the differenced series,

$$
y_t - y_{t-1} = \hat\phi_0 + \hat\phi_1(y_{t-1}-y_{t-2}) + \hat\phi_2(y_{t-2}-y_{t-3}) + \hat\phi_3(y_{t-3}-y_{t-4}) + \epsilon_t,
$$

is just an AR(3) model written in terms of differences; collecting the $y$ terms turns it into an
**AR(4) model for $y_t$ itself**:

$$
y_t = \hat\phi_0 + (1+\hat\phi_1)y_{t-1} + (\hat\phi_2-\hat\phi_1)y_{t-2} + (\hat\phi_3-\hat\phi_2)y_{t-3} - \hat\phi_3 y_{t-4} + \epsilon_t.
$$

Plugging in the fitted values gives coefficients $(0.0021,\ 1.2148,\ -0.1513,\ 0.1378,\ -0.2014)$,
and this AR(4) can be iterated forward directly to forecast $y_t$ — no separate step of
"un-differencing" the forecast is needed once the model is written this way. This is worth
noticing in general: fitting AR($p$) to a once-differenced series is *always* equivalent to fitting
a constrained AR($p+1$) to the original series, one with a built-in unit root. That equivalence is
exactly what an ARIMA($p,1,0$) model automates.

## The intercept is easy to lose

Refit the same AR(3) to the differenced series with **no intercept** (`trend='n'`):
$\hat\phi_1=0.2497,\ \hat\phi_2=0.0941,\ \hat\phi_3=0.2363$. The roots are still outside the unit
circle (moduli $1.30$ and $1.81$), so this fit is causal too — but the corresponding AR(4) for
$y_t$ now has *no* constant term, and forecasting with it produces a completely different
long-range picture: the with-intercept model's forecasts keep climbing, while the no-intercept
model's forecasts settle down and converge to a fixed level within a few dozen steps. One binary
choice — keep the intercept or drop it — changes the qualitative shape of every forecast beyond the
sample.

This matters because of a default that is easy to miss. Fitting `ARIMA(y, order=(3,1,0))` directly
to the *undifferenced* $y_t$ — the one-line alternative to differencing by hand and calling
`AutoReg` — reproduces the AR(3) **coefficients of the no-intercept fit exactly**, not the
with-intercept one. The reason: **`ARIMA` does not include an intercept term by default whenever
the differencing order $d \geq 1$.** If the intercept is wanted, it has to be requested explicitly
with `trend='t'`. Two calls that look like they should agree —
"difference then fit AR(3) with an intercept" versus "call `ARIMA` with $d=1$" — silently answer
different questions unless this is caught.

## Automatic order selection with AIC and BIC

Once $p,q$ (or $p,d,q$) are more than one or two candidates, comparing fits by eye stops being
practical, and the search is automated using two information criteria built from the maximized
log-likelihood $\hat\ell$ of each candidate fit:

$$
\mathrm{AIC} = -2\hat\ell + 2k, \qquad \mathrm{BIC} = -2\hat\ell + (\log n)\,k,
$$

where $k$ is the number of estimated parameters and $n$ the sample size. Both are minimized; both
penalize extra parameters, but BIC's penalty grows with $\log n$, so it penalizes complexity more
heavily than AIC once $n$ is reasonably large. Fitting ARMA(1,1) to a differenced log series from
earlier in the lecture gives log-likelihood $\hat\ell = 932.499$ with $n=313$ and $k=4$ parameters
(intercept, one AR coefficient, one MA coefficient, innovation variance), and indeed
$-2(932.499)+2(4) = -1857.0 = \mathrm{AIC}$ and $-2(932.499)+\log(313)\cdot4 = -1842.0 = \mathrm{BIC}$,
matching the values statsmodels reports directly.

Searching over all ARMA($p,q$) with $p,q \leq 5$ for that same differenced series, by both AIC and
BIC, lands on **AR(2)** as the best model overall. But a further, wider search directly on the
undifferenced log series, over all ARIMA($p,d,q$) with $p\leq5$, $d\leq2$, $q\leq5$ (using the
default, no-intercept `ARIMA` calls throughout), finds ARIMA(1,1,3) best by AIC and ARIMA(0,2,3)
best by BIC — and **both are worse (larger AIC/BIC) than the hand-fit AR(2)-with-intercept
model from the narrower search.** The wider, automated search never tried the model that actually
wins, because its default silently excludes the intercept once $d\geq1$. An automatic search is
only as good as the family of models it actually considers.

The same two lessons reappear, self-contained, on the TTLCONS series itself. Searching ARMA($p,q$)
for $p,q\leq5$ on $w_t = \Delta\log(\text{TTLCONS}_t)$ gives AR(5) best by AIC, AR(3) best by BIC,
and ARMA(1,1) best overall by both criteria. Searching the full ARIMA($p,d,q)$ grid directly on
$\log(\text{TTLCONS}_t)$ (again with the no-intercept default) gives **ARIMA(1,1,1)** as best by
both AIC ($-2405.5$) and BIC ($-2393.6$) — the two criteria agree this time. But adding an
intercept to that same ARIMA(1,1,1) (`trend='t'`) moves the AIC to $-2406.9$ (an improvement) while
moving the BIC to $-2391.0$ (worse): AIC is happy to pay for the extra parameter, BIC is not.
Neither criterion is "wrong" — they are answering slightly different questions about how much
complexity a fixed amount of data can support — but a search that reports a single winner hides
this disagreement unless both numbers are looked at.

## Double differencing and the risk of over-fitting the search

If the once-differenced series still shows visible structure, a second difference,
$w_t^{(2)} = \Delta^2 y_t = y_t - 2y_{t-1} + y_{t-2}$, is the next step. For TTLCONS its sample ACF
suggests a simple MA(1), which is fit directly on the original (log) series as
ARIMA(0,2,1) — a model of the form

$$
y_t - 2y_{t-1} + y_{t-2} = \epsilon_t + \theta\epsilon_{t-1},
$$

with no mean term at all (differencing twice removes it). The fitted $\hat\theta \approx -0.88$.

Searching ARMA($p,q$), $p,q\leq5$, on the twice-differenced series is numerically the least stable
part of the whole exercise — several candidate fits fail to converge, and one version of the code
rescales the data by $\times 100$ before fitting just to get sensible answers. Even so, the two
criteria disagree on the winner: AIC prefers a much richer ARMA(3,2), BIC prefers the same simple
MA(1)/MA(2) already suggested by the ACF. Fitting the AIC-preferred ARIMA(3,2,2) to the log series
gives coefficients most of which are far from statistically significant ($p$-values of $0.98$,
$0.97$, $0.11$, $0.80$ for four of its five AR/MA terms), and its forecasts turn out to be nearly
indistinguishable from the much simpler ARIMA(3,1,0) fit from earlier. AIC will sometimes accept
extra parameters that buy essentially nothing; checking the individual coefficient $p$-values, and
comparing forecasts rather than trusting the criterion number alone, catches this.

## Forecast horizon and model disagreement

A last, general observation from comparing all of these fitted models side by side: forecasts that
look dramatically different on a long horizon can look nearly identical on a short one. Plotting
100 months of forecasts (over 25 years, for a monthly series) from several "best" models — chosen
by different criteria, or with and without an intercept — shows them fanning out to very different
long-run levels. Restricting the same plot to the next 12 months shows the same models agreeing
closely. The visual drama of a long-range forecast plot is mostly the compounding of small
per-step differences, not necessarily evidence that one model fits the data much better than
another; short-horizon agreement is the more informative comparison when the models were all
selected on roughly the same evidence.

## Sources

- Berkeley STAT 153, Fall 2025, `CodeLectureTwentyTwo153248Fall2025` notebook:
  - [ACF and PACF of ARMA processes](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb)
    — the three cutoff facts and the `arma_acf`/`arma_pacf` demonstration.
  - [ARMA($p,q$) model fitting, AIC and BIC](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb)
    — the AIC/BIC formulas, the hand-checked ARMA(1,1) example, and the $p,q\leq5$ / $p,d,q$ grid
    searches on a differenced log series introduced earlier in this lecture as "the GNP dataset";
    that introduction (the notebook section immediately before this one) was not part of the
    material supplied for this chapter, so only the fitting and search steps that follow it are
    used here.
  - [ARIMA Models](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb)
    — the no-intercept-by-default trap, the full $(p,d,q)$ grid search on that same series, and the
    long- versus short-horizon forecast comparison.
  - [TTLCONS Dataset](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb)
    and [Other Models for TTLCONS](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb)
    — the self-contained TTLCONS grid searches (AR/MA/ARMA, then full $(p,d,q)$), the AIC-versus-BIC
    disagreement on the intercept for ARIMA(1,1,1), and the double-differenced MA(1)/ARIMA(0,2,1)
    model.
- Berkeley STAT 153, Spring 2025, `CodeLectureTwentyTwo153248Spring2025` notebook:
  - [AR(2)](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyTwo153248Spring2025.ipynb)
    — the reciprocal-root parametrization, the real- and complex-root simulations, the unit-root
    boundary case, and reading causality off `AutoReg`'s reported roots and moduli.
  - [ARIMA Modeling](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyTwo153248Spring2025.ipynb)
    — the full worked TTLCONS example: differencing, PACF-based identification of AR(3), the
    by-hand AR(3)-on-differences to AR(4)-on-levels conversion, the with/without-intercept
    comparison, the `AutoReg`-versus-`ARIMA` equivalence, the double-differenced MA(1) model, and
    the ARMA(3,2) grid-search result with its mostly-insignificant coefficients.

---

[← 59. Multiplicative Seasonal ARMA Models](59-multiplicative-seasonal-arma-models.md) · [Contents](index.md) · [61. Regression for Time Series Trends →](61-regression-for-time-series-trends.md)
