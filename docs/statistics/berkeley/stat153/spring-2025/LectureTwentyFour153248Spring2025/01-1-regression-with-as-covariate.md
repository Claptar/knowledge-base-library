---
title: 1 Regression with $t$ as covariate
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyFour153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentyFour153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Regression with $t$ as covariate

## Lecture Twenty Four

Spring 2025, UC Berkeley

Aditya Guntuboyina

April 24, 2025

The last topic in this course is Recurrent Neural Networks (RNNs). In order to motivate RNNs, let us first recap some models that we have already studied in this class.

The simplest and the first model that we studied was the linear regression model:
$$y_t = \beta_0 + \beta_1 t + \epsilon_t \quad \text{with } \epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2). \tag{1}$$
We then studied at nonlinear regression. One way to make the right hand side of (1) nonlinear in $t$ is to introduce terms involving $(t - c)_+$ for certain knots $c$:
$$y_t = \beta_0 + \beta_1 t + \beta_2(t - c_1)_+ + \dots + \beta_{k+1}(t - c_k)_+ + \epsilon_t. \tag{2}$$
Here $(t - c)_+$ is the positive part function applied to $t - c_1$. We shall also use the notation ReLU and $\sigma(\cdot)$ to denote this function (please do not confuse the function $\sigma(\cdot)$ with the standard deviation $\sigma$ of $\epsilon_t$; we shall use the same notation for both but they can be easily distinguished from the context):
$$\sigma(u) = \text{ReLU}(u) = u_+ := \max(u, 0).$$
The unknown parameters in (2) are $\beta_0, \dots, \beta_{k+1}, c_1, \dots, c_k$ and $\sigma$.

The model (2) is also a linear model but it is linear in the modified variables $1, t, (t - c_1)_+, \dots, (t - c_k)_+$ (and nonlinear in the original variable $t$). The vector of these modified variables:
$$(1, t, (t - c_1)_+, \dots, (t - c_k)_+)^T$$
can be called the feature vector. The model is a linear function of the feature vectors.

We now rewrite the model (2) in a slightly different form. The time $t$ represents the covariate $x_t$ here, so we write $x_t = t$. We shall remove the term $t$ as it is covered by $t = (t - c)_+$ for $c = 0$ (note that $1 \le t \le n$). We also write $\mu_t$ for the mean of $y_t$. We shall also use $r_t$ to denote the feature vector:
$$r_t = (\sigma(x_t - c_1), \dots, \sigma(x_t - c_k))^T$$
and $s_t$ to denote:
$$s_t = (x_t - c_1, \dots, x_t - c_k)^T.$$

With these changes, the model (2) becomes:
$$\begin{aligned}
x_t &= t \\
s_t &= (x_t - c_1, \dots, x_t - c_k)^T \\
r_t &= \sigma(s_t) \\
\mu_t &= \beta_0 + \beta^T r_t \\
y_t &= \mu_t + \epsilon_t.
\end{aligned} \tag{3}$$
In words, the univariate covariate $x_t$ (which is simply $t$) is first converted to the $k \times 1$ vector $s_t$ in a linear fastion. Then the nonlinear function $\sigma(\cdot)$ is applied to $s_t$ (here $\sigma(\cdot)$ is applied separately to each coordinate of $s_t$) to generate the feature vector $r_t$. Then $\mu_t$ is a linear function of $r_t$ which serves as the mean to $y_t$.

---

[Up: contents](index.md) · [2 AutoRegression →](02-2-autoregression.md)
