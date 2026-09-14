---
title: Running the Kalman Filter
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/22_state_space_models_2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Running the Kalman Filter

**Source:** [`public/lectures/22_state_space_models_2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Given a model $(\Phi, A, Q,R)$ and initial conditions $(\mu_0, \sigma_0)$, the filter moves forward through the data one time step at a time.

At each $t$ we do two things:

1. Prediction: propagate the previous estimate forward using the dynamics $x_{t-1}^{t-1} \rightarrow x_t^{t-1}$  (Uncertainty grows)
2. Update: Correct the prediction using new measurements $y_t$ through the Kalman gain. (Uncertainty shrinks)

---

[← The Kalman Filter](05-the-kalman-filter.md) · [Up: contents](index.md) · [The Kalman Smoother →](07-the-kalman-smoother.md)
