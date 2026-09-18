---
title: 1 Posterior $t$-density in Multiple Linear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFive153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFive153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Posterior $t$-density in Multiple Linear Regression

## Lecture Five
Fall 2025, UC Berkeley

Aditya Guntuboyina

September 11, 2025

In the last lecture, we saw the following formula for the posterior distribution in multiple linear regression:

$$
\beta_0, \dots, \beta_m \mid \text{data} \sim t_{m+1} \left( \hat{\beta}, \frac{S(\hat{\beta})}{n - m - 1} (X^T X)^{-1}, n - m - 1 \right). \tag{1}
$$

Recall in multiple regression: the data is $(x_{i1}, \dots, x_{im}, y_i)$, $i = 1, \dots, n$, and the model is:

$$
y_i = \beta_0 + \beta_1 x_{i1} + \dots + \beta_m x_{im} + \epsilon_i \quad \text{with } \epsilon_i \overset{\text{i.i.d}}{\sim} N(0, \sigma^2). \tag{2}
$$

For doing calculations in regression, we use the matrix notation:

$$
y = \begin{pmatrix} y_1 \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix}, \quad X = \begin{pmatrix} 1 & x_{11} & \dots & x_{1m} \\ 1 & x_{21} & \dots & x_{2m} \\ \cdot & \cdot & \dots & \cdot \\ \cdot & \cdot & \dots & \cdot \\ \cdot & \cdot & \dots & \cdot \\ 1 & x_{n1} & \dots & x_{nm} \end{pmatrix}, \quad \beta = \begin{pmatrix} \beta_0 \\ \beta_1 \\ \cdot \\ \cdot \\ \cdot \\ \beta_m \end{pmatrix}, \quad \hat{\beta} = \begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \\ \cdot \\ \cdot \\ \cdot \\ \hat{\beta}_m \end{pmatrix}
$$

In terms of this notation, we can rewrite the model equation (2) as:

$$
y = X\beta + \epsilon.
$$

In (1), $S(\hat{\beta})$ denotes the sum of squares evaluated at the least squares estimator. It is the smallest possible value of the sum of squares, and it is also known as the Residual Sum of Squares (RSS).

(1) represents the joint density of $(\beta_0, \dots, \beta_m)$ given the observed data. It turns out that the posterior distribution of each individual $\beta_j$ is also given by a $t$-density. This follows from properties of the multivariate $t$-density which we go over next.

---

[Up: contents](index.md) · [2 $t$-density →](02-2--density.md)
