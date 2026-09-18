---
title: Ex. Exponential Families
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture08-fisherinfo.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture08-fisherinfo.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture08-fisherinfo.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture08-fisherinfo.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Ex. Exponential Families

$$p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x)$$
$$\ell(\eta; x) = \eta' T(x) - A(\eta) + \log h(x)$$
$$\nabla \ell(\eta; x) = T(x) - \nabla A(\eta)$$
$$= T(x) - \mathbb{E}_\eta T(X)$$

$$\mathrm{Var}_\eta(\nabla \ell(\eta)) = \mathrm{Var}_\eta(T(X)) = \nabla^2 A(\eta)$$
$$\nabla^2 \ell(\eta; x) = -\nabla^2 A(\eta)$$
$$\mathbb{E}_\eta [-\nabla^2 \ell(\eta; x)] = \nabla^2 A(\eta) \quad \checkmark$$

So any unbiased est. of $\eta$ has
$$\mathrm{Var}_\eta(\delta) \ge \nabla^2 A(\eta)^{-1}$$

---

**Curved family**:
$$p_\theta(x) = e^{\eta(\theta)' T(x) - B(\theta)} h(x), \quad \theta \in \mathbb{R}$$
$$B(\theta) = A(\eta(\theta))$$

$$\ell(\theta; x) = \eta(\theta)' T(x) - B(\theta) + \log h(x)$$
$$\dot{\ell}(\theta; x) = \dot{\eta}(\theta)' T(x) - \dot{\eta}(\theta)' \nabla_\eta A(\eta(\theta))$$
$$= \dot{\eta}(\theta)' (T(x) - \nabla_\eta A(\eta(\theta)))$$
$$= \dot{\eta}(\theta)' (T(x) - \mathbb{E}_\theta T(X))$$

$\implies \dot{\eta}(\theta)' T(X)$ is "locally complete suff. stat."

$$\dot{\eta}(\theta) = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \implies T_2(X) \text{ important}$$
$$\dot{\eta}(\theta) = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \implies T_1(X) \text{ important}$$

---

## Fisher info as local metric

**Kullback-Leibler Divergence**
$$D_{KL}(p \parallel q) = \mathbb{E}_p [\log p(X) - \log q(X)]$$
$$= \int \log\left(\frac{p}{q}\right) p \, d\mu$$

Distance between two distributions

**Parametric model**
$$D_{KL}(\theta^* \parallel \theta) = D_{KL}(p_{\theta^*} \parallel p_\theta)$$
$$= \int (\ell(\theta^*) - \ell(\theta)) e^{\ell(\theta^*)} d\mu$$

Standard "distance" between two distributions
$\theta^*$ "real" distribution, function of $\theta$

---

Maximized at $\theta = \theta^*$:

$$\frac{\partial}{\partial \theta_j} D_{KL}(\theta^* \parallel \theta) = - \int \frac{\partial \ell}{\partial \theta_j}(\theta) e^{\ell(\theta^*)} d\mu$$
$$= 0 \quad \text{at } \theta = \theta^*$$

$$\frac{\partial^2}{\partial \theta_j \partial \theta_k} D_{KL}(\theta^* \parallel \theta) = - \int \frac{\partial^2 \ell}{\partial \theta_j \partial \theta_k}(\theta) e^{\ell(\theta^*)} d\mu$$
$$= + \mathcal{J}(\theta^*)_{jk} \quad \text{at } \theta = \theta^*$$

$d = 1$:

---

[← Lecture 08 — fisherinfo Part 01 —](01-lecture-08-fisherinfo-part-01.md) · [Up: contents](index.md)
