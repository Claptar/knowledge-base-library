---
title: 2 Estimation of $\beta0$ and $\beta1$
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwo153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwo153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwo153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwo153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Estimation of $\beta0$ and $\beta1$

## 2.1 Least Squares Estimates

The estimates of $\beta_0$ and $\beta_1$ reported by standard libraries (such as `statsmodels`) are obtained using the method of least squares. This involves minimizing the sum of squares criterion:

$$
S(\beta_0, \beta_1) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2 \tag{3}
$$

over all values of $\beta_0$ and $\beta_1$. It is left as an exercise to verify that:

$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x} \quad \text{and} \quad \hat{\beta}_1 = \frac{\sum_{i=1}^n (y_i - \bar{y})(x_i - \bar{x})}{\sum_{i=1}^n (x_i - \bar{x})^2},
$$

where

$$
\bar{y} = \frac{y_1 + \dots + y_n}{n} \quad \text{and} \quad \bar{x} = \frac{x_1 + \dots + x_n}{n}.
$$

## 2.2 MLE under Normality of Errors

Suppose we assume that the error terms $\epsilon_1, \dots, \epsilon_n$ in (2) are i.i.d normal with mean zero and some variance $\sigma^2$:

$$
\epsilon_1, \dots, \epsilon_n \overset{\text{i.i.d}}{\sim} N(0, \sigma^2). \tag{4}
$$

Then the least squares estimates of $\beta_0$ and $\beta_1$ coincide with the Maximum Likelihood Estimates (MLEs).

Another way of writing the model (2) and (4) is:

$$
y_i \overset{\text{independent}}{\sim} N(\beta_0 + \beta_1 x_i, \sigma^2).
$$

To obtain the MLEs of the parameters ($\beta_0, \beta_1$ as well as $\sigma$), we need to write the likelihood function and then maximize it. The likelihood function is the joint density of the data for fixed values of the parameters $\beta_0, \beta_1, \sigma$:

\$\$
\begin{aligned}
f_{y_1, \dots, y_n \mid \beta_0, \beta_1, \sigma}(y_1, \dots, y_n) &= \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left(-\frac{(y_i - \beta_0 - \beta_1 x_i)^2}{2\sigma^2}\right) \\
&= (2\pi)^{-n/2}\sigma^{-n} \exp\left(-\frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2\right) \\
&= (2\pi)^{-n/2}\sigma^{-n} \exp\left(-\frac{S(\beta_0, \beta_1)}{2\sigma^2}\right) \tag{5

---

[← 1 Simple Linear Regression](01-1-simple-linear-regression.md) · [Up: contents](index.md)
