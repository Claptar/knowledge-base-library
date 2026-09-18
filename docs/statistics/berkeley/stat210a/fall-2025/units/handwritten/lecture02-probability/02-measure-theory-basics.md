---
title: Measure theory basics
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/handwritten/lecture02-probability.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/handwritten/lecture02-probability.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/handwritten/lecture02-probability.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/handwritten/lecture02-probability.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Measure theory basics

Measure theory is a rigorous grounding for probability theory [subject of 205A]

Simplifies notation & clarifies concepts, especially around integration & conditioning

Given a set $\mathcal{X}$, a measure $\mu$ maps subsets $A \subseteq \mathcal{X}$ to non-negative numbers $\mu(A) \in [0, \infty]$

**Example** $\mathcal{X}$ countable (e.g. $\mathcal{X} = \mathbb{Z}$)

**Counting measure** $#(A) = # \text{ points in } A$

**Example** $\mathcal{X} = \mathbb{R}^n$

**Lebesgue measure** $\lambda(A) = \int \dots \int_A dx_1 \dots dx_n = \text{Volume}(A)$

**Standard Gaussian distribution**:
$$P_Z(A) = \mathbb{P}(Z \in A) \quad \text{where } Z \sim \mathcal{N}(0, 1)$$
$$= \int_A \phi(x)\,dx \qquad \phi(x) = \frac{e^{-x^2/2}}{\sqrt{2\pi}}$$

**NB** Because of pathological sets, $\lambda(A)$ can only be defined for certain subsets $A \subseteq \mathbb{R}^n$

---

In general, the domain of a measure $\mu$ is a collection of subsets $\mathcal{F} \subseteq 2^{\mathcal{X}}$ (power set)

$\mathcal{F}$ should satisfy certain closure properties
(technical term: $\sigma$-field) (not important for us)

1. $\mathcal{X} \in \mathcal{F}$
2. If $A \in \mathcal{F}$ then $\mathcal{X} \setminus A \in \mathcal{F}$
3. If $A_1, A_2, \dots \in \mathcal{F}$ then $\bigcup_{i=1}^\infty A_i \in \mathcal{F}$

**Ex**: $\mathcal{X}$ countable, $\mathcal{F} = 2^{\mathcal{X}}$

**Ex**: $\mathcal{X} = \mathbb{R}^n$, $\mathcal{F} = \text{Borel } \sigma\text{-field } \mathcal{B}$
$\mathcal{B} = \text{smallest } \sigma\text{-field including all open rectangles}$
$$(a_1, b_1) \times \dots \times (a_n, b_n) \quad a_i < b_i \quad \forall i$$

Given a **measurable space** $(\mathcal{X}, \mathcal{F})$, a **measure** is a map $\mu : \mathcal{F} \to [0, \infty]$ with
$$\mu\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty \mu(A_i) \quad \text{for disjoint } A_1, A_2, \dots \in \mathcal{F}$$
$$\mu(\emptyset) = 0$$

$\mu$ **probability measure** if $\mu(\mathcal{X}) = 1$

---

## Integrals

Measures let us define **integrals** that put weight $\mu(A)$ on $A \subseteq \mathcal{X}$

Define $\int \mathbf{1}\{x \in A\} \, d\mu(x) = \mu(A)$, extend to other functions by linearity & limits:

Indicator: $\int \mathbf{1}\{x \in A\} \, d\mu(x) = \mu(A)$

Simple Function: $\int \left(\sum c_i \, \mathbf{1}\{x \in A_i\}\right) d\mu(x) = \sum c_i \, \mu(A_i)$

"Nice enough" (measurable) + function: $\int f(x) \, d\mu(x)$ approximated by simple functions

---

### Examples:

Counting: $\int f \, d# = \sum_{x \in \mathcal{X}} f(x)$

Lebesgue: $\int f \, d\lambda = \int \dots \int f(x) \, dx_1 \dots dx_n$  $\leftarrow$ Lebesgue integral

Gaussian: Note $\int \mathbf{1}_A(x) \, dP_Z(x) = P_Z(A) = \int_{-\infty}^\infty \mathbf{1}_A \, \phi \, dx$

By extension,
$$\int f \, dP_Z = \int f(x) \, \phi(x) \, dx = \mathbb{E}[f(Z)]$$

To evaluate $\int f \, dP_Z$, rewrite as $\int f \phi \, dx$. $\leftarrow$ density [can't always do this, e.g. Binom]

It is nice to turn integrals we care about into Lebesgue integrals. When can we do this?

---

---

[← Probability as a measure](01-probability-as-a-measure.md) · [Up: contents](index.md) · [Densities →](03-densities.md)
