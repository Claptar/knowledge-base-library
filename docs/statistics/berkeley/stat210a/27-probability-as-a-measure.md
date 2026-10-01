---
title: "27. Probability as a Measure"
course: "Berkeley Stat 210A"
chapter: 27
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 27. Probability as a Measure

## What this covers

What does it mean, mathematically, for something to have a probability? This chapter gives
Kolmogorov's answer: probability is a special case of a *measure*, and expectation is an integral
against one. It builds up the minimal apparatus needed to say that precisely — measures,
$\sigma$-fields, integration against a measure, densities (the Radon–Nikodym derivative), and the
formal notion of a probability space and a random variable — and shows why this single framework
covers both the discrete case (sums, pmfs) and the continuous case (integrals, pdfs) as two
instances of the same construction. It assumes only ordinary calculus-based probability: you should
already be comfortable with expectations, discrete and continuous random variables, and the idea
that $\int f(x)\,dx$ and $\sum_x f(x)$ both compute an average, without yet having a reason to think
of these as the same operation.

## Two informal answers, and why the mathematics can ignore them

There are two common informal answers to "what is a probability?"

1. **Frequentist**: the relative frequency of an event over many repetitions of an experiment.
2. **Bayesian**: a degree of belief that something is true, or will happen.

These disagree, and the disagreement is sharpest over *which* things can meaningfully be assigned a
probability at all — compare "the probability the die lands on 4" with "the probability $P = NP$"
or "the probability the $20^{\text{th}}$ digit of $\sqrt2$ is 5". A Bayesian is willing to put a
probability on essentially anything; a frequentist tries to restrict probability to things that
could, at least in principle, be repeated. This is a live and genuine controversy.

It is also one the mathematics does not have to settle. Whatever probability *means*, once you have
decided that some collection of statements has probabilities, those probabilities behave in a fixed
way — and it is that behavior, not the interpretation, that the rest of the course works with.

## The mathematical definition, and why it needed revising

**Mathematical definition.** A probability is a function $P$ mapping (some) subsets of a sample
space $\mathcal{X}$ to $[0,1]$, satisfying countable additivity over disjoint sets,
$$P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i) \quad \text{if } A_i \cap A_j = \emptyset \text{ for all } i \ne j,$$
together with $P(\mathcal{X}) = 1$.

This definition was invented to analyze games of chance, and Laplace's classical theory handles the
discrete case — finitely or countably many outcomes — perfectly well. It runs into real trouble once
$\mathcal{X}$ is continuous: some subsets of $\mathbb{R}^n$ are pathological enough that no
consistent probability can be assigned to them, and conditioning on an event of probability zero
(e.g. "given that a continuous random variable equals exactly $3$") has no obvious meaning even
though such conditioning is exactly what a density is for.

Kolmogorov (1933) resolved this by recognizing two things at once:

- probability is a special case of a **measure**, and
- expectation is an **integral** against a probability measure.

Once this identification is made, the discrete and continuous cases stop being two separate
theories glued together and become one theory with two examples.

## Measures and $\sigma$-fields

A **measure** $\mu$ on a set $\mathcal{X}$ assigns to (suitable) subsets $A \subseteq \mathcal{X}$ a
non-negative number $\mu(A) \in [0,\infty]$. Three examples fix the idea:

- **Counting measure**, when $\mathcal{X}$ is countable (e.g. $\mathcal{X} = \mathbb{Z}$):
  $\#(A) = $ the number of points in $A$.
- **Lebesgue measure**, when $\mathcal{X} = \mathbb{R}^n$:
  $\lambda(A) = \int \cdots \int_A dx_1 \cdots dx_n$, i.e. ordinary volume.
- The **standard Gaussian probability measure**: for $Z \sim \mathcal{N}(0,1)$,
$$P_Z(A) = \mathbb{P}(Z \in A) = \int_A \phi(x)\,dx, \qquad \phi(x) = \frac{e^{-x^2/2}}{\sqrt{2\pi}}.$$

The pathological-sets issue mentioned above is exactly why $\lambda(A)$ cannot be defined for *every*
$A \subseteq \mathbb{R}^n$: a measure's domain has to be restricted to a well-behaved collection of
subsets, called a **$\sigma$-field** $\mathcal{F} \subseteq 2^{\mathcal{X}}$. The defining closure
properties are:

1. $\mathcal{X} \in \mathcal{F}$;
2. if $A \in \mathcal{F}$ then $\mathcal{X}\setminus A \in \mathcal{F}$;
3. if $A_1, A_2, \dots \in \mathcal{F}$ then $\bigcup_{i=1}^\infty A_i \in \mathcal{F}$.

The two running examples: if $\mathcal{X}$ is countable, take $\mathcal{F} = 2^{\mathcal{X}}$ (every
subset is fine). If $\mathcal{X} = \mathbb{R}^n$, take $\mathcal{F}$ to be the **Borel
$\sigma$-field** $\mathcal{B}$, the smallest $\sigma$-field containing every open rectangle
$(a_1,b_1)\times\cdots\times(a_n,b_n)$ with $a_i < b_i$ for all $i$. The technical content of
$\sigma$-fields is not the point of this course; what matters is only that a measure needs a
domain, and that domain excludes the pathological sets.

Given a **measurable space** $(\mathcal{X}, \mathcal{F})$, a **measure** is a map
$\mu : \mathcal{F} \to [0,\infty]$ with
$$\mu\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty \mu(A_i) \quad \text{for disjoint } A_1, A_2, \dots \in \mathcal{F}, \qquad \mu(\emptyset) = 0.$$
$\mu$ is a **probability measure** if, additionally, $\mu(\mathcal{X}) = 1$. Compare this to the
definition of $P$ two sections up: it is the same statement, now made precise about which sets it
applies to.

## Integrating against a measure

A measure lets you define an **integral**: it puts weight $\mu(A)$ on the set $A$, so declare
$$\int \mathbf{1}\{x \in A\}\,d\mu(x) = \mu(A),$$
extend to a **simple function** (a finite linear combination of indicators) by linearity,
$$\int \left(\sum_i c_i \,\mathbf{1}\{x \in A_i\}\right) d\mu(x) = \sum_i c_i\,\mu(A_i),$$
and extend to a general measurable function $f$ by approximating it with simple functions and
taking limits. This is exactly the construction of the Lebesgue integral, done relative to an
arbitrary measure rather than only Lebesgue measure.

The three running examples become three familiar operations:

- **Counting measure**: $\int f\,d\# = \sum_{x \in \mathcal{X}} f(x)$ — an ordinary sum.
- **Lebesgue measure**: $\int f\,d\lambda = \int\cdots\int f(x)\,dx_1\cdots dx_n$ — the ordinary
  multivariable integral.
- **Gaussian measure**: since $\int \mathbf{1}_A(x)\,dP_Z(x) = P_Z(A) = \int_{-\infty}^{\infty}
  \mathbf{1}_A\,\phi\,dx$, the same extension gives
$$\int f\,dP_Z = \int f(x)\,\phi(x)\,dx = \mathbb{E}[f(Z)].$$

So $\int f\,dP_Z$, an integral against a probability measure, is evaluated in practice by rewriting
it as $\int f\phi\,dx$, an ordinary Lebesgue integral, using the density $\phi$. This is the move
that makes measure-theoretic probability computable — but it is not always available: for a
Binomial random variable, for instance, there is no such rewriting into a Lebesgue integral. The
natural question is *when* an integral against $P$ can be turned into a Lebesgue integral (or, more
generally, an integral against some other reference measure). That is what a density answers.

## Densities and the Radon–Nikodym derivative

Fix a measurable space $(\mathcal{X}, \mathcal{F})$ and two measures $P$ and $\mu$ on it. Say $P$ is
**absolutely continuous** with respect to $\mu$, written $P \ll \mu$ (or "$\mu$ dominates $P$"), if
$$\mu(A) = 0 \implies P(A) = 0 \quad \text{for every } A \in \mathcal{F}.$$

If $P \ll \mu$ then, under mild conditions, there is always a **density function** $p : \mathcal{X}
\to [0,\infty)$ with
$$P(A) = \int_A p(x)\,d\mu(x), \qquad \int f(x)\,dP(x) = \int f(x)\,p(x)\,d\mu(x).$$
This $p$ is sometimes written $p(x) = \dfrac{dP}{d\mu}(x)$, the **Radon–Nikodym derivative** of $P$
with respect to $\mu$. It is the device that turns $\int f\,dP$ into something computable: an
ordinary integral or sum against the reference measure $\mu$.

The two familiar objects from elementary probability are exactly two special cases of this one
construction:

1. When $\mathcal{X} \subseteq \mathbb{R}^n$ and $\mu = \lambda$ is Lebesgue measure, $p$ is called
   the **probability density function** (pdf), and $\int f\,dP = \int_{\mathcal{X}} f(x)\,p(x)\,dx$.
2. When $\mathcal{X}$ is countable and $\mu = \#$ is counting measure, $p$ is called the
   **probability mass function** (pmf), and $\int f\,dP = \sum_{x \in \mathcal{X}} f(x)\,p(x)$.

A pdf and a pmf are the same kind of object — a Radon–Nikodym derivative — differing only in which
measure is being dominated. Distributions are routinely defined this way, by specifying their
density with respect to some fixed reference measure. For example, $\mathrm{Binom}(n,\theta)$ has
pmf
$$p(x) = \binom{n}{x}\theta^x(1-\theta)^{n-x}, \qquad x = 0, \dots, n,$$
which is its density with respect to counting measure on $\mathcal{X} = \{0, \dots, n\}$.

This distribution has **no** density with respect to Lebesgue measure: since $\{0,\dots,n\}$ has
Lebesgue measure zero, $\int_{\{0,\dots,n\}} p(x)\,dx = 0$ for *any* function $p$, whatever values it
takes. So the discrete/continuous distinction is not just a habit of writing sums instead of
integrals — a discrete distribution genuinely fails to be absolutely continuous with respect to
Lebesgue measure, and needs counting measure (or some other dominating measure) as its reference
instead.

## Probability spaces and random variables

A real problem typically involves many random quantities with complicated relationships to one
another, and it is convenient to build all of them out of one abstract **outcome** $\omega \in
\Omega$, standing for "everything that happens" in one instance of the experiment; every quantity of
interest is then just a function of $\omega$.

A **probability space** is a triple $(\Omega, \mathcal{F}, \mathbb{P})$: $\omega \in \Omega$ is an
outcome, $A \in \mathcal{F}$ is an **event**, and $\mathbb{P}(A)$ is the probability of that event. A
**random variable** is a function $X : \Omega \to \mathcal{X}$. It has **distribution** $Q$, written
$X \sim Q$, if
$$\mathbb{P}(X \in B) = \mathbb{P}(\{\omega : X(\omega) \in B\}) = Q(B) \quad \text{for every relevant } B.$$
$Q$ is called the **push-forward** of $\mathbb{P}$ under $X$: $Q(B) = \mathbb{P}(X^{-1}(B))$. The
construction is general and has nothing special to do with probability — if $\mu$ is any measure on
$\mathcal{X}$ and $f : \mathcal{X} \to \mathcal{Y}$, then $\nu(B) = \mu(f^{-1}(B))$ defines a new
measure $\nu$ on $\mathcal{Y}$.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="A random variable X maps outcomes in Omega to the sample space, pulling an event B back to its preimage in Omega">
  <defs>
    <marker id="arrow44d5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <ellipse cx="100" cy="120" rx="85" ry="90" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <ellipse cx="300" cy="120" rx="85" ry="90" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <ellipse cx="90" cy="130" rx="35" ry="45" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <ellipse cx="300" cy="130" rx="30" ry="40" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="35" y="45" font-size="13" fill="currentColor">&#937;</text>
  <text x="345" y="45" font-size="13" fill="currentColor">&#119964;</text>
  <text x="90" y="133" text-anchor="middle" font-size="12" fill="currentColor">X&#8315;&#185;(B)</text>
  <text x="300" y="133" text-anchor="middle" font-size="12" fill="currentColor">B</text>
  <line x1="190" y1="70" x2="270" y2="70" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow44d5)"/>
  <text x="230" y="58" text-anchor="middle" font-size="12" fill="currentColor">X</text>
</svg>
<figcaption>The random variable X pushes P forward: the distribution Q(B) is defined by pulling B back to its preimage in Ω and reading off P there.</figcaption>
</figure>

This abstraction pays off once several random variables are in play. An event like
$\mathbb{P}(X > Y \ge Z \ge 0)$ is really shorthand for $\mathbb{P}(\{\omega : X(\omega) > Y(\omega)
\ge Z(\omega) \ge 0\})$ — a single event in $\mathcal{F}$, however many random variables it is
stated in terms of. Expectation, correspondingly, is an integral with respect to $\mathbb{P}$ over
$\Omega$:
$$\mathbb{E}[f(X,Y)] = \int_\Omega f(X(\omega), Y(\omega))\,d\mathbb{P}(\omega).$$

None of this abstraction is optional decoration: to actually compute a probability or an
expectation, $\mathbb{P}$ or $\mathbb{E}$ must eventually be boiled down to a concrete sum or
integral, which is exactly the job the density does — rewrite the integral against $\mathbb{P}$ as
an integral against a reference measure via the Radon–Nikodym derivative, then compute.

Finally, one piece of terminology used throughout: if $\mathbb{P}(A) = 1$, the event $A$ is said to
occur **almost surely**.

## Sources

- Handwritten lecture notes, `lecture02-probability.pdf`, reconstructed to markdown across four
  sections — *Probability as a measure*, *Measure theory basics*, *Densities*, and *Probability
  spaces, random variables*. The same lecture appears twice in the supplied material, from Berkeley
  STAT 210A fall 2024 and fall 2025 (identical content in both years); this chapter draws on the
  single underlying lecture rather than repeating it.
  - `docs/statistics/berkeley/stat210a/fall-2024/handwritten/lecture02-probability/01-probability-as-a-measure.md`
    through `04-probability-spaces-random-variables.md`
  - `docs/statistics/berkeley/stat210a/fall-2025/units/handwritten/lecture02-probability/01-probability-as-a-measure.md`
    through `04-probability-spaces-random-variables.md`
- No slide deck, transcript, or problem set was supplied for this lecture, so no `## Exercises`
  section is included.
- The lecture notes are themselves a model reconstruction from a handwritten PDF with no text
  layer, flagged by the source as reconstructed and with every equation unverified against the
  original; this chapter follows their content and organization but the reader should check
  numerical details (e.g. the exact Binomial pmf constant) against a written reference if precision
  matters.
- The lecture points to material it does not itself contain: Keener, *Theoretical Statistics*,
  chapter 1, for a fuller treatment of probability spaces and random variables, and Stat 205A for
  the underlying measure theory in depth.

---

[← 26. Statistical Models and Decision Theory](26-statistical-models-and-decision-theory.md) · [Contents](index.md) · [28. Statistical models and decisions →](28-statistical-models-and-decisions.md)
