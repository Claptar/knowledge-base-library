---
title: Model
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwelve153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureTwelve153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureTwelve153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwelve153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Model

## Model:
$$y_t = \beta_0 + \beta_1(t-1) + \beta_2 \text{ReLU}(t-2) + \dots + \beta_{n-1} \text{ReLU}(t-(n-1)) + \varepsilon_t$$
$$t = 1 \dots, n$$

$\to$ high-dimension linear regression

$$y = X\beta + \varepsilon \qquad \underset{n \times n}{X} = \begin{bmatrix} 1 & 0 & 0 & \dots & 0 \\ 1 & 1 & 0 & \dots & 0 \\ 1 & 2 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & n-1 & n-2 & \dots & 1 \end{bmatrix}$$

### (1) Least squares $\to$ Overfitting
$$\text{(fitted values} = \text{data)}$$
$$\hat{\beta} = (X^T X)^{-1} X^T y$$
$$X\hat{\beta} = y \to \text{overfitting}$$

### (2) Regularization:
- **Ridge:** $\|y - X\beta\|^2 + \lambda \left[ \sum_{j=2}^{n-1} \beta_j^2 \right]$
- **LASSO:** $\|y - X\beta\|^2 + \lambda \sum_{j=2}^{n-1} |\beta_j|$

### Why Regularize?
(1) want smoother fits without overfitting $\Big\}$ Our preference

---

(2) Regularization leads to improved prediction.
(underlies CV for $\lambda$-selection)
**Cross Validation**

## Formula for the Ridge Estimator

$$\|y - X\beta\|^2 + \lambda \sum_{j=2}^{n-1} \beta_j^2$$

$$(y - X\beta)^T(y - X\beta)$$

$$\nabla_\beta \left[ \beta^T X^T X \beta - 2\beta^T X^T y + y^T y + \lambda \sum_{j=2}^{n-1} \beta_j^2 \right]$$

$$= 2 X^T X \beta - 2 X^T y + 2\lambda \begin{pmatrix} 0 \\ 0 \\ \beta_2 \\ \vdots \\ \beta_{n-1} \end{pmatrix} = 0$$

$$\begin{pmatrix} 0 \\ 0 \\ \beta_2 \\ \vdots \\ \beta_{n-1} \end{pmatrix} = J\beta \quad \text{where} \quad J = \begin{bmatrix} 0 & & & 0 \\ & 0 & & \\ & & 1 & & \\ & & & \ddots & \\ 0 & & & & 1 \end{bmatrix}$$

$$X^T X \beta - X^T y + \lambda J \beta = 0$$
$$(X^T X + \lambda J)\beta = X^T y$$

---

$$\hat{\beta}^{\text{Ridge}}(\lambda) = (X^T X + \lambda J)^{-1} X^T y$$
$$\hat{\beta}^{\text{least squares}} = (X^T X)^{-1} X^T y \quad \swarrow \lambda = 0$$

---

[Up: contents](index.md) · [Bayesian Regularization →](02-bayesian-regularization.md)
