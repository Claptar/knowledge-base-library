---
title: Stationarity
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/04_dependence_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Stationarity

**Source:** [`public/lectures/04_dependence_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Recall that for a moving average, the autocovariance $\gamma_v(s,t)$ depends only on the time separation between $s$ and $t$ (also called the *lag*). This is important because this implies the concept of *stationarity*.

A *strictly stationary* time series is one where every collection of values has identical probabilistic behavior to the time-shifted set:

$\{x_t, x_{t_2}, \dots, x_{t_k}\} \overset{d}{=} \{x_{t_1+h}, x_{t_2+h}, \dots, x_{t_k+h}\}$

(that is, same mean, variance, higher-order moments for all $t$). Examples: iid process

This is not true for most applications and is too strict of a definition. So instead, we will introduce the concept of weak stationarity. In your book this is just called "stationary" as short hand.

## Weakly stationary

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

---

[← Cross-correlation](04-cross-correlation.md) · [Up: contents](index.md) · [Estimating covariance of a single time series →](06-estimating-covariance-of-a-single-time-series.md)
