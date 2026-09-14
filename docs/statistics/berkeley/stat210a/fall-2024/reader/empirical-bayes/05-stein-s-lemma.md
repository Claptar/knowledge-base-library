---
title: Stein's Lemma
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/empirical-bayes.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/empirical-bayes.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Stein's Lemma

**Source:** [`reader/empirical-bayes.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/empirical-bayes.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Useful tool for computing/estimating risk in Gaussian estimation
problems.

### Theorem (Stein's Lemma - Univariate)

Suppose $X \sim N(\theta, \sigma^2)$ $h: \mathbb{R} → \mathbb{R}$
differentiable, $\mathbb{E}|h'(X)| < \infty$

Then $\mathbb{E}[(X-\theta)h(X)] = \sigma^2\mathbb{E}[h'(X)]$

$\text{Cov}(X, h(X)) = \sigma^2\mathbb{E}[h'(X)]$

Proof: Note we can assume w.l.o.g. $h(0) = 0$ (why?) First assume
$\theta = 0$, $\sigma^2 = 1$

$$\mathbb{E}[Xh(X)] = \int xh(x)\phi(x)dx = \int xh(x)\phi(x)dx - \int h(x)\phi'(x)dx = \int h'(x)\phi(x)dx$$

In the last step we have used $\phi'(x) = -x\phi(x)$

Similar argument shows $\int h(x)\phi(x)dx = \int h'(x)\phi(x)dx$

Result holds for $\theta = 0$, $\sigma^2 = 1$

General $\theta$, $\sigma^2 \neq 1$: write $X = \theta + \sigma Z$,
$Z \sim N(0,1)$

$$\mathbb{E}[(X-\theta)h(X)] = \sigma\mathbb{E}[Zh(\theta+\sigma Z)] = \sigma^2\mathbb{E}[h'(\theta+\sigma Z)] = \sigma^2\mathbb{E}[h'(X)]$$

### Multivariate Version

Define Frobenius norm:
$\|A\|_F^2 = \sum_{i,j} A_{ij}^2 = \text{tr}(A^TA)$

### Theorem (Stein's Lemma - Multivariate)

$X \sim N_d(\theta, \sigma^2 I_d)$, $\theta \in \mathbb{R}^d$
$h: \mathbb{R}^d → \mathbb{R}^d$ differentiable,
$\mathbb{E}\|Dh(X)\|_F < \infty$

Then
$\mathbb{E}[(X-\theta)^Th(X)] = \sigma^2\mathbb{E}[\text{tr}(Dh(X))]$

$\mathbb{E}[(X-\theta)h(X)^T] = \sigma^2\mathbb{E}[Dh(X)]$

Proof:

$$\mathbb{E}[(X_i-\theta_i)h_i(X)] = \mathbb{E}[\mathbb{E}[(X_i-\theta_i)h_i(X)|X_{-i}]]$$
$$= \sigma^2\mathbb{E}[\frac{\partial h_i}{\partial x_i}(X)]$$

---

[← James-Stein Estimator](04-james-stein-estimator.md) · [Up: contents](index.md) · [Stein's Unbiased Risk Estimator (SURE) →](06-stein-s-unbiased-risk-estimator-sure.md)
