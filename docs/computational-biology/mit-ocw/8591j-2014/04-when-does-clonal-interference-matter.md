---
title: "4. When Does Clonal Interference Matter"
course: "MIT 8.591J 2014"
chapter: 4
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 4. When Does Clonal Interference Matter

## What this covers

This chapter picks up right where the Moran-process fixation formula left off and asks what
changes when *two* mutant lineages are alive in the population at once. A set of in-class
quantitative questions builds the idea of when a beneficial mutation has become **established** —
safely past the risk of early chance extinction — and that idea is then used to derive the two
competing time scales that decide whether one lineage's fate is affected by another's at all: this
is **clonal interference**. The second half applies the same machinery to a real measurement
problem — why the distribution of effect sizes of beneficial mutations is much harder to measure
than it sounds, for a reason that turns out to have nothing to do with competition between
lineages. It assumes the Moran model and the fixation-probability formula from the previous
lecture, $x_i = \dfrac{1-r^{-i}}{1-r^{-N}}$, where $r$ is a mutant lineage's fitness relative to
the rest of the population, $N$ is the (fixed) population size, and $i$ is how many copies of the
mutant are currently present.

## Recap: fixation probability in the Moran model

$x_i$ is the probability that a lineage currently at $i$ copies eventually takes over the whole
population of $N$. Writing $s = r - 1$ for the mutant's selective advantage, this formula has two
limits worth having on hand for everything below:

- **Neutral** ($s = 0$): $x_i \to i/N$, and in particular a single neutral mutant ($i=1$) fixes
  with probability $1/N$.
- **Moderately beneficial** ($s > 0$ and $Ns \gg 1$): $x_1 \to s$.

Both limits come from the same formula; the second is *only* valid once $Ns \gg 1$, and forgetting
that condition is the first trap below.

## A single mutant against a single mutant, small population

Take a population of $N=10$, with the other eight individuals at fitness $1$, and introduce one
copy each of two mutants: $A$ with $r_A = 1.01$ (slightly beneficial, $s_A = 0.01$) and $B$ with
$r_B = 0.99$ (slightly deleterious, $s_B = -0.01$). Neither new mutation is allowed to appear once
the clock starts. What is the probability that $A$ fixes?

The tempting shortcut is to plug $s_A = 0.01$ straight into the "moderately beneficial" limit and
answer $1\%$. That answer is nonsensical, and the reason is instructive: it would say that $A$
fixes *less* often than a neutral mutation would ($1/N = 10\%$), even though $A$ is (weakly)
beneficial. The $x_1 \to s$ limit is only the right tool when $Ns \gg 1$; here
$s_A N = 0.01 \times 10 = 0.1$, which is small, not large. $A$ is not moderately beneficial at this
population size — it is **nearly neutral**, the regime $|s|N \ll 1$, in which the fixation
probability is (to good approximation) the *neutral* value regardless of the sign of $s$:
$$x_1(A) \approx x_1(B) \approx \frac1N = 0.1.$$

The same population size that makes $s_A N = 0.1$ small would not do so for a much larger
population: with a million individuals, an $s=0.01$ mutation would be solidly in the moderately
beneficial regime instead. Whether a given selective advantage counts as "detectable" by drift is
a statement about $sN$, not about $s$ alone.

This resolves a natural piece of intuition, that $A$ and $B$ should fix with roughly the same
probability by symmetry (both nearly neutral, one just slightly on each side of neutral) — that
part is right. What that intuition misses is that $A$ and $B$ fixing are not the *only* two
outcomes. In fact, in the fully neutral limit, every one of the $N$ individuals present — the two
mutants and the eight ordinary ones — is equally likely to be the eventual common ancestor of the
whole population, each with probability $1/N$. $A$ and $B$ being nearly neutral just means they
inherit this same $1/N$ share; the remaining $8/N = 80\%$ belongs, in total, to the eight
individuals that are not mutants at all. The "50/50 between $A$ and $B$" answer is wrong not
because the two are unequal, but because it silently assumes one of the two mutants has to win.

## A single mutant against a single mutant, large population

Now change the numbers: $N = 10^6$, and two single mutants, $A$ with $r_A = 2$ and $B$ with
$r_B = 1.01$ ($s_B = 0.01$). What is the probability that $B$ fixes?

First, a contrast worth keeping in mind throughout: if this population were instead modeled by a
deterministic differential equation — no stochasticity at all — whichever mutant has the larger
fitness would win with probability $1$, full stop. $A$ would fix, always. The entire content of
this section is where that certainty breaks down once the dynamics are stochastic at low copy
number.

For $B$ to fix, two things both have to happen: $B$ has to survive its own early stochastic
extinction, *and* $A$ has to fail to survive its own. (If $A$ survives, it establishes and then
spreads essentially deterministically, since it is far more fit — it wins.) So
$$P(B \text{ fixes}) \approx P(B \text{ survives}) \times P(A \text{ does not survive}).$$

$B$ is moderately beneficial here ($s_B N = 0.01 \times 10^6 = 10^4 \gg 1$), so
$P(B \text{ survives}) \approx x_1(B) \approx s_B = 0.01$.

$A$ is *not* a small perturbation ($s_A = 1$ is not small), so the $x_1 \to s$ shortcut does not
apply to it at all — the exact formula must be used instead:
$$x_1(A) = \frac{1 - r_A^{-1}}{1 - r_A^{-N}} \approx 1 - \frac12 = \frac12,$$
since $r_A^{-N} = 2^{-10^6}$ is utterly negligible. So $P(A \text{ does not survive}) = \tfrac12$.

Multiplying,
$$P(B \text{ fixes}) \approx 0.01 \times 0.5 = 0.005 = 0.5\%.$$

Multiplying the two probabilities together treats $A$'s survival and $B$'s survival as
*independent* events. That is justified here specifically because the population is enormous: while
both lineages are still rare, each one is overwhelmingly interacting with the sea of $10^6$
ordinary individuals, not with each other, so to a very good approximation they do not "see" one
another yet. This has nothing to do with how close $r_A$ and $r_B$ are — it would hold even if both
mutants had exactly the same fitness. What it does depend on is that this is only true of the early,
still-rare phase: if both $A$ and $B$ happen to survive stochastic extinction and both start
spreading, the independence assumption breaks down and the two lineages genuinely compete — that
joint event is itself rare (each survives with probability of order $s$, so the joint probability
is of order $s_A s_B$), but it is exactly the event that clonal interference, discussed below, is
about.

As a check: the three exhaustive outcomes — $A$ fixes, $B$ fixes, or both go extinct and the
already-dominant background remains — should sum to $1$:
$0.5 + 0.005 + (0.5)(0.99) \approx 1$. ✓.

## Starting from ten copies instead of one: what "established" means

Same population, same two fitnesses, but now $10$ copies of $A$ and $10$ copies of $B$ appear at
once instead of one copy each. Does the answer change much?

Redo the same calculation using $x_{10}$ instead of $x_1$. For $B$:
$$x_{10}(B) = 1 - r_B^{-10} = 1 - 1.01^{-10} \approx 1 - \frac{1}{1.1} \approx 0.1,$$
using $(1+x)^n \approx 1+nx$ for small $nx$. Starting with ten copies instead of one raises $B$'s
own survival chance tenfold, from $1\%$ to about $10\%$ — consistent with $x_i \approx is$ while
$is \ll 1$.

For $A$:
$$x_{10}(A) = 1 - r_A^{-10} = 1 - 2^{-10} \approx 1 - \frac{1}{1024} \approx 0.999,$$
so $P(A \text{ does not survive}) \approx 2^{-10} \approx 10^{-3}$ — starting $A$ at ten copies makes
its extinction a thousand-to-one long shot rather than a coin flip.

$$P(B \text{ fixes}) \approx 0.1 \times 10^{-3} = 10^{-4}.$$

This is the *opposite* of what a naive "bigger head start helps" intuition suggests: giving both
lineages the same tenfold head start actually makes $B$'s overall fixation probability roughly
$50$ times *smaller* (from $0.5\%$ down to $0.01\%$), because it barely moves $B$'s survival chance
but almost eliminates $A$'s risk of extinction. The reason the two respond so differently to the
same head start is the real content of this problem: how much extra survival probability an
additional copy buys you depends on how far $i$ already is from a characteristic threshold,
$1/s$. For $B$ ($s_B = 0.01$), that threshold is around $100$ copies, and $i=10$ is still well
below it — $B$ is still deep in the regime where each extra copy helps roughly linearly. For $A$
($s_A = 1$), the threshold is around $1$ copy, and $i=10$ is already far past it — $A$ is
essentially already safe.

That threshold is worth deriving properly, because it is the general notion of an **established**
mutation: one that has grown large enough that further stochastic extinction is unlikely, so from
that point on its spread is well described by a deterministic exponential, not by chance. Dropping
the $r^{-N}$ term as before,
$$1 - x_i \approx r^{-i} = (1+s)^{-i} \approx e^{-is}$$
for small $s$, using $\ln(1+s) \approx s$. This extinction probability is small once $is \gg 1$, so
the number of copies needed to be established is
$$n_{\text{established}} \sim \frac1s.$$
At exactly $i = 1/s$, the extinction probability is $e^{-1} \approx 0.37$ — the crossover point
where a lineage becomes more likely than not to survive. For the beneficial mutations discussed
later in this chapter, with $s$ of a few percent, $1/s$ is a few tens, so $n_{\text{established}}$
is of order a hundred individuals.

## Two competing time scales, and when clonal interference can be ignored

Once a lineage is established, it grows roughly deterministically, from $n_{\text{established}}$
up to the full population $N$, at exponential rate $s$. That takes a time
$$T_{\text{establish} \to \text{fix}} \sim \frac1s \ln\!\left(\frac{N}{n_{\text{established}}}\right) \sim \frac1s\ln(Ns).$$
The time to become established in the first place is comparatively short and does not much affect
this, because it is a highly biased sample over trajectories — most attempts at establishment fail
quickly, and the rare ones that do not, establish quickly too.

The other relevant clock is how often new established mutations appear at all. Let $\mu$ be the
per-individual, per-generation probability of acquiring a beneficial mutation of the (single,
for simplicity) magnitude $s$ under discussion. New mutations of this kind arise in the whole
population at rate $\mu N$, so the time between successive *appearances* is exponentially
distributed with mean $1/(\mu N)$. But only a fraction of order $s$ of those appearances go on to
establish — the rest go extinct — so the time between successive *established* mutations is
exponentially distributed with the longer mean
$$T_{\text{mutation, established}} \sim \frac{1}{\mu N s}.$$
(Both $s$ and $\mu$ are already rates per generation, so both time scales above come out in units
of generations — there is no unit mismatch, even though it can look that way at first.) As a
concrete illustration, for $s = 0.02$ one has to wait for around $1/s = 50$ appearances of this
mutation, on average, before one of them happens to be the lucky one that establishes.

**Clonal interference** is what happens once two lineages are *both* established and spreading at
the same time: growing exponentially, a fitter lineage can catch up to and overtake a lineage that
established earlier but is spreading more slowly, so the first mutation never gets to fix before
being out-competed by the second.

<figure>
<svg viewBox="0 0 380 220" role="img" aria-label="Population fractions over time: the wild type gives way to a spreading mutant B, which is in turn overtaken by a fitter mutant C before B can fix.">
  <line x1="40" y1="190" x2="350" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="195" y="208" text-anchor="middle" font-size="12" fill="currentColor">time</text>
  <text x="16" y="105" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 16 105)">fraction of population</text>
  <polyline points="45,30 90,32 130,55 170,100 210,140 250,165 290,178 330,182" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="60" y="24" font-size="12" fill="currentColor">A</text>
  <polyline points="100,182 130,150 160,105 190,65 210,45 230,55 260,80 290,120 320,155 345,175" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="6 3"/>
  <text x="205" y="38" font-size="12" fill="currentColor">B</text>
  <polyline points="210,182 230,150 255,100 280,55 305,30 330,20 345,18" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="2 2"/>
  <text x="300" y="16" font-size="12" fill="currentColor">C</text>
</svg>
<figcaption>Wild type A gives way as mutant B establishes and spreads; before B can fix, a fitter
mutant C establishes on top of the same background and overtakes B in turn. Neither B nor A ever
fixes — this competition between simultaneously-spreading lineages is clonal interference.</figcaption>
</figure>

No clonal interference means the two time scales are far apart — mutations are established, spread,
and fix one at a time, well-separated:
$$T_{\text{mutation, established}} \gg T_{\text{establish}\to\text{fix}} \quad\Longleftrightarrow\quad \mu N \ll \frac{1}{\ln(Ns)},$$
which, up to the slowly-varying logarithm, is the familiar criterion $\mu N \ll 1$: the population-wide
rate of new mutations, per generation, must be much less than one.

## Measuring the distribution of fitness effects

This machinery was built to make sense of an experimental question: given a population dropped
into a new environment, what is the probability distribution of the *sizes* of the beneficial
mutations available to it?

Picture a thought experiment: take an *E. coli* genome (a few million base pairs, depending on
strain) and make every possible point mutation — on the order of ten million distinct single-mutant
strains — then measure each one's growth rate $\gamma$ relative to wild type $\gamma_{\text{wt}}$ in
some fixed environment. What should the histogram of $\gamma/\gamma_{\text{wt}}$ look like? Two
naive extremes are both wrong: it is not the case that almost nothing matters (a spike exactly at
$1$), nor that almost everything is lethal (a spike at $0$). What is known independently — from
whole-gene knockout screens, a much harsher perturbation than a single point mutation — is that only
some $10$–$20\%$ of genes are individually essential, and only a small fraction of point mutations
within a gene actually knock its function out, and not all of the genome even codes for protein; so
the lethal fraction of point mutations is small (very roughly $10^{-4}$ to $10^{-3}$, an order of
magnitude, not a measurement). The bulk of the distribution is a sharp peak at $\gamma/\gamma_{\text
{wt}} = 1$ (most point mutations have no measurable effect at all), with a small tail down toward
$0$ (rare lethal mutations) and — the part of interest here — a much smaller, even more tightly
clustered, tail above $1$: the beneficial mutations. Writing $s = \gamma/\gamma_{\text{wt}} - 1$ and
zooming into just that tail gives a density $p(s)$ for $s>0$: many mutations nearly neutral, falling
off in some way as $s$ grows. This is the quantity a paper referred to in the lecture only as "Roy's
paper" set out to measure directly, by evolving replicate populations in a new environment and
tracking which beneficial mutations actually took hold.

The paper's puzzle was that several qualitatively different candidate shapes for $p(s)$ — for
example a single fixed effect size, a uniform spread of effects, or an exponential tail — could each
be tuned (by choosing a mutation rate and a mean effect size) to reproduce the *same* observed data.
Bulk measurements of this kind cannot, by themselves, tell the shapes apart; the lecture calls this
the **equivalence principle**, and returns to it in more detail in the next lecture.

A sharper question, though, is this: suppose clonal interference is eliminated entirely — take
$\mu \to 0$, or work in a small enough population that only ever one beneficial mutation is present
at a time. Would the distribution of mutations you then see spreading finally equal the true
$p(s)$? The answer is no, and the reason has nothing to do with competition between lineages at all:
even a mutation with no competitors still has to survive its own stochastic extinction before you
ever see it spread, and the probability of surviving is proportional to $s$. So what you observe is
not $p(s)$ but something shaped like $s\,p(s)$: small effects are thrown away disproportionately
often, purely by early-generation bad luck, regardless of whether any other mutation is around to
compete with. If the true $p(s)$ is, say, monotonically decreasing and maximal at $s=0$ (an
exponential, for instance — there are arguments from extreme value theory for something like this
shape), the observed, survival-weighted distribution $s\,p(s)$ starts at $0$, rises, and only then
falls: it is peaked at some *nonzero* value of $s$, even with zero clonal interference. Add clonal
interference back in and the effect compounds: what spreads is now (roughly) the larger of several
independent draws from that already survival-biased distribution, which pushes the observed peak
further to the right and makes it narrower and taller still.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="The true distribution of beneficial-mutation effect sizes peaks at zero, but what is actually observed is shifted away from zero, and shifted further by clonal interference.">
  <line x1="40" y1="190" x2="320" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="300" y="206" text-anchor="middle" font-size="12" fill="currentColor">s</text>
  <text x="18" y="100" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 18 100)">density</text>
  <path d="M40,190 L40,40 L70,70 L100,100 L140,135 L180,155 L220,170 L260,180 L300,186 L320,188 L320,190 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <polyline points="40,40 70,70 100,100 140,135 180,155 220,170 260,180 300,186 320,188" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="46" y="34" font-size="11" fill="currentColor">true p(s)</text>
  <polyline points="40,190 60,160 90,110 120,80 140,65 160,70 190,95 220,130 260,165 300,183 320,188" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="6 3"/>
  <text x="95" y="66" font-size="11" fill="currentColor">observed, no interference</text>
  <polyline points="40,190 80,175 120,140 150,95 170,55 190,60 210,90 240,130 270,160 300,182 320,188" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="2 2"/>
  <text x="172" y="40" font-size="11" fill="currentColor">observed, with interference</text>
</svg>
<figcaption>The true effect-size distribution p(s) is maximal at s=0 (shaded). What is actually
observed spreading is size-biased toward larger s even with no competing lineages, because only
mutations that survive early stochastic extinction are ever seen, and survival probability scales
with s; clonal interference (taking the winner among several established competitors) shifts the
observed peak further right and sharpens it.</figcaption>
</figure>

So there are two entirely separate reasons the measured distribution of fitness effects is not the
true one: the survival-bias effect above, which is present even for a single mutation with no
competition, and clonal interference proper, which only matters once more than one lineage
establishes at a time. Untangling how much of the "equivalence principle" puzzle is due to each is
exactly where the discussion picks up in the next lecture.

## Sources

- Recording: `recordings/6pxncdxixne-captions.srt`, converted to
  `docs/computational-biology/mit-ocw/8591j-2014/recordings/recordings/6pxncdxixne.md` — MIT 8.591J
  *Systems Biology*, Fall 2014, transcript timestamps [00:00]–[1:20:02]. This lecture is
  transcript-only: nothing written on the board or shown on a slide survives in the source. In
  particular, the exact wording and numeric options of the in-class multiple-choice questions, any
  board work for the arithmetic in the worked examples, and the two schematic drawings described at
  [45:48]–[46:56] (lineages spreading and being out-competed) and [1:05:44]–[1:20:02] (shapes of the
  fitness-effect histogram) are not in the transcript; both figures above are reconstructed here from
  what the lecturer said about them, not copied from a board or slide.
- The Moran-process fixation-probability formula and its two limits are recapped from "last time"
  ([02:17]–[04:35]) but were derived in the previous lecture, which is not part of the material
  supplied for this chapter.
- A paper referred to throughout only as "Roy's paper" ([01:10] onward), on measuring the
  distribution of effects of beneficial mutations in *E. coli* and introducing what the lecture
  calls the "equivalence principle" — not identified further (no title, author spelling, or venue is
  audible in the transcript).
- Martin Nowak, *Evolutionary Dynamics*, chapter 6, referred to again at [35:26] as the source of
  the fixation formula being used ("that was the equation that was derived in chapter six") — not
  supplied to this chapter.
- Michael Desai's work on evolving yeast populations with high-resolution lineage tracking,
  mentioned at [46:56] as "maybe Nature 2012, '13" — not identified further.
- Charlie Boone's (Toronto) genome-wide pairwise gene-knockout screen in yeast, mentioned at
  [1:05:44] — not identified further.
- Topics flagged as continuing "on Tuesday" and not developed further here: more discussion of
  "Roy's paper," and fitness landscapes and the rate of evolution ([1:20:02]).

---

[← 3. Lotka-Volterra Dynamics and Population Waves](03-lotka-volterra-dynamics-and-population-waves.md) · [Contents](index.md) · [5. Cost-Benefit Optimization and Statistical Evidence →](05-cost-benefit-optimization-and-statistical-evidence.md)
