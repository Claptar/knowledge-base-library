---
title: Stein's Lemma
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture12-jamesstein.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture12-jamesstein.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture12-jamesstein.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture12-jamesstein.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Stein's Lemma

Useful tool for computing / estimating risk in Gaussian estimation problems

**Theorem (Stein's Lemma, univariate):**

Suppose $X \sim N(\theta, \sigma^2)$

$h(x): \mathbb{R} \to \mathbb{R}$ differentiable, $\mathbb{E}|h'(x)| < \infty$

Then $\mathbb{E}[(X - \theta)h(X)] = \sigma^2 \mathbb{E}[h'(X)]$

$$\overset{\parallel}{\text{Cov}(X, h(X))}$$

**Proof** Note we can assume wlog $h(0) = 0$ (why?)

First assume $\theta = 0$, $\sigma^2 = 1$:

Note $\mathbb{E}[X h(X)] = \int_0^\infty x h(x)\phi(x)\,dx + \int_{-\infty}^0 x h(x)\phi(x)\,dx$

$$\begin{aligned}
\int_0^\infty x h(x)\phi(x)\,dx &= \int_0^\infty x \left[\int_0^x h'(y)\,dy\right] \phi(x)\,dx \\
&= \int_0^\infty \int_0^\infty \mathbf{1}_{\{y < x\}} x\, h'(y)\phi(x)\,dx\,dy \\
&= \int_0^\infty h'(y) \left[\int_y^\infty x\phi(x)\,dx\right] dy \\
&= \int_0^\infty h'(y)\phi(y)\,dy
\end{aligned}$$

---

In the last step we have used:

$$\frac{d}{dx} \left[\frac{1}{\sqrt{2\pi}} e^{-x^2/2}\right] = -x \cdot \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$$

Similar argument shows $\int_{-\infty}^0 x h(x)\phi(x)\,dx = \int_{-\infty}^0 h'(x)\phi(x)\,dx$

$\implies$ Result holds for $\theta = 0$, $\sigma^2 = 1$

General $\theta$, $\sigma^2$:

write $X = \theta + \sigma Z$, $Z \sim N(0, 1)$

$$\begin{aligned}
\mathbb{E}[(X - \theta)h(X)] &= \sigma \mathbb{E}[Z h(\theta + \sigma Z)] \\
&= \sigma^2 \mathbb{E}[h'(\theta + \sigma Z)] \\
&= \sigma^2 \mathbb{E}[h'(X)]
\end{aligned}$$

---

## Multivariate Stein's Lemma

**Def** $h: \mathbb{R}^d \to \mathbb{R}^d$, $Dh \in \mathbb{R}^{d \times d}$

$$(Dh(x))_{ij} = \frac{\partial h_i}{\partial x_j}(x)$$

**Def (Frobenius norm):** $A \in \mathbb{R}^{d \times d}$

$$\|A\|_F = \left(\sum_{i,j} A_{ij}^2\right)^{1/2}$$

**Theorem (Stein's Lemma, Multivariate):**

$$X \sim N_d(\theta, \sigma^2 I_d) \quad \theta \in \mathbb{R}^d$$

$h: \mathbb{R}^d \to \mathbb{R}^d \quad \text{diffable}, \quad \mathbb{E}\|Dh(x)\|_F < \infty$

Then $\mathbb{E}[(X - \theta)' h(X)] = \sigma^2 \mathbb{E}\operatorname{tr}(Dh(X))$

$$= \sigma^2 \sum_i \mathbb{E}\frac{\partial h_i}{\partial x_i}(X)$$

**Proof**

$$\begin{aligned}
\mathbb{E}[(X_i - \theta_i)h_i(X)] &= \mathbb{E}\left[\mathbb{E}\left[(X_i - \theta_i)h_i(X) \mid X_{-i}\right]\right] \\
&= \mathbb{E}\left[\mathbb{E}\left[\sigma^2 \frac{\partial h_i}{\partial x_i}(X) \mid X_{-i}\right]\right] \\
&= \sigma^2 \mathbb{E}\frac{\partial h_i}{\partial x_i}(X) \quad \boxtimes
\end{aligned}$$

---

## Stein's Unbiased Risk Estimator (SURE)

Can use Stein's Lemma to get unbiased estimator of the MSE of any $\delta(X)$:

apply Stein's Lemma with $h(X) = X - \delta(X)$

Assume $\sigma^2 = 1$:

\$\$\begin{aligned}
R(\theta; \delta) &= \mathbb{E}_\theta \left[\|X - \theta - h(X)\|^2\right] \\
&= \mathbb{E}_\theta \|X - \theta\|^2 + \mathbb{E}_\theta \|h(X)\|^2 - 2\mathbb{E}_\theta

---

[← Linear shrinkage estimator](01-linear-shrinkage-estimator.md) · [Up: contents](index.md)
