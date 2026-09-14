---
title: AR(1) process
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/16_ar_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/16_ar_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# AR(1) process

**Source:** [`public/lectures/16_ar_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/16_ar_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

The simplest AR model is the AR(1) model, where $x_t$ depends on $\phi x_{t-1}$ plus some white noise (or "shock"). This could be used to look at temperature (if it's 72 degrees F right now, what's your best guess for one hour from now?), stock returns (if the market went up 2% today, what does that tell you about tomorrow?), etc.

**What does $\phi$ control?**

| $\phi$           | Behavior                                  |
|------------------|-------------------------------------------|
| $\phi = 0$       | White noise (no memory)                   |
| $0 < \phi < 1$   | Positive memory - values drift slowly     |
| $\phi \to 1$     | Very long memory                          |
| $\phi = 1$       | Random walk (nonstationary)               |
| $-1 < \phi < 0$  | Oscillatory memory - alternating values   |

So what happens if $|\phi| > 1$? In this case, the influence of past shocks doesn't decay and the variance of $x_t$ increases without bound. The AR(1) process is stationary iff $|\phi| < 1$. Below are some example AR1 time series from the accompanying lecture notebook:

![Example AR1 time series](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/16_AR1_phi.png)

![Example AR1 time series for negative values of $\phi$](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/16_AR1_phi_neg.png)

Some observations:

* As $\phi$ increases, the series becomes smoother - why?
* The variance of the series also increases with $\phi$ - why?
* At $\phi = 0.99$, this looks close to a random walk

---

[← Intro to Autoregressive models](01-intro-to-autoregressive-models.md) · [Up: contents](index.md) · [Properties of the stationary AR(1) model →](03-properties-of-the-stationary-ar-1-model.md)
