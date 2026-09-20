---
title: "66. Measure Theory for Probability"
course: "Berkeley Stat 210A Fall 2024"
chapter: 66
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 66. Measure Theory for Probability

## What this covers

This chapter collects the minimal vocabulary of measure theory that the rest of the course leans
on: what a measure is, how it lets you build an integral, how a *density* lets you trade one
measure's integral for another's, and how "abstract" probability spaces and random variables let
you talk about many random quantities — some discrete, some continuous, some functions of the
others — without constantly renegotiating what an event or a probability even is. It assumes
ordinary calculus and the elementary (non-measure-theoretic) probability of an undergraduate
course; it deliberately does not develop measure theory as a subject in its own right, and says so
at several points along the way.

## Why bother with measures

Measure theory is, at bottom, about assigning a consistent notion of "size" to subsets of a set.
It was developed in the early twentieth century, and soon afterward Kolmogorov realized that it
gives probability theory a rigorous foundation, resolving a number of long-standing paradoxes about
what a probability even is. This course does not develop measure-theoretic probability properly
(that is Stat 205A); the point of borrowing its language here is to simplify notation and make
later ideas about integration and conditioning precise enough to state carefully.

The need for this care is not mere fussiness. It is not even possible to define a sensible "volume"
for *every* subset of $\mathbb{R}$: using the axiom of choice, one can construct pathological,
*non-measurable* sets to which no volume can be consistently assigned. One of the original
motivations for measure theory was exactly to rule these pathological sets out of consideration,
and to define integration rigorously over the sets that remain.

## Measures and $\sigma$-fields

Let $\mathcal{X}$ be a set. A **measure** $\mu$ is a function assigning to "nice enough" subsets
$A \subseteq \mathcal{X}$ a non-negative number $\mu(A) \in [0,\infty]$, meant to capture the size
of $A$. Three examples recur through the chapter:

- **Counting measure.** If $\mathcal{X}$ is countable (e.g. $\mathcal{X} = \mathbb{Z}$), the
  *counting measure* $\#(A)$ just counts the points of $A$: $\#(\{0,1\}) = 2$ and
  $\#(\{2,4,6,\dots\}) = \infty$.
- **Lebesgue measure.** If $\mathcal{X} = \mathbb{R}^n$, the *Lebesgue measure* $\lambda(A)$ is the
  ordinary volume of $A$,
  $$
  \lambda(A) = \int\cdots\int_A dx_1\,dx_2\cdots dx_n.
  $$
- **Gaussian measure.** If $\mathcal{X} = \mathbb{R}$, we might instead measure a set by the
  probability that a standard Gaussian $Z \sim \mathcal{N}(0,1)$ lands in it:
  $$
  P_Z(A) = \mathbb{P}(Z \in A) = \int_A \phi(x)\,dx, \qquad \phi(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}.
  $$

The non-measurable-set example shows that the right-hand sides of the last two displays cannot be
made sense of for *every* subset $A$. So a measure is not defined on the full power set
$2^{\mathcal{X}}$ of all subsets, but on a restricted collection $\mathcal{F} \subseteq 2^{\mathcal{X}}$
of "nice" subsets. For the restriction to behave sensibly — so that the operations you actually
want to perform on events (complementing them, taking countable unions) keep you inside the
collection — $\mathcal{F}$ is required to be a **$\sigma$-field** (or $\sigma$-algebra):

1. $\mathcal{X} \in \mathcal{F}$.
2. If $A \in \mathcal{F}$ then $\mathcal{X} \setminus A \in \mathcal{F}$ ($\mathcal{F}$ is closed
   under complementation).
3. If $A_1, A_2, \dots \in \mathcal{F}$ then $\bigcup_{i=1}^\infty A_i \in \mathcal{F}$
   ($\mathcal{F}$ is closed under countable unions).

The details of this definition don't matter much for this course; what matters is that it exists
and rules out pathological sets. If $\mathcal{X}$ is countable, we can simply take $\mathcal{F}$ to
be the entire power set. If $\mathcal{X} = \mathbb{R}^n$, we use the **Borel $\sigma$-field**
$\mathcal{B}$: the smallest $\sigma$-field containing every open rectangle
$(a_1,b_1) \times \cdots \times (a_n,b_n)$. Starting from the open rectangles and closing under
complements and countable unions produces a very large collection — informally, "all the
non-pathological subsets of $\mathbb{R}^n$."

A set $\mathcal{X}$ together with a $\sigma$-field $\mathcal{F}$ is a **measurable space**
$(\mathcal{X}, \mathcal{F})$. A **measure** on $(\mathcal{X},\mathcal{F})$ is a function
$\mu: \mathcal{F} \to \mathbb{R}$ satisfying:

1. **Non-negativity:** $\mu(A) \geq 0$ for all $A \in \mathcal{F}$.
2. $\mu(\emptyset) = 0$.
3. **Countable additivity:** if $A_1, A_2, \dots \in \mathcal{F}$ are pairwise disjoint, then
   $$
   \mu\Big(\bigcup_{i=1}^\infty A_i\Big) = \sum_{i=1}^\infty \mu(A_i).
   $$

The triple $(\mathcal{X},\mathcal{F},\mu)$ is a **measure space**. When $\mu(\mathcal{X}) = 1$,
$\mu$ is a **probability measure** and $(\mathcal{X}, \mathcal{F}, \mu)$ is a **probability space**.

## Building the integral

The payoff of having a measure is that it lets you integrate functions against it: $\int f\,d\mu$
is meant to weight the value of $f$ at each point by how much "size" $\mu$ assigns nearby. The
construction proceeds in stages, each extending the last by linearity or by a limit.

**Indicators.** For an indicator $1_A(x) = 1\{x \in A\}$ of a set $A \in \mathcal{F}$, the only
sensible definition is $\int 1_A\,d\mu = \mu(A)$. This is exactly why the integral is only defined
for functions built out of sets in $\mathcal{F}$ — asking for the integral of $1_A$ with
$A \notin \mathcal{F}$ makes no more sense than asking for $\mu(A)$ itself.

**Simple functions.** A *simple function* is a non-negative combination of indicators,
$f(x) = \sum_i c_i 1_{A_i}(x)$ with $c_i \geq 0$, $A_i \in \mathcal{F}$. Linearity forces
$$
\int f\,d\mu = \sum_i c_i \int 1_{A_i}\,d\mu = \sum_i c_i\, \mu(A_i).
$$

**Non-negative functions.** A general non-negative $f$ is approximated from below by an increasing
sequence of simple functions $f_1 \leq f_2 \leq \cdots \leq f$, and
$$
\int f\,d\mu = \lim_{i\to\infty} \int f_i\, d\mu.
$$

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="A nonnegative function approximated from below by increasingly fine step functions">
  <line x1="30" y1="180" x2="315" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="180" x2="30" y2="15" stroke="currentColor" stroke-width="1.5"/>
  <text x="312" y="195" text-anchor="middle" font-size="12" fill="currentColor">x</text>
  <text x="18" y="20" text-anchor="middle" font-size="12" fill="currentColor">f</text>
  <rect x="40" y="170" width="40" height="10" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="0.75"/>
  <rect x="80" y="95" width="40" height="85" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="0.75"/>
  <rect x="120" y="55" width="40" height="125" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="0.75"/>
  <rect x="160" y="62" width="40" height="118" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="0.75"/>
  <rect x="200" y="102" width="40" height="78" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="0.75"/>
  <rect x="240" y="148" width="40" height="32" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="0.75"/>
  <rect x="280" y="165" width="20" height="15" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="0.75"/>
  <path d="M40,170 H60 V130 H80 V95 H100 V70 H120 V55 H140 V47 H160 V50 H180 V62 H200 V80 H220 V102 H240 V125 H260 V148 H280 V165 H300" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
  <polyline points="40,170 60,130 80,95 100,70 120,55 140,47 160,45 180,50 200,62 220,80 240,102 260,125 280,148 300,165" fill="none" stroke="currentColor" stroke-width="2"/>
</svg>
<figcaption>A nonnegative function $f$ (solid curve), a coarse simple function below it (shaded
rectangles, of total area $\sum_i c_i\mu(A_i)$), and a finer simple function (dashed staircase)
closer still to $f$. Taking the limit of $\int f_i\,d\mu$ over ever-finer such approximations
defines $\int f\,d\mu$.</figcaption>
</figure>

**General functions.** Write $f = f^+ - f^-$ with $f^+(x) = \max\{f(x),0\}$ and
$f^-(x) = \max\{-f(x),0\}$, both non-negative, and set
$$
\int f\,d\mu = \int f^+\,d\mu - \int f^-\,d\mu \in [-\infty,\infty],
$$
leaving the integral undefined if both terms are infinite.

Several technical questions are glossed over here — which functions are "nice enough" to be
approximated by simple functions, and in what sense the limit in the second step doesn't depend on
the approximating sequence chosen — and none of them matter for this course. What matters is that
every measure $\mu$ comes with a well-defined integral $\int \cdot\, d\mu$ that behaves the way you
would want it to.

Returning to the three running examples:

- **Counting measure:** $\int f\,d\# = \sum_{x \in \mathcal{X}} f(x)$ — the integral is just a sum.
- **Lebesgue measure:** $\int f\, d\lambda = \int\cdots\int f(x)\,dx_1\cdots dx_n$, the ordinary
  (multivariable) integral from calculus. This *Lebesgue integral* extends the Riemann integral:
  wherever the Riemann integral of $f$ exists, the Lebesgue integral exists and agrees with it, but
  the Lebesgue integral is also defined for functions like $f(x) = 1\{x \in \mathbb{Q}\}$, whose
  Riemann integral does not exist.
- **Gaussian measure:** $P_Z(A)$ was itself defined as $\int 1_A(x)\phi(x)\,dx$, so by the same
  extension the integral of $f$ against $P_Z$ is the Lebesgue integral of $f(x)\phi(x)$ — which is
  nothing but the expectation of $f(Z)$:
  $$
  \int f\,dP_Z = \int_{-\infty}^\infty f(x)\phi(x)\,dx = \mathbb{E}[f(Z)].
  $$

## Densities: moving between measures

The Gaussian example above is a special case of something worth naming: it let us turn an integral
against $P_Z$ into an integral against $\lambda$, just by multiplying by $\phi$. This is valuable
because a great deal of mathematical effort has already gone into computing Lebesgue integrals —
most expectations in statistics are integrals against some joint probability measure, and it would
be wasteful to reinvent integration from scratch for every new distribution.

This trick doesn't always work. If $Y$ is binomial, $P_Y(A) = \mathbb{P}(Y \in A)$ is a perfectly
good measure, but there is no function playing the role of $\phi$ that turns $P_Y$-integrals into
Lebesgue integrals — a discrete measure cannot be captured by a Lebesgue density.

Formally: given two measures $P$ and $\mu$ on the same measurable space $(\mathcal{X}, \mathcal{F})$,
say $P$ is **absolutely continuous with respect to** $\mu$, written $P \ll \mu$, if $P(A) = 0$
whenever $\mu(A) = 0$. Under mild conditions (the Radon–Nikodym theorem), $P \ll \mu$ guarantees a
**density function** $p: \mathcal{X} \to [0,\infty)$ exists such that
$$
P(A) = \int 1_A(x)\, p(x)\, d\mu(x) \quad \text{for all } A \in \mathcal{F},
$$
and, extending in the usual way, $\int f\,dP = \int f(x)\,p(x)\,d\mu(x)$ for any $f$. The function
$p$ is also called the **Radon–Nikodym derivative** of $P$ with respect to $\mu$, sometimes written
suggestively as $\frac{dP}{d\mu}(x)$: once you have it, any integral against $P$ becomes an integral
against $\mu$ with the integrand multiplied by $p$.

Two conventions worth fixing: if no reference measure is named, $\mu$ is taken to be Lebesgue
measure — so "$P$ is absolutely continuous" unqualified means $P \ll \lambda$. And when $P$ is a
probability measure, $p$ is called its **probability density function** (pdf) if $\mu = \lambda$,
or its **probability mass function** (pmf) if $\mu$ is counting measure.

## Probability spaces and random variables

A typical statistics problem involves many random variables of assorted types — some discrete,
some continuous, some functions of others — with their joint distribution specified implicitly, by
describing how they relate to one another or how they are generated in sequence. Questions about
them are questions about functions of several variables at once: in a variance-estimation problem
with i.i.d. $X_1,\dots,X_n$, for instance, you might want
$$
\mathbb{P}\left(\left|\frac{1}{n-1}\sum_{i=1}^n (X_i - \bar X)^2 - \sigma^2\right| < \delta\right).
$$
Phrasing this directly in terms of a measure on the joint distribution of $(X_1,\dots,X_n)$ means
translating the event into a set of vectors satisfying it — workable here, but increasingly awkward
as the setup grows more complicated.

The standard fix is to stop working directly with the measure on the variables of interest, and
instead imagine all of them as functions of one abstract "outcome" $\omega$ that carries all the
randomness in the problem. This gives an abstract **probability space** $(\Omega, \mathcal{F},
\mathbb{P})$, where $\omega \in \Omega$ is an **outcome**, $A \in \mathcal{F}$ is an **event**, and
$\mathbb{P}(A)$ is the **probability of** $A$. A **random variable** is then any (nice enough)
function $X: \Omega \to \mathcal{X}$. We say $X$ has **distribution** $P$, written $X \sim P$, if
$$
\mathbb{P}(X \in B) = \mathbb{P}(\{\omega : X(\omega) \in B\}) = P(B)
$$
for all relevant $B$. A real-valued random variable is **continuous** if its distribution is
absolutely continuous with respect to Lebesgue measure. If $X$ is a random variable, so is $f(X)$
for any nice enough $f$.

Expectation, correspondingly, is defined as an integral over the outcome space:
$$
\mathbb{E}[X] = \int X(\omega)\, d\mathbb{P}(\omega), \qquad
\mathbb{E}[f(X,Y)] = \int f(X(\omega), Y(\omega))\, d\mathbb{P}(\omega).
$$
In practice, actual calculations will always reduce $\mathbb{P}$ or $\mathbb{E}$ to a composition of
ordinary sums and integrals — the abstract outcome space is bookkeeping, not something you compute
with directly.

## Conditioning, informally

Measure theory also lets you patch the definition of conditional probability, though doing this
properly is beyond the scope of this course. If $\mathbb{P}(B) > 0$, the ordinary definition
$$
\mathbb{P}(A \mid B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}
$$
is unproblematic — but it breaks down exactly when $\mathbb{P}(B) = 0$, and there is in general no
way to repair it for an individual measure-zero event $B$.

The case that matters in practice is different: if $X$ and $Y$ are continuous random variables with
some dependence between them, we still want to talk about the distribution or expectation of $Y$
given that $X$ takes a *specific* value $x$ — even though $\{X = x\}$ has probability zero. The
resolution is to define the **conditional expectation** $\mathbb{E}[Y \mid X]$ not as a number but
as a *random variable* $g(X)$, characterized by the property
$$
\mathbb{E}\big[(Y - g(X))\, 1_A(X)\big] = 0 \quad \text{for every (nice) set } A.
$$
Evaluating $g$ at the value $x$ then answers the original question. This is a genuinely informal
sketch — it skips the existence and uniqueness argument entirely — but it is enough to make sense of
expressions like $\mathbb{E}[Y\mid X]$ that appear later in the course; the honest treatment is in
Stat 205A. Once conditional expectation is defined this way, conditional *probabilities* come along
for free by conditioning indicators: $\mathbb{P}(Y \in A \mid X) = \mathbb{E}[1_A(Y) \mid X]$.

Two more pieces of standard vocabulary, collected here because the source does: an event $A$ with
$\mathbb{P}(A) = 1$ is said to occur **almost surely**, and the variance of a random variable is
$$
\mathrm{Var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2.
$$

## Sources

This chapter merges the "measure theory basics" reader chapter as it appears — essentially
unchanged in substance — across three offerings of Stat 210A (Berkeley):

- **Fall 2025**, `reader/measure-theory-basics/{01-introduction, 02-measures, 03-integrals,
  04-densities, 05-probability-spaces-and-random-variables, 06-conditional-probability}.md` — used
  as the primary text, since its file split lines up most closely with this chapter's sections.
- **Fall 2024**, the same content with the introduction folded into `01-measures.md` rather than
  split out, continuing through `02-integrals.md`–`05-conditional-probability.md`.
- **Fall 2026**, the same content again, at `01-measures.md`–`05-conditional-probability.md`.

(A near-duplicate copy of the fall 2025 files also exists under `fall-2025/units/reader/`, from a
different path in the same course repository; it was not used separately since the text is
identical.)

The diagram illustrating simple-function approximation is redrawn from the description of a
screenshot present in all three versions of the source (the image itself is not reproduced here).
The formula for $\mathrm{Var}(X)$ is stated correctly above; the source text has a typo dropping the
square on the second term.

Referred to by the source but not contained in it, and not reproduced here: **Homework 0**
(`stat.berkeley.edu/~wfithian/courses/stat210a/hw0.pdf`), whose Problem 3 constructs a
non-measurable set via the axiom of choice, and which elsewhere illustrates the ambiguity of
conditioning on a measure-zero event; **Stat 205A**, for the rigorous treatment of conditional
expectation; **Keener, Ch. 1**, for further background on probability; and David Aldous's
historical note on Kolmogorov's axiomatization of probability, linked from the introduction.

---

[← 65. Maximum Likelihood Estimation](65-maximum-likelihood-estimation.md) · [Contents](index.md) · [67. Least Favorable Priors →](67-least-favorable-priors.md)
