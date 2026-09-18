---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture22-mle-consistency.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture22-mle-consistency.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture22-mle-consistency.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture22-mle-consistency.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

1) Maximum Likelihood Estimator
2) Asymptotic Distribution of MLE
3) Consistency of MLE

---

## Asymptotic Dist. of MLE

Under mild conditions, $\hat{\theta}_{\text{MLE}}$ is asy. Gaussian, efficient

We will be interested in $\ell(\theta; X)$ as a function of $\theta$

Notate "true" value as $\theta_0 \quad (X \sim P_{\theta_0})$

Derivatives of $\ell_n$ at $\theta_0$: $(\theta_0 \in \Theta^\circ)$

$$\nabla \ell_1(\theta_0; X_i) \overset{\text{iid}}{\sim} (0, J_1(\theta_0))$$

$$\frac{1}{\sqrt{n}} \nabla \ell_n(\theta_0; X) = \sqrt{n} \cdot \frac{1}{n} \sum \nabla \ell_1(\theta_0; X_i) \xrightarrow{P_{\theta_0}} \mathcal{N}(0, J_1(\theta_0))$$

$$\frac{1}{n} \nabla^2 \ell_n(\theta_0; X) \xrightarrow{P_{\theta_0}} \mathbb{E}_{\theta_0} \nabla^2 \ell_1(\theta_0; X_i) = -J_1(\theta_0)$$

**Proof sketch:**

$$0 = \nabla \ell_n(\hat{\theta}_n; X) = \nabla \ell_n(\theta_0) + \nabla^2 \ell_n(\tilde{\theta}_n)(\hat{\theta}_n - \theta_0) \quad \text{($\tilde{\theta}_n$ between $\theta_0, \hat{\theta}_n$)}$$

$$\sqrt{n}(\hat{\theta}_n - \theta_0) = -\left(\frac{1}{n} \nabla^2 \ell_n(\tilde{\theta}_n)\right)^{-1} \frac{1}{\sqrt{n}} \nabla \ell_n(\theta_0)$$

$$\text{(want)} \xrightarrow{P} J(\theta_0)^{-1} \implies \mathcal{N}(0, J(\theta_0))$$

$$\implies \mathcal{N}(0, J(\theta_0)^{-1})$$

More rigorous proof later, but note we need consistency of $\hat{\theta}_n$ first to even justify Taylor expansion

---

## Asymptotic Picture ($d=1$)

Recall $(\ell_n(\theta) - \ell_n(\theta_0))_{\theta \in \Theta}$ is minimal suff.

**Quadratic approximation near $\theta_0$:**

$$\ell_n(\theta) - \ell_n(\theta_0) \approx \dot{\ell}_n(\theta_0)(\theta - \theta_0) + \frac{1}{2}\ddot{\ell}_n(\theta_0)(\theta - \theta_0)^2$$

\$\$\dot{\ell}_n(\theta_0) \approx \mathcal{N}(0, nJ_1(\theta

---

[Up: contents](../index.md)
