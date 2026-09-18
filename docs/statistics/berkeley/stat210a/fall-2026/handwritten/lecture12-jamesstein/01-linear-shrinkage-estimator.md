---
title: Linear shrinkage estimator
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture12-jamesstein.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture12-jamesstein.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture12-jamesstein.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture12-jamesstein.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Linear shrinkage estimator

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

Ex. $X_1, \dots, X_n \overset{iid}{\sim} (\theta, \sigma^2 I_d)$

$$\Rightarrow \quad \bar{Z} = \frac{1}{\sigma \sqrt{n}} \sum_{k=1}^n X_k \approx N_d\left(\frac{\theta \sqrt{n}}{\sigma}, I_d\right)$$

**Estimators**

$\delta_0(X) = X$ has much to recommend it
* UMVU
* MLE
* Objective Bayes (flat or Jeffreys prior)

---

$$\delta_\zeta(X) = (1 - \zeta) X$$

Arises from Bayes:

Simple Bayes:
$$\theta_i \overset{iid}{\sim} N(0, \tau^2)$$
$$\Rightarrow \text{use } \zeta = \frac{1}{1 + \tau^2}$$

Hierarchical Bayes:
$$\tau^2 \sim \lambda_0$$
$$\theta_i \mid \tau^2 \overset{iid}{\sim} N(0, \tau^2)$$
$$\Rightarrow \text{use } \zeta = \mathbb{E}\left[\frac{1}{1 + \tau^2} \mid X\right] = \hat{\zeta}_{\text{Bayes}}(X)$$

Empirical Bayes:
Estimate $\zeta$ (est. $\tau^2$), plug in as if known

$$X \mid \tau^2 \overset{iid}{\sim} N(0, 1 + \tau^2)$$

$$\overset{(\text{suff.})}{\implies} \|X\|^2 \sim (1 + \tau^2) \chi_d^2$$

Options:
$$\hat{\zeta}_{\text{MLE}}(X) = d / \|X\|^2$$
$$\hat{\zeta}_{\text{UMVU}}(X) = \frac{d-2}{\|X\|^2}$$
$$\left(\text{since } \mathbb{E}[1/Y] = \frac{1}{d-2} \text{ for } Y \sim \chi_d^2\right)$$

---

**Lemma** If $Y \sim \chi_d^2$, $\mathbb{E}[1/Y] = \frac{1}{d-2}$

**Proof:**

$$\mathbb{E}\left[\frac{1}{Y}\right] = \int_0^\infty \frac{1}{y} \frac{1}{2^{d/2}\Gamma(\frac{d}{2})} \cdot y^{\frac{d}{2}-1} e^{-y/2} \, dy$$

$$= \frac{2^{\frac{(d-2)}{2}}\Gamma(\frac{d-2}{2})}{2^{d/2}\Gamma(\frac{d}{2})} \int_0^\infty \underbrace{\frac{1}{2^{\frac{(d-2)}{2}}\Gamma(\frac{d-2}{2})} y^{\frac{(d-2)}{2}-1} e^{-y/2}}_{\chi_{d-2}^2\text{ density}} \, dy$$

use $\Gamma(x) = (x-1)\Gamma(x-1)$
$\Gamma(x)$ is analytic ext. of $\Gamma(n) = (n-1)!$ for $n \in \mathbb{Z}$

$$= \frac{1}{2} \cdot \frac{1}{(d-2)/2}$$

$$= \frac{1}{d-2} \quad \boxtimes$$

**UMVU estimator for $\zeta$:**

$$\zeta \|X\|^2 \sim \chi_d^2 \implies \zeta^{-1} \mathbb{E}_\zeta\left[\frac{1}{\|X\|^2}\right] = \frac{1}{d-2}$$
$$\implies \hat{\zeta} = \frac{d-2}{\|X\|^2}$$

James & Stein proposed instead ($d \ge 3$):

$$\delta_{\text{JS}, i}(X) = \left(1 - \frac{d-2}{\|X\|^2}\right) X_i$$

Paradox: Better MSE than $\delta_0(X) = X$ for all $\theta \in \mathbb{R}^d$

---

## James-Stein Paradox

Back to non-Bayesian Gaussian seq. model:
$$X_i \overset{iid}{\sim} N_d(\theta, \sigma^2 I_d), \quad \theta \in \mathbb{R}^d \text{ (fixed)}, \quad \sigma^2 > 0 \text{ known}$$
$$i = 1, \dots, n$$

Shocking result of James & Stein (1956):

For $d \ge 3$, the sample mean $\bar{X} = \frac{1}{n}\sum X_i$ is **inadmissible** as an estimator of $\theta$ under squared error loss:

For $\delta_{\text{JS}}(\bar{X}) = \left(1 - \frac{(d-2)\frac{\sigma^2}{n}}{\|\bar{X}\|^2}\right) \bar{X}$

$$\text{MSE}(\theta, \delta_{\text{JS}}) < \text{MSE}(\theta, \bar{X}) \quad \forall \theta \in \mathbb{R}^d \text{ (!!!)}$$

$\bar{X}$ is UMVU, Minimax, objective Bayes, ....

Note: Might as well take $n=1$ (Suff. reduction) $\Rightarrow (1 - \frac{d-2}{\|X\|^2})X$

Note this result holds **without** assumption of Bayes model on $\theta$: true for $\theta = (500, -10^{10}, 4)$

Nothing special about 0: for any $\theta_0 \in \mathbb{R}^d$

$$\delta(X) = \theta_0 + \left(1 - \frac{d-2}{\|X - \theta_0\|^2}\right)(X - \theta_0)$$

also dominates $X$

Deep implication: shrinkage makes sense even without Bayes justification.

---

## Linear shrinkage w/o Bayesian assumptions

Gaussian seq. model: $X \sim N_d(\theta, I_d)$, fixed $\theta \in \mathbb{R}^d$

Let $\delta_\zeta(X) = (1-\zeta)X$, $\zeta$ is tuning parameter

$$\begin{aligned}
\underset{\substack{\uparrow \\ (\text{MSE})}}{R(\theta; \delta_\zeta)} &= \|\theta - \mathbb{E}\delta_\zeta(X)\|^2 + \sum_i \text{Var}((1-\zeta)X_i) \\
&= \underbrace{\zeta^2 \|\theta\|^2}_{\text{bias}^2} + \underbrace{d(1-\zeta)^2}_{\text{variance}}
\end{aligned}$$

What is optimal $\zeta$?

$$\frac{d}{d\zeta} R(\theta; \delta_\zeta) = 2\zeta \|\theta\|^2 - 2(1-\zeta)d$$

$$\implies \text{minimizer } = \zeta^*(\theta) = \frac{d}{d + \|\theta\|^2} = \frac{1}{1 + \|\theta\|^2/d}$$

$\zeta^*$ always $> 0$, but $\to 0$ as $\theta \to \infty$

What if we estimate $\zeta^*(\theta)$?

How does adaptivity of $\hat{\zeta}^*(X)$ affect MSE?

---

---

[Up: contents](index.md) · [Stein's Lemma →](02-stein-s-lemma.md)
