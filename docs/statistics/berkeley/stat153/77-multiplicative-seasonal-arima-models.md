---
title: "77. Multiplicative Seasonal ARIMA Models"
course: "Berkeley Stat 153"
chapter: 77
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 77. Multiplicative Seasonal ARIMA Models

## What this covers

This lecture asks how to model a time series that repeats itself on a fixed calendar cycle —
monthly data with a yearly pattern is the running case — and answers it by building a second,
"seasonal" ARMA structure on top of the ordinary one, multiplying the two together rather than
adding them. It assumes the reader already has ARMA$(p,q)$, ARIMA$(p,d,q)$, the backshift operator
$B$, and how to read a sample ACF/PACF, from earlier lectures in the course.

## Recap: ARMA and ARIMA

An $\mathrm{ARMA}(p,q)$ model is written in terms of the backshift operator $B$, where $By_t=y_{t-1}$,
as

$$\phi(B)(y_t-\mu)=\theta(B)\varepsilon_t,$$

with $\phi$ and $\theta$ the AR and MA polynomials built up in previous lectures. The model is
causal and stationary exactly when every root of $\phi(z)$ lies outside the unit circle, i.e. has
modulus greater than $1$.

Differencing is repeated application of $(I-B)$:

$$y\ \to\ \underbrace{(I-B)y}_{y_t-y_{t-1}}\ \to\ (I-B)^2y = y_t-2y_{t-1}+y_{t-2}.$$

Differencing $d$ times before fitting an ARMA model gives $\mathrm{ARIMA}(p,d,q)$:

$$\phi(B)\big((I-B)^d y-\mu\big)=\theta(B)\varepsilon_t,$$

fit in software as `ARIMA(data, order=(p, d, q))`. As a rule of thumb, $d\le 2$ and $p,q\le 5$ cover
the cases that come up in practice — $d=0,1,2$ corresponding to no differencing, $y_t-y_{t-1}$, and
$y_t-2y_{t-1}+y_{t-2}$.

## Why an ordinary ARMA model cannot capture seasonality

Monthly data very often carries a pattern that repeats every twelve observations. Suppose we want a
model whose autocorrelation is zero everywhere except at lag $12$:

$$\mathrm{ACF}(h)=\begin{cases}1 & h=0\\ \ne0 & h=12\\ 0 & \text{otherwise.}\end{cases}$$

An ordinary $\mathrm{MA}(1)$, $y_t=\mu+\varepsilon_t+\theta\varepsilon_{t-1}$, has
$\mathrm{ACF}(1)=\theta/(1+\theta^2)$ and nothing elsewhere — a spike at the wrong lag. The fix is to
put the moving-average term twelve steps back instead of one:

$$y_t=\mu+\varepsilon_t+\theta\varepsilon_{t-12}.$$

Checking the covariance directly,

$$\mathrm{Cov}(y_t,y_{t+h})=\mathrm{Cov}(\varepsilon_t+\theta\varepsilon_{t-12},\,\varepsilon_{t+h}+\theta\varepsilon_{t+h-12}),$$

which is nonzero only when an index on the left matches one on the right, i.e. only for
$h=0,12,-12$ — exactly the pattern wanted. This is a **seasonal $\mathrm{MA}(1)$ with period 12**,
written with $B^{12}y_t=y_{t-12}$ as

$$y_t-\mu=\Theta(B^{12})\varepsilon_t,\qquad \Theta(z)=1+\Theta z.$$

The same idea generalizes: a **seasonal $\mathrm{ARMA}(P,Q)$ with period $s$** is

$$\Phi(B^s)(y_t-\mu)=\Theta(B^s)\varepsilon_t,$$

an ordinary $\mathrm{ARMA}(P,Q)$ built out of $B^s$ instead of $B$. Because it only ever links
observations a whole multiple of $s$ apart, **its ACF and PACF have exactly the shape of an
ordinary $\mathrm{ARMA}(P,Q)$'s, relocated to lags that are multiples of $s$**: whatever would sit
at lag $k$ in the non-seasonal version sits at lag $ks$ here. The lecture illustrated this by
comparing the ACF/PACF of $\mathrm{MA}(2)$ against a seasonal $\mathrm{MA}(2)$ with period $s$, and
by fitting a plain $\mathrm{MA}(1)$ to the CO2 series and then a seasonal $\mathrm{MA}(1)$ with
$s=12$ — as board plots that are not reproduced here (see Sources).

## Multiplicative seasonal ARMA

A real series usually needs both kinds of structure at once: a short-run $\mathrm{ARMA}(p,q)$ near
lag $0$, and a seasonal $\mathrm{ARMA}(P,Q)$ with period $s$ near lags $s,2s,\dots$. The two are
combined **multiplicatively**, not added:

$$\phi(B)\Phi(B^s)(y_t-\mu)=\theta(B)\Theta(B^s)\varepsilon_t.$$

**Worked example: $\mathrm{MA}(1)\times\mathrm{MA}(1)_{12}$.** Take a regular
$\mathrm{MA}(1)$, $y_t-\mu=\theta(B)\varepsilon_t$ with $\theta(z)=1+\theta z$, together with a
seasonal $\mathrm{MA}(1)$ of period $12$, $y_t-\mu=\Theta(B^{12})\varepsilon_t$. Their product is

$$y_t-\mu=(1+\theta B)(1+\Theta B^{12})\varepsilon_t=\varepsilon_t+\theta\varepsilon_{t-1}+\Theta\varepsilon_{t-12}+\theta\Theta\varepsilon_{t-13},$$

a special case of $\mathrm{MA}(13)$ in which only $4$ of the $13$ possible coefficients are
nonzero. To find its ACF, compare which $\varepsilon$-indices $y_t$ and $y_{t+h}$ share. For
$h=11$:

$$y_t=\varepsilon_t+\theta\varepsilon_{t-1}+\Theta\varepsilon_{t-12}+\theta\Theta\varepsilon_{t-13},\qquad
y_{t+11}=\varepsilon_{t+11}+\theta\varepsilon_{t+10}+\Theta\varepsilon_{t-1}+\theta\Theta\varepsilon_{t-2}.$$

The only shared index is $t-1$, entering $y_t$ with coefficient $\theta$ and $y_{t+11}$ with
coefficient $\Theta$, so $\mathrm{Cov}(y_t,y_{t+11})=\theta\Theta\sigma^2$. Running the same check
at every $h$ gives nonzero autocorrelation only at $h=0,1,11,12,13$:

$$\mathrm{ACF}(h)=\begin{cases}
1 & h=0\\
\dfrac{\theta}{1+\theta^2} & h=1\\[4pt]
\dfrac{\Theta}{1+\Theta^2} & h=12\\[4pt]
\dfrac{\theta\Theta}{(1+\theta^2)(1+\Theta^2)} & h=11,13\\[2pt]
0 & \text{otherwise.}
\end{cases}$$

The two flanking values are not an independent feature of the model — they are exactly the product
of the lag-$1$ and lag-$12$ values, $\mathrm{ACF}(11)=\mathrm{ACF}(13)=\mathrm{ACF}(1)\cdot\mathrm{ACF}(12)$,
which is what multiplying the two factors together buys you: a short-run bump, a seasonal bump, and
a pair of cross terms straddling the seasonal lag where the two overlap.

<figure>
<svg viewBox="0 0 420 200" role="img" aria-label="Stem plot of the autocorrelation of the multiplicative MA(1) times seasonal MA(1) with period 12 model">
  <line x1="30" y1="170" x2="390" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <text x="400" y="174" font-size="12" fill="currentColor">h</text>
  <text x="150" y="167" text-anchor="middle" font-size="12" fill="currentColor">…</text>
  <text x="370" y="167" text-anchor="middle" font-size="12" fill="currentColor">…</text>

  <line x1="40" y1="170" x2="40" y2="40" stroke="currentColor" stroke-width="2"/>
  <circle cx="40" cy="40" r="3" fill="currentColor"/>
  <text x="40" y="185" text-anchor="middle" font-size="12" fill="currentColor">0</text>

  <line x1="64" y1="170" x2="64" y2="115" stroke="currentColor" stroke-width="2"/>
  <circle cx="64" cy="115" r="3" fill="currentColor"/>
  <text x="64" y="185" text-anchor="middle" font-size="12" fill="currentColor">1</text>

  <line x1="304" y1="170" x2="304" y2="152" stroke="#d97706" stroke-width="2"/>
  <circle cx="304" cy="152" r="3" fill="#d97706"/>
  <text x="304" y="185" text-anchor="middle" font-size="12" fill="currentColor">11</text>

  <line x1="328" y1="170" x2="328" y2="125" stroke="currentColor" stroke-width="2"/>
  <circle cx="328" cy="125" r="3" fill="currentColor"/>
  <text x="328" y="185" text-anchor="middle" font-size="12" fill="currentColor">12</text>

  <line x1="352" y1="170" x2="352" y2="152" stroke="#d97706" stroke-width="2"/>
  <circle cx="352" cy="152" r="3" fill="#d97706"/>
  <text x="352" y="185" text-anchor="middle" font-size="12" fill="currentColor">13</text>

  <text x="10" y="45" font-size="12" fill="currentColor">1</text>
  <text x="205" y="16" text-anchor="middle" font-size="12" fill="currentColor">ACF(h) of MA(1) × MA(1) period 12</text>
</svg>
<figcaption>Nonzero autocorrelation sits only at lag 0, the short lag 1, the seasonal lag 12, and
the two lags flanking it. The flanking values (amber) are not fitted separately: they equal the
product of the lag-1 and lag-12 values.</figcaption>
</figure>

The lecture's heuristic for reading the ACF/PACF of a general multiplicative model — sketched for
$\mathrm{MA}(2)\times\mathrm{MA}(2)_{12}$ on the board but not carried through in equations — is the
same idea one level up: near lag $0$ the correlogram looks like the non-seasonal factor's; near
each multiple of $s$ it looks like the seasonal factor's; and, as in the worked example, cross terms
appear at the lags straddling each seasonal multiple where the two factors' index ranges overlap.

## SARIMA: multiplicative ARMA with two kinds of differencing

Putting differencing back in gives the full model fit in practice. There are now two differencing
operators available before the multiplicative ARMA step: an ordinary difference $(I-B)^d$, as
before, and a **seasonal difference** $(I-B^s)^D$, which differences a value against the same point
in the previous cycle. Preprocessing the raw series with both,

$$x_t=(I-B^s)^D(I-B)^d y_t,$$

and then fitting a multiplicative seasonal ARMA to $x_t$,

$$\Phi(B^s)\phi(B)(x_t-\mu)=\Theta(B^s)\theta(B)\varepsilon_t,$$

gives, written out in terms of the original series $y_t$,

$$\Phi(B^s)\phi(B)\Big((I-B^s)^D(I-B)^d y_t-\mu\Big)=\Theta(B^s)\theta(B)\varepsilon_t.$$

This is a **SARIMA** model, denoted $\mathrm{SARIMA}(p,d,q)\times(P,D,Q)_s$ and fit in software as
`ARIMA(data, order=(p, d, q), seasonal_order=(P, D, Q, s))`. It has three pieces working together:
ordinary differencing and short-run ARMA handle trend and short-range dependence, and seasonal
differencing and seasonal ARMA handle a recurring pattern at period $s$.

## Sources

Everything above is from the single input supplied for this lecture: the handwritten notes
`HandwrittenNotesLectureTwentyThree153248Fall2025.md` (Berkeley STAT 153, Fall 2025, licensed CC BY
4.0). No slide deck, transcript, or problem set was supplied for this lecture, so there is no
Exercises section.

That source is itself a caveat: the original PDF has no text layer, so a model read the handwritten
pages and reconstructed the markdown — the notes themselves flag the prose as paraphrase in places
and every equation as unverified. This chapter follows the notes' equations and worked example
(the $\mathrm{MA}(1)\times\mathrm{MA}(1)_{12}$ covariance computation) as given, but they should be
checked against the lecture recording or a textbook treatment of SARIMA before being relied on.

The source also refers to material it does not actually contain: board plots of the ACF/PACF for
$\mathrm{MA}(2)$ versus a seasonal $\mathrm{MA}(2)$, a fitted $\mathrm{MA}(1)$ (then seasonal
$\mathrm{MA}(1)$ with $s=12$) for the CO2 data, and a sketch of the ACF/PACF heuristic for
$\mathrm{MA}(2)\times\mathrm{MA}(2)_{12}$. These appear in the notes only as section headers or
axis labels with no accompanying data or curves, and are described qualitatively above rather than
invented in full.

---

[← 76. Neural Network Models for Time Series](76-neural-network-models-for-time-series.md) · [Contents](index.md) · [78. ARMA and ARIMA Models →](78-arma-and-arima-models.md)
