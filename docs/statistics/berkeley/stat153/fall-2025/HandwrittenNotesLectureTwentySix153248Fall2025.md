---
title: Lecture Twenty-Six
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwentySix153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureTwentySix153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureTwentySix153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwentySix153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture Twenty-Six

Time Series: $y_1, \dots, y_n \qquad \{y_t\}, t=1\dots n$
$\downarrow$
Convert it into regression:
$$
\longrightarrow (x_t, y_t), \quad t=1,\dots,n
$$
$$
x_t = (y_{t-1}, y_{t-2}, \dots, y_{t-p})
$$

## ① Linear AR:
$$
\mu_t = \beta_0 + \beta^T x_t \qquad \text{AR}(p)
$$
Loss: $\sum (y_t - \mu_t)^2$

## ② Nonlinear AR:
Single Hidden Layer Neural Network:
$$
r_t &= \sigma(W x_t + b) \\
\mu_t &= \beta_0 + \beta^T r_t
$$
$r_t$: $k \times 1$
$x_t$: $p \times 1$

$r_t$: Hidden layer output or Hidden state

$$
\sigma\begin{pmatrix} u_1 \\ \vdots \\ u_k \end{pmatrix} = \begin{pmatrix} \sigma(u_1) \\ \sigma(u_2) \\ \vdots \\ \sigma(u_k) \end{pmatrix}
$$

$$
\sigma(u_i) = \max(u_i, 0) = (u_i)_+
$$

e.g. $p=1$
$$
r_t = \begin{pmatrix} (x_t - c_1)_+ \\ \vdots \\ (x_t - c_k)_+ \end{pmatrix}
$$

## ③ Recurrent Neural Networks (RNN)

$$
r_t &= \tanh(W_r r_{t-1} + W x_t + b), \quad t=1,\dots \\
\mu_t &= \beta_0 + \beta^T r_t \\
r_0 &= \begin{pmatrix} 0 \\ \vdots \\ 0 \end{pmatrix}
$$
$$
W &: k \times p \\
W_r &: k \times k \\
b &: k \times 1
$$
$r_t$: Hidden State

More commonly people use $h_t$ instead of $r_t$.

$$
h_t &= \tanh(W_h h_{t-1} + W x_t + b), \quad t=1, 2, \dots \\
h_0 &= 0
$$

```
   x_t^(1) ----> h_t^(1) = \sigma(W x_t + b)
                      \
   x_t^(2) ----> h_t^(2) --------> (  ) ----> \mu_t
        :             :          /
   x_t^(p) ----> h_t^(k) -------/
```
(with recurrent connections from $h_{t-1}$ to $h_t$)

If all eigenvalues of $W_h < 1$ in modulus, then RNN equations are stable but $h_t$ may not have dependence on $x_u$ for $u \ll t$.

$\downarrow$

## ④ GRU (Gated Recurrent Unit)

$$
\tilde{h}_t = \tanh(W_h h_{t-1} + W x_t + b)
$$
$$
h_t = (1 - z_t) \odot \tilde{h}_t + z_t \odot h_{t-1}
$$

$$
h_t = z_t \odot h_{t-1} + (1 - z_t) \odot \tilde{h}_t
$$

$$
z_t = \sigma_{\text{sigmoid}}(W_{hz} h_{t-1} + W_z x_t + b_z)
$$
$$
\mu_t = \beta_0 + \beta^T h_t
$$

$$
\text{Loss} = \min_{\substack{W_h, W, b \\ W_{hz}, W_z, b_z \\ \beta_0, \beta}} \sum (y_t - \mu_t)^2
$$

GRU:
$$
\tilde{h}_t = \tanh(W_h(h_{t-1} \odot g_t) + W x_t + b)
$$
$$
h_t = z_t \odot h_{t-1} + (1 - z_t) \odot \tilde{h}_t
$$

$z_t$: UPDATE GATE
$$
z_t = \sigma_{\text{sigmoid}}(W_{zh} h_{t-1} + W_z x_t + b_z)
$$

$g_t$: RESET GATE
$$
g_t = \sigma_{\text{sigmoid}}(W_{gh} h_{t-1} + W_g x_t + b_g)
$$

## ⑤ LSTM (Long Short Term Memory)

The hidden state $\{h_t\}$ has two purposes:
$\rightarrow$ ① Immediate prediction of $y_t$
② Saving information relevant for future prediction of $y_t$

$$
\mu_t = \beta_0 + \beta^T h_t
$$
$$
(y_t - \mu_t)^2
$$

$h_t$: hidden state (Immediate prediction of "$y_t$"), current context, 'Short Term Memory'
$c_t$: cell state ('Long Term Memory')

$$
\begin{pmatrix} c_t \\ h_t \end{pmatrix}
$$

RNN:
$$
h_{t-1}&, \ x_t \\
&\downarrow \\
&h_t
$$

LSTM:
$$
(c_{t-1}, \ h_{t-1})&, \ x_t \\
&\downarrow \\
(c_t, \ h_t)
$$

Diagram of flow:
$$
h_t \longrightarrow \mu_{t+1} \longrightarrow y_{t+1}
$$
$$
h_t \longrightarrow h_{t+1}
$$

---

$$
c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t
$$
$$
\tilde{c}_t = \tanh(W_{ch} h_{t-1} + W_c x_t + b_c)
$$
$$
f_t = \sigma_{\text{sigmoid}}(W_{fh} h_{t-1} + W_f x_t + b_f)
$$
$$
i_t = \sigma_{\text{sigmoid}}(W_{ih} h_{t-1} + W_i x_t + b_i)
$$
$$
h_t = o_t \odot \tanh(c_t)
$$
$$
o_t = \sigma_{\text{sigmoid}}(W_{oh} h_{t-1} + W_o x_t + b_o)
$$

$\longrightarrow$ LSTM Unit

---

[Up: contents](index.md)
