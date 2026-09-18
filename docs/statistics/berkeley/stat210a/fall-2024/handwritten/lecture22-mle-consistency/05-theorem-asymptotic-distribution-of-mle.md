---
title: Theorem (Asymptotic distribution of MLE)
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture22-mle-consistency.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture22-mle-consistency.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture22-mle-consistency.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture22-mle-consistency.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Theorem (Asymptotic distribution of MLE)

$X_1, \ldots, X_n \overset{\text{iid}}{\sim} P_{\theta_0}, \quad \mathcal{P} \text{ has densities } p_\theta, \quad \theta \in \Theta$

Assume
- $\mathcal{P}$ identifiable
- $\Theta$ compact
- $\mathbb{E}_{\theta_0} \left[\sup_{\theta \in \Theta} |W_1(\theta)|\right] < \infty$
- $l(\theta; x) = \log p_\theta(x)$ has two cts derivatives in $\theta$
- $\mathbb{E}_{\theta_0} \sup_{\theta \in \Theta} \|\nabla^2 l_1(\theta; X_i)\| < \infty$
- $J_1(\theta_0) = \mathbb{E}_{\theta_0} \nabla^2 l_1(\theta_0; X_i) \succ 0 \quad \swarrow \text{positive definite}$

Then $\sqrt{n}(\hat{\theta}_n - \theta_0) \Rightarrow \mathcal{N}(0, J_1(\theta_0)^{-1})$

**Proof** From before, we had

$$\sqrt{n}(\hat{\theta}_n - \theta_0) = \left(-\frac{1}{n} \nabla^2 l_n(\tilde{\theta}_n)\right)^{-1} \nabla l_n(\theta_0)$$

for $\tilde{\theta}_n$ between $\theta_0$ and $\hat{\theta}_n$

Previous result shows $\hat{\theta}_n \overset{P}{\to} \theta_0$, so $\tilde{\theta}_n \overset{P}{\to} \theta_0$ also

Define $V_i(\theta) = -\nabla^2 l_1(\theta; X_i) \in C(\Theta)$, $\mathbb{E}_{\theta_0} \|V_1\|_\infty < \infty$ by assumption

Then $v(\theta) = \mathbb{E}_{\theta_0} V_1(\theta) \in C(\Theta)$, $v(\theta_0) = J_1(\theta_0)$

$\bar{V}_n(\theta) = \frac{1}{n}\sum V_i(\theta)$, $\|\bar{V}_n - v\|_\infty \overset{P}{\to} 0$

---

$$\|-\frac{1}{n} \nabla^2 l_n(\tilde{\theta}_n) - J_1(\theta_0)\| \le \|\bar{V}_n(\tilde{\theta}_n) - v(\tilde{\theta}_n)\| + \|v(\tilde{\theta}_n) - v(\theta_0)\|$$

$$\le \|\bar{V}_n - v\|_\infty + \|v(\tilde{\theta}_n) - v(\theta_0)\|$$

$$\underbrace{\phantom{\|\bar{V}_n - v\|_\infty}}_{\overset{P}{\to} 0} \quad \underbrace{\phantom{\|v(\tilde{\theta}_n) - v(\theta_0)\| \qquad}}_{\overset{P}{\to} 0 \text{ (cts mapping)}}$$

Hence $\left(-\frac{1}{n}\nabla^2 l_n(\tilde{\theta}_n)\right)^{-1} \overset{P}{\to} J_1(\theta_0)^{-1}$ (cts mapping)

And $\sqrt{n}(\hat{\theta}_n - \theta_0) \Rightarrow \mathcal{N}_d(0, J_1(\theta_0)^{-1})$ (Slutsky) $\tag*{$\blacksquare$}$

**Note** In this proof we played a bit fast and loose with our LLN for random functions, which we only stated for real-valued $W_n$.

So technically we have only justified for $d = 1$.

But proof works for $d > 1$.

---

[← Theorem (Consistency of MLE for compact $\Theta$)](04-theorem-consistency-of-mle-for-compact.md) · [Up: contents](index.md)
