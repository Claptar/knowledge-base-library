---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework1.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework1.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`homework/homework1.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework1.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Intuition may fail us when we condition on a measure-zero event, and in cases like this the meaning can be ambiguous and give different answers. Conditioning on a random variable, on the other hand, tends to give less ambiguous answers (there are still some ambiguities, similar to those we encounter in defining densities, but they don’t really matter).

**Problem 3** (Densities for continuous-discrete mixtures). Suppose $\mu_1$ and $\mu_2$ are both measures on $\mathcal{X}$, and $a_1,a_2 \geq 0$. You may use without proof that the sum $\nu = a_1\mu_1 + a_2\mu_2$ is also a measure, and that we have $$\int f(x)\,d \nu(x) = a_1\int f(x)\,d \mu_1(x) + a_2\int f(x)\,d \mu_2(x),$$ provided the two integrals on the right are well-defined and finite.

1.  For $\mathcal{X}= \mathbb{R}$, define the measure $\mu(A) = \lambda(A) + \#(A)$, where $\lambda$ represents the Lebesgue measure and $\#$ represents the counting measure on the set of integers $\mathbb{Z}$. For fixed $\theta \in \mathbb{R}$, define the random variable $$X = \max(0,Z) \text{ where } Z \sim N(\theta, 1),$$ Let $P_\theta$ represent the probability distribution of $X$. Show that $P_\theta$ has no density with respect to $\lambda$ or $\#$. Find a density of $P_\theta$ with respect to $\mu$.

2.  Find a density for $P_\theta$ with respect to $P_0$, or show that none exists.

---

[← Moral](02-moral.md) · [Up: contents](index.md) · [Moral →](04-moral.md)
