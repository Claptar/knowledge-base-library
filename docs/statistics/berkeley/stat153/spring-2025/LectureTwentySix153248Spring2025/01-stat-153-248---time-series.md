---
title: STAT 153 & 248 - Time Series
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentySix153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentySix153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentySix153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentySix153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# STAT 153 & 248 - Time Series

## Lecture Twenty Six

Spring 2025, UC Berkeley

Aditya Guntuboyina

May 01, 2025

## 1 RNN

RNN is given by
$$
\begin{aligned}
r_0 &= 0 \\
s_t &= W_r r_{t-1} + W x_t + b \\
r_t &= \sigma_{\text{tanh}}(s_t) \\
\mu_t &= \beta_0 + \beta^T r_t
\end{aligned}
\tag{1}
$$

This formula can also be written as
$$
\begin{aligned}
r_0 &= 0 \\
r_t &= \sigma_{\text{tanh}}(W_r r_{t-1} + W x_t + b) \\
\mu_t &= \beta_0 + \beta^T r_t
\end{aligned}
\tag{2}
$$

Here the activation function $\sigma_{\text{tanh}}$ is the tanh activation function given by
$$
\sigma_{\text{tanh}}(u) := \frac{e^u - e^{-u}}{e^u + e^{-u}}.
$$

The parameters now are $W_r$ ($k \times k$ matrix), $W$ ($k \times p$ matrix), $b$ ($k \times 1$ vector), $\beta_0$ (scalar) and $\beta$ ($k \times 1$ vector).

In the last lecture, we saw that RNNs have a "lack of long memory" problem. This means that even though $r_t$ technically depends on all of $x_t, x_{t-1}, \dots$, in practice, it is mainly controlled by $x_u$ for $u$ close to $t$. This problem is fixed, to some extent, by GRUs and LSTMs.

## 2 GRU (Gated Recurrent Unit)

GRU is
$$
\begin{aligned}
r_0 &= 0 \\
g_t &= \sigma_{\text{sigmoid}}(W_r^g r_{t-1} + W^g x_t + b^g) \\
z_t &= \sigma_{\text{sigmoid}}(W_r^z r_{t-1} + W^z x_t + b^z) \\
\tilde{r}_t &:= \sigma_{\text{tanh}}(W_r (r_{t-1} \odot g_t) + W x_t + b) \\
r_t &= z_t \odot r_{t-1} + (1 - z_t) \odot \tilde{r}_t \\
\mu_t &= \beta_0 + \beta^T r_t.
\end{aligned}
\tag{3}
$$

$z_t$ is called the update gate while $g_t$ is called the reset gate. The unknown parameters in this model (which need to be estimated from the data) are $W_r^g, W^g, b^g, W_r^z, W^z, b^z, W_r, W, b, \beta_0, \beta$.

Because of the presence of $z_t$, it is possible for $r_t$ to be quite close to $r_{t-1}$ for many time points $t$. This allows $r_t$ to have a relatively long memory.

---

[Up: contents](index.md) · [3 LSTM (Long Short Term Memory) →](02-3-lstm-long-short-term-memory.md)
