---
title: Homework1 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework1.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework1.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework1 Part 01 —

**Source:** [`homework/homework1.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework1.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

You may disregard measure-theoretic niceties about conditioning on measure-zero sets, almost-sure equality vs. actual equality, “all functions” vs. “all measurable functions,” etc. (unless the problem is explicitly asking about such issues).

**Problem 1** (Non-measurable sets). This problem goes through a construction of a non-measurable set, meant to motivate measure theory from a real analysis perspective. It concerns the impossibility of defining “volume” for every subset of the unit interval $U=[0,1)$.

For $x,y \in \mathbb{R}$ define the “wraparound addition” (modulo 1) as the fractional part of their sum: $$x \oplus y = x + y - \lfloor x + y \rfloor.$$

Recall that for $x \in \mathbb{R}$ and $A \subseteq \mathbb{R}$ we define the set $x + A = \{x + a:\; a \in A\}$. Analogously, we can define $$x \oplus A = \{x \oplus a:\; a \in A\} \subseteq U$$

Any reasonable definition of “volume” on the interval should have several properties:

1.  Additivity: $\lambda(\bigcup_{i=1}^\infty A_i) = \sum_{i=1}^\infty \lambda(A_i)$ if all $A_i\subseteq U$ and $A_i \cap A_j = \emptyset$ for all $i \neq j$.

2.  Translation invariance: $\lambda(x \oplus A) = \lambda(A), \;\forall x\in U, A\subseteq U$.

3.  Interval length: $\lambda([x,y]) = y - x, \;\forall 0 \leq x \leq y < 1$.

Assume that some measure $\lambda$ exists which satisfies (i)–(iii) and which is defined for all subsets of $U$. We will go through several steps to derive a contradiction.

1.  Define the function $A(x)$ mapping elements of $U$ to subsets of $U$, via $A(x) = x \oplus \mathbb{Q}$, where $\mathbb{Q}$ is the set of rational numbers. Show that $\lambda(A(x)) = 0$ for any $x$.

2.  Consider the range $\mathcal{R}_A = \{A(x):\; x\in U\}$. Show that $\mathcal{R}_A$ is a collection of uncountably many subsets of $U$, all of which are disjoint from each other. That is, show that for any $x,y\in U$, we have either $A(x)=A(y)$ or $A(x) \cap A(y) = \emptyset$.

3.  Now, let $B\subseteq U$ denote a new set, which we construct by selecting a *single element* from each set $R\in\mathcal{R}_A$ (it doesn’t matter which element; note this step uses the axiom of choice.)

    Define a new function $C(x) = x \oplus B$ and define $\mathcal{R}_C = \{C(x):\; x \in \mathbb{Q}\}$. Show that $\mathcal{R}_C$ is a collection of *countably* many subsets of $U$, all of which are disjoint from each other, and whose union is $U$.

4.  Show that no matter what value $\lambda(B)$ takes, $\lambda$ will have to violate one of the properties (i)–(iii)

    **Hint:** what does the value of $\lambda(B)$ imply about $\lambda(U)$?

Because the Lebesgue measure satisfies properties (i)–(iii), it follows that $\lambda$ must not be defined for every subset of $U$.

---

[Up: contents](index.md) · [Moral →](02-moral.md)
