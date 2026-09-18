---
title: The Kalman Filter
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/22_state_space_models_2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/22_state_space_models_2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.md`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# The Kalman Filter

For the state space model with:

*(Hidden) State equation*: $$x_t = \Phi x_{t-1} + \Upsilon u_t + w_t$$ and

*Observation equation*: $$y_t = A_t x_t+\Gamma u_t + v_t$$

with initial conditions $x_0^0=\mu_0$ and $P_0^0 = \sigma_0$ for $t=1,\dots,n$:

$$
\begin{aligned}
x_t^{t-1} &= \Phi x_{t-1}^{t-1} + \Upsilon u_t,\\
P_t^{t-1} &= \Phi P_{t-1}^{t-1}\Phi^\prime + Q,
\end{aligned}
$$

* $x_t^{t-1}$ is the predicted state mean, which is your best guess for the state at $t$ based on $t-1$, applying the dynamics ($\Phi$)
* $P_t^{t-1}$ is the predicted state covariance. Uncertainty is growing during prediction as propagated through $\Phi$ and new process noise $Q$

with

$$
\begin{aligned}
x_t^t &= x_t^{t-1} + K_t(y_t-A_t x_t^{t-1}-\Gamma u_t),\\
P_t^t &= [I-K_t A_t]P_t^{t-1},
\end{aligned}
$$

* $x_t^t$ is the filter state mean, where we correct our prediction by a fraction $K_t$ of the innovation, which is how much today's measurement disagrees with what you predicted
* $P_t^t$ shows how uncertainty shrinks after an update, where the factor $[I-K_t A_t]$ quantifies how much the measurement reduced your uncertainty. When $K_t A_t = I$, we have full reduction, and no reduction when $K_t=0$.

where

$$K_t=P_t^{t-1} A_t^\prime [A_tP_t^{t-1}A_t^\prime + R]^{-1}$$

is called the Kalman gain. The Kalman gain weighs how much we should trust the measurement vs. the prediction. Noisy measurements (with big $R$) will shrink this gain, while uncertain predictions with big $P_t^{t-1}$

## Running the Kalman Filter

Given a model $(\Phi, A, Q,R)$ and initial conditions $(\mu_0, \sigma_0)$, the filter moves forward through the data one time step at a time.

At each $t$ we do two things:

1. Prediction: propagate the previous estimate forward using the dynamics $x_{t-1}^{t-1} \rightarrow x_t^{t-1}$  (Uncertainty grows)
2. Update: Correct the prediction using new measurements $y_t$ through the Kalman gain. (Uncertainty shrinks)

## The Kalman Smoother

The Kalman Smoother (in the accompanying notebook this is implemented using the Rauch-Tung-Striebel/RTS algorithm, published in 1965). This can be used *post hoc* to refine state estimates retrospectively, using all data (including future data)!

In practice, this runs using a forward pass (the Kalman filter), followed by a backward pass, which modifies earlier estimates based on the filter's stored outputs.

## When to use the filter vs. smoother

It's helpful to use the Kalman filter for real-time estimates where you can't use future data because it doesn't exist yet. Computationally, the Kalman filter is also very cheap, because you only need data from the previous time step for your estimates.

On the other hand, the Kalman smoother is helpful for post hoc analyses where getting the best possible estimate at each time point is your goal. For example, in the bone marrow transplant data, if we are trying to look at platelet, WBC, and hematocrit data after the fact to make some claims about patient outcomes, we may want to use the smoother to get better estimates.

## Examples

Next, we'll show an example using the Kalman filter and smoother for estimating 2D trajectory data in the accompanying Lecture22 notebook.

---

[← Filtering, smoothing, and forecasting](02-filtering-smoothing-and-forecasting.md) · [Up: contents](index.md)
