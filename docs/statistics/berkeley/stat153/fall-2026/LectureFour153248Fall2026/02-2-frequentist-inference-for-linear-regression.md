---
title: 2 Frequentist Inference for Linear Regression
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFour153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureFour153248Fall2026.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFour153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFour153248Fall2026.pdf) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Frequentist Inference for Linear Regression

The basic ideas behing frequentist inference are as follows:

1. Construct a method for estimating the unknown parameters. In the simple linear regression context, one can use least squares to estimate $\beta_0, \beta_1, \dots, \beta_m$. Probably the most popular estimation strategy is Maximum Likelihood Estimation (this requires writing down a likelihood function).

2. Calculate (exactly or using some approximations) the distribution of the estimators. Use quantiles of the distribution for obtaining interval estimates for the unknown parameters. The quantiles might themselves depend on other unknown parameters (which would then have to be replaced by estimates).

## 2.1 Estimates

### 2.1.1 Least Squares Estimates

For linear regression, the estimates are obtained by the method of least squares, where the sum of squares

$$S(\beta_0, \beta_1, \dots, \beta_m) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_{i1} - \dots - \beta_m x_{im})^2 \tag{2}$$

is minimized over all values of $\beta_0, \beta_1, \dots, \beta_m$. The minimizing values $\hat{\beta}_0, \dots, \hat{\beta}_m$ are known as least squares estimates.

Using the notation:

$$y = \begin{pmatrix} y_1 \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix} \quad X = \begin{pmatrix} 1 & x_{11} & \dots & x_{1m} \\ 1 & x_{21} & \dots & x_{2m} \\ \cdot & \cdot & \dots & \cdot \\ \cdot & \cdot & \dots & \cdot \\ \cdot & \cdot & \dots & \cdot \\ 1 & x_{n1} & \dots & x_{nm} \end{pmatrix} \quad \beta = \begin{pmatrix} \beta_0 \\ \beta_1 \\ \cdot \\ \cdot \\ \cdot \\ \beta_m \end{pmatrix} \quad \hat{\beta} = \begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \\ \cdot \\ \cdot \\ \cdot \\ \hat{\beta}_m \end{pmatrix},$$

the sum of squares function $S(\beta_0, \dots, \beta_m)$ can be written as

$$S(\beta) = \|y - X\beta\|^2.$$

The least squares estimator $\hat{\beta}$ is given by the formula:

$$\hat{\beta} = (X^T X)^{-1} X^T y. \tag{3}$$

The proof of (3) is as follows. The gradient of $S(\beta)$ is given by

$$\nabla S(\beta) = \nabla \left[ \|y - X\beta\|^2 \right]$$
$$= \nabla \left[ (y - X\beta)^T (y - X\beta) \right]$$
$$= \nabla \left[ y^T y - \beta^T X^T y - y^T X\beta + \beta^T X^T X\beta \right] = 2X^T y - 2X^T X\beta.$$

Because $\hat{\beta}$ minimizes $S(\beta)$, the gradient should equal zero when $\beta = \hat{\beta}$, and this leads to

$$X^T (y - X\hat{\beta}) = 0 \implies X^T X\hat{\beta} = X^T y \implies \hat{\beta} = (X^T X)^{-1} X^T y. \tag{4}$$

### 2.1.2 Maximum Likelihood Estimates (MLEs)

Under the assumption $\epsilon_i \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$, we can write the likelihood explicitly and maximize it to obtain MLEs. As seen below, the MLE of $\beta_0, \dots, \beta_m$ will coincide with least squares, but the ML method additionally will give an estimate of $\sigma$.

With the normality assumption $\epsilon_i \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$, the linear regression model can be rewritten as:

$$y_i \overset{\text{independent}}{\sim} N(\beta_0 + \beta_1 x_{i1} + \dots + \beta_m x_{im}, \sigma^2). \tag{5}$$

The likelihood then becomes:

$$f_{y_1, \dots, y_n \mid \beta_0, \dots, \beta_m, \sigma}(y_1, \dots, y_n) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left(-\frac{(y_i - \beta_0 - \beta_1 x_{i1} - \dots - \beta_m x_{im})^2}{2\sigma^2}\right)$$
$$= (2\pi)^{-n/2} \sigma^{-n} \exp\left(-\frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_{i1} - \dots - \beta_m x_{im})^2\right)$$
$$= (2\pi)^{-n/2} \sigma^{-n} \exp\left(-\frac{S(\beta_0, \dots, \beta_m)}{2\sigma^2}\right) \tag{6}$$

Recall $S(\beta_0, \dots, \beta_m)$ above is the sum of squares defined in (2). To write this likelihood, we are assuming that $x_1, \dots, x_n$ are fixed. This assumption is fine if $x_i = i$ (regression with time as covariate) but not strictly true when $x_i = y_{i-1}$ (auto-regression). We shall see how it is still approximately true in the case of AutoRegression later.

Another way to write the likelihood is to note that (5) is equivalent to:

$$y \sim N_n(X\beta, \sigma^2 I_n). \tag{7}$$

In other words, the $n$-dimensional vector $y$ is multivariate normal with mean $X\beta$ and covariance $\sigma^2 I_n$. Recall that the density of the multivariate normal $y \sim N_n(\mu, \Sigma)$ is given by:

$$\frac{1}{(2\pi)^{n/2}} \frac{1}{\sqrt{\det \Sigma}} \exp\left(-\frac{1}{2}(y - \mu)^T \Sigma^{-1} (y - \mu)\right).$$

Thus the density corresponding to (7) is:

\$\$(2\pi)^{-n/2} \sigma^{-n} \exp\left(-\frac{1}{2}(y - X\beta)^T (\sigma^2 I_n)^{-1} (y - X\beta)\right) = (2\pi)^{-n/2} \sigma^{-n

---

[← 1 Multiple Linear Regression](01-1-multiple-linear-regression.md) · [Up: contents](index.md)
