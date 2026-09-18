---
title: Invertibility of the MA model
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/17_arma_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/17_arma_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/17_arma_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/17_arma_models_notes.md) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.md`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Invertibility of the MA model

Another important characteristic of the MA model is its invertibility. Invertibility means $\theta(B)$ can be inverted as a power series, giving $w_t = \theta(B)^-1 x_t$.

Let's first look at an important property - for an MA(1) model, $p_x(h)$ is the same for $\theta$ and $1/\theta$. For example, you could try calculating this for $\theta=5$ and $\theta=1/5$. Similarly, if we have $\sigma_w^2=1$ and $\theta=5$, this will yield the same autocovariance as $\sigma_w^2=25$ and $\theta=1/5$. This means that we cannot distinguish between the two MA(1) processes:

$$x_t=w_t +\frac{1}{5} w_{t-1},\quad w_t \overset{iid}{\sim} N(0,25)$$

and

$$y_t=v_t +5 v_{t-1},\quad w_t \overset{iid}{\sim} N(0,1)$$

- they are stochastically equal because of normality. Because we only observe the time series $x_t$ or $y_t$, we do not observe the noise independently and cannot distinguish between these models, so we have to choose one. We want to choose the version where $|\theta| <1$, because this is the version we can invert into an infinite AR representation:

$$w_t = \sum_{j=0}^\infty (-\theta)^j x_{t-k}$$

This is the MA equivalent of requiring AR models to be causal/stationary by having their roots outside the unit circle. So in this particular case, we'd choose $\theta=1/5$ and $\sigma_w^2=25$.

## ARMA models

We can now use these two concepts (the AR and MA models) to extend our models to Autoregressive Moving Average (ARMA) models, which contain elements of both. The autocovariance of an AR model generally decays away from $h=0$, while the autocovariance of an MA process becomes exactly 0 after a certain lag.

*Definition:* A time series is ARMA(p,q) if it is stationary and:

$$x_t=\mu + \phi_1(x_{t-1}-\mu) + \dots + \phi_p (x_{t-p}-\mu) + w_t + \theta_1 w_{t-1} +  \dots + \theta_q w_{t-q}$$

The parameters $p$ and $q$ are called the autoregressive and moving average orders. We also often set $\alpha = \mu (1-\phi_1 - \dots - \phi_p)$ and write:

$$x_t= \alpha + \phi_1 x_{t-1} + \dots + \phi_p x_{t-p} + w_t + \theta_1 w_{t-1} +  \dots + \theta_q w_{t-q}$$

![Video showing the difference between AR, MA, and ARMA models as a schematic](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/17_ARMAScene.mp4)

We can also write the ARMA(p,q) more precisely as

$$\phi(B)(x_t-\mu) = \theta(B)w_t$$

Since ARMA is just an extension of AR and MA models, ARMA(p,0) = AR(p) and ARMA(0,q) = MA(q).

## When do we use ARMA models?

* To forecast stationary time series data by combining previous values (AR) and previous error terms (MA)
* Ex: sales, temperature, financial time series

## When not to use ARMA models?

* When data are nonstationary / have trends
* When the data have strong seasonal patterns
* If the data have complex, nonlinear relationships

---

[← Autoregressive Moving Average Models](01-autoregressive-moving-average-models.md) · [Up: contents](index.md)
