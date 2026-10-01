---
title: "23. Measures, Integration, and Densities"
course: "Berkeley Stat 210A"
chapter: 23
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 23. Measures, Integration, and Densities

## What this covers

Stat 210A opens by putting probability on a measure-theoretic footing. This chapter answers two
questions: what is a measure, and how does it let us build a single notion of integral —
$\int f\,d\mu$ — that specializes to a sum for a discrete space and to an ordinary integral for a
continuous one? It then asks when two measures on the same space are related by a *density*, which
is the tool that turns an otherwise abstract integral $\int f\,dP$ into something computable. It
closes by fixing the vocabulary — probability space, random variable, expectation — in these terms.
The chapter assumes elementary probability (the kind covered in Stat 205A: random variables,
expectation, standard distributions) but not measure theory itself.

## Why bother with measure theory

Measure theory is a rigorous grounding for probability. The payoff the lecture points to is
practical rather than aesthetic: it simplifies notation and clarifies concepts, especially around
integration and conditioning — the two operations that ordinary calculus-based probability handles
by case analysis (a sum here, an integral there, a mixture of both when a random variable is part
discrete and part continuous). Measure theory handles all three with one symbol.

## Measures and measurable spaces

Given a set $\mathcal{X}$, a **measure** $\mu$ assigns to (suitable) subsets $A \subseteq \mathcal{X}$
a non-negative number $\mu(A) \in [0, \infty]$. Two examples fix the idea before the formalism does:

- $\mathcal{X}$ countable (e.g. $\mathcal{X} = \mathbb{Z}$): the **counting measure** $\#(A)$ is just
  the number of points in $A$.
- $\mathcal{X} = \mathbb{R}^n$: **Lebesgue measure** $\lambda(A) = \int \cdots \int_A dx_1 \cdots dx_n$
  is the volume of $A$.

A third example is the point of the whole construction: for $Z \sim N(0,1)$, define
$P_Z(A) = \mathbb{P}(Z \in A) = \int_A \phi(x)\,dx$ with $\phi(x) = e^{-x^2/2}/\sqrt{2\pi}$. This is
already a measure on $\mathbb{R}$ — it assigns a non-negative number to a set — and it is built out
of Lebesgue measure via the density $\phi$. Making that relationship precise is the subject of the
densities section below.

One warning attaches to Lebesgue measure immediately: because of pathological sets, $\lambda(A)$
can only be defined for certain subsets $A \subseteq \mathbb{R}^n$, not for every subset (this is
the content of HW 0, Problem 3, referred to but not worked out in the lecture). This is why a
measure is not defined on the full power set in general, but on a restricted collection of subsets.

That collection is required to satisfy closure properties. A collection $\mathcal{F} \subseteq
2^{\mathcal{X}}$ is a **$\sigma$-field** if

1. $\mathcal{X} \in \mathcal{F}$,
2. $A \in \mathcal{F} \implies \mathcal{X}\setminus A \in \mathcal{F}$ (closed under complement),
3. $A_1, A_2, \dots \in \mathcal{F} \implies \bigcup_{i=1}^\infty A_i \in \mathcal{F}$ (closed under
   countable union).

The two running examples: if $\mathcal{X}$ is countable, take $\mathcal{F} = 2^{\mathcal{X}}$ (every
subset is fine). If $\mathcal{X} = \mathbb{R}^n$, take $\mathcal{F}$ to be the **Borel
$\sigma$-field** $\mathcal{B}$, the smallest $\sigma$-field containing every open rectangle
$(a_1,b_1)\times\cdots\times(a_n,b_n)$ with $a_i < b_i$ for all $i$. The precise closure properties
are not the point for this course; what matters is that $\mathcal{F}$ is *some* collection of
"measurable" subsets that a measure is allowed to see.

A pair $(\mathcal{X}, \mathcal{F})$ is a **measurable space**. A **measure** on it is a map
$\mu: \mathcal{F} \to [0,\infty]$ satisfying countable additivity,
$$
\mu\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty \mu(A_i) \quad \text{for disjoint } A_1, A_2, \dots \in \mathcal{F},
$$
together with $\mu(\emptyset) = 0$. If in addition $\mu(\mathcal{X}) = 1$, $\mu$ is a **probability
measure**.

## Building the integral from the measure

Measure theory buys a single definition of integration that specializes correctly in every case.
The construction goes up in three stages, each defined so it is forced to agree with the last:

- **Indicator**: $\int 1\{x \in A\}\, d\mu(x) := \mu(A)$. This is the definition — an integral of an
  indicator function is exactly the measure of the set it indicates.
- **Simple function** (a finite linear combination of indicators): $\int \left(\sum_i c_i
  1\{x\in A_i\}\right) d\mu(x) := \sum_i c_i\, \mu(A_i)$, forced by linearity.
- **General (measurable) function** $f$: $\int f\, d\mu$ is defined by approximating $f$ with simple
  functions and taking a limit.

The specializations recover the familiar objects:

- Counting measure: $\int f\, d\# = \sum_{x\in\mathcal{X}} f(x)$ — an integral against counting
  measure is a sum.
- Lebesgue measure: $\int f\, d\lambda = \int\cdots\int f(x)\, dx_1\cdots dx_n$ — the ordinary
  Lebesgue integral.
- The Gaussian measure $P_Z$: since $\int 1_A(x)\, dP_Z(x) = P_Z(A) = \int_{-\infty}^{\infty} 1_A(x)
  \phi(x)\, dx$ on indicators, the same identity extends by linearity and limits to
$$
\int f\, dP_Z = \int f(x)\, \phi(x)\, dx = \mathbb{E}[f(Z)].
$$

So to evaluate $\int f\, dP_Z$, rewrite it as $\int f\phi\, dx$ using the density $\phi$ — but this
route is not always available. A distribution such as the Binomial has no such density against
Lebesgue measure (see below), so "turn the integral into a Lebesgue integral" cannot be the general
method; it works exactly when the measure in question has a density against a measure we already
know how to integrate against. That is the question the next section answers.

## Absolute continuity and densities

Fix a measurable space $(\mathcal{X}, \mathcal{F})$ and two measures $P, \mu$ on it. $P$ is
**absolutely continuous** with respect to $\mu$, written $P \ll \mu$ (equivalently, "$\mu$
dominates $P$"), if
$$
\mu(A) = 0 \implies P(A) = 0.
$$

If $P \ll \mu$ then, under mild conditions, there is always a **density function** $p: \mathcal{X}
\to [0,\infty)$ with
$$
P(A) = \int_A p(x)\, d\mu(x), \qquad \int f(x)\, dP(x) = \int f(x)\, p(x)\, d\mu(x).
$$
The density is sometimes written $p(x) = \dfrac{dP}{d\mu}(x)$ and called the **Radon-Nikodym
derivative** of $P$ with respect to $\mu$.

The value of a density is exactly what the Gaussian example needed: it turns $\int f\, dP$, an
integral against a measure we may not know how to compute directly, into an integral against a
measure we do — Lebesgue measure or counting measure. Two standard cases:

1. $\mathcal{X}$ continuous, $\mathcal{X}\subseteq \mathbb{R}^n$: $\int f\, dP = \int_{\mathcal{X}}
   f(x)\, p(x)\, dx$, and $p$ is called the **probability density function** (pdf).
2. $\mathcal{X}$ discrete, countable: $\int f\, dP = \sum_{x\in\mathcal{X}} f(x)\, p(x)$, and $p$ is
   called the **probability mass function** (pmf).

Distributions are often defined exactly this way — by giving a density against a known dominating
measure. For $X \sim \text{Binom}(n,\theta)$,
$$
p(x) = \binom{n}{x}\theta^x(1-\theta)^{n-x}, \qquad x = 0, 1, \dots, n,
$$
is the density with respect to *counting measure* on $\mathcal{X} = \{0,\dots,n\}$. This
distribution has **no** density with respect to Lebesgue measure: $\int_{\{0,\dots,n\}} p(x)\,dx = 0$
for any function $p$, because $\{0,\dots,n\}$ has Lebesgue measure zero. This is the counterexample
that shows the earlier "rewrite as a Lebesgue integral" trick is not universal — it depends on which
measure the distribution in question is absolutely continuous with respect to.

## Probability spaces and random variables

With measures and densities in hand, the standard objects of probability get precise definitions.
A problem typically involves several random variables with various relationships to one another,
and we want to talk about "the probability that something happens." The convenient setup treats
random variables as functions of an abstract outcome $\omega$.

Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a **probability space**: $\Omega$ a set, $\mathcal{F}$ a
$\sigma$-field on it, $\mathbb{P}$ a probability measure on $(\Omega,\mathcal{F})$. Then:

- $\omega \in \Omega$ is an **outcome**.
- $A \in \mathcal{F}$ is an **event**.
- $\mathbb{P}(A)$ is the **probability of $A$**.
- A **random variable** is a (measurable) function $X: \Omega \to \mathcal{X}$.

$X$ has **distribution** $Q$ (written $X \sim Q$) if $\mathbb{P}(X \in B) := \mathbb{P}(\{\omega :
X(\omega) \in B\}) = Q(B)$ for every measurable $B$.

More generally, an event can involve several random variables at once, e.g.
$$
\mathbb{P}(X > Y > Z \ge 0) = \mathbb{P}(\{\omega : X(\omega) > Y(\omega) > Z(\omega) \ge 0\}),
$$
and **expectation** is an integral with respect to $\mathbb{P}$:
$$
\mathbb{E}[f(X,Y)] = \int_\Omega f(X(\omega), Y(\omega))\, d\mathbb{P}(\omega).
$$

To do real calculations, $\mathbb{P}$ or $\mathbb{E}$ must eventually be reduced to a concrete
integral or sum — which is exactly the density machinery above. Finally, if $\mathbb{P}(A) = 1$, we
say $A$ occurs **almost surely**.

## Sources

- Berkeley Stat 210A, Fall 2024, Lecture 1 (dated 8/24/2023 on the slide itself), handwritten notes,
  reconstructed by a model from a PDF with no text layer: `01-measure-theory-basics.md` (measures,
  $\sigma$-fields, the integral built from indicators up) and `02-densities.md` (absolute continuity,
  Radon-Nikodym densities, probability spaces and random variables), both in
  `docs/statistics/berkeley/stat210a/fall-2024/handwritten/lecture01-F24/`. Both carry the
  reconstruction caveat that the prose paraphrases the source and every equation is unverified
  against the original handwriting.
- No slides, transcript, or exercise set was supplied for this lecture.
- The lecture points to material it does not itself contain: the syllabus and course goals section
  of the same lecture (outline items 1–2, not reconstructed here), Pset 0 and HW 0 Problem 3 (on
  which subsets of $\mathbb{R}^n$ Lebesgue measure can be defined), and Keener's textbook, Chapter 1,
  plus "much more" in Stat 205A, for the material this lecture only summarizes.

---

[← 22. Reader Notation Conventions](22-reader-notation-conventions.md) · [Contents](index.md) · [24. Measures, Integrals, and Densities →](24-measures-integrals-and-densities.md)
