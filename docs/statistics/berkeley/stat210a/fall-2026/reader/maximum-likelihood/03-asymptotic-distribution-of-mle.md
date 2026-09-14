---
title: Asymptotic Distribution of MLE
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/maximum-likelihood.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/maximum-likelihood.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Asymptotic Distribution of MLE

**Source:** [`reader/maximum-likelihood.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/maximum-likelihood.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Under mild conditions, $\hat{\theta}_n$ is asymptotically Gaussian efficient

We will be interested in $\ell_n(\theta; X)$ as a function of $\theta$
Notate true value as $\theta_0$: $X \sim P_{\theta_0}$

Derivatives of $\ell_n$ at $\theta_0$: $S_0$, $S_1$

$S_n(\theta_0; X) = \sum_{i=1}^n \nabla \ell_i(\theta_0; X_i) \sim N(0, J_n(\theta_0))$

$\mathbb{E}[S_n(\theta; X)] = n\mathbb{E}[\nabla \ell_i(\theta_0; X_i)] = 0$

$\mathbb{E}[-\nabla^2 \ell_n(\theta; X)] = \mathbb{E}[\sum_{i=1}^n -\nabla^2 \ell_i(\theta_0; X_i)] = J_n(\theta_0)$

### Informal Proof

Taylor expansion between $\theta_0$, $\hat{\theta}_n$:

$S_n(\hat{\theta}_n; X) = S_n(\theta_0; X) + S_n'(\theta_0; X)(\hat{\theta}_n - \theta_0)$

$\sqrt{n}(\hat{\theta}_n - \theta_0) = J_n^{-1}(\theta_0) S_n(\theta_0; X)/\sqrt{n}$

$\xrightarrow{d} N(0, J_1^{-1}(\theta_0))$

More rigorous proof later, but note we need consistency of $\hat{\theta}_n$ first to even justify Taylor expansion

### Quadratic Approximation

Quadratic approximation near $\theta_0$:

$\ell_n(\theta) \approx \ell_n(\theta_0) + (\theta - \theta_0)^T S_n(\theta_0) - \frac{1}{2}(\theta - \theta_0)^T J_n(\theta_0)(\theta - \theta_0)$

$N(J_n^{-1}(\theta_0)S_n(\theta_0), J_n^{-1}(\theta_0))$

Gaussian linear term + Deterministic curvature

$\ell_n(\theta) - \ell_n(\theta_0) \approx -\frac{n}{2}(\theta - \hat{\theta}_n)^T J_1(\theta_0)(\theta - \hat{\theta}_n) + \text{const}$

---

[← Asymptotic Efficiency](02-asymptotic-efficiency.md) · [Up: contents](index.md) · [Consistency of MLE →](04-consistency-of-mle.md)
