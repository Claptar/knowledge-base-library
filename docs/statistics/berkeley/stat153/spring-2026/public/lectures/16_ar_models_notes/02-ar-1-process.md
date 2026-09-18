---
title: AR(1) process
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/16_ar_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/16_ar_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/16_ar_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/16_ar_models_notes.md) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.md`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# AR(1) process

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

## Properties of the stationary AR(1) model
When $|\phi| < 1$, we can derive closed-form expressions (see the derivations of these in your book, Ch 3 example 3.1):

| Property       | Formula                                                        |
|----------------|----------------------------------------------------------------|
| Mean           | $\mu_x = 0$ (assuming zero-mean)                               |
| Variance       | $\gamma(0) = \frac{\sigma_w^2}{1 - \phi^2}$                    |
| Autocovariance | $\gamma(h) = \frac{\sigma_w^2\phi^h}{1 - \phi^2}$ for $h\geq 0$|
| ACF            | $\rho(h) = \frac{\gamma(h)}{\gamma(0)} = \phi^{h}$             |

Note that the ACF of an AR(1) process decays exponentially! We can also see here that $|\phi| < 1$ is needed for stationarity, because the denominator in the variance equation goes to zero as $|\phi| \to 1$. Let's look at an example for the ACF in the notebook.

![Example ACF for AR(1) process with phi=0.9](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/16_acf.png)

## The backshift operator

Next, to look into the properties of the AR models, we're going to define the *backshift operator* $B$:

$B x_t = x_{t-1}$

Then we can rewrite the AR(1) model as:

$$\begin{aligned}
x_t - \phi x_{t-1} &= w_t\\
x_t - \phi B x_t &= w_t\\
(1 - \phi B) x_t &= w_t
\end{aligned}
$$

or the AR(p) model:

$$(1 - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p) x_t = w_t$$

---

[← Intro to Autoregressive models](01-intro-to-autoregressive-models.md) · [Up: contents](index.md) · [The autoregressive operator/characteristic polynomial →](03-the-autoregressive-operator-characteristic-polynomial.md)
