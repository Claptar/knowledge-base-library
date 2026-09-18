---
title: Multiple Linear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureFour153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureFour153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureFour153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureFour153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Multiple Linear Regression

$y$: response
$x_1, x_2, \dots, x_m$: covariates

Data: $(y_i, x_{i1}, x_{i2}, \dots, x_{im}), \quad i = 1, \dots, n$

**Tabular Data**

| $y$ | $x_1$ | $\dots$ | $x_m$ |
|---|---|---|---|
|   |   |   |   |
| $y_i$ | $x_{i1}$ | $\dots$ | $x_{im}$ |
|   |   |   |   |

Model: $y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \dots + \beta_m x_{im} + \varepsilon_i$
$\varepsilon_i \overset{iid}{\sim} N(0, \sigma^2)$

(a) **Functions of Time as Covariates**:
- $x_1 = \text{time} \rightarrow x_{i1} = i$
- $x_2 = (\text{time})^2 \rightarrow x_{i2} = i^2$

---

- $x_3 = \cos(2\pi \times \text{time}) \rightarrow x_{i3} = \cos\left(2\pi \frac{i}{12}\right)$

(b) **AutoRegression**:
- $x_1 = y \text{ at the previous time} \rightarrow x_{i1} = y_{i-1}$
- $x_2 = y \text{ two time points before} \rightarrow x_{i2} = y_{i-2}$

$$S(\beta_0, \dots, \beta_m) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_{i1} - \dots - \beta_m x_{im})^2$$
$$\rightarrow \text{minimize to get } \hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_m \ (\text{least squares estimators})$$

$$\beta_0, \beta_1, \dots, \beta_m, \log\sigma \overset{iid}{\sim} \text{Unif}(-C, C)$$

$$\text{posterior of } \beta_0, \dots, \beta_m \propto \left[\frac{S(\hat{\beta}_0, \dots, \hat{\beta}_m)}{S(\beta_0, \dots, \beta_m)}\right]^{\frac{n}{2}}$$
$$p = m + 1$$

**Fact**: This posterior is a multivariate t-density

## Multivariate t-Density

$$\propto \left[\frac{1}{1 + \frac{1}{\nu}(x - \mu)^T \Sigma^{-1} (x - \mu)}\right]^{\frac{\nu + p}{2}}$$

$(x_1, \dots, x_p)$
$p$: dimension
$\nu$: degrees of freedom
$\mu$: location, $\Sigma$: scale or covariance

---

$$\left[\left(\frac{S(\hat{\beta}_0, \dots, \hat{\beta}_m)}{S(\beta_0, \dots, \beta_m)}\right)\right]^{\frac{n}{2}}$$

---

[← Bayesian Inference for Simple Linear Regression](01-bayesian-inference-for-simple-linear-regression.md) · [Up: contents](index.md) · [Matrix Notation for Regression →](03-matrix-notation-for-regression.md)
