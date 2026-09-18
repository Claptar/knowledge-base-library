---
title: 1 Moving Average (MA) Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Moving Average (MA) Models

## Lecture Twenty

Fall 2025, UC Berkeley

Aditya Guntuboyina

November 06, 2025

In the last lecture, we introduced the notion of stationary time series models, and also started discussing stationarity of AutoRegressive models.

A time series model $\{y_t\}$ is said to be stationary if:

1. $\mathbb{E}y_t$ does not change with $t$
2. $\text{var}(y_t)$ does not change with $t$
3. $\text{cov}(y_t, y_{t+h})$ does not change with $t$ for every $h$.

For a stationary time series, the AutoCovariance Function (ACVF) is defined as
$$\gamma(h) := \text{cov}(y_t, y_{t+h}).$$

By stationarity,
$$\gamma(-h) = -\text{cov}(y_t, y_{t-h}) = \text{cov}(y_{t-h}, y_t) = \text{cov}(y_{t-h}, y_{t-h+h}) = \gamma(h).$$

Note also that $\gamma(0)$ equals the variance of $y_t$. The Autocorrelation Function (ACF) is given by:
$$\rho(h) = \text{corr}(y_t, y_{t+h}) = \frac{\text{cov}(y_t, y_{t+h})}{\sqrt{\text{var}(y_t)\text{var}(y_{t+h})}} = \frac{\gamma(h)}{\sqrt{\gamma(0) \times \gamma(0)}} = \frac{\gamma(h)}{\gamma(0)}.$$

An important class of stationary time series models are the Moving Average Models.

Given a positive integer $q \ge 1$, the Moving Average model with order $q$ (denoted by $\text{MA}(q)$) is defined by the equation:
$$y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \dots + \theta_q \epsilon_{t-q} \tag{1}$$
where $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. The $\text{MA}(q)$ model has $q + 2$ unknown parameters which are estimated from observed data: $\mu, \theta_1, \dots, \theta_q, \sigma$.

The $\text{MA}(q)$ model has been called the "Summation of Random Causes" by its inventor Slutzky in the original paper titled "The summation of random causes as the source of cyclic processes" published in Econometrica in 1937. Basically the $\epsilon_t$'s can be treated as random causes which are assumed to be independently and identically distributed. The actual observations $y_t$'s are consequences of these causes. The consequence for time $t$ depends on the cause for time $t$ as well as the causes for times $t - 1, \dots, t - q$. These different causes affect the consequence at time $t$ differently depending on the values of $\theta_1, \dots, \theta_q$. Note that successive observations $y_t$ share some common causes leading to dependence between the successive values of $y_t$.

The simplest of these $\text{MA}(q)$ models is $\text{MA}(1)$ (i.e., $q = 1$):
$$y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1}.$$

It is easy to check that each $\text{MA}(q)$ model is stationary. Here is the proof for $\text{MA}(1)$ (the proof for stationarity of $\text{MA}(q)$ for $q \ge 1$ is left as exercise). The mean of $y_t$ is clearly $\mathbb{E}y_t = \mu$ which does not change with $t$. The variance of $y_t$ is
$$\text{var}(y_t) = \text{var}(\mu + \epsilon_t + \theta_1 \epsilon_{t-1}) = \sigma^2 + \theta_1^2 \sigma^2$$
which also does not change with $t$. The covariance between $y_t$ and $y_{t+1}$ is
$$\text{cov}(y_t, y_{t+1}) = \text{cov}(\mu + \epsilon_t + \theta_1 \epsilon_{t-1}, \mu + \epsilon_{t+1} + \theta_1 \epsilon_t) = \text{cov}(\epsilon_t, \theta_1 \epsilon_t) = \theta_1 \sigma^2$$
which does not depend on $t$. The covariance between $y_t$ and $y_{t+2}$ is
$$\text{cov}(y_t, y_{t+2}) = \text{cov}(\mu + \epsilon_t + \theta_1 \epsilon_{t-1}, \mu + \epsilon_{t+2} + \theta_1 \epsilon_{t+1}) = 0$$
Similarly, it is easy to see that the covariance between $y_t$ and $y_{t+h}$ equals zero for every $h \ge 2$. The ACVF of $\text{MA}(1)$ is therefore
$$\gamma(h) = \begin{cases} \sigma^2 (1 + \theta_1^2) & : h = 0 \\ \sigma^2 \theta_1 & : |h| = 1 \\ 0 & : |h| > 1 \end{cases}$$
The ACF of $\text{MA}(1)$ is:
$$\rho(h) = \begin{cases} 1 & : h = 0 \\ \frac{\theta_1}{1+\theta_1^2} & : h = 1 \\ 0 & : h > 1 \end{cases}$$

---

[Up: contents](index.md) · [2 Stationarity of AR(1) →](02-2-stationarity-of-ar-1.md)
