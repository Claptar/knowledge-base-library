---
title: "20. The Kalman Filter and Smoother"
course: "Berkeley Stat 153"
chapter: 20
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 20. The Kalman Filter and Smoother

## What this covers

This chapter finishes the introduction to state space models begun the previous lecture and answers
the question the whole framework exists to solve: given noisy, partial observations $y_t$ of a
hidden process $x_t$, how do you estimate $x_t$, and does the answer change depending on which
observations you're allowed to use? It assumes the state space setup from the prior lecture — a
hidden-state equation and an observation equation, contrasted with ARIMA and ordinary regression —
and builds the Kalman filter and Kalman smoother on top of it, closing with a worked physics example
that tracks a moving object in two dimensions.

## Why a state space model

Recall the running examples motivating the framework: estimating global temperature $x_t$ from land
and sea measurements $y_t$; inferring intended cursor velocity $x_t$ from 100 electrodes of motor
cortex signal $y_t$ in a brain-computer interface; recovering true blood glucose $x_t$ from
intermittent, drift-prone continuous glucose monitor readings $y_t$; and estimating the volatility
$x_t$ of the S&P 500 from daily log returns $y_t$.

Against ARIMA models and fixed-coefficient regression, state space models offer three things:

1. **They handle missing data gracefully.** Not every time point needs to be observed, and you can
   still recover an estimate of the latent state at the missing points.
2. **They separate process noise from measurement noise.** An ARIMA model has a single innovation
   term. A real sensor has its own error on top of whatever noise already sits in the true signal,
   and the state space model keeps the two apart.
3. **They allow time-varying parameters**, where a regression model is stuck with a fixed $\beta$.

## Three questions about the same hidden state

For a state space model, the object of interest is the conditional mean of the hidden state given
data up to some time $s$:

$$x_t^s = E(x_t \mid y_{1:s}), \qquad y_{1:s} = \{y_1, \dots, y_s\}$$

together with its uncertainty, the prediction error covariance (notation follows Shumway and Stoffer,
and the original Kalman 1960 paper):

$$P_{t_1,t_2}^s = E\{(x_{t_1}-x_{t_1}^s)(x_{t_2}-x_{t_2}^s)'\}$$

Which relationship between $s$ and $t$ you're in determines which of three problems you're solving:

- **Filtering** ($s = t$): estimate $x_t$ using only the data seen up through time $t$ itself.
- **Prediction / forecasting** ($s < t$): estimate a *future* state $x_t$ using data only up through
  an earlier time $s$.
- **Smoothing** ($s > t$): estimate $x_t$ using the *whole* dataset, including observations that
  come after $t$ — this is what lets a state space model give a better estimate of a missing or
  noisy value than filtering alone could.

The Kalman filter, named after Kalman's 1960 paper, gives the filtering and forecasting equations.
Its retrospective counterpart, the Kalman smoother, handles the third case.

**An aside on where this is used.** Modifications of the Kalman filter flew on Apollo 8 and every
subsequent Apollo lunar mission, and current variants are part of the navigation system for
Artemis, NASA's return-to-the-Moon program. A NASA technical report on the Orion spacecraft
describes four navigation Extended Kalman Filters (EKFs) — one each for atmospheric flight, Earth
orbit, cislunar flight, and attitude — that propagate the vehicle's position, velocity and
orientation forward using an inertial measurement unit, then correct that estimate against GPS,
optical navigation, and star-tracker measurements. The filter developed below is for a *linear*
system; the EKF is the extension of the same idea to nonlinear dynamics.

## The Kalman filter

The model is a linear-Gaussian state space model with a hidden state equation and an observation
equation:

$$x_t = \Phi x_{t-1} + \Upsilon u_t + w_t \qquad \text{(state equation)}$$
$$y_t = A_t x_t + \Gamma u_t + v_t \qquad \text{(observation equation)}$$

with initial conditions $x_0^0 = \mu_0$, $P_0^0 = \sigma_0$. For $t = 1, \dots, n$, the filter
alternates two steps.

**Predict.** Propagate the previous filtered estimate forward through the dynamics, before seeing
$y_t$:

$$x_t^{t-1} = \Phi x_{t-1}^{t-1} + \Upsilon u_t, \qquad P_t^{t-1} = \Phi P_{t-1}^{t-1}\Phi' + Q$$

$x_t^{t-1}$ is the best guess for the state at $t$ given only what was known at $t-1$. Uncertainty
grows here: it gets pushed through the dynamics $\Phi$ and picks up a fresh dose of process noise
$Q$.

**Update.** Correct the prediction once $y_t$ arrives:

$$x_t^t = x_t^{t-1} + K_t\big(y_t - A_t x_t^{t-1} - \Gamma u_t\big), \qquad P_t^t = [I - K_t A_t]P_t^{t-1}$$

The term $y_t - A_t x_t^{t-1} - \Gamma u_t$ is the **innovation**: how much the actual measurement
disagrees with what was predicted. $K_t$ decides what fraction of that disagreement to fold into the
estimate. Correspondingly, uncertainty *shrinks* here: $[I - K_t A_t]$ measures how much the
measurement reduced it, with full reduction when $K_t A_t = I$ and none when $K_t = 0$.

$K_t$ is the **Kalman gain**:

$$K_t = P_t^{t-1}A_t'\big[A_t P_t^{t-1}A_t' + R\big]^{-1}$$

It weighs prediction against measurement: a noisy sensor (large $R$) shrinks the gain and the filter
leans on its own dynamics; an uncertain prediction (large $P_t^{t-1}$) pushes the gain up and the
filter leans on the data instead.

Running the filter, given a model $(\Phi, A, Q, R)$ and initial conditions $(\mu_0,\sigma_0)$, means
moving forward through the data one step at a time, alternately predicting (uncertainty grows) and
updating (uncertainty shrinks).

## The Kalman smoother

The smoother — implemented in the accompanying notebook as the Rauch–Tung–Striebel (RTS) algorithm,
published in 1965 — refines the state estimates *post hoc*, using the entire dataset including
future observations. It runs the Kalman filter forward first, then makes a second, backward pass
that revises every earlier estimate using the filter's stored outputs.

<figure>
<svg viewBox="0 0 340 190" role="img" aria-label="The filter sweeps forward through time while the smoother makes a second pass backward, revising every earlier estimate">
  <defs>
    <marker id="arrowfwd" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="40" y1="45" x2="300" y2="45" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowfwd)"/>
  <text x="170" y="30" text-anchor="middle" font-size="12" fill="currentColor">filter: forward pass, $x_t^t$</text>

  <line x1="300" y1="150" x2="40" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowfwd)"/>
  <text x="170" y="172" text-anchor="middle" font-size="12" fill="currentColor">smoother: backward pass, $x_t^n$</text>

  <g fill="currentColor">
    <circle cx="40" cy="97" r="4"/>
    <circle cx="110" cy="97" r="4"/>
    <circle cx="180" cy="97" r="4"/>
    <circle cx="250" cy="97" r="4"/>
    <circle cx="300" cy="97" r="4"/>
  </g>
  <text x="40" y="118" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="110" y="118" text-anchor="middle" font-size="12" fill="currentColor">2</text>
  <text x="180" y="118" text-anchor="middle" font-size="12" fill="currentColor">&#8230;</text>
  <text x="250" y="118" text-anchor="middle" font-size="12" fill="currentColor">n-1</text>
  <text x="300" y="118" text-anchor="middle" font-size="12" fill="currentColor">n</text>

  <line x1="40" y1="60" x2="40" y2="90" stroke="currentColor" stroke-width="0.75" stroke-dasharray="2,2"/>
  <line x1="300" y1="60" x2="300" y2="90" stroke="currentColor" stroke-width="0.75" stroke-dasharray="2,2"/>
  <line x1="40" y1="104" x2="40" y2="140" stroke="currentColor" stroke-width="0.75" stroke-dasharray="2,2"/>
  <line x1="300" y1="104" x2="300" y2="140" stroke="currentColor" stroke-width="0.75" stroke-dasharray="2,2"/>
</svg>
<figcaption>The filter can only look backward at each time step, so it sweeps forward once. The
smoother then sweeps backward, letting information from later observations correct earlier state
estimates.</figcaption>
</figure>

## Filter vs. smoother: which one to use

Use the **filter** for real-time estimates, where future data doesn't exist yet to condition on.
It's also computationally cheap: the update at time $t$ only needs the estimate from $t-1$, not the
whole history.

Use the **smoother** for post hoc analysis, where the goal is the best possible estimate at every
time point and all the data is already in hand. The lecture's example is clinical: given platelet,
white blood cell, and hematocrit measurements after a bone marrow transplant, looking back to draw
conclusions about a patient's course is exactly the setting where the smoother's use of future
observations earns its keep.

## Worked example: tracking a 2D trajectory

The Kalman filter is applied to tracking the position and velocity of an object moving through the
plane. Unlike the blood-glucose example, where the dynamics matrix $\Phi$ would have to be estimated
from data, here it's known outright from physics: position updates as $p_t = p_{t-1} + \Delta t\,
v_{t-1}$.

The state is $x_t = [p_x, p_y, v_x, v_y]^\top$, with

$$x_t = \Phi x_{t-1} + w_t, \quad w_t \sim \mathcal{N}(0, Q), \qquad y_t = A x_t + v_t, \quad v_t \sim \mathcal{N}(0, R)$$

$$\Phi = \begin{bmatrix} 1 & 0 & \Delta t & 0 \\ 0 & 1 & 0 & \Delta t \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}, \qquad A = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{bmatrix}$$

$\Phi$ says position advances by $\Delta t$ times velocity, while velocity itself is left unchanged
from one step to the next — the 1's on the bottom-right diagonal. $A$ says only position is
observed: the zero columns for $v_x, v_y$ mean velocity never appears directly in $y_t$, and the
filter has to infer it purely from how the observed position moves over time.

The ground truth used in the demo is a *gentle curve*, not a straight line — deliberately, since the
model's assumption of constant velocity is then wrong and the true velocity is actually changing.
This is what lets the example show what happens when the model is misspecified. Measurements are
generated by adding Gaussian noise with covariance $\sigma_R$ to the true position. The accompanying
notebook visualises uncertainty as covariance ellipses: 95% confidence regions built from the
$2\times2$ position block of $P$, so the ellipse shrinks after an update and grows again during
prediction.

## Exercises

From the accompanying interactive notebook (Lecture 22), which lets you vary the process noise
$\sigma_Q$, the measurement noise $\sigma_R$, and whether the smoother is shown, on the gently
curving trajectory described above.

1. With the default noise levels ($\sigma_Q = 0.05$, $\sigma_R = 0.80$), predict what the filter's
   estimated trajectory will look like before running it, and say why.
2. Set $\sigma_R$ much larger (around 2.5), so the measurements are nearly useless. Does the filter
   still manage to track the object? What does the estimate look like, and why?
3. Set $\sigma_Q$ much smaller (around 0.005), so the filter is told to trust its dynamics model
   almost completely. What goes wrong here, and why — think about what the dynamics model assumes
   about the trajectory versus what the ground truth actually does.
4. Turn on the smoother and compare it to the filter along the trajectory. Where does the smoother's
   correction help most — the beginning, the middle, or the end — and why would that be?

## Sources

- `22_state_space_models_2_notes/01-continuation-of-state-space-models.md` — the recap of motivating
  examples and the three advantages of state space models over ARIMA and regression. Cites Shumway
  and Stoffer, Ch. 6.2, as the reading.
- `22_state_space_models_2_notes/02-filtering-smoothing-and-forecasting.md` — the $x_t^s$ notation,
  the prediction error covariance $P^s_{t_1,t_2}$, and the Apollo/Artemis aside, including the quoted
  passage from the NASA Orion EKF technical report
  (<https://ntrs.nasa.gov/api/citations/20230000548/downloads/Orion_EKF_AAS_2023.pdf>), which is
  referred to but not otherwise contained in the supplied material. One passage in this file has its
  `<` and `>` symbols swallowed by a markdown-conversion artifact ("where we have $s t$"); the
  filtering/prediction/smoothing cases given above reconstruct it using the standard
  Shumway–Stoffer convention ($s=t$, $s<t$, $s>t$), which is consistent with the surrounding text.
- `22_state_space_models_2_notes/03-the-kalman-filter.md` — the filter recursion, the Kalman gain,
  the RTS smoother (Rauch–Tung–Striebel, 1965), and the filter-vs-smoother discussion, including the
  bone marrow transplant example.
- `Lecture22/01-introduction.md` — the 2D tracking model, its $\Phi$ and $A$ matrices, and the
  contrast with the blood-glucose example where $\Phi$ must be estimated rather than known.
- `Lecture22/03-interactive-version.md` — the interactive demo's suggested experiments, rewritten
  above as exercises, and the description of the covariance ellipses. The `kalman_filter` and
  `rts_smoother` functions this demo calls are defined in a notebook cell not included in the
  supplied material (only the introduction and interactive-demo cells were provided, not the
  intervening implementation cell).

---

[← 19. State Space Models](19-state-space-models.md) · [Contents](index.md) · [21. Convolutional Networks and Discrete Convolution →](21-convolutional-networks-and-discrete-convolution.md)
