---
title: 1 The Box-Jenkins Time Series Modeling Strategy
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyThree153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentyThree153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyThree153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 The Box-Jenkins Time Series Modeling Strategy

## Lecture Twenty Three

Fall 2025, UC Berkeley

Aditya Guntuboyina

November 20, 2025

Box and Jenkins popularized the following strategy for modeling an observed time series $y_1, \dots, y_n$:

1. Generally $y_1, \dots, y_n$ will exhibit various kinds of trends. Preprocess the data to transform it to another series $x_t$ which does not have any discernible trends.
2. Fit an $\text{ARMA}(p, q)$ model for appropriate $p$ and $q$ to the transformed data $x_t$.

The preprocessing in the first step above is usually done in one of the following two ways:

1. **Differencing.** The first difference of $\{y_t\}$ is given by $\nabla y_t := y_t - y_{t-1}$ for $t = 2, \dots, n$. The second difference is given by
$$
\begin{aligned}
\nabla^2 y_t &= \nabla (\nabla y_t) \\
&= \nabla (y_t - y_{t-1}) = \nabla y_t - \nabla y_{t-1} = (y_t - y_{t-1}) - (y_{t-1} - y_{t-2}) = y_t - 2y_{t-1} + y_{t-2}.
\end{aligned}
$$
Higher order differences $\nabla^k y_t$ are defined recursively. Note that the length of the time series comes down after each successive differencing. For example, $\nabla y_t$ has length $n-1$, $\nabla^2 y_t$ has length $n - 2$ and so on. Differencing usually eliminates increasing/decreasing trends. Usually one or two orders of differencing is enough to take care of increasing/decreasing trends.

2. **Seasonal Differencing.** Seasonal differencing is used to eliminate seasonal trends. Suppose we have a dataset having seasonal trends with period $s$ (for example, for monthly datasets, $s = 12$). The seasonal first difference of $y_t$ with period $s$ is defined as
$$
\nabla_s y_t := y_t - y_{t-s}
$$
Note that $\nabla_s y_t$ is a time series of length $n - s$. The second order seasonal difference is
$$
\nabla_s^2 y_t = \nabla_s (\nabla_s y_t) = y_t - 2y_{t-s} + y_{t-2s}
$$
and higher order seasonal differences are defined recursively. Seasonal differences eliminate seasonal trends. Usually, in datasets having seasonal and increasing/decreasing trends, one first takes a seasonal difference. This often eliminates seasonality and might also eliminate the linear trend. If a linear trend still persists, one takes a regular difference of the seasonal differenced series. This will often give a series with no trend and seasonality.

To the transformed data $x_t$, one fits an $\text{ARMA}(p, q)$ model which can be done via the `ARIMA` function from the `statsmodels` library. The order $p$ and $q$ can be determined via a model selection criterion such as AIC or BIC.

## 2 ARIMA models

ARIMA stands for AutoRegressive Integrated Moving Average. ARIMA is essentially differencing plus ARMA.

**Definition 2.1** (ARIMA). *A time series model $y_t$ is said to be $\text{ARIMA}(p, d, q)$ if*
$$
\phi(B)((\nabla^d y_t) - \mu) = \theta(B)\epsilon_t,
$$
*where $\epsilon_t \overset{\text{i.i.d.}}{\sim} N(0, \sigma^2)$.*

ARIMA models are fit by the function `ARIMA()` in `statsmodels`. The mean $\mu$ above is taken to be zero by default when the order parameter $d$ in ARIMA is strictly larger than zero.

---

[Up: contents](index.md) · [3 Seasonal ARMA Models →](02-3-seasonal-arma-models.md)
