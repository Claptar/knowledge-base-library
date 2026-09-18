---
title: '1 Recap: Ridge Regression'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwelve153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwelve153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Recap: Ridge Regression

## Lecture Twelve
### Fall 2025, UC Berkeley
### Aditya Guntuboyina
### October 6, 2025

In this lecture, we discuss the Bayesian analogue of ridge regularization. Let us start by recapping ridge regression from the previous lecture.

Our model from the last two lectures is given by:
$$y_t = \beta_0 + \beta_1(t - 1) + \beta_2\text{ReLU}(t - 2) + \dots + \beta_{n-1}\text{ReLU}(t - (n - 1)) + \epsilon_t \tag{1}$$
where, as always, $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. Here $\text{ReLU}(t - c) = (t - c)_+$ equals $0$ if $t \le c$ and equals $(t - c)$ if $t > c$.

The unknown parameters in this model are $\beta_0, \beta_1, \dots, \beta_{n-1}$ as well as $\sigma$.

Alternatively, (1) can be written as:
$$y = X\beta + \epsilon$$
where
$$X = \begin{pmatrix}
1 & 0 & 0 & \dots & 0 \\
1 & 1 & 0 & \dots & 0 \\
1 & 2 & 1 & \dots & 0 \\
\cdot & \cdot & \cdot & \dots & \cdot \\
\cdot & \cdot & \cdot & \dots & \cdot \\
\cdot & \cdot & \cdot & \dots & \cdot \\
1 & n - 1 & n - 2 & \dots & 1
\end{pmatrix} \quad \text{and} \quad \beta = \begin{pmatrix}
\beta_0 \\
\beta_1 \\
\beta_2 \\
\beta_{n-1}
\end{pmatrix}. \tag{2}$$

The ridge regression estimator $\hat{\beta}_{\text{ridge}}(\lambda)$ for $\beta$ is given by the minimizer of:
$$\sum_{t=1}^n (y_t - \beta_0 - \beta_1(t - 1) - \beta_2\text{ReLU}(t - 2) - \dots - \beta_{n-1}\text{ReLU}(t - (n - 1)))^2$$
$$+ \lambda \left(\beta_2^2 + \beta_3^2 + \dots + \beta_{n-1}^2\right). \tag{3}$$

The objective function above can also be written as
$$\|y - X\beta\|^2 + \lambda \sum_{t=2}^{n-1} \beta_j^2.$$

It turns out that $\hat{\beta}_{\text{ridge}}(\lambda)$ can be written in closed form using matrix notation. To see this, note first that the gradient of the above objective function with respect to $\beta$ is given by
$$\nabla \left( \|y - X\beta\|^2 + \lambda \sum_{t=2}^{n-1} \beta_j^2 \right) = -2X^T y + 2X^T X\beta + 2\lambda \begin{pmatrix}
0 \\
0 \\
\beta_2 \\
\beta_{n-1}
\end{pmatrix}.$$

Let $J$ denote the $n \times n$ diagonal matrix whose diagonal entries are $0, 0, 1, \dots, 1$. In other words, the first two diagonal entries of $J$ are $0$ and the rest of the diagonal entries equal $1$:
$$J = \begin{pmatrix}
0 & 0 & 0 & 0 & \dots & 0 \\
0 & 0 & 0 & 0 & \dots & 0 \\
0 & 0 & 1 & 0 & \dots & 0 \\
0 & 0 & 0 & 1 & \dots & 0 \\
\cdot & \cdot & \cdot & \cdot & \dots & \cdot \\
\cdot & \cdot & \cdot & \cdot & \dots & \cdot \\
\cdot & \cdot & \cdot & \cdot & \dots & \cdot \\
0 & 0 & 0 & 0 & \dots & 1
\end{pmatrix}.$$

With this matrix, we can write
$$\nabla \left( \|y - X\beta\|^2 + \lambda \sum_{t=2}^{n-1} \beta_j^2 \right) = -2X^T y + 2X^T X\beta + 2\lambda \begin{pmatrix}
0 \\
0 \\
\beta_2 \\
\beta_{n-1}
\end{pmatrix} = -2X^T y + 2X^T X\beta + 2\lambda J\beta.$$

Setting this gradient equal to zero, we get
$$-2X^T y + 2X^T X\beta + 2\lambda J\beta = 0 \implies \left(X^T X + \lambda J\right) \beta = X^T y.$$
which gives
$$\hat{\beta}_{\text{ridge}}(\lambda) = (X^T X + \lambda J)^{-1} X^T y. \tag{4}$$
This looks very similar to the usual linear regression least squares formula $(X^T X)^{-1} X^T y$ with the only difference being the presence of the $\lambda J$ term.

---

[Up: contents](index.md) · [2 Bayesian Regularization →](02-2-bayesian-regularization.md)
