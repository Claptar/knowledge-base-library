---
title: Q7. Random walk and a trend stationary process
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_Homework1.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat153_Homework1.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Q7. Random walk and a trend stationary process

**Source:** [`public/homework/Stat153_Homework1.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_Homework1.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

(a) Write a python function to generate six series that are random walk with drift, of length $n =100$ with $\delta=0.1$ and $\sigma_w =1$. Call the data $x_t$ for $t =1,\dots,100$. Fit the regression $x_t = \beta t + w_t$ using least squares. Plot the data, the true mean function (i.e., $\hat{μ}(t) = 0.1 t$) and the fitted line, $\hat{x}(t) = \beta t$, on the same graph.  (3 points)

(b) Write a python function to generate six series of length $n =100$ that are linear trend plus noise, for example $y_t =0.1 t + w_t$, where $t$ and $w_t$ are as in part (a). Fit the regression $y_t = \beta t +w_t$ using least squares. Plot the data, the true mean function (i.e., $\hat{μ}(t) = 0.1 t$) and the fitted line, $\hat{y}(t) = \beta t$, on the same graph.  (3 points)

(c) Comment on what differences you notice between these. (2 points)

---

[← Q6. Theoretical and sample ACF](08-q6-theoretical-and-sample-acf.md) · [Up: contents](index.md) · [Q8. Linear trends and stationarity →](10-q8-linear-trends-and-stationarity.md)
