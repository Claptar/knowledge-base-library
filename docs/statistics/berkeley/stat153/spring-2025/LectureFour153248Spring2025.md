---
title: STAT 153 & 248 - Time Series
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFour153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFour153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFour153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFour153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# STAT 153 & 248 - Time Series

### Lecture Four
#### Spring 2025, UC Berkeley
#### Aditya Guntuboyina
#### January 30, 2025

## 1 Bayesian Inference for Regression

We observe a time series $y_1, \dots, y_n$. We can fit a line to this data using the model:
$$y_t = \beta_0 + \beta_1 t + \epsilon_t \quad \text{with } \epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2). \tag{1}$$
We can fit a more complicated trend function such as the cubic function to the data using the model:
$$y_t = \beta_0 + \beta_1 t + \beta_2 t^2 + \beta_3 t^3 + \epsilon_t \quad \text{with } \epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2). \tag{2}$$
(1) and (2) are both examples of the multiple linear regression model. More generally, the multiple linear regression model is given by:
$$y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \dots + \beta_m x_{im} + \epsilon_i \quad \text{with } \epsilon_i \overset{\text{i.i.d}}{\sim} N(0, \sigma^2). \tag{3}$$
There are $m$ covariates here and $x_{ij}$ is the $i^{\text{th}}$ value of the $j^{\text{th}}$ covariate. (1) is a special case of (3) with $m = 1$ and $x_{i1} = i$ for $i = 1, \dots, n$. (2) is a special case of (3) with $m = 3$ and $x_{i1} = i$, $x_{i2} = i^2$, $x_{i3} = i^3$. We shall assume that $n$ is much larger than $m$ (the case where $n$ is comparable or even smaller to $m$ is known as high-dimensional linear regression and we shall look at this later).

In Bayesian inference for (3), we work with the prior
$$\beta_0, \beta_1, \dots, \beta_m, \log \sigma \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C)$$
for a very large positive $C$. The joint posterior density of $\beta_0, \dots, \beta_m, \sigma$ is then given by
$$f_{\beta_0, \beta_1, \dots, \beta_m, \sigma|\text{data}}(\beta_0, \beta_1, \dots, \beta_m, \sigma)$$
$$\propto \sigma^{-n-1} \exp\left( -\frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_{i1} - \dots - \beta_m x_{im})^2 \right) I\{-C < \beta_0, \beta_1, \dots, \beta_m, \log \sigma < C\}.$$
The above is the joint posterior over $\beta_0, \beta_1, \dots, \beta_m \sigma$. The posterior over only the coefficient parameters $\beta_0, \beta_1$ can be obtained by integrating (or marginalizing) the parameter $\sigma$.
$$f_{\beta_0, \beta_1, \dots, \beta_m|\text{data}}(\beta_0, \beta_1, \dots, \beta_m)$$
\$\$=

---

[Up: contents](index.md)
