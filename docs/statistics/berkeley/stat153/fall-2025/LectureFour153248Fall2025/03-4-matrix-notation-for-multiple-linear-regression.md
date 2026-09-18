---
title: 4 Matrix Notation for Multiple Linear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFour153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFour153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFour153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFour153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Matrix Notation for Multiple Linear Regression

$$
y = \begin{pmatrix} y_1 \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix} \quad
X = \begin{pmatrix} 1 & x_{11} & \dots & x_{1m} \\ 1 & x_{21} & \dots & x_{2m} \\ \cdot & \cdot & \dots & \cdot \\ \cdot & \cdot & \dots & \cdot \\ \cdot & \cdot & \dots & \cdot \\ 1 & x_{n1} & \dots & x_{nm} \end{pmatrix} \quad
\beta = \begin{pmatrix} \beta_0 \\ \beta_1 \\ \cdot \\ \cdot \\ \cdot \\ \beta_m \end{pmatrix} \quad
\hat{\beta} = \begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \\ \cdot \\ \cdot \\ \cdot \\ \hat{\beta}_m \end{pmatrix}
$$
This notation is used not just to write formulae for linear regression, but also in code. For example, the OLS function in statsmodels uses the syntax `sm.OLS(y, X).fit()` to fit the linear regression model, where $y$ ($n \times 1$ vector) and $X$ ($n \times (m + 1)$ matrix) are defined above.

With this notation, one can write the sum of squares $S(\beta_0, \dots, \beta_m)$ as:
$$
S(\beta) = S(\beta_0, \dots, \beta_m) = \|y - X\beta\|^2.
$$
There are two important facts about $S(\beta)$:

1. **Fact 1:** the least squares estimator $\hat{\beta}$ is given by the formula:
$$
\hat{\beta} = (X^T X)^{-1} X^T y. \tag{7}
$$
The proof of (7) is as follows. The gradient of $S(\beta)$ is given by
$$
\begin{aligned}
\nabla S(\beta) &= \nabla [\|y - X\beta\|^2] \\
&= \nabla [(y - X\beta)^T (y - X\beta)] \\
&= \nabla [y^T y - \beta^T X^T y - y^T X\beta + \beta^T X^T X \beta] = 2X^T y - 2X^T X\beta.
\end{aligned}
$$

Because $\hat{\beta}$ minimizes $S(\beta)$, the gradient should equal zero when $\beta = \hat{\beta}$, and this leads to
$$
X^T(y - X\hat{\beta}) = 0 \implies X^T X\hat{\beta} = X^T y \implies \hat{\beta} = (X^T X)^{-1} X^T y. \tag{8}
$$

2. **Fact 2:** The following Pythagorean identity holds:
$$
S(\beta) = S(\hat{\beta}) + \|X\beta - X\hat{\beta}\|^2 = S(\hat{\beta}) + (\beta - \hat{\beta})^T X^T X (\beta - \hat{\beta}). \tag{9}
$$
To prove (9), write
$$
\begin{aligned}
S(\beta) &= \|y - X\beta\|^2 \\
&= \|y - X\hat{\beta} + X\hat{\beta} - X\beta\|^2 \\
&= \|y - X\hat{\beta}\|^2 + \|X\hat{\beta} - X\beta\|^2 + 2\langle y - X\hat{\beta}, X\hat{\beta} - X\beta \rangle.
\end{aligned}
$$
The cross product is zero (leading to (9)) because:
$$
\begin{aligned}
\langle y - X\hat{\beta}, X\hat{\beta} - X\beta \rangle &= (X\hat{\beta} - X\beta)^T (y - X\hat{\beta}) \\
&= (\hat{\beta} - \beta)^T X^T (y - X\hat{\beta}) = (\hat{\beta} - \beta)^T (X^T y - X^T X\hat{\beta}) = 0
\end{aligned}
$$
where we used (8).

Using (9), we can write the posterior density (2) as
$$
\begin{aligned}
f_{\beta|\text{data}}(\beta) &\propto \left( \frac{S(\hat{\beta})}{S(\beta)} \right)^{n/2} \\
&= \left( \frac{S(\hat{\beta})}{S(\hat{\beta}) + (\beta - \hat{\beta})^T X^T X (\beta - \hat{\beta})} \right)^{n/2} \\
&= \left( \frac{1}{1 + (\beta - \hat{\beta})^T \frac{X^T X}{S(\hat{\beta})} (\beta - \hat{\beta})} \right)^{n/2}.
\end{aligned} \tag{10}
$$
The above formula is a special case of (6) with
$$
x = \beta, \quad p = m + 1, \quad \mu = \hat{\beta}, \quad \nu + p = n, \quad \frac{\Sigma^{-1}}{\nu} = \frac{X^T X}{S(\hat{\beta})}
$$
or equivalently
$$
x = \beta, \quad p = m + 1, \quad \mu = \hat{\beta}, \quad \nu = n - m - 1, \quad \Sigma = \frac{S(\hat{\beta})}{n - m - 1} (X^T X)^{-1}.
$$
We thus have
$$
\beta_0, \dots, \beta_m \mid \text{data} \sim t_{m+1} \left( \hat{\beta}, \frac{S(\hat{\beta})}{n - m - 1} (X^T X)^{-1}, n - m - 1 \right). \tag{11}
$$
With the posterior density (11), one can do uncertainty quantification about the parameters $\beta_0, \beta_1, \dots, \beta_m$. One can generate multiple samples from $t_{m+1}(\hat{\beta}, (S(\hat{\beta})/(n - m - 1))(X^T X)^{-1}, n - m - 1)$ and plot the resulting fitted values to visualize the uncertainty in the coefficients.

---

[← 2 Multiple Linear Regression](02-2-multiple-linear-regression.md) · [Up: contents](index.md)
