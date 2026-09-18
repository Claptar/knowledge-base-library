---
title: STAT 153 & 248 - Time Series
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEleven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEleven153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureEleven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEleven153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# STAT 153 & 248 - Time Series

### Lecture Eleven
Fall 2025, UC Berkeley
Aditya Guntuboyina
October 2, 2025

## 1 High-dimensional Linear Model from last class

In the last lecture, we introduced the following model for a given time series $y_1, \dots, y_n$:
$$y_t = \beta_0 + \beta_1(t - 1) + \beta_2 \text{ReLU}(t - 2) + \dots + \beta_{n-1} \text{ReLU}(t - (n - 1)) + \epsilon_t \tag{1}$$
where, as always, $\epsilon_t \stackrel{\text{i.i.d}}{\sim} N(0, \sigma^2)$. Here $\text{ReLU}(t - c) = (t - c)_+$ equals 0 if $t \leq c$ and equals $(t - c)$ if $t > c$.

The unknown parameters in this model are $\beta_0, \beta_1, \dots, \beta_{n-1}$ as well as $\sigma$. This is a high-dimensional model because the number of parameters (which is $n + 1$) is larger than the sample size $n$.

## 2 Two alternative representations of (1)

There are two alternative ways of writing the model (1). The first one is
$$y_t = \mu_t + \epsilon_t \quad \text{with } \epsilon_t \stackrel{\text{i.i.d}}{\sim} N(0, \sigma^2) \tag{2}$$
and
$$\mu_t = \beta_0 + \beta_1(t - 1) + \beta_2 \text{ReLU}(t - 2) + \dots + \beta_{n-1} \text{ReLU}(t - (n - 1)). \tag{3}$$
The $\beta$'s can be written in terms of $\mu_t$ as follows: $\beta_0 = \mu_1$, $\beta_1 = \mu_2 - \mu_1$, and
$$\beta_t = (\mu_{t+1} - \mu_t) - (\mu_t - \mu_{t-1}) \quad \text{for } t = 2, \dots, n - 1.$$
In (2), $\mu_t$ can be interpreted as the underlying trend present in the data.

The second way of writing (1) is in regression form:
$$y = X\beta + \epsilon$$
where
\$\$X = \begin{pmatrix}
1 & 0 & 0 & \cdot & \cdot & \cdot & 0 \\
1 & 1 & 0 & \cdot & \cdot & \cdot & 0 \\
1 & 2 & 1 & \cdot & \cdot & \cdot & 0 \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
1 & n-1 & n-2 & \cdot & \cdot & \cdot & 1
\end{pmatrix}
\quad \text{and } \beta = \begin{pmatrix}
\beta_0 \\
\beta_1 \\
\beta

---

[Up: contents](index.md)
