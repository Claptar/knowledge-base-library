---
title: Matrix Notation for Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureFour153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureFour153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureFour153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureFour153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Matrix Notation for Regression

Data: $y_i, \quad x_{i1}, \dots, x_{im} \quad i = 1, \dots, n$

$$\underset{n \times 1}{\underline{y}} = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix} \qquad \underset{n \times (m+1)}{X} = \begin{pmatrix} 1 & x_{11} & x_{12} & \dots & x_{1m} \\ 1 & x_{21} & x_{22} & & x_{2m} \\ \vdots & \vdots & \vdots & & \vdots \\ 1 & x_{n1} & x_{n2} & & x_{nm} \end{pmatrix}$$

`sm.OLS(y, X).fit()`

$$\underset{(m+1) \times 1}{\underline{\beta}} = \begin{pmatrix} \beta_0 \\ \beta_1 \\ \vdots \\ \beta_m \end{pmatrix} \qquad \underset{(m+1) \times 1}{\hat{\underline{\beta}}} = \begin{pmatrix} \hat{\beta}_0 \\ \vdots \\ \hat{\beta}_m \end{pmatrix}$$

$$S(\beta_0, \dots, \beta_m) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_{i1} - \dots - \beta_m x_{im})^2$$

$$S(\beta) = \|\underset{n \times 1}{y} - \underset{n \times (m+1)}{X}\underset{(m+1) \times 1}{\beta}\|^2$$

$$S(\beta) = \|y - X\beta\|^2$$

---

$$S(\beta) = (y - X\beta)^T (y - X\beta)$$
$$= y^T y - 2\beta^T X^T y + \beta^T X^T X \beta$$

Minimize to get a formula for least squares:

$$\nabla S(\beta) = \begin{pmatrix} \frac{\partial}{\partial \beta_0} S(\beta) \\ \frac{\partial}{\partial \beta_1} S(\beta) \\ \vdots \\ \frac{\partial}{\partial \beta_m} S(\beta) \end{pmatrix} = -2\nabla(\beta^T X^T y) + \nabla(\beta^T X^T X \beta)$$
$$= -2 X^T y + 2 X^T X \beta = 0$$

$$X^T X \beta = X^T y \implies \hat{\beta} = (X^T X)^{-1} X^T y$$

**Facts about $S(\beta)$**:

1. $\hat{\beta} = (X^T X)^{-1} X^T y \qquad \begin{cases} \hat{\beta}_1 = \frac{\sum (y_i - \bar{y})(x_i - \bar{x})}{\sum (x_i - \bar{x})^2} \\ \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x} \end{cases}$

2. $S(\beta) = \|y - X\beta\|^2$
   $= \|y - X\hat{\beta} + X\hat{\beta} - X\beta\|^2$
   $= (y - X\hat{\beta} + X\hat{\beta} - X\beta)^T (y - X\hat{\beta} + X\hat{\beta} - X\beta)$
   $= (y - X\hat{\beta})^T (y - X\hat{\beta}) + (\hat{\beta} - \beta)^T X^T X (\hat{\beta} - \beta) + \text{cross product term}$
   $= S(\hat{\beta}) + \text{Exercise : } = 0$

$$S(\beta) = S(\hat{\beta}) + (\hat{\beta} - \beta)^T X^T X (\hat{\beta} - \beta)$$

---

Posterior $\beta$: $\left[\frac{S(\hat{\beta})}{S(\beta)}\right]^{\frac{n}{2}}$

$$= \left\{\frac{S(\hat{\beta})}{S(\hat{\beta}) + (\beta - \hat{\beta})^T X^T X (\beta - \hat{\beta})}\right\}^{\frac{n}{2}}$$

**t-density**:

$$\left\{\frac{1}{1 + \frac{1}{\nu}(x - \mu)^T \Sigma^{-1} (x - \mu)}\right\}^{\frac{\nu + p}{2}}$$

$$\left\{\frac{1}{1 + \frac{(\beta - \hat{\beta})^T X^T X (\beta - \hat{\beta})}{S(\hat{\beta})}}\right\}^{\frac{n}{2}}$$

$p = m + 1, \quad \nu + p = n \implies \nu = n - p = n - m - 1$

$\mu = \hat{\beta}: \quad \frac{1}{\nu} \Sigma^{-1} = \frac{X^T X}{S(\hat{\beta})}$

$$\implies \Sigma = \frac{S(\hat{\beta})}{\nu} (X^T X)^{-1}$$

$$\Sigma = \frac{S(\hat{\beta})}{n - m - 1} (X^T X)^{-1}$$

---

$$\underset{\text{of } \beta_0, \dots, \beta_m}{\text{Posterior}} : t_{m+1}\left(\underset{\substack{\downarrow \\ \text{least} \\ \text{squares}}}{\hat{\beta}}, \, \frac{S(\hat{\beta})}{n - m - 1}(X^T X)^{-1}, \, n - m - 1\right)$$

$$\text{Simulate } \beta^{(1)}, \beta^{(2)}, \dots, \beta^{(N)}$$

$S(\hat{\beta})$: Residual Sum of Squares

$$\sum (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_{i1} - \dots - \hat{\beta}_m x_{im})^2$$

$y_i - \hat{\beta}_0 - \hat{\beta}_1 x_{i1} - \dots - \hat{\beta}_m x_{im}: i^{\text{th}}$ residual

---

[← Multiple Linear Regression](02-multiple-linear-regression.md) · [Up: contents](index.md)
