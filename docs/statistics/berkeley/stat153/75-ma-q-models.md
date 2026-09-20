---
title: "75. $MA(q)$ models"
course: "Berkeley Stat 153 Fall 2024"
chapter: 75
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 75. $MA(q)$ models

## What this covers

This chapter builds the moving-average model $MA(q)$ and sets it next to the autoregressive model
from earlier in the course. It answers three linked questions: what does averaging together the
last few white-noise shocks do to a series' correlation structure, how do you read that structure
off real data through the sample autocorrelation function (ACF), and — since it turns out $MA(q)$
models are *always* well-behaved while $AR(p)$ models are not — exactly when is an autoregression
well-behaved at all? It assumes the reader already has: an i.i.d. Gaussian white-noise sequence
$\varepsilon_t \sim N(0,\sigma^2)$, the definition of (weak) stationarity, the $AR(1)$ model
$y_t - \phi_1 y_{t-1} = \phi_0 + \varepsilon_t$, and ordinary least squares.

## The $MA(q)$ model

A **moving-average model of order $q$**, $MA(q)$, is built from i.i.d. innovations
$\varepsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2)$, $t = \dots,-2,-1,0,1,2,\dots$, by

$$
y_t = \mu + \varepsilon_t + \theta_1\varepsilon_{t-1} + \cdots + \theta_q\varepsilon_{t-q}.
$$

Each observation is a fixed linear combination of the current shock and the $q$ shocks immediately
before it — a finite moving average of white noise, hence the name. Nothing here feeds $y$ back
into itself the way an autoregression does; $y_t$ is just a snapshot of a sliding window of noise.

The simplest case, $q=1$,

$$
y_t = \mu + \varepsilon_t + \theta_1\varepsilon_{t-1},
$$

is the model behind Slutsky's 1937 paper "The Summation of Random Causes as the Source of Cyclic
Processes": the point being made there is that averaging independent random shocks together can
produce a series that *looks* cyclical, with no actual cycle driving it.

## The $MA(1)$ autocorrelation

Take variances and covariances directly from the definition, using that the $\varepsilon_t$ are
independent with variance $\sigma^2$:

$$
\operatorname{Var}(y_t) = \operatorname{Var}(\varepsilon_t) + \theta_1^2\operatorname{Var}(\varepsilon_{t-1}) = \sigma^2(1+\theta_1^2),
$$

$$
\operatorname{Cov}(y_t,y_{t+1}) = \operatorname{Cov}(\varepsilon_t+\theta_1\varepsilon_{t-1},\ \varepsilon_{t+1}+\theta_1\varepsilon_t) = \theta_1\operatorname{Var}(\varepsilon_t) = \theta_1\sigma^2,
$$

since every other pair in that expansion involves two *different* noise terms and is therefore
independent, hence covariance $0$. Dividing gives the lag-$1$ correlation

$$
\operatorname{Corr}(y_t,y_{t+1}) = \frac{\theta_1}{1+\theta_1^2}.
$$

Because the denominator is always positive, the sign of the correlation is exactly the sign of
$\theta_1$: $\theta_1 = 0$ collapses the model to plain i.i.d. noise $y_t\sim N(\mu,\sigma^2)$;
$\theta_1>0$ gives positively correlated neighbours; $\theta_1<0$ gives negatively correlated
neighbours.

For $h\ge 2$, $y_t$ is built only from $\varepsilon_t,\varepsilon_{t-1}$ and $y_{t+h}$ only from
$\varepsilon_{t+h},\varepsilon_{t+h-1}$ — for $h\ge2$ these two index sets share nothing, so every
cross term is a covariance between independent variables:

$$
\operatorname{Corr}(y_t,y_{t+h}) = 0 \quad \text{for } h\ge 2.
$$

The same overlap argument scales up to $MA(q)$: $y_t$ depends on $\varepsilon_t,\dots,\varepsilon_{t-q}$
and $y_{t+h}$ on $\varepsilon_{t+h},\dots,\varepsilon_{t+h-q}$, and these ranges intersect exactly
when $h\le q$. So the theoretical ACF of an $MA(q)$ is some (generally messy) nonzero value for
$|h|\le q$ and is *exactly* zero for $|h|>q$ — a hard cutoff at lag $q$.

None of $\mu$, $\operatorname{Var}(y_t)$ or $\operatorname{Cov}(y_t,y_{t+h})$ depends on $t$, and all
are finite for every choice of the $\theta_i$'s — there is no feedback loop that could make them
blow up. So an $MA(q)$ model is **always causal and stationary**, regardless of the values of
$\theta_1,\dots,\theta_q$.

## Reading the ACF off data

The theoretical quantity $\rho(h) = \operatorname{Corr}(y_t,y_{t+h})$ is a property of the *model*:
for a stationary series it cannot depend on $t$, only on the lag $h$. Its empirical counterpart,
the **sample ACF**, is computed from data $y_1,\dots,y_n$ by treating $(y_t,y_{t+h})$ for
$t=1,\dots,n-h$ as $m=n-h$ paired observations and taking their sample correlation:

$$
\text{Correlation of }(a_1,b_1),\dots,(a_m,b_m) = \frac{\sum_{i=1}^m(a_i-\bar a)(b_i-\bar b)}{\sqrt{\sum_{i=1}^m(a_i-\bar a)^2\sum_{i=1}^m(b_i-\bar b)^2}}
$$

with $a_i=y_i$, $b_i=y_{i+h}$. Once $n$ is not tiny relative to $h$, the two means
$\bar a = \frac1{n-h}\sum_{i=1}^{n-h}y_i$ and $\bar b=\frac1{n-h}\sum_{i=1}^{n-h}y_{i+h}$ are both
close to the overall sample mean $\bar y$, so both get replaced by it. The two sums under the
square root are then each a sum of $n-h$ squared deviations of the *same* series and are both
close to the full-sample sum $\sum_{t=1}^n(y_t-\bar y)^2$; substituting that in for both gives the
sample ACF actually reported by software:

$$
\widehat\rho(h) = \frac{\sum_{t=1}^{n-h}(y_t-\bar y)(y_{t+h}-\bar y)}{\sum_{t=1}^n(y_t-\bar y)^2}.
$$

This is the empirical version of $\rho(h)$: computed from the data rather than from a model. The
identification idea that follows immediately is that if the sample ACF of a real series spikes at
lag $1$ and is negligible everywhere after — matching the $MA(1)$ shape

$$
\rho(h) = \begin{cases} 1 & h=0 \\ \dfrac{\theta}{1+\theta^2} & |h|=1 \\ 0 & |h|\ge 2\end{cases}
$$

— the series "looks like $MA(1)$". More generally, a sample ACF that is non-negligible up through
lag $q$ and cuts off to (near) zero beyond it is evidence the series is $MA(q)$.

## $MA(1)$ versus $AR(1)$: stationarity is not automatic

Put the two side by side:

$$
MA(1):\quad y_t = \mu+\varepsilon_t+\theta\varepsilon_{t-1} \qquad\text{— always stationary,}
$$

$$
AR(1):\quad y_t - \phi_1 y_{t-1} = \phi_0 + \varepsilon_t \qquad\text{— not necessarily causal and stationary.}
$$

The asymmetry is structural. An $MA(1)$ is a fixed, finite combination of noise terms, so nothing
in it can ever diverge — the argument of the previous section works for *any* $\theta$. An $AR(1)$
feeds its own past value back into itself, so whether the series stays bounded depends on how
strong that feedback is; the precise condition is worked out below.

## Estimating the parameters

For the $AR(1)$ model, rearrange as $y_t = \phi_0 + \phi_1 y_{t-1} + \varepsilon_t$: this is exactly
a linear regression of $y_t$ on an intercept and $y_{t-1}$, with i.i.d. Gaussian errors. Stack the
response as $y=(y_t)$ and the design matrix as $X=[\mathbf 1,\ y_{t-1}]$, and ordinary least squares
(`sm.OLS(y, X).fit()`) gives $\hat\phi_0,\hat\phi_1$ directly — there is a closed form because every
regressor is observed data.

That shortcut is not available for $MA(1)$: the regressor $\varepsilon_{t-1}$ is latent, never
observed, so there is no design matrix to build. Instead, use that $(y_1,\dots,y_n)$ is itself
jointly Gaussian — it is a linear function of the jointly Gaussian noise vector — with mean
$\mu\mathbf 1$ and a covariance matrix built entirely from the $MA(1)$ autocovariances derived
above. Since $\operatorname{Cov}(y_t,y_{t+h})=0$ for $h\ge2$, the matrix is tridiagonal:

$$
\Sigma = \sigma^2\begin{pmatrix}
1+\theta^2 & \theta & 0 & \cdots & 0\\
\theta & 1+\theta^2 & \theta & \cdots & 0\\
0 & \theta & 1+\theta^2 & \ddots & \vdots\\
\vdots & & \ddots & \ddots & \theta\\
0 & \cdots & 0 & \theta & 1+\theta^2
\end{pmatrix}.
$$

The likelihood is the multivariate normal density evaluated at the data,

$$
f(y_1,\dots,y_n) = \frac{1}{(2\pi)^{n/2}(\det\Sigma)^{1/2}}\exp\!\left[-\tfrac12(y-\mu\mathbf 1)^\top\Sigma^{-1}(y-\mu\mathbf 1)\right],
$$

and maximum likelihood maximises this over $(\mu,\theta,\sigma)$ — with no closed form the way OLS
has one, so this has to be done numerically. This is what an `ARIMA`-style fitting routine (e.g. in
`statsmodels`) runs under the hood, and it is the general route used whenever a model has latent
noise terms in it rather than only observed regressors.

## The ARMA/ARIMA family

Putting the two model types together in one recursion gives $ARMA(p,q)$:

$$
\text{AR}(p):\quad y_t - \phi_1y_{t-1}-\cdots-\phi_py_{t-p} = \phi_0+\varepsilon_t,
$$

$$
\text{MA}(q):\quad y_t = \mu+\varepsilon_t+\theta_1\varepsilon_{t-1}+\cdots+\theta_q\varepsilon_{t-q},
$$

$$
\text{ARMA}(p,q):\quad y_t-\phi_1y_{t-1}-\cdots-\phi_py_{t-p} = \phi_0+\varepsilon_t+\theta_1\varepsilon_{t-1}+\cdots+\theta_q\varepsilon_{t-q}.
$$

$ARIMA(p,d,q)$ adds one more step in front: difference the raw data $d$ times, then fit
$ARMA(p,q)$ to what is left. In software this is one call, `arima(data, order=(p,d,q))`, and the
pure cases are the special cases with $p=0$, $q=0$ or $d=0$: an $MA(q)$ is `arima(data, order=(0,0,q))`,
an $AR(p)$ is `arima(data, order=(p,0,0))`. Fitting an $MA(q)$ to the once-differenced series
$y_t-y_{t-1}$ can be done two equivalent ways — difference by hand and call
`arima(differenced data, order=(0,0,q))`, or hand the routine the original series and let it
difference internally with `arima(data, order=(0,1,q))`.

## When is an $AR(p)$ causal and stationary?

Write the **backshift (lag) operator** $B$ by $By_t = y_{t-1}$, so $B^ky_t=y_{t-k}$. The $AR(p)$
recursion is then

$$
\phi(B)y_t = \phi_0+\varepsilon_t, \qquad \phi(z) = 1-\phi_1z-\phi_2z^2-\cdots-\phi_pz^p,
$$

where $\phi(z)$ is called the $AR(p)$ polynomial. The model is causal and stationary exactly when
**every root of $\phi(z)$ has modulus strictly greater than $1$** — every root lies outside the
unit circle in the complex plane.

<figure>
<svg viewBox="0 0 320 240" role="img" aria-label="The unit circle in the complex plane: an AR(p) model is causal and stationary exactly when every root of its characteristic polynomial lands outside it">
  <line x1="20" y1="120" x2="300" y2="120" stroke="currentColor" stroke-width="1"/>
  <line x1="160" y1="15" x2="160" y2="225" stroke="currentColor" stroke-width="1"/>
  <text x="290" y="113" font-size="12" fill="currentColor">Re</text>
  <text x="168" y="24" font-size="12" fill="currentColor">Im</text>
  <circle cx="160" cy="120" r="60" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="52" text-anchor="middle" font-size="11" fill="currentColor">|z| = 1</text>
  <text x="160" y="150" text-anchor="middle" font-size="11" fill="currentColor">non-causal</text>
  <circle cx="255" cy="120" r="4" fill="currentColor"/>
  <text x="255" y="138" text-anchor="middle" font-size="11" fill="currentColor">causal root</text>
  <circle cx="140" cy="95" r="4" fill="currentColor"/>
  <text x="140" y="80" text-anchor="middle" font-size="11" fill="currentColor">non-causal root</text>
</svg>
<figcaption>The AR(p) polynomial φ(z) = 1 − φ₁z − ⋯ − φₚzᵖ must have every root strictly outside the
shaded unit disk for the model to be causal and stationary; a root landing inside breaks it.</figcaption>
</figure>

When the condition holds, the recursion can be unwound into an infinite moving average of past
shocks — every causal-stationary $AR(p)$ is secretly an $MA(\infty)$:

$$
y_t = \mu+\varepsilon_t+\psi_1\varepsilon_{t-1}+\psi_2\varepsilon_{t-2}+\cdots,
$$

which is why the two families sit together rather than being unrelated special cases. (A tool such
as `ARMA2MA` computes these $\psi$ coefficients numerically for general $p$ and $q$, rather than by
hand.)

The $AR(1)$ case makes the correspondence concrete. Its polynomial is $\phi(z)=1-\phi_1z$, with the
single root $z=1/\phi_1$; requiring $|z|>1$ is exactly $|\phi_1|<1$, the familiar $AR(1)$
stationarity condition. Substituting the recursion $y_t=\phi_0+\phi_1y_{t-1}+\varepsilon_t$ into
itself repeatedly,

$$
y_t = \phi_0(1+\phi_1+\phi_1^2+\cdots) + \varepsilon_t+\phi_1\varepsilon_{t-1}+\phi_1^2\varepsilon_{t-2}+\cdots
= \frac{\phi_0}{1-\phi_1}+\varepsilon_t+\phi_1\varepsilon_{t-1}+\phi_1^2\varepsilon_{t-2}+\phi_1^3\varepsilon_{t-3}+\cdots,
$$

which converges term by term exactly when $|\phi_1|<1$ — the geometric series $\phi_1^k$ shrinking
to zero is what makes the mean finite and the $MA(\infty)$ representation well-defined, and is the
same condition read off the root of $\phi(z)$ above.

## Sources

All material in this chapter comes from the handwritten lecture notes for Berkeley STAT 153 (Fall
2025), Lecture 21 (`HandwrittenNotesLectureTwentyOne153248Fall2025.pdf`, CC BY 4.0); no slide deck,
transcript or problem set was supplied for this lecture:

- `01-models.md` ("$MA(q)$ models") — the $MA(q)$ definition, the Slutsky (1937) attribution for
  $MA(1)$, the $MA(1)$ variance/covariance/correlation derivation, the $h\ge2$ cutoff, the
  sample-ACF-vs-theoretical-ACF pairing, and the derivation of the sample ACF formula
  $\widehat\rho(h)$ from the general sample-correlation formula.
- `02-vs.md` ("$MA(1)$ vs $AR(1)$") — the always-stationary/not-necessarily-stationary contrast
  between $MA(1)$ and $AR(1)$, the OLS setup for $AR(1)$ and the Gaussian-likelihood setup for
  $MA(1)$, the $AR(p)/MA(q)/ARMA(p,q)/ARIMA(p,d,q)$ definitions and their `arima(...)` call forms,
  the backshift-operator/root criterion for $AR(p)$ causal stationarity, and the $AR(1)$ worked
  example of the $MA(\infty)$ expansion.
- Both pages are flagged by the conversion as reconstructed by a model from a handwritten PDF with
  no text layer, with every equation unverified against the original scan. The covariance matrix
  $\Sigma$ and the Gaussian likelihood above have been re-derived independently from the stated
  $\operatorname{Var}(y_t)$ and $\operatorname{Cov}(y_t,y_{t+1})$, since the source's own rendering
  of that matrix is visibly corrupted by the OCR/reconstruction step.
- Named in the source but not developed there: Slutsky's 1937 paper "The Summation of Random
  Causes as the Source of Cyclic Processes," and the specific `statsmodels` routines `sm.OLS`,
  `ARIMA` and `ARMA2MA` used for fitting and for computing $MA(\infty)$ coefficients.

---

[← 73. Stationary MA and AR Processes](73-stationary-ma-and-ar-processes.md) · [Contents](index.md) · [76. Neural Network Models for Time Series →](76-neural-network-models-for-time-series.md)
