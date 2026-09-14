---
title: Measures
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/probability.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/probability.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Measures

**Source:** [`reader/probability.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/probability.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Given a set $\cX$, a measure $\mu$ is a certain kind of function mapping (non-pathological[^1]) subsets $A \subseteq \cX$ to non-negative numbers $\mu(A) \in [0,\infty]$.


**Example 1 (Counting measure):** If $\cX$ is countable, e.g. $\cX = \mathbb{Z}$, then a natural measure is the *counting measure* $\#(A)$*,* which simply counts the number of points in a subset $A$. That is, $\#(\{0,1\}) = 2$, and $\#(\{2,4,6,8,\ldots\}) = \infty$ .

**Example 2 (Lebesgue measure):** If $\cX = \RR^n$ for some integer $n$, a natural measure is the *Lebesgue measure* $\lambda(A)$, which returns the *volume* of a subset $A$. Roughly speaking, we can write

$$
\lambda(A) = \int \cdots \int_A \,d x_1\,d x_2\cdots \,d x_n.
$$

**Example 3 (Gaussian measure):** Now taking $\cX = \RR$, we might instead want to define the "size" of a set as the probability that a standard Gaussian random variable $Z \sim \cN(0,1)$ is observed to be in the set $A$. That is, we can define the measure:

$$
P_Z(A) = \PP(Z \in A) = \int_A \phi(x)\,d x, \quad \text{ where } \;\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}
$$

is the probability density function of $Z$.

As it turns out, it is not so obvious how to define what exactly we mean by taking an integral when the set is sufficiently pathological: some sets are just called *non-measurable* and we can't hope to meaningfully assign them a measure. Sets of this kind are important to consider when building a rigorous theory about measures but they are not the sort of thing you would stumble upon unless you went out looking for them.

One of the original motivations for measure theory was to provide a framework for excluding these pathological sets and rigorously defining integrals over the other, nicer sets. In general, the domain of a measure is not all subsets of $\cX$ (called the power set and notated $2^{\cX}$), but rather a collection of "nice enough" subsets $\cF \subseteq 2^{\cX}$.

Formally, the collection $\cF$ must be a $\sigma$-field, meaning that it satisfies certain closure properties. We say $\cF$ is a $\sigma$-*field* (or $\sigma$-*algebra*) if

1.  The full set $\cX$ is in $\cF$.

2.  If $A$ is in $\cF$ then its complement $\cX \setminus A$ is also in $\cF$ (i.e., $\cF$ is *closed under complementation*)

3.  If $A_1,A_2,\ldots \in \cF$ then $\bigcup_{i=1}^\infty A_i$ is also in $\cF$ (i.e. $\cF$ is *closed under countable unions*)

The details of this definition are not important for purposes of this course.

**Example:** If $\cX$ is countable we can take $\cF$ to be the entire power set.

**Example:** If $\cX = \mathbb{R}^n$ we will typically use the *Borel* $\sigma$-*field* $\cB$, defined as the smallest $\sigma$-field that includes all open rectangles $(a_1,b_1)\times (a_2,b_2) \times \cdots \times (a_n, b_n)$, where $a_i < b_i$ for all $i$. That is, we start with the open rectangles and recursively apply the closure properties to obtain a very large collection of sets, which informally we can think of as containing all non-pathological subsets of $\mathbb{R}^n$.

We are now ready to define a measure. We call a pair of a set $\cX$ and an associated $\sigma$-field $\cF \subseteq 2^{\cX}$ a *measurable space*.

**Definition:** Given a measurable space $(\cX, \cF)$, a *measure* is a function $\mu: \cF \to [0,\infty]$ (inclusive of $+\infty$) satisfying three properties:

1.  **Non-negativity:** $\mu(A) \geq 0$ for all $A\in \cF$.

2.  **Countable additivity:** If $A_1,A_2,\ldots\in \cF$ are all disjoint, then

$$
\mu\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty \mu(A_i)
$$

3.  **Empty set maps to zero:** $\mu(\emptyset) = 0$[^2]


If $\mu$ is a measure on $(\cX, \cF)$ we call $(\cX, \cF, \mu)$ a *measure space*. In the special case $\mu(\cX) = 1$, we call $\mu$ a *probability measure* and $(\cX, \cF, \mu)$ is called a *probability space*.

[^1]: A problem in the first homework will guide you step-by-step in constructing the kind of pathological set that makes the parenthetical caveat necessary when we are dealing with continuous spaces.

[^2]: The requirement that $\mu(\emptyset) = 0$ is redundant if $\mu(\cX)$ is finite. Otherwise, it prevents us from assigning infinite measure to every set including $\emptyset$.

---

[← Probability as a measure](02-probability-as-a-measure.md) · [Up: contents](index.md) · [Integrals →](04-integrals.md)
