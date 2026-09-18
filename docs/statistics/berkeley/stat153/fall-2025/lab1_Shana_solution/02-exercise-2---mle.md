---
title: Exercise 2 - MLE
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/lab1_Shana_solution.pdf
source_file: sources/berkeley-stat153/fall-2025/lab1_Shana_solution.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`lab1_Shana_solution.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/lab1_Shana_solution.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Exercise 2 - MLE

Given data $y_1, \dots, y_n$, consider the model $y_i \overset{\text{i.i.d.}}{\sim} \mathcal{N}(\mu, \sigma^2)$ for two unknown parameters $\mu$ and $\sigma > 0$.

Find the maximum likelihood estimators (MLEs) of $\mu$ and $\sigma$ by maximizing the log-likelihood (use first-order derivatives).

**Requirement.** Show that the solution is the unique interior maximizer by arguing concavity of the log-likelihood OR by showing a sign change of the derivative and checking boundary behavior.

*Proof.* 1) **Likelihood and log-likelihood.** The likelihood is

$$L(\mu, \sigma) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left\{-\frac{(y_i - \mu)^2}{2\sigma^2}\right\} = (2\pi\sigma^2)^{-n/2} \exp\left\{-\frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - \mu)^2\right\}.$$

Hence the log-likelihood is

$$\ell(\mu, \sigma) = -\frac{n}{2}\log(2\pi) - n\log\sigma - \frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - \mu)^2.$$

2) **Maximize in $\mu$ for fixed $\sigma$.** Differentiate w.r.t. $\mu$:

$$\frac{\partial \ell}{\partial \mu} = \frac{1}{\sigma^2} \sum_{i=1}^n (y_i - \mu) = \frac{n}{\sigma^2}(\bar{y} - \mu), \quad \frac{\partial^2 \ell}{\partial \mu^2} = -\frac{n}{\sigma^2} < 0.$$

Setting the first derivative to zero yields

$$\hat{\mu} = \bar{y} = \frac{1}{n} \sum_{i=1}^n y_i.$$

Since $\partial^2 \ell / \partial \mu^2 < 0$, $\ell(\mu, \sigma)$ is strictly concave down in $\mu$ (for fixed $\sigma$), so $\hat{\mu}$ is the unique maximizer in $\mu$. Equivalently, maximizing $\ell$ in $\mu$ is the same as minimizing $\sum_{i=1}^n (y_i - \mu)^2$, a strictly convex (concave up) quadratic in $\mu$ with unique minimizer $\bar{y}$.

3) **Maximize in $\sigma$ for $\mu = \bar{y}$.** Let $S = \sum_{i=1}^n (y_i - \bar{y})^2$. The profile log-likelihood is

$$\ell(\bar{y}, \sigma) = -\frac{n}{2}\log(2\pi) - n\log\sigma - \frac{S}{2\sigma^2}, \quad \sigma > 0.$$

Differentiate w.r.t. $\sigma$:

$$\frac{d\ell(\bar{y}, \sigma)}{d\sigma} = -\frac{n}{\sigma} + \frac{S}{\sigma^3} = \frac{S - n\sigma^2}{\sigma^3}.$$

Set to zero:

$$S - n\sigma^2 = 0 \implies \hat{\sigma}^2 = \frac{S}{n}, \quad \hat{\sigma} = \sqrt{\frac{S}{n}}.$$

*Uniqueness and interiority.*
As $\sigma \to 0^+$, $\ell(\bar{y}, \sigma) \to -\infty$ and as $\sigma \to \infty$, $\ell(\bar{y}, \sigma) \to -\infty$. Moreover,

$$\frac{d\ell}{d\sigma} = \frac{S - n\sigma^2}{\sigma^3} \begin{cases} > 0, & \sigma < \sqrt{S/n} = \hat{\sigma} \\ < 0, & \sigma > \sqrt{S/n} = \hat{\sigma} \end{cases}$$

so the log-likelihood increases on $(0, \hat{\sigma})$ and decreases on $(\hat{\sigma}, \infty)$. Therefore $\hat{\sigma}$ is the *unique interior maximizer* over $\sigma > 0$.

**Conclusion.** The MLEs are

$$\boxed{\hat{\mu} = \bar{y}, \quad \hat{\sigma}^2 = \frac{1}{n}\sum_{i=1}^n (y_i - \bar{y})^2, \quad \hat{\sigma} = \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i - \bar{y})^2}}$$

These form the unique interior maximizer of the log-likelihood over $\mu \in \mathbb{R}$, $\sigma > 0$.

---

[← Exercise 1 - Change of Variables](01-exercise-1---change-of-variables.md) · [Up: contents](index.md)
