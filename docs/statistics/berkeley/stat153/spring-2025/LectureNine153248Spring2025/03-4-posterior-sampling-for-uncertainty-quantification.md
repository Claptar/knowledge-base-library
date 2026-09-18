---
title: 4 Posterior Sampling for Uncertainty Quantification
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureNine153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureNine153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Posterior Sampling for Uncertainty Quantification

A useful way of visualizing the uncertainty is to draw posterior samples from the unknown parameters, and then plot the corresponding fitted values along with the observed data. The algorithm for drawing the posterior samples is as follows.

1. Obtain samples $c^{(1)}, \dots, c^{(N)}$ by sampling, with replacement, from the set of possible values of $c : \{2, \dots, n\}$ with probability weights given by the posterior pmf $\pi(c \mid \text{data})$. For this, one can use, for example, the choice function in `np.random.default_rng()`.
2. For each $j = 1, \dots, N$,
   a) Fix $c = c^{(j)}$.
   b) Calculate $RSS(c)$ and $\hat{\beta}_c$ by implementing linear regression with fixed $c$.
   c) Generate a chi-squared random variable $\chi^2$ with $n - 3$ degrees of freedom. Take $\sigma^{(j)} = \sqrt{RSS(c)/\chi^2}$.
   d) Take $\beta^{(j)}$ to be a generated random vector from the multivariate normal distribution with mean $\hat{\beta}_c$ and covariance $(\sigma^{(j)})^2 (X_c^T X_c)^{-1}$.

Suppose the posterior samples are given by $(c^{(j)}, \beta_0^{(j)}, \beta_1^{(j)}, \beta_2^{(j)}, \sigma^{(j)})$ for $j = 1, \dots, N$. The corresponding fitted values are given by:
$$t \mapsto \beta_0^{(j)} + \beta_1^{(j)} t + \beta_2^{(j)} \text{ReLU}(t - c^{(j)})$$
for $t = 1, \dots, n$. These can be plotted along with the original data.

One can also plot vertical lines corresponding to $c^{(j)}$ to visualize uncertainty in the change-of-slope time point parameter $c$.

The 95% approximate credible intervals for each parameter can be obtained by computing the 2.5th and 97.5th percentiles of the corresponding posterior samples.

Suppose you want to obtain posterior samples for $y_{t^*}$ for a future time point $t^*$. One can follow the algorithm listed above with one additional step to generate $y_{t^*}^{(j)}, j = 1, \dots, N$ as follows:

1. Obtain samples $c^{(1)}, \dots, c^{(N)}$ by sampling, with replacement, from the set of possible values of $c : \{2, \dots, n\}$ with probability weights given by the posterior pmf $\pi(c \mid \text{data})$. For this, one can use, for example, the choice function in `np.random.default_rng()`.
2. For each $j = 1, \dots, N$,
   a) Fix $c = c^{(j)}$.
   b) Calculate $RSS(c)$ and $\hat{\beta}_c$ by implementing linear regression with fixed $c$.
   c) Generate a chi-squared random variable $\chi^2$ with $n - 3$ degrees of freedom. Take $\sigma^{(j)} = \sqrt{RSS(c)/\chi^2}$.
   d) Take $\beta^{(j)}$ to be a generated random vector from the multivariate normal distribution with mean $\hat{\beta}_c$ and covariance $(\sigma^{(j)})^2 (X_c^T X_c)^{-1}$.
   e) Generate $y_{t^*}^{(j)}$ from the normal distribution with mean $\beta_0^{(j)} + \beta_1^{(j)} t^* + \beta_2^{(j)} \text{ReLU}(t^* - c^{(j)})$ and variance $(\sigma^{(j)})^2$.

---

[← 3 Uncertainty Quantification for $c, \beta0, \beta1, \beta2, \sigma$](02-3-uncertainty-quantification-for.md) · [Up: contents](index.md) · [5 More Changes of Slope →](04-5-more-changes-of-slope.md)
