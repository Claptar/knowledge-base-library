---
title: "17. Fitting and Diagnosing ARIMA Models"
course: "Berkeley Stat 153 Fall 2024"
chapter: 17
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 17. Fitting and Diagnosing ARIMA Models

## What this covers

Every model so far in the course — AR, MA, ARMA — was fit to *stationary* data. Most series
worth forecasting are not stationary: GDP grows, sediment layers respond to a warming or cooling
climate, and neither has a fixed mean to revert to. This chapter asks how to extend ARMA to
nonstationary data by differencing, how to tell when a proposed differencing order is doing its
job, and how to choose and check a full ARIMA specification end to end. It assumes the reader
already has AR($p$), MA($q$) and ARMA($p,q$) models, the backshift operator $B$, stationarity, and
the idea of differencing a random walk to stationary white noise ($\nabla x_t = x_t - x_{t-1}$),
all from earlier lectures. Reading: Shumway and Stoffer, Ch. 3.

## From ARMA to ARIMA: absorbing a trend

A nonstationary series often decomposes as a trend plus stationary noise. Take

$$x_t = \mu_t + y_t, \qquad \mu_t = \beta_0 + \beta_1 t, \qquad y_t \text{ stationary.}$$

Differencing once,

$$\nabla x_t = x_t - x_{t-1} = \beta_1 + y_t - y_{t-1} = \beta_1 + \nabla y_t,$$

which is stationary: the deterministic linear trend has been converted into a constant, and the
stationary part is still stationary after differencing. This is the "I" in ARIMA — Autoregressive
**I**ntegrated Moving Average — and it says: difference first to kill the trend, then model what's
left with ARMA.

One difference does not always suffice. Suppose the trend is itself a random walk built from
another random walk:

$$\mu_t = \mu_{t-1} + v_t, \qquad v_t = v_{t-1} + e_t, \qquad e_t \text{ stationary.}$$

Differencing $x_t = \mu_t + y_t$ once gives $\nabla x_t = \nabla \mu_t + \nabla y_t = v_t + \nabla
y_t$, since $\nabla \mu_t = \mu_t - \mu_{t-1} = v_t$. Because $\nabla y_t$ is already stationary,
whether $\nabla x_t$ is stationary depends entirely on $v_t$. Unrolling the recursion for $v_t$
from an initial value $v_0$,

$$v_t = v_0 + \sum_{s=1}^{t} e_s,$$

which still depends on $t$ — it's itself a random walk, so $\nabla x_t$ is not stationary.
Differencing a second time,

$$\nabla^2 x_t = \nabla v_t + \nabla^2 y_t = e_t + \nabla^2 y_t,$$

and now both terms are stationary. The underlying trend here is a "random walk of a random walk,"
what's sometimes called $I(2)$: a stochastic trend built from two nested random walks needs two
differences to reduce to stationarity, exactly as a $k$th-order deterministic polynomial trend
$\mu_t = \sum_{j=0}^k \beta_j t^j$ needs $k$ differences ($\nabla^k x_t$).

**Definition.** A process is **ARIMA$(p,d,q)$** if $\nabla^d x_t = (1-B)^d x_t$ is ARMA$(p,q)$. In
operator form,

$$\phi(B)(1-B)^d x_t = \theta(B) w_t,$$

and if $E(\nabla^d x_t) = \mu \neq 0$, this is written with an explicit drift term,

$$\phi(B)(1-B)^d x_t = \delta + \theta(B) w_t, \qquad \delta = \mu(1 - \phi_1 - \cdots - \phi_p).$$

$\delta$ is exactly the mean-adjustment term familiar from ARMA, just applied to the differenced
series rather than the raw one: it is zero unless the differenced series itself has a nonzero
mean. This is the practical hook for a modeling choice made in both worked examples below — GDP's
differenced (quarter-over-quarter growth) series has a genuine positive drift, so its ARIMA(*,1,*)
fits included a linear-trend term; the varve series' first differences were fit with no such
drift term, because there was no reason to expect a nonzero mean growth in sediment thickness.

## How much differencing is enough?

It is rare that $d > 1$ is needed, and differencing is not free: **over-differencing manufactures
correlation that was never there.** Take the simplest possible case, a random walk
$x_t = x_{t-1} + w_t$. One difference gives exactly the driving white noise, $\nabla x_t = w_t$ —
already stationary, nothing left to model. Differencing again anyway gives

$$\nabla^2 x_t = \nabla x_t - \nabla x_{t-1} = w_t - w_{t-1},$$

an MA(1) with $\theta = -1$. This is stationary in the technical sense, but its moving-average
polynomial has a unit root, so it is **non-invertible** — it cannot be written as a (convergent)
autoregression in the past values, and standard ARMA fitting routines struggle with it. The moral:
check whether a difference actually removed nonstationarity before taking another one, rather than
differencing pre-emptively.

A second bookkeeping point: once a model is fit to $\nabla^d x_t$, the *forecasts* it produces are
forecasts of the differenced series, not of $x_t$ itself. Recovering a forecast for $x_t$ means
summing (integrating) the differenced forecasts back up — done already for a random walk in an
earlier lecture, and illustrated again below.

## Building an ARIMA model: the workflow

Putting AR, MA, differencing and diagnostics together, the recommended sequence for fitting any
ARIMA model is:

1. Plot the data.
2. Transform if needed (log transform for variance, differencing for trend).
3. Identify the dependence orders $p$ and $q$ by inspecting the ACF and PACF of the (differenced,
   transformed) series.
4. Estimate the parameters.
5. Run diagnostics on the residuals.
6. Choose among the candidate models.

Step 3 leans on the identification behavior established for pure AR and MA processes:

| | AR($p$) | MA($q$) | ARMA($p,q$) |
|---|---|---|---|
| ACF | tails off | cuts off after lag $q$ | tails off |
| PACF | cuts off after lag $p$ | tails off | tails off |

An ARMA process — and, after differencing, an ARIMA process — tails off in *both* the ACF and the
PACF, so identification from the correlogram alone is only ever a starting point for a **grid** of
candidate $(p,d,q)$ that is then compared on out-of-sample forecast error and residual diagnostics
(steps 4–6). Both worked examples below follow exactly this loop.

## Worked example: forecasting quarterly US real GDP

The GDP series (in logs) is neither stationary nor obviously a fixed low-order trend, so it makes
a good testbed for choosing $d$. The lecture fit a grid of specifications — AR-only ($d=0$,
$q=0$), ARMA ($d=0$, $q=1$), "ARI" (differencing with no MA term, $d=1$, $q=0$), ARIMA with one
difference ($d=1$, $q=1$), and ARIMA with two differences ($d=2$, $q=1$), each for $p=1,2,3$ — on
all data up to the last 20 quarters (5 years), forecast that held-out window, and scored each
model by RMSE against the actual held-out values. (For $d=0$ a constant intercept was included; for
$d=1$ a linear-drift term; for $d=2$ no deterministic term, since two differences already remove a
linear trend.)

**Full sample (including COVID).** The training window here includes the COVID-19 pandemic, during
which GDP's growth *rate* itself changed sharply and briefly — a nonstationarity in the trend
itself, not just in the level. A single difference removes a *constant* growth rate; it cannot
track a growth rate that jumps. Models with $d=2$ had a visible edge here, because a second
difference is more responsive to a rapidly moving local trend.

**Restricting to pre-COVID data.** Repeating the comparison on data truncated to 2019 shrinks that
advantage for $d=2$: with the COVID trend break removed from the training window, there is less
for the extra difference to track that a $d=1$ model could not also capture. The lecture notes
that some remaining gap between $d=1$ and $d=2$ might still be an artifact of the 2008 financial
crisis sitting in this window.

**Restricting further, to pre-2008 data.** Pushing the training window back to a stretch where
GDP's log-linear trend was comparatively stable tests that suspicion directly.

The general lesson drawn from all three fits is not "always difference twice" or "never difference
twice," but that **the right order of differencing is a property of the trend actually present in
the training window, not a fixed number to memorize.** A structural break (COVID, a financial
crisis) in the fitting period can make a higher difference order look better than it would on a
calmer stretch of the same series — which is exactly why step 1 of the workflow (plot the data,
and look at *which era* of it you are fitting) comes before any model is chosen. For series whose
trend evolves in more complex ways than a fixed differencing order can capture, the course flags
*state-space* methods, covered later, as the natural next tool.

## Worked example: glacial varve thickness

The second example, from Shumway and Stoffer (Example 2.8), is the thickness of yearly glacial
varves — sedimentary layers of sand and silt deposited by melting glaciers each spring — measured
at one Massachusetts site across 634 years, starting roughly 11,834 years ago. Because a warmer
year deposits more sand and silt, varve thickness is used as a proxy for paleoclimate.

The workflow again:

- **Plot the raw series.** The variance visibly changes over time — a sign that a variance-
  stabilizing transform, not just differencing, will be needed.
- **Check a QQ-plot.** The raw series deviates noticeably from the 45° reference line, confirming
  it is not close to normal/homoscedastic on its original scale.
- **Log-transform.** $y_t = \log(\text{thickness}_t)$ behaves much better on both the time plot and
  the QQ-plot.
- **Difference the log series** and re-examine the ACF/PACF of $\nabla y_t$ to identify candidate
  orders, using the tailing-off/cutting-off table above.

A grid of AR, MA, ARMA and ARIMA specifications was fit to the log-transformed series — pure AR
($p=1,2,3$; $d=q=0$), pure MA on the raw log series ($q=1,2,3$; $p=d=0$), MA fit after one
difference ($d=1$, $q=1,2,3$), ARMA ($p=1,2,3$, $q=1$, $d=0$), and ARI ($p=1,2,3$, $d=1$, $q=0$) —
scored by forecast RMSE against a held-out tail, exactly as for GDP. Three specifications were
carried forward for a closer look at forecasts and residual diagnostics: an MA(1) fit to the
undifferenced log series, ARIMA(0,1,1), and ARIMA(1,1,1).

## Checking residuals: the Ljung–Box statistic

`fit.plot_diagnostics()` gives a residual correlogram lag by lag, but reading it lag by lag can
hide a real problem: every single $\hat\rho_e(h)$ can sit just under the significance threshold
individually while the residuals are, taken together, still too autocorrelated to be white noise.
The **Ljung–Box–Pierce $Q$ statistic** tests the lags jointly:

$$Q = n(n+2)\sum_{h=1}^{H} \frac{\hat\rho_e^2(h)}{n-h},$$

where $n$ is the number of residuals, $h$ indexes the lag, and $H$ is the largest lag pooled over.
Under the null that the residuals are white noise, $Q$ is (approximately) $\chi^2$ with
$H - (p+q)$ degrees of freedom — the $p+q$ correction is why a fitted model's residual test needs
the model's own order as an input (`model_df=p+q` in the fitting call), and why the smallest lags
have no defined $p$-value at all: there aren't enough degrees of freedom yet to test them.

Run on the varve residuals, the contrast between two candidate models makes the point concrete.
For the ARIMA(0,1,1) fit ($p+q=1$, so the first $p$-value is defined at $h=2$):

| lag $h$ | 2 | 5 | 10 | 15 | 20 |
|---|---|---|---|---|---|
| $p$-value | 0.006 | 0.011 | 0.047 | 0.019 | 0.025 |

Every one of these is below 0.05: the null of white-noise residuals is rejected almost everywhere,
so an MA(1) term alone, after one difference, is not enough — there is autocorrelation left over
that the model isn't capturing.

For ARIMA(1,1,1) — adding a single AR term — ($p+q=2$, so the first $p$-value is defined at
$h=3$):

| lag $h$ | 3 | 5 | 10 | 15 | 20 |
|---|---|---|---|---|---|
| $p$-value | 0.24 | 0.67 | 0.63 | 0.35 | 0.36 |

None of these approach 0.05: the residuals are consistent with white noise at every lag tested.
Adding the AR(1) term is what actually clears up the leftover structure that the pure MA(1)-on-
differenced-data model left behind — a case where the correlogram and the joint test agree, and
where comparing two nested candidates side by side, rather than eyeballing one plot, is what
settles the choice.

The notes close with a full `summary()` printout for a fitted ARIMA specification, useful as a
worked example of everything such a table reports even though its order label, ARIMA(3,2,1), does
not match the (1,1,1) specification set immediately above it in the same code cell (most likely a
stale notebook output rather than a fourth model). Reading it as a template for what to check:

```
ar.L1    0.1414   (s.e. 0.053, p = 0.007)
ar.L2    0.1514   (s.e. 0.073, p = 0.038)
ar.L3   -0.0988   (s.e. 0.082, p = 0.226)
ma.L1   -0.9895   (s.e. 0.021, p < 0.001)
sigma2   0.0001

Ljung-Box (L1) (Q) = 0.17,  Prob(Q) = 0.68
Jarque-Bera (JB)   = 5608,  Prob(JB) = 0.00      (Skew 0.01, Kurtosis 24.4)
Heteroskedasticity (H) = 1.54, Prob(H) = 0.03
```

The point worth taking from this table regardless of which fit produced it: **passing the
Ljung–Box test is not the same as the residuals being well-behaved in every sense.** Here
Ljung–Box is comfortably non-significant (no leftover autocorrelation), yet the Jarque–Bera test
rejects normality overwhelmingly, driven by a kurtosis of 24.4 — badly heavy-tailed residuals.
An ARIMA model can be adequate for the autocorrelation structure it is built to capture while
still producing a poor set of prediction intervals, because those intervals typically assume
approximately normal residuals. Diagnostics should be read as a checklist, not a single pass/fail
gate.

## Sources

- `19_arima_time_lagged_reg_notes.md` — ARIMA definition, the linear-trend and $I(2)$ differencing
  derivations, the over-differencing/non-invertibility example, and the reading assignment
  (Shumway and Stoffer, Ch. 3).
- `Lecture19/02-fitting-the-model.md` — the six-step ARIMA workflow, the GDP model grid and the
  three-window (full sample / pre-COVID / pre-2008) comparison, and the pointer to state-space
  methods as a later topic. RMSE values and the two comparison figures (RMSE-vs-complexity;
  held-out forecasts with intervals) are in the original notebook but were not carried into the
  converted source, so are not reproduced numerically here.
- `Lecture19/03-one-more-example.md` — the glacial varve dataset (Shumway and Stoffer, Example
  2.8), the log-transform/QQ-plot diagnosis, the ACF/PACF identification table, and the varve
  model grid. Figures (raw and log series, QQ-plots, ACF/PACF panels, diagnostic plots) are in the
  original notebook but were not carried into the converted source.
- `Lecture19/04-ljung-box-p-values.md` — the Ljung–Box $Q$ statistic, the two residual $p$-value
  tables (condensed here to representative lags; the source gives all lags 1–20), and the closing
  `summary()` table, including the ARIMA(3,2,1)/(1,1,1) order mismatch noted above.
- No transcript, written notes or problem set were supplied for this lecture.

---

[← 16. Identifying ARMA Models via ACF/PACF](16-identifying-arma-models-via-acf-pacf.md) · [Contents](index.md) · [18. Time-Lagged Regression and the STRF →](18-time-lagged-regression-and-the-strf.md)
