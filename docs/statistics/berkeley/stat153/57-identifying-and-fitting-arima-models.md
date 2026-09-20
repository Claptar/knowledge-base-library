---
title: "57. Identifying and Fitting ARIMA Models"
course: "Berkeley Stat 153 Fall 2024"
chapter: 57
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 57. Identifying and Fitting ARIMA Models

## What this covers

This is a code lecture: instead of proving a new result, it walks through fitting MA, AR and
ARIMA models to real data in `statsmodels`, and reading the diagnostics that tell you which model
to try. It answers a practical question — given a time series, how do you decide whether an MA($q$),
an AR($p$), or a differenced ARIMA($p,d,q$) model is appropriate, fit it, and use it to forecast —
and along the way it surfaces two traps: how the intercept term is silently dropped once you
difference the data, and what happens when you fit a causal model to data that was not generated
causally. It assumes you already know the definitions of white noise, the MA($q$)/AR($p$)/ARMA($p,q$)
and ARIMA($p,d,q$) models, and the causality test via the roots of the characteristic polynomial
(a root of modulus $\le 1$ means the process is not causal). This chapter keeps the code and the
numbers from the lecture; the figures themselves are not reproduced, but every plot is described.

## The MA(1) model, and what its sign does to the data

Recall the MA(1) model,
$$
y_t = \mu + \epsilon_t + \theta\,\epsilon_{t-1}, \qquad \epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2).
$$
Setting $\theta = 0$ recovers plain i.i.d. Gaussian white noise, $N(\mu,\sigma^2)$ — so the i.i.d.
model is the special case of MA(1) with no dependence at all. Simulating $\epsilon_t$ and then
building $y_t = \epsilon_t + \theta\,\epsilon_{t-1}$ (with $\mu = 0$) makes the effect of $\theta$
visible directly in the trace: with $\theta = 0.8$ the series looks noticeably smoother than white
noise, because each $y_t$ shares an $\epsilon_{t-1}$ with its neighbor $y_{t-1}$, so *positive*
$\theta$ induces *positive* correlation between consecutive observations. With $\theta = -0.8$ the
same sharing produces *negative* correlation, and the series looks rougher than white noise —
it tends to zig-zag, since a large $y_{t-1}$ makes the next $y_t$ likely to be pulled the other way.
A scatter plot of $y_t$ against $y_{t-1}$ for $\theta = 0.8$ shows this positive dependence directly
as an upward-tilted cloud of points.

## The sample ACF: reading off the order of an MA model

The tool for detecting this kind of dependence from data is the **sample autocorrelation
function** (sample ACF). Given $y_1,\dots,y_n$ and a lag $h = 0,1,2,\dots$, define
$$
r_h := \frac{\sum_{t=1}^{n-h} (y_t - \bar y)(y_{t+h} - \bar y)}{\sum_{t=1}^{n} (y_t - \bar y)^2},
$$
where $\bar y$ is the sample mean. By construction $r_0 = 1$ always, so the spike at lag $0$
carries no information — only $h \ge 1$ matters. Coded directly,

```python
def sample_acf(y, h_max):
    n = len(y)
    y_mean = sum(y) / n
    denominator = sum((y_t - y_mean) ** 2 for y_t in y)
    autocorr = []
    for h in range(h_max + 1):
        numerator = sum((y[t] - y_mean) * (y[t + h] - y_mean) for t in range(n - h))
        autocorr.append(numerator / denominator)
    return autocorr
```

this matches `statsmodels.tsa.stattools.acf` value for value, and `statsmodels.graphics.tsaplots.plot_acf`
draws the same numbers as a stem plot with a shaded significance band. Run on the three simulated
series:

- **White noise** ($\theta = 0$): every $r_h$ for $h\ge 1$ is negligible — no spike stands out.
- **MA(1), $\theta = 0.8$**: a clear spike at lag 1, and nothing beyond it.
- **MA(1), $\theta = -0.8$**: the same, but the spike at lag 1 is negative.

That single spike at lag 1, with everything past it negligible, is the diagnostic signature of
MA(1); this is what lets you read the order $q$ of an MA model off a plot before fitting anything.

## Example: glacial varves

The varve dataset (Shumway & Stoffer, 4th ed., Example 2.6) records the thickness of $634$
annual glacial varves — sediment layers deposited by glacial meltwater — from a site in
Massachusetts, spanning a period starting about $11{,}834$ years ago as the last Ice Age glaciers
retreated. Thicker varves mean warmer years with more melt; thinner ones mean colder years. The
raw series is worked with on the **log** scale (`ylog = np.log(yraw)`), and even the log series
does not have a constant mean, so an MA($q$) model — which assumes stationarity — is not directly
appropriate. Differencing once, `ylogdiff = np.diff(ylog)`, removes the drifting mean.

The sample ACF of the differenced log series shows exactly one non-negligible spike, at lag 1,
and it is **negative**. That is the MA(1) signature (with negative $\theta$), so MA(1) is the
model to try.

## Fitting MA models with the ARIMA function

Fitting an MA model is harder computationally than fitting an AR model (there is no simple
regression trick), so the course uses `statsmodels`'s `ARIMA` function, which is specified by three
orders $(p,d,q)$: $p$ is the AR order, $q$ the MA order, and $d$ the number of times the series is
differenced before an ARMA($p,q$) model is fit to what remains. MA(1) is $(p,d,q) = (0,0,1)$:

```python
mamod = ARIMA(ylogdiff, order=(0, 0, 1)).fit()
```

gives $\hat\mu = -0.0013$, $\hat\theta = -0.7710$, $\hat\sigma = 0.4851$. The same model can be
fit directly to the (undifferenced) log data by moving the differencing into the ARIMA order,
$(p,d,q) = (0,1,1)$:

```python
mamod_ylog = ARIMA(ylog, order=(0, 1, 1)).fit()
```

which gives essentially the same $\hat\theta = -0.7705$ — but **with no intercept at all**. This
is a general rule worth holding onto: *`ARIMA` does not fit a constant term by default once the
differencing order $d$ is strictly positive.* Concretely, for $d \ge 1$ it fits
$y_t = \epsilon_t + \theta\,\epsilon_{t-1}$ (or the AR/ARMA analogue) with $\mu$ pinned at $0$,
rather than estimating a mean for the differenced series. It matters, and it resurfaces below.

## The MA(2) model and why its ACF has a cutoff

The MA(2) model is $y_t = \mu + \epsilon_t + \theta_1\epsilon_{t-1} + \theta_2\epsilon_{t-2}$.
Because $y_t$ depends on only three consecutive noise terms $\epsilon_t,\epsilon_{t-1},\epsilon_{t-2}$,
once the lag $h$ exceeds $2$, $y_t$ and $y_{t+h}$ share no common $\epsilon$ at all and — since the
$\epsilon$'s are independent — their covariance is exactly zero. So the *theoretical* ACF of an
MA(2) process is nonzero only at lags $0,1,2$ and identically zero afterward. Computing it for
$\theta_1=\theta_2=0.2$ (`arma_acf`) gives
$$
\rho_0 = 1,\qquad \rho_1 \approx 0.222,\qquad \rho_2 \approx 0.185,\qquad \rho_h = 0 \ (h\ge 3).
$$

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Theoretical autocorrelation of an MA(2) process, nonzero only at lags 0, 1 and 2">
  <line x1="40" y1="170" x2="325" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="170" x2="40" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <text x="182" y="192" text-anchor="middle" font-size="12" fill="currentColor">lag h</text>
  <text x="18" y="100" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 18 100)">ACF</text>
  <g stroke="currentColor" stroke-width="2">
    <line x1="40" y1="170" x2="40" y2="40"/>
    <line x1="75" y1="170" x2="75" y2="141"/>
    <line x1="110" y1="170" x2="110" y2="146"/>
    <line x1="145" y1="170" x2="145" y2="170"/>
    <line x1="180" y1="170" x2="180" y2="170"/>
    <line x1="215" y1="170" x2="215" y2="170"/>
    <line x1="250" y1="170" x2="250" y2="170"/>
    <line x1="285" y1="170" x2="285" y2="170"/>
  </g>
  <g fill="currentColor">
    <circle cx="40" cy="40" r="3"/>
    <circle cx="75" cy="141" r="3"/>
    <circle cx="110" cy="146" r="3"/>
    <circle cx="145" cy="170" r="3"/>
    <circle cx="180" cy="170" r="3"/>
    <circle cx="215" cy="170" r="3"/>
    <circle cx="250" cy="170" r="3"/>
    <circle cx="285" cy="170" r="3"/>
  </g>
  <text x="40" y="185" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="75" y="185" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="110" y="185" text-anchor="middle" font-size="11" fill="currentColor">2</text>
  <text x="145" y="185" text-anchor="middle" font-size="11" fill="currentColor">3</text>
  <text x="180" y="185" text-anchor="middle" font-size="11" fill="currentColor">4</text>
</svg>
<figcaption>Theoretical ACF of MA(2) with &#952;&#8321;=&#952;&#8322;=0.2: spikes at lags 0-2, exactly
zero beyond — the pattern the sample ACF is checked against to read off q.</figcaption>
</figure>

Simulating $500$ points from this MA(2) model and computing its *sample* ACF gives a noisy version
of exactly this picture: nonzero-looking bars at lags 1 and 2, and negligible ones after. This is
the general identification principle for moving-average models: **an MA($q$) process has zero
autocorrelation beyond lag $q$**, so the largest lag at which the sample ACF still shows a
non-negligible spike is a direct estimate of $q$.

## Example: GDP growth rate

The second real dataset is the U.S. GDP growth rate (from FRED). Quarterly nominal GDP is
log-transformed and differenced, `ylogdiff = np.diff(np.log(y)) * 100` (the growth rate as a
percentage), and its sample ACF shows two spikes sticking out, at lags 1 and 2 — indicating MA(2)
rather than MA(1). Fitting with `ARIMA(ylogdiff, order=(0,0,2))` gives
$$
\hat\mu = 1.5418,\qquad \hat\theta_1 = 0.1893,\qquad \hat\theta_2 = 0.2232,\qquad \hat\sigma^2 = 1.4628.
$$
A practical wrinkle worth keeping: fitting MA models this way is numerically delicate. Applying
the same `ARIMA(order=(0,0,2))` call directly to `np.diff(np.log(y))` (without the $\times 100$
rescaling) can produce a non-convergence warning from the optimizer; multiplying the series by
$100$ before fitting made the warning go away. Scaling the data changes nothing about the model,
only the numerical conditioning of the likelihood surface the optimizer has to climb.

## The sample PACF: reading off the order of an AR model

The analogous diagnostic for AR models is the **sample partial autocorrelation function** (sample
PACF). At lag $p$, the sample PACF is simply the estimated coefficient $\hat\phi_p$ obtained by
fitting an AR($p$) model to the data — computed by fitting AR models of increasing order and
reading off the *last* coefficient each time:

```python
def sample_pacf(y, p_max):
    pautocorr = []
    for p in range(1, p_max + 1):
        armd = AutoReg(y, lags=p).fit()
        pautocorr.append(armd.params[-1])
    return pautocorr
```

This matches `statsmodels.tsa.stattools.pacf(y, method='ols')` exactly. (Why fitting AR($p$)
models this way produces something with "partial autocorrelation" in its name was discussed
earlier in lecture, not in this notebook, and is revisited in lab — it is not reconstructed here.)
The `plot_pacf` convenience function draws the same values as a stem plot, additionally showing
the value $1$ at lag $0$ and a shaded band for assessing which spikes are negligible.

## AR and MA representations of the same data

Fitting the sample PACF of the GDP growth series and reading off where it becomes negligible
suggests $p = 2$ — the same series that MA(2) was fit to above. Fitting
`AutoReg(ylogdiff, lags=2)` gives the AR(2) model
$$
x_t = 0.9099 + 0.2100\,x_{t-1} + 0.2010\,x_{t-2} + \delta_t, \qquad \delta_t \overset{\text{i.i.d.}}{\sim} N(0, 1.207^2),
$$
with characteristic roots of modulus $1.7686$ and $2.8136$ — both outside the unit circle, so the
fit is causal and stationary. Since the same data was also fit with the MA(2) model
$$
x_t = 1.5418 + \epsilon_t + 0.1893\,\epsilon_{t-1} + 0.2232\,\epsilon_{t-2}, \qquad \epsilon_t \overset{\text{i.i.d.}}{\sim} N(0, 1.4628),
$$
it is natural to ask whether these two very different-looking equations are actually saying
something similar about the data. They are, and it can be checked in two ways.

**The means agree.** The MA(2) mean is visibly $1.5418$. For the AR(2) model, take expectations
on both sides — stationarity means $x_t, x_{t-1}, x_{t-2}$ all share the same mean $\mu$, and
$\delta_t$ has mean zero — giving
$$
\mu = 0.9099 + 0.21\mu + 0.201\mu \;\implies\; \mu = \frac{0.9099}{1 - 0.21 - 0.201} = 1.5446.
$$
$1.5446$ against $1.5418$: essentially the same mean, recovered two completely different ways.

**The autocovariances agree.** Using `arma_acovf` to compute $\gamma(h)$ for both fitted models
and overlaying them shows the two curves tracking each other closely at every lag. An AR(2) and an
MA(2), fit independently to the same data, turn out to describe almost the same second-order
behavior — a reminder that the AR and MA families overlap in what they can represent, and that
"which model is right" is often better read as "which model is a convenient description" here.

## The Box-Jenkins workflow, worked in full: TTLCONS

The **Box-Jenkins philosophy** is: difference a nonstationary series until what is left looks
stationary, identify a causal, stationary ARMA($p,q$) model for the differenced series using the
sample ACF/PACF, fit it, and use it to forecast — converting back to the original scale at the end.
The lecture works this all the way through on monthly total construction spending in the US
(TTLCONS, log scale, $391$ months from 1993).

The log series clearly trends, so a stationary model is not appropriate for it directly. Once
differenced, `ydiff = np.diff(y)`, the sample PACF is negligible past lag 3, suggesting AR(3).
Fitting `AutoReg(ydiff, lags=3)` gives
$$
y_t - y_{t-1} = 0.0019 + 0.2221\,(y_{t-1}-y_{t-2}) + 0.0644\,(y_{t-2}-y_{t-3}) + 0.2077\,(y_{t-3}-y_{t-4}) + \epsilon_t
$$
(the middle coefficient is not significant at conventional levels, $p = 0.201$), and the fitted
model's characteristic roots all have modulus above $1$, confirming it is a causal, stationary
model **for the differenced series.**

### Converting back to the original scale

To forecast $y_t$ itself, rearrange the differenced equation:
$$
y_t = \hat\phi_0 + (1+\hat\phi_1)\,y_{t-1} + (\hat\phi_2-\hat\phi_1)\,y_{t-2} + (\hat\phi_3-\hat\phi_2)\,y_{t-3} - \hat\phi_3\,y_{t-4} + \epsilon_t,
$$
an AR(4) model for the *original* (undifferenced) $y_t$, with coefficients
$a_1 = 1.2221,\ a_2=-0.1577,\ a_3=0.1433,\ a_4=-0.2077$. Checking its characteristic roots gives
moduli $1.0000,\ 0.7166,\ 0.5384,\ 0.5384$ — **one root sits exactly on the unit circle**, so this
AR(4) model for the original series is *not* stationary. That is exactly as it should be: the
whole point of differencing was that the original series is not stationary, and converting the
fitted model back to the original scale reproduces that non-stationarity as a literal unit root.
Predictions are still made in the ordinary way, by iterating the AR(4) recursion forward from the
end of the data for $k=100$ steps and exponentiating back to the original (non-logged) scale.

### The intercept is a drift term, and it matters

Refitting the differenced AR(3) model **without** an intercept (`AutoReg(ydiff, lags=3, trend='n')`)
gives similar AR coefficients ($0.2542,\ 0.0923,\ 0.2400$, still causal and stationary) but converts
to an AR(4) model for $y_t$ with **no additive constant at all**. Iterating this no-intercept
model forward, the $100$-step-ahead forecasts converge to a fixed value ($\approx 14.5706$ on the
log scale) and flatten out completely. Iterating the with-intercept model instead, the forecasts
keep climbing steadily for the full $100$ steps. This is the same distinction as a random walk
with versus without drift: once the differenced series has a unit root, a nonzero intercept in the
differenced model becomes a linear **drift** in the level forecasts, while dropping it leaves the
long-run forecast pinned to a constant. The two forecasts end up "quite different" — the lecture's
own words — purely because of whether that one constant term was included.

### Fitting directly with ARIMA, and double differencing

The same AR(3)-on-differenced-data model can be fit directly to the *original* series with
`ARIMA(y, order=(3, 1, 0))` — no manual differencing or back-conversion needed. Consistent with
the earlier rule, `ARIMA` does not include an intercept when $d \ge 1$, so its fitted coefficients
match the **no-intercept** `AutoReg` case exactly, and `get_prediction()` reproduces the same
forecast automatically (already on the $y_t$ scale, with no manual conversion required).

The once-differenced series `ydiff` still shows some residual trend-like behavior, so the lecture
differences a second time, `ydiff2 = np.diff(np.diff(y))`. Its sample ACF/PACF suggest a simple
MA(1) is enough for this twice-differenced series. Rather than fit that by hand, `ARIMA(y, order=(0,2,1))`
fits it directly to the original series:
$$
y_t - 2y_{t-1} + y_{t-2} = \epsilon_t + \theta\,\epsilon_{t-1}, \qquad \hat\theta = -0.8730,
$$
again with no $\mu$ term (as expected for $d \ge 1$). Plotting all three forecasts together — AR(3)
with intercept, AR(3) without intercept (equivalently ARIMA$(3,1,0)$), and MA(1) on the
twice-differenced data (ARIMA$(0,2,1)$) — shows genuinely different long-run behavior from three
models that all looked like reasonable choices from the diagnostics. The moral the lecture draws
explicitly: models chosen this way can give predictions that "behave quite differently," and the
choice of $d$, of whether to include an intercept, and of $(p,q)$ all matter for what the forecast
looks like far from the data.

## A trap: fitting a causal model to non-causal data

Recall that for the AR(1) model $y_t = \phi_1 y_{t-1} + \delta_t$, the characteristic polynomial
$1-\phi_1 z$ has its root at $z = 1/\phi_1$, and causality requires that root to lie **outside**
the unit circle, i.e. $|\phi_1| < 1$. When $|\phi_1| > 1$ instead, the usual forward recursion
does not converge, but there is still a unique stationary — non-causal — solution, expressed in
terms of *future* noise:
$$
y_t = \mu - \sum_{j=1}^{\infty} \frac{\epsilon_{t+j}}{\phi_1^{\,j}}.
$$
It can be simulated, but only by working *backward*: fix a value at the end of the series (built
from a truncated version of the infinite sum) and recurse $t = n, n-1, \dots, 1$ using
$y_{t-1} = y_t/\phi_1 - \mu(1-\phi_1)/\phi_1 - \epsilon_t/\phi_1$, since attempting the usual
forward recursion for $|\phi_1|>1$ blows up numerically.

The lecture simulates $n=2000$ points this way with the true values $\phi_1 = 2$, $\mu = 10$,
$\sigma = 3$ (so $\sigma^2 = 9$), then fits an ordinary `ARIMA(y, order=(1,0,0))` to the resulting
series. The fit reports $\hat\phi_1 = 0.4581$ and $\hat\sigma^2 = 2.2268$ — nowhere near the true
$\phi_1 = 2$ or $\sigma^2 = 9$. The reason is built into the fitting procedure itself:
`ARIMA`'s parameter transform enforces stationarity by construction (`enforce_stationarity=True`
is the default), so the search is restricted to AR coefficients with $|\phi| < 1$ from the start.
Data generated by a non-causal model can still be fit — the process is stationary, just not by the
recursion the fitted model assumes — but the optimizer can only ever return some point in the
causal region, never the true $\phi_1 = 2$. (It is worth noticing that the numbers it lands on are
suggestively close to $1/\phi_1 = 0.5$ and $\sigma^2/\phi_1^2 = 2.25$, though the lecture does not
pursue why.)

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="The characteristic root of the true model sits inside the unit circle; the fitted model's root is forced outside it">
  <circle cx="140" cy="110" r="55" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="80" y1="110" x2="200" y2="110" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="140" y1="50" x2="140" y2="170" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <circle cx="167.5" cy="110" r="4" fill="currentColor"/>
  <text x="167.5" y="130" text-anchor="middle" font-size="11" fill="currentColor">z=0.5</text>
  <text x="167.5" y="144" text-anchor="middle" font-size="11" fill="currentColor">(true, non-causal)</text>
  <circle cx="260" cy="110" r="4" fill="currentColor"/>
  <text x="260" y="94" text-anchor="middle" font-size="11" fill="currentColor">z&#8776;2.18</text>
  <text x="260" y="80" text-anchor="middle" font-size="11" fill="currentColor">(fitted, causal)</text>
  <text x="140" y="42" text-anchor="middle" font-size="11" fill="currentColor">unit circle</text>
</svg>
<figcaption>Root z = 1/&#966;&#8321; of the AR(1) characteristic polynomial: the true generating
model has its root at 0.5, inside the unit circle (non-causal); an estimator that enforces
causality can only return a root outside it, landing on a different process entirely.</figcaption>
</figure>

## Sources

- Berkeley STAT 153, Code Lecture 21 ("Moving Average Models" / "ACF, PACF, AR models and
  Stationarity"), two taught instances:
  - Fall 2025 (`CodeLectureTwentyOne153248Fall2025.ipynb`):
    [`01-introduction.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) —
    MA(1) simulation and the effect of the sign of $\theta$.
    [`02-sample-acf.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) —
    the sample ACF, its manual computation, and comparison with `statsmodels`.
    [`03-varve-dataset.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) —
    the glacial varve example (data description credited there to Shumway & Stoffer, Example 2.6,
    4th ed. — that book is referred to but not itself part of the supplied material).
    [`04-fitting-ma-models-using-the-arima-function.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) —
    the `ARIMA(p,d,q)` fitting interface and the no-intercept-when-$d\ge1$ rule.
    [`05-ma-2-model.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) —
    the theoretical ACF of MA(2) and its cutoff.
    [`06-gdp-growth-rate-data.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) —
    the GDP growth rate example and the numerical-convergence note.
    [`07-ar-models.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) —
    the AR(2) fit to the same GDP data and its comparison with the MA(2) fit (mean and
    autocovariance agreement).
    [`08-arima-modeling.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) —
    the full Box-Jenkins workflow on the TTLCONS dataset: identification, fitting, the AR(4)
    conversion back to the original scale, the intercept/drift comparison, direct `ARIMA` fitting,
    and double differencing.
  - Spring 2025 (`CodeLectureTwentyOne153248Spring2025.ipynb`):
    [`01-sample-pacf.md`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyOne153248Spring2025.ipynb) —
    the definition and manual computation of the sample PACF (used here in preference to the
    thinner fall-2025 treatment of the same tool), including the note that the "partial
    autocorrelation" naming was explained in an earlier, unsupplied part of the lecture. This file
    also contains a full `help(ARIMA)` docstring dump, from which only the `enforce_stationarity`
    default is used below; the rest is library reference material, not lecture content, and is
    omitted here.
    [`02-ar-1-with.md`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyOne153248Spring2025.ipynb) —
    the non-causal AR(1) simulation and the causal-fit mismatch.

---

[← 56. Model Fitting via PyTorch](56-model-fitting-via-pytorch.md) · [Contents](index.md) · [58. LSTM Networks for Forecasting →](58-lstm-networks-for-forecasting.md)
