---
title: Multiple Regression
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureFive153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/HandwrittenNotesLectureFive153248Fall2026.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureFive153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureFive153248Fall2026.pdf) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Multiple Regression

153 - 248

## Multiple Regression:

Covariates: $(x_{i1} \dots x_{im})$

Response: $y_i$

$i = 1 \dots n$

Equation:
$$y_i = \beta_0 + \beta_1 x_{i1} + \dots + \beta_m x_{im} + \varepsilon_i$$

Model:
$$\begin{aligned}
\beta_0, \beta_1, \dots, \beta_m &\overset{iid}{\sim} \text{Unif}(-C, C) \quad C \to \infty \\
\varepsilon_i &\overset{iid}{\sim} N(0, \sigma^2) \\
\log \sigma &\sim \text{Unif}(-C, C)
\end{aligned}$$

Likelihood model: $\beta_0, \beta_1, \dots, \beta_m$

Prior: Figure this out

$\text{data} = (y_1 \dots y_n)$

$\longrightarrow$ posterior: $\beta, \sigma \mid y_1 \dots y_n$

$$f_{\beta_0 \dots \beta_m \mid y_1 \dots y_n}(\beta_0 \dots \beta_m) = \int_0^\infty f_{\beta_0 \dots \beta_m, \sigma \mid y_1 \dots y_n}(\beta_0 \dots \beta_m, \sigma) \, d\sigma$$

can be written explicitly.

Integration also explicit ($C \to \infty$)

$$f_{\beta_0 \dots \beta_m \mid y_1 \dots y_n}(\beta_0 \dots \beta_m) \propto \left[ \frac{1}{S(\beta)} \right]^{n/2}$$

$$S(\beta) = S(\beta_0, \beta_1, \dots, \beta_m) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_{i1} - \dots - \beta_m x_{im})^2$$

(1) Suppose $\hat{\beta}$ minimizes $S(\beta)$ $\longrightarrow$ least squares estimate
then $f_{\beta \mid \text{data}}(\beta)$ is maximized at $\hat{\beta}$.

$$\begin{aligned}
f_{\beta \mid \text{data}}(\beta) &\propto \left( \frac{1}{S(\beta)} \right)^{n/2} \longrightarrow \\
&\propto \left( \frac{S(\hat{\beta})}{S(\beta)} \right)^{n/2} \longrightarrow
\end{aligned}$$

$$f_{\beta \mid \text{data}}(\beta) \propto \left( \frac{S(\hat{\beta})}{S(\beta)} \right)^{n/2} \longrightarrow \text{maximized at } \beta = \hat{\beta}$$

$(\beta_0 \dots \beta_m)$

When $n$ is large, this is highly concentrated around the least squares estimator.

## Connection to the multivariate $t$-density

$t$-density: $x = (x_1, \dots x_p)$, $\nu$: degrees of freedom

$$\propto \left[ \frac{1}{1 + \frac{1}{\nu}(x - \mu)^T \Sigma^{-1} (x - \mu)} \right]^{\frac{\nu + p}{2}} \longleftarrow \left( \frac{S(\hat{\beta})}{S(\beta)} \right)^{n/2}$$

$$t_p(\mu, \Sigma, \nu)$$

## Normal Density

$$\propto \exp\left[ -\frac{(x - \mu)^T \Sigma^{-1} (x - \mu)}{2} \right]$$

$\exp[-\text{square function}]$

Notation: $N_p(\mu, \Sigma)$

(a) $X \sim N_p(\mu, \Sigma)$ then $\mu = \begin{pmatrix} \mathbb{E} X_1 \\ \mathbb{E} X_2 \\ \vdots \\ \mathbb{E} X_p \end{pmatrix}$

$$\Sigma = \begin{bmatrix} \text{Var}(X_1) & & & \\ & \text{Var}(X_2) & \text{Cov}(X_i, X_j) & \\ & \text{Cov}(X_i, X_j) & \ddots & \\ & & & \text{Var}(X_p) \end{bmatrix}$$

$$\Sigma(i, j) = \text{Cov}(X_i, X_j)$$

$$\begin{pmatrix} X_1 \\ X_2 \\ \vdots \\ X_5 \end{pmatrix} \sim N_5(\mu, \Sigma)$$

$\to \text{Var}(X_4) = \Sigma(4, 4)$

(b) $X \sim N_p(\mu, \Sigma) \to$ all components of $X$ are normal
$$\implies X_2 \sim N(\mu_2, \Sigma(2, 2))$$
$$X_j \sim N(\mu_j, \Sigma(j, j))$$

$\to$ every linear combination of $X_1 \dots X_p$ is normal

$$\begin{pmatrix} X_1 \\ X_2 \end{pmatrix} \sim N_2 \left( \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \begin{pmatrix} \Sigma(1, 1) & \Sigma(1, 2) \\ \Sigma(2, 1) & \Sigma(2, 2) \end{pmatrix} \right)$$

## $t$ & Normal

Suppose $X \sim N_p(\mu, \Sigma)$

$$X = \mu + (X - \mu)$$

Define
$$T = \mu + \frac{X - \mu}{\sqrt{V / \nu}} \quad \text{where } V \sim \chi^2_\nu$$

**chi-squared $\chi^2_\nu$**:
$$Z_1^2 + \dots + Z_\nu^2$$
$$Z_j \sim N(0, 1)$$
$$\mathbb{E}(\chi^2_\nu) = \nu$$
$$\mathbb{E}(Z_j^2) = 1$$

$$T = \mu + \frac{X - \mu}{\sqrt{\frac{Z_1^2 + \dots + Z_\nu^2}{\nu}}}$$

**Fact:** $T \sim t_p(\mu, \Sigma, \nu)$

$T_j \to j^{\text{th}}$ component of $T$

$$T = \mu + \frac{X - \mu}{\sqrt{\frac{Z_1^2 + \dots + Z_\nu^2}{\nu}}}$$

$$T_j = \mu_j + \frac{X_j - \mu_j}{\sqrt{\frac{Z_1^2 + \dots + Z_\nu^2}{\nu}}} \sim t_1(\mu_j, \Sigma(j, j), \nu)$$

Individual components of Multivariate $t$ are univariate $t$.

---

Up: contents · Back to Linear Regression →
