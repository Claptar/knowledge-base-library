---
title: "15. Autoregressive Moving Average Models"
course: "Berkeley Stat 153"
chapter: 15
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 15. Autoregressive Moving Average Models

## What this covers

This chapter answers: once we have autoregressive (AR) models, why do we also need a *moving
average* (MA) piece, and how do the two combine into a single ARMA model? It assumes the AR(p)
model, the stationarity condition on the roots of its characteristic polynomial, and the backshift
operator $B$ (with $Bx_t = x_{t-1}$) are already familiar.

## Recap: AR models and causality

An AR(p) process is

$$x_t = \phi_1 x_{t-1} + \phi_2 x_{t-2} + \dots + \phi_p x_{t-p} + w_t.$$

It is stationary if and only if the roots of its characteristic polynomial lie outside the unit
circle. When that holds, the process can be rewritten as an infinite weighted sum of present and
past white noise,

$$x_t = \mu + \sum_{j=0}^{\infty} \psi_j \epsilon_{t-j}, \qquad \sum_j |\psi_j| < \infty,$$

for some mean $\mu$ and coefficients $\psi_j$. This is called a *causal* representation — not in
the everyday sense of cause and effect, but meaning the process can be written purely in terms of
current and past noise, with no dependence on the future.

## The moving average model MA($q$)

The moving average model takes the opposite approach: instead of a value depending on its own past
values, it is built directly as a finite, weighted average of past noise terms.

**MA($q$):**

$$x_t = w_t + \theta_1 w_{t-1} + \theta_2 w_{t-2} + \dots + \theta_q w_{t-q}, \qquad w_t \sim
\text{white noise}(0, \sigma_w^2),$$

with parameters $\theta_1, \dots, \theta_q$ and $\theta_q \neq 0$. Using the backshift operator this
is

$$x_t = \theta(B) w_t, \qquad \theta(B) = 1 + \theta_1 B + \theta_2 B^2 + \dots + \theta_q B^q.$$

### Why the backshift operator is legitimate to manipulate this way

The reason expressions like $\theta(B)$ or a characteristic polynomial in $B$ are meaningful is that
$B$ is a **linear operator**. A function $f$ is linear if, for all inputs $x, y$ and scalars $a, b$,

1. **Additivity**: $f(x+y) = f(x) + f(y)$,
2. **Scalar homogeneity**: $f(ax) = af(x)$,

equivalently $f(ax+by) = af(x) + bf(y)$. The backshift operator satisfies this: shifting a scaled or
summed series in time gives the same result as scaling or summing the shifted series. That is what
licenses treating $B$ as if it were a number when forming a polynomial — it is the same property
that made the characteristic-polynomial test for AR stationarity valid, and it will do the same job
for testing invertibility of the MA part below.

## Autocovariance and ACF of an MA(1) process

Take the simplest case, $x_t = w_t + \theta w_{t-1}$. Unlike an AR model, an MA model is stationary
for *every* value of $\theta_1, \dots, \theta_q$ — there is no root condition to check. Its mean is
$E(x_t) = 0$, and its autocovariance is

$$\gamma_x(h) = \begin{cases} (1+\theta^2)\sigma_w^2 & h = 0, \\ \theta \sigma_w^2 & h = 1, \\ 0 & h >
1, \end{cases}$$

so the autocorrelation function is

$$\rho_x(h) = \begin{cases} \dfrac{\theta}{1+\theta^2} & h = 1, \\ 0 & h > 1. \end{cases}$$

The qualitative point is the contrast with AR(1): here $x_t$ is correlated with $x_{t-1}$ but with
nothing further back — the correlation *cuts off* exactly at lag $q$. In an AR(1) model, by
contrast, the correlation between $x_t$ and $x_{t-k}$ decays but is never exactly zero at any lag.
This is the basic diagnostic difference between the two model families: an MA autocovariance drops
to zero past a fixed lag, while an AR autocovariance decays smoothly but persists.

<figure>
<svg viewBox="0 0 380 220" role="img" aria-label="MA(1) autocorrelation cutting off after lag 1, compared with AR(1) autocorrelation decaying but never reaching zero">
  <line x1="40" y1="170" x2="340" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="170" x2="40" y2="40" stroke="currentColor" stroke-width="1.5"/>
  <text x="345" y="174" font-size="12" fill="currentColor">h</text>
  <text x="20" y="45" font-size="12" fill="currentColor">&#961;</text>

  <rect x="50" y="50" width="20" height="120" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="110" y="110" width="20" height="60" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <line x1="180" y1="170" x2="200" y2="170" stroke="currentColor" stroke-width="2"/>
  <line x1="240" y1="170" x2="260" y2="170" stroke="currentColor" stroke-width="2"/>
  <line x1="300" y1="170" x2="320" y2="170" stroke="currentColor" stroke-width="2"/>

  <polyline points="60,50 128,86 188,111.2 248,128.8 308,141" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>

  <text x="60" y="185" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <text x="120" y="185" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="190" y="185" text-anchor="middle" font-size="12" fill="currentColor">2</text>
  <text x="250" y="185" text-anchor="middle" font-size="12" fill="currentColor">3</text>
  <text x="310" y="185" text-anchor="middle" font-size="12" fill="currentColor">4</text>

  <text x="80" y="210" font-size="11" fill="currentColor">bars: MA(1), &#952;/(1+&#952;&#178;) then 0</text>
  <text x="80" y="30" font-size="11" fill="currentColor">dashed: AR(1), decays but stays nonzero</text>
</svg>
<figcaption>The MA(1) autocorrelation is nonzero only up to lag 1 and exactly zero beyond it,
while the AR(1) autocorrelation decays geometrically but never reaches zero at any lag.</figcaption>
</figure>

The lecture illustrated this with simulated MA(1) series for $\theta = 0.9$ and $\theta = -0.9$: the
$\theta = 0.9$ series looked visibly smoother than the $\theta = -0.9$ series, but neither has the
AR-style correlation structure that persists across all lags — both cut off after lag 1.

## Invertibility of the MA model

MA models have a subtlety AR models do not: the parameters are not always identifiable from the
autocovariance alone. For an MA(1) process, $\rho_x(h)$ is exactly the same whether the parameter is
$\theta$ or $1/\theta$ — check this directly in $\rho_x(1) = \theta/(1+\theta^2)$, which is unchanged
under $\theta \mapsto 1/\theta$. Pairing this with a matching change in noise variance makes the two
processes not just have the same ACF, but be **the same process**: for $\theta = 1/5$ with
$\sigma_w^2 = 25$,

$$x_t = w_t + \tfrac{1}{5} w_{t-1}, \qquad w_t \overset{iid}{\sim} N(0, 25),$$

and for $\theta = 5$ with $\sigma_v^2 = 1$,

$$y_t = v_t + 5 v_{t-1}, \qquad v_t \overset{iid}{\sim} N(0, 1),$$

both give $\gamma(0) = 26$ and $\gamma(1) = 5$. Because $w_t$ and $v_t$ are Gaussian, matching mean
and autocovariance makes $x_t$ and $y_t$ stochastically identical processes. Since we only ever
observe the series itself and not the noise separately, these two parameterisations cannot be told
apart from data, and we are forced to choose a convention.

The convention is **invertibility**: choose the representation with $|\theta| < 1$, because that is
the one that can be inverted into an infinite AR representation,

$$w_t = \sum_{j=0}^{\infty} (-\theta)^j x_{t-j}.$$

Invertibility means $\theta(B)$ can be inverted as a power series, $w_t = \theta(B)^{-1} x_t$ — this
is the exact MA counterpart of requiring an AR model's characteristic roots to lie outside the unit
circle for causality. In the example above, that means preferring $\theta = 1/5$, $\sigma_w^2 = 25$
over $\theta = 5$, $\sigma_v^2 = 1$.

## ARMA($p,q$) models

Putting the two pieces together: the AR autocovariance decays away from lag 0, while the MA
autocovariance drops to exactly zero past a fixed lag. Combining both gives a model rich enough to
capture behaviour that neither alone can.

*Definition.* A time series is **ARMA($p,q$)** if it is stationary and satisfies

$$x_t = \mu + \phi_1(x_{t-1}-\mu) + \dots + \phi_p(x_{t-p}-\mu) + w_t + \theta_1 w_{t-1} + \dots +
\theta_q w_{t-q}.$$

Here $p$ is the autoregressive order and $q$ is the moving-average order. Writing $\alpha = \mu(1 -
\phi_1 - \dots - \phi_p)$, this is equivalent to

$$x_t = \alpha + \phi_1 x_{t-1} + \dots + \phi_p x_{t-p} + w_t + \theta_1 w_{t-1} + \dots + \theta_q
w_{t-q},$$

or, in backshift-operator form,

$$\phi(B)(x_t - \mu) = \theta(B) w_t.$$

ARMA is a genuine extension of both earlier models: setting $q=0$ recovers ARMA($p,0$) = AR($p$),
and setting $p=0$ recovers ARMA($0,q$) = MA($q$).

## When to use ARMA, and when not to

ARMA models are useful for forecasting **stationary** time series by combining information from
previous values (the AR part) with information from previous forecast errors (the MA part) —
typical applications mentioned include sales, temperature, and financial time series.

They are the wrong tool when:

- the data are nonstationary or have a trend,
- the data have strong seasonal patterns,
- the relationships in the data are complex and nonlinear.

## Sources

- Slide/notes set *Autoregressive Moving Average Models*
  (`17_arma_models_notes/01-autoregressive-moving-average-models.md`): AR(p) recap and causal
  representation, MA($q$) definition and backshift form, the linear-operator aside, and the MA(1)
  autocovariance/ACF derivation and comparison with AR(1).
- Slide/notes set *Invertibility of the MA model*
  (`17_arma_models_notes/02-invertibility-of-the-ma-model.md`): the $\theta$ vs. $1/\theta$
  non-identifiability of MA(1), the invertibility convention and infinite-AR inversion, the
  ARMA($p,q$) definition, and when ARMA models are and are not appropriate.
- Referred to but not contained in the supplied material: the reading assignment "Ch. 3 — Shumway
  and Stoffer"; a plotted figure of simulated MA(1) series for $\theta = 0.9$ and $\theta = -0.9$
  (described in text, image not reproduced here); and a short video schematic contrasting AR, MA,
  and ARMA models (linked in the source, not viewable from the transcript).

---

[← 14. Intro to Autoregressive Models](14-intro-to-autoregressive-models.md) · [Contents](index.md) · [16. Identifying ARMA Models via ACF/PACF →](16-identifying-arma-models-via-acf-pacf.md)
