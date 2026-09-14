---
title: Intro to Autoregressive models
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/16_ar_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/16_ar_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Intro to Autoregressive models

**Source:** [`public/lectures/16_ar_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/16_ar_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Up until now we've thought about signals in both the frequency and the time domain, and most recently we've been looking at decomposing signals into sinusoids and looking at power spectra. Today, we look at autoregressive models, which allow us to predict a signal from its past.

Autoregression = regression on self.

**Ordinary regression:** $Y=X\beta$

**AR(1) process:** $x_t = \phi x_{t-1} + w_t$

In the AR process, $x_t$ can be written as a function of $p$ past values $x_{t-1}, x_{t-2}, \dots, x_{t-p}$. $p$ determines the number of steps in the past needed to forecast the current value. This is also called the *order* of the AR($p$) process.

**AR(p) process:** $x_t = \phi_1 x_{t-1} +\phi_2 x_{t-2} + \dots + \phi_p x_{t-p} + w_t$

* $x_t$ is stationary
* $w_t \sim \text{white noise}(0,\sigma^2_w)$
* $\phi_1, \phi_2, \dots, \phi_p$ are constants $\neq 0$

We can also add an intercept, $\alpha$ if $\bar{x_t} \neq 0$.

Let's look at some examples of these in the accompanying Lecture 16 notebook. In the plot below, series A is white noise, series B is an AR(1) model with $\phi=0.9$, series C is a random walk (AR with $\phi=1$, which is not stationary, and series D is an AR(1) model with $\phi=-0.8$.

![Example time series](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/16_example_ar.png)

---

[Up: contents](index.md) · [AR(1) process →](02-ar-1-process.md)
