---
title: "70. Measure-Theoretic Foundations of Probability"
course: "Berkeley Stat 210A"
chapter: 70
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 70. Measure-Theoretic Foundations of Probability

## What this covers

This chapter answers a question that sits underneath every probability calculation: what,
formally, *is* a probability? It surveys the two informal answers — frequentist and Bayesian — and
then gives the mathematical answer both frameworks share: a probability is a measure. From there it
builds just enough measure theory to make that definition usable — $\sigma$-fields, measures,
integrals, densities, random variables, and a first patch of conditional expectation — assuming
only comfort with basic set operations, countable versus uncountable sets, and the calculus
(Riemann) integral. None of this is meant to make you a measure theorist; the goal is the
vocabulary and the unifying viewpoint, not the technical fine print, which belongs to a dedicated
measure-theoretic probability course.

## Two everyday answers, and where they strain

There are two common informal answers to "what is a probability?":

- **Frequentist:** probability is the relative frequency of an outcome across (imagined) repeated
  trials of an experiment.
- **Bayesian:** probability is a degree of belief that something is true, or that something will
  happen.

Frequentists tend to doubt that every question can be given a meaningful probability — there is no
sense in which the next presidential election is a repeatable experiment. It is worth lining up
examples in decreasing order of how comfortable it feels to assign them a number, and noticing
where your own agreement runs out:

1. **A symmetric die rolling a 4.** Nearly everyone agrees on $1/6$, whether because they imagine
   many repeated tosses, believe the die has an equal physical propensity for each face, or simply
   feel no reason to favor one face over another.
2. **A radiation treatment succeeding for a given patient.** You could use the success rate among
   similar patients, but choosing "similar" is already a judgment call — cancer stage, age, family
   history, the tumor's genetic profile. Condition on enough of these and the patient may be the
   only member left in their own comparison class.
3. **The Democratic candidate winning the next election.** Every election has its own unprecedented
   features, so there is no obvious reference class of repetitions to fall back on at all.
4. **A subatomic particle having the mass predicted by some theory.** This is not the probability
   that something *will happen* — it is a probability that something *is or was already true*
   about the world, and has been so since the creation of the universe.
5. **Whether $P = NP$.** A purely mathematical question with a determinate answer, one that may or
   may not be resolved in our lifetimes.
6. **The 20th digit of $\sqrt{2}$ being $5$.** You could work this out yourself with pencil and
   paper in a few minutes, with no new data about the world — it seems perverse to call it
   "random." Yet if forced to bet without time to compute it, you might still say $10\%$.

These roughly track the frequentist/Bayesian divide: Bayesians get a lot of mileage from being
willing to assign probabilities all the way down this list, while frequentists are more
conservative and would rather leave some of these quantities simply unknown. Fifty years ago
statisticians were often dogmatic about which framework was correct; today the mainstream view is
that the choice between them is pragmatic, made case by case.

## The mathematical answer

The good news is that this whole dispute is about *when and how* to attach a probability to a
question about the world — it is not a disagreement about the mathematical object itself. There is
very little controversy about how to formalize probability mathematically:

> **Mathematical answer.** A probability is a measure $P$ on a sample space $\mathcal{X}$ that
> assigns total measure $1$ to the sample space.

Measure theory — the branch of mathematics concerned with measuring the "size" of subsets of a set
— was developed in the early twentieth century, and Kolmogorov soon realized it could put
probability on a rigorous footing, resolving several paradoxes that dogged informal treatments of
probability (the Bertrand paradox is the standard example; David Aldous gives a historical account
of Kolmogorov's contribution). This is not a course in measure-theoretic probability, and nothing
below is developed with full rigor — but the framework is worth borrowing because it clarifies what
conditioning means and, usefully for this course, lets a single notion of "density" cover
probability mass functions, probability density functions, discrete–continuous mixtures, and even
random variables on more exotic spaces (random graphs, manifolds) all at once.

## Measures and $\sigma$-fields

Given a set $\mathcal{X}$, a **measure** $\mu$ maps (non-pathological) subsets $A \subseteq
\mathcal{X}$ to non-negative numbers $\mu(A) \in [0,\infty]$. Three examples fix the idea before the
formal definition:

- **Counting measure.** If $\mathcal{X}$ is countable, e.g. $\mathcal{X} = \mathbb{Z}$, the counting
  measure $\#(A)$ just counts the points of $A$: $\#(\{0,1\}) = 2$ and
  $\#(\{2,4,6,8,\ldots\}) = \infty$.
- **Lebesgue measure.** If $\mathcal{X} = \mathbb{R}^n$, the Lebesgue measure $\lambda(A)$ returns
  the volume of $A$, informally $\lambda(A) = \int \cdots \int_A dx_1 \cdots dx_n$.
- **Gaussian measure.** On $\mathcal{X} = \mathbb{R}$, define the "size" of $A$ as the probability
  that a standard Gaussian $Z \sim \mathcal{N}(0,1)$ lands in $A$:
$$
P_Z(A) = \mathbb{P}(Z \in A) = \int_A \phi(x)\, dx, \qquad \phi(x) = \frac{1}{\sqrt{2\pi}}
e^{-x^2/2}.
$$

Not every subset can be sensibly measured. Some sets are pathological enough to be genuinely
**non-measurable**, and part of the point of measure theory is excluding them cleanly (constructing
one is a homework exercise; you would not stumble on one by accident). So a measure's domain is
usually not the full power set $2^{\mathcal{X}}$ but a restricted collection
$\mathcal{F} \subseteq 2^{\mathcal{X}}$ of "nice enough" sets, called a **$\sigma$-field** (or
**$\sigma$-algebra**):

1. $\mathcal{X} \in \mathcal{F}$.
2. $\mathcal{F}$ is closed under complementation: $A \in \mathcal{F} \implies \mathcal{X}\setminus A
   \in \mathcal{F}$.
3. $\mathcal{F}$ is closed under countable unions: $A_1, A_2, \ldots \in \mathcal{F} \implies
   \bigcup_i A_i \in \mathcal{F}$.

Exactly which sets satisfy this does not matter for this course. Two examples: if $\mathcal{X}$ is
countable, $\mathcal{F}$ is usually the whole power set; if $\mathcal{X} = \mathbb{R}^n$,
$\mathcal{F}$ is usually the **Borel $\sigma$-field** $\mathcal{B}$, the smallest $\sigma$-field
containing every open rectangle $(a_1,b_1)\times \cdots \times (a_n,b_n)$ — start from the
rectangles and close them off under the three properties above, and what results can be thought of,
informally, as all the non-pathological subsets of $\mathbb{R}^n$.

A set $\mathcal{X}$ together with a $\sigma$-field $\mathcal{F}$ on it is a **measurable space**. On
such a space, a **measure** is a function $\mu: \mathcal{F} \to [0,\infty]$ satisfying:

1. **Non-negativity:** $\mu(A) \geq 0$ for all $A \in \mathcal{F}$.
2. **Countable additivity:** if $A_1, A_2, \ldots \in \mathcal{F}$ are pairwise disjoint, then
   $\mu\left(\bigcup_i A_i\right) = \sum_i \mu(A_i)$.
3. $\mu(\emptyset) = 0$ — redundant if $\mu(\mathcal{X})$ is finite, but needed otherwise to rule
   out assigning infinite measure to every set, including the empty one.

$(\mathcal{X}, \mathcal{F}, \mu)$ is then a **measure space**. When $\mu(\mathcal{X}) = 1$, $\mu$ is
a **probability measure** and $(\mathcal{X}, \mathcal{F}, \mu)$ is a **probability space**.

### Push-forward measures

Given a measure space $(\mathcal{X}, \mathcal{F}, \mu)$ and a (nice enough) function
$f: \mathcal{X} \to \mathcal{Y}$, define a new measure $\nu$ on $\mathcal{Y}$ by
$\nu(B) = \mu(f^{-1}(B))$ — the amount of $\mu$-measure that $f$ maps into $B$; more compactly,
$\nu = \mu \circ f^{-1}$. This **push-forward measure** is exactly how the distribution of a
function of a random variable arises: if $Y = \max\{0, Z\}$ for $Z \sim \mathcal{N}(0,1)$, then
$Y$'s distribution $P_Y$ is the push-forward of $P_Z$ through $f(z) = \max\{0,z\}$.

## Building the integral

A measure $\mu$ on $(\mathcal{X}, \mathcal{F})$ lets us define an integral $\int f\, d\mu$ of a
(nice enough) real-valued $f$, weighted so that each set $A$ carries total weight $\mu(A)$. The
construction goes in stages, each forced by wanting the integral to be linear:

1. For an indicator function $1_A(x) = 1\{x \in A\}$ with $A \in \mathcal{F}$: $\int 1_A\, d\mu =
   \mu(A)$.
2. For a **simple function** $f(x) = \sum_i c_i 1_{A_i}(x)$ with $c_i \geq 0$ and $A_i \in
   \mathcal{F}$, linearity forces $\int f\, d\mu = \sum_i c_i \mu(A_i)$.
3. For a general non-negative $f$, approximate it from below by a sequence of simple functions and
   take the limit: $\int f\, d\mu = \lim_n \int f_n\, d\mu$. One natural choice inscribes a
   "ziggurat" of vertical steps of size $2^{-n}$ beneath $f$:
$$
f_n(x) = 2^{-n}\lfloor 2^n f(x)\rfloor = \sum_{k=0}^\infty k2^{-n} 1_{A_{n,k}}(x), \qquad
A_{n,k} = \left\{x : f(x) \in \left[k2^{-n}, (k+1)2^{-n}\right)\right\}.
$$
4. For a general (signed) $f$, split it into positive and negative parts $f = f^+ - f^-$ with
   $f^+ = \max\{f,0\}$ and $f^- = \max\{-f,0\}$, each of which has a well-defined non-negative
   integral by step 3, and set
$$
\int f\, d\mu = \int f^+\, d\mu - \int f^-\, d\mu \in [-\infty,\infty],
$$
   undefined only if both pieces are infinite.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="A bump-shaped function with a staircase of simple functions approximating it from below">
  <line x1="30" y1="170" x2="290" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <polygon points="70,170 70,155 100,155 100,120 130,120 130,68 170,68 170,120 200,120 200,155 230,155 230,170" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <polyline points="40,165 90,140 120,70 150,50 180,70 210,140 260,165" fill="none" stroke="currentColor" stroke-width="1.75"/>
  <text x="278" y="185" font-size="12" fill="currentColor">x</text>
  <text x="150" y="30" text-anchor="middle" font-size="12" fill="currentColor">f</text>
  <text x="233" y="150" font-size="11" fill="currentColor">fₙ</text>
</svg>
<figcaption>Building the integral: the curve is $f$; the staircase is the simple function $f_n$,
constant at height $k2^{-n}$ on the level set $A_{n,k}$. Refining the staircase as $n \to \infty$
makes the shaded area converge to $\int f\, d\mu$.</figcaption>
</figure>

This leaves out real technical work — exactly which functions can be approximated this way — but
the upshot is what matters: every measure $\mu$ comes with a well-behaved integral $\int \cdot\,
d\mu$. Returning to the three measures above:

- **Counting measure:** $\int f\, d\# = \sum_{x \in \mathcal{X}} f(x)$ — integration is just
  summation.
- **Lebesgue measure:** $\int f\, d\lambda = \int \cdots \int f(x)\, dx_1 \cdots dx_n$, the ordinary
  calculus integral. The Lebesgue integral agrees with the Riemann integral whenever the latter is
  defined, but is also defined for functions the Riemann integral cannot handle — for instance
  $f(x) = 1\{x \in \mathbb{Q}\}$, whose Lebesgue integral is $\lambda(\mathbb{Q}) = 0$ (since
  $\mathbb{Q}$ is countable), while its Riemann integral does not exist. (**Exercise, posed in the
  source:** what is the Lebesgue integral of $1\{x \in \mathbb{Q}\}$?)
- **Gaussian measure:** since $P_Z(A)$ is by definition the Lebesgue integral of $1_A(x)\phi(x)$,
  integrating against $P_Z$ in general means integrating against $\phi$:
$$
\int f\, dP_Z = \int_{-\infty}^\infty f(x)\phi(x)\, dx = \mathbb{E}[f(Z)].
$$
  An integral against a probability measure is exactly an expectation.

## Densities and the Radon–Nikodym derivative

The Gaussian example above is an instance of something more general: it lets us turn a
$P_Z$-integral into a Lebesgue integral, and it would be nice not to reinvent every piece of
calculus machinery for every new measure. But this trick is not always available — if $Y$ is
binomial, $P_Y(A) = \mathbb{P}(Y \in A)$ is a perfectly good probability measure, yet there is no
function playing the role $\phi$ played for the Gaussian.

Formally: given two measures $P$ and $\mu$ on $(\mathcal{X}, \mathcal{F})$, $P$ is **absolutely
continuous with respect to** $\mu$, written $P \ll \mu$, if $\mu(A) = 0 \implies P(A) = 0$. When
$P \ll \mu$, the Radon–Nikodym theorem guarantees, under mild conditions, a **density function**
$p: \mathcal{X} \to [0,\infty)$ with
$$
P(A) = \int 1_A(x) p(x)\, d\mu(x) \quad \text{for all } A \in \mathcal{F},
$$
and hence $\int f\, dP = \int f(x) p(x)\, d\mu(x)$ for any $f$ — a $P$-integral becomes a
$\mu$-integral by multiplying the density into the integrand. $p$ is also called the
**Radon–Nikodym derivative** of $P$ with respect to $\mu$, written suggestively as
$\frac{dP}{d\mu}$.

Left unqualified, "$P$ is absolutely continuous" means $P \ll \lambda$ (Lebesgue measure). When
$\mu = \lambda$, $p$ is the ordinary probability density function; when $\mu$ is counting measure,
$p$ is the probability mass function — one notion, two familiar names, depending only on which
measure sits underneath.

## Probability spaces and random variables

A typical statistics problem juggles several random variables at once — some discrete, some
continuous, some functions of the others — and needs workable notation for statements like
$\mathbb{P}(X^2 < (Y+Z)/W)$ or $\mathbb{E}[(XY - ZW)^2]$. In principle this is just a measure or an
integral: if $P$ is the joint distribution of $(X,Y,Z,W)$, the first expression is $P$ evaluated on
$\{(x,y,z,w) : x^2 < (y+z)/w\}$, and the second is $\int (xy-zw)^2\, dP(x,y,z,w)$. But writing this
out explicitly every time is unwieldy.

Instead, introduce an abstract outcome $\omega$ in an **outcome space** $\Omega$ — informally, all
the information needed to evaluate every random variable in the problem. A **random variable** is
then just a function of $\omega$; $\mathbb{P}$ is a measure on $\Omega$, and $\mathbb{E}$ is the
corresponding integral, so that
$$
\mathbb{P}(X^2 < (Y+Z)/W) = \mathbb{P}\big(\{\omega \in \Omega : X(\omega)^2 < (Y(\omega)+Z(\omega))
/W(\omega)\}\big),
$$
$$
\mathbb{E}[(XY-ZW)^2] = \int_\Omega \big(X(\omega)Y(\omega) - Z(\omega)W(\omega)\big)^2\,
d\mathbb{P}(\omega),
$$
without ever having to say what kind of object $\omega$ actually is. A subset of $\Omega$ that
$\mathbb{P}$ assigns a probability to is an **event**; if $\mathbb{P}(A) = 1$, $A$ occurs **almost
surely**.

In practice, calculations use the **distribution** of a random variable — the push-forward measure
$Q = \mathbb{P} \circ X^{-1}$ — rather than $\omega$ itself. $\omega$ does its job just by existing:
it is the scaffolding that lets $\mathbb{P}$ and $\mathbb{E}$ be a genuine measure and integral, and
it is never mentioned again once the distributions of the actual random variables in a problem are
pinned down.

## Conditional probability, informally patched

For events $A, B$ with $\mathbb{P}(B) > 0$, conditional probability is unproblematic:
$\mathbb{P}(A \mid B) = \mathbb{P}(A \cap B)/\mathbb{P}(B)$. This breaks down exactly when
$\mathbb{P}(B) = 0$ — and it is not just a technicality to wave away: conditioning on a measure-zero
event is genuinely ambiguous (a homework problem illustrates this directly), because there is no
canonical way to resolve the ratio $0/0$ that a naive limiting argument can be trusted to respect.

Yet this is exactly the situation whenever $X$ is continuous and we want to talk about $Y$'s
distribution or expectation given $X = x$: the event $\{X = x\}$ has probability zero. Measure
theory patches this by defining the **conditional expectation** $\mathbb{E}(Y \mid X)$ not
pointwise but all at once, as a random variable $g(X)$ characterized by the defining property
$$
\mathbb{E}[(Y - g(X))1_A(X)] = 0 \quad \text{for every (nice) set } A.
$$
Evaluating $g$ at a particular $x$ then answers the informal question "what do we expect $Y$ to be,
given $X = x$?" — but this is only a sketch of the idea, not a construction; existence, uniqueness,
and what "nice" means are the subject of a dedicated measure-theoretic probability course (Stat
205A).

Once conditional expectation is defined this way, conditional distributions come for free by
plugging in indicator functions:
$$
\mathbb{P}(Y \in A \mid X) = \mathbb{E}[1_A(Y) \mid X].
$$

This is the hinge for what comes next in the course: the same defining property is what lets
conditioning work uniformly across discrete and continuous random variables, which is the whole
reason for having gone through measure theory in the first place.

## Sources

All material is from the STAT 210A (UC Berkeley) course reader's "Probability" chapter, sections
1–7 — *What is a probability?*, *Probability as a measure*, *Measures*, *Integrals*, *Densities*,
*Probability spaces and random variables*, and *Conditional probability*. The fall-2026 edition was
used as the clearest and most complete (it includes the push-forward-measure section that the
fall-2024 edition omits), converted losslessly from the source `.qmd`:

- `docs/statistics/berkeley/stat210a/fall-2026/reader/probability/01-what-is-a-probability.md`
  through `07-conditional-probability.md` (library repository).

The fall-2024 edition (also `.qmd`, lossless) carries the same text with that one omission and is
otherwise identical; the two fall-2025 editions (`reader/` and `units/reader/`, pandoc-converted
from `.html`) are the same reader duplicated across course offerings and were checked but not drawn
on separately.

Referred to but not contained in the supplied material: the homework problem constructing a
non-measurable/pathological set (§1, §3); the homework problem illustrating the ambiguity of
conditioning on a measure-zero event (§7); the Radon–Nikodym theorem itself, linked externally
rather than proved (§5); David Aldous's historical note connecting Kolmogorov's work to the
Bertrand paradox, linked externally (§2); and Stat 205A, named as the course where conditional
expectation is treated rigorously (§7). The diagram above redraws, as a static figure, an idea the
source illustrates with an interactive plot ("as illustrated in the picture below," §4).

---

[← 69. Old Exams Archive](69-old-exams-archive.md) · [Contents](index.md) · [71. Recitation Materials Index →](71-recitation-materials-index.md)
