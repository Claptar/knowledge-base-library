---
title: What does this mean?
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture19.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# What does this mean?

**Source:** [`public/lectures/Lecture19.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

So what does this mean about AR, ARMA, and ARIMA models and their use? In each case, it's very important to understand and plot the underlying data and to look for trends *before* fitting models. For time series data that have multiple underlying trends or more complex behavior, *state space* methods (which we will discuss later) may be more helpful. The steps for building any ARIMA models should be:

1. Plot the data
2. Possibly transform the data (log transform, differencing, etc)
3. Identify the dependence orders of the model (inspect ACF, PACF)
4. Parameter estimation
5. Diagnostics
6. Choosing a model

---

[← Forecast](21-forecast.md) · [Up: contents](index.md) · [One more example →](23-one-more-example.md)
