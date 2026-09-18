---
title: Densities
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture01-F24
  Copy.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture01-F24 Copy.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture01-F24 Copy.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture01-F24 Copy.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Densities

$\lambda$ and $P$ above are closely related. Want to make this precise.

Given $(\mathcal{X}, \mathcal{F})$, two measures $P, \mu$

We say $P$ is **absolutely continuous** wrt $\mu$ if $P(A) = 0$ whenever $\mu(A) = 0$

Notation: **$P \ll \mu$** or we say $\mu$ **dominates** $P$

If $P \ll \mu$ then (under mild conditions) we can always define a **density function**

$$p : \mathcal{X} \to [0, \infty) \quad \text{with}$$

$$P(A) = \int_A p(x) d\mu(x)$$

$$\int f(x) dP(x) = \int f(x) p(x) d\mu(x)$$

Sometimes written $p(x) = \frac{dP}{d\mu}(x)$, called **Radon-Nikodym derivative**

---

Densities are very useful:

Turn $\int f(x) dP(x)$ into something we know how to evaluate, such as

1) $\int_\mathcal{X} f(x) p(x) \, dx \quad (\mathcal{X} \text{ continuous}, \mathcal{X} \subseteq \mathbb{R}^n)$

   $p(x)$ called **probability density function** (pdf)

2) $\sum_{x \in \mathcal{X}} f(x) p(x) \quad (\mathcal{X} \text{ discrete}, \mathcal{X} \text{ countable})$

   $p(x)$ called **probability mass function** (pmf)

Often define distributions by giving their density wrt some known measure, e.g.

**Ex:** $\text{Binom}(n, \theta)$ pmf: $p(x) = \theta^x (1 - \theta)^{n-x} \binom{n}{x}, \quad x = 0, \dots, n$

(density $p$ wrt counting measure on $\mathcal{X} = \{0, \dots, n\}$)

Note this dist. has **no** density wrt Lebesgue:

$$\int_{\{0, \dots, n\}} p(x) \, dx = 0 \quad \text{for any function } p$$

---

## Probability Spaces, Random Variables

Typically, we set up a problem with multiple random variables having various relationships to one another.

Want to be able to talk about the "prob. that something happens"

Convenient setup:

R.V.s as functions of an abstract "outcome" $\omega$

Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a **probability space**

$\omega \in \Omega$ called **outcome**

$A \in \mathcal{F}$ called **event**

$\mathbb{P}(A)$ called **probability of $A$**

A **random variable** is a function $X : \Omega \to \mathcal{X}$

We say $X$ has distribution $Q$ ($X \sim Q$) if

$$\mathbb{P}(X \in B) = \mathbb{P}(\{\omega : X(\omega) \in B\})$$

$$= Q(B)$$

---

More generally, could write events involving many R.V.s:

$$\mathbb{P}(X > Y > Z \ge 0) = \mathbb{P}(\{\omega : \dots \})$$

The **expectation** is an integral wrt $\mathbb{P}$

$$\mathbb{E}[f(X, Y)] = \int_\Omega f(X(\omega), Y(\omega)) \, d\mathbb{P}(\omega)$$

To do real calculations we must eventually boil $\mathbb{P}$ or $\mathbb{E}$ down to concrete integrals/sums/etc.

If $\mathbb{P}(A) = 1$ we say $A$ occurs **almost surely**

More in Keener ch. 1, much more in Stat 205A

---

[← Measure theory basics](01-measure-theory-basics.md) · [Up: contents](index.md)
