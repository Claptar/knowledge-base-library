---
title: Generalized LRT
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture23-likelihoodbasedinference.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture23-likelihoodbasedinference.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture23-likelihoodbasedinference.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture23-likelihoodbasedinference.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Generalized LRT

Test $H_0: \theta = \theta_0 \quad \text{vs.} \quad H_1: \theta \ne \theta_0$

Taylor expand around $\hat{\theta}_n$:

$$\ell_n(\theta_0) - \ell_n(\hat{\theta}_n) = \nabla \ell(\hat{\theta}_n)^0 + \frac{1}{2}(\theta_0 - \hat{\theta}_n)' \nabla^2 \ell_n(\tilde{\theta}_n) (\theta_0 - \hat{\theta}_n)$$
$$= -\frac{1}{2} \cdot \left\| \underbrace{\left(-\frac{1}{n}\nabla^2 \ell_n(\tilde{\theta}_n)\right)^{1/2}}_{\xrightarrow{P} J_1(\theta_0)} \underbrace{(\sqrt{n}(\theta_0 - \hat{\theta}_n))}_{\Rightarrow \mathcal{N}(0, J_1(\theta_0)^{-1})} \right\|_2^2$$
$$\Rightarrow -\frac{1}{2}\chi^2_d$$

Test stat:
$$2(\ell_n(\hat{\theta}_n; X) - \ell_n(\theta_0; X)) \overset{P_{\theta_0}}{\Longrightarrow} \chi^2_d$$

---

### Composite vs. Composite:

$$H_0: \theta \in \Theta_0 \quad \text{vs} \quad H_1: \theta \in \Theta \setminus \Theta_0,$$

Assume
- $\Theta = \mathbb{R}^d$, $\Theta_0$ $d_0$-dim manifold
- $\theta_0 \in \text{relint}(\Theta_0)$
- $\hat{\theta}_n \xrightarrow{P_{\theta_0}} \theta_0$
- Likelihood "smooth"

Then $2(\ell_n(\hat{\theta}_n) - \ell_n(\hat{\theta}_0)) \Rightarrow \chi^2_{d-d_0}$
where $\hat{\theta}_0 = \operatorname{argmin}_{\theta \in \Theta_0} \ell_n(\theta; X)$

Why? Assume wlog $\theta_0 = 0$, $J_1(0) = I_d$ (reparam.)
Then $\hat{\theta}_n \approx \mathcal{N}_d(\theta_0, \frac{1}{n}I_d)$
And locally, $\nabla^2 \ell_n(\theta) \approx -n I_d$ near $\theta_0$

$$\ell_n(\theta) - \ell_n(\hat{\theta}_n) \approx \frac{n}{2} \|\theta - \hat{\theta}_n\|^2$$

$$\hat{\theta}_0 \approx \operatorname{argmin}_{\theta \in \Theta_0} \|\theta - \hat{\theta}_n\| = \mathrm{Proj}_{\Theta_0}(\hat{\theta}_n)$$

$$2(\ell(\hat{\theta}_0) - \ell_n(\hat{\theta}_n)) \approx n \|\hat{\theta}_n - \mathrm{Proj}_{\Theta_0}(\hat{\theta}_n)\|^2$$
$$= n \|\mathrm{Proj}_{\Theta_0}^\perp(\hat{\theta}_n)\|^2$$
$$\Rightarrow \chi^2_{d-d_0}$$

---

## Asymptotic Equivalence

Recall quadratic approx. picture ($d=1$):

$$\ell(\theta) - \ell_n(\theta_0) \approx \dot{\ell}(\theta_0)(\theta - \theta_0) + \frac{1}{2} J_n(\theta_0)(\theta - \theta_0)^2$$

- GLRT: $\ell_n(\hat{\theta}_n) - \ell_n(\theta_0) \approx \frac{1}{2} J_n^{-1} \dot{\ell}(\theta_0)^2$
- Score: slope is $\dot{\ell}_n(\theta_0)$
- Wald: $\hat{\theta}_n - \theta_0 \approx J_n^{-1} \dot{\ell}(\theta_0)$

For large $n$,

$$\underbrace{\ell_n(\hat{\theta}_n) - \ell_n(\theta_0)}_{(\text{GLRT})} \approx \|J_n(\theta_0)^{1/2}(\hat{\theta}_n - \theta_0)\|^2$$

$$\approx \|\hat{J}_n^{1/2}(\hat{\theta}_n - \theta_0)\|^2 \quad (\text{Wald})$$

$$\approx \|J_n(\theta_0)^{-1/2} \nabla \ell_n(\theta_0)\|^2 \quad (\text{Score})$$

---

## Asymptotic Relative Efficiency (ARE)

Suppose $\hat{\theta}_n^{(i)}$, $i=1,2$ are two asy. Normal estimators of $\theta \in \mathbb{R}$, with

$$\sqrt{n}(\hat{\theta}_n^{(i)} - \theta_0) \Rightarrow \mathcal{N}(0, \sigma_i^2)$$

The ARE of $\hat{\theta}^{(2)}$ wrt $\hat{\theta}^{(1)}$ is $\sigma_1^2 / \sigma_2^2$
e.g. if $\sigma_2^2 = 2\sigma_1^2$ then $\hat{\theta}^{(2)}$ is 50% as efficient

**Interpretation:** Suppose $\sigma_1^2 / \sigma_2^2 = \gamma \in (0, 1)$

Then for large $n$,

$$\hat{\theta}_{\lfloor \gamma n \rfloor}^{(1)}(X_1, \dots, X_{\lfloor \gamma n \rfloor}) \overset{D}{\approx} \hat{\theta}_n^{(2)}(X_1, \dots, X_n) \approx \mathcal{N}\left(\theta, \frac{\sigma_2^2}{n}\right)$$

Using $\hat{\theta}^{(2)}$ is like throwing away $100(1-\gamma)\%$ of the data and then using $\hat{\theta}^{(1)}$

---

[← Lecture 23 — likelihoodbasedinference Part 03 —](03-lecture-23-likelihoodbasedinference-part-03.md) · [Up: contents](index.md)
