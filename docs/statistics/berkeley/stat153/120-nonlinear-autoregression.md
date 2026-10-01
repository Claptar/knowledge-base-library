---
title: "120. Nonlinear Autoregression"
course: "Berkeley Stat 153"
chapter: 120
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 120. Nonlinear Autoregression

## What this covers

This chapter picks up a single idea from the last lecture of a time series course: how to make
autoregression **nonlinear**. It assumes the linear AR($p$) model and least-squares fitting as
background, and answers one question — if the mean of $y_t$ is allowed to be a nonlinear function
of the recent past $y_{t-1}, \dots, y_{t-p}$, what is a concrete, fittable family of such functions?
The lecture builds one such family out of "hinge" functions and starts, but does not finish,
rewriting it in the vector notation used for neural networks. The material below is exactly what
survives from that lecture; where it breaks off, this chapter says so rather than completing it.

## From linear to nonlinear autoregression

For an observed series $y_1, \dots, y_n$ and an integer $p \ge 1$, write the lagged vector at time
$t$ as
$$
x_t = (y_{t-1}, \dots, y_{t-p})^T.
$$
$x_t$ is the **covariate** at time $t$ for the response $y_t$ — in the language borrowed from
recurrent neural networks, $x_t$ is the *input* at time $t$.

The ordinary linear AR($p$) model sets the conditional mean of $y_t$ to a linear function of $x_t$:
$$
\mu_t = \beta_0 + \beta^T x_t, \tag{1}
$$
and fits $\beta_0, \beta$ by minimizing the squared-error loss $\sum_t (y_t - \mu_t)^2$.

**Nonlinear autoregression** keeps this setup — a covariate $x_t$ built from the lags, a loss that
penalizes $(y_t - \mu_t)^2$ — and only replaces (1) with a nonlinear function of $x_t$. The question
is which nonlinear function to use.

## A hinge-function nonlinear AR(1) model

Take $p = 1$, so $x_t = y_{t-1}$ is a scalar. A **hinge function** (or ramp function) at a knot $c$
is
$$
(x - c)_+ = \max(x - c, 0):
$$
it is zero up to $c$ and rises with slope 1 beyond it — a straight line with a single kink at $c$.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="the hinge function (x minus c) positive part, flat then kinking upward at the knot c">
  <line x1="30" y1="170" x2="300" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="170" x2="30" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="295" y="188" text-anchor="middle" font-size="12" fill="currentColor">x</text>
  <text x="14" y="28" text-anchor="middle" font-size="12" fill="currentColor">(x-c)&#8314;</text>
  <line x1="30" y1="170" x2="170" y2="170" stroke="currentColor" stroke-width="2"/>
  <line x1="170" y1="170" x2="280" y2="45" stroke="currentColor" stroke-width="2"/>
  <line x1="170" y1="170" x2="170" y2="180" stroke="currentColor" stroke-width="1"/>
  <text x="170" y="196" text-anchor="middle" font-size="12" fill="currentColor">c</text>
</svg>
<figcaption>The hinge function $(x-c)_+$: zero to the left of the knot $c$, then rising with slope
one. A sum of these, one per knot, is a piecewise-linear function that can bend as often as there
are knots.</figcaption>
</figure>

A simple nonlinear AR(1) model takes $\mu_t$ to be a linear combination of $x_t$ itself and hinge
functions of $x_t$ at knots $c_1, \dots, c_k$:
$$
\mu_t = \beta_0 + \beta_1 x_t + \beta_2 (x_t - c_1)_+ + \dots + \beta_{k+1} (x_t - c_k)_+.
$$

This can be simplified by dropping the separate linear term $\beta_1 x_t$. The reason it costs
nothing to drop is the identity
$$
x_t = (x_t - c_0)_+ + c_0
$$
for any knot $c_0$ placed below every observed value of $x_t$ — since then $x_t - c_0$ is always
positive and the hinge is just $x_t - c_0$ itself. So a plain linear term is already representable
as a hinge function at a sufficiently low knot, plus a constant that the intercept $\beta_0$ absorbs.
Dropping it and renaming the remaining knots gives the model in its simplified form:
$$
\mu_t = \beta_0 + \beta_1 (x_t - c_1)_+ + \dots + \beta_k (x_t - c_k)_+.
$$
Fitting proceeds exactly as in the linear case — minimize $\sum_t (y_t - \mu_t)^2$ — except now the
mean is a sum of $k$ hinge functions of the single lag $x_t$ rather than a single linear function of
it.

## Toward a neural-network form

The lecture then starts rewriting this sum of hinges in vector notation, evidently heading toward
the same form used for a single-hidden-layer neural network — consistent with the "input" language
already used for $x_t$. It introduces, for each $t$, the vector of shifted covariates
$$
s_t = (x_t - c_1, \dots, x_t - c_k)^T,
$$
and applies the positive-part function componentwise to get
$$
r_t = \sigma(s_t),
$$
so that the $j$-th entry of $r_t$ is exactly the hinge term $(x_t - c_j)_+$ used above. **The
transcribed material breaks off at this point**, in the middle of rewriting $\mu_t$ in terms of
$r_t$ — the natural next line would express $\mu_t$ as an intercept plus a linear combination of the
entries of $r_t$, i.e. $\beta_0 + \beta^T r_t$, but that line is not present in the source and is not
reconstructed here.

## Sources

- Notes: `LectureTwentyFive153248Spring2025.md` (STAT 153 & 248, UC Berkeley, Spring 2025, Lecture
  25, Aditya Guntuboyina, April 29, 2025), Section 1 "Nonlinear AutoRegression" — the entire chapter.
- The source document is itself an incomplete machine transcription of the lecture PDF: it ends
  mid-equation immediately after introducing $r_t = \sigma(s_t)$, before stating the resulting form
  of $\mu_t$. Nothing past that point is available in the supplied material, so the chapter stops
  there rather than completing the derivation.
- The lecture explicitly refers back to "the last lecture," where nonlinear autoregression was
  first introduced; that earlier lecture was not supplied and is not covered here.
- No slides, transcript, or exercises were supplied for this lecture (all empty in the task inputs).

---

[← 119. MA Models and AR(p) Stationarity](119-ma-models-and-ar-p-stationarity.md) · [Contents](index.md) · [121. From Regression to RNNs →](121-from-regression-to-rnns.md)
