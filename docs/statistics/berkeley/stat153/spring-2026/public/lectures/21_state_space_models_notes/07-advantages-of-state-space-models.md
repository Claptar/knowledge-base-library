---
title: Advantages of state space models
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/21_state_space_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/21_state_space_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Advantages of state space models

**Source:** [`public/lectures/21_state_space_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/21_state_space_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

What are the advantages of state space models as opposed to other models we've discussed in this class?

1. They deal well with missing data and don't require every time point to be observed. You can still get estimates of the latent state for those missing time points.
2. We can separate process noise from measurement noise. In ARIMA models, we have just one noise term (innovations/shocks). For real scientific applications, we may have noisy sensors where the measurement reading's error is distinct from underlying noise in the true signal.
3. We can have time-varying parameters (unlike fixed $\beta$ in a regression model).

---

[← Other examples](06-other-examples.md) · [Up: contents](index.md)
