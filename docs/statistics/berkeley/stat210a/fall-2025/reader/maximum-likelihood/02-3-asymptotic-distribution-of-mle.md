---
title: 3 Asymptotic Distribution of MLE
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/maximum-likelihood.html
source_file: sources/berkeley-stat210a/fall-2025/reader/maximum-likelihood.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/maximum-likelihood.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/maximum-likelihood.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 3 Asymptotic Distribution of MLE

Under mild conditions, $\hat{\theta}_n$ is asymptotically Gaussian efficient

We will be interested in $\ell_n(\theta; X)$ as a function of $\theta$ Notate true value as $\theta_0$: $X \sim P_{\theta_0}$

Derivatives of $\ell_n$ at $\theta_0$: $S_0$, $S_1$

$S_n(\theta_0; X) = \sum_{i=1}^n \nabla \ell_i(\theta_0; X_i) \sim N(0, J_n(\theta_0))$

$\mathbb{E}[S_n(\theta; X)] = n\mathbb{E}[\nabla \ell_i(\theta_0; X_i)] = 0$

$\mathbb{E}[-\nabla^2 \ell_n(\theta; X)] = \mathbb{E}[\sum_{i=1}^n -\nabla^2 \ell_i(\theta_0; X_i)] = J_n(\theta_0)$

## 3.1 Informal Proof {.anchored number="3.1" anchor-id="informal-proof"}

Taylor expansion between $\theta_0$, $\hat{\theta}_n$:

$S_n(\hat{\theta}_n; X) = S_n(\theta_0; X) + S_n'(\theta_0; X)(\hat{\theta}_n - \theta_0)$

$\sqrt{n}(\hat{\theta}_n - \theta_0) = J_n^{-1}(\theta_0) S_n(\theta_0; X)/\sqrt{n}$

$\xrightarrow{d} N(0, J_1^{-1}(\theta_0))$

More rigorous proof later, but note we need consistency of $\hat{\theta}_n$ first to even justify Taylor expansion

## 3.2 Quadratic Approximation {.anchored number="3.2" anchor-id="quadratic-approximation"}

Quadratic approximation near $\theta_0$:

$\ell_n(\theta) \approx \ell_n(\theta_0) + (\theta - \theta_0)^T S_n(\theta_0) - \frac{1}{2}(\theta - \theta_0)^T J_n(\theta_0)(\theta - \theta_0)$

$N(J_n^{-1}(\theta_0)S_n(\theta_0), J_n^{-1}(\theta_0))$

Gaussian linear term + Deterministic curvature

$\ell_n(\theta) - \ell_n(\theta_0) \approx -\frac{n}{2}(\theta - \hat{\theta}_n)^T J_1(\theta_0)(\theta - \hat{\theta}_n) + \text{const}$

---

[← 1 Maximum Likelihood Estimation](01-1-maximum-likelihood-estimation.md) · [Up: contents](index.md) · [4 Consistency of MLE →](03-4-consistency-of-mle.md)
