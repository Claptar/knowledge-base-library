---
title: 1 Background
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Background

## Lecture Ten
Fall 2025, UC Berkeley

Aditya Guntuboyina

October 1, 2025

We will now start our third main topic: High-dimensional linear regression. We shall motivate our basic high-dimensional linear regression model starting from the change of slope (or broken stick regression) model that we previously considered.

The change of slope (or broken stick regression) model is given by:
$$
y_t = \beta_0 + \beta_1 t + \beta_2(t - c)_+ + \epsilon_t. \tag{1}
$$
Recall that $(t - c)_+$ equals $0$ if $t \leq c$ and $t - c$ if $t \geq c$. We shall also sometimes write $(t - c)_+ = \text{ReLU}(t - c)$. The model (1) says that for times $t \leq c$, the slope of the regression line is $\beta_1$ while for $t > c$, the slope changes to $\beta_1 + \beta_2$. Note $\beta_2$ represents the change in slopes (after $t = c$ and before $t = c$).

Generalizations of model (1) can be obtained by having $k$ points of change of slope (instead of just one):
$$
y_t = \beta_0 + \beta_1 t + \beta_2\text{ReLU}(t - c_1) + \beta_3\text{ReLU}(t - c_2) + \dots + \beta_{k+1}\text{ReLU}(t - c_k) + \epsilon_t. \tag{2}
$$
We use least squares to estimate the unknown parameters $c_1, \dots, c_k, \beta_0, \beta_1, \dots, \beta_{k+1}$ in this model. In the previous lectures, we recommended the method where we first compute the function:
$$
RSS(c_1, \dots, c_k) := \min_{\beta_0, \dots, \beta_{k+1}} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 t - \beta_2\text{ReLU}(t - c_1) - \dots - \beta_{k+1}\text{ReLU}(t - c_k))^2
$$
and then attempt to minimize $RSS(c_1, \dots, c_k)$ by some grid-based search jointly over $c_1, \dots, c_k$ to estimate $c_1, \dots, c_k$. Once $c_1, \dots, c_k$ are estimated by $\hat{c}_1, \dots, \hat{c}_k$, we estimate the remaining parameters $\beta_0, \dots, \beta_{k+1}$ by least squares in the linear regression model obtained by fixing each $c_j$ by $\hat{c}_j$.

This method is computationally inefficient especially when $k$ is not small (even when $k \geq 3$). An alternative method of obtaining the least squares estimates is to directly minimize the least squares objective with respect to all parameters:
$$
\min_{\beta_0, \dots, \beta_{k+1}, c_1, \dots, c_k} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 t - \beta_2\text{ReLU}(t - c_1) - \dots - \beta_{k+1}\text{ReLU}(t - c_k))^2. \tag{3}
$$

This is a non-trivial optimization problem but several optimization libraries provide functions which can be employed for solving this. One option is the PyTorch library in Python which uses first order optimization algorithms (gradient descent and related methods). These methods require a good initialization for the parameters (for $c_1, \dots, c_k$, a natural initialization is to take equally spaced quantiles of $t$; once $c_j$'s are chosen, initial values for $\beta_0, \dots, \beta_{k+1}$ can be obtained by running a linear regression with those fixed $c_j$'s).

When $k$ is not small, the least squares estimates (3) can lead to fitted values which overfit the data. In such cases, we need to add a regularization term to the objective function to prevent overfitting. We shall see how to do this in the case of the high-dimensional model which uses all possible $c_j$'s.

---

[Up: contents](index.md) · [2 High-dimensional Version of (2) →](02-2-high-dimensional-version-of-2.md)
