---
title: Back to the MA model
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/17_arma_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/17_arma_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Back to the MA model

**Source:** [`public/lectures/17_arma_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/17_arma_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Let's consider an example MA(1) process:

$$x_t = w_t + \theta w_{t-1}$$

The MA model, unlike the AR model, is stationary for any values of $\theta_1, \dots, \theta_q$. We have $E(x_t)=0$, and the autocovariance is:

$$
\begin{aligned}
\gamma_x(h) = \begin{cases}
(1+\theta^2)\sigma^2_w & h=0,\\
\theta\sigma^2_w & h=1,\\
0 & h>1,
\end{cases}
\end{aligned}
$$

and the ACF is:

$$
\begin{aligned}
\rho_x(h) = \begin{cases}
\frac{\theta}{(1+\theta^2)} & h=1,\\
0 & h > 1.
\end{cases}
\end{aligned}
$$

Note that $x_t$ is correlated with $x_{t-1}$, but not $x_{t-2}, x_{t-3}, \dots$. On the other hand, in an AR(1) model, the correlation between $x_t$ and $x_{t-k}$ is never 0. An example below is shown for an MA(1) model for $\theta=0.9$ and $\theta=-0.9$. The time series is smoother for $\theta=0.9$ than $\theta=-0.9$, but we don't have the same correlation structure as an AR model.

![Example MA(1) models](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/17_MA_models.png)

---

[← Autoregressive Moving Average Models](01-autoregressive-moving-average-models.md) · [Up: contents](index.md) · [Invertibility of the MA model →](03-invertibility-of-the-ma-model.md)
