---
title: Gaussian Hierarchical Model
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture10-bayesinterp.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture10-bayesinterp.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture10-bayesinterp.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture10-bayesinterp.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Gaussian Hierarchical Model

$$
\begin{aligned}
\tau^2 &\sim \lambda_0 \\
\theta_i \mid \tau^2 &\overset{\text{iid}}{\sim} N(0, \tau^2) \qquad i \le d \\
X_i \mid \tau^2, \theta &\overset{\text{ind.}}{\sim} N(\theta_i, 1)
\end{aligned}
$$

**Posterior mean:**

$$
\begin{aligned}
\delta(X_i) &= \mathbb{E}[\theta_i \mid X] \\
&= \mathbb{E}\left[ \mathbb{E}[\theta_i \mid X, \tau^2] \mid X \right] \\
&= \mathbb{E}\left[ \frac{\tau^2}{1+\tau^2} X_i \;\middle|\; X \right] \\
&= \mathbb{E}\left[ \frac{\tau^2}{1+\tau^2} \;\middle|\; X \right] \cdot X_i
\end{aligned}
$$

**Linear shrinkage estimator**,
Bayes-optimal shrinkage estimated from data

Likelihood for $\tau^2$: marginalize over $\theta_i$

$$
\begin{aligned}
X_i \mid \tau^2 &\sim N(0, 1+\tau^2) \\
\Rightarrow \frac{1}{d} \|X\|^2 &\sim \frac{1+\tau^2}{d} \chi^2_d \\
&\sim \left( 1+\tau^2, \; \frac{2+2\tau^2}{d} \right) \quad \begin{matrix} \text{notation} \\ (\text{mean}, \; \text{variance}) \end{matrix}
\end{aligned}
$$

---

Define $\zeta(\tau^2) = \frac{1}{1+\tau^2}$

$\Rightarrow \delta(X) = (1 - \mathbb{E}[\zeta \mid X]) X_i$

Conjugate prior:
$$
v = \|X\|^2 \mid \zeta \sim \frac{1}{\zeta} \chi^2_d = \frac{\zeta^{d/2}}{\Gamma(d/2)} v^{\frac{d}{2}-1} e^{-\zeta v}
$$

$$
\zeta \sim \frac{1}{s} \chi^2_k = \frac{s^{k/2}}{\Gamma(k/2)} \zeta^{\frac{k}{2}-1} e^{-s\zeta}
$$

$$
\begin{aligned}
\Rightarrow \zeta \mid \|X\|^2 &\propto_\zeta \zeta^{\frac{k+d}{2}-1} e^{-(s + \|X\|^2)\zeta} \\
&\sim \frac{1}{s + \|X\|^2} \chi^2_{k+d}
\end{aligned}
$$

$$
\mathbb{E}[\zeta \mid \|X\|^2] = \frac{k+d}{s + \|X\|^2} \approx d(1+\tau^2) + O(d^{1/2})
$$

$\left[ \text{might want to truncate prior to } [0, 1] \text{ if } d \text{ small} \right]$

---

[← Flexibility of Bayes](03-flexibility-of-bayes.md) · [Up: contents](index.md)
