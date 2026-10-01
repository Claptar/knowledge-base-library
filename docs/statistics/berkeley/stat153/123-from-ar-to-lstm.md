---
title: "123. From AR to LSTM"
course: "Berkeley Stat 153"
chapter: 123
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 123. From AR to LSTM

## What this covers

How do you get from a linear autoregressive model of a time series to a model that can carry
information across many time steps? This chapter follows one lecture's route from AR($p$) through
a single hidden-layer network, the plain recurrent neural network (RNN), the gated recurrent unit
(GRU), and finally the LSTM — at each step naming the specific failure of the previous model that
the next one is built to fix. It assumes the reader already has AR($p$) models, least-squares
fitting, and the idea of a feedforward neural network with an activation function.

## Setting up the regression

Start from an observed series $\{y_t\}$ and the goal of predicting its future values. Convert this
into a standard regression problem by building, for each $t$, an input vector from the recent past:
$$x_t = (y_{t-1}, \dots, y_{t-p}), \qquad p \ge 1.$$
After re-indexing, both $x_t$ and $y_t$ are defined for $t = 1, \dots, n$. Every model in this
chapter is a rule for turning $x_t$ — together with the *earlier* inputs $x_{t-1}, x_{t-2}, \dots,
x_1$ — into a prediction $\mu_t$ for $y_t$. All of them are fit by minimizing the same squared-error
loss,
$$\sum_{t=1}^n (y_t - \mu_t)^2,$$
in practice by some variant of gradient descent rather than by solving a linear system, since the
later models are nonlinear in their parameters. What differs between the models is *how* $\mu_t$
is allowed to depend on the history $x_1, \dots, x_t$.

## From linear to nonlinear autoregression

The plain **AR($p$)** model is linear in the lagged inputs:
$$\mu_t = \beta_0 + \beta^T x_t.$$

The natural nonlinear extension passes $x_t$ through one hidden layer of a feedforward network
before the linear output step:
$$h_t = \sigma(W x_t + b), \qquad \mu_t = \beta_0 + \beta^T h_t,$$
where $x_t$ is $p \times 1$, $h_t$ is $k \times 1$, $W$ is $k \times p$, and $b$ is $k \times 1$.
This is an ordinary single-hidden-layer neural network, but it is worth naming $h_t$ the **hidden
state**, because every subsequent model keeps this same shape — a hidden state that a linear
readout turns into $\mu_t$ — and only changes how $h_t$ is computed. In this model $h_t$ depends
only on the *current* input $x_t$; it has no memory of $x_{t-1}, x_{t-2}, \dots$ at all. That is
exactly the limitation the recurrent models below remove.

## The recurrent neural network

The **RNN** lets the hidden state depend on its own previous value as well as on the current input:
$$h_0 = 0, \qquad h_t = \tanh(W_h h_{t-1} + W x_t + b), \qquad \mu_t = \beta_0 + \beta^T h_t,$$
with $\tanh(u) = \dfrac{e^u - e^{-u}}{e^u + e^{-u}}$. Feeding $h_{t-1}$ back in is what lets $h_t$,
in principle, carry information from every past input $x_t, x_{t-1}, \dots, x_1$, not just the
current one.

In principle, but not in practice. As the lecture recalled from an earlier session, an RNN's
behaviour is governed by the eigenvalues of $W_h$: if at least one eigenvalue exceeds 1 in modulus
the hidden state explodes, and if all eigenvalues are strictly smaller than 1 in modulus the
influence of any given $x_u$ on $h_t$ decays geometrically as $t - u$ grows — the network has no
real long memory. (The argument for this dichotomy was given in the lecture immediately before
this one, which is not among the material available here.) Both GRUs and LSTMs are attempts to fix
this without discarding recurrence altogether.

## The gated recurrent unit

The **GRU** introduces two gates that modulate how much the hidden state is allowed to change at
each step:
$$
\begin{aligned}
h_0 &= 0\\
g_t &= \sigma_{\text{sigmoid}}(W_h^g h_{t-1} + W^g x_t + b^g) & \text{(reset gate)}\\
z_t &= \sigma_{\text{sigmoid}}(W_h^z h_{t-1} + W^z x_t + b^z) & \text{(update gate)}\\
\tilde h_t &= \tanh\big(W_h(h_{t-1} \odot g_t) + W x_t + b\big) & \text{(candidate hidden state)}\\
h_t &= z_t \odot h_{t-1} + (1 - z_t) \odot \tilde h_t\\
\mu_t &= \beta_0 + \beta^T h_t,
\end{aligned}
$$
where $\sigma_{\text{sigmoid}}(u) = e^u/(1+e^u)$ and $\odot$ is elementwise multiplication. If every
component of $z_t$ were 0 and every component of $g_t$ were 1, this reduces exactly to the plain
RNN — so the GRU is a strict generalization of it.

The mechanism that fixes the memory problem is the update gate. If a component of $z_t$ is close
to 1, the corresponding component of $h_t$ is close to $h_{t-1}$: the hidden state is passed
through almost unchanged. Because $z_t$ is itself a learned function of the current input and
state, the network can choose, input by input, whether to overwrite a piece of memory or to
protect it — which is precisely what a fixed linear map $W_h$ with eigenvalues below 1 could never
do, since it damps every direction by the same fixed factor regardless of content. (The last line,
$\mu_t = \beta_0 + \beta^T h_t$, is not usually counted as part of the GRU itself: the unit's output
is the sequence of hidden states $h_1, \dots, h_T$, and a separate linear layer turns those into
predictions compared against $y_t$ in the loss.)

## The LSTM: splitting short-term and long-term memory

In both the RNN and the GRU, the single vector $h_t$ is asked to do two jobs at once: hold whatever
is needed to predict the *current* output $y_t$, and hold whatever will be needed to predict
*future* outputs $y_{t+1}, y_{t+2}, \dots$. The **LSTM** assigns these two jobs to two separate
vectors. $h_t$ keeps the name hidden state and plays the first role — short-term memory, the
current context. A new vector $c_t$, the **cell state**, plays the second role — long-term memory,
information kept around for predictions that may be far in the future. The name Long Short-Term
Memory refers to exactly this pairing.

$$
\begin{aligned}
h_0 &= 0, \quad c_0 = 0\\
\tilde c_t &= \tanh(W_{hc} h_{t-1} + W_{ic} x_t + b_c) & \text{(candidate cell state)}\\
f_t &= \sigma_{\text{sigmoid}}(W_{hf} h_{t-1} + W_{if} x_t + b_f) & \text{(forget gate)}\\
i_t &= \sigma_{\text{sigmoid}}(W_{hi} h_{t-1} + W_{ii} x_t + b_i) & \text{(input gate)}\\
o_t &= \sigma_{\text{sigmoid}}(W_{ho} h_{t-1} + W_{io} x_t + b_o) & \text{(output gate)}\\
c_t &= f_t \odot c_{t-1} + i_t \odot \tilde c_t\\
h_t &= o_t \odot \tanh(c_t)\\
\mu_t &= \beta_0 + \beta^T h_t
\end{aligned}
$$

Reading the equations gate by gate:

- **Candidate cell state $\tilde c_t$** is the proposed new content for long-term memory — the
  same conceptual role that $\tilde h_t$ played in the GRU.
- **Forget gate $f_t$** decides how much of the previous long-term memory $c_{t-1}$ survives. A
  component near 1 keeps most of $c_{t-1}$; a component near 0 discards it. This selective
  preservation — rather than the uniform decay a fixed $W_h$ imposes — is what lets an LSTM hold
  information over hundreds of time steps.
- **Input gate $i_t$** decides how much of the candidate $\tilde c_t$ is actually written into
  long-term memory. Together, $f_t$ and $i_t$ jointly control how $c_t$ evolves from $c_{t-1}$.
- **Output gate $o_t$** decides how much of the cell state is exposed through the hidden state,
  via $h_t = o_t \odot \tanh(c_t)$. Even when $c_t$ carries a great deal of information, the model
  can reveal only the part relevant to the current prediction.

Two structural points are worth noting. First, all three gates and the candidate cell state are
functions of $h_{t-1}$ and $x_t$ only — none of them look directly at $c_{t-1}$. Second, exactly as
with the GRU, the final linear readout $\mu_t = \beta_0 + \beta^T h_t$ is not counted as part of
the LSTM unit itself; the unit's output is the sequence of pairs $(h_1, c_1), \dots, (h_T, c_T)$,
and note that $\mu_t$ depends on $h_t$ alone, never on $c_t$ directly.

## Forecasting with a fitted LSTM

Once an LSTM has been fit — the lecture used $p = 1$, so $x_t = y_{t-1}$, trained on
$(x_1, y_1), \dots, (x_T, y_T)$ — forecasting beyond the observed data proceeds recursively:

1. Run the LSTM equations over the observed inputs $x_1, \dots, x_T$ to obtain the final hidden and
   cell states $(h_T, c_T)$.
2. Use the last observed value as the first input for prediction: set $x_{T+1} = y_T$.
3. Feed each prediction back in as the next input, recursively, to generate $x_{T+2}, x_{T+3},
   \dots$ and their corresponding predictions.

Concretely, for the first forecast step one computes $(i_{T+1}, f_{T+1}, o_{T+1}, \tilde c_{T+1})$
from $(h_T, c_T)$ and $x_{T+1} = y_T$ using the LSTM equations above, then would combine them into
$c_{T+1}$, $h_{T+1}$, and finally the forecast $\mu_{T+1}$ — the same update used at every training
step, just with the network's own output standing in for an observation that has not happened yet.
The lecture material available here breaks off at the point of computing the gates for this first
step, before writing out the resulting $c_{T+1}$, $h_{T+1}$, and $\mu_{T+1}$ explicitly.

## Sources

- Guntuboyina, STAT 153 & 248 (UC Berkeley), Lecture 26, Fall 2025 (Dec 04, 2025) —
  `docs/statistics/berkeley/stat153/fall-2025/LectureTwentySix153248Fall2025.md` in the library
  repository. Primary source for this chapter: the AR($p)$-to-LSTM progression, the RNN
  memory-decay/explosion remark, the GRU, the full LSTM with per-gate intuition, and the start of
  the forecasting recursion. This note is itself a model's reconstruction of a PDF with no text
  layer, converted 2026-09-18; every equation in it is marked unverified by the conversion, and the
  note breaks off mid-explanation of the forecasting procedure.
- Guntuboyina, STAT 153 & 248 (UC Berkeley), Lecture 26, Spring 2025 (May 01, 2025) — same course,
  a different offering of the same lecture, used only to cross-check the RNN and GRU equations
  (given there with the hidden/candidate state written as $r_t$, $\tilde r_t$ instead of $h_t$,
  $\tilde h_t$): `docs/statistics/berkeley/stat153/spring-2025/LectureTwentySix153248Spring2025/01-stat-153-248---time-series.md`
  and `.../02-3-lstm-long-short-term-memory.md`. The Fall 2025 treatment was used as the primary
  text throughout because it additionally motivates the hidden-state idea from AR($p$) and a
  single hidden layer network, gives the intuition for each LSTM gate, and carries further into
  the forecasting recursion; the Spring 2025 LSTM note is also truncated, mid-equation, before
  reaching the forecasting discussion at all.
- The lecture explicitly refers to "the last lecture" for the derivation of why RNNs either explode
  or lose long memory depending on the eigenvalues of $W_h$; that derivation is not contained in
  either note supplied here.
- No slides, transcript, or exercises were supplied for this chapter; both inputs are lecture-notes
  reconstructions of a PDF.

---

[← 122. Stationarity and Causality of AR(p)](122-stationarity-and-causality-of-ar-p.md) · [Contents](index.md) · [124. Box-Jenkins Strategy and SARIMA Models →](124-box-jenkins-strategy-and-sarima-models.md)
