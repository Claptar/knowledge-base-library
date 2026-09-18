---
title: "2. Diffusion Limit of Allele Frequencies"
course: "MIT 8.592J"
chapter: 2
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 2. Diffusion Limit of Allele Frequencies

## What this covers

This chapter turns a discrete master equation on a population count $n = 0, 1, \dots, N$ into a
continuous diffusion equation, and then uses that equation to describe how the frequency of an
allele in a population changes under mutation, genetic drift, and selection. It assumes the master
equation itself — the balance of transition rates $R_{mn}$ into and out of a state $n$ — has already
been introduced, together with the one-step (birth–death) process in which $n$ only moves to
$n\pm1$ at a time. The goal is a single equation for the probability density of allele frequency,
and its steady state, which is then used to read off whether a population settles near a fixed
mixture of two alleles or drifts to fixation of one of them.

## From a discrete master equation to a diffusion equation

### The general derivation

Start again from the general master equation for states ordered along a line,

$$\frac{dp_n}{dt} = -\sum_{m \neq n} R_{mn}p_n + \sum_{m \neq n} R_{nm}p_m ,$$

where $R_{mn}$ is the rate of the transition $n \to m$. When the number of states is large and the
probability varies smoothly from one to the next, it is reasonable to pass to a continuum
description: replace the index $n$ by a continuous variable $x$, the probabilities $p_n(t)$ by a
density $p(x,t)$, and the rates $R_{mn}$ by a rate function $R(x'-x, x)$ — the rate of a jump,
starting at $x$, that lands a distance $\Delta = x'-x$ away. Rates of this kind are usually local:
they fall off quickly once $\Delta$ is large.

Relabelling the master equation this way turns the sum into an integral over the continuous jump
size $y$, and bookkeeping the flux into and out of a neighbourhood of $x$ gives

$$\frac{\partial}{\partial t}p(x, t) = \int dy \left[ R(y, x - y)p(x - y) - R(y, x)p(x) \right].$$

The first term is probability flowing in from $x - y$ by a jump of size $y$; the second is
probability flowing out of $x$ by the same jump. Now Taylor-expand the incoming term, but only in
its *starting position* — treat the jump size $y$ as fixed while expanding the dependence on where
the jump began, around $x$:

$$R(y, x - y)p(x - y) = R(y, x)p(x) - y \frac{\partial}{\partial x} \big(R(y, x)p(x)\big) + \frac{y^2}{2} \frac{\partial^2}{\partial x^2} \big(R(y, x)p(x)\big) - \cdots$$

This is legitimate precisely when typical jumps are small — almost-local transitions. Keeping terms
to second order, the two $R(y,x)p(x)$ terms cancel between the incoming and outgoing flux, and
pulling the $y$-integrals inside the $x$-derivatives leaves

$$\frac{\partial p(x, t)}{\partial t} = -\frac{\partial}{\partial x} \big[v(x) p(x, t)\big] + \frac{\partial^2}{\partial x^2} \big[D(x) p(x, t)\big],$$

with

$$v(x) \equiv \int dy \, y\, R(y, x) = \frac{\langle \Delta(x) \rangle}{\Delta t}, \qquad D(x) \equiv \frac{1}{2} \int dy \, y^2 R(y, x) = \frac{1}{2}\frac{\langle \Delta(x)^2 \rangle}{\Delta t}.$$

This drift–diffusion equation is a **forward Kolmogorov equation**: $v(x)$ is the mean rate of
change of position — the drift — and $D(x)$ is a position-dependent diffusion coefficient built
from the variance of the jump. The same equation, derived for a random walk rather than a
population, is the Fokker–Planck equation of statistical physics.

### Specializing to allele counts

In population genetics the natural variable is the allele frequency $x = n/N \in [0,1]$, and the
processes of interest change $n$ by exactly $\pm1$ at a time. For such a one-step process the
integrals collapse to the two rates $R_{n+1,n}$ (birth: $n \to n+1$) and $R_{n-1,n}$ (death:
$n \to n-1$), and

$$v(x) = \frac{\langle \Delta n\rangle}{N} = \frac{R_{n+1,n} - R_{n-1,n}}{N}, \qquad D(x) = \frac{\langle \Delta n^2\rangle}{2N^2} = \frac{R_{n+1,n} + R_{n-1,n}}{2N^2}.$$

These two lines do all the work in what follows: write down the up- and down-rates of whatever
birth–death process is under discussion, and $v(x)$, $D(x)$ fall out directly.

## Three models for how allele frequency changes

### Mutation alone

Suppose a locus carries two alleles, $A_1$ and $A_2$, and each of the $N$ copies mutates
independently: $A_2 \to A_1$ at per-copy rate $\mu_1$, and $A_1 \to A_2$ at rate $\mu_2$. With $n$
copies of $A_1$, the $N-n$ copies of $A_2$ each mutate at total rate $\mu_1(N-n)$ (giving
$R_{n+1,n} = \mu_1(N-n)$) and the $n$ copies of $A_1$ mutate at total rate $\mu_2 n$ (giving
$R_{n-1,n} = \mu_2 n$). Substituting into the formulas above,

$$v(x) = \mu_1(1-x) - \mu_2 x, \qquad D(x) = \frac{\mu_1(1-x) + \mu_2 x}{2N}.$$

Mutation alone is a deterministic-looking drift: it pushes $x$ toward the balance point where
$\mu_1(1-x) = \mu_2 x$, at a rate that vanishes only there.

### Genetic drift: binomial sampling

Now switch off mutation and ask instead what fluctuation is generated purely by finite population
size in reproduction. The mutation rates $\mu_1=\mu_2=0$ are negligible for something like eye
colour, yet the proportion of the two alleles still drifts from generation to generation, because
some individuals leave no descendants and others leave several — itself a random process, and the
main source of rapid change in allele proportion.

The simplest model of this, **binomial selection**, treats each new generation as $N$ independent
draws with replacement from the current pool: with $n$ of $N$ alleles being $A_1$, the number $m$
of $A_1$ copies in the next generation is Binomial$(N, n/N)$,

$$\Pi_{mn} = \binom{N}{m}\left(\frac{n}{N}\right)^m\left(1-\frac{n}{N}\right)^{N-m}.$$

This is exactly drawing a coloured ball from a bag of $n$ blue and $N-n$ brown balls, recording its
colour, and returning it, repeated $N$ times. From the standard moments of the binomial
distribution,

$$\langle m \rangle = n \quad\Rightarrow\quad \langle m-n\rangle = 0, \qquad \langle (m-n)^2\rangle = N\cdot\frac{n}{N}\Big(1-\frac{n}{N}\Big).$$

The mean does not move — there is no drift, $v(x) = 0$ — so this really is pure noise. Converting
the second moment into a diffusion coefficient (with a whole generation as the time step) gives, for
a haploid population,

$$D_{\text{haploid}}(x) = \frac{1}{2N}x(1-x).$$

The diploid case works the same way once genotype frequencies are related to allele frequencies.
With three genotypes $A_1A_1$, $A_1A_2$, $A_2A_2$ in Hardy–Weinberg proportions
$x_1^2$, $2x_1x_2$, $x_2^2$, mating one allele from each of two parents chosen at random is again
equivalent to drawing $A_1$ with probability $x = x_1$ — except that a diploid population of $N$
individuals carries $2N$ allele copies, so

$$D_{\text{diploid}}(x) = \frac{1}{4N}x(1-x).$$

### Selection as a competing chemical reaction

A third force, selection, can be introduced through a chemical analogue of mutation: molecules $A$
and $B$ interact so that

$$A + B \xrightarrow{\;c\;} A + A \qquad\text{or}\qquad A + B \xrightarrow{\;d\;} B + B,$$

which mimics the offspring of a heterozygote and a homozygote resolving toward one allele or the
other. In a mean-field (deterministic) approximation, $\dot N_A = (c-d)N_AN_B$, with steady states
$N_A^*=0$ for $c<d$, $N_A^*=N$ for $c>d$, and every composition marginally stable when $c=d$ —
fluctuations, as the rest of this section shows, break that degeneracy.

Writing $n=N_A$ as before, a single reaction changes $n$ by $\pm1$ at rates proportional to the
number of possible $A$–$B$ pairs,

$$R_{n,n+1} = d(n+1)(N-n-1), \qquad R_{n,n-1} = c(n-1)(N-n+1),$$

giving a master equation with the usual bulk terms plus boundary terms at $n=0,N$. Taking the large
$N$ limit,

$$v(x) = \frac{R_{n+1,n}-R_{n-1,n}}{N} = N(c-d)\,x(1-x), \qquad D(x) = \frac{R_{n+1,n}+R_{n-1,n}}{2N^2} = \frac{c+d}{2}\,x(1-x).$$

Comparing with the binomial-selection results above, this reaction reproduces genetic drift exactly
when $c = d = 1/(4N)$: the apparent factor of $N$ difference is only because here reactions are
followed one at a time, whereas binomial selection advances a whole generation ($N$ reproduction
events) in one step.

When $c \neq d$ one allele is genuinely favoured — this is *selection* — and the resulting drift
term makes that precise. Population genetics conventionally parametrizes the asymmetry by a
selection coefficient $s$,

$$c = \frac{1}{4N}(1+s), \qquad d = \frac{1}{4N}(1-s),$$

which is mathematically equivalent to the reaction model above and turns the drift and diffusion
into the standard forms used from here on,

$$v(x) = \frac{s}{2}x(1-x), \qquad D(x) = \frac{1}{4N}x(1-x).$$

## The steady-state distribution of allele frequency

### A general recipe for one dimension

The time-dependent Kolmogorov equation is generally hard to solve, but its steady state $p^*(x)$,
defined by $\partial p^*/\partial t = 0$, is not. Setting the right-hand side of the drift–diffusion
equation to zero,

$$-\frac{\partial}{\partial x}\big[v(x)p^*(x)\big] + \frac{\partial^2}{\partial x^2}\big[D(x)p^*(x)\big] = 0.$$

The most general solution allows a constant probability current threading through the whole
interval, but there is no reason for such a circulating flow in population genetics, so we look
instead for the solution with **zero current**:

$$-v(x)p^*(x) + \frac{\partial}{\partial x}\big(D(x)p^*(x)\big) = 0.$$

Dividing through by $D(x)p^*(x)$ turns the left side into a total derivative of a logarithm,

$$\frac{\partial}{\partial x}\ln\big(D(x)p^*(x)\big) = \frac{v(x)}{D(x)},$$

which integrates directly to

$$p^*(x) \propto \frac{1}{D(x)}\exp\left[\int^x \frac{v(x')}{D(x')}\,dx'\right],$$

with the proportionality constant fixed by normalization.

### Mutation, selection and drift together

Adding the three contributions found above,

$$v(x) = \frac{s}{2}x(1-x) + \mu_1(1-x) - \mu_2 x, \qquad D(x) = \frac{1}{4N}x(1-x) + \frac{\mu_1(1-x)+\mu_2x}{2N} \approx \frac{1}{4N}x(1-x),$$

where the last step drops mutation's own (much smaller) contribution to the diffusion coefficient —
a standard approximation in population genetics, adopted here without further justification, but
one that buys a closed-form steady state. With it,

$$\frac{v(x)}{D(x)} = 4N\left[\frac{\mu_1}{x} - \frac{\mu_2}{1-x} + \frac{s}{2}\right],$$

so that

$$\ln\big(D(x)p^*(x)\big) = 4N\left[\mu_1\ln x + \mu_2\ln(1-x) + \frac{s}{2}x\right] + \text{const},$$

and, restoring the $1/D(x) \propto 1/[x(1-x)]$ prefactor,

$$p^*(x) \propto \frac{1}{x(1-x)}\, x^{4N\mu_1}\,(1-x)^{4N\mu_2}\, e^{2Nsx} = x^{4N\mu_1 - 1}(1-x)^{4N\mu_2-1}e^{2Nsx}.$$

### Two regimes: polymorphism versus fixation

Take the neutral, symmetric case $s=0$, $\mu_1=\mu_2=\mu$, where the steady state reduces to

$$p^*(x) \propto \big[x(1-x)\big]^{4N\mu - 1}.$$

The single combination $4N\mu$ decides the shape:

- If $4N\mu > 1$, the exponent is positive, $p^*(x)$ vanishes at both boundaries and peaks at
  $x=1/2$: mutation resupplies both alleles fast enough, relative to drift, that the population
  sits near an even mixture — a **polymorphic** steady state.
- If $4N\mu < 1$, the exponent is negative, and $p^*(x)$ diverges at $x=0$ and $x=1$: mutation is
  too weak to counteract drift, and the population spends most of its time near fixation of one
  allele or the other.

<figure>
<svg viewBox="0 0 480 220" role="img" aria-label="Steady-state allele-frequency distribution for 4N mu greater than 1, peaked in the middle, versus 4N mu less than 1, peaked at both ends">
  <line x1="40" y1="180" x2="220" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <path d="M40,178 C70,60 100,40 130,40 C160,40 190,60 220,178" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="130" y="205" text-anchor="middle" font-size="12" fill="currentColor">x</text>
  <text x="40" y="195" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="220" y="195" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="55" y="35" text-anchor="start" font-size="12" fill="currentColor">p*(x)</text>
  <text x="130" y="20" text-anchor="middle" font-size="12" fill="currentColor">4N&#956; &#62; 1</text>

  <line x1="260" y1="180" x2="440" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <path d="M260,45 C290,140 320,170 350,170 C380,170 410,140 440,45" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="350" y="205" text-anchor="middle" font-size="12" fill="currentColor">x</text>
  <text x="260" y="195" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="440" y="195" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="275" y="35" text-anchor="start" font-size="12" fill="currentColor">p*(x)</text>
  <text x="350" y="20" text-anchor="middle" font-size="12" fill="currentColor">4N&#956; &#60; 1</text>
</svg>
<figcaption>Neutral steady-state allele-frequency distribution $p^*(x) \propto [x(1-x)]^{4N\mu-1}$.
Left, mutation dominates drift ($4N\mu>1$) and the population sits near an even mixture of the two
alleles. Right, drift dominates mutation ($4N\mu<1$) and the population spends most of its time
close to fixation of one allele or the other.</figcaption>
</figure>

This is the sense in which **genetic drift** — the pure sampling noise identified in binomial
selection, with no drift term of its own — nonetheless comes to dominate the long-run behaviour of
a small population: it is not that $v(x)$ favours the boundary, but that weak mutation is not
enough to keep pulling the distribution away from it.

## Sources

- Slides: `lectures/03-slides/01-introduction.md` (continuum limit and forward Kolmogorov
  equation, §1.3), `02-1-3-1-binomial-selection.md` (§1.3.1, binomial selection), the reaction
  model in `03-1-3-2-chemical-analog-selection.md` (§1.3.2, chemical analogue and selection), and
  `04-1-3-3-steady-states.md` (§1.3.3, steady states) — MIT OCW 8.592J/HST.452J, *Statistical
  Physics in Biology*, Spring 2011, lecture 3. No transcript or written notes were supplied for
  this lecture; the exposition above follows the slides' own derivations and worked comparisons.
- The birth–death rates for the mutation model ($R_{n+1,n}=\mu_1(N-n)$, $R_{n-1,n}=\mu_2 n$) are
  not stated explicitly in the supplied slides; they are recovered here from the drift formula
  (the slides' Eq. 1.38) that does state them implicitly. The slides refer to a fuller mutation
  model as Eqs. (1.22)–(1.23), an earlier chemical analogue of mutation as Eq. (1.25), and a
  normalization condition as Eq. (1.14) — none of these were among the files supplied, so they are
  named here but not reconstructed.
- The slides note that "the population genetics perspective on selection will be covered in detail
  by Professor Mirny" — a portion of the course not contained in the supplied material.
- Exercises: the supplied problem set, `psets/03-questions.md` ("Assignment #3"), is titled
  *Extreme Values* and covers the statistics of maxima of many random variables (order statistics
  and the Gumbel distribution, applied to homodimer/heterodimer binding energies, thymic selection
  of T-cell receptors, and gapless sequence alignment). None of its four questions concerns the
  diffusion approximation, mutation, drift, or selection treated in this lecture's slides, so no
  exercises are given here; that problem set belongs with a different lecture's material on
  extreme-value statistics.

---

[← 1. Sequence Entropy and Evolving Probabilities](01-sequence-entropy-and-evolving-probabilities.md) · [Contents](index.md) · [3. Absorbing States and Fixation →](03-absorbing-states-and-fixation.md)
