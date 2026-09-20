---
title: "11. Clonal Interference and Fitness Landscapes"
course: "MIT 8.591J 2014"
chapter: 11
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 11. Clonal Interference and Fitness Landscapes

## What this covers

This chapter finishes the course's discussion of clonal interference — competition between
several beneficial mutant lineages present in a population at the same time — and then turns to
fitness landscapes shaped by interactions (epistasis) between mutations. It assumes the previous
lecture's results for a single beneficial mutation: a mutation of selective advantage $s$
establishes (survives early stochastic loss) with probability of order $s$, and establishment and
fixation happen on characteristic timescales of order $1/s$ and $(1/s)\ln N$ respectively, giving
a criterion for when competing lineages can be ignored. Building on that, the chapter asks two
separate questions: how fast does a population's mean fitness actually increase with time, with
and without clonal interference; and, unrelated to speed, what a single completely measured
fitness landscape can tell us about how repeatable evolution is.

## Inferring a distribution of beneficial effects from lineage-tracking data

The setting is an *E. coli* population evolving in a new environment, split at the start into two
equal, differently labeled halves. After a few hundred generations these populations typically
improve in fitness by something like a percent or a few percent — the scale that keeps recurring
below. As beneficial mutations arise in one half or the other and spread, the log-ratio of the two
sub-populations, $\log(F_1/F_2)$, stays flat near zero until a mutation establishes, then bends
upward.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="Log ratio of two competing lineages staying flat near zero, then bending upward once a beneficial mutation establishes and spreads.">
  <line x1="40" y1="170" x2="300" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="170" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="130" x2="300" y2="130" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <polyline points="45,130 90,130 120,128 150,120 180,104 210,82 240,58 270,36 295,20" fill="none" stroke="currentColor" stroke-width="2"/>
  <circle cx="120" cy="128" r="3" fill="currentColor"/>
  <text x="120" y="145" text-anchor="middle" font-size="11" fill="currentColor">t*</text>
  <text x="230" y="55" text-anchor="middle" font-size="11" fill="currentColor">slope</text>
  <text x="170" y="192" text-anchor="middle" font-size="12" fill="currentColor">time</text>
  <text x="20" y="30" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 20 30)">log(F1/F2)</text>
</svg>
<figcaption>The two numbers read off each trajectory: the time t* at which the log-ratio first departs
from 1:1, and the slope once it does. Histogrammed over many replicate populations, these are the
whole of the data being explained.</figcaption>
</figure>

The question the paper (referred to in the lecture as the paper on the "equivalence principle") asks
is: what underlying distribution of beneficial-mutation effect sizes $p(s)$, together with what rate
$\mu_b$ of acquiring such mutations, would produce this histogram of times and slopes? It compares
three qualitatively different shapes for $p(s)$ — a delta function (every beneficial mutation has
exactly the same effect), a uniform distribution on $[0, s_{\max}]$, and an exponential distribution —
each specified by only two numbers, a mutation rate and a mean effect $\langle s\rangle$. The three
are not the only conceivable shapes; they are chosen to be as different from each other as possible,
to make the point sharply.

**Working out the ordering.** For each shape, some range of $(\mu_b, \langle s\rangle)$ fits the
data. Why must the mutation rate and mean effect needed be so different across the three shapes?

- *Delta.* With only one possible effect size, no clonal interference is needed at all to explain
  the basic shape of the data: one lineage acquires the single available beneficial mutation, of
  effect $s\approx 5$–$5.5\%$ (the value that matches the observed slope), and it simply spreads.
  Explaining why some trajectories later flatten out needs the *other* side to pick up a mutation
  too, but that is a mild, occasional need for competition, not the dominant feature of the fit —
  which is why the delta fit works with the lowest mutation rate of the three.
- *Uniform.* Trying to use the *same* mean effect ($\approx5$–$5.5\%$) for a uniform distribution on
  $[0, 2\langle s\rangle]$ fails: it predicts trajectories peaked at roughly *twice* that value.
  The reason is that the mutation you actually observe spreading is not a uniformly random draw from
  $p(s)$ — it has to survive early stochastic loss (probability of establishment $\propto s$, so
  bigger draws survive more often), and if more than one lineage appears, it has to win the
  competition against the others, which again favors the larger of the sampled values. Both effects
  push the observed slopes above the mean of the underlying distribution. A uniform distribution
  that reproduces the same observed peak needs a *smaller* mean than the delta fit — the region that
  works has $\langle s\rangle\approx3\%$, with the top of the range near $6\%$, about half the delta
  value — and it needs a somewhat higher mutation rate than delta, since a couple of surviving draws
  are now needed before their maximum lands in the right place. The amount of clonal interference
  required is still modest: just sampling two or three values from the uniform and keeping the one
  that survives stochastic extinction already peaks the outcome well above the naive mean.
- *Exponential.* An exponential distribution weights small effects even more heavily, so matching
  the same observed slope now means sampling several characteristic scales out on the tail — the fit
  needs a mean around $1\%$ (ranging from about $0.5\%$ to $1.5\%$ across the parameters that work),
  meaning the beneficial mutations that actually matter are being drawn from around $e^{-5}$ or so
  out on the tail relative to that mean. Getting enough of those rare, large draws to dominate the
  observed dynamics needs a much higher mutation rate — of order a factor of $100$ higher than for
  the other two distributions, across the range of parameters that fit — with a corresponding factor
  of about $3$ range in the compatible mean.

So there is a consistent trend: the more $p(s)$ is weighted toward small effects, the smaller its
characteristic mean must be and the larger the mutation rate must be, in order to reproduce the same
coarse statistics. This is the **equivalence principle**: bulk lineage-frequency data of this kind
cannot pin down the shape of $p(s)$ on its own, because the observed dynamics only ever samples a
size-biased, competition-filtered tail of $p(s)$ — never $p(s)$ itself. What the data constrains, for
each assumed shape, is a trade-off curve between $\mu_b$ and $\langle s\rangle$, not a unique answer.
One constraint does survive regardless of shape: a mutation has to arise within the first few tens of
generations to have had time to spread by the time it is observed, which puts a shape-independent
floor under $\mu_b$.

## The rate of evolution without clonal interference

Set the distribution question aside and ask something more basic: how fast does the population's
mean fitness $\bar w$ actually increase, $\Delta \bar w/\Delta t$? While selection coefficients are
small it barely matters whether fitness effects of successive mutations add or multiply — for
$s_1, s_2 \ll 1$, $(1+s_1)(1+s_2)\approx 1+s_1+s_2$ — so treating fitness as additive is a reasonable
first model. Under it, and while the population hasn't yet run out of beneficial mutations to draw
on (roughly true for the first several thousand generations before the curve bends over), the rate
of evolution is a meaningful, roughly constant quantity to compute.

Work in the regime $\mu_b N \ll 1$: the mutation rate is low enough relative to the population size
that fixation of one mutation ($\sim (1/s)\ln N$) is much faster than the typical wait between
successive establishments, so — using the previous lecture's criterion — clonal interference does
not matter. Then:

- New mutations enter the population at rate $\mu_b N$ (each of $N$ individuals mutates at rate
  $\mu_b$).
- A mutation of effect $s$ establishes with probability of order $s$ (exactly $s$ in some models,
  $2s$ in others — the constant is model-dependent, the scaling is not).
- With nothing to compete against, every mutation that establishes eventually fixes, adding its full
  effect $s$ to the mean fitness — nothing is wasted.

Putting these together, the rate of evolution is
$$ v \equiv \frac{\Delta \bar w}{\Delta t} = \mu_b N \int p(s)\, s\cdot s\, ds = \mu_b N \langle s^2\rangle. $$

This is linear in $\mu_b$: doubling the mutation rate doubles the rate at which mutations enter and,
since nothing competes, doubles the rate of fixation. It is also linear in $N$: doubling the
population doubles the rate at which new mutations appear, and, provided $s$ is not so small that
near-neutral mutations start behaving specially (not the relevant regime for populations of order
$10^4$ or more), the establishment probability doesn't depend on $N$, so the fixation rate doubles as
well.

Why $\langle s^2\rangle$ and not $\langle s\rangle^2$: a mutation of size $s$ enters $v$ through two
independent factors of $s$ — once via its probability of establishing ($\propto s$) and once via the
size of the increment it delivers if it does ($=s$). Two powers of $s$ per successful mutation give
$\langle s^2\rangle$. For a delta distribution the distinction is invisible, since $\langle
s^2\rangle=\langle s\rangle^2$ trivially when $s$ only ever takes one value; making the distinction
vivid for a distribution with real spread needs a sharper example than a rough two-point sketch, and
that was left as an open thread in the lecture rather than finished.

## Where this breaks down: clonal interference and the Desai–Fisher–Murray model

Plotting $\log v$ against $\log N$ makes the crossover visible: for small $N$ it is a straight line
of slope $1$ (the $v\propto N$ result above). It cannot continue forever — once clonal interference
sets in, the curve bends below that line and grows more slowly.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Rate of evolution against population size on log-log axes: a straight slope-one line for small populations bending over to a shallower, logarithmic rise for large populations.">
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <line x1="45" y1="180" x2="280" y2="30" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <path d="M45,180 L120,120 L170,90 L210,68 L245,53 L280,42" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="150" y="75" text-anchor="middle" font-size="11" fill="currentColor">slope 1: v &#8733; N</text>
  <text x="245" y="35" text-anchor="middle" font-size="11" fill="currentColor">v &#8733; log N</text>
  <text x="170" y="208" text-anchor="middle" font-size="12" fill="currentColor">log N</text>
  <text x="15" y="105" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 15 105)">log v</text>
</svg>
<figcaption>Without clonal interference the rate of evolution grows linearly with population size;
once competing beneficial lineages are common the curve falls below the slope-one line and grows
only logarithmically.</figcaption>
</figure>

The mechanism: when two or more beneficial mutations are present at the same time, only one can
ultimately fix. The population effectively keeps the *maximum* of the competing gains rather than
their *sum*. Without competition you eventually get one mutation, then another, each adding its own
$s$; with competition you only keep the best of however many arose together, and the gap between
"sum" and "maximum" widens as the population grows and more lineages compete simultaneously. The rate
does not fall in absolute terms — it simply grows more slowly than it otherwise would, because some
beneficial mutations are wasted.

Solving for the rate of evolution *with* clonal interference, for a general distribution of effect
sizes, is a genuinely hard problem — hard experimentally and theoretically — and has been an active
research question for roughly the last decade. One tractable simplification, due to Desai, Fisher and
Murray (*Current Biology*, 2007), drops the distribution of effects altogether and assumes every
beneficial mutation has exactly the same effect $s$. The population's fitness distribution then
becomes a set of discrete classes at fitness $0, s, 2s, 3s, 4s,\dots$ relative to the least-fit class
present.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="Bars showing population abundance at discrete fitness classes 0, s, 2s, 3s, 4s, decreasing toward the leading edge, with the leading edge singled out as the nose that drives the wave forward.">
  <line x1="40" y1="170" x2="300" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="170" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <rect x="55" y="40" width="30" height="130" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="100" y="70" width="30" height="100" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="145" y="100" width="30" height="70" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="190" y="128" width="30" height="42" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="235" y="150" width="30" height="20" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="70" y="185" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="115" y="185" text-anchor="middle" font-size="11" fill="currentColor">s</text>
  <text x="160" y="185" text-anchor="middle" font-size="11" fill="currentColor">2s</text>
  <text x="205" y="185" text-anchor="middle" font-size="11" fill="currentColor">3s</text>
  <text x="250" y="185" text-anchor="middle" font-size="11" fill="currentColor">4s</text>
  <text x="250" y="145" text-anchor="middle" font-size="11" fill="currentColor">nose</text>
  <text x="170" y="15" text-anchor="middle" font-size="12" fill="currentColor">fitness relative to bulk</text>
</svg>
<figcaption>Most individuals sit in a bulk that grows exponentially without changing the population's
progress; a mutation acquired at the thin leading edge (the "nose") is what extends the whole
distribution forward and sets the rate of evolution.</figcaption>
</figure>

Most of the population sits in some roughly steady-shaped bulk across these classes; a mutation
picked up deep in the bulk doesn't change much, since everything there is already growing
exponentially relative to the mean. What matters is the leading edge, or "nose": individuals that
already carry several more mutations than the bulk. When one of *those* acquires yet another
mutation, it extends the front of the distribution further ahead, and it is this leading-edge process
that sets how fast the whole distribution — and hence the mean fitness — moves forward.

The model is still hard to solve exactly and the lecture does not reproduce the full derivation, but
for large $N$ the dominant behavior of the velocity is
$$ v \sim s^2 \ln N, $$
in place of the linear-in-$N$ result found without clonal interference. The $s^2$ is the same
combination as before (the delta-function case of $\langle s^2\rangle$); what clonal interference
changes is the $N$-dependence, from linear to logarithmic — a much smaller payoff from a larger
population once competing lineages are common. Real populations don't have every beneficial mutation
carrying exactly the same effect, so this is a first-order model, but the qualitative crossover from
linear to logarithmic growth is the point worth keeping.

## Rugged fitness landscapes: the beta-lactamase example

A fitness landscape is rugged — has more than one peak, or blocks some uphill paths — when there is
**epistasis**: the fitness effect of one mutation depends on which others are already present.
Weinreich (2006) turned this from a purely theoretical picture into something measured directly, in a
case where the interactions were known to matter: resistance conferred by the enzyme beta-lactamase
(TEM-1) to a beta-lactam antibiotic. All natural variants of the enzyme can break down an older drug
such as ampicillin, but they vary hugely in their ability to break down a newer one, cefotaxime — a
version with none of five specific point mutations is essentially unable to break it down at all,
while the version carrying all five breaks it down at very high rates. Of the five mutations, one is
in the promoter and roughly doubles or triples expression; the other four are protein-coding, each
changing a single amino acid.

Resistance was quantified by the **Minimum Inhibitory Concentration (MIC)**: the lowest antibiotic
concentration that stops growth of the population over a fixed window (20 hours), starting from a
standard cell density. In practice this is read off a dilution series (concentration stepped down by
a fixed factor from well to well) — the population grows up to some concentration and not above it,
and that boundary is the MIC. (The mapping from MIC to absolute fitness is itself nontrivial, but for
this landscape MIC is simply used as a monotonic stand-in for fitness.)

With five point mutations there are $2^5 = 32$ possible genotypes. Weinreich constructed all 32, in
the same genetic background, and measured the MIC of each — that is the entire experimental dataset
in the paper. Everything else is analysis of the resulting, completely measured fitness landscape,
which is itself unusual: a fitness landscape is normally something reasoned about abstractly, not
something fully mapped from real measurements.

The measured landscape had exactly **one peak** — the genotype carrying all five mutations. This
matters: if a population can only fix mutations that increase fitness at each step (evolution moves
only "uphill"), then starting from the ancestral genotype and always taking some uphill step, it is
guaranteed to reach that one peak eventually, no matter which uphill path it happens to take. A single
peak means there is no way to get trapped at a suboptimal local maximum.

The landscape is nonetheless rugged in a different, more precise sense. There are $5! = 120$ possible
orderings in which the five mutations could be acquired one at a time, but only $18$ of them have
fitness increasing at *every* step; the other $102$ are **selectively inaccessible**, because
somewhere along that ordering the next mutation on the path would have to be one that does not
increase MIC. A mutation that is neutral (or worse) is treated as unable to fix within a reasonable
time in a population of, say, $10^6$, when genuinely beneficial mutations are simultaneously
available elsewhere to out-compete it — the same competitive logic as clonal interference, applied
here to which paths are reachable rather than to speed. Even among the 18 monotonic orderings, not
all are equally likely to be realized in an actual population, since the paths branch with unequal
probability, so in practice only a handful of the 18 dominate.

The lecture's point in putting these two facts side by side: it is easy to read this landscape as
extremely rugged, since $102$ of $120$ naive orderings are blocked — but that overstates it. It is a
*moderately* rugged landscape, because there is still only one peak: ruggedness here constrains which
path evolution takes without being able to trap it anywhere. A later laboratory-evolution study on a
different antibiotic-resistance gene, from the same experimentalist, tested whether a landscape
measured this way can actually predict what happens when a population is evolved in the lab, and
found that — at least in some cases — it can: a hint that the course of evolution may be more
predictable than it would otherwise seem.

## Sources

- Transcript: `docs/computational-biology/mit-ocw/8591j-2014/recordings/recordings/efxjkhdbi6a.md`
  (MIT 8.591J, Systems Biology, Fall 2014). Timestamps [02:08]–[38:00] for the equivalence-principle
  discussion; [38:00]–[1:05:00] for the rate of evolution and the Desai–Fisher–Murray model;
  [1:05:00]–end for the Weinreich beta-lactamase landscape. Administrative remarks about an upcoming
  exam ([01:02]–[02:08]) are omitted as boilerplate.
- Referred to but not contained in this source: the lineage-tracking paper on the "equivalence
  principle" — named in the transcript as "Roy Kashoney's paper," almost certainly a mis-transcription
  of Roy Kishony; neither its title nor the figures it repeatedly points to (called "figure 3A" and
  "figure 4" in the lecture) are given, only described in speech.
- Desai, Fisher and Murray, *Current Biology*, 2007 — named and dated in the transcript, but its
  title and the full velocity expression are not given; only the model setup and the leading-order
  scaling $v\sim s^2\ln N$ are stated.
- Weinreich, 2006 — named and dated in the transcript (on beta-lactamase/cefotaxime resistance);
  described in enough quantitative detail (MIC assay, five mutations, 32 genotypes, 120 orderings,
  the 102/18 split) to reconstruct directly, though its title is not given.
- The previous lecture's derivation of the establishment probability ($\approx s$) and the fixation
  timescale ($\sim (1/s)\ln N$) is referred to ("you should be able to derive this") but is not part
  of this transcript.
- Whatever was actually drawn on the board — the real trajectory plots, the MIC dilution series, the
  abundance-vs-fitness sketch — exists in this source only as spoken description; the figures
  themselves are not part of the transcript.

---

[← 10. Single Molecules and Protein Bursts](10-single-molecules-and-protein-bursts.md) · [Contents](index.md) · [12. Three Views of Stochastic Kinetics →](12-three-views-of-stochastic-kinetics.md)
