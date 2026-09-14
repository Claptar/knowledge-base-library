---
title: The Kalman Filter
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/22_state_space_models_2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# The Kalman Filter

**Source:** [`public/lectures/22_state_space_models_2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

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

---

[← Filtering, smoothing, and forecasting](04-filtering-smoothing-and-forecasting.md) · [Up: contents](index.md) · [Running the Kalman Filter →](06-running-the-kalman-filter.md)
