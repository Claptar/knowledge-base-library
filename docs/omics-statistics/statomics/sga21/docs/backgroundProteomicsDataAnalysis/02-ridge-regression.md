---
title: Ridge regression
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/backgroundProteomicsDataAnalysis.pdf
source_file: sources/statomics-sga21/docs/backgroundProteomicsDataAnalysis.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`docs/backgroundProteomicsDataAnalysis.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/backgroundProteomicsDataAnalysis.pdf) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Ridge regression

The untransformed, preprocessed intensities for each peptide $p$ in each run $r$ are assumed to follow a log-normal distribution. After log-transformation, these intensities become normally distributed. In all generality, for each protein, we propose the following peptide-based regression model that has also been proposed by Daly et al. (2008) [1]:

$$y_{pr} = \boldsymbol{x}_{pr}\boldsymbol{\beta} + \beta_p^{\text{peptide}} + u_r^{\text{run}} + \varepsilon_{pr}$$

Herein, $\boldsymbol{x}_{pr}$ is a row matrix with the covariate pattern related to peptide $p$ in run $r$, $\boldsymbol{\beta} = \left[\beta_0, \beta_1^1 \dots, \beta_{m_1}^1 \dots, \beta_{M_1}^1, \dots, \beta_{m_g}^g, \dots, \beta_{M_g}^g, \dots, \beta_{M_G}^G\right]^{\mathrm{T}}$ is a vector with $1 + M = 1 + \sum_{g=1}^G M_g$ parameters denoting the effects of $M$ predictors corresponding to $G$ covariates. $\beta_p^{\text{peptide}}$ is a peptide-specific effect for peptide $p$, $u_r^{\text{run}}$ a random run effect to account for within-run correlation, with $u_r^{\text{run}} \sim \mathrm{N}(0, \sigma_u^2)$. $\varepsilon_{pr} \sim \mathrm{N}(0, \sigma^2)$ is a random error term.

We now want to introduce an extra penalization on the fixed effects beta by exploiting the link between ridge regression and mixed models (see section 4.2.4). Except for a fixed intercept $\beta_0$, we penalize the parameters corresponding to each covariate group $g$ by assuming: $\beta_{m_g}^g \sim \mathrm{N}(0, \sigma^2 / \lambda_g)$ for $m_g = 1, \dots, M_g$. Herein, $g$ refers to the $g$th covariate and accounts for the fact that certain covariates are modeled with more than one parameter. For example, a treatment effect with three levels will be modeled with three dummy parameters $\beta_1^{\text{treatment}}$, $\beta_2^{\text{treatment}}$, and $\beta_3^{\text{treatment}}$ whereby $\beta_1^{\text{treatment}} + \beta_2^{\text{treatment}} + \beta_3^{\text{treatment}} = 0$. We also assume $\beta_p^{\text{peptide}} \sim \mathrm{N}(0, \sigma^2 / \lambda_{\text{peptide}})$. Therefore, the BLUP estimator for $\begin{bmatrix} \boldsymbol{\beta} \\ \boldsymbol{\beta}^{\text{peptide}} \\ \boldsymbol{u}^{\text{run}} \end{bmatrix}$ can be written as follows:

$$\begin{bmatrix} \hat{\boldsymbol{\beta}} \\ \hat{\boldsymbol{\beta}}^{\text{peptide}} \\ \hat{\boldsymbol{u}}^{\text{run}} \end{bmatrix} = (\boldsymbol{C}^{\mathrm{T}}\boldsymbol{C} + \boldsymbol{B})^{-1} \boldsymbol{C}^{\mathrm{T}}\boldsymbol{y}$$

With $\boldsymbol{y} = \begin{bmatrix} y_{11} \\ \dots \\ y_{1R} \\ \dots \\ y_{pr} \\ \dots \\ y_{P1} \\ \dots \\ y_{PR} \end{bmatrix}$ and $\boldsymbol{C} = \begin{bmatrix} \boldsymbol{x}_{11} & \boldsymbol{x}_1^{\text{peptide}} & \boldsymbol{x}_1^{\text{run}} \\ \dots & \dots & \dots \\ \boldsymbol{x}_{1R} & \boldsymbol{x}_1^{\text{peptide}} & \boldsymbol{x}_R^{\text{run}} \\ \dots & \dots & \dots \\ \boldsymbol{x}_{pr} & \boldsymbol{x}_p^{\text{peptide}} & \boldsymbol{x}_r^{\text{run}} \\ \dots & \dots & \dots \\ \boldsymbol{x}_{P1} & \boldsymbol{x}_P^{\text{peptide}} & \boldsymbol{x}_1^{\text{run}} \\ \dots & \dots & \dots \\ \boldsymbol{x}_{PR} & \boldsymbol{x}_P^{\text{peptide}} & \boldsymbol{x}_R^{\text{run}} \end{bmatrix}$. Herein $\boldsymbol{x}_p^{\text{peptide}}$ is a row vector of dummies, for which the $p$th element is equal to 1 and all other elements equal to 0. $\boldsymbol{x}_r^{\text{run}}$ is a row vector of dummies with the $r$th element equal to 1 and all other elements equal to 0. $\boldsymbol{B}$ is an $(1 + M + P + R) \times (1 + M + P + R)$ diagonal matrix with diagonal elements $[0\ \boldsymbol{g}\ \boldsymbol{p}\ \boldsymbol{r}]$, with $\boldsymbol{g}$ a vector of length $M$ containing the $\lambda_g$ that corresponds to each parameter estimate $\hat{\beta}_{m_g}^g$ for $m_g = 1, \dots, M_g$ and $g = 1, \dots, G$, $\boldsymbol{p}$ a vector of length $P$ containing the $\lambda_{\text{peptide}}$ that corresponds to each parameter estimate $\hat{\beta}_p^{\text{peptide}}$ for $p = 1, \dots, P$ and $\boldsymbol{r}$ a vector of length $R$ containing the $\frac{\hat{\sigma}_u^2}{\hat{\sigma}^2}$ that corresponds to each parameter estimate $\hat{u}_r^{\text{run}}$ for $r = 1, \dots, R$.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Robust regression with M estimation →](03-robust-regression-with-m-estimation.md)
