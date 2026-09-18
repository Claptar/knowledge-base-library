---
title: Canonical Form
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture04-exponentialfamilies.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture04-exponentialfamilies.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture04-exponentialfamilies.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture04-exponentialfamilies.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Canonical Form

### Outline

1) Exponential families
2) Differential identities
3) MGF

---

## Exponential Families

An $s$-parameter exponential family is a family $\mathcal{P} = \{P_\eta : \eta \in \Xi\}$ with densities $p_\eta$ wrt a common measure $\mu$ on $\mathcal{X}$ [$\mathcal{X}$ not nec. in $\mathbb{R}^n$] of the form
$$p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x), \quad \text{where}$$

| | |
| :--- | :--- |
| $T : \mathcal{X} \to \mathbb{R}^s$ | **sufficient statistic** |
| $h : \mathcal{X} \to \mathbb{R}$ | **carrier/base density** |
| $\eta \in \Xi \subseteq \mathbb{R}^s$ | **natural parameter** |
| $A : \mathbb{R}^s \to \mathbb{R}$ | **log-partition function** or **normalizing const** |

**Note** The function $A(\cdot)$ is totally determined by $h$ and $T$, since we must always have
$$\int_\mathcal{X} p_\eta d\mu = 1, \quad \forall \eta.$$
$$\Rightarrow A(\eta) = \log \left[ \int_\mathcal{X} e^{\eta' T(x)} h(x) d\mu(x) \right] \le \infty$$

---

The structure is most evident when:
- $T(x) = x \quad$ (wlog: **sufficiency reduction**)
- $h(x) \equiv 1 \quad$ (wlog: absorb $h$ into $\mu$)
- $\theta = \eta \quad$ (wlog: parameterize by $\eta$)

Then, we say the family is in **canonical form**:
$$p_\eta(x) = e^{\eta' x - A(\eta)}$$

Density function is **$\log$-linear** in $\eta$
better than linear: we multiply or divide densities much more often than add or subtract

Multiplying or dividing densities
- Combining evidence from independent obs.
- $\text{Prior} \times \text{likelihood}$ in Bayesian calculations
- Divide to calculate conditional probabilities
- Divide to get likelihood ratios
- Divide to get relative densities

Add to get mixtures

---

The natural parameter space is the set of all $\eta$ that give us normalizable $p_\eta$

$$\Xi_1 = \{\eta : A(\eta) < \infty\}$$

**Note** $\Xi_1$ determined by $T$, $h$, $\mu$
We could take $\Xi \subsetneq \Xi_1$ if we wanted

$A(\eta)$ is always convex
$$\Rightarrow \quad \Xi_1 \text{ is convex} \quad (\text{HW 1 Prob. 2})$$

### Example: Poisson

$$X \sim \text{Pois}(\lambda) = \frac{\lambda^x e^{-\lambda}}{x!} \qquad x \in 0, 1, \dots$$

$$p_\lambda(x) = \exp\left\{ (\log \lambda) x - \lambda \right\} \frac{1}{x!}$$

$$\eta(\lambda) = \log \lambda \qquad T(x) = x$$
$$A(\lambda) = \lambda = e^\eta \qquad h(x) = \frac{1}{x!}$$

---

---

[Up: contents](index.md) · [Differential Identities →](02-differential-identities.md)
