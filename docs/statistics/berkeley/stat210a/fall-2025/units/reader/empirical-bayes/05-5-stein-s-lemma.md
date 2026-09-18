---
title: 5 Stein’s Lemma
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/empirical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/empirical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/empirical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/empirical-bayes.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 5 Stein’s Lemma

Useful tool for computing/estimating risk in Gaussian estimation problems.

## 5.1 Theorem (Stein’s Lemma - Univariate) {.anchored number="5.1" anchor-id="theorem-steins-lemma---univariate"}

Suppose $X \sim N(\theta, \sigma^2)$ $h: \mathbb{R} → \mathbb{R}$ differentiable, $\mathbb{E}|h'(X)| < \infty$

Then $\mathbb{E}[(X-\theta)h(X)] = \sigma^2\mathbb{E}[h'(X)]$

$\text{Cov}(X, h(X)) = \sigma^2\mathbb{E}[h'(X)]$

Proof: Note we can assume w.l.o.g. $h(0) = 0$ (why?) First assume $\theta = 0$, $\sigma^2 = 1$

$$
\mathbb{E}[Xh(X)] = \int xh(x)\phi(x)dx = \int xh(x)\phi(x)dx - \int h(x)\phi'(x)dx = \int h'(x)\phi(x)dx
$$

In the last step we have used $\phi'(x) = -x\phi(x)$

Similar argument shows $\int h(x)\phi(x)dx = \int h'(x)\phi(x)dx$

Result holds for $\theta = 0$, $\sigma^2 = 1$

General $\theta$, $\sigma^2 \neq 1$: write $X = \theta + \sigma Z$, $Z \sim N(0,1)$

$$
\mathbb{E}[(X-\theta)h(X)] = \sigma\mathbb{E}[Zh(\theta+\sigma Z)] = \sigma^2\mathbb{E}[h'(\theta+\sigma Z)] = \sigma^2\mathbb{E}[h'(X)]
$$

## 5.2 Multivariate Version {.anchored number="5.2" anchor-id="multivariate-version"}

Define Frobenius norm: $\|A\|_F^2 = \sum_{i,j} A_{ij}^2 = \text{tr}(A^TA)$

## 5.3 Theorem (Stein’s Lemma - Multivariate) {.anchored number="5.3" anchor-id="theorem-steins-lemma---multivariate"}

$X \sim N_d(\theta, \sigma^2 I_d)$, $\theta \in \mathbb{R}^d$ $h: \mathbb{R}^d → \mathbb{R}^d$ differentiable, $\mathbb{E}\|Dh(X)\|_F < \infty$

Then $\mathbb{E}[(X-\theta)^Th(X)] = \sigma^2\mathbb{E}[\text{tr}(Dh(X))]$

$\mathbb{E}[(X-\theta)h(X)^T] = \sigma^2\mathbb{E}[Dh(X)]$

Proof:

$$
\mathbb{E}[(X_i-\theta_i)h_i(X)] = \mathbb{E}[\mathbb{E}[(X_i-\theta_i)h_i(X)|X_{-i}]]
$$

$$
= \sigma^2\mathbb{E}[\frac{\partial h_i}{\partial x_i}(X)]
$$

---

[← 4 James-Stein Estimator](04-4-james-stein-estimator.md) · [Up: contents](index.md) · [6 Stein’s Unbiased Risk Estimator (SURE) →](06-6-stein-s-unbiased-risk-estimator-sure.md)
