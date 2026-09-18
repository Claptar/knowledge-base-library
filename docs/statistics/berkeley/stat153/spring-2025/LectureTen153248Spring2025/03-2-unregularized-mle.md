---
title: 2 (Unregularized) MLE
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTen153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 (Unregularized) MLE

Since (1) is a linear regression model, we can estimate the coefficients in the usual way by the MLE, or equivalently, least squares by minimizing
$$\sum_{t=1}^n (y_t - \beta_0 - \beta_1(t - 1) - \beta_2\text{ReLU}(t - 2) - \dots - \beta_{n-1}\text{ReLU}(t - (n - 1)))^2$$
over all $\beta_0, \dots, \beta_{n-1}$. The smallest value achievable in the above minimization will be the RSS. The MLE of $\sigma$ is then given by
$$\hat{\sigma}_{\text{MLE}} = \sqrt{\frac{RSS}{n}}.$$
Since there are as many coefficients as there are data points, this approach will give a perfect fit to the data leading to $RSS = 0$. In fact, from the work done in the previous section, the values of $\beta_0, \dots, \beta_{n-1}$ which minimize the sum of squares are given by:
$$\beta_0 = y_1 \quad \beta_1 = y_2 - y_1 \quad \beta_j = (y_{j+1} - y_j) - (y_j - y_{j-1})$$
for $j = 2, \dots, n - 1$. This will lead to the estimated trend function $\mu_t = y_t$ for all $t$. Also the MLE of $\sigma$ will be zero. The unbiased estimate of $\sigma$ (that we previousy used in linear regression) will not exist because it will equal $\sqrt{RSS/(n - p)}$ with $p = n$.

To summarize, these estimates will overfit the data, and will not produce a trend estimate that is simpler than the observed data.

---

[← 1 Parameter Interpretation in (1)](02-1-parameter-interpretation-in-1.md) · [Up: contents](index.md) · [3 Regularization →](04-3-regularization.md)
