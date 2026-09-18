---
title: Stationarity
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/04_dependence_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/04_dependence_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.md`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Stationarity

Recall that for a moving average, the autocovariance $\gamma_v(s,t)$ depends only on the time separation between $s$ and $t$ (also called the *lag*). This is important because this implies the concept of *stationarity*.

A *strictly stationary* time series is one where every collection of values has identical probabilistic behavior to the time-shifted set:

$\{x_t, x_{t_2}, \dots, x_{t_k}\} \overset{d}{=} \{x_{t_1+h}, x_{t_2+h}, \dots, x_{t_k+h}\}$

(that is, same mean, variance, higher-order moments for all $t$). Examples: iid process

This is not true for most applications and is too strict of a definition. So instead, we will introduce the concept of weak stationarity. In your book this is just called "stationary" as short hand.

### Weakly stationary

A weakly stationary time series $x_t$ is a finite variance process where:

* The mean function is constant and doesn't depend on $t$
* The autocovariance function $\gamma(s,t)$ depends on $s$ and $t$ only through their difference $|s-t|$.

This is convenient because we can then estimate things about time series where we don't have multiple repeated observations (and thus we can't actually estimate the variability for a given time sample directly). In a stationary time series, the mean function is independent of time, so we have:

 $\mu_t = \mu$

 We can also simplify the autocovariance function so that it is only dependent on the time shift / lag. For example, if $s=t+h$, $h$ is the *lag* between $s$ and $t$. We then have:

 $\gamma(t+h, t) = \operatorname{cov}(x_{t+h}, x_t)=\operatorname{cov}(x_h,x_0) = \gamma(h,0) = \gamma(h)$

The autocovariance of a (weakly) stationary time series is thus:

$\gamma(h) = \operatorname{cov}(x_{t+h}, x_t) = \mathbb{E}[(x_{t+h}-\mu)(x_t-\mu)]$

* In your lab, you will look at the stationarity of white noise (strictly stationary), moving average (weakly stationary), random walks (not stationary), and linear trends (not stationary).
* If mean and/or autocovariance change with time, your time series is not stationary

## Estimating covariance of a single time series

Much of the time we don't have multiple samples of our time series, so we can't estimate $\mu_t$ separately for each $t$. If we assume stationarity, $\mu_t = \mu$, so we can use the sample mean instead of $\mu_t$:

$\hat{\gamma}(h) = \frac{1}{n}\displaystyle\sum_{t=1}^{n-h}(x_{t+h}-\bar{x})(x_t-\bar{x})$,

where $\bar{x} = \frac{1}{n}\sum_{t=1}^n x_t$ is the sample mean. Also, $\hat{\gamma}(-h) = \hat{\gamma}(h)$ for $h=0,1,\dots,n-1$.

This is nice because we can always calculate the sample autocovariance. However, whether it is interpretable or meaningful will depend on whether the stationarity assumption is approximately true.

## Estimating relationships between two time series

We can use cross-correlation to estimate relationships between two series $x_t$ and $y_t$. For signals that are jointly weakly stationary:

$\hat{\rho}_{xy}(h) = \frac{\hat{\gamma_{xy}}(h)}{\sqrt{\hat{\gamma_x}(0)\hat{\gamma_y}(0)}}$

Here is an example of the autocorrelation functions for the Southern Oscillation Index, fish recruitment, and their relationship (cross-correlation function):

![SOI and fish recruitment](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/Lec4_SOI.png)

![Sample ACFs and CCFs of Southern Oscillation Index and fish recruitment](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/Lec4_acf_soi.png)

## Next time:

* Linear regression (Chapter 2 SS)

---

[← Today](01-today.md) · [Up: contents](index.md)
