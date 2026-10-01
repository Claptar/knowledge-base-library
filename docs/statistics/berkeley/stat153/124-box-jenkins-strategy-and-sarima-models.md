---
title: "124. Box-Jenkins Strategy and SARIMA Models"
course: "Berkeley Stat 153"
chapter: 124
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 124. Box-Jenkins Strategy and SARIMA Models

## What this covers

This chapter covers the Box-Jenkins strategy for fitting ARMA models to real time series that show
trend and/or seasonality: preprocess by differencing until the series looks stationary, then fit an
ARMA model to what remains. It builds up the resulting model families — ARIMA, seasonal ARMA,
multiplicative seasonal ARMA, and SARIMA — and closes with a worked look at why estimating even the
simplest of these models (MA(1)) is genuinely harder than the least-squares fitting used for AR
models. It assumes the reader already has the ARMA$(p,q)$ model, the backshift operator $B$,
causality and stationarity, and the ACF/PACF.

## Recap: the ARMA(p, q) model

The $\text{ARMA}(p,q)$ model is
$$(y_t-\mu) - \phi_1(y_{t-1}-\mu) - \cdots - \phi_p(y_{t-p}-\mu) = \epsilon_t + \theta_1\epsilon_{t-1}+\cdots+\theta_q \epsilon_{t-q},$$
with $\epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2)$. In backshift notation,
$$\phi(B)(y_t-\mu) = \theta(B)\epsilon_t, \qquad \phi(z) = 1-\phi_1 z - \cdots - \phi_p z^p,\quad \theta(z)=1+\theta_1 z + \cdots +\theta_q z^q.$$
Writing the intercept explicitly instead of centering the series, this is the same as $\phi(B) y_t = \delta + \theta(B)\epsilon_t$.

Formally solving for $y_t$ gives $y_t - \mu = \dfrac{\theta(B)}{\phi(B)}\epsilon_t$. To make sense of
dividing by a polynomial in $B$, factor $\phi(z) = (1-a_1z)\cdots(1-a_pz)$, where $1/a_1,\dots,1/a_p$
are the roots of $\phi$. Each factor $(1-a_kB)^{-1}$ can be expanded either as $\sum_{j\ge0} a_k^j
B^j$ (if $|a_k|<1$) or as $-\sum_{j\ge1} a_k^{-j}B^{-j}$ (if $|a_k|>1$). When every $|a_k|<1$ —
equivalently, every root of $\phi(z)$ has modulus strictly greater than one — the first expansion
applies to every factor and $y_t = \mu + \sum_{j\ge0}\psi_j \epsilon_{t-j}$ for some coefficients
$\psi_j$: a causal stationary process. This is the only regime used from here on.

ARMA is strictly more flexible than pure AR or pure MA, and that flexibility costs the clean
diagnostic the pure models have: for AR$(p)$ the theoretical PACF vanishes past lag $p$, and for
MA$(q)$ the theoretical ACF vanishes past lag $q$, but for a genuine ARMA$(p,q)$ with $p,q\ge 1$
typically *neither* cuts off. So $p$ and $q$ cannot generally be read straight off an ACF/PACF plot
the way they can for a pure AR or MA model; in practice one searches over a grid of $(p,q)$ values
and picks whichever pair a model-selection criterion such as AIC, BIC, or cross-validation favors.

## The Box-Jenkins strategy: detrend, then model

Box and Jenkins popularized a two-step strategy for modeling an observed series $y_1,\dots,y_n$:

1. Preprocess $y_1,\dots,y_n$ — which typically shows some kind of trend — into a transformed
   series $x_t$ with no discernible trend.
2. Fit an ARMA$(p,q)$ model, for appropriate $p,q$, to $x_t$.

Step 1 is usually done by one or both of the following two operations.

**Differencing.** The first difference of $\{y_t\}$ is $\nabla y_t := y_t - y_{t-1}$, for
$t=2,\dots,n$. The second difference is
$$\nabla^2 y_t = \nabla(\nabla y_t) = \nabla y_t - \nabla y_{t-1} = y_t - 2y_{t-1}+y_{t-2},$$
and higher-order differences $\nabla^k y_t$ are defined recursively. Each difference shortens the
series by one: $\nabla y_t$ has length $n-1$, $\nabla^2 y_t$ has length $n-2$, and so on.
Differencing removes increasing/decreasing trends, and one or two orders are usually enough.

**Seasonal differencing.** This removes seasonal trends of period $s$ (for example $s=12$ for
monthly data). The seasonal first difference is
$$\nabla_s y_t := y_t - y_{t-s},$$
a series of length $n-s$, and the seasonal second difference is $\nabla_s^2 y_t = \nabla_s(\nabla_s
y_t) = y_t - 2y_{t-s}+y_{t-2s}$, with higher orders again defined recursively. When a series carries
both a seasonal trend and a linear one, the usual order is to take a seasonal difference first —
this often removes the seasonality and sometimes the linear trend along with it — and then, if a
linear trend still persists, take a further regular difference of the seasonally-differenced series.

Once $x_t$ looks trend-free, fitting the ARMA$(p,q)$ model — with $p,q$ chosen by AIC/BIC — can be
done directly with the `ARIMA` function from `statsmodels`.

## ARIMA: folding the differencing into the model

Rather than differencing by hand and then fitting ARMA as a separate step, the two can be folded
into a single model. **ARIMA** stands for AutoRegressive Integrated Moving Average — "integrated"
because differencing is, informally, the inverse of summing (integration). Formally:

*A time series $y_t$ is $\text{ARIMA}(p,d,q)$ if*
$$\phi(B)\big((\nabla^d y_t)-\mu\big) = \theta(B)\epsilon_t,$$
*with $\epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2)$.*

So an ARIMA model is exactly an ARMA$(p,q)$ model fit to the $d$-th difference of $y_t$. It is fit
with the same `ARIMA()` function in `statsmodels`; the mean $\mu$ defaults to zero once $d>0$
(differencing already removes a constant level).

## Seasonal ARMA models

Differencing handles trend and seasonality in the mean, but a series can also carry seasonal
*dependence* — correlation concentrated at multiples of the period $s$ — that a plain ARMA model
does not target. A **seasonal ARMA$(P,Q)$ process with period $s$** satisfies
$$\Phi(B^s)(y_t-\mu) = \Theta(B^s)\epsilon_t, \qquad \epsilon_t\overset{\text{i.i.d.}}{\sim}N(0,\sigma^2),$$
where
$$\Phi(B^s) = 1-\Phi_1B^s-\Phi_2B^{2s}-\cdots-\Phi_PB^{Ps}, \qquad \Theta(B^s)=1+\Theta_1B^s+\cdots+\Theta_QB^{Qs}.$$

This is a special case of an ordinary $\text{ARMA}(Ps,Qs)$ model — every $\Phi_iB^{is}$ is also a
polynomial in $B$ — but a much sparser one: the seasonal model has $P+Q+1$ parameters (the $+1$ for
$\sigma^2$), against $Ps+Qs+1$ for the unrestricted $\text{ARMA}(Ps,Qs)$. A causal stationary
solution exists exactly when every root of $\Phi(z^s)$ — equivalently, every root of $\Phi(z)$ — has
modulus strictly greater than one.

The payoff of the restriction shows up in the ACF and PACF: for a seasonal ARMA model they are
**zero except at the seasonal lags** $h=0,s,2s,3s,\dots$, and at those lags they behave exactly as
the ACF/PACF of the corresponding unseasonal model $\Phi(B)X_t=\Theta(B)\epsilon_t$ would at lags
$0,1,2,3,\dots$.

## Multiplicative seasonal ARMA models

A seasonal ARMA model on its own only produces correlation *at* the seasonal lags — it cannot also
produce the short-range correlation an ordinary ARMA model would give at the nearby non-seasonal
lags. Combining the two by multiplication fixes that.

The motivating example is the `co2` dataset (from the time series textbook by Cryer and Chan): after
taking a first difference and a seasonal difference of period 12, the sample ACF is non-negligible
only at lags $0,1,11,12,13$. An $\text{MA}(13)$ model can produce exactly that shape, but at the
cost of 14 parameters — likely overfitting. A far more parsimonious model multiplies an
$\text{MA}(1)$ factor by a seasonal $\text{MA}(1)$ factor of period 12:
$$y_t = (1+\Theta B^{12})(1+\theta B)\epsilon_t = \epsilon_t + \theta\epsilon_{t-1}+\Theta\epsilon_{t-12}+\theta\Theta\epsilon_{t-13}.$$
This model has only two MA parameters (plus $\sigma^2$), and its autocorrelation function is
$$\rho(1)=\frac{\theta}{1+\theta^2}, \qquad \rho(12)=\frac{\Theta}{1+\Theta^2}, \qquad \rho(11)=\rho(13)=\frac{\theta\Theta}{(1+\theta^2)(1+\Theta^2)},$$
and zero at every other positive lag — matching the shape seen in the data, with three parameters
in place of fourteen.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Sample ACF of the differenced co2 series, non-negligible only at lags 0, 1, 11, 12, 13">
  <line x1="40" y1="185" x2="320" y2="185" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="30" x2="40" y2="185" stroke="currentColor" stroke-width="1"/>
  <g stroke="currentColor" stroke-width="2" fill="currentColor">
    <line x1="40" y1="185" x2="40" y2="35"/><circle cx="40" cy="35" r="3"/>
    <line x1="60" y1="185" x2="60" y2="130"/><circle cx="60" cy="130" r="3"/>
    <line x1="80" y1="185" x2="80" y2="177"/><circle cx="80" cy="177" r="2"/>
    <line x1="100" y1="185" x2="100" y2="177"/><circle cx="100" cy="177" r="2"/>
    <line x1="120" y1="185" x2="120" y2="177"/><circle cx="120" cy="177" r="2"/>
    <line x1="140" y1="185" x2="140" y2="177"/><circle cx="140" cy="177" r="2"/>
    <line x1="160" y1="185" x2="160" y2="177"/><circle cx="160" cy="177" r="2"/>
    <line x1="180" y1="185" x2="180" y2="177"/><circle cx="180" cy="177" r="2"/>
    <line x1="200" y1="185" x2="200" y2="177"/><circle cx="200" cy="177" r="2"/>
    <line x1="220" y1="185" x2="220" y2="177"/><circle cx="220" cy="177" r="2"/>
    <line x1="240" y1="185" x2="240" y2="177"/><circle cx="240" cy="177" r="2"/>
    <line x1="260" y1="185" x2="260" y2="145"/><circle cx="260" cy="145" r="3"/>
    <line x1="280" y1="185" x2="280" y2="120"/><circle cx="280" cy="120" r="3"/>
    <line x1="300" y1="185" x2="300" y2="145"/><circle cx="300" cy="145" r="3"/>
    <line x1="320" y1="185" x2="320" y2="177"/><circle cx="320" cy="177" r="2"/>
  </g>
  <text x="40" y="200" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="60" y="200" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="260" y="200" text-anchor="middle" font-size="11" fill="currentColor">11</text>
  <text x="280" y="200" text-anchor="middle" font-size="11" fill="currentColor">12</text>
  <text x="300" y="200" text-anchor="middle" font-size="11" fill="currentColor">13</text>
  <text x="180" y="214" text-anchor="middle" font-size="12" fill="currentColor">lag h</text>
</svg>
<figcaption>Sample ACF of the first- and seasonally-differenced co2 series: only lags 0, 1, 11, 12,
and 13 stand out. This is exactly the shape produced by an MA(1) times a seasonal MA(1) of period
12 — three parameters instead of the fourteen an MA(13) would need.</figcaption>
</figure>

In general, ARMA and seasonal ARMA factors can be multiplied together to build models with special
autocorrelation structure at seasonal lags. The **multiplicative seasonal ARMA model**
$\text{ARMA}(p,q)\times(P,Q)_s$ is defined by
$$\Phi(B^s)\phi(B)(y_t-\mu) = \Theta(B^s)\theta(B)\epsilon_t.$$
The `co2` model above is $\text{ARMA}(0,1)\times(0,1)_{12}$.

A second example, mixing an MA factor with a seasonal *AR* factor, is $\text{ARMA}(0,1)\times
(1,0)_{12}$ (equivalently $\text{MA}(1)\times\text{AR}(1)_{12}$):
$$(y_t-\mu)-\Phi(y_{t-12}-\mu) = \epsilon_t+\theta\epsilon_{t-1}.$$
Its ACF is $\rho(12h)=\Phi^h$ for $h\ge0$, and
$$\rho(12h-1)=\rho(12h+1) = \frac{\theta}{1+\theta^2}\Phi^h, \qquad h=0,1,2,\dots,$$
with $\rho(h)=0$ at every other lag. Whenever a dataset's ACF/PACF show a pattern concentrated at
and around seasonal lags, a multiplicative seasonal ARMA model is worth trying; `statsmodels`'s
`arma_acf` and `arma_pacf` functions compute the theoretical ACF/PACF of a candidate model directly,
which is how formulas like the two above would be checked in practice.

## SARIMA models: differencing plus multiplicative seasonal ARMA

Combining differencing with a multiplicative seasonal ARMA model gives the full **SARIMA** family,
written $\text{ARIMA}(p,d,q)\times(P,D,Q)_s$: difference $d$ times, seasonally difference $D$ times
with period $s$, and fit a multiplicative seasonal $\text{ARMA}(p,q)\times(P,Q)_s$ model to what
remains. Formally, $\{y_t\}$ is $\text{ARIMA}(p,d,q)\times(P,D,Q)_s$ if
$$\Phi(B^s)\phi(B)\,\nabla_s^D\nabla^d(y_t-\mu) = \delta + \Theta(B^s)\theta(B)\epsilon_t,$$
where $\nabla^d=(1-B)^d$ and $\nabla_s^D=(1-B^s)^D$ are the differencing operators from above.

For the `co2` example, fitting $\text{ARMA}(0,1)\times(0,1)_{12}$ to the once-differenced,
seasonally-differenced series $\nabla\nabla_{12}y_t$ is the same as fitting the SARIMA model with
non-seasonal order $(0,1,1)$ and seasonal order $(0,1,1)_{12}$ to the original series.
`statsmodels`'s `ARIMA` function fits this directly, given both an `order` and a `seasonal_order`
argument.

## Why estimating ARMA parameters is hard: MLE for MA(1)

Fitting AR$(p)$ models reduces to ordinary least squares — the AR equation is linear in the observed
$y$'s, so it is just regression. ARMA, ARIMA, and SARIMA models are not linear in the parameters in
that way, and fitting them is correspondingly harder. Rather than working through the general case,
the lecture illustrates the difficulty on the simplest non-AR model, MA(1) (in practice one simply
calls `ARIMA` and lets `statsmodels` handle the optimization).

Recall $y_t = \mu + \epsilon_t + \theta\epsilon_{t-1}$, with $\epsilon_t\overset{\text{i.i.d.}}{\sim}
N(0,\sigma^2)$. The joint distribution of $y_1,\dots,y_n$ is multivariate normal with mean
$(\mu,\dots,\mu)^T$ and covariance matrix $\Sigma$ where
$$\Sigma(i,j) = \begin{cases}\sigma^2(1+\theta^2) & i=j\\ \sigma^2\theta & |i-j|=1\\ 0 & \text{otherwise.}\end{cases}$$
The exact likelihood is
$$\left(\frac{1}{\sqrt{2\pi}}\right)^n(\det\Sigma)^{-1/2}\exp\!\left(-\tfrac12(y-m)^T\Sigma^{-1}(y-m)\right),$$
and the obstacle is $\Sigma^{-1}$: inverting an $n\times n$ matrix at every step of a numerical
maximization is expensive, so what is needed is an exact or approximate closed form for
$\Sigma^{-1}$, not a literal matrix inversion recomputed every time the log-likelihood is evaluated.

**An approximation via the AR representation.** Write the MA(1) equation as $y_t-\mu=\theta(B)\epsilon_t$
with $\theta(B)=1+\theta B$, and invert it — valid when $|\theta|<1$:
$$\epsilon_t = \frac{1}{1+\theta B}(y_t-\mu) = (1-\theta B+\theta^2B^2-\theta^3B^3+\cdots)(y_t-\mu),$$
i.e.
$$y_t-\theta y_{t-1}+\theta^2y_{t-2}-\theta^3y_{t-3}+\cdots = \frac{\mu}{1+\theta}+\epsilon_t.$$
This turns MA(1) into an (infinite-order) AR model, for which the likelihood would be
$$\left(\frac{1}{\sqrt{2\pi}\sigma}\right)^n\exp\!\left(-\frac{1}{2\sigma^2}\sum_{t=1}^n\Big(y_t-\frac{\mu}{1+\theta}-\theta y_{t-1}+\theta^2y_{t-2}-\cdots\Big)^2\right).$$
The catch is that this needs $y_0,y_{-1},y_{-2},\dots$, which were never observed. The standard fix
is to set them to zero — equivalently, to work with the likelihood of $y_1,\dots,y_n$ *conditional
on* $y_0,y_{-1},\dots$ all being zero. That truncation gives a likelihood of the form
$$\left(\frac{1}{\sqrt{2\pi}\sigma}\right)^n\exp\!\left(-\frac{S(\mu,\theta)}{2\sigma^2}\right),$$
where $S(\mu,\theta)$ sums the truncated residuals:
$$S(\mu,\theta) = \Big(y_1-\tfrac{\mu}{1+\theta}\Big)^2 + \Big(y_2-\tfrac{\mu}{1+\theta}-\theta y_1\Big)^2 + \cdots + \Big(y_n - \tfrac{\mu}{1+\theta}-\theta y_{n-1}+\cdots+(-1)^{n-1}\theta^{n-1}y_1\Big)^2.$$
The MLEs $\hat\mu,\hat\theta$ minimize $S(\mu,\theta)$ — a nonlinear least-squares problem solved
numerically (e.g. with `scipy`) rather than in closed form — and then
$$\hat\sigma = \frac{S(\hat\mu,\hat\theta)}{n}.$$

**A Bayesian aside** (not covered live in either lecture; included in the notes for completeness
only). Uncertainty about $\hat\mu,\hat\theta$ can be quantified by putting flat priors on
$\theta\in(-1,1)$, $\mu\in(-C,C)$, and $\log\sigma\in(-C,C)$ for large $C$, and integrating $\sigma$
out of the posterior — the same move used earlier in the course for AR(1) — to get
$$f_{\mu,\theta\mid\text{data}}(\mu,\theta) \propto \Big(\frac{1}{S(\mu,\theta)}\Big)^{n/2}\mathbb{I}\{-1<\theta<1,\,-C<\mu<C\}.$$
A second-order Taylor expansion of $S$ around its minimizer $\hat\alpha=(\hat\mu,\hat\theta)$ — using
$\nabla S(\hat\alpha)=0$ since $\hat\alpha$ minimizes $S$ — turns this into the kernel of a
multivariate $t$-distribution:
$$\alpha\mid\text{data} \sim t_{n-2,2}\!\left(\hat\alpha,\ \frac{S(\hat\alpha)}{n-2}\Big(\tfrac12 HS(\hat\alpha)\Big)^{-1}\right),$$
where $HS(\hat\alpha)$ is the Hessian of $S$ at $\hat\alpha$. This gives an approximate posterior for
$(\mu,\theta)$ without a grid search — though evaluating the un-approximated posterior numerically
over a grid of $(\mu,\theta)$ values is also an option.

## Sources

- UC Berkeley STAT 153, Fall 2025, Lecture Twenty-Three (Aditya Guntuboyina, November 20, 2025) —
  the Box-Jenkins strategy, ARIMA, seasonal ARMA, multiplicative seasonal ARMA, and SARIMA:
  `01-1-the-box-jenkins-time-series-modeling-strategy.md`, `02-3-seasonal-arma-models.md`,
  `03-4-multiplicative-seasonal-arma-models.md`.
- UC Berkeley STAT 153, Spring 2025, Lecture Twenty-Three (Aditya Guntuboyina, April 17, 2025),
  which covers the same ground plus two sections absent from the Fall run: the ARMA$(p,q)$ recap
  (`01-1-model.md`) and MLE for MA(1), including the Bayesian aside (`05-7-parameter-estimation-in-
  ma-1.md`). Its Box-Jenkins/ARIMA/seasonal/multiplicative/SARIMA sections (`02-2-the-box-jenkins-
  time-series-modeling-strategy.md`, `03-4-seasonal-arma-models.md`,
  `04-5-multiplicative-seasonal-arma-models.md`) duplicate the Fall material almost verbatim; this
  chapter merges the two rather than repeating them.
- Both runs are model reconstructions of a slide PDF with no extractable text layer (`route: llm`,
  `fidelity: reconstructed` in each file's frontmatter); every equation carries that source's own
  caveat of being unverified against the original slides, and this chapter has not independently
  re-checked them.
- The `co2` dataset used as the running seasonal example is from the time series textbook by Cryer
  and Chan — referred to by the lecture but not itself contained in these notes.
- Further reading named by the lecture but not contained here: Shumway and Stoffer, *Time Series
  Analysis and Its Applications*, 4th edition, §§3.5, 3.6, 3.9.

---

[← 123. From AR to LSTM](123-from-ar-to-lstm.md) · [Contents](index.md) · [125. Stationary Solutions of AR(p) →](125-stationary-solutions-of-ar-p.md)
