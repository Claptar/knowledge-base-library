---
title: Measures
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/measure-theory-basics.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/measure-theory-basics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Measures

**Source:** [`reader/measure-theory-basics.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/measure-theory-basics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Given a set $\cX$, a measure$\mu$ is a certain kind of function mapping "nice enough" subsets $A \subseteq \cX$ to non-negative numbers $\mu(A) \in [0,\infty]$.

**Example 1 (Counting measure):** If $\cX$ is countable, e.g. $\cX = \mathbb{Z}$, then a natural measure is the *counting measure* $\#(A)$*,* which simply counts the number of points in a subset $A$. That is, $\#(\{0,1\}) = 2$, and $\#(\{2,4,6,8,\ldots\}) = \infty$ .

**Example 2 (Lebesgue measure):** If $\cX = \RR^n$ for some integer $n$, a natural measure is the *Lebesgue measure* $\lambda(A)$, which returns the *volume* of a subset $A$. Roughly speaking, we can write

$$
\lambda(A) = \int \cdots \int_A \td x_1\td x_2\cdots \td x_n.
$$

**Example 3 (Gaussian measure):** Now taking $\cX = \RR$, we might instead want to define the "size" of a set as the probability that a standard Gaussian random variable $Z \sim \cN(0,1)$ is observed to be in the set $A$. That is, we can define the measure:

$$
P_Z(A) = \PP(Z \in A) = \int_A \phi(x)\td x, \quad \text{ where } \;\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}
$$

is the probability density function of $Z$.

As it turns out, it is not so obvious how to define what exactly we mean by the right-hand side of the previous two equations; in fact, it is not even possible to define the volume of *every* subset $A \in \mathbb{R}$. In [Homework 0](https://www.stat.berkeley.edu/~wfithian/courses/stat210a/hw0.pdf), Problem 3, you will use the axiom of choice to construct pathological subsets (so-called *non-measurable sets*) to which we cannot sensibly assign any volume.

One of the original motivations for measure theory was to provide a framework for excluding these pathological sets and rigorously defining integrals over the other, nicer sets. In general, the domain of a measure is not all subsets of $\cX$ (called the power set and notated $2^{\cX}$), but rather a collection of nice subsets $\cF \subseteq 2^{\cX}$.

Formally, the collection $\cF$ must be a $\sigma$-field, meaning that it satisfies certain closure properties. We say $\cF$ is a $\sigma$-*field* (or $\sigma$-*algebra*) if

1.  The full set $\cX$ is in $\cF$.

2.  If $A$ is in $\cF$ then its complement $\cX \setminus A$ is also in $\cF$ (i.e., $\cF$ is *closed under complementation*)

3.  If $A_1,A_2,\ldots \in \cF$ then $\bigcup_{i=1}^\infty A_i$ is also in $\cF$ (i.e. $\cF$ is *closed under countable unions*)

**Note:** The details of this definition are not important for purposes of this course.

**Example:** If $\cX$ is countable we can take $\cF$ to be the entire power set.

**Example:** If $\cX = \mathbb{R}^n$ we will typically use the *Borel* $\sigma$-*field* $\cB$, defined as the smallest $\sigma$-field that includes all open rectangles $(a_1,b_1)\times (a_2,b_2) \times \cdots \times (a_n, b_n)$, where $a_i < b_i$ for all $i$. That is, we start with the open rectangles and recursively apply the closure properties to obtain a very large collection of sets, which informally we can think of as containing all non-pathological subsets of $\mathbb{R}^n$.

We are now ready to define a measure. We call a pair of a set $\cX$ and an associated $\sigma$-field $\cF \subseteq 2^{\cX}$ a *measurable space*. Given a measurable space $(\cX, \cF)$, a *measure* is a function $\mu: \cF \to \mathbb{R}$ satisfying three properties:

1.  **Non-negativity:** $\mu(A) \geq 0$ for all $A\in \cF$.

2.  **Empty set maps to zero:** $\mu(\emptyset) = 0$

3.  **Countable additivity:** If $A_1,A_2,\ldots\in \cF$ are all disjoint, then

$$
\mu\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty \mu(A_i)
$$

If $\mu$ is a measure on $(\cX, \cF)$ we call $(\cX, \cF, \mu)$ a *measure space*.

In the special case $\mu(\cX) = 1$, we call $\mu$ a *probability measure* and $(\cX, \cF, \mu)$ is called a *probability space*.

---

[← Measure theory: a rigorous grounding for probability](01-measure-theory-a-rigorous-grounding-for-probability.md) · [Up: contents](index.md) · [Integrals →](03-integrals.md)
