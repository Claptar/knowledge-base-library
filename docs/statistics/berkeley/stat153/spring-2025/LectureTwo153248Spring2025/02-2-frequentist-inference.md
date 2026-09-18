---
title: 2 Frequentist Inference
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwo153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwo153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwo153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwo153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Frequentist Inference

Frequentist inference is most commonly done via Maximum Likelihood Estimators. The MLEs for $\beta_0, \beta_1, \sigma$ are obtained by maximizing the likelihood. From the expression (1) for the likelihood, the following is a natural strategy for maximizing it: (a) first maximize over $\beta_0, \beta_1$ for fixed $\sigma$. This is equivalent to minimizing $S(\beta_0, \beta_1)$ and will lead to the MLEs $\hat{\beta}_0$ and $\hat{\beta}_1$. (b) Plug in the values $\beta_0 = \hat{\beta}_0$ and $\beta_1 = \hat{\beta}_1$ in (1) and then maximize over $\sigma$.

$\hat{\beta}_0$ and $\hat{\beta}_1$ are therefore given by the minimizers of $S(\beta_0, \beta_1)$. It is left as an exercise to verify that
$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x} \quad \text{and} \quad \hat{\beta}_1 = \frac{\sum_{i=1}^n (y_i - \bar{y})(x_i - \bar{x})}{\sum_{i=1}^n (x_i - \bar{x})^2},
$$
where
$$
\bar{y} = \frac{y_1 + \dots + y_n}{n} \quad \text{and} \quad \bar{x} = \frac{x_1 + \dots + x_n}{n}.
$$
To get the MLE for $\sigma$, we need to maximize
$$
(2\pi)^{-n/2}\sigma^{-n}\exp\left(-\frac{S(\hat{\beta}_0, \hat{\beta}_1)}{2\sigma^2}\right).
$$
It is left as an exercise to show that
$$
\hat{\sigma}_{\text{MLE}} = \sqrt{\frac{S(\hat{\beta}_0, \hat{\beta}_1)}{n}}.
$$
The quantities $\hat{\beta}_0, \hat{\beta}_1, \hat{\sigma}$ provide point estimates of the unknown parameters $\beta_0, \beta_1$ and $\sigma$. More work is needed for uncertainty quantification. For this, one attempts to deduce the distribution of $\hat{\beta}_0, \hat{\beta}_1, \hat{\sigma}$. This can be done in closed form. As an example, for $\hat{\beta}_1$, we have
$$
\hat{\beta}_1 = \frac{\sum_{i=1}^n (y_i - \bar{y})(x_i - \bar{x})}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{\sum_{i=1}^n y_i(x_i - \bar{x})}{\sum_{i=1}^n (x_i - \bar{x})^2} \sim N\left(\beta_1, \frac{\sigma^2}{\sum_{i=1}^n (x_i - \bar{x})^2}\right).
$$
One can also check that, jointly, $\hat{\beta}_0$ and $\hat{\beta}_1$ have the following bivariate normal distribution:
$$
\begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{pmatrix} \sim N\left(\begin{pmatrix} \beta_0 \\ \beta_1 \end{pmatrix}, \frac{\sigma^2}{n \sum_{i=1}^n (x_i - \bar{x})^2}\begin{pmatrix} \sum_i x_i^2 & -\sum_i x_i \\ -\sum_i x_i & n \end{pmatrix}\right)
$$

These formulae are easier to deduce if we use matrix notation (which we shall do when we look at multiple linear regression next week). The distribution of $\hat{\sigma}_{\text{MLE}}$ is given by:
$$
\frac{n\hat{\sigma}^2_{\text{MLE}}}{\sigma^2} \sim \chi^2_{n-2}
$$
where $\chi^2_{n-2}$ denotes the chi-squared distribution with $n - 2$ degrees of freedom. The mean of the chi-squared distribution equals its degrees of freedom which implies that
$$
\mathbb{E}\hat{\sigma}^2_{\text{MLE}} = \sigma^2 \frac{n - 2}{n}.
$$
Therefore the MLE for $\sigma^2$ is not unbiased (in contrast, the MLEs $\hat{\beta}_0$ and $\hat{\beta}_1$ are unbiased). It is easy to correct the bias leading to the following unbiased estimator of $\sigma^2$:
$$
\hat{\sigma}^2_{\text{unbiased}} = \frac{n}{n - 2}\hat{\sigma}^2_{\text{MLE}} = \frac{S(\hat{\beta}_0, \hat{\beta}_1)}{n - 2}.
$$
Usage of $\hat{\sigma}_{\text{unbiased}}$ is much more common than that of $\hat{\sigma}_{\text{MLE}}$ (note that $\hat{\sigma}_{\text{unbiased}}$ is not unbiased for $\sigma$; rather the square of $\hat{\sigma}_{\text{unbiased}}$ is unbiased for $\sigma^2$).

Another important fact is that $(\hat{\beta}_0, \hat{\beta}_1)$ and $\hat{\sigma}^2_{\text{unbiased}}$ are independent.

These facts are used to derive the following confidence interval for $\beta_1$:
$$
\left[\hat{\beta}_1 - \frac{\hat{\sigma}_{\text{unbiased}}}{\sqrt{\sum_i (x_i - \bar{x})^2}} t_{n-2, \alpha/2}, \, \hat{\beta}_1 + \frac{\hat{\sigma}_{\text{unbiased}}}{\sqrt{\sum_i (x_i - \bar{x})^2}} t_{n-2, \alpha/2}\right]
\tag{2}
$$
where $t_{n-2, \alpha/2}$ is the positive point such that $\mathbb{P}\{t_{n-2} \ge t_{n-2, \alpha/2}\} = \alpha/2$ (i.e., the $t$-distribution with $n - 2$ degrees of freedom assigns probability mass $\alpha/2$ to the right of $t_{n-2, \alpha/2}$). (2) is a valid confidence interval because:
$$
\frac{\hat{\beta}_1 - \beta_1}{\sigma} \sqrt{\sum_i (x_i - \bar{x})^2} \sim N(0, 1) \quad \text{and} \quad \frac{\hat{\beta}_1 - \beta_1}{\hat{\sigma}} \sqrt{\sum_i (x_i - \bar{x})^2} \sim t_{n-2}
$$
where $t_{n-2}$ is the $t$-distribution with $n - 2$ degrees of freedom.

---

[← 1 Simple Linear Regression](01-1-simple-linear-regression.md) · [Up: contents](index.md) · [3 Bayesian Inference →](03-3-bayesian-inference.md)
