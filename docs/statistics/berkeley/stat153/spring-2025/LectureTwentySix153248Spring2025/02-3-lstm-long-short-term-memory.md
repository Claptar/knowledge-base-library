---
title: 3 LSTM (Long Short Term Memory)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentySix153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentySix153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentySix153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentySix153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 LSTM (Long Short Term Memory)

LSTM is another modification to the basic RNN for enabling long memory. It also uses gates and has one more gate compared to the GRU. Instead of a recursion directly between $r_{t-1}$ and $r_t$, the LSTM recursions are between the pairs $(s_{t-1}, r_{t-1}) \to (s_t, r_t)$:
$$
\begin{aligned}
r_0 &= 0 \text{ and } s_0 = 0 \\
f_t &= \sigma_{\text{sigmoid}}(W_r^f r_{t-1} + W^f x_t + b^f) \\
i_t &= \sigma_{\text{sigmoid}}(W_r^i r_{t-1} + W^i x_t + b^i) \\
o_t &= \sigma_{\text{sigmoid}}(W_r^o r_{t-1} + W^o x_t + b^o) \\
\tilde{r}_t &:= \sigma_{\text{tanh}}(W_r r_{t-1} + W x_t + b) \\
s_t &= f_t \odot s_{t-1} + i_t \odot \tilde{r}_t \\
r_t &= o_t \odot \sigma_{\text{tanh}}(s_t) \\
\mu_t &= \beta_0 + \beta^T r_t
\end{aligned}
\tag{4}
$$

$f_t$ is called the forget gate, $i_t$ is called the input gate and $o_t$ is called the output gate. The presence of these gates allow $r_t$ to draw information from $x_u$ even for $u$ quite far from $t$.

The unknown parameters in this model are $W_r^f, W^f, b^f, W_r^i, W^i, b^i, W_r^o, W^o, b^o, W_r, W, b, \beta_0, \beta$.

The LSTM unit is all the equations in (4) excluding the last linear layer $\mu_t = \beta_0 + \beta^T r_t$:
\$\$
\begin{aligned}
r_0 &=

---

[← STAT 153 & 248 - Time Series](01-stat-153-248---time-series.md) · [Up: contents](index.md)
