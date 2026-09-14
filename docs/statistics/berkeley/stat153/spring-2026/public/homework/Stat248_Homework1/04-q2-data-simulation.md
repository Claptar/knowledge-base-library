---
title: Q2. Data simulation {-}
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework1.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat248_Homework1.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Q2. Data simulation {-}

**Source:** [`public/homework/Stat248_Homework1.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework1.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

(a) Write two separate python functions to simulate two time series of length $T=500$: (1) Gaussian white noise, (2) an autoregressive process defined by $x_t = 0.5 x_{t-1} + w_t$ where $w_t$ is Gaussian white noise with $\sigma_w=1$. (2 points)

(b) Compute and plot the sample autocorrelation function for up to lag 40 for each time series. Be sure to label your x and y axes appropriately. (2 points)

(c) For each time series, estimate $\gamma(1)$ using the formula

$$\hat{\gamma}(1) = \frac{1}{T}\displaystyle\sum_{t=1}^{T-1}(x_t-\bar{x})(x_{t+1}-\bar{x})$$

and report the value for each case (2 points).

(d) Apply the moving average filter $v_t=\frac{1}{4}(x_t+x_{t-1}+x_{t-2}+x_{t-3})$ to the data generated from the autoregressive process you generated previously. How does the moving average affect the signal? (2 points)

---

[← Q1. Autocovariance, autocorrelation, and stationarity {-}](03-q1-autocovariance-autocorrelation-and-stationarity.md) · [Up: contents](index.md) · [Q3. Correlation and independence {-} →](05-q3-correlation-and-independence.md)
