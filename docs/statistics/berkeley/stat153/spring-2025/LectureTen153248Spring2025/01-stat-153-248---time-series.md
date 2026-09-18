---
title: STAT 153 & 248 - Time Series
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTen153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# STAT 153 & 248 - Time Series

## Lecture Ten
### Spring 2025, UC Berkeley
### Aditya Guntuboyina
### February 20, 2025

For a given time series $y_1, \dots, y_n$, we consider the model:
$$y_t = \beta_0 + \beta_1(t - 1) + \beta_2\text{ReLU}(t - 2) + \dots + \beta_{n-1}\text{ReLU}(t - (n - 1)) + \epsilon_t \tag{1}$$
where, as always, $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. Here $\text{ReLU}(t - c) = (t - c)_+$ equals $0$ if $t \le c$ and equals $(t - c)$ if $t > c$.

The unknown parameters in this model are $\beta_0, \beta_1, \dots, \beta_{n-1}$ as well as $\sigma$. The model (1) should be compared with the following model that we studied in the previous lecture:
$$y_t = \beta_0 + \beta_1(t - 1) + \beta_2\text{ReLU}(t - c_1) + \beta_3\text{ReLU}(t - c_2) + \dots + \beta_{k+1}\text{ReLU}(t - c_k) + \epsilon_t. \tag{2}$$
Here are the main differences between these two models:

1. The model (2) will be used with a small value of $k$ (such as $1, 2, 3, 4$). This makes it a low-dimensional model. On the other hand, the number of unknown parameters in (1) equals $n + 1$ which is quite large. So (1) is an example of a high-dimensional model.

2. (2) is a nonlinear model because of the presence of the parameters $c_1, \dots, c_k$. On the other hand, there are no such nonlinear parameters in (1) which makes it a linear regression model.

To summarize, (2) is a low-dimensional nonlinear regression model, while (1) is a high-dimensional linear regression model.

---

[Up: contents](index.md) · [1 Parameter Interpretation in (1) →](02-1-parameter-interpretation-in-1.md)
