---
title: Estimating covariance of a single time series
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/04_dependence_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Estimating covariance of a single time series

**Source:** [`public/lectures/04_dependence_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/04_dependence_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Much of the time we don't have multiple samples of our time series, so we can't estimate $\mu_t$ separately for each $t$. If we assume stationarity, $\mu_t = \mu$, so we can use the sample mean instead of $\mu_t$:

$\hat{\gamma}(h) = \frac{1}{n}\displaystyle\sum_{t=1}^{n-h}(x_{t+h}-\bar{x})(x_t-\bar{x})$,

where $\bar{x} = \frac{1}{n}\sum_{t=1}^n x_t$ is the sample mean. Also, $\hat{\gamma}(-h) = \hat{\gamma}(h)$ for $h=0,1,\dots,n-1$.

This is nice because we can always calculate the sample autocovariance. However, whether it is interpretable or meaningful will depend on whether the stationarity assumption is approximately true.

---

[← Stationarity](05-stationarity.md) · [Up: contents](index.md) · [Estimating relationships between two time series →](07-estimating-relationships-between-two-time-series.md)
