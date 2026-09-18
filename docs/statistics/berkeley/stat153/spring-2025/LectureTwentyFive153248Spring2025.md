---
title: STAT 153 & 248 - Time Series
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFive153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyFive153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentyFive153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFive153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# STAT 153 & 248 - Time Series

### Lecture Twenty Five
Spring 2025, UC Berkeley

Aditya Guntuboyina

April 29, 2025

## 1 Nonlinear AutoRegression

In the last lecture, we started discussing nonlinear forms of autoregression for an observed time series $y_1, \dots, y_n$. For each $t$, we take $x_t = (y_{t-1}, \dots, y_{t-p})^T$ for some integer $p \ge 1$. $x_t$ can be called the covariate at time $t$ corresponding to the response value $y_t$. In the context of recurrent neural network models, $x_t$ is referred to as the input at time $t$.

The usual (linear) autoregression AR($p$) model corresponds to:
$$
\mu_t = \beta_0 + \beta^T x_t. \tag{1}
$$
The loss function is $\sum_t (y_t - \mu_t)^2$, and the parameters $\beta_0, \beta$ are estimated by minimizing the loss.

In nonlinear autoregression, we change the formula (1) into a nonlinear function of $x_t$. When $p = 1$, one simple nonlinear AR(1) model is:
$$
\mu_t = \beta_0 + \beta_1 x_t + \beta_2 (x_t - c_1)_+ + \dots + \beta_{k+1} (x_t - c_k)_+.
$$
We simplify this slightly by dropping $x_t$ (because $x_t = (x_t - c_0)_+ + c_0$ for all $t$ provided $c_0$ is smaller than all the observed values of $x_t$; we will not lose anything by dropping $x_t$). This leads to
$$
\mu_t = \beta_0 + \beta_1 (x_t - c_1)_+ + \dots + \beta_k (x_t - c_k)_+.
$$
We rewrite this equation using the following notation:
\$\$
\begin{aligned}
s_t &= (x_t - c_1, \dots, x_t - c_k)^T \\
r_t &= \sigma(s_t) \\
\mu_t

---

[Up: contents](index.md)
