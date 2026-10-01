---
title: "121. From Regression to RNNs"
course: "Berkeley Stat 153"
chapter: 121
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 121. From Regression to RNNs

## What this covers

This is the last lecture of the course, and it asks a single question: what is the smallest change
that turns the linear regression and autoregression models built up over the term into a recurrent
neural network? It assumes the reader already has ordinary linear regression $y_t = \beta_0 +
\beta_1 t + \epsilon_t$, basis expansions with knots, and the $\mathrm{AR}(p)$ autoregressive model
$y_t = \beta_0 + \beta_1 y_{t-1} + \dots + \beta_p y_{t-p} + \epsilon_t$. Everything here is obtained
from those by one modification at a time, which is also the reason to read it in order rather than
jumping to the RNN equation.

## From linear to nonlinear regression on time

The simplest model in the course was linear regression on time itself:

$$y_t = \beta_0 + \beta_1 t + \epsilon_t, \qquad \epsilon_t \overset{\text{i.i.d.}}{\sim} N(0, \sigma^2). \tag{1}$$

One way to make the right-hand side nonlinear in $t$ is to add terms built from the positive-part
function at a set of knots $c_1, \dots, c_k$:

$$y_t = \beta_0 + \beta_1 t + \beta_2 (t - c_1)_+ + \dots + \beta_{k+1}(t - c_k)_+ + \epsilon_t. \tag{2}$$

Write $\sigma(u) = \mathrm{ReLU}(u) = u_+ := \max(u, 0)$ for this positive-part function. (This reuses
the letter $\sigma$ for two different things — the activation function and the noise standard
deviation of $\epsilon_t$ — a clash the lecture keeps throughout because context always disambiguates
it; the same overload is worth watching for below.) Model (2) is still *linear*, just not in $t$
directly: it is linear in the modified variables $1, t, (t-c_1)_+, \dots, (t-c_k)_+$, collectively
called the **feature vector**.

It is worth rewriting (2) as an explicit pipeline, because that pipeline is exactly the shape every
later model reuses. Let $x_t = t$ be the covariate (dropping the raw $t$ term itself, since it is
recovered by taking one knot at $c = 0$), let

$$s_t = (x_t - c_1, \dots, x_t - c_k)^T, \qquad r_t = \sigma(s_t)$$

(with $\sigma$ applied coordinatewise), and let $\mu_t$ be the mean of $y_t$. Then (2) becomes

$$\begin{aligned}
x_t &= t \\
s_t &= (x_t - c_1, \dots, x_t - c_k)^T \\
r_t &= \sigma(s_t) \\
\mu_t &= \beta_0 + \beta^T r_t \\
y_t &= \mu_t + \epsilon_t.
\end{aligned} \tag{3}$$

In words: the scalar covariate $x_t$ is mapped **linearly** to a $k \times 1$ vector $s_t$, then
**nonlinearly** (coordinatewise) to a feature vector $r_t$, and then $\mu_t$ is again a **linear**
function of $r_t$. Every model in the rest of the chapter is this same linear – nonlinear – linear
sandwich, with only the first linear step changing.

## From AR(1) to a single-hidden-layer network

The other family in the course was autoregression, where the covariate is a lagged value of $y_t$
itself rather than $t$. The simplest case, $\mathrm{AR}(1)$, is exactly (1) with $t$ replaced by
$x_t = y_{t-1}$:

$$y_t = \beta_0 + \beta_1 x_t + \epsilon_t, \qquad \epsilon_t \overset{\text{i.i.d.}}{\sim} N(0, \sigma^2).$$

Running the same nonlinear recipe (3) with $x_t = y_{t-1}$ gives a nonlinear version, $\mathrm{NAR}(1)$
(one nonlinear autoregression of order 1 among many possible ones):

$$\begin{aligned}
x_t &= y_{t-1} \\
s_t &= (x_t - c_1, \dots, x_t - c_k)^T \\
r_t &= \sigma(s_t) \\
\mu_t &= \beta_0 + \beta^T r_t \\
y_t &= \mu_t + \epsilon_t.
\end{aligned} \tag{4}$$

Now go to order $p$. The usual linear $\mathrm{AR}(p)$ model is

$$\begin{aligned}
x_t &= (y_{t-1}, \dots, y_{t-p})^T \\
\mu_t &= \beta_0 + \beta^T x_t \\
y_t &= \mu_t + \epsilon_t,
\end{aligned} \tag{5}$$

which is just the familiar $y_t = \beta_0 + \beta_1 y_{t-1} + \dots + \beta_p y_{t-p} + \epsilon_t$
written in vector form. What is the right nonlinear extension of (5)? The covariate $x_t$ is now a
vector, $(y_{t-1}, \dots, y_{t-p})^T$, so the line that builds $s_t$ in (4) has to change. The most
direct fix is to repeat the $k$-knot construction separately for each of the $p$ lagged coordinates
$x_{t1} = y_{t-1}, \dots, x_{tp} = y_{t-p}$:

$$\begin{aligned}
x_t &= (y_{t-1}, \dots, y_{t-p})^T \\
s_t &= \big(x_{t1} - c_1^{(1)}, \dots, x_{t1} - c_k^{(1)},\ \dots,\ x_{tp} - c_1^{(p)}, \dots, x_{tp} - c_k^{(p)}\big)^T \\
r_t &= \sigma(s_t) \\
\mu_t &= \beta_0 + \beta^T r_t \\
y_t &= \mu_t + \epsilon_t.
\end{aligned} \tag{6}$$

With this choice, $\mu_t$ collapses to a sum of separate functions of each lag:

$$\mu_t = \beta_0 + \sum_{j=1}^p g_j(x_{tj}), \qquad g_j(x) := \sum_{i=1}^k \beta_{i,j}\,\sigma\!\big(x - c_j^{(i)}\big),$$

i.e. an **additive model** in $x_{t1}, \dots, x_{tp}$. Additive models cannot represent interactions
between the covariates. If the data were actually generated by $y_t = 0.5\,y_{t-1} y_{t-2} +
\epsilon_t$, an additive model would not fit well, because $(x_1, x_2) \mapsto 0.5\, x_1 x_2$ is not
a sum of a function of $x_1$ and a function of $x_2$.

So instead of building $s_t$ knot-by-knot per coordinate, take the second line of (6) to be an
**arbitrary linear function** of the whole vector $x_t$:

$$\begin{aligned}
x_t &= (y_{t-1}, \dots, y_{t-p})^T \\
s_t &= W x_t + b \\
r_t &= \sigma(s_t) \\
\mu_t &= \beta_0 + \beta^T r_t \\
y_t &= \mu_t + \epsilon_t,
\end{aligned} \tag{7}$$

where $W$ is $k \times p$ and $b$ is $k \times 1$. Because $W$ mixes all $p$ coordinates of $x_t$
together before the nonlinearity is applied, $\mu_t$ is no longer additive in the lags — interactions
like $y_{t-1} y_{t-2}$ are back within reach. This is taken as the definition of $\mathrm{NAR}(p)$,
the nonlinear generalisation of $\mathrm{AR}(p)$.

Model (7) is also exactly a **single-hidden-layer neural network**: a linear map takes the input
$x_t$ to $s_t$, the nonlinearity $\sigma$ turns $s_t$ into the hidden layer $r_t$, and a second
linear map turns $r_t$ into the output $\mu_t$ (with $\epsilon_t$ added to account for the gap
between $y_t$ and its mean $\mu_t$). One nonlinear transformation sandwiched between two linear
ones is precisely the single-hidden-layer architecture. Note again that (7) is a linear model — but
linear in $r_t$, the feature vector, not in the original $x_t$; $r_t$ is also called the hidden
layer output at time $t$.

## Recurrent neural networks

Model (7) has a specific limitation: the hidden state $r_t$ is built from the current input $x_t$
alone. Whatever happened at $t-1$ enters (7) only through $x_t$ itself (i.e. through $y_{t-1},
\dots, y_{t-p}$), not directly. The recurrent neural network removes exactly this limitation, by one
more modification of the same line that has changed at every step so far — the formula for $s_t$.
Let $s_t$ be a linear function of $x_t$ **and** of the previous feature vector $r_{t-1}$:

$$\begin{aligned}
x_t &= (y_{t-1}, \dots, y_{t-p})^T \\
s_t &= W_r r_{t-1} + W x_t + b \\
r_t &= \sigma(s_t) \\
\mu_t &= \beta_0 + \beta^T r_t \\
y_t &= \mu_t + \epsilon_t,
\end{aligned} \tag{8}$$

where $W_r$ is a $k \times k$ square matrix and $r_0 = 0$ by convention (typically $k$ is chosen
larger than $p$). The extra term $W_r r_{t-1}$ is the **recurrent connection**: it feeds the previous
hidden state back into the current one, giving the network a form of memory across time that (7)
does not have. Unrolling the recursion from $r_0 = 0$ shows this memory explicitly:

$$\begin{aligned}
r_1 &= \sigma(Wx_1 + b) \\
r_2 &= \sigma\big(W_r\,\sigma(Wx_1+b) + Wx_2 + b\big) \\
r_3 &= \sigma\big(W_r\,\sigma(W_r\,\sigma(Wx_1+b)+Wx_2+b) + Wx_3+b\big) \\
&\ \ \vdots
\end{aligned} \tag{9}$$

so $r_t$ depends on **every** past input $x_1, \dots, x_t$, not just the current one — though, as
the nested formula makes visible, the strength of that dependence on an old input $x_s$ need not be
uniform in $s$.

<figure>
<svg viewBox="0 0 460 220" role="img" aria-label="Unrolling the RNN recurrence over three time steps">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
    <marker id="arrowRec" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#3b82f6"/>
    </marker>
  </defs>

  <circle cx="50" cy="90" r="20" fill="none" stroke="currentColor" stroke-dasharray="3,3"/>
  <text x="50" y="94" text-anchor="middle" font-size="11" fill="currentColor">r&#8320;=0</text>

  <circle cx="185" cy="90" r="20" fill="none" stroke="currentColor"/>
  <text x="185" y="94" text-anchor="middle" font-size="12" fill="currentColor">r&#8321;</text>

  <circle cx="320" cy="90" r="20" fill="none" stroke="currentColor"/>
  <text x="320" y="94" text-anchor="middle" font-size="12" fill="currentColor">r&#8322;</text>

  <circle cx="420" cy="90" r="20" fill="none" stroke="currentColor"/>
  <text x="420" y="94" text-anchor="middle" font-size="12" fill="currentColor">r&#8323;</text>

  <line x1="70" y1="90" x2="163" y2="90" stroke="#3b82f6" stroke-width="1.8" marker-end="url(#arrowRec)"/>
  <text x="117" y="80" text-anchor="middle" font-size="11" fill="#3b82f6">W&#8348;</text>

  <line x1="205" y1="90" x2="298" y2="90" stroke="#3b82f6" stroke-width="1.8" marker-end="url(#arrowRec)"/>
  <text x="251" y="80" text-anchor="middle" font-size="11" fill="#3b82f6">W&#8348;</text>

  <line x1="340" y1="90" x2="398" y2="90" stroke="#3b82f6" stroke-width="1.8" marker-end="url(#arrowRec)"/>
  <text x="369" y="80" text-anchor="middle" font-size="11" fill="#3b82f6">W&#8348;</text>

  <text x="180" y="185" text-anchor="middle" font-size="12" fill="currentColor">x&#8321;</text>
  <line x1="185" y1="178" x2="185" y2="112" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>

  <text x="315" y="185" text-anchor="middle" font-size="12" fill="currentColor">x&#8322;</text>
  <line x1="320" y1="178" x2="320" y2="112" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>

  <text x="415" y="185" text-anchor="middle" font-size="12" fill="currentColor">x&#8323;</text>
  <line x1="420" y1="178" x2="420" y2="112" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
</svg>
<figcaption>Unrolling the recurrence (9): each hidden state combines the current input with the
previous hidden state through the shared weight $W_r$ (highlighted), so information from $x_1$
keeps propagating into every later $r_t$, while the plain feedforward model (7) would have no
horizontal arrows at all.</figcaption>
</figure>

### Why RNNs are hard to train stably

The formula for $r_t$ multiplies $W_r$ into itself repeatedly (see the nested expression for $r_3$
above, or $r_t$ in general). Imagine, just to see the effect, that $W_r$ were a scalar rather than a
matrix. It cannot land exactly at magnitude $1$, because it is produced by a training algorithm and
landing exactly on $1$ has probability zero; so it is either strictly greater than $1$ or strictly
less than $1$ in magnitude. If $|W_r| > 1$, repeated multiplication blows the product up, so $r_t$
explodes for moderate or large $t$. If $|W_r| < 1$, repeated multiplication shrinks the product
toward zero, so $r_t$ ends up depending essentially only on the inputs $x_s$ with $s$ close to $t$
— which means an RNN built this way **cannot capture long-range dependence**. When $W_r$ is an
actual $k \times k$ matrix, the same dichotomy holds with the **spectral radius** of $W_r$ (the
largest eigenvalue magnitude) playing the role that $|W_r|$ played in the scalar case.

The nonlinearity $\sigma$ is also applied repeatedly along the same nested formula, which is the
second source of instability. The standard fix is to take $\sigma$ to be the hyperbolic tangent
rather than ReLU:

$$\sigma(u) := \frac{e^u - e^{-u}}{e^u + e^{-u}}.$$

Unlike ReLU, which is unbounded above, $\tanh$ always takes values in $(-1, 1)$, which keeps the
repeated composition in (9) from growing without bound and makes the RNN more stable to train.

## Fitting the models: least squares via PyTorch

All of these models — from the nonlinear regression (3) through $\mathrm{NAR}(p)$ (7) to the RNN
(8) — are fit the same way, given data $y_1, \dots, y_n$: choose the parameters ($W$, $W_r$, $b$,
$\beta_0$, $\beta$, and the knots or their equivalents) to minimise the residual sum of squares

$$\sum_{t=1}^n (y_t - \mu_t)^2, \tag{10}$$

where $\mu_t$ is the model's mean, a function of the parameters. Because $\mu_t$ is no longer a
simple linear function of the parameters once a $\sigma$ is involved, (10) is minimised iteratively
— by gradient descent, say — starting from some initial parameter values, rather than solved in
closed form the way ordinary least squares is. Computing the gradients efficiently for models with
this much composition is what a package like PyTorch is for.

## Further reading pointed to but not covered here

The lecture named two references for material beyond this chapter, without covering their content:
the recurrent connection defined in (8) is what the Wikipedia article on recurrent neural networks
calls the *Elman network*, and a suggested paper for more on RNNs is arXiv:1808.03314. Neither is
reproduced here; the course said it would return to RNNs, and to related architectures such as GRU
and LSTM, the following week.

## Sources

All three sections come from a single lecture: Berkeley STAT 153, Spring 2025, Lecture 24 (Aditya
Guntuboyina, April 24, 2025), reconstructed from a slide PDF with no text layer:

- "1 Regression with $t$ as covariate" — equations (1)–(3), the linear/nonlinear-in-$t$ regression
  and its feature-vector pipeline.
- "2 AutoRegression" — equations (4)–(7), $\mathrm{NAR}(1)$, the additive-model attempt at
  $\mathrm{NAR}(p)$ and the interaction counterexample $y_t = 0.5 y_{t-1}y_{t-2}+\epsilon_t$, and the
  single-hidden-layer network (7).
- "3 Recurrent Neural Networks (RNNs)" — equation (8), the unrolled recurrence (9), the stability
  discussion (spectral radius, $\tanh$), and §4–5 on least-squares fitting via PyTorch and the
  pointers to the Elman-network Wikipedia article and arXiv:1808.03314.

The source files flag every equation as a model's unverified reconstruction of a PDF the OCR layer
could not read directly (`fidelity: reconstructed`, `route: llm`); this chapter follows their
notation and content but inherits that caveat — the original PDF, not this chapter or its source
markdown, is the citable authority on the exact formulas.

---

[← 120. Nonlinear Autoregression](120-nonlinear-autoregression.md) · [Contents](index.md) · [122. Stationarity and Causality of AR(p) →](122-stationarity-and-causality-of-ar-p.md)
