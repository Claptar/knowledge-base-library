---
title: "114. AR Models and Sunspots"
course: "Berkeley Stat 153 Fall 2024"
chapter: 114
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 114. AR Models and Sunspots

## What this covers

This chapter introduces the Auto-Regressive, or $AR(p)$, model: a time series regressed on its own
past values. It sets up $AR(p)$ as an ordinary linear regression in disguise, shows how it is used
to forecast, and then works through the reason Yule invented it in the first place — the sunspot
counts, and the observation that a sinusoid can be described either as a curve or as the solution
of a difference equation. It assumes familiarity with ordinary least squares and with fitting a
single-sinusoid regression model (the $\cos/\sin$ model used earlier for the sunspots data).

## The $AR(p)$ model as a regression

We observe a time series $y_1, \dots, y_n$. The $AR(p)$ model says that $y_t$ is a linear function
of its own $p$ most recent values, plus noise:

$$y_t = \phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t, \qquad t = p+1, \dots, n. \tag{1}$$

This is exactly a linear regression, $Y = X\beta + \epsilon$, once the covariates are read off the
same series as the response:

$$Y = \begin{pmatrix} y_{p+1} \\ y_{p+2} \\ \vdots \\ y_n \end{pmatrix}, \qquad
X = \begin{pmatrix}
1 & y_p & y_{p-1} & \cdots & y_1 \\
1 & y_{p+1} & y_p & \cdots & y_2 \\
1 & y_{p+2} & y_{p+1} & \cdots & y_3 \\
\vdots & \vdots & \vdots & & \vdots \\
1 & y_{n-1} & y_{n-2} & \cdots & y_{n-p}
\end{pmatrix}, \qquad
\beta = \begin{pmatrix} \phi_0 \\ \phi_1 \\ \vdots \\ \phi_p \end{pmatrix}, \qquad
\epsilon = \begin{pmatrix} \epsilon_{p+1} \\ \vdots \\ \epsilon_n \end{pmatrix}.$$

The model is called "auto"-regression precisely because the response column and the covariate
columns are all built out of the one series $y_t$: row $t$ regresses $y_t$ on the $p$ values that
immediately precede it. Nothing about fitting it is new — $\phi_0, \dots, \phi_p$ are estimated by
ordinary least squares, minimizing $\|Y - X\beta\|^2$, giving estimates $\hat\phi_0, \dots,
\hat\phi_p$. What is new is what the design matrix is made of.

## Forecasting from a fitted $AR(p)$ model

Because the model expresses $y_t$ in terms of the past, a fitted $AR(p)$ model forecasts forward by
just plugging in $t = n+1, n+2, \dots$. For $y_{n+1}$,

$$\hat y_{n+1} = \hat\phi_0 + \hat\phi_1 y_n + \hat\phi_2 y_{n-1} + \dots + \hat\phi_p y_{n+1-p},$$

and every value on the right is observed — it is the last $p$ points of the series. For $y_{n+2}$,
equation (1) with $t = n+2$ calls for $y_{n+1}$, which has not been observed yet. The fix is to use
the forecast in its place:

$$\hat y_{n+2} = \hat\phi_0 + \hat\phi_1 \hat y_{n+1} + \hat\phi_2 y_n + \dots + \hat\phi_p y_{n+2-p}.$$

This is the general pattern: forecasts further out are generated recursively, feeding earlier
forecasts back in as if they were data,

$$\hat y_{n+i} = \hat\phi_0 + \hat\phi_1 \hat y_{n+i-1} + \dots + \hat\phi_p \hat y_{n+i-p}, \qquad i = 1, 2, \dots,$$

initialized with $\hat y_j = y_j$ for the last $p$ observed indices $j = n, n-1, \dots, n+1-p$.

## Where the model comes from: Yule and the sunspots

Earlier, the sunspot series was modeled as a single noisy sinusoid,

$$y_t = \beta_0 + \beta_1\cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t, \qquad t = 1,\dots,n, \tag{2}$$

and a Bayesian argument was used to infer the frequency $f$, landing on a period close to 11 years
— the period usually quoted for the solar cycle. But (2) is not a good description of the data on
two counts: the fit is poor, because some of the real oscillations have amplitude well beyond what
a single sinusoid can produce, and series simulated from (2) look far noisier than actual sunspot
counts do. Yule's response, in the 1927 paper that effectively invented AR modeling, was to keep the
idea that a single sinusoid drives the series but to change *where the randomness enters*. That
change is exactly the $AR(p)$ idea, and to see why it fixes the two problems it helps to first
understand a sinusoid in a different light: as the solution of a difference equation rather than as
a curve given by a formula.

## A sinusoid as the solution of a difference equation

Write $s_t = \beta_0 + \beta_1\cos(2\pi f t) + \beta_2\sin(2\pi f t)$ for the noiseless sinusoid, and
$\omega = 2\pi f$. In continuous time, the analogous function $s(t)$ satisfies the differential
equation

$$s''(t) = -\omega^2\big(\beta_1\cos(\omega t) + \beta_2 \sin(\omega t)\big) = -\omega^2\big(s(t) - \beta_0\big). \tag{4}$$

A second derivative is a limit of a second difference, so the discrete-time analogue of (4) should
be a statement about $s_t - 2s_{t-1} + s_{t-2}$. Indeed:

$$s_t - 2s_{t-1} + s_{t-2} = 2(\cos\omega - 1)\big(s_{t-1} - \beta_0\big). \tag{5}$$

To check this, expand the left side in terms of $\beta_1, \beta_2$ and the cosine and sine parts
separately. With $A = \omega(t-1)$ and $B = \omega$,

$$\cos(\omega t) - 2\cos(\omega(t-1)) + \cos(\omega(t-2)) = \cos(A+B) - 2\cos A + \cos(A - B) = 2\cos A(\cos B - 1) = 2(\cos\omega - 1)\cos(\omega(t-1)),$$

and the same manipulation on the sine terms gives $2(\cos\omega - 1)\sin(\omega(t-1))$. Adding the
two pieces back with their $\beta_1,\beta_2$ coefficients gives exactly
$2(\cos\omega-1)(s_{t-1}-\beta_0)$, which is (5).

The converse also holds: any sequence satisfying the recurrence (5), started from two initial
values $s_1, s_2$, is of the form $s_t = \beta_0 + \beta_1\cos(\omega t) + \beta_2 \sin(\omega t)$
for some choice of $\beta_1, \beta_2$ (with $\beta_0$ fixed by the recurrence). The argument is an
induction. Let $g_t = s_t - \beta_0$, so that $g_t - 2g_{t-1} + g_{t-2} = 2(\cos\omega - 1)g_{t-1}$,
i.e. $g_t = (2\cos\omega) g_{t-1} - g_{t-2}$. Choose $\beta_1, \beta_2$ so that
$h_t := \beta_1\cos(\omega t) + \beta_2\sin(\omega t)$ agrees with $g_t$ at $t = 1, 2$ — this is
just two linear equations in two unknowns. Now suppose $g_{t-1} = h_{t-1}$ and $g_{t-2} = h_{t-2}$.
Then

$$g_t = (2\cos\omega) h_{t-1} - h_{t-2} = \beta_1\big(2\cos\omega\cos(\omega(t-1)) - \cos(\omega(t-2))\big) + \beta_2\big(2\cos\omega\sin(\omega(t-1)) - \sin(\omega(t-2))\big).$$

A short trigonometric check shows $2\cos\omega\cos(\omega(t-1)) - \cos(\omega(t-2)) = \cos(\omega t)$
and likewise for sine, so $g_t = \beta_1\cos(\omega t) + \beta_2 \sin(\omega t) = h_t$. Since the base
case $t=1,2$ holds by construction, induction gives $g_t = h_t$ for every $t$, which is the claim.

So the recurrence (5) and the sinusoid (3) describe exactly the same object, viewed two ways. Solved
forward, (5) reads

$$s_t = (2\cos\omega)\, s_{t-1} - s_{t-2} + 2(1-\cos\omega)\beta_0. \tag{5'}$$

## Two ways to add noise to a sinusoid

Equation (5') is deterministic — it reproduces the sinusoid exactly, forever. Yule's move was to add
noise to the *recurrence* itself rather than to the curve, giving

$$y_t = \phi_0 + \phi_1 y_{t-1} - y_{t-2} + \epsilon_t, \qquad \epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2), \tag{6}$$

with $\phi_1$ playing the role of $2\cos\omega$ and $\phi_0$ the role of $2(1-\cos\omega)\beta_0$.
Model (6) is, like (2), "a sinusoid plus noise" — but the noise sits in a different place, and that
placement is the entire content of Yule's idea.

The difference is easiest to see through the physical situation that produces sinusoids in the
first place: a mass on a spring. Let $\beta_0$ be the rest position, $\kappa$ the spring constant,
and $y(t)$ the mass's displacement at time $t$. Hooke's law gives a restoring force
$F = -\kappa(y(t) - \beta_0)$, and Newton's law $F = my''(t)$ then gives

$$y''(t) = -\omega^2\big(y(t) - \beta_0\big), \qquad \omega := \sqrt{\kappa/m},$$

whose solutions are exactly the sinusoids $y(t) = \beta_0 + \beta_1\cos(\omega t) + \beta_2\sin(\omega t)$.
Now compare the two ways of taking noisy measurements of this system:

- **Model (2): measurement noise.** The mass moves perfectly sinusoidally, but every reading of its
  position is corrupted by independent noise $\epsilon_t \sim N(0,\sigma^2)$ — an instrument-error
  model.
- **Model (6): process noise.** The measuring instrument is perfect, but the mass itself is not
  moving in a perfect sinusoid — its motion is buffeted by outside disturbances at every step. Yule's
  own image was of children randomly throwing stones at the mass, sometimes from the left and
  sometimes from the right, while it oscillates.

These give visibly different data. A series generated from (6) looks much smoother than one
generated from (2), because in (6) the randomness only ever nudges the *next* value away from where
the recurrence would otherwise send it, and the recurrence itself has memory — a nudge at time $t$
still shapes $y_{t+1}$ through $\phi_1 y_t$. In (2) each observation's noise is independent of every
other observation's, so the series can jump around from one point to the next with none of that
carried-over smoothness. This is exactly the mismatch that made (2) a bad model for the sunspots
series in the first place, and it is what led Yule to (6).

## From Yule's model to $AR(2)$

Model (6) is a special case of the general $AR(2)$ model

$$y_t = \phi_0 + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \epsilon_t, \tag{7}$$

obtained by fixing $\phi_2 = -1$ rather than estimating it. Yule fit both (6) and the freely
estimated $AR(2)$ model (7) to the sunspots data, and the two make qualitatively different forecasts:
(6), with $\phi_2$ pinned at $-1$, forecasts a sinusoid that keeps oscillating at constant amplitude
forever, while (7), with $\phi_2$ estimated from the data, forecasts a *damped* sinusoid whose
amplitude shrinks toward the mean.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Two forecast paths from an AR(2) fit: a constant-amplitude sinusoid when phi_2 is fixed at minus one, against a damped sinusoid when phi_2 is estimated freely">
  <line x1="20" y1="100" x2="320" y2="100" stroke="currentColor" stroke-width="1" stroke-opacity="0.4"/>
  <polyline points="30.0,100.0 34.7,77.1 39.3,56.7 44.0,41.1 48.7,32.0 53.3,30.3 58.0,36.3 62.7,49.4 67.3,68.0 72.0,90.1 76.7,113.3 81.3,135.1 86.0,153.0 90.7,165.0 95.3,169.9 100.0,167.1 104.7,156.9 109.3,140.5 114.0,119.6 118.7,96.5 123.3,73.8 128.0,54.0 132.7,39.3 137.3,31.2 142.0,30.7 146.7,37.9 151.3,51.9 156.0,71.2 160.7,93.6 165.3,116.8 170.0,138.1 174.7,155.2 179.3,166.2 184.0,170.0 188.7,166.0 193.3,154.8 198.0,137.6 202.7,116.2 207.3,93.0 212.0,70.6 216.7,51.4 221.3,37.6 226.0,30.7 230.7,31.3 235.3,39.6 240.0,54.5 244.7,74.4 249.3,97.1 254.0,120.2 258.7,141.0 263.3,157.3 268.0,167.3 272.7,169.9 277.3,164.8 282.0,152.6 286.7,134.6 291.3,112.7 296.0,89.5 300.7,67.4 305.3,49.0 310.0,36.1"
    fill="none" stroke="currentColor" stroke-width="1.6"/>
  <polyline points="30.0,100.0 34.7,77.8 39.3,59.2 44.0,46.2 48.7,39.7 53.3,40.0 58.0,46.8 62.7,59.0 67.3,74.8 72.0,92.5 76.7,109.9 81.3,125.2 86.0,137.0 90.7,144.0 95.3,145.9 100.0,142.8 104.7,135.2 109.3,124.3 114.0,111.4 118.7,98.0 123.3,85.6 128.0,75.5 132.7,68.6 137.3,65.5 142.0,66.3 146.7,70.7 151.3,77.9 156.0,87.2 160.7,97.2 165.3,107.0 170.0,115.5 174.7,121.8 179.3,125.4 184.0,126.0 188.7,123.8 193.3,119.2 198.0,112.8 202.7,105.3 207.3,97.8 212.0,90.9 216.7,85.4 221.3,81.8 226.0,80.3 230.7,81.1 235.3,83.9 240.0,88.2 244.7,93.6 249.3,99.3 254.0,104.8 258.7,109.4 263.3,112.8 268.0,114.6 272.7,114.7 277.3,113.2 282.0,110.4 286.7,106.6 291.3,102.4 296.0,98.1 300.7,94.3 305.3,91.3 310.0,89.4"
    fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/>
  <text x="312" y="34" font-size="12" fill="currentColor">$\phi_2=-1$</text>
  <text x="312" y="93" font-size="12" fill="currentColor">$\phi_2$ estimated</text>
</svg>
<figcaption>Forecasts from the two AR(2) fits share the same start but diverge: pinning
$\phi_2 = -1$ (solid) keeps the oscillation going at constant amplitude, while letting $\phi_2$ be
estimated (dashed) typically damps the amplitude back toward the mean.</figcaption>
</figure>

The chapter that follows takes up $AR(p)$ models in general — in particular, how the choice of
$\phi_1, \dots, \phi_p$ governs whether forecasts oscillate, damp, or explode.

## Sources

- Both sections of this chapter are drawn from Lecture Sixteen, "2 AR (Auto-Regressive) Models" and
  "3 AR Models for the Sunspots Data," UC Berkeley Stat 153, Aditya Guntuboyina. The regression
  formulation of $AR(p)$ and the forecasting recursion are common to both the fall-2025 (October 23,
  2025) and spring-2025 (March 13, 2025) offerings; the sunspots motivation, the difference-equation
  derivation, the spring analogy, and the $AR(2)$ comparison are taken from the spring-2025 file
  (`02-3-ar-models-for-the-sunspots-data.md`), whose text is complete, in preference to the
  fall-2025 file of the same title, which is cut off mid-sentence partway through the spring
  analogy.
- The lecture names, but does not reproduce, three outside sources: G. U. Yule (1927), "On a Method
  of Investigating Periodicities Disturbed Series, with Special Reference to Wolfer's Sunspot
  Numbers," *Philosophical Transactions of the Royal Society of London* A 226(636–646), 267–298 —
  the original paper this chapter's motivation follows; T. C. Mills (2011), *The Foundations of
  Modern Time Series Analysis*, Chapter 6, described as a secondary account of Yule's paper; and
  Stein and Shakarchi's *Fourier Analysis*, page 2, cited for the mass-on-a-spring example. None of
  the three is included in the supplied material.
- No slides or transcript were supplied for this chapter; the two markdown files per year are
  themselves a model's reconstruction of the lecture PDF (flagged in each file as "reconstructed,"
  with prose paraphrased and every equation unverified against the original).

---

[← 113. Broken-Stick Regression](113-broken-stick-regression.md) · [Contents](index.md) · [115. High-Dimensional Regression and Regularization →](115-high-dimensional-regression-and-regularization.md)
