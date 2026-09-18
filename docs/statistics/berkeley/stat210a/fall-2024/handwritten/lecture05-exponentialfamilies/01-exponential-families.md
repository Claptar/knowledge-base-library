---
title: Exponential Families
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture05-exponentialfamilies.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture05-exponentialfamilies.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture05-exponentialfamilies.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture05-exponentialfamilies.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Exponential Families

### Outline

1) Exponential families
2) Differential identities
3) MGF

---

An $s$-parameter **exponential family** is a family $\mathcal{P} = \{P_\eta : \eta \in \Xi\}$ with densities of the form
$$p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x)$$
wrt base measure $\mu$ on sample space $\mathcal{X}$

### Components of $p_\eta$:

* $\eta \in \Xi \subseteq \mathbb{R}^s$ called **natural parameter**
* $T(x)$ is $s$-dimensional **sufficient statistic**
  $$\text{factorization theorem: } g_\eta(T(x)) = e^{\eta' T(x) - A(\eta)}$$
* $h(x) \ge 0$ called **base density** or **carrier density**
  can be absorbed into base measure $\mu$
* $A(\eta)$ called **log-partition function** or **normalizing const.**
  $A(\cdot)$ determined by $T, h, \mu$:
  $$A(\eta) = \log \left[ \int_{\mathcal{X}} e^{\eta' T(x)} h(x) \, d\mu(x) \right] \le \infty$$

---

The natural parameter space is the set of all $\eta$ that give us normalizable $p_\eta$

$$\Xi_1 = \{\eta : A(\eta) < \infty\}$$

**Note**: $\mathcal{P}$ can use strict subset ($\Xi \subsetneq \Xi_1$) if scientific considerations constrain $\eta$

$A(\eta)$ is always a convex function $\Rightarrow \Xi_1$ convex set

If we absorb $h$ into $\mu$, log-densities almost linear
$$\log p_\eta(x) = \eta' T(x) - A(\eta) \quad (\text{wrt } h \, d\mu)$$

Can think of $T(x)$ as basis

Very nice structure when we multiply densities
* Combining evidence from independent obs.
* $\text{Prior} \times \text{likelihood}$ in Bayesian calculations

or divide them
* Calculating conditional probabilities
* Likelihood ratios
* Relative densities

---

## Examples

### Poisson (single obs)

$$X \sim \text{Pois}(\lambda) = \frac{\lambda^x e^{-\lambda}}{x!} \quad x \in 0, 1, \dots$$

$$p_\lambda(x) = \exp \{ (\log \lambda) x - \lambda \} \frac{1}{x!}$$

$$\eta(\lambda) = \log \lambda \qquad T(x) = x$$
$$A(\eta) = \lambda = e^\eta \qquad h(x) = \frac{1}{x!}$$

### Poisson ($n$ obs) $X_1, \dots, X_n \overset{iid}{\sim} \text{Pois}(\lambda)$

$$p_\lambda(x) = \prod_{i=1}^n \exp \{ (\log \lambda) x_i - \lambda \} \frac{1}{x_i!}$$
$$= \exp \left\{ (\log \lambda) (\sum x_i) - n\lambda \right\} \prod_i \frac{1}{x_i!}$$

$$\eta(\lambda) = \log \lambda \qquad T(x) = \sum x_i$$
$$A(\eta) = n e^\eta \qquad h(x) = \prod_i \frac{1}{x_i!}$$

### Generic ($n$ obs) $X_1, \dots, X_n \overset{iid}{\sim} p_\eta^{(1)}(x) = e^{\eta' T^{(1)}(x) - A^{(1)}(\eta)} h^{(1)}(x)$

$$p_\eta(x) = \prod_{i=1}^n \exp \left\{ \eta' T^{(1)}(x_i) - A^{(1)}(\eta) \right\} h^{(1)}(x_i)$$
$$= \exp \Big\{ \eta' \underbrace{\Big(\sum_i T^{(1)}(x_i)\Big)}_{T(x)} - \underbrace{n A^{(1)}(\eta)}_{A(\eta)} \Big\} \underbrace{\prod_i h^{(1)}(x_i)}_{h(x)}$$

$\Rightarrow$ Dimension of $T(x)$ doesn't grow with $n$

---

---

[Up: contents](index.md) · [Differential Identities →](02-differential-identities.md)
