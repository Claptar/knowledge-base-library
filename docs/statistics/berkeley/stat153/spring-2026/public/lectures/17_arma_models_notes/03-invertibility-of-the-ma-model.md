---
title: Invertibility of the MA model
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/17_arma_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/17_arma_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Invertibility of the MA model

**Source:** [`public/lectures/17_arma_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/17_arma_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Another important characteristic of the MA model is its invertibility. Invertibility means $\theta(B)$ can be inverted as a power series, giving $w_t = \theta(B)^-1 x_t$.

Let's first look at an important property - for an MA(1) model, $p_x(h)$ is the same for $\theta$ and $1/\theta$. For example, you could try calculating this for $\theta=5$ and $\theta=1/5$. Similarly, if we have $\sigma_w^2=1$ and $\theta=5$, this will yield the same autocovariance as $\sigma_w^2=25$ and $\theta=1/5$. This means that we cannot distinguish between the two MA(1) processes:

$$x_t=w_t +\frac{1}{5} w_{t-1},\quad w_t \overset{iid}{\sim} N(0,25)$$

and

$$y_t=v_t +5 v_{t-1},\quad w_t \overset{iid}{\sim} N(0,1)$$

- they are stochastically equal because of normality. Because we only observe the time series $x_t$ or $y_t$, we do not observe the noise independently and cannot distinguish between these models, so we have to choose one. We want to choose the version where $|\theta| <1$, because this is the version we can invert into an infinite AR representation:

$$w_t = \sum_{j=0}^\infty (-\theta)^j x_{t-k}$$

This is the MA equivalent of requiring AR models to be causal/stationary by having their roots outside the unit circle. So in this particular case, we'd choose $\theta=1/5$ and $\sigma_w^2=25$.

---

[← Back to the MA model](02-back-to-the-ma-model.md) · [Up: contents](index.md) · [ARMA models →](04-arma-models.md)
