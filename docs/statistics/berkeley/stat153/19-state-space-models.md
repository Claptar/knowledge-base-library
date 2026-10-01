---
title: "19. State Space Models"
course: "Berkeley Stat 153"
chapter: 19
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 19. State Space Models

## What this covers

Every model so far in the course — regression, AR, ARIMA — fits a series $y_t$ directly. This
chapter asks what happens when $y_t$ is not the quantity of interest at all, but a noisy,
partial measurement of some other process $x_t$ that we never see. It builds the state space
model (also called the dynamic linear model, DLM) that formalizes this, works through the linear
Gaussian version in detail, and follows one worked biomedical example — monitoring a bone marrow
transplant from three blood markers with 40% missing data — from raw variables to fitted
parameters. It assumes the AR(1) and VAR-style vector generalization of AR, and the language of
white noise and covariance matrices; the reading behind it is Shumway and Stoffer, Ch. 5.5 and
6–6.1.

## From a fixed coefficient to a hidden process

Ordinary regression writes $y_t = X\beta + \epsilon$ and treats $\beta$ as a fixed unknown
constant, estimated once from the data. The natural generalization is to let $\beta$ drift over
time: $\beta_t = \beta_{t-1} + \eta_t$, with $y_t = X\beta_t + \epsilon$. The moment $\beta$ is
allowed to be time-varying and only inferred through $y_t$, this is already a state space model —
the "state" is the time-varying coefficient $\beta_t$, which is never observed directly.

A second route to the same idea starts from an AR(1) process, $x_t = \phi x_{t-1} + w_t$. Suppose
$x_t$ itself is not observed, and all that is available is a noisy version of it,
$y_t = x_t + v_t$. The pair of equations — a state equation $x_t = \phi x_{t-1} + w_t$ describing
how the hidden signal evolves, and an observation equation $y_t = x_t + v_t$ describing how it is
measured — is a state space model.

Both examples share the same two organizing principles, stated generally:

1. There is a hidden, or **latent, state process** $x_t$. It is a **Markov process**: conditional
   on the present state $x_t$, the future $\{x_s : s>t\}$ and the past $\{x_s : s<t\}$ are
   independent.
2. The **observations** $y_t$ are independent given the states $x_t$. Any dependence between the
   observations — the reason $y_1$ tells you something about $y_5$ — is entirely inherited through
   the states; nothing in the observation process itself carries memory.

<figure>
<svg viewBox="0 0 460 220" role="img" aria-label="A hidden Markov chain of states, each generating one noisy, conditionally independent observation">
  <defs>
    <marker id="da38-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <circle cx="80" cy="50" r="26" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="80" y="55" text-anchor="middle" font-size="13" fill="currentColor">xₜ₋₁</text>

  <circle cx="230" cy="50" r="26" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="230" y="55" text-anchor="middle" font-size="13" fill="currentColor">xₜ</text>

  <circle cx="380" cy="50" r="26" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="380" y="55" text-anchor="middle" font-size="13" fill="currentColor">xₜ₊₁</text>

  <line x1="106" y1="50" x2="204" y2="50" stroke="currentColor" stroke-width="1.5" marker-end="url(#da38-arrow)"/>
  <line x1="256" y1="50" x2="354" y2="50" stroke="currentColor" stroke-width="1.5" marker-end="url(#da38-arrow)"/>

  <rect x="55" y="150" width="50" height="34" rx="4" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <text x="80" y="171" text-anchor="middle" font-size="13" fill="currentColor">yₜ₋₁</text>

  <rect x="205" y="150" width="50" height="34" rx="4" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <text x="230" y="171" text-anchor="middle" font-size="13" fill="currentColor">yₜ</text>

  <rect x="355" y="150" width="50" height="34" rx="4" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <text x="380" y="171" text-anchor="middle" font-size="13" fill="currentColor">yₜ₊₁</text>

  <line x1="80" y1="76" x2="80" y2="148" stroke="currentColor" stroke-width="1.5" marker-end="url(#da38-arrow)"/>
  <line x1="230" y1="76" x2="230" y2="148" stroke="currentColor" stroke-width="1.5" marker-end="url(#da38-arrow)"/>
  <line x1="380" y1="76" x2="380" y2="148" stroke="currentColor" stroke-width="1.5" marker-end="url(#da38-arrow)"/>
</svg>
<figcaption>The state chain runs along the top, hidden; each observation below depends only on the
state directly above it. Correlation between $y_{t-1}$ and $y_{t+1}$ exists only because it is
carried through $x_t$.</figcaption>
</figure>

## A building block: from AR to VAR

Before assembling the general model, it helps to have the vector generalization of AR(1) in hand.
Everything discussed under AR so far has been a single series. When $k$ series influence each
other, the **vector autoregressive (VAR) model** writes

$$x_t = \alpha + \Phi x_{t-1} + w_t,$$

where $x_t$ is now a $k$-vector and $\Phi$ is a $k\times k$ **transition matrix** expressing how
all of $x_{t-1}$'s components feed into $x_t$. A state space model is a further generalization of
this: it keeps a VAR-like equation for the hidden state, but adds a second equation for how that
state is actually measured.

## The linear Gaussian model

The linear Gaussian state space model — also called the **dynamic linear model (DLM)** — pairs a
vector-autoregressive **state equation**

$$x_t = \Phi x_{t-1} + \Upsilon u_t + w_t, \qquad w_t \overset{iid}{\sim} N_p(0, Q), \qquad x_0 \sim N_p(\mu_0, \sigma_0),$$

with an **observation equation**

$$y_t = A_t x_t + \Gamma u_t + v_t, \qquad v_t \sim N_q(0, R).$$

Reading off each piece:

- $x_t$ is $p$-dimensional and hidden. $\Phi$, a $p\times p$ matrix, is the state transition
  parameter: it describes the internal dynamics, how the state at $t-1$ produces the state at $t$.
- $u_t$ is an $r$-dimensional **fixed input series** — covariates, experimental conditions,
  interventions, anything supplied rather than learned from the data.
- $\Upsilon$ ($p\times r$) controls how those inputs move the *state*; $w_t$ is the state noise,
  covariance $Q$.
- $y_t$ is $q$-dimensional data — $q$ can be larger or smaller than $p$, the state dimension —
  and is a linearly transformed, noisy view of $x_t$.
- $A_t$, a $q\times p$ **measurement (observation) matrix**, picks out which linear combinations
  of the state are actually measured. Letting $A_t$ depend on $t$ is what lets the model handle
  missing data cleanly: for a time point where a measurement is missing, drop the corresponding
  row of $A_t$.
- $v_t$ is measurement noise, covariance $R$; $\Gamma$ ($q\times r$) lets inputs affect the
  *observation* directly, bypassing the state.

So an external input can act on $y_t$ through two different routes: $\Upsilon u_t$ (through the
state) or $\Gamma u_t$ (through the observation). The distinction is the difference between
something that changes the underlying reality and something that only changes how the reality is
reported. Take $x_t$ to be a person's true blood pressure and $y_t$ the reading from a blood
pressure cuff. A drug administered at time $t$ belongs in the state equation, because it changes
the actual blood pressure. Which nurse took the reading, or which cuff was used, belongs in the
observation equation: it changes what the meter reports without touching the underlying
physiology. $\Gamma = 0$ is the common choice, when inputs are believed to only drive the state;
$\Upsilon = 0$ shows up when modeling a known measurement artifact that has no bearing on the true
state at all.

## Worked example: monitoring a bone marrow transplant

As a concrete case, consider three biomedical markers tracked in a cancer patient who has
undergone a bone marrow transplant:

- log(white blood cell count) [WBC] — essential for immune function
- log(platelet count) [PLT] — essential for blood clotting
- hematocrit [HCT] — percentage of red blood cells in total blood volume

Each measures a distinct aspect of bone marrow function, and a transplant is judged successful
once the new marrow is producing all three. As with much longitudinal follow-up data, a large
fraction of the readings are missing — about 40% here, concentrated after day 35. A state space
model can be fit to the three series jointly and used both to estimate those missing values and
to track the trajectory; platelet count at 100 days post-transplant is known from prior work to
predict long-term survival, giving a concrete reason to want a good estimate of it even on days
with no blood draw.

The state equation stacks the three series into a VAR(1):

$$
\begin{pmatrix} x_{t1} \\ x_{t2} \\ x_{t3} \end{pmatrix}
=
\begin{pmatrix}
\phi_{11} & \phi_{12} & \phi_{13} \\
\phi_{21} & \phi_{22} & \phi_{23} \\
\phi_{31} & \phi_{32} & \phi_{33}
\end{pmatrix}
\begin{pmatrix} x_{t-1,1} \\ x_{t-1,2} \\ x_{t-1,3} \end{pmatrix}
+
\begin{pmatrix} w_{t1} \\ w_{t2} \\ w_{t3} \end{pmatrix}.
$$

This is three stacked regressions. Writing out the first row,

$$x_{t1} = \phi_{11}x_{t-1,1} + \phi_{12}x_{t-1,2} + \phi_{13}x_{t-1,3} + w_{t1},$$

today's log(WBC) is a weighted sum of yesterday's WBC, platelets, and hematocrit, plus noise. The
**diagonal** entries measure self-persistence: $\phi_{11}$ near $1$ means WBC changes slowly and
its own recent value strongly predicts tomorrow's; a value near $0$ would say today's value has
almost nothing to do with yesterday's, which would be unusual for a blood marker and would more
plausibly signal a data problem than genuine dynamics. The **off-diagonal** entries $\phi_{ij}$
measure cross-influence: how much yesterday's marker $j$ predicts today's marker $i$ — for
instance $\phi_{12}$ is the effect of yesterday's platelet count on today's WBC, and $\phi_{21}$
the effect of yesterday's WBC on today's platelet count.

The observation equation is $y_t = A_t x_t + v_t$, where the $3\times 3$ matrix $A_t$ is either
the identity or the zero matrix, according to whether a blood sample was actually drawn on day
$t$. This is the missing-data mechanism made concrete: a missing day does not require deleting
that time point or interpolating by hand, it is handled by zeroing out $A_t$ for that day, and the
state equation still propagates an estimate of $x_t$ through it.

Fitting such a model — by maximum likelihood or by the EM algorithm — means estimating:

- $\Phi$: a $3\times 3$ matrix, 9 parameters,
- $Q$: the $3\times 3$ symmetric state noise covariance, 6 free parameters (diagonal plus one set
  of off-diagonals),
- $R$: the $3\times 3$ symmetric observation noise covariance, 6 free parameters (often assumed
  diagonal in practice),
- $\mu_0, \sigma_0$: mean and covariance of the initial state, $3 + 6 = 9$ parameters (sometimes
  fixed from prior knowledge instead of estimated),
- $A$: usually fixed at the identity (up to the missing-data zeroing above), though it can be fit.

In Python, `statsmodels.tsa.statespace` provides the machinery to fit models of this form.

## Filtering, prediction, and smoothing

Given data $y_{1:s} = \{y_1,\dots,y_s\}$, the task of estimating the hidden state $x_t$ splits
into three cases depending on how $s$ compares to $t$:

1. **Filtering** ($s = t$): estimate $x_t$ using only the measurements up through time $t$ — the
   online case, updating the state estimate as each new observation arrives.
2. **Prediction / forecasting** ($s < t$): estimate a *future* state $x_t$ using data only up to
   an earlier time $s$ — projecting the state forward before the later observations exist.
3. **Smoothing** ($s > t$): estimate $x_t$ using the *entire* dataset, including observations that
   came after time $t$. Because it uses more information than filtering does, smoothing gives the
   best estimate of the state at any interior time point — this is exactly what is used to fill in
   the missing values in the bone marrow example, since data collected on later days sharpens the
   estimate of what happened on the missing days in between.

## Other applications

The same two-equation structure recurs across very different measurement problems:

- Estimating global temperature $x_t$ from land and sea temperature measurements $y_t$.
- Brain-computer interfaces: inferring intended cursor velocity $x_t$ from measurements $y_t$ at
  100 electrodes in motor cortex.
- Estimating true blood glucose level $x_t$ from intermittent readings $y_t$ from a continuous
  glucose monitor subject to sensor drift.
- Estimating the volatility $x_t$ of the S&P 500 on day $t$ from the observed daily log return
  $y_t$.

## Why use a state space model

Set against ARIMA and ordinary regression, a state space model offers three specific advantages:

1. **Missing data** is handled naturally — every time point does not need to be observed, and the
   latent state can still be estimated for the gaps (as in dropping rows of $A_t$ above).
2. **Process noise and measurement noise are separated.** ARIMA-type models carry a single
   innovation term; a state space model distinguishes noise intrinsic to the true underlying
   signal ($w_t$) from noise introduced by an imperfect sensor ($v_t$) — a distinction real
   instruments (and real biology) actually have.
3. **Parameters can vary over time**, unlike the fixed $\beta$ of a regression model — as in the
   drifting-coefficient example that opened the chapter.

## Sources

- Slides/lecture notes: `01-state-space-models.md` — motivation from regression and AR(1) to the
  general state space framework, the two organizing principles, and the AR-to-VAR extension.
- Slides/lecture notes: `02-linear-gaussian-model.md` — the linear Gaussian model (DLM): state and
  observation equations, and the blood pressure illustration of $\Upsilon$ versus $\Gamma$.
- Slides/lecture notes: `03-bone-marrow-transplant-example.md` — the bone marrow transplant
  worked example, parameter counts and fitting, filtering/prediction/smoothing, other applications,
  and the advantages of state space models. The prediction/smoothing definitions ($s<t$ versus
  $s>t$) were reconstructed from a markdown rendering artifact in this file that dropped the
  inequality signs; the reconstruction follows the standard usage in the assigned reading.
- Referred to but not supplied: Shumway and Stoffer, *Time Series Analysis and Its Applications*,
  Ch. 5.5 and 6–6.1 (the assigned reading for this lecture), and the state-space diagram image
  linked from `01-state-space-models.md`, which is represented here by an original schematic
  rather than reproduced. No transcript, additional notes, or exercises were supplied for this
  lecture.

---

[← 18. Time-Lagged Regression and the STRF](18-time-lagged-regression-and-the-strf.md) · [Contents](index.md) · [20. The Kalman Filter and Smoother →](20-the-kalman-filter-and-smoother.md)
