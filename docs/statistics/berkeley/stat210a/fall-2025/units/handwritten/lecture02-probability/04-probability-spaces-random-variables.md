---
title: Probability spaces, random variables
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/handwritten/lecture02-probability.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/handwritten/lecture02-probability.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/handwritten/lecture02-probability.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/handwritten/lecture02-probability.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Probability spaces, random variables

Problem setup may have many random outcomes with complex relationships to one another

Convenient to start with abstract outcome $\omega \in \Omega$
- represents "everything that happens"
- quantities of interest are functions of $\omega$

Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a **probability space**
- $\omega \in \Omega$ called **outcome**
- $A \in \mathcal{F}$ called **event**
- $\mathbb{P}(A)$ called **probability of $A$**

A **random variable** is a function $X : \Omega \to \mathcal{X}$

We say $X$ has distribution $Q$ ($X \sim Q$) if
$$\mathbb{P}(X \in B) = \mathbb{P}(\{\omega : X(\omega) \in B\}) = Q(B)$$

$Q(B)$ is the **push-forward** of $\mathbb{P}$: $Q(B) = \mathbb{P} \circ X^{-1}(B)$

Idea applies more generally: if $\mu$ measure on $\mathcal{X}$, $f : \mathcal{X} \to \mathcal{Y}$ induces new measure $\nu(B) = \mu(f^{-1}(B))$

---

Can write events involving many R.V.s:
$$\mathbb{P}(X > Y > Z \ge 0) = \mathbb{P}(\{\omega : \dots \})$$

The expectation is an integral wrt $\mathbb{P}$
$$\mathbb{E}[f(X, Y)] = \int_\Omega f(X(\omega), Y(\omega)) \, d\mathbb{P}(\omega)$$

To do real calculations we must eventually boil $\mathbb{P}$ or $\mathbb{E}$ down to concrete integrals/sums/etc.

If $\mathbb{P}(A) = 1$ we say $A$ occurs **almost surely**

More in Keener ch. 1, much more in Stat 205A

---

[← Densities](03-densities.md) · [Up: contents](index.md)
