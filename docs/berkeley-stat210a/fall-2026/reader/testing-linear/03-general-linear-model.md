---
title: General Linear Model
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-linear.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-linear.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# General Linear Model

**Source:** [`reader/testing-linear.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-linear.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Many problems can be put into canonical linear model after change of basis.

### Basic Setup

Observe $Y \sim N(X\beta, \sigma^2 I_n)$, $\sigma^2$ known or unknown
Test $\beta \in \Theta_0$ vs $\beta \in \Theta_1$
where $\Theta_0 \subset \Theta_1$ are subspaces of $\mathbb{R}^p$
$\text{dim}(\Theta_0) = d_0$, $\text{dim}(\Theta_1) = d = d_0 + d_1$

Idea: rotate into canonical form

$d_0$, $d_1$, $n-d$
$\Theta_0$, $\Theta_1 \setminus \Theta_0$, $\mathbb{R}^n \setminus \Theta_1$

$Q = (Q_0 | Q_1 | Q_2)$ orthonormal basis for $(\Theta_0 | \Theta_1 \setminus \Theta_0 | \mathbb{R}^n \setminus \Theta_1)$

$Z = Q'Y \sim N_n(Q'\beta, \sigma^2 I_n)$

$H_0: Q_1'\beta = 0$

Do $Z$ $\chi^2$ or $F$ test as appropriate

### Example 1: Linear Regression

$Y_i = X_i'\beta + \epsilon_i$, $\epsilon_i \sim N(0, \sigma^2)$
$Y \sim N_n(X\beta, \sigma^2 I_n)$, $X \in \mathbb{R}^{n \times p}$

Assume $X$ has full column rank
$\Theta = X\beta \in \Theta = \text{Span}(X_1, \ldots, X_p)$

$H_0: \beta = (\beta_0', 0')' \in \Theta_0 = \text{Span}(X_1, \ldots, X_q)$ or $\beta_q = 0$ if $d_1 = 1$

$\|\hat{\beta} - \beta\|^2 = \|Y - \text{Proj}_\Theta Y\|^2$
$\hat{\beta} = \arg\min_\beta \|Y - X\beta\|^2 = (X'X)^{-1}X'Y$

$\hat{Y} = X\hat{\beta}$

Residual sum of squares (RSS): $\|Y - \hat{Y}\|^2 = \|Y - X\hat{\beta}\|^2$
$\text{RSS}_0 - \text{RSS}_1$

F-statistic is:

$$F = \frac{(\text{RSS}_0 - \text{RSS}_1)/d_1}{\text{RSS}_1/(n-d)} \sim F_{d_1,n-d}$$

$n-d$ called residual degrees of freedom

Let $X = (X_0 | X_1)$, $X \in \mathbb{R}^{n \times p}$
Let $X_1^\perp = X_1 - \text{Proj}_{X_0} X_1$
$X = (X_0 | X_0^\perp)$

Reparametrize: $X_1^\perp \beta_1 = X_1 \beta_1 - X_0 \beta_0$
$\Theta = X\beta = X_0 \beta_0 + X_1^\perp \beta_1$

$\hat{\beta}_1 = (X_1^{\perp'} X_1^\perp)^{-1} X_1^{\perp'} Y$
$\|\hat{\beta}_1\|^2 = \text{RSS}_0 - \text{RSS}_1$
$\text{SE}(\hat{\beta}_1) = \hat{\sigma}^2 (X_1^{\perp'} X_1^\perp)^{-1}$

t-statistic: $t = \frac{\hat{\beta}_1}{\text{SE}(\hat{\beta}_1)} \sim t_{n-d}$

### Example 2: Two-sample t-test (equal variance)

$Y_1, \ldots, Y_n \sim N(\mu_1, \sigma^2)$, $Y_{n+1}, \ldots, Y_{n+m} \sim N(\mu_2, \sigma^2)$

$Y = (Y_1, \ldots, Y_{n+m})'$, $\mathbb{E}[Y] = \mu_1 1_n + \mu_2 1_m$
Model: $\Theta = \text{Span}(1_{n+m}, (1_n', 0_m')')$

$H_0: \mu_1 = \mu_2 \implies \Theta_0 = \text{Span}(1_{n+m})$

$d_0 = 1$, $d = 2$, $d_1 = n+m-2$

Orthogonalize $1_{n+m}$

Reject for large:

$$t = \frac{\bar{Y}_1 - \bar{Y}_2}{\hat{\sigma}\sqrt{\frac{1}{n} + \frac{1}{m}}} \sim t_{n+m-2}$$

where $\hat{\sigma}^2 = \frac{\sum_{i=1}^n (Y_i - \bar{Y}_1)^2 + \sum_{i=1}^m (Y_i - \bar{Y}_2)^2}{n+m-2}$

### Example 3: One-way ANOVA (fixed effects)

$Y_{ki} \sim N(\mu_k, \sigma^2)$, $k=1,\ldots,m$, $i=1,\ldots,n$

$H_0: \mu_1 = \cdots = \mu_m$

$Y_{ki} = \mu + \alpha_k + \epsilon_{ki}$, $\sum \alpha_k = 0$

$\bar{Y}_{k\cdot} = \frac{1}{n} \sum_{i=1}^n Y_{ki}$, $\bar{Y} = \frac{1}{mn

---

[← Canonical Linear Model](02-canonical-linear-model.md) · [Up: contents](index.md)
