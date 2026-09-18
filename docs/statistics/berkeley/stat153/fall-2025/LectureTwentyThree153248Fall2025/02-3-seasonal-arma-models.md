---
title: 3 Seasonal ARMA Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyThree153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentyThree153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Seasonal ARMA Models

Seasonal ARMA models are often useful while modeling datasets having seasonal features (e.g., monthly datasets). We say that $\{y_t\}$ is a seasonal $\text{ARMA}(P, Q)$ process with period $s$ if it satisfies the difference equation $\Phi(B^s)(y_t - \mu) = \Theta(B^s)\epsilon_t$ where $\epsilon_t \overset{\text{i.i.d.}}{\sim} N(0, \sigma^2)$ and
$$
\Phi(B^s) = 1 - \Phi_1 B^s - \Phi_2 B^{2s} - \dots - \Phi_P B^{Ps}
$$
and
$$
\Theta(B^s) = 1 + \Theta_1 B^s + \Theta_2 B^{2s} + \dots + \Theta_Q B^{Qs}.
$$
The seasonal $\text{ARMA}(P, Q)$ model with period $s$ is a special case of an $\text{ARMA}(Ps, Qs)$ model. However the seasonal model has $P + Q + 1$ (the 1 is for $\sigma^2$) parameters while a general $\text{ARMA}(Ps, Qs)$ model will have $Ps + Qs + 1$ parameters. So the seasonal models are much sparser.

Causal stationary solution exists when every root of $\Phi(z^s)$ (equivalently, $\Phi(z)$) has modulus strictly larger than one.

The ACF and PACF of seasonal ARMA models are **non-zero only** at the seasonal lags $h = 0, s, 2s, 3s, \dots$. At these seasonal lags, the ACF and PACF of these models behave just as the case of the unseasonal ARMA model: $\Phi(B)X_t = \Theta(B)\epsilon_t$.

---

[← 1 The Box-Jenkins Time Series Modeling Strategy](01-1-the-box-jenkins-time-series-modeling-strategy.md) · [Up: contents](index.md) · [4 Multiplicative Seasonal ARMA Models →](03-4-multiplicative-seasonal-arma-models.md)
