---
title: 3 Uncertainty Quantification for $c, \beta0, \beta1, \beta2, \sigma$
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureNine153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureNine153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Uncertainty Quantification for $c, \beta0, \beta1, \beta2, \sigma$

For this, we use Bayesian analysis. Our prior for $\beta_0, \beta_1, \beta_2, \sigma$ is the same as the one used for linear regression:
$$\beta_0, \beta_1, \beta_2, \log \sigma \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C)$$
for a large $C$.

For the parameter $c$, we also use a uniform prior. The range of values of $c$ is $1, 2, \dots, n$. But actually there is no reason to allow $c = 1$ and $c = n$ as explained below.

When $c = 1$, the variable $\text{ReLU}(t - c)$ simply becomes $t - c = t - 1$ so that the nonlinear term $\text{ReLU}(t - c)$ can be absorbed with the other terms as:
$$\beta_0 + \beta_1 t + \beta_2 \text{ReLU}(t - 1) = \beta_0 + \beta_1 t + \beta_2 (t - 1) = (\beta_0 - \beta_2) + (\beta_1 + \beta_2)t.$$
In other words, when $c = 1$, the model reverts to the simple linear trend model (it is no longer a broken stick regression model). On the other hand, when $c = n$, we simply have $\text{ReLU}(t - c) = 0$ (because $t = 1, \dots, n$ is always smaller than $n$) so the term $\text{ReLU}(t - c)$ has no effect when $c = n$.

Our range of values is therefore $c = 2, \dots, n$. The prior for $c$ will be taken to be
$$c \sim \text{uniform}\{2, \dots, n - 1\}.$$
With these priors, calculate the posterior distributions, exactly as in the case of the sinusoidal model. This leads to the following. The posterior distribution of $c$ is:
$$\pi(c \mid \text{data}) \propto \left(\frac{1}{RSS(c)}\right)^{(n-3)/2} |X_c^T X_c|^{-1/2} I\{c = 2, \dots, n - 1\}.$$

In other words, this is a discrete distribution with pmf:
$$\pi(c \mid \text{data}) = \frac{\left(\frac{1}{RSS(c)}\right)^{(n-3)/2} |X_c^T X_c|^{-1/2}}{\sum_{c=2}^{n-1} \left(\frac{1}{RSS(c)}\right)^{(n-3)/2} |X_c^T X_c|^{-1/2}} \quad \text{for } c = 2, \dots, n - 1.$$
The denominator above is simply the sum of the numerator values for all $c = 2, \dots, n - 1$. In particular, the denominator does not depend on the particular value of $c$ anymore and is a constant. We can also write:
$$\pi(c \mid \text{data}) = \frac{\left(\frac{1}{RSS(c)}\right)^{(n-3)/2} |X_c^T X_c|^{-1/2}}{\left(\frac{1}{RSS(2)}\right)^{(n-3)/2} |X_2^T X_2|^{-1/2} + \dots + \left(\frac{1}{RSS(n-1)}\right)^{(n-3)/2} |X_{n-1}^T X_{n-1}|^{-1/2}}$$
for $c = 2, \dots, n - 1$.

Given $c$, as remarked before, the model is just a linear regression model with $X$-matrix given by $X_c$. Therefore, by results from linear regression (see Problem 4 in Homework 1), the posterior density of $\sigma$ given the data as well as $c$ is characterized by:
$$\frac{RSS(c)}{\sigma^2} \Bigm| \text{data}, c \sim \chi_{n-3}^2.$$
Finally, the posterior distribution of $\beta$ given the data as well as $c$ and $\sigma$ is
$$\beta \mid \text{data}, c, \sigma \sim N_3\left(\hat{\beta}_c, \sigma^2 (X_c^T X_c)^{-1}\right),$$
where
$$\hat{\beta}_c := (X_c^T X_c)^{-1} X_c^T y.$$

---

[← 1 Change of Slope Model](01-1-change-of-slope-model.md) · [Up: contents](index.md) · [4 Posterior Sampling for Uncertainty Quantification →](03-4-posterior-sampling-for-uncertainty-quantification.md)
