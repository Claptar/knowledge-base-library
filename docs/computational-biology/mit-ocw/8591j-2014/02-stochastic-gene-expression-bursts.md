---
title: "2. Stochastic Gene Expression Bursts"
course: "MIT 8.591J 2014"
chapter: 2
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 2. Stochastic Gene Expression Bursts

## What this covers

This chapter works through a single model of gene expression — constitutive transcription and
translation, each followed by first-order degradation — in as much depth as it will bear: first
the deterministic (mean) behaviour, then the full probability distributions of mRNA and protein
copy number, built up from a simple renewal argument and from the master equation. It assumes the
two-stage birth-death picture of gene expression introduced in the previous lecture (via Sunney
Xie's single-molecule counting experiments in *E. coli*), basic ODEs, and the Poisson, geometric,
exponential and gamma distributions.

## The model

Two species, mRNA (count $m$) and protein (count $p$):

- mRNA is made at constant rate $S_m$ and degraded at rate $\delta_m$ per molecule.
- Protein is made (translated) at rate $S_p$ per mRNA molecule present, and degraded at rate
  $\delta_p$ per molecule.

This is a first-order (linear) description: nothing here depends on repressors, feedback, or
cooperative binding — it is meant as a reasonable model of a bacterial gene sitting in an "on"
state (no repressor bound, or already time-averaged over one that binds and unbinds). It is the
model behind the Xie-lab paper discussed in the previous lecture.

None of the four rates $S_m,\delta_m,S_p,\delta_p$ is set equal to 1. This is deliberately not yet
a non-dimensionalized model — the rates carry real units (per second, per minute, whatever they
were measured in) — so "one unit of time" in this model is not automatically a cell cycle, an mRNA
lifetime, or anything else in particular.

## Growth dilution counts as degradation

Take the protein to be chemically stable: no enzymatic or other physical decay. Even so, if the
cell population is doubling, the number of protein molecules per cell is effectively being
"degraded" by dilution — stop making protein, double the number of cells, and the concentration
per cell has dropped by a factor of two. So write the effective protein degradation rate as

$$\delta_p = \gamma_{\text{growth}} + \delta_p^{\text{phys}}$$

where $\gamma_{\text{growth}}$ is the exponential growth rate of the cell population and
$\delta_p^{\text{phys}}$ is true chemical degradation. For a stable protein $\delta_p^{\text{phys}}
= 0$, so the effective degradation rate of the protein *is* the population's growth rate: measure
the exponential growth of a bacterial culture in a spectrophotometer, and that rate is exactly
$\delta_p$ in this model.

The same effective/physical split applies to $\delta_m$, but for mRNA the physical decay rate is
normally so much faster than the dilution rate that $\delta_m$ is, in practice, just the chemical
degradation rate — mRNA is short-lived; protein, in general, is longer-lived.

## Four mean copy numbers

Before doing any of the probability theory, get the mean behaviour of the model straight — this is
what polling the class on "which ratio of $S_m,\delta_m,S_p,\delta_p$ is this?" was for.

Mean number of mRNA per cell:
$$\langle m \rangle = \frac{S_m}{\delta_m}$$
mRNA is made at a fixed rate and lives for a mean time $1/\delta_m$, and that is the whole story —
it does not matter what happens to the mRNA's eventual protein output.

Mean number of protein molecules made from a single mRNA, over its lifetime:
$$\langle n_{\text{burst}} \rangle = \frac{S_p}{\delta_m}$$
Not $\delta_p$. Once an mRNA exists, the question is a competition between two rates racing against
each other: translation, at rate $S_p$, versus that same mRNA's own degradation, at rate $\delta_m$.
If $S_p=\delta_m$, you expect one protein made before the mRNA is degraded; if $S_p$ is twice
$\delta_m$, two. This is a genuinely different quantity from the ratio of steady-state protein and
mRNA *concentrations* in the cell, which does involve $\delta_p$ (below) — the two get conflated
easily and are worth keeping visibly separate.

Mean number of mRNA molecules produced per cell cycle (ignoring factors of $\ln 2$):
$$\langle m_{\text{per cycle}} \rangle \approx \frac{S_m}{\delta_p}$$
because with the protein stable, $\delta_p$ *is* the growth rate, and the cell generation time is
$\ln 2$ divided by that growth rate. This quantity — the mean number of transcriptional "bursts"
per cell cycle — is the one measured directly as burst frequency in the Xie-lab paper.

Mean number of protein molecules per cell:
$$\langle p \rangle = \frac{S_m}{\delta_m}\cdot\frac{S_p}{\delta_p}$$
One way to see this: $S_p/\delta_p$ is what the steady-state protein count *would* be if there were
exactly one constant mRNA sitting there feeding translation (same reasoning as
$\langle m\rangle = S_m/\delta_m$, one level up); multiply by the mean number of mRNA actually
present, $S_m/\delta_m$, since translation does not care about mRNA concentration beyond "how many
templates are there right now."

## Two Poisson distributions, easy to mix up

Two different quantities both turn out to be Poisson-distributed, with two different means, and
they are easy to confuse precisely because the model has only one obvious length-scale-like
quantity to reach for.

- **mRNA produced per cell cycle**: Poisson with mean $S_m/\delta_p$. A Poisson distribution is
  what you get whenever there is a constant probability per unit time of an event, and you ask how
  many events happen in a fixed window — that is the definition, and a cell cycle is a fixed window.
- **mRNA present in the cell at a given instant**: also Poisson, but with mean $S_m/\delta_m$ — a
  smaller mean, since $\delta_m \gg \delta_p$ typically (mRNA turns over much faster than cell
  division).

In the data referred to from the previous lecture, there was on the order of one mRNA burst
produced per cell cycle, but the mean number of mRNA actually sitting in a cell at any moment was
around $1/30$ of that, because the mRNA lifetime was only about 1.5 minutes. In other words: in a
typical snapshot of that cell, you would most often see *no* mRNA at all, even though transcription
is firing roughly once a cycle.

## The burst-size distribution: geometric, and its continuous cousin

How many proteins get made from a single mRNA, not on average, but as a distribution? Model it as
a two-state process: the mRNA is either intact or degraded, and while it is intact, two things
race — degradation, at rate $\delta_m$, and "go around a loop and emit one protein," at rate $S_p$.

<figure>
<svg viewBox="0 0 360 200" role="img" aria-label="A two-state diagram: an intact-mRNA state with a self-loop that emits a protein and returns, and an exit arrow to a degraded-mRNA state.">
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
</marker>
</defs>
<circle cx="110" cy="110" r="50" fill="none" stroke="currentColor" stroke-width="1.5"/>
<text x="110" y="106" text-anchor="middle" font-size="12" fill="currentColor">mRNA</text>
<text x="110" y="122" text-anchor="middle" font-size="12" fill="currentColor">intact</text>
<circle cx="300" cy="110" r="42" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
<text x="300" y="106" text-anchor="middle" font-size="12" fill="currentColor">mRNA</text>
<text x="300" y="122" text-anchor="middle" font-size="12" fill="currentColor">degraded</text>
<path d="M 158 110 L 254 110" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="205" y="98" text-anchor="middle" font-size="12" fill="currentColor">&#948;m</text>
<path d="M 90 64 C 50 20, 150 -6, 152 62" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="115" y="18" text-anchor="middle" font-size="12" fill="currentColor">Sp (emit one protein)</text>
</svg>
<figcaption>The competition, per mRNA: loop around and emit a protein at rate S_p, or exit
(degrade) at rate delta_m. The number of loops taken before the exit is what makes the protein
burst geometric.</figcaption>
</figure>

Let $\rho$ be the probability that, from the intact state, the *next* thing that happens is
another lap of the loop rather than degradation:
$$\rho = \frac{S_p}{S_p + \delta_m}$$
That is just the rate of the loop divided by the sum of the two competing rates. Then:

- $P(0) = 1-\rho$ — the very first thing that happens is degradation.
- $P(1) = \rho(1-\rho)$ — first lap the loop once (probability $\rho$), then degrade (probability
  $1-\rho$).
- $P(2) = \rho^2(1-\rho)$ — loop twice, then degrade.
- in general, $P(n) = \rho^n(1-\rho)$.

That is the geometric distribution. Check it is normalized:
$\sum_{n=0}^\infty \rho^n(1-\rho) = (1-\rho)\cdot\frac{1}{1-\rho} = 1$, using the geometric series.
Its mean is
$$\langle n\rangle = \frac{\rho}{1-\rho},$$
which diverges as $\rho\to 1$ — makes sense, since $\rho\to1$ means the mRNA essentially never
degrades, so it keeps making proteins forever.

Two things worth flagging. First, this derivation assumes each lap of the loop is an independent
trial with the same $\rho$ — a real simplification, raised directly in discussion (do ribosomes
get "caught," and so on). The answer given: write down the simplest model first, measure, and ask
whether the simple model is adequate; if the data force in more mechanism, you add it, at the cost
of more parameters. In the case referred to (the Xie-lab data), a plain geometric distribution with
one free parameter (mean around 4–5 proteins per mRNA) fit well. Second, "geometric distribution"
has more than one standard convention floating around — depending on whether the count is of
successes or of trials-including-the-terminating-one — so a memorized formula for $P(n)$ can easily
be for a *different* definition than the one actually needed. In the continuous limit this
distribution becomes the exponential distribution, $P(n)\propto e^{-n/b}$ for some scale $b$ — and
it is this continuous version that gets used below.

## The master equation, and why mRNA number comes out Poisson

Fix a snapshot in time and ask about the *number* of mRNA molecules in the cell, as a probability
distribution over states $n = 0, 1, 2, \dots$ (you cannot go below zero). This is the stochastic
counterpart of the deterministic equation
$$\dot m = S_m - \delta_m m,$$
whose equilibrium is $m_{\rm eq} = S_m/\delta_m$, approached on a timescale $1/\delta_m$.

<figure>
<svg viewBox="0 0 460 170" role="img" aria-label="A birth-death chain over mRNA counts 0, 1, 2, 3, with forward rate S_m and backward rate n times delta_m.">
<defs>
<marker id="arrow2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
</marker>
</defs>
<g font-size="13" fill="currentColor">
<circle cx="40" cy="90" r="26" fill="none" stroke="currentColor" stroke-width="1.5"/>
<text x="40" y="95" text-anchor="middle">0</text>
<circle cx="160" cy="90" r="26" fill="none" stroke="currentColor" stroke-width="1.5"/>
<text x="160" y="95" text-anchor="middle">1</text>
<circle cx="280" cy="90" r="26" fill="none" stroke="currentColor" stroke-width="1.5"/>
<text x="280" y="95" text-anchor="middle">2</text>
<circle cx="400" cy="90" r="26" fill="none" stroke="currentColor" stroke-width="1.5"/>
<text x="400" y="95" text-anchor="middle">3</text>
<text x="440" y="95" text-anchor="middle">&#8943;</text>
<path d="M 66 78 C 100 55, 120 55, 154 78" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow2)"/>
<path d="M 186 78 C 220 55, 240 55, 274 78" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow2)"/>
<path d="M 306 78 C 340 55, 360 55, 394 78" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow2)"/>
<text x="110" y="45" text-anchor="middle">Sm</text>
<text x="230" y="45" text-anchor="middle">Sm</text>
<text x="350" y="45" text-anchor="middle">Sm</text>
<path d="M 154 102 C 120 125, 100 125, 66 102" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow2)"/>
<path d="M 274 102 C 240 125, 220 125, 186 102" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow2)"/>
<path d="M 394 102 C 360 125, 340 125, 306 102" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow2)"/>
<text x="110" y="150" text-anchor="middle">1&#183;&#948;m</text>
<text x="230" y="150" text-anchor="middle">2&#183;&#948;m</text>
<text x="350" y="150" text-anchor="middle">3&#183;&#948;m</text>
</g>
</svg>
<figcaption>The mRNA-count chain: a constant rate S_m pushes every state up by one; a rate
proportional to occupancy, n times delta_m, pushes state n down to n-1. Balancing each pair of
arrows at steady state gives the Poisson distribution.</figcaption>
</figure>

Write $P_n(t)$ for the probability of having $n$ mRNA molecules at time $t$, and let $f_n$ be the
rate of the transition $n\to n+1$ and $g_n$ the rate of $n \to n-1$. The general master equation —
probability flowing in minus probability flowing out — reads, for every $n \ge 1$,
$$\frac{dP_n}{dt} = f_{n-1}P_{n-1} + g_{n+1}P_{n+1} - (f_n+g_n)P_n,$$
with the boundary case $n=0$ missing the "leave downward" and "arrive from below" terms, since
there is no state $-1$. This has traded one differential equation (the deterministic one) for an
*infinite* family of coupled differential equations — one per value of $n$ — each of which is
otherwise more complicated to solve than the single deterministic equation was. That trade buys the
full stochastic description: start from any initial distribution over $n$ and this machinery tells
you how the whole distribution evolves, not just its mean. It is also the natural way to organize
the bookkeeping if the goal is instead a stochastic simulation (the subject of the next lecture,
along with the Fokker–Planck approximation and the Gillespie algorithm).

For this model the rates are simple: $f_n = S_m$ (transcription does not care how many mRNA already
exist), and $g_n = \delta_m\, n$ (each of the $n$ existing mRNA molecules degrades independently at
rate $\delta_m$, so the *total* exit rate scales with how many there are to degrade).

At steady state, $dP_n/dt = 0$ for every $n$, which is most simply read arrow-by-arrow: the
probability flux across each edge of the chain has to balance, i.e. $f_n P_n = g_{n+1}P_{n+1}$ for
every $n$ (if it did not, probability would be draining across that one link and nothing could be
stationary). That gives a clean recursion:
$$\frac{P_{n+1}}{P_n} = \frac{f_n}{g_{n+1}} = \frac{S_m}{\delta_m(n+1)}.$$
Unwind it, writing $\lambda \equiv S_m/\delta_m$:
$$P_1 = \lambda P_0,\qquad P_2 = \frac{\lambda^2}{2!}P_0,\qquad P_3 = \frac{\lambda^3}{3!}P_0,\qquad
\dots,\qquad P_n = \frac{\lambda^n}{n!}P_0.$$
Normalize using $\sum_{n\ge0}\lambda^n/n! = e^\lambda$:
$$1 = \sum_n P_n = P_0\, e^\lambda \implies P_0 = e^{-\lambda}.$$
So $P_n = \dfrac{\lambda^n}{n!}e^{-\lambda}$ — a Poisson distribution with mean
$\lambda = S_m/\delta_m$, exactly the mean computed earlier by the simpler rate argument, now
recovered as the full distribution.

One structural fact worth keeping: because $f_n$ and $g_n$ here are both *linear* in $n$, the mean
of this stochastic process obeys exactly the same differential equation, over time, as the
deterministic equation $\dot m = S_m - \delta_m m$ — a single stochastic trajectory looks jagged,
and even at steady state wobbles up and down, but averaged over infinitely many such trajectories
it reproduces the smooth deterministic curve exactly. That equivalence is special to this linear
case; if $f_n$ or $g_n$ were nonlinear functions of $n$ (as they will be once feedback or
cooperative binding enters), the mean of the stochastic distribution and the deterministic
trajectory can genuinely differ.

## From burst size to protein number: the gamma distribution

The distribution of protein number *in the cell* is harder — knowing the burst-size distribution
(geometric, per mRNA) and the mRNA-number distribution (Poisson) does not immediately hand you the
protein distribution, because a cell's total protein count is built from a random *number* of
bursts, each of random size. The exact discrete answer is a negative binomial distribution (derived
earlier by Paulsson); the exact continuous approximation to it — used here in place of the harder
discrete derivation — is the **gamma distribution**, worked out for this model in a PRL paper by
Sunney Xie's group. It is to the geometric/negative-binomial world what the exponential is to it in
the single-burst case: the continuous stand-in.

The gamma distribution needs two parameters, $\Gamma(a,b)$:

- $a$ = mean number of bursts (mRNA produced) per cell cycle, $a \approx S_m/\delta_p$;
- $b$ = mean burst size, $b = S_p/\delta_m$;

with mean $\langle p\rangle = ab$ (matching the product computed earlier) and variance $ab^2$.

The way to picture where it comes from: a single burst is exponentially distributed with scale $b$
— that is the continuous version of the geometric burst-size distribution above. Over one cell
cycle there are, on average, $a$ such bursts, each independent, and the total protein made is their
*sum* — a convolution of $a$ exponential distributions. Add one exponential to itself and the peak,
which starts at zero, shifts away from zero and the distribution's rise becomes linear near the
origin; add three, and it starts out quadratic near the origin; more generally, summing $a$
exponentials moves the distribution from something peaked at zero to something peaked at a nonzero
value once $a$ is large enough. This corresponds directly to the biological picture: proteins are
stable, so it takes roughly a cell cycle for a given cohort of protein to be diluted away, and what
matters for the total is how many bursts occurred in that cycle and how big each one was.

## Both limiting distributions become Gaussian

What happens to the gamma distribution as $a$ grows (many bursts per cycle)? It converges to a
Gaussian — an instance of the central limit theorem: sum a well-behaved distribution with itself
many times, and a Gaussian is what falls out, regardless of the shape of what you started with. The
Poisson distribution shows exactly the same behaviour as its mean $\lambda$ grows large, and the
reason is the same kind of argument: take two independent draws from a Poisson process with the
same rate over the same length of time — the resulting counts are each $\mathrm{Poisson}(\lambda)$.
Convolve those two distributions (add the counts) and the result must be
$\mathrm{Poisson}(2\lambda)$ — forced without doing the convolution integral, because "twice as many
independent draws from the same rate over the same window" is exactly the same process as one draw
over twice the window, and it must have twice the mean (means add for independent variables
regardless). Chain $n$ such windows together and the count is $\mathrm{Poisson}(n\lambda)$, i.e. the
sum of $n$ independent, identically shaped distributions — which by the central limit theorem has to
approach a Gaussian as $n$ grows. So the Poisson distribution *has* to become Gaussian for large
$\lambda$, and by roughly $\lambda \sim 100$ it already looks like one. (This chain of windows does
not even need equal rates — a Poisson process with a *different* rate over each of several
sub-intervals is still, added across the whole interval, Poisson; see below.) For small $\lambda$
the Poisson distribution instead piles up near zero — it cannot take negative values, so it is
visibly skewed rather than Gaussian, which is the regime the model lives in for many real mRNA
counts.

## Where the simple picture breaks

The lecture's data reference (Xie-lab, *E. coli*) showed one deviation from the picture above even
in bacteria: the transcriptional burst rate was not constant across the cell cycle. Longer cells —
those that had already replicated the gene and so carried two copies of it — had a higher mRNA
synthesis rate than shorter, pre-replication cells. This does *not* break the Poisson-ness of the
per-cycle mRNA count, though: splitting the cycle into a sub-interval with rate $\lambda_1$ and one
with rate $\lambda_2$ still gives two independent Poisson counts, which add to a Poisson count with
mean $\lambda_1+\lambda_2$ — Poissons stay Poisson under addition even when the underlying rate
changes partway through.

Eukaryotic promoters break the picture more seriously. Real eukaryotic genes switch between an
active and an inactive state, at some rate in each direction — timescales debated in the field,
roughly minutes to hours depending on organism and gene, sometimes on the order of a full (possibly
day-long, in mammalian cells) cell cycle. Once that switching is added, the mRNA number is *no
longer Poisson* — the resulting steady-state distribution has been solved analytically (attributed
to Arjun Raj, author of the assigned review), and involves gamma functions together with a
confluent hypergeometric function of the first kind — a solution described as complicated enough
that its exact form was only gestured at, not reproduced. What that complexity buys biologically is
exactly what is observed: in mammalian cells, individual-cell mRNA counts vary enormously, with some
cells carrying almost none and others a great many, at the same time and in the same population.
Protein-number distributions, by contrast, stay comparatively regular, because the much longer
protein lifetime averages out the wild cell-to-cell mRNA fluctuations.

## Noise-induced competence in *B. subtilis*

One worked biological application, from a study by Hedia Maamar, Arjun Raj and Dave Dubnau:
*B. subtilis* cells occasionally enter a state called competence, in which they take up DNA from
outside — sometimes just consumed, sometimes incorporated into the genome — typically triggered
under starvation or other stress. Competence is controlled by a protein, ComK, that positively
activates its own expression, a positive feedback loop that produces bistability in the network:
only a small fraction of cells reach the high-ComK state and switch on competence.

The question the study addressed was whether that switching was noise-induced — i.e., whether it
was fluctuations, not some deterministic per-cell difference, driving which cells committed. The
experimental handle, in the language of this model: the mean ComK level is set by the product
$S_m S_p/(\delta_m\delta_p)$, while the *noise* in ComK level is driven mainly by the translational
burst size, $b = S_p/\delta_m$ (the bigger each burst, the noisier the total, for the same mean). So
it is possible to change the transcription rate $S_m$ and translation rate $S_p$ in *opposite*
directions, by the same factor, holding their product — and hence the mean protein level — fixed,
while changing the burst size and hence the noise. Raising $S_m$ and lowering $S_p$ by the same
factor keeps the mean the same but shrinks the burst size, lowering the noise. That is what they
did — varied $S_m$ and $S_p$ by about a factor of two in opposite directions — and found that the
lower-noise condition, at the same mean ComK level, produced measurably fewer competent cells:
evidence that the switching itself is driven by noise in ComK level, not by mean level alone.

## Sources

All of this chapter is drawn from a single transcript-only lecture recording: MIT OCW 8.591J
(Systems Biology, Fall 2014), recording `03bvgr-vyhq` (converted transcript at
`computational-biology/mit-ocw/8591j-2014/recordings/recordings/03bvgr-vyhq.md` in the library). No
slides, problem sets, or written notes were supplied for this lecture; several diagrams the
professor drew on the board — the loop-and-exit diagram for the burst distribution, the mRNA-count
chain, the deterministic $m(t)$ sketch, the gamma- and geometric-distribution plots, and Arjun Raj's
exact two-state-promoter solution — were described verbally but not captured, and the versions
above are reconstructed from what was said about them, not copied from the board.

The lecture explicitly points at, but does not supply the content of:

- **"Sunney Xie's paper"** discussed in the prior lecture — the single-molecule mRNA/protein
  counting experiment in *E. coli* referenced throughout for the burst statistics
  ($S_p/\delta_m \approx 4$–$5$, roughly one mRNA burst per cell cycle, mRNA lifetime around 1.5
  minutes), and a separate PRL paper from the same group deriving the gamma distribution for
  protein number.
- **Paulsson's earlier derivation** of the discrete negative-binomial solution that the gamma
  distribution approximates.
- **The assigned review** (by Arjun Raj, referred to only as "the review you guys just read"),
  including his exact analytic solution for the two-state-promoter mRNA distribution (gamma
  functions and a confluent hypergeometric function of the first kind).
- **Maamar, Raj and Dubnau's competence study** in *B. subtilis*.
- **Chapters 1–2 of Uri Alon's book**, referred to for the growth-dilution argument.
- **Problem sets**, referred to ("you guys will have an opportunity to practice this") but not
  supplied to this chapter.
- **The next lecture's material** — the master equation in general, the Fokker–Planck
  approximation, and the Gillespie algorithm — flagged as coming next but not covered here.

---

[← 1. Feed-Forward Loops as Network Motifs](01-feed-forward-loops-as-network-motifs.md) · [Contents](index.md) · [3. Lotka-Volterra Dynamics and Population Waves →](03-lotka-volterra-dynamics-and-population-waves.md)
