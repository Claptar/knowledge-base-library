---
title: "6. Evolutionary Paths and Game Theory"
course: "MIT 8.591J 2014"
chapter: 6
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 6. Evolutionary Paths and Game Theory

## What this covers

Two questions fill this lecture. First, a worked review problem: given a small, fully specified
fitness landscape, which of two possible beneficial mutations does an evolving population actually
acquire first, and how do you decide whether the mutations even arise and fix one at a time rather
than competing with each other? This uses — without re-deriving — the Moran process, selection
coefficients, "establishment," and the comparison of timescales used to diagnose clonal interference
from earlier in the course. Second, the lecture opens **evolutionary game theory**: why the
machinery of game theory (payoff matrices, Nash equilibria) describes evolving populations without
any individual ever reasoning about anything, and why letting fitness depend on the make-up of the
population breaks the whole idea of a fixed fitness landscape. No board work survives in the source
for this lecture — it is audio only — so every matrix and diagram below is reconstructed from the
numbers spoken aloud, not copied from a slide.

## Which path up a rugged landscape?

The setup: a population of constant size $N=1000$ evolving under the Moran process, with a
per–base-pair mutation rate $\mu=10^{-6}$. Genotypes are length-2 binary strings — two loci, each
0 or 1 — and fitness is measured relative to the all-zero genotype:

| genotype | relative fitness |
|---|---|
| $00$ | $1$ |
| $01$ | $1.02$ |
| $10$ | $1.1$ |
| $11$ | $1.2$ |

The population starts as 1000 copies of $00$. Mutations are assumed to run only $0\to1$ at each
locus (so $00\to11$ is reachable only via $01$ or $10$), and the question is: **which of the two
intermediate genotypes does the population pass through on its way to the peak, and with what
probability?**

<figure>
<svg viewBox="0 0 320 240" role="img" aria-label="Two mutational routes from genotype 00 to the fitness peak 11, through the intermediates 01 and 10">
  <defs>
    <marker id="arrowLandscape" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="160" y1="199" x2="94" y2="146" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowLandscape)"/>
  <line x1="160" y1="199" x2="226" y2="146" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowLandscape)"/>
  <line x1="90" y1="134" x2="153" y2="51" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowLandscape)"/>
  <line x1="230" y1="134" x2="167" y2="51" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowLandscape)"/>
  <circle cx="160" cy="205" r="4" fill="currentColor"/>
  <circle cx="90" cy="140" r="4" fill="currentColor"/>
  <circle cx="230" cy="140" r="4" fill="currentColor"/>
  <circle cx="160" cy="45" r="4" fill="currentColor"/>
  <text x="160" y="224" text-anchor="middle" font-size="12" fill="currentColor">00, fitness 1</text>
  <text x="15" y="140" text-anchor="start" font-size="12" fill="currentColor">01, fitness 1.02</text>
  <text x="235" y="140" text-anchor="start" font-size="12" fill="currentColor">10, fitness 1.1</text>
  <text x="160" y="24" text-anchor="middle" font-size="12" fill="currentColor">11, fitness 1.2</text>
  <text x="90" y="180" text-anchor="middle" font-size="11" fill="currentColor">S=0.02</text>
  <text x="230" y="180" text-anchor="middle" font-size="11" fill="currentColor">S=0.1</text>
</svg>
<figcaption>The two routes from the ancestral genotype to the fitness peak. Both steps are strongly
selected, so once one fixes the population cannot drift back down; the only open question is which
intermediate is reached first, decided by the relative rates $\mu N S_{01}$ and $\mu N S_{10}$.</figcaption>
</figure>

**Two different questions, easy to conflate.** A first, tempting calculation: if you already had
one copy of a $01$ mutant and one copy of a $10$ mutant sitting in the population together, the
probability that the $01$ lineage is the one that fixes is (probability $01$ survives stochastic
extinction) $\times$ (probability $10$ goes extinct) $\approx 0.02\times0.9$. That is a real
calculation, but it answers a different question — it assumes both mutants are already present as
single copies, competing. The question actually being asked starts the population as pure $00$ and
lets mutations arise at rate $\mu$ per division; it asks which mutation is more likely to be the one
that establishes and fixes first, given that mutations of each kind are constantly, randomly being
sampled.

**Step 1 — check the regime.** Recall that a mutation is "nearly neutral" when $|S|N\lesssim1$ and
strongly selected when $|S|N\gg1$; only in the latter case is the probability that a single new
mutant survives stochastic extinction well approximated by $S$ itself (Haldane's approximation).
Taking the smaller of the two selection coefficients, $S_{01}=0.02$, gives $S_{01}N=20\gg1$, and
$S_{10}N=100$ is larger still — both mutations are strongly beneficial, not nearly neutral. So:

$$P(\text{a new } 01 \text{ mutant survives stochastic extinction}) \approx S_{01}=0.02,\qquad
P(\text{a new } 10 \text{ mutant survives}) \approx S_{10}=0.1.$$

Surviving stochastic extinction is what the course calls becoming **established**: growing to
roughly $1/S$ copies, at which point fixation is essentially guaranteed. For $S_{01}=0.02$ that is
about 50 individuals.

**Step 2 — check for clonal interference.** Establishing is only the same thing as fixing if no
second mutant lineage is competing with the first while it fixes. That is decided by comparing two
timescales: the typical time between successive establishment events, $\sim 1/(\mu N S)$, against
the typical time for an established lineage to sweep to fixation, $\sim (1/S)\log(NS)$. There is no
clonal interference exactly when the first time is much longer than the second:

$$\mu N \log(NS) \ll 1.$$

Since $\log(NS)$ grows with $S$, the conservative check uses the *larger* selection coefficient,
$S_{10}=0.1$: $\mu N \log(NS_{10}) = 10^{-6}\cdot10^3\cdot\log(100) \approx 10^{-3}\times4.6\approx
5\times10^{-3}\ll1$. So clonal interference can be ignored: mutations appear, and each one's fate —
extinction or fixation — is resolved before the next relevant mutation appears. (The probability of
both loci mutating in the same generation is $\mu^2=10^{-12}$, negligible, so the direct jump
$00\to11$ is not in play either.)

**Step 3 — treat it as a chemical reaction.** With no clonal interference, the population sits in
state $00$ and transitions to $01$ or $10$ at *effective rates*, exactly like two parallel channels
of a chemical reaction:

$$k_{00\to01}=\mu N S_{01}, \qquad k_{00\to10}=\mu N S_{10}.$$

The probability that the population's first successful step is to $01$ rather than $10$ is the
branching ratio

$$P(00\to01) = \frac{k_{00\to01}}{k_{00\to01}+k_{00\to10}} = \frac{S_{01}}{S_{01}+S_{10}} =
\frac{0.02}{0.12} = \frac{1}{6}.$$

This is *not* the naive ratio $S_{01}/S_{10}=1/5$ that a quick glance might suggest — that ratio
answers the "already-competing single mutants" question above, not this one.

**Why the population can't backtrack, and why it is certain to reach the peak.** Both steps are
non-neutral in the *forward* direction, which means the reverse step (say $01\to00$) is a
non-neutral *deleterious* mutation — not merely unfavoured but exponentially suppressed. As a small
check, strip the problem down to just $00$ (fitness 1) and $01$ (fitness $r=1.02$). The forward rate
is $\mu N S_{01}\approx2\times10^{-5}$ per unit time. The backward rate needs the exact Moran
fixation probability for a single mutant of relative fitness $r$ in a population of size $N$,

$$P_{\text{fix}}(r)=\frac{1-1/r}{1-1/r^{N}},$$

applied with $r=1/1.02$ (the $00$-type is now the disadvantaged mutant against an all-$01$
background). Since $1.02^{1000}\approx e^{1000\ln1.02}\approx4\times10^{8}$, this works out to
$P_{\text{fix}}\approx0.02/(4\times10^{8})\sim5\times10^{-11}$ — far smaller than the neutral value
$1/N=10^{-3}$, as it must be for a genuinely deleterious mutation. The backward rate $\mu N
P_{\text{fix}}$ is therefore many orders of magnitude below the forward rate: once a step fixes, it
is effectively a ratchet. Combined with the observation that both intermediates are dead ends only
in the sense that they must eventually mutate onward (there is no other allowed move), the
population is *guaranteed*, with probability 1, eventually to reach the peak $11$ — the only
question was ever about the path, never about the destination.

One more remark for the strongly-selected, low-mutation-rate regime this problem sits in: over long
times the distribution over genotypic states satisfies detailed balance and behaves like a
thermodynamic system, with fitness playing the role of energy and population size setting how
sharply the distribution peaks — the relative equilibrium weight of two states scales as the ratio
of their fitnesses raised to the power $N$. With $N=1000$, even a fitness ratio as modest as $1.1$
raised to the $1000$th power is enormous, so almost all of the equilibrium probability sits at the
peak.

**What changes at higher mutation rates.** If $\mu$ were large enough that clonal interference did
matter, the outcome would flip: once several mutant lineages are established simultaneously, the
fitter one (larger $S$, here the $10$ mutant) essentially always wins the competition, so the
population is driven almost deterministically through the higher-fitness intermediate rather than
splitting probability between the two routes. Push the mutation rate higher still, and the
population need not fix an intermediate at all — a lineage can cross directly to the double mutant
while still a minority, without ever fixing $01$ or $10$. This "crossing a fitness valley" has the
same exponential-suppression flavour as tunnelling in quantum mechanics, and there is a literature
on the rate at which it happens (pointed to as optional reading, not covered here).

## Evolutionary game theory needs no rational player

The second half of the lecture opens a new topic with one deliberate framing move: **evolutionary
game theory borrows the vocabulary of game theory — strategies, payoffs, Nash equilibria — without
borrowing its usual assumption of rationality.** Ordinary game theory (as in the puzzles built on
"if he knows that I know that he knows...") assumes players reason about each other's reasoning.
Biological populations do nothing of the sort. Instead: mutations occasionally sample a different
strategy at random, individuals following a more profitable strategy leave more descendants, and
the population's composition drifts toward the same equilibria that a rational analysis would
predict — without any actual reasoning taking place anywhere. It is evolution *to* the solutions of
the game, never evolution *by* solving it.

**Why this needs its own theory at all: frequency-dependent fitness kills the fitness landscape.**
Everything done with the rugged-landscape problem above assumed each genotype has one fixed fitness
number. That assumption can fail. If the fitness of a genotype depends on the composition of the
rest of the population — how many other individuals are playing which strategy — then there is no
longer a single number to assign to that genotype, and *no fitness landscape can be drawn at all*.
The sharp version of the point: measuring the fitness of a pure population of genotype 0 (say,
fitness 1) and of a pure population of genotype 1 (say, fitness 1.2) does **not** tell you which one
wins in a mixed population. It is entirely possible for genotype 0 to out-compete genotype 1 once
they are mixed together, even though genotype 1 looked fitter in isolation. That is the basic
insight evolutionary game theory exists to handle.

## Two-player games as population interactions

The formal object is a **symmetric two-player game**: two strategies (say 1 and 2), and a payoff
matrix $M$ whose entry $M_{ij}$ is the payoff to a focal player using strategy $i$ against an
opponent using strategy $j$. Symmetry means the opponent's payoff in the same encounter is $M_{ji}$
— you can read off both players' payoffs from one matrix. Ported to a population: instead of one
named opponent, a focal individual meets a random member of the population, so an individual
playing strategy $i$ against a population in which strategy $j$ has frequency $f_j$ collects
expected payoff $\sum_j M_{ij}f_j$. Reading convention, stated the way it came up repeatedly: **the
row is the one thing an individual controls (their own strategy); the column is set by the rest of
the population.**

A **Nash equilibrium** is a strategy such that, if the whole population (or opponent) is playing it,
no individual has an incentive to switch to a different strategy — switching cannot increase their
own payoff. A **strict** Nash equilibrium is the stronger statement that switching strictly
*decreases* payoff; an ordinary (non-strict) Nash equilibrium only requires that switching does not
help, and leaves open the possibility that it is perfectly neutral.

## The Prisoner's Dilemma: one strategy dominates

The best-known example needs two strategies, Cooperate ($C$) and Defect ($D$), and a payoff matrix
(rows and columns both ordered $C,D$; entries are the row player's payoff):

$$M=\begin{pmatrix}3 & 0\\ 5 & 1\end{pmatrix}.$$

So: mutual cooperation pays 3 to each; mutual defection pays 1 to each; a defector meeting a
cooperator gets 5 (the "temptation" payoff) while the cooperator gets 0 (the "sucker's" payoff).
Defecting is strictly better *whatever the opponent does*: against a cooperator, $5>3$; against a
defector, $1>0$. So $D$ is a dominant strategy, and dominance makes all-$D$ the unique (strict) Nash
equilibrium — even though both players would be better off at all-$C$, where each gets 3 rather than
1. Nobody has an individual incentive to move there and stay: a lone cooperator in a population of
defectors is punished (payoff 0 instead of 1), so $C$ is not evolutionarily stable, while a lone
defector in a population of cooperators is rewarded (payoff 5 instead of 3), so $D$ always invades.

<figure>
<svg viewBox="0 0 300 210" role="img" aria-label="Payoff to a cooperator and a defector as a function of the fraction of the population that cooperates, in the Prisoner's Dilemma">
  <defs>
    <marker id="arrowPD" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="40" y1="170" x2="282" y2="170" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowPD)"/>
  <line x1="40" y1="180" x2="40" y2="15" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowPD)"/>
  <line x1="40" y1="170" x2="270" y2="80" stroke="currentColor" stroke-width="2"/>
  <line x1="40" y1="140" x2="270" y2="20" stroke="currentColor" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="160" y="196" text-anchor="middle" font-size="12" fill="currentColor">fraction cooperator, f_C</text>
  <text x="15" y="95" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 15 95)">payoff</text>
  <text x="250" y="70" text-anchor="start" font-size="12" fill="currentColor">cooperator</text>
  <text x="250" y="15" text-anchor="start" font-size="12" fill="currentColor">defector</text>
</svg>
<figcaption>Expected payoff to a cooperator (solid) and a defector (dashed) as the fraction of
cooperators in the population, $f_C$, varies from 0 to 1. The defector's line lies above the
cooperator's line everywhere, so whatever the starting composition, selection drives $f_C\to0$ — even
though the mean population payoff is higher at $f_C=1$ (payoff 3) than at $f_C=0$ (payoff 1).</figcaption>
</figure>

A subtlety raised in class and worth flagging without dwelling on it: if the temptation payoff were
raised from 5 to 7, the single-shot Nash equilibrium is unchanged (still all-defect), but now
$2\times3=6 < 7+0$, meaning two players who *could* coordinate turn-taking would earn more on
average by alternating cooperation and defection than by mutual cooperation. That is a fact about
repeated games between agents who can coordinate, not about the one-shot equilibrium computed here;
the payoffs in this example (temptation 5, not 7) were chosen precisely so that this complication
does not arise.

## Bi-stability and coexistence: when the lines cross

Not every two-strategy game has one strategy dominating the other everywhere. Plotting each
strategy's payoff against the population composition, as above, the only thing that matters for a
linear (two-player, two-strategy) game is whether and how the two lines cross:

- **No crossing (dominance):** one strategy is better regardless of composition — the Prisoner's
  Dilemma above. The dominant strategy fixes regardless of where the population starts.
- **Crossing, each strategy favoured when *common*:** self-reinforcing, giving **bi-stability** —
  two stable pure endpoints (all-$A$ or all-$B$, whichever the population starts closer to) and an
  unstable equilibrium at the crossing point. Both pure states are Nash equilibria. A matrix with
  this property (rows/columns ordered $A,B$):
  $$M=\begin{pmatrix}5&0\\3&1\end{pmatrix}.$$
  All-$A$ is Nash: a lone individual switching to $B$ against an all-$A$ population drops from
  payoff 5 to 3. All-$B$ is Nash too: switching to $A$ against an all-$B$ population drops from 1 to
  0.
- **Crossing, each strategy favoured when *rare*:** anti-coordination, giving **coexistence** — a
  single stable interior equilibrium, reached from any mixed starting composition, and *neither*
  pure state is a Nash equilibrium. This is the structure of the classic **Hawk–Dove** game. With
  the numbers used in the lecture (rows/columns ordered $A,B$):
  $$M=\begin{pmatrix}3&1\\5&0\end{pmatrix},$$
  at an all-$A$ population a lone $B$-mutant does better than the resident (5 against 3), and at an
  all-$B$ population a lone $A$-mutant does better than the resident (1 against 0) — each strategy
  is punished for being common and rewarded for being rare, so neither pure state resists invasion.

<figure>
<svg viewBox="0 0 380 230" role="img" aria-label="Two ways two payoff lines can cross: bi-stability, with an unstable interior point and stable ends, versus coexistence, with a stable interior point">
  <defs>
    <marker id="arrowGame" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <text x="90" y="15" text-anchor="middle" font-size="12" fill="currentColor">bi-stability</text>
  <line x1="30" y1="170" x2="155" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="170" x2="150" y2="20" stroke="currentColor" stroke-width="2"/>
  <line x1="30" y1="140" x2="150" y2="80" stroke="currentColor" stroke-width="2" stroke-dasharray="6 4"/>
  <circle cx="70" cy="120" r="3" fill="currentColor"/>
  <text x="70" y="134" text-anchor="middle" font-size="10" fill="currentColor">unstable</text>
  <line x1="65" y1="182" x2="42" y2="182" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowGame)"/>
  <line x1="75" y1="182" x2="138" y2="182" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowGame)"/>
  <text x="30" y="198" text-anchor="middle" font-size="10" fill="currentColor">all B</text>
  <text x="150" y="198" text-anchor="middle" font-size="10" fill="currentColor">all A</text>

  <text x="280" y="15" text-anchor="middle" font-size="12" fill="currentColor">coexistence</text>
  <line x1="220" y1="170" x2="345" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="220" y1="140" x2="340" y2="80" stroke="currentColor" stroke-width="2"/>
  <line x1="220" y1="170" x2="340" y2="20" stroke="currentColor" stroke-width="2" stroke-dasharray="6 4"/>
  <circle cx="260" cy="120" r="3" fill="currentColor"/>
  <text x="260" y="134" text-anchor="middle" font-size="10" fill="currentColor">stable</text>
  <line x1="235" y1="182" x2="255" y2="182" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowGame)"/>
  <line x1="325" y1="182" x2="265" y2="182" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowGame)"/>
  <text x="220" y="198" text-anchor="middle" font-size="10" fill="currentColor">all B</text>
  <text x="340" y="198" text-anchor="middle" font-size="10" fill="currentColor">all A</text>

  <text x="190" y="218" text-anchor="middle" font-size="11" fill="currentColor">solid = strategy A, dashed = strategy B</text>
</svg>
<figcaption>Solid line is strategy $A$'s payoff, dashed is $B$'s, plotted against the fraction of the
population playing $A$. Left: each strategy does best where it is already common, so the interior
crossing repels and the population runs to whichever pure state it started nearer. Right: each
strategy does best where it is rare (Hawk–Dove), so the interior crossing attracts from both sides
and the population settles into a stable mixture.</figcaption>
</figure>

For the Hawk–Dove matrix above, setting the two payoffs-as-a-function-of-frequency equal,
$1+2f_A=5f_A$, gives an equilibrium frequency $f_A^*=1/3$ — the composition at which a Hawk-playing
individual and a Dove-playing individual have exactly equal fitness.

## Nash's theorem and mixed strategies

Neither pure strategy is a Nash equilibrium in the Hawk–Dove game — yet the lecture is emphatic that
the game still *has* a Nash equilibrium, once **mixed (probabilistic) strategies** are allowed: this
is what Nash proved, in the short paper (cited in the lecture as a one-page result published in
PNAS) for which he is remembered, that every such game has at least one Nash equilibrium in this
broader sense, no matter how many strategies or players are involved.

The defining feature of a mixed Nash equilibrium is that, at the equilibrium probability, **every
strategy — and every mixture of strategies — yields exactly the same expected fitness.** If the
equilibrium plays $A$ with probability $p^*$, then $\pi_A(p^*)=\pi_B(p^*)$, and this equality (rather
than a strict inequality) is exactly what it takes for the equilibrium condition (switch cannot
*increase* payoff) to hold with equality: no incentive to change strategy, but also no active
penalty for changing it. It is a Nash equilibrium, but not a strict one — and, the lecture notes,
this is the sense in which such an equilibrium is an **evolutionarily stable strategy (ESS)**.

**Two different biological pictures realise the same equilibrium fraction.** Suppose the
population-level equilibrium is "play $A$ with frequency $f_A^*$." That can be implemented by:

1. **Genetic diversity** — two distinct genotypes, one committed to $A$ and one to $B$, coexisting
   stably at frequencies $f_A^*$ and $1-f_A^*$: genetic diversity producing phenotypic diversity.
2. **A single genotype playing the mixed strategy itself** — every individual genetically identical,
   each one independently playing $A$ with probability $p=f_A^*$: phenotypic heterogeneity with no
   genetic diversity at all.

Both are consistent with, and realise, the same solution to the same game.

**A biological instance.** Wild-type yeast, in some environments, activates the genes needed to
metabolise the sugar galactose bimodally or stochastically — within a genetically identical
population, some cells switch the genes on and others do not. Mutants locked permanently "on" and
permanently "off" were made and set to compete; the two strategies evolved toward *coexistence* at
some equilibrium mixture — exactly the Hawk–Dove structure above. That does not prove why the
stochastic behaviour evolved (the lecture is explicit that evolutionary origins generally cannot be
proven, only supported by testable hypotheses), but it makes it plausible that the wild type's own
stochastic switching between "on" and "off" is a single genotype implementing the mixed-strategy
solution of a frequency-dependent game, rather than requiring two separate genotypes to coexist. A
second, complementary explanation — **bet hedging**, where diversifying strategies helps a clonal
population cope with an uncertain or fluctuating environment even with no frequency-dependent payoff
at all — was flagged as a topic for a later lecture rather than covered here.

## Sources

All content is from the single transcript-only recording `a8fbmj4nixy` (MIT 8.591J, Fall 2014,
converted from `sources/ocw-8591j-2014/recordings/a8fbmj4nixy-captions.srt`, CC BY-NC-SA 4.0). This
lecture has no accompanying slides, notes or problem set in the supplied material, and no board work
survives — every matrix, graph and diagram in this chapter is reconstructed from numbers and
descriptions spoken aloud, not copied from a visual source.

- Rugged-landscape review problem, setup through the branching-ratio answer and the ratchet/detailed-
  balance discussion: **[01:07]–[31:59]**.
- Worked reversion-rate example (two-state toy model, exact Moran fixation probability): **[32:04]–
  [37:40]**.
- Clonal-interference limit and the pointer to fitness-valley "tunnelling": **[37:40]–[38:47]**.
- No rationality needed / frequency-dependent fitness / no fitness landscape: **[38:47]–[44:26]**.
- Payoff-matrix formalism and reading convention: **[45:33]–[48:02]**.
- Prisoner's Dilemma, Nash equilibrium, dominance, the temptation-payoff aside: **[48:02]–[57:12]**.
- Payoff-vs-frequency plot and the dominance figure: **[57:12]–[1:03:26]**.
- Bi-stability example: **[1:03:26]–[1:09:06]**.
- Hawk–Dove, coexistence, Nash's existence theorem: **[1:09:06]–[1:13:41]**.
- Mixed strategies, ESS, genetic-vs-phenotypic diversity, yeast galactose example, bet-hedging
  pointer: **[1:13:41]–[1:20:30]**.

Named but not contained in this source, and not reconstructed here:

- The **Weinreich paper** and its measured fitness landscape (32 genotypes, minimum inhibitory
  concentration), discussed in the *previous* lecture and referred to only as background for the
  review problem — **[01:07]**.
- The assigned textbook reading behind the two-player game payoff tables ("Chapter Four," and later
  "it's explained in the book as well") — title and author not stated in the transcript — **[46:59],
  [1:20:30]**.
- Nash's original one-page paper, published in PNAS — cited by venue only, not by title — **[1:12:30]**.
- An unnamed paper in the *Journal of Theoretical Biology*, listed as optional reading in the course
  syllabus, on the rate of crossing fitness valleys — **[38:47]**.
- Later-lecture material on bet hedging under environmental uncertainty, flagged as coming but not
  covered in this session — **[1:16:07]**.

---

[← 5. Cost-Benefit Optimization and Statistical Evidence](05-cost-benefit-optimization-and-statistical-evidence.md) · [Contents](index.md) · [7. Anticipatory Regulation and Bet Hedging →](07-anticipatory-regulation-and-bet-hedging.md)
