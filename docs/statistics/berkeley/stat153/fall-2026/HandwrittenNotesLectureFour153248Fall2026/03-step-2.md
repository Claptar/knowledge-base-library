---
title: 'Step 2: $\boxed{\text{Calculate the distribution.}}$'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureFour153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/HandwrittenNotesLectureFour153248Fall2026.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureFour153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureFour153248Fall2026.pdf) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Step 2: $\boxed{\text{Calculate the distribution.}}$

$$\hat{\beta} = \underbrace{(X^T X)^{-1} X^T}_{A} y \qquad y_i \overset{\text{ind}}{\sim} N(\beta_0 + \beta_1 x_{i1} + \dots + \beta_m x_{im}, \sigma^2)$$

$$y = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix} \sim N$$

Recall:
(a) $X \sim N_p(\mu, \Sigma) : \frac{1}{(\sqrt{2\pi})^p \sqrt{\det \Sigma}} \exp\left(-\frac{(x - \mu)^T \Sigma^{-1}(x - \mu)}{2}\right)$
(b) $X \sim N(\mu, \Sigma) \Rightarrow AX \sim N(A\mu, A\Sigma A^T)$

$$\hat{\beta} = (X^T X)^{-1} X^T y, \quad \boxed{y \sim N(X\beta, \sigma^2 I)}$$

$$y_i \overset{\text{ind}}{\sim} N(\beta_0 + \beta_1 x_{i1} + \dots + \beta_m x_{im}, \sigma^2)$$

$$\begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix} \sim N\left( \begin{pmatrix} \beta_0 + \beta_1 x_{11} + \dots + \beta_m x_{1m} \\ \beta_0 + \beta_1 x_{21} + \dots + \beta_m x_{2m} \\ \vdots \\ \beta_0 + \beta_1 x_{n1} + \dots + \beta_m x_{nm} \end{pmatrix}, \begin{pmatrix} \sigma^2 & & 0 \\ & \ddots & \\ 0 & & \sigma^2 \end{pmatrix} \right)$$
$$= X\beta, \quad \sigma^2 I_n$$

$$\left. \begin{aligned} y &\sim N(X\beta, \sigma^2 I) \\ \hat{\beta} &= \underbrace{(X^T X)^{-1} X^T}_{A} y \end{aligned} \right\} \Rightarrow \boxed{\hat{\beta} \sim N(\beta, \sigma^2(X^T X)^{-1})} \quad \begin{gathered} \text{DETAILS} \\ \text{SKIPPED} \end{gathered}$$

$$\boxed{\hat{\beta} \sim N(\beta, \sigma^2(X^T X)^{-1})}$$

$$\hat{\sigma}_{\text{MLE}} = \sqrt{\frac{S(\hat{\beta})}{n}}$$
$$\Rightarrow \hat{\sigma}_{\text{MLE}}^2 = \frac{S(\hat{\beta})}{n} \sim \frac{\sigma^2}{n} \chi_{n-m-1}^2$$
$$S(\hat{\beta}) = \sum (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_{i1} - \dots - \hat{\beta}_m x_{im})^2$$

---

$$\boxed{\hat{\sigma}_{\text{MLE}}^2 \sim \frac{\sigma^2}{n} \chi_{n-m-1}^2}$$

$$\mathbb{E}\,\hat{\sigma}_{\text{MLE}}^2 = \frac{\sigma^2}{n} \times (n - m - 1)$$

$\hat{\sigma}_{\text{MLE}}^2$ is **NOT** unbiased for $\sigma^2$.

$$\hat{\sigma}_{\text{unbiased}}^2 = \frac{S(\hat{\beta})}{n - m - 1} \leftrightarrow \hat{\sigma}_{\text{MLE}}^2 = \frac{S(\hat{\beta})}{n}$$

**Recap:** $\hat{\beta} = (X^T X)^{-1} X^T y \sim N(\beta, \sigma^2(X^T X)^{-1})$
$$\hat{\sigma}_{\text{MLE}}^2 \sim \frac{\sigma^2}{n} \chi_{n-m-1}^2$$
$$\hat{\sigma}_{\text{unbiased}}^2 = \frac{n}{n - m - 1} \hat{\sigma}_{\text{MLE}}^2$$

$$\beta_j : \quad \hat{\beta}_j \sim N\left(\beta_j, \sigma^2 ((X^T X)^{-1})_{(j+1, j+1)}\right)$$

$$\left[ \hat{\beta}_j - z_{\frac{\alpha}{2}} \sigma \sqrt{(X^T X)^{-1}_{(j+1, j+1)}}, \quad \hat{\beta}_j + z_{\frac{\alpha}{2}} \sigma \sqrt{(X^T X)^{-1}_{(j+1, j+1)}} \right]$$

$$\left[ \hat{\beta}_j - t_{n-m-1, \frac{\alpha}{2}} \hat{\sigma}_{\text{unbiased}} \sqrt{(X^T X)^{-1}_{(j+1, j+1)}}, \quad \hat{\beta}_j + t_{n-m-1, \frac{\alpha}{2}} \hat{\sigma}_{\text{unbiased}} \sqrt{(X^T X)^{-1}_{(j+1, j+1)}} \right]$$

---

$t$-distribution
quantile $t_{n-m-1, \frac{\alpha}{2}}$

$$\hat{\beta} = (X^T X)^{-1} X^T y \qquad (y \sim N(X\beta, \sigma^2 I))$$

---

[← Frequentist Inference](02-frequentist-inference.md) · [Up: contents](index.md) · [Bayesian Approach →](04-bayesian-approach.md)
