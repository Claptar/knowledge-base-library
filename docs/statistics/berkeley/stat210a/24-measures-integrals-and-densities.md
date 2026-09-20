---
title: "24. Measures, Integrals, and Densities"
course: "Berkeley Stat 210A Fall 2024"
chapter: 24
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 24. Measures, Integrals, and Densities

## What this covers

Ordinary probability gets by with sums and Riemann integrals until it needs to handle continuous
and discrete random variables in one framework, or to make sense of conditioning rigorously. This
chapter lays down the minimum measure-theoretic vocabulary for that: what a measure is, how an
integral is built out of one, when one measure has a *density* with respect to another, and how a
probability space and a random variable fit into this picture. It assumes ordinary calculus and an
elementary, pre-measure-theoretic sense of probability (sample spaces, events); no prior exposure
to measure theory is assumed.

## Why bother with measure theory

Measure theory is the rigorous grounding for probability. The payoff the lecture points to is
practical rather than aesthetic: it simplifies notation and clarifies concepts, especially around
integration and conditioning — conditioning on a set of probability zero, for instance, is exactly
the kind of thing that is hard to state correctly without it.

## Measures and $\sigma$-fields

Given a set $\mathcal{X}$, a **measure** $\mu$ assigns to subsets $A \subseteq \mathcal{X}$ a
non-negative number $\mu(A) \in [0, \infty]$. Two examples fix the idea before the formal
definition:

- $\mathcal{X}$ countable (e.g. $\mathcal{X} = \mathbb{Z}$): the **counting measure**
  $\#(A) = $ the number of points in $A$.
- $\mathcal{X} = \mathbb{R}^n$: **Lebesgue measure**
  $\lambda(A) = \int \cdots \int_A dx_1 \cdots dx_n$, i.e. the volume of $A$.

A third example carries the thread that the rest of the chapter follows: for $Z \sim \mathcal{N}(0,1)$,
$$P_Z(A) = \mathbb{P}(Z \in A) = \int_A \phi(x)\, dx, \qquad \phi(x) = \frac{e^{-x^2/2}}{\sqrt{2\pi}}.$$
$P_Z$ is itself a measure on $\mathbb{R}$ — it just happens to be built by integrating a density
against Lebesgue measure, which is the phenomenon this chapter is aimed at.

A subtlety flagged immediately: because of pathological sets, $\lambda(A)$ cannot be defined for
*every* subset $A \subseteq \mathbb{R}^n$. So in general the domain of a measure $\mu$ is not the
whole power set $2^{\mathcal{X}}$ but some collection of subsets $\mathcal{F} \subseteq 2^{\mathcal{X}}$,
called a **$\sigma$-field**, required to satisfy closure properties (the lecture notes that the
closure conditions themselves are not something to dwell on here):

1. $\mathcal{X} \in \mathcal{F}$,
2. if $A \in \mathcal{F}$ then $\mathcal{X} \setminus A \in \mathcal{F}$,
3. if $A_1, A_2, \dots \in \mathcal{F}$ then $\bigcup_{i=1}^{\infty} A_i \in \mathcal{F}$.

Two standard choices: if $\mathcal{X}$ is countable, take $\mathcal{F} = 2^{\mathcal{X}}$ (no
pathology to avoid). If $\mathcal{X} = \mathbb{R}^n$, take $\mathcal{F}$ to be the **Borel
$\sigma$-field** $\mathcal{B}$, the smallest $\sigma$-field containing all open rectangles
$(a_1,b_1) \times \cdots \times (a_n,b_n)$ with $a_i < b_i$ for every $i$.

Given a **measurable space** $(\mathcal{X}, \mathcal{F})$, a **measure** is a map
$\mu : \mathcal{F} \to [0,\infty]$ satisfying countable additivity on disjoint sets,
$$\mu\Big(\bigcup_{i=1}^{\infty} A_i\Big) = \sum_{i=1}^{\infty} \mu(A_i) \quad \text{for disjoint } A_1, A_2, \dots \in \mathcal{F},$$
together with $\mu(\emptyset) = 0$. If in addition $\mu(\mathcal{X}) = 1$, $\mu$ is a **probability
measure**.

## Building integrals from a measure

A measure gives a notion of "weight" on subsets, and that weight is what an integral against the
measure sums up. The definition is built in three stages, each extending the last:

- **Indicator functions.** Declare $\int 1\{x \in A\}\, d\mu(x) = \mu(A)$ — the integral of the
  indicator of $A$ is just the measure of $A$.
- **Simple functions.** Extend by linearity: for a function that only takes finitely many values,
  $\int \big(\sum_i c_i 1\{x \in A_i\}\big)\, d\mu(x) = \sum_i c_i\, \mu(A_i)$.
- **General measurable functions.** A "nice enough" (measurable) function $f$ is approximated by
  simple functions, and $\int f\, d\mu$ is defined as the corresponding limit.

Specialising this construction to the three measures above recovers familiar objects. Against
counting measure, $\int f\, d\# = \sum_{x \in \mathcal{X}} f(x)$ — an ordinary sum. Against Lebesgue
measure, $\int f\, d\lambda = \int \cdots \int f(x)\, dx_1 \cdots dx_n$, the ordinary (Lebesgue)
integral from calculus. Against the Gaussian measure $P_Z$, since
$\int 1_A(x)\, dP_Z(x) = P_Z(A) = \int_{-\infty}^{\infty} 1_A(x)\, \phi(x)\, dx$ on indicators, the
same identity extends to general $f$:
$$\int f\, dP_Z = \int f(x)\, \phi(x)\, dx = \mathbb{E}[f(Z)].$$

That last line is the pattern to notice: to *evaluate* $\int f\, dP_Z$ in practice, rewrite it as
$\int f \phi\, dx$, an ordinary Lebesgue integral against the density $\phi$. This does not always
work — the lecture flags the Binomial distribution as a case where it fails (see below). The
question the lecture poses at exactly this point is the one the rest of the chapter answers: *it is
nice to turn the integrals we care about into Lebesgue integrals — when can we do this?*

## Densities and the Radon–Nikodym derivative

$\lambda$ and $P_Z$ above are closely related — $P_Z$ is built directly from $\lambda$ via $\phi$ —
and the goal now is to make that relationship precise in general.

Given a measurable space $(\mathcal{X}, \mathcal{F})$ and two measures $P, \mu$ on it, $P$ is
**absolutely continuous** with respect to $\mu$, written $P \ll \mu$ (equivalently, $\mu$
**dominates** $P$), if
$$P(A) = 0 \quad \text{whenever} \quad \mu(A) = 0.$$

If $P \ll \mu$, then — under mild conditions — there is always a **density function**
$p : \mathcal{X} \to [0,\infty)$ such that
$$P(A) = \int_A p(x)\, d\mu(x), \qquad \text{and more generally} \qquad \int f(x)\, dP(x) = \int f(x)\, p(x)\, d\mu(x).$$
This $p$ is sometimes written $p(x) = \dfrac{dP}{d\mu}(x)$ and called the **Radon–Nikodym
derivative** of $P$ with respect to $\mu$.

Densities are useful precisely because they turn an integral $\int f\, dP$ that we may not know how
to evaluate directly into one we do:

1. If $\mathcal{X} \subseteq \mathbb{R}^n$ is continuous, $\int f\, dP = \int_{\mathcal{X}} f(x)\, p(x)\, dx$
   — an ordinary integral against Lebesgue measure, and $p$ is called a **probability density
   function (pdf)**.
2. If $\mathcal{X}$ is countable, $\int f\, dP = \sum_{x \in \mathcal{X}} f(x)\, p(x)$ — an ordinary
   sum against counting measure, and $p$ is called a **probability mass function (pmf)**.

Distributions are routinely *defined* by giving their density with respect to some known measure.
For example, $\mathrm{Binom}(n,\theta)$ has pmf
$$p(x) = \binom{n}{x}\, \theta^x (1-\theta)^{n-x}, \qquad x = 0, \dots, n,$$
which is a density with respect to counting measure on $\mathcal{X} = \{0, \dots, n\}$. This is
exactly the case where the "turn it into a Lebesgue integral" trick from the previous section
fails: the Binomial has **no** density with respect to Lebesgue measure, because
$$\int_{\{0,\dots,n\}} p(x)\, dx = 0 \qquad \text{for any function } p,$$
a finite set having Lebesgue measure zero. A discrete distribution is simply not absolutely
continuous with respect to Lebesgue measure — it needs counting measure underneath it instead.

## Probability spaces and random variables

The measure-theoretic setup for probability keeps a strict separation between an abstract source of
randomness and the quantities computed from it. Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a
**probability space**: $\omega \in \Omega$ is called an **outcome**, $A \in \mathcal{F}$ an
**event**, and $\mathbb{P}(A)$ the **probability of $A$**.

A **random variable** is simply a function $X : \Omega \to \mathcal{X}$. Saying $X$ has
distribution $Q$, written $X \sim Q$, means
$$\mathbb{P}(X \in B) = \mathbb{P}(\{\omega : X(\omega) \in B\}) = Q(B);$$
$Q$ is the measure on $\mathcal{X}$ obtained by pushing $\mathbb{P}$ forward along $X$. The same
idea extends to events built from several random variables at once, e.g.
$$\mathbb{P}(X > Y > Z \ge 0) = \mathbb{P}(\{\omega : X(\omega) > Y(\omega) > Z(\omega) \ge 0\}),$$
and **expectation** is itself an integral with respect to $\mathbb{P}$:
$$\mathbb{E}[f(X,Y)] = \int_{\Omega} f(X(\omega), Y(\omega))\, d\mathbb{P}(\omega).$$

This is where the earlier machinery earns its keep: to do an actual calculation, an integral or
probability stated over the abstract space $\Omega$ must eventually be boiled down to a concrete
integral or sum over $\mathcal{X}$ — which is exactly what rewriting $\int f\, dP_X$ via a density
$p = dP_X/d\mu$ against a known measure $\mu$ (counting or Lebesgue) accomplishes.

One further piece of vocabulary: if $\mathbb{P}(A) = 1$, $A$ is said to occur **almost surely**.

## Sources

- Berkeley Stat 210A, Fall 2024, Lecture 1 (8/24/2023 per the slide date), handwritten notes,
  reconstructed pages: `01-measure-theory-basics.md` — measures, $\sigma$-fields, the counting/
  Lebesgue/Gaussian examples, and the construction of the integral from indicators through simple
  functions to general measurable functions.
- Same lecture, `02-densities.md` — absolute continuity, the Radon–Nikodym derivative, the pdf/pmf
  split, the Binomial counterexample, and the probability-space/random-variable formalism.
- Both source files are model reconstructions of a handwritten PDF with no text layer; their own
  banners flag the prose as paraphrase in places and every equation as unverified against the
  original scan.
- The lecture points to material it does not itself contain: Pset 0 (on why measure theory
  clarifies integration and conditioning), HW 0 Problem 3 (on the pathological subsets of
  $\mathbb{R}^n$ to which Lebesgue measure cannot be extended), Keener Chapter 1, and Stat 205A,
  where the measure-theoretic development continues in full.

---

[← 23. Measures, Integration, and Densities](23-measures-integration-and-densities.md) · [Contents](index.md) · [25. Induction and the Coin-Flip Example →](25-induction-and-the-coin-flip-example.md)
