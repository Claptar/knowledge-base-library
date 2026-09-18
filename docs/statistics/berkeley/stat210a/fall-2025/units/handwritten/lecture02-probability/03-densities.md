---
title: Densities
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/handwritten/lecture02-probability.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/handwritten/lecture02-probability.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/handwritten/lecture02-probability.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/handwritten/lecture02-probability.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Densities

$\lambda$ and $P$ above are closely related. Want to make this precise.

Given $(\mathcal{X}, \mathcal{F})$, two measures $P$, $\mu$
We say $P$ is **absolutely continuous** wrt $\mu$ if $P(A) = 0$ whenever $\mu(A) = 0$

Notation: $P \ll \mu$ or we say **$\mu$ dominates $P$**

If $P \ll \mu$ then (under mild conditions) we can always define a **density function**
$$p : \mathcal{X} \to [0, \infty) \quad \text{with}$$
$$P(A) = \int_A p(x) \, d\mu(x)$$
$$\int f(x) \, dP(x) = \int f(x) \, p(x) \, d\mu(x)$$

Sometimes written $p(x) = \frac{dP}{d\mu}(x)$, called **Radon-Nikodym derivative**

---

Densities are very useful:

Turn $\int f(x) \, dP(x)$ into something we know how to evaluate, such as

1) $\int_{\mathcal{X}} f(x) \, p(x) \, dx \quad (\mathcal{X} \text{ continuous}, \mathcal{X} \subseteq \mathbb{R}^n)$
$p(x)$ called **probability density function** (pdf)

2) $\sum_{x \in \mathcal{X}} f(x) \, p(x) \quad (\mathcal{X} \text{ discrete}, \mathcal{X} \text{ countable})$
$p(x)$ called **probability mass function** (pmf)

Often define distributions by giving their density wrt some known measure, e.g.

**Ex**: $\text{Binom}(n, \theta)$ pmf : $p(x) = \theta^x (1 - \theta)^{n-x} \binom{n}{x}$, $x = 0, \dots, n$
(density $p$ wrt counting measure on $\mathcal{X} = \{0, \dots, n\}$)

Note this dist. has **no** density wrt Lebesgue:
$$\int_{\{0, \dots, n\}} p(x) \, dx = 0 \quad \text{for any function } p$$

---

---

[← Measure theory basics](02-measure-theory-basics.md) · [Up: contents](index.md) · [Probability spaces, random variables →](04-probability-spaces-random-variables.md)
