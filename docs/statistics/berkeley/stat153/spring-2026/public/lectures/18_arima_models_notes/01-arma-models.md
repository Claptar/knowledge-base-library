---
title: ARMA Models
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/18_arima_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/18_arima_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# ARMA Models

**Source:** [`public/lectures/18_arima_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/18_arima_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Let's recall that we can represent an Autoregressive Moving Average (ARMA) model as:

$$x_t = \sum_{j=1}^p \phi_j x_{t-j} + \sum_{j=0}^q \theta_j w_{t-j}$$

where $w_t$ is a white noise sequence. The coefficients $\phi_1, \dots, \phi_j, \theta_0, \dots, \theta_q$ are fixed (nonrandom), $\phi_p,\theta_q\neq 0$, and we set $\theta_0=1$.

We talked last time about:

* Causality: a causal AR(p) process can be written as an MA($\infty$) process: $x_t=\sum_{j=0}^\infty \psi_j w_{t-j}$ where $\sum_{j=0}^\infty |\psi_j| < \infty$
* Invertibility: An invertible MA(q) process can be written as an AR($\infty$) process: $x_t = -\sum_{j=1}^{\infty} \phi_j x_{t-j} + w_t$
* (Refer to Appendix B2 of SS for proofs, also see Ch3)

Because causality implies stationarity, this renders the ARMA(p,q) process stationary, as long as the roots of $\phi$ and $\theta$ lie outside the unit circle.

---

[Up: contents](index.md) · [Autocorrelation and Partial Autocorrelation →](02-autocorrelation-and-partial-autocorrelation.md)
