---
title: Frequentist Inference
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureFour153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/HandwrittenNotesLectureFour153248Fall2026.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureFour153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureFour153248Fall2026.pdf) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Frequentist Inference

$$y_i = \underbrace{\beta_0} + \underbrace{\beta_1} x_{i1} + \dots + \underbrace{\beta_m} x_{im} + \underbrace{\varepsilon_i}_{\text{error}}$$

Unknown parameters:
$\beta_0, \beta_1, \beta_2, \dots, \beta_m, \quad \sigma$

$\to \varepsilon_i \overset{\text{iid}}{\sim} N(0, \sigma^2)$
$\varepsilon_i$ mean 0, independence, finite variance

(1) Construct estimates for the parameters. MLE, least squares
(2) Figure out the distribution of the estimate (exact or approximate). Use the distribution to construct confidence intervals.

**Estimate:** $\boxed{\text{Least Squares}} \qquad \beta = \begin{pmatrix} \beta_0 \\ \vdots \\ \beta_m \end{pmatrix}$

$\beta_0, \dots, \beta_m$

$$S(\beta) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_{i1} - \dots - \beta_m x_{im})^2$$

minimize $S(\beta)$ to get $\hat{\beta} = \begin{pmatrix} \hat{\beta}_0 \\ \vdots \\ \hat{\beta}_m \end{pmatrix}$

Solve $\hat{\beta}$ in closed form:
$$S(\beta) = \|y - X\beta\|^2, \qquad y = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}, \quad X = \begin{bmatrix} 1 & \vdots \\ & x_{ij} \\ 1 & \vdots \end{bmatrix}$$
$$= (y - X\beta)^T(y - X\beta)$$
$$= \underline{y^T y} - \underline{y^T X \beta} - \underline{\beta^T X^T y} + \beta^T X^T X \beta$$

$$\nabla S(\beta) = \begin{pmatrix} \frac{\partial S}{\partial \beta_0} \\ \vdots \\ \frac{\partial S}{\partial \beta_m} \end{pmatrix} \qquad \begin{aligned} f(x_1, \dots, x_k) &= a_1 x_1 + \dots + a_k x_k \\ \nabla f &= a \end{aligned}$$

$$\nabla S(\beta) = -X^T y - X^T y + 2X^T X \beta \quad (\text{Check})$$
$$\nabla (\beta^T X^T X \beta)$$
$\nabla(\beta^T A \beta) = 2A\beta$ if $A$ is symmetric.

$$\nabla S(\beta) = -2X^T y + 2X^T X \beta = 0$$
$$\boxed{X^T X \beta = X^T y}$$
$$\Rightarrow \boxed{\hat{\beta} = (X^T X)^{-1} X^T y} \to \text{Least Squares Estimator.}$$

## Maximum Likelihood

$$\varepsilon_i \overset{\text{iid}}{\sim} N(0, \sigma^2)$$
$$\to y_i \overset{\text{independent}}{\sim} N(\beta_0 + \beta_1 x_{i1} + \dots + \beta_m x_{im}, \sigma^2)$$

Data: $(y_i, x_{i1}, \dots, x_{im})$
Assume $x_{ij}$'s are fixed.

$$\prod_{i=1}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left[-\frac{(y_i - \beta_0 - \dots - \beta_m x_{im})^2}{2\sigma^2}\right]$$
$$= (2\pi)^{-n/2} \sigma^{-n} \exp\left[-\frac{S(\beta)}{2\sigma^2}\right] \to \text{Likelihood}$$

$$\text{log-likelihood} = -\frac{n}{2}\log 2\pi - n\log \sigma - \frac{S(\beta)}{2\sigma^2}$$

$$\nabla S(\beta) = 0 \Rightarrow \hat{\beta}_{\text{MLE}} = \hat{\beta}_{\text{Least Squares}}$$

$$-\frac{n}{\sigma} + \frac{S(\beta)}{\sigma^3} = 0 \Rightarrow \sigma = \sqrt{\frac{S(\beta)}{n}} \to \hat{\sigma}_{\text{MLE}} = \sqrt{\frac{S(\hat{\beta})}{n}}$$

Remember: $\hat{\beta}_{\text{MLE}} = \hat{\beta}_{\text{Least Squares}} = \hat{\beta} = (X^T X)^{-1} X^T y$
$$\hat{\sigma}_{\text{MLE}} = \sqrt{\frac{S(\hat{\beta})}{n}}$$

---

[← Multiple Linear Regression](01-multiple-linear-regression.md) · [Up: contents](index.md) · [Step 2: $\boxed{\text{Calculate the distribution.}}$ →](03-step-2.md)
