---
title: 3 Back to Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFive153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFive153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Back to Regression

Let us get back to

$$
\beta_0, \dots, \beta_m \mid \text{data} \sim t_{m+1} \left( \hat{\beta}, \frac{S(\hat{\beta})}{n - m - 1}(X^T X)^{-1}, n - m - 1 \right). \tag{5}
$$

The quantity $S(\hat{\beta})/(n - m - 1)$ is the frequentist unbiased estimator for $\sigma^2$, so we denote it by $\hat{\sigma}^2$:

$$
\hat{\sigma} := \sqrt{\frac{S(\hat{\beta})}{n - m - 1}}.
$$

$\hat{\sigma}$ can also be justified as a Bayesian estimator of $\sigma$ (See Question 5 (e) of Homework One). The terminology **Residual Standard Error** is sometimes used for $\hat{\sigma}$.

With the notation for $\hat{\sigma}$, the posterior (6) becomes:

$$
\beta_0, \dots, \beta_m \mid \text{data} \sim t_{m+1} \left( \hat{\beta}, \hat{\sigma}^2 (X^T X)^{-1}, n - m - 1 \right). \tag{6}
$$

By one of the facts mentioned about the $t$-distribution, the posterior of each individual $\beta_j$ is also $t$:

$$
\beta_j \mid \text{data} \sim t_1 \left( \hat{\beta}_j, \hat{\sigma}^2 (X^T X)^{j+1, j+1}, n - m - 1 \right) \tag{7}
$$

where $(X^T X)^{j+1, j+1}$ is the $(j + 1)$th diagonal entry of $(X^T X)^{-1}$ (note that we are using the $(j + 1)$th diagonal entry of $X^T X$ because $\beta_j$ is the $(j + 1)$th component of $\beta$). Writing this density out, we have

$$
f_{\beta_j \mid \text{data}}(\beta_j) \propto \left( 1 + \frac{1}{n-m-1} \frac{(\beta_j - \hat{\beta}_j)^2}{\hat{\sigma}^2(X^T X)^{j+1, j+1}} \right)^{-n/2}
$$

which implies that

$$
\frac{\beta_j - \hat{\beta}_j}{\hat{\sigma}\sqrt{(X^T X)^{j+1, j+1}}} \sim \text{univariate standard } t \text{ with } n - m - 1 \text{ d.f.}
$$

This can be used to obtain uncertainty intervals for $\beta_j$. If $t_{n-m-1, \alpha/2}$ is the point beyond which the $t$-distribution (with $n - m - 1$ degrees of freedom) assigns probability $\alpha/2$, then

$$
\mathbb{P}\left( -t_{n-m-1, \alpha/2} \le \frac{\beta_j - \hat{\beta}_j}{\hat{\sigma}\sqrt{(X^T X)^{j+1, j+1}}} \le t_{n-m-1, \alpha/2} \;\middle|\; \text{data} \right) = 1 - \alpha
$$

which is same as:

$$
\mathbb{P}\left( \hat{\beta}_j - \hat{\sigma}\sqrt{(X^T X)^{j+1, j+1}} t_{n-m-1, \alpha/2} \le \beta_j \le \hat{\beta}_j + \hat{\sigma}\sqrt{(X^T X)^{j+1, j+1}} t_{n-m-1, \alpha/2} \;\middle|\; \text{data} \right) = 1 - \alpha
$$

This interval:

$$
\left[ \hat{\beta}_j - \hat{\sigma}\sqrt{(X^T X)^{j+1, j+1}} t_{n-m-1, \alpha/2}, \; \hat{\beta}_j + \hat{\sigma}\sqrt{(X^T X)^{j+1, j+1}} t_{n-m-1, \alpha/2} \right]
$$

is called the $100(1 - \alpha)\%$ Bayesian Credible interval for $\beta_j$. It exactly coincides with the frequentist $100(1 - \alpha)\%$ confidence interval for $\beta_j$.

When $n - m - 1$ is large, the $t$-density (6) is approximately equal to the $N_{m+1}(\hat{\beta}, \hat{\sigma}^2(X^T X)^{-1})$. Further, when $n - m - 1$ is large, the distribution (7) will be close to the normal distribution $N(\hat{\beta}_j, \hat{\sigma}^2(X^T X)^{j+1, j+1})$. The quantity $\hat{\sigma}\sqrt{(X^T X)^{j+1, j+1}}$ is known as the standard error corresponding to $\beta_j$.

---

[← 2 $t$-density](02-2--density.md) · [Up: contents](index.md) · [4 Proof of (4) →](04-4-proof-of-4.md)
