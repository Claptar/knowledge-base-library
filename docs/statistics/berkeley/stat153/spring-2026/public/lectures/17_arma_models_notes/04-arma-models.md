---
title: ARMA models
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/17_arma_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/17_arma_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# ARMA models

**Source:** [`public/lectures/17_arma_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/17_arma_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

We can now use these two concepts (the AR and MA models) to extend our models to Autoregressive Moving Average (ARMA) models, which contain elements of both. The autocovariance of an AR model generally decays away from $h=0$, while the autocovariance of an MA process becomes exactly 0 after a certain lag.

*Definition:* A time series is ARMA(p,q) if it is stationary and:

$$x_t=\mu + \phi_1(x_{t-1}-\mu) + \dots + \phi_p (x_{t-p}-\mu) + w_t + \theta_1 w_{t-1} +  \dots + \theta_q w_{t-q}$$

The parameters $p$ and $q$ are called the autoregressive and moving average orders. We also often set $\alpha = \mu (1-\phi_1 - \dots - \phi_p)$ and write:

$$x_t= \alpha + \phi_1 x_{t-1} + \dots + \phi_p x_{t-p} + w_t + \theta_1 w_{t-1} +  \dots + \theta_q w_{t-q}$$

![Video showing the difference between AR, MA, and ARMA models as a schematic](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/17_ARMAScene.mp4)

We can also write the ARMA(p,q) more precisely as

$$\phi(B)(x_t-\mu) = \theta(B)w_t$$

Since ARMA is just an extension of AR and MA models, ARMA(p,0) = AR(p) and ARMA(0,q) = MA(q).

---

[← Invertibility of the MA model](03-invertibility-of-the-ma-model.md) · [Up: contents](index.md) · [When do we use ARMA models? →](05-when-do-we-use-arma-models.md)
