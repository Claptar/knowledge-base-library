---
title: Empirical Bayes, James-Stein
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture12-jamesstein.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture12-jamesstein.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture12-jamesstein.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture12-jamesstein.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Empirical Bayes, James-Stein

### Outline

1) Empirical Bayes
2) James-Stein Paradox
3) Stein's Lemma
4) Stein's unbiased risk estimator (SURE)

---

## Estimators for Gaussian seq. model

**Gaussian sequence model**

$$X \sim N_d(\theta, I_d)$$

Goal: estimate $\theta \in \mathbb{R}^d$ via $\delta(X)$
with low $\text{MSE}(\theta; \delta) = \mathbb{E}_\theta \|\theta - \delta(X)\|^2$

Model more general than it might appear:

Ex. $X_1, \ldots, X_n \overset{iid}{\sim} (\theta, \sigma^2 I_d)$

$$\implies Z = \frac{1}{\sigma \sqrt{n}} \sum_{k=1}^n X_k \approx N_d(\theta, I_d)$$

**Estimators**

$\delta_0(X) = X$ has much to recommend it
- UMVU
- MLE
- Objective Bayes (flat or Jeffreys prior)

---

## Linear shrinkage estimator

$$\delta_\zeta(X) = (1 - \zeta) X$$

Arises from Bayes:

Simple Bayes:
$$\theta_i \overset{iid}{\sim} N(0, \tau^2)$$
$$\implies \text{use } \zeta = \frac{1}{1 + \tau^2}$$

Hierarchical Bayes:
$$\tau^2 \sim \lambda_0$$
$$\theta_i \mid \tau^2 \overset{iid}{\sim} N(0, \tau^2)$$
$$\implies \text{use } \zeta = \mathbb{E}\left[\frac{1}{1+\tau^2} \mid X\right] = \hat{\zeta}_{\text{Bayes}}(X)$$

Empirical Bayes:
Estimate $\zeta$ (est. $\tau^2$)

$$X \mid \tau^2 \overset{iid}{\sim} N(0, 1 + \tau^2)$$

$$\overset{(\text{Suff.})}{\leadsto} \|X\|^2 \sim (1+\tau^2)\chi_d^2$$

$$\hat{\zeta}_{\text{MLE}}(X) = d / \|X\|^2$$

$$\hat{\zeta}_{\text{UMVU}}(X) = \frac{d-2}{\|X\|^2}$$

$$\left(\text{since } \mathbb{E}[1/Y] = \frac{1}{d-2} \text{ for } Y \sim \chi_d^2\right)$$

---

**Lemma** If $Y \sim \chi_d^2$, $\mathbb{E}[1/Y] = \frac{1}{d-2}$

**Proof:**

---

---

[Up: contents](index.md) · [Empirical Bayes →](02-empirical-bayes.md)
