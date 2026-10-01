---
title: "14. Intro to Autoregressive Models"
course: "Berkeley Stat 153"
chapter: 14
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 14. Intro to Autoregressive Models

## What this covers

This chapter introduces autoregressive (AR) models: models that forecast a time series from its
own past values rather than from an external predictor. It builds the AR($p$) model as the
self-referential analogue of ordinary regression, works out exactly when the simplest case — the
AR(1) model — is stationary, and then introduces the backshift operator and the characteristic
polynomial as the general tools for deciding stationarity (and predicting oscillation) at any
order. It assumes the reader already knows what a stationary process is, what white noise is, and
what the autocovariance function and the ACF are, together with basic complex arithmetic (modulus
of a complex number).

## Autoregression as regression on the past

Ordinary regression predicts a response from external predictors: $Y = X\beta$. Autoregression
predicts a value from *itself* — hence the name, "regression on self." The simplest case is the
AR(1) process,

$$x_t = \phi x_{t-1} + w_t,$$

and the general AR($p$) process extends this to $p$ past values:

$$x_t = \phi_1 x_{t-1} + \phi_2 x_{t-2} + \dots + \phi_p x_{t-p} + w_t.$$

Here $p$, the *order* of the process, is how many steps into the past are needed to forecast the
current value. The model carries three standing assumptions:

- $x_t$ is stationary;
- $w_t$ is white noise with mean $0$ and variance $\sigma_w^2$, uncorrelated with everything that
  came before it;
- the coefficients $\phi_1, \dots, \phi_p$ are constants, none of them zero (otherwise $p$ would
  not really be the order).

If the series does not have mean zero, an intercept $\alpha$ can be added to the right-hand side.

## The AR(1) process and what $\phi$ controls

The AR(1) model already captures the basic idea of a signal with memory. Think of temperature: if
it is 72°F right now, your best guess for an hour from now is close to 72°F, not a fresh draw from
the distribution of all temperatures. Or stock returns: if the market moved 2% today, $\phi$
measures how much that carries into tomorrow's move.

The single parameter $\phi$ controls the qualitative behaviour of the whole process:

| $\phi$ | Behaviour |
|---|---|
| $\phi = 0$ | white noise (no memory) |
| $0 < \phi < 1$ | positive memory — values drift slowly |
| $\phi \to 1$ | very long memory |
| $\phi = 1$ | random walk (nonstationary) |
| $-1 < \phi < 0$ | oscillatory memory — alternating values |

What happens outside this range? If $|\phi| > 1$, the influence of past shocks no longer decays,
and the variance of $x_t$ grows without bound. So **the AR(1) process is stationary if and only if
$|\phi| < 1$.**

A lecture demo compared four series: white noise, an AR(1) with $\phi = 0.9$, a random walk
(AR(1) with $\phi = 1$, not stationary), and an AR(1) with $\phi = -0.8$. Two things were visible
by eye and left as questions: as $\phi$ increases toward 1 the series looks smoother and its
variance grows, and at $\phi = 0.99$ the series is nearly indistinguishable from a random walk. The
next section answers both "why" questions directly from the formulas.

## Properties of the stationary AR(1) process

When $|\phi| < 1$, the mean, variance, autocovariance and ACF all have closed form (the lecture
points to Shumway & Stoffer, Ch. 3, Example 3.1, for the full derivation; the short argument below
is the plausibility version). Assume $x_t$ has mean zero.

**Variance.** Since $w_t$ is uncorrelated with $x_{t-1}$ (which is built only from past shocks),

$$\operatorname{Var}(x_t) = \phi^2 \operatorname{Var}(x_{t-1}) + \sigma_w^2.$$

Stationarity means $\operatorname{Var}(x_t) = \operatorname{Var}(x_{t-1}) = \gamma(0)$, so

$$\gamma(0) = \phi^2 \gamma(0) + \sigma_w^2 \quad\Longrightarrow\quad \gamma(0) = \frac{\sigma_w^2}{1-\phi^2}.$$

This already explains the observation above: as $\phi \to 1$, the denominator $1 - \phi^2 \to 0$
and the variance blows up — exactly why the series looked more variable as $\phi$ grew, and why
$|\phi| < 1$ is required for a finite (hence stationary) variance in the first place.

**Autocovariance and ACF.** For $h \geq 1$, $x_{t-h}$ is built entirely from shocks up to time
$t-h$, all earlier than $w_t$, so $w_t$ is uncorrelated with $x_{t-h}$. Then

$$\gamma(h) = \operatorname{Cov}(x_t, x_{t-h}) = \operatorname{Cov}(\phi x_{t-1} + w_t,\, x_{t-h}) = \phi\, \gamma(h-1).$$

Unrolling this recursion from $\gamma(0)$ gives $\gamma(h) = \phi^h \gamma(0)$, i.e.

$$\gamma(h) = \frac{\sigma_w^2 \phi^h}{1-\phi^2}, \qquad \rho(h) = \frac{\gamma(h)}{\gamma(0)} = \phi^h \quad (h \geq 0).$$

The ACF of an AR(1) process decays **exponentially**, at rate $\phi$ — the smoothness observed for
large $\phi$ is exactly this: each new value keeps a large fraction $\phi$ of its predecessor, so
consecutive values stay correlated for many lags instead of decorrelating quickly.

## The backshift operator

To handle general order $p$, define the *backshift operator* $B$ by

$$B x_t = x_{t-1}.$$

Applying it repeatedly shifts further back: $B^k x_t = x_{t-k}$. The AR(1) model rewrites as

$$x_t - \phi x_{t-1} = w_t \;\;\Longrightarrow\;\; x_t - \phi B x_t = w_t \;\;\Longrightarrow\;\; (1-\phi B)x_t = w_t,$$

and the general AR($p$) model as

$$(1 - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p)\, x_t = w_t.$$

## The characteristic polynomial and stationarity

Write $\phi(B) = 1 - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p$, the *autoregressive operator*, so
that the model is just $\phi(B) x_t = w_t$. Treating $B$ as a formal variable, $\phi(B)$ is also
called the *characteristic polynomial*: its roots determine stationarity and, for order 2 and
above, whether the process oscillates.

**AR(1).** Here $\phi(B) = 1 - \phi B$, with a single root at $B = 1/\phi$. Stationarity ($|\phi| <
1$) translates into a statement about this root: $|1/\phi| > 1$. **The general rule for any order is
that the process is stationary exactly when every root of $\phi(B)$ lies outside the unit circle.**

**AR(2).** For $x_t = \phi_1 x_{t-1} + \phi_2 x_{t-2} + w_t$, the characteristic polynomial is
$\phi(B) = 1 - \phi_1 B - \phi_2 B^2$, a genuine quadratic, so it can have:

1. **two real roots** — overdamped behaviour, the process decays smoothly back to its mean without
   oscillating; or
2. **a complex conjugate pair of roots** — oscillatory decay.

Either way, stationarity is the same test: both roots must lie outside the unit circle.

## Worked example: an oscillatory but stationary AR(2)

Take $x_t = 0.6\,x_{t-1} - 0.5\,x_{t-2} + w_t$. The steps are always the same: write the
characteristic polynomial, find its roots, check whether they lie outside the unit circle, and
read off the qualitative behaviour.

**Characteristic polynomial:** $\phi(B) = 1 - 0.6B + 0.5B^2$.

**Roots**, by the quadratic formula:

$$B = \frac{0.6 \pm \sqrt{(-0.6)^2 - 4(0.5)(1)}}{2(0.5)} = 0.6 \pm 1.28i.$$

The discriminant is negative, so the roots are a complex conjugate pair — case 2 above, so decay
should be oscillatory rather than smooth.

**Modulus**, to check stationarity:

$$|z| = \sqrt{0.6^2 + 1.28^2} \approx 1.41.$$

Since $1.41 > 1$, both roots lie outside the unit circle, so **the process is stationary**. The
modulus carries a second piece of information beyond the yes/no stationarity answer: a modulus
close to 1 means light damping and a persistent, slowly-dying oscillation, while a modulus close to
0 means heavy damping and a signal that dies out fast. At $1.41$, this process is stationary but
only moderately damped. A simulation of this exact model confirms the prediction: the sample path
shows a damped, oscillatory wiggle rather than a smooth drift, and its sample ACF alternates in
sign while decaying, tracking the complex-root case rather than the AR(1)-style smooth exponential
decay.

<figure>
<svg viewBox="0 0 320 300" role="img" aria-label="The complex plane showing the AR(2) example's characteristic roots relative to the unit circle">
  <line x1="20" y1="160" x2="300" y2="160" stroke="currentColor" stroke-width="1"/>
  <line x1="160" y1="20" x2="160" y2="290" stroke="currentColor" stroke-width="1"/>
  <text x="288" y="152" font-size="12" fill="currentColor">Re</text>
  <text x="168" y="32" font-size="12" fill="currentColor">Im</text>
  <circle cx="160" cy="160" r="60" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="200" y="176" font-size="11" fill="currentColor">unit circle</text>
  <circle cx="196" cy="83" r="4" fill="currentColor"/>
  <circle cx="196" cy="237" r="4" fill="currentColor"/>
  <line x1="160" y1="160" x2="196" y2="83" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
  <text x="203" y="118" font-size="12" fill="currentColor">|z| = 1.41</text>
  <text x="203" y="75" font-size="12" fill="currentColor">0.6 + 1.28i</text>
  <text x="203" y="253" font-size="12" fill="currentColor">0.6 - 1.28i</text>
</svg>
<figcaption>The characteristic roots of $\phi(B) = 1 - 0.6B + 0.5B^2$ are a complex conjugate pair
lying outside the dashed unit circle (modulus 1.41, greater than 1), so the process is stationary;
because the roots are complex rather than real, the decay back to the mean is oscillatory rather
than smooth.</figcaption>
</figure>

## Looking ahead

The lecture closes by flagging, but not covering, two extensions: the general AR($p$) case with
$p > 2$ (where the characteristic polynomial can mix real and complex-conjugate root pairs), and
ARMA models, which add a moving-average component so that the model can also respond to *recent*
shocks and not only past values of $x_t$ itself. Both are previewed as "next time" material and are
not developed further here.

## Sources

- Berkeley STAT 153/248, Spring 2026, Lecture 16 lecture notes (`16_ar_models_notes.md`), split into
  three pages: *Intro to Autoregressive models* (AR($p$) definition, order, standing assumptions,
  the four-series demo description), *AR(1) process* (interpretation, the $\phi$-behaviour table,
  the stationary AR(1) property table, the backshift operator), and *The autoregressive
  operator/characteristic polynomial* (the characteristic polynomial, AR(1) and AR(2) root cases,
  the worked AR(2) example with numeric roots and modulus).
- The accompanying Lecture 16 Jupyter notebook, split into *Stat 153/248 - Lecture 16* (simulation
  code for the four-series demo and for AR(1) at several $\phi$ values) and *Properties of the
  AR(1) model* (simulated vs. theoretical ACF for AR(1); simulation and root computation for the
  same AR(2) worked example, confirming the modulus $1.41$ and the oscillatory, stationary
  conclusion numerically).
- Referred to but not contained in the supplied material: Shumway & Stoffer, *Time Series Analysis
  and Its Applications*, Ch. 3, Example 3.1 (assigned reading, and the source cited for the full
  derivation of the AR(1) mean/variance/autocovariance formulas), the lecture's plotted figures
  (referenced by URL in the slides but not themselves supplied as data), and the next lecture's
  material on general AR($p$) and ARMA models.
- No transcript, written notes, or problem set were supplied for this lecture.

---

[← 13. Time-Frequency Analysis of Music](13-time-frequency-analysis-of-music.md) · [Contents](index.md) · [15. Autoregressive Moving Average Models →](15-autoregressive-moving-average-models.md)
