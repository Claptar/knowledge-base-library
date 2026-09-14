---
title: Autoregressive Moving Average Models
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/17_arma_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/17_arma_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Autoregressive Moving Average Models

**Source:** [`public/lectures/17_arma_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/17_arma_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Before the break, we started talking about AR models:

**AR(p) process:** $x_t = \phi_1 x_{t-1} +\phi_2 x_{t-2} + \dots + \phi_p x_{t-p} + w_t$

We showed that AR models are stationary iff the roots of their characteristic polynomial equation lie outside the unit circle.

If this is satisfied, we can rewrite our AR(p) model as:

$$x_t = \mu + \sum_{j=0}^{\infty} \psi_j \epsilon_{t-j}$$

for some $\mu$ and coefficients $\psi_1, \psi_2, \dots$ satisfying $\sum_j |\psi_j| < \infty$. This is sometimes also referred to as a *causal* process (though not in the same way that the word causal is used in a lot of statistics -- here it just means that the model can be expressed purely as a function of current and past information).

As an alternative, we will now introduce the idea of the moving average model of order $q$ (MA($q$)), which is defined as:

**MA($q$):** $x_t = w_t + \theta_1 w_{t-1} +\theta_2 w_{t-2} + \dots + \theta_q w_{t-q}$ where $w_t \sim \text{white noise}(0, \sigma_w^2)$ and $\theta_1, \theta_2, \dots, \theta_q (\theta_q \neq 0)$ are parameters. We can also write this equivalently as:

$$x_t = \theta(B)w_t$$

using the backshift operator, which we also defined last time as $B x_t = x_{t-1}$

## An aside - why does the backshift operator make sense?

The backshift operator allows us to express a shift in time as a linear operator, which allows us to form expressions like the characteristic polynomial to tell us whether a signal is stationary.

### Linear operators

A function $f$ is a linear operator if it satisfies two properties for all inputs $x$, $y$, and scalars $a$:

1. Additivity: f(x+y) = f(x) + f(y)
2. Scalar homogeneity: f(ax) = a f(x)

Sometimes these are combined into one: $f(ax+by) = af(x) + bf(y)$.

The backshift operator $B$ is a linear operator because shifting a scaled or summed series is the same as scaling or summing the shifted series. This is what allows us to use tricks like the characteristic polynomial as a diagnostic tool for calculating the stationarity of an AR model and (as we will discuss later) the invertibility of the MA part of the model.

---

[Up: contents](index.md) · [Back to the MA model →](02-back-to-the-ma-model.md)
