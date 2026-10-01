---
title: "76. Neural Network Models for Time Series"
course: "Berkeley Stat 153"
chapter: 76
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 76. Neural Network Models for Time Series

## What this covers

This chapter follows a single thread: turn a time series into a regression problem, then watch the
regression function grow more expressive — from a linear autoregression, to a single hidden layer
network, to recurrent architectures (RNN, GRU, LSTM) that carry a summary of the whole past forward
one step at a time. It assumes familiarity with linear AR($p$) models, least-squares fitting, and
the basic shape of a feedforward neural network layer.

## From a time series to a regression problem

Given a series $y_1, \dots, y_n$, the same trick used elsewhere in this course turns it into a list
of input-output pairs: pick a lag $p$ and set

$$
x_t = (y_{t-1}, y_{t-2}, \dots, y_{t-p}), \qquad t = 1, \dots, n,
$$

so that predicting $y_t$ from its own recent past becomes predicting $y_t$ from $x_t$ — an ordinary
regression problem on the pairs $(x_t, y_t)$. What differs across the models below is only the
function used to turn $x_t$ (and, later, a running hidden state) into a prediction $\mu_t$ of
$y_t$; the fitting criterion throughout is the same sum of squared errors, $\sum_t (y_t-\mu_t)^2$.

## Linear AR($p$): the regression function is linear

The simplest choice is a linear function of the lags,

$$
\mu_t = \beta_0 + \beta^T x_t,
$$

which is exactly the AR($p$) model, fit by minimizing $\sum_t (y_t - \mu_t)^2$ — ordinary least
squares on the lagged design matrix.

## Nonlinear AR: a single hidden layer

Replace the linear map with a single hidden layer network. The lags $x_t$ ($p\times 1$) are first
mapped to a hidden vector $r_t$ ($k \times 1$),

$$
r_t = \sigma(Wx_t + b), \qquad \mu_t = \beta_0 + \beta^T r_t,
$$

where $\sigma$ is applied coordinatewise,

$$
\sigma\begin{pmatrix}u_1\\ \vdots \\ u_k\end{pmatrix} = \begin{pmatrix}\sigma(u_1)\\ \vdots \\ \sigma(u_k)\end{pmatrix},
$$

and the lecture's choice of nonlinearity is the ReLU, $\sigma(u) = \max(u,0) = (u)_+$. The
prediction $\mu_t$ is then an affine combination of $k$ "features" of the lagged values rather than
of the lagged values directly — $r_t$ is called the hidden layer output, or hidden state.

A concrete case makes this readable: with a single lag ($p=1$) and hidden units placed at knots
$c_1, \dots, c_k$,

$$
r_t = \begin{pmatrix}(x_t - c_1)_+ \\ \vdots \\ (x_t-c_k)_+ \end{pmatrix},
$$

so each hidden unit is a hinge that stays at zero until $x_t$ passes its knot $c_j$, then rises
linearly. $\mu_t$ is a weighted sum of these hinges plus an intercept — a piecewise linear function
of $x_t$ with breakpoints at the $c_j$. A single hidden layer ReLU network is, in this sense, doing
the same thing as fitting a broken-line (spline-like) regression, with the knots and slopes learned
rather than chosen in advance.

This model is still an AR($p$) in the sense that $\mu_t$ depends on the past only through the fixed
window $x_t = (y_{t-1}, \dots, y_{t-p})$: to look further back, $p$ has to grow, and so does the
input dimension. The recurrent models below remove that restriction.

## Recurrent networks: a hidden state carried forward

Instead of feeding a fixed window of lags into a stateless function, a recurrent network keeps a
hidden state $r_t$ that is updated at every time step from the *previous* hidden state and the
current input:

$$
r_t = \tanh(W_r r_{t-1} + Wx_t + b), \qquad r_0 = 0, \qquad \mu_t = \beta_0 + \beta^T r_t,
$$

with $W_r$ a $k\times k$ matrix, $W$ a $k \times p$ matrix, and $b$ a $k \times 1$ vector. Because
$r_t$ feeds into $r_{t+1}$, it can in principle carry information from arbitrarily far back — not
just the last $p$ lags — which is the whole point of moving to a recurrent architecture. The
lecture's own notation switches at this point from $r_t$ to $h_t$ (the more common symbol for the
hidden state elsewhere), giving the same recursion:

$$
h_t = \tanh(W_h h_{t-1} + Wx_t + b), \qquad h_0 = 0.
$$

<figure>
<svg viewBox="0 0 460 260" role="img" aria-label="One step of a recurrent cell, showing the hidden state carried forward and, for an LSTM, a second cell-state channel carried alongside it">
  <defs>
    <marker id="arrow26" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>

  <rect x="170" y="70" width="100" height="70" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="220" y="110" text-anchor="middle" font-size="12" fill="currentColor">cell at t</text>

  <line x1="20" y1="95" x2="168" y2="95" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow26)"/>
  <text x="20" y="86" font-size="12" fill="currentColor">h(t-1)</text>
  <line x1="272" y1="95" x2="430" y2="95" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow26)"/>
  <text x="330" y="86" font-size="12" fill="currentColor">h(t) forward</text>

  <circle cx="300" cy="95" r="2.5" fill="currentColor"/>
  <line x1="300" y1="95" x2="300" y2="32" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow26)"/>
  <text x="308" y="28" font-size="12" fill="currentColor">mu(t) -&#62; y(t)</text>

  <line x1="20" y1="128" x2="168" y2="128" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arrow26)"/>
  <text x="20" y="145" font-size="11" fill="currentColor">c(t-1), LSTM only</text>
  <line x1="272" y1="128" x2="430" y2="128" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arrow26)"/>
  <text x="300" y="145" font-size="11" fill="currentColor">c(t) forward, LSTM only</text>

  <line x1="220" y1="228" x2="220" y2="142" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow26)"/>
  <text x="220" y="243" text-anchor="middle" font-size="12" fill="currentColor">x(t)</text>
</svg>
<figcaption>One step of a recurrent cell. The hidden state h(t) carries information to the next
step and branches off to predict y(t); a plain RNN has only this channel. LSTM adds the dashed
channel below it, a separate cell state c(t), so that carrying information forward and predicting
right now are no longer the same variable's job.</figcaption>
</figure>

## The trouble with plain RNNs

The recursion above is only as good as its long-range memory. If every eigenvalue of $W_h$ has
modulus less than $1$, the recursion is stable — $h_t$ does not blow up — but the same contraction
that keeps it stable also keeps *shrinking* the influence of an input $x_u$ from far in the past:
$h_t$ may end up with essentially no dependence on $x_u$ for $u \ll t$. Stability and memory pull in
opposite directions for a plain RNN, and everything from here on is a different way of resolving
that tension.

## GRU: gating what the state remembers

The gated recurrent unit lets the network choose, at each step and coordinate, how much of a new
candidate state to accept versus how much of the old state to keep. Compute a candidate update
exactly as in the plain RNN,

$$
\tilde h_t = \tanh(W_h h_{t-1} + Wx_t + b),
$$

and blend it with the previous state using an update gate $z_t \in [0,1]^k$,

$$
h_t = z_t \odot h_{t-1} + (1-z_t)\odot \tilde h_t, \qquad
z_t = \sigma_{\text{sigmoid}}(W_{hz}h_{t-1} + W_z x_t + b_z),
$$

with $\mu_t = \beta_0 + \beta^T h_t$, and all of $W_h, W, b, W_{hz}, W_z, b_z, \beta_0, \beta$ fit
jointly by minimizing $\sum_t (y_t - \mu_t)^2$. Where $z_t$ is close to $1$ the state barely changes
($h_t \approx h_{t-1}$); where it is close to $0$ the state is overwritten by the new candidate —
the update gate is what lets information survive many steps without the plain RNN's uniform
contraction.

The full GRU adds a second gate, the reset gate $g_t$, which controls how much of the previous
state is even consulted when *forming* the candidate in the first place:

$$
\tilde h_t = \tanh\big(W_h(h_{t-1}\odot g_t) + Wx_t + b\big), \qquad
h_t = z_t \odot h_{t-1} + (1-z_t) \odot \tilde h_t,
$$

$$
z_t = \sigma_{\text{sigmoid}}(W_{zh}h_{t-1} + W_z x_t + b_z) \quad\text{(update gate)}, \qquad
g_t = \sigma_{\text{sigmoid}}(W_{gh}h_{t-1} + W_g x_t + b_g) \quad\text{(reset gate)}.
$$

$z_t$ decides how much of the old state to keep; $g_t$ decides how much of the old state is even
looked at when computing what the new candidate would be.

## LSTM: splitting short-term and long-term memory

The lecture motivates the LSTM by pointing out that the hidden state $h_t$ has been asked to do two
jobs at once: predict $y_t$ right now, and carry forward whatever will be needed to predict future
values. The LSTM gives these two jobs separate variables — a hidden state $h_t$ ("short-term
memory", used for the immediate prediction) and a cell state $c_t$ ("long-term memory") — so the
full state carried from one step to the next is the pair $(c_t, h_t)$, compared to just $h_t$ for a
plain RNN:

$$
\text{RNN: } (h_{t-1}, x_t) \to h_t \qquad\qquad
\text{LSTM: } \big((c_{t-1}, h_{t-1}), x_t\big) \to (c_t, h_t).
$$

The cell state is updated by a forget gate $f_t$ (how much of the old cell state to keep) and an
input gate $i_t$ (how much of a new candidate cell value to add):

$$
c_t = f_t \odot c_{t-1} + i_t \odot \tilde c_t, \qquad
\tilde c_t = \tanh(W_{ch}h_{t-1} + W_c x_t + b_c),
$$

$$
f_t = \sigma_{\text{sigmoid}}(W_{fh}h_{t-1} + W_f x_t + b_f), \qquad
i_t = \sigma_{\text{sigmoid}}(W_{ih}h_{t-1} + W_i x_t + b_i).
$$

The hidden state is then read off the cell state through an output gate $o_t$:

$$
h_t = o_t \odot \tanh(c_t), \qquad
o_t = \sigma_{\text{sigmoid}}(W_{oh}h_{t-1} + W_o x_t + b_o),
$$

with the prediction and loss exactly as before, $\mu_t = \beta_0 + \beta^T h_t$ and
$\sum_t(y_t - \mu_t)^2$. The point of separating $c_t$ from $h_t$ is precisely the tension flagged
for plain RNNs: when the forget gate $f_t$ is close to $1$, the cell update is close to the
identity plus an addition, $c_t \approx c_{t-1} + i_t \odot \tilde c_t$, so information can pass
through many steps without being repeatedly squashed by a $\tanh$ or contracted by a fixed matrix —
it can survive far longer than in the plain RNN recursion.

## Sources

- Berkeley STAT 153 (fall 2025), handwritten lecture notes for Lecture 26 — the only material
  supplied for this chapter; no slide deck, transcript or problem set was given. The notes file is
  itself a model reconstruction of a handwritten PDF with no text layer, and its own banner marks
  every equation as unverified; this chapter reorganizes and explains that reconstruction without
  adding any model, example or claim beyond what appears in it.
- All five models discussed — linear AR, the single hidden layer nonlinear AR, the plain RNN, the
  GRU and the LSTM — and every displayed equation come from that one file.

---

[← 75. $MA(q)$ models](75-ma-q-models.md) · [Contents](index.md) · [77. Multiplicative Seasonal ARIMA Models →](77-multiplicative-seasonal-arima-models.md)
