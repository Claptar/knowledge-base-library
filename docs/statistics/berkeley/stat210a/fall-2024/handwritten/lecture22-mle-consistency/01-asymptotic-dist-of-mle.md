---
title: Asymptotic Dist. of MLE
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture22-mle-consistency.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture22-mle-consistency.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture22-mle-consistency.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture22-mle-consistency.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Asymptotic Dist. of MLE

1) Maximum Likelihood Estimator
2) Asymptotic Distribution of MLE
3) Consistency of MLE

---

Under mild conditions, $\hat{\theta}_{\text{MLE}}$ is asy. Gaussian, efficient

We will be interested in $l(\theta; X)$ as a function of $\theta$

Notate "true" value as $\theta_0 \quad (X \sim P_{\theta_0})$

Derivatives of $l_n$ at $\theta_0$: $\quad (\theta_0 \in \Theta^\circ)$

$\nabla l_1(\theta_0; X_i) \overset{\text{iid}}{\sim} (0, J_1(\theta_0))$

$\frac{1}{\sqrt{n}} \nabla l_n(\theta_0; X) = \sqrt{n} \cdot \frac{1}{n} \sum \nabla l_1(\theta_0; X_i) \overset{P_{\theta_0}}{\Rightarrow} \mathcal{N}(0, J_1(\theta_0))$

$\frac{1}{n} \nabla^2 l_n(\theta_0; X) \overset{P_{\theta_0}}{\to} \mathbb{E}_{\theta_0} \nabla^2 l_1(\theta_0; X_i) = -J_1(\theta_0)$

**Proof sketch:**

$$0 = \nabla l_n(\hat{\theta}_n; X) = \nabla l_n(\theta_0) + \nabla^2 l_n(\tilde{\theta}_n)(\hat{\theta}_n - \theta_0) \quad \text{($\tilde{\theta}_n$ between $\theta_0, \hat{\theta}_n$)}$$

$$\sqrt{n}(\hat{\theta}_n - \theta_0) = -\left(\frac{1}{n} \nabla^2 l_n(\tilde{\theta}_n)\right)^{-1} \frac{1}{\sqrt{n}} \nabla l_n(\theta_0)$$

$$\text{(want) } \overset{P}{\to} J(\theta_0)^{-1} \quad \Rightarrow \mathcal{N}_d(0, J(\theta_0))$$

$$\Rightarrow \mathcal{N}_d(0, J(\theta_0)^{-1})$$

More rigorous proof later, but note we need consistency of $\hat{\theta}_n$ first to even justify Taylor expansion

---

---

[Up: contents](index.md) · Asymptotic Picture ($d=1$) →
