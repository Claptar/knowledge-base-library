---
title: "7. Anticipatory Regulation and Bet Hedging"
course: "MIT 8.591J 2014"
chapter: 7
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 7. Anticipatory Regulation and Bet Hedging

## What this covers

Why does a clonal bacterial population sometimes look genetically diverse when it is not? This
chapter works through three distinct evolutionary answers, built around two papers the lecture
treats as a matched pair: one on gene regulation that *anticipates* a predictable future
environment (Tagkopoulos et al., Mitchell et al.), and one on gene expression that goes
*heterogeneous* in a population facing an unpredictable one. It assumes the reader already has
the idea of a Nash equilibrium from an earlier lecture in the course (game theory is used but not
re-derived here), and basic comfort with fitness as a growth rate.

## Direct sensing versus anticipating the future

Take a bacterium moving between two environments that present two different cues, $S_1$ and
$S_2$, each of which calls for its own response, $R_1$ and $R_2$. The naive strategy is **direct
sensing**: $S_1$ drives $R_1$, $S_2$ drives $R_2$, and that is all. (These arrows need not even be
all-or-nothing — $S_1$ could drive $R_1$ strongly and $R_2$ only weakly.)

The interesting alternative is that a cue *pre-activates* the response to a cue it hasn't seen
yet, because in the organism's normal life history the two cues are correlated. This is
**anticipatory regulation**, and the lecture's classic frame for it is Pavlovian conditioning: ring
a bell, then give the dog food, and eventually the bell alone makes the dog salivate. The bell
($S_1$) has come to drive the food response ($R_2$) because in the dog's experience one reliably
precedes the other. The question for a cell is whether something structurally identical could
evolve without any nervous system at all, just from selection acting on a gene network — and
whether it has.

Two versions of this idea appear in the readings, and they differ in exactly one thing: whether the
cross-activation runs both ways.

<figure>
<svg viewBox="0 0 760 220" role="img" aria-label="Three regulatory architectures: direct sensing, symmetric anticipatory regulation, and asymmetric anticipatory regulation">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <text x="110" y="22" text-anchor="middle" font-size="12" fill="currentColor">direct sensing</text>
  <line x1="72" y1="80" x2="148" y2="80" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="72" y1="150" x2="148" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <circle cx="65" cy="80" r="3" fill="currentColor"/><text x="65" y="65" text-anchor="middle" font-size="12" fill="currentColor">S1</text>
  <circle cx="65" cy="150" r="3" fill="currentColor"/><text x="65" y="168" text-anchor="middle" font-size="12" fill="currentColor">S2</text>
  <circle cx="155" cy="80" r="3" fill="currentColor"/><text x="155" y="65" text-anchor="middle" font-size="12" fill="currentColor">R1</text>
  <circle cx="155" cy="150" r="3" fill="currentColor"/><text x="155" y="168" text-anchor="middle" font-size="12" fill="currentColor">R2</text>

  <text x="380" y="22" text-anchor="middle" font-size="12" fill="currentColor">symmetric anticipatory</text>
  <line x1="342" y1="80" x2="418" y2="80" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="342" y1="150" x2="418" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="342" y1="80" x2="418" y2="150" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="342" y1="150" x2="418" y2="80" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <circle cx="335" cy="80" r="3" fill="currentColor"/><text x="335" y="65" text-anchor="middle" font-size="12" fill="currentColor">S1</text>
  <circle cx="335" cy="150" r="3" fill="currentColor"/><text x="335" y="168" text-anchor="middle" font-size="12" fill="currentColor">S2</text>
  <circle cx="425" cy="80" r="3" fill="currentColor"/><text x="425" y="65" text-anchor="middle" font-size="12" fill="currentColor">R1</text>
  <circle cx="425" cy="150" r="3" fill="currentColor"/><text x="425" y="168" text-anchor="middle" font-size="12" fill="currentColor">R2</text>

  <text x="650" y="22" text-anchor="middle" font-size="12" fill="currentColor">asymmetric anticipatory</text>
  <line x1="612" y1="80" x2="688" y2="80" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="612" y1="150" x2="688" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="612" y1="80" x2="688" y2="150" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <circle cx="605" cy="80" r="3" fill="currentColor"/><text x="605" y="65" text-anchor="middle" font-size="12" fill="currentColor">S1</text>
  <circle cx="605" cy="150" r="3" fill="currentColor"/><text x="605" y="168" text-anchor="middle" font-size="12" fill="currentColor">S2</text>
  <circle cx="695" cy="80" r="3" fill="currentColor"/><text x="695" y="65" text-anchor="middle" font-size="12" fill="currentColor">R1</text>
  <circle cx="695" cy="150" r="3" fill="currentColor"/><text x="695" y="168" text-anchor="middle" font-size="12" fill="currentColor">R2</text>
</svg>
<figcaption>Direct sensing has each stimulus drive only its own response. Symmetric anticipatory
regulation (temperature/oxygen) adds a cross-activation arrow in both directions. Asymmetric
anticipatory regulation (lactose/maltose) adds only one of the two — the one corresponding to the
stimulus that is actually predictive of the other.</figcaption>
</figure>

## Symmetric anticipatory regulation: temperature and oxygen

*E. coli* live part of their life cycle in the mammalian gut, and entering it means a
characteristic, correlated change in conditions: temperature rises and oxygen availability drops
at the same time. Tagkopoulos et al. (*Science*, 2008) showed that exposing *E. coli* to a
temperature rise turns on not only the genes needed to survive heat, but also the genes needed to
survive low oxygen — and exposure to low oxygen turns on the heat-response genes too. The
cross-activation runs both ways, hence *symmetric*.

A cheap objection is that this could just mean the same genes happen to help against both
stresses — not a "predictive" regulatory link at all, just one response that happens to cover two
problems. The way to rule that out is to break the correlation experimentally: evolve a population
in an environment where temperature changes but oxygen doesn't, and see whether the unnecessary
cross-activation arrow disappears. It does — the cross-regulation can be selectively removed,
which argues that it really was a distinct, evolved link between the two cues rather than a
side-effect of two response programs sharing components.

Why would symmetric — cross-activation both ways — ever be worth it, rather than each cue only
predicting its own future need? Two considerations came up. First, when both cues are individually
noisy predictors of "you are now in a gut," seeing both together is much stronger evidence than
seeing either alone, and this also controls false positives: if each cue fires spuriously at some
low rate, the two firing together at the same time is far rarer, so requiring (or reinforcing on)
both lowers the false-alarm rate. Second, if there's no reliable temporal order between the two
cues — they arrive together rather than one before the other — there's no basis for making one of
them the "leading" predictor, which pushes the design toward symmetry.

## Asymmetric anticipatory regulation: lactose before maltose

Mitchell et al. (*Nature*, 2009) is built around a case where there *is* a reliable order: bacteria
entering a mammalian gut typically encounter lactose before they encounter maltose (lactose comes
from milk, and young mammals drink milk; adults mostly do not, so an adult gut may present maltose
with no lactose at all). What they found is that exposure to lactose pre-activates the maltose
(*mal*) genes — not to the same level as exposure to maltose itself, but well above the baseline
for other carbon sources — while exposure to maltose does **not** pre-activate the lactose genes.
The cross-activation only runs one way: *asymmetric*.

**Why asymmetric survives even though the correlation is weak.** Only about 10% of the time that
*E. coli* encounter maltose did they see lactose first. That sounds like it should scotch the whole
idea, but the cost-benefit accounting is one-sided. When maltose shows up with no preceding
lactose, the anticipatory strategy and plain direct sensing behave *identically* — both are simply
surprised and switch on the *mal* genes on contact, at the same cost. The only place the two
strategies diverge is after seeing lactose: the anticipatory strategy pays a cost by activating the
*mal* genes early, and that cost is worth paying only if maltose reliably follows lactose closely
enough in time. It has nothing to do with what fraction of *maltose* encounters were preceded by
lactose — only with what fraction of *lactose* encounters are followed by maltose soon after.

**What it takes to show the mechanism actually evolved for this purpose**, and not just observed
by chance in one strain, the lecture distilled to three requirements the paper had to establish:

1. **Fitness**: pre-exposure to $S_1$ (lactose) increases fitness under $S_2$/$R_2$ (maltose) —
   i.e., seeing lactose first genuinely helps when maltose arrives.
2. **Cost**: there is a real cost to up-regulating $R_2$ (the *mal* genes) when it turns out not to
   be needed — otherwise there's nothing to explain, since a free response would always be worth
   having.
3. **Specificity**: it is specifically lactose that pre-activates the *mal* genes, and other sugar
   sources should not.

The evidence assembled for each: cross-activation is present in more than one *E. coli* strain, not
just theirs (adding generality, and also — worth noting honestly — this particular cross-regulation
of the *mal* genes by lactose had already been reported by someone else). Most tellingly, they
compared the wild-type strain to one that had been laboratory-evolved for 500 generations in
lactose alone — evolved by a different group, for a different purpose, and simply reused here
rather than repeated from scratch, since redoing three months of daily dilutions to get the same
strain would have been pointless. In that lactose-evolved strain, the anticipatory arrow is gone:
lactose exposure no longer pre-activates the *mal* genes. And in a separate measurement (their
Figure 3), the *fitness* benefit of pre-exposure is specific to the lactose-then-maltose ordering —
not maltose-then-lactose, not galactose-then-maltose, not sucrose-then-maltose — and that fitness
benefit is likewise absent in the lactose-evolved strain that lost the regulatory arrow. Losing the
regulation and losing the benefit together, in the same strain, is a stronger case than either
result alone.

*A brief aside on reading the figure itself*: the lecture points out that the paper's fitness data
(Figure 3) is presented as a figure with color-coded points — one color for the main comparison,
others for the various control orderings and for the extinction control — precisely because a
table of the same numbers would not make the argument visible. The advice offered for writing one's
own figures was to choose a color scheme that stays legible printed in black and white, not only on
screen (Bang Wong's series of short articles on figure design in *Nature Methods* was named as a
good source for this, but not itself part of the lecture's content).

The paper also treats a "stochastic switching" mechanism as a third alternative to direct sensing
and anticipatory regulation — cells switching into different response states at some rate
independent of a specific predictive cue. That is exactly the segue into the rest of the lecture:
stochastic switching between phenotypes, and why it might be favored by selection at all.

## Heterogeneity in a clonal population

Even a genetically identical population can look strikingly heterogeneous in one environment. The
lecture is explicit that observing this is not, by itself, evidence of anything adaptive: a trait
can be observed without having been selected for — it could be a side effect of something else
entirely. But when there *is* an evolutionary explanation, the lecture identifies three, and
warns against reflexively reaching for the first one:

| Explanation | Idea | Lecture's example |
|---|---|---|
| Bet hedging | stochastic diversification against an *unpredictable* environment | persister cells / antibiotic tolerance |
| Mixed strategy | equilibrium of a game played *within* the population | glucose/galactose bimodal expression in yeast |
| Altruistic self-sacrifice | division of labor, some individuals pay a lethal cost for relatives | colicin production |

## Bet hedging and the geometric mean

**The seed germination problem.** A desert annual plant releases seeds. Suppose it rains in 75% of
years and doesn't in the other 25%. A seed that germinates and gets rain goes on to produce, on
average, 2 seeds the following year; a seed that germinates without rain has only a 10% chance of
surviving, so its expected contribution is $0.1$ seed. A seed that does *not* germinate simply
survives to try again next year, contributing exactly 1 seed regardless of rain.

| | Rain (75% of years) | No rain (25% of years) |
|---|---|---|
| Germinate | $\times 2$ | $\times 0.1$ |
| Don't germinate | $\times 1$ | $\times 1$ |

Which is the better strategy, in the long run? The tempting shortcut — average the two outcomes
weighted by their frequency — is the wrong average. What matters for a quantity that *multiplies*
across generations is the **geometric mean**, not the arithmetic mean. Over a representative run
of four years matching the 3-to-1 ratio (three rain years, one drought), always-germinate multiplies
the population by
$$2 \times 2 \times 2 \times 0.1 = 0.8,$$
so the population *shrinks* by a factor of $0.8$ every four generations, while never-germinate
multiplies it by $1 \times 1 \times 1 \times 1 = 1$ — flat. In this instance, always sitting out
beats always germinating, even though germinating is the better bet in any single rainy year.

The reason the geometric mean is the right quantity, and not the arithmetic mean, is starkest in
the limit where the bad-year payoff goes to zero. If a germinated seed's survival probability in a
drought is exactly $0$, then always-germinating guarantees eventual extinction, full stop — the
population is certain to encounter a drought eventually, and one factor of zero erases everything
before it, no matter how good the good years were. An arithmetic mean of the two payoffs can still
look attractive (three factors of 2 outweigh one factor of $0$, arithmetically) while the true
long-run growth rate is exactly zero. It is precisely in this regime — a rare, catastrophic
environment with a payoff near zero for the "committed" phenotype — that bet hedging earns its
keep: instead of an all-or-nothing strategy, germinate with some probability $p$ and hold the rest
in reserve. That reserve need not be large — a small $p$ that leaves most seeds ungerminated most
of the time can still maximize the population's long-run growth rate, because it buys insurance
against the catastrophic year while still capturing most of the benefit of the good ones.

**Persister cells** are the microbial version of the ungerminated seed. In a population exposed to
antibiotics, only about one cell in $10^5$–$10^6$ enters a slow-growing, drug-tolerant "persister"
state. Growing slowly is a real cost — but because so few cells pay it, the cost to the population
as a whole is small. Add antibiotic and wait 12 hours, and the persisters are what's left; this
looks like resistance, but it is not: regrow that surviving population and it is once again fully
sensitive to the antibiotic. That reversibility is exactly what distinguishes phenotypic
(persister) tolerance from true genetic resistance, which arises independently at a much lower rate
(around one cell in $10^8$) and, being a mutation, is stable across generations rather than
reverting. The mechanism proposed for entering the persister state involves toxin–antitoxin
modules that are normally repressed but triggered stochastically at a low rate — though the lecture
flags this as a genuinely unsettled debate, complicated by the fact that any slow-dividing cell
tends to be broadly protected against many stresses, which makes it hard to tell a specific
persister mechanism apart from generic dormancy.

## Mixed strategies: heterogeneity from a game within the population

Bet hedging is about coping with an unpredictable *environment*. Mixed strategies are a different
mechanism entirely: heterogeneity that arises from a game played among members of the *same*
population, with no environmental uncertainty required at all.

**Hawk–Dove.** Two individuals meet over a resource worth $b$. A dove backs down rather than
fight; a hawk fights. If two doves meet, they split the resource: each gets $b/2$. If a hawk meets
a dove, the hawk takes the whole resource, $b$, and the dove gets $0$ (and avoids the fight). If
two hawks meet, they fight: each has a 50% chance of winning the whole resource and a 50% chance of
losing and paying the cost of the fight, $c$, for an expected payoff of $(b-c)/2$.

Assume the fight is not worth it on average, $b < c$ — the interesting regime. Then neither pure
strategy is a Nash equilibrium: starting from all-dove, a single individual does strictly better by
switching to hawk (getting $b$ instead of $b/2$, since it never has to fight); but hawk isn't stable
either, since $b<c$ means the equilibrium condition for hawk (which needs $b>c$) fails. What *is*
an equilibrium is a mixed strategy — play hawk with some probability $p^\ast$. Setting the expected
payoff of hawk equal to the expected payoff of dove against a population playing hawk with
probability $p$,
$$p\cdot\frac{b-c}{2} + (1-p)\, b \;=\; (1-p)\cdot\frac{b}{2},$$
and solving gives
$$p^\ast = \frac{b}{c}.$$
A bigger benefit pushes the equilibrium frequency of hawks up; a bigger cost of fighting pushes it
down — matching the intuition that fighting becomes more attractive exactly when it's more
rewarding and less costly.

This is **negative frequency-dependent selection**: whichever strategy is currently rare does
better than whichever is currently common. A lone hawk among doves does great; a lone dove among
hawks does great (it just avoids every fight). That pressure pushes the population toward the
equilibrium mix and holds it there — and the mix can be implemented either as two coexisting
genotypes (pure hawks and pure doves, at frequencies $p^\ast$ and $1-p^\ast$) or as one genotype
that plays hawk with probability $p^\ast$ on each encounter. Either way, it looks like phenotypic
heterogeneity in the population.

**Rock–paper–scissors** is the sharpest illustration of what a Nash equilibrium does and doesn't
mean. The equilibrium of that game is to play each of the three moves with probability $1/3$ — at
that mixture, no one has an incentive to deviate, *given* everyone else is playing it. But that
equilibrium is emphatically *not* the best response to any particular opponent: if you know your
opponent always plays rock, the best response is always paper, not $1/3$-$1/3$-$1/3$. A Nash
equilibrium is a description of stability under mutual best response, not a claim that the
equilibrium strategy is optimal against a given fixed strategy.

**A foraging-game reading of yeast on mixed sugars.** Yeast grown in a mix of glucose and galactose
show a bimodal response in the *GAL* genes (needed to metabolize galactose): measuring galactose-
pathway expression across single cells, some cells switch it on strongly and others don't switch
it on at all — a clonal population splitting into two visibly different phenotypes. One reading of
this, offered as work from the lecturer's own group, treats it as a foraging game: imagine a
population choosing between two food sources (blueberries and red berries, say). If everyone else
is eating blueberries, it pays you to switch to red berries — you don't have to share. If everyone
else switches to red berries, blueberries become the better choice. That is exactly the negative
frequency dependence of Hawk–Dove, transplanted to resource choice, and it again predicts
coexistence of the two phenotypes as the equilibrium — implementable either by two genotypes or by
one genotype expressing both phenotypes with some probability.

One thing this equilibrium does **not** do is maximize the population's total fitness. In
Hawk–Dove, a population that was entirely doves would do strictly better in aggregate than the
mixed equilibrium $p^\ast$ — but that all-dove state isn't stable, so it never gets there. The
lesson generalizes: a mixed-strategy explanation for heterogeneity is a claim about individual-level
stability under negative frequency dependence, not a claim that the observed mixture is good for
the population as a whole.

## Altruism and division of labor: colicin

The third explanation gives up individual payoff altogether. Many gram-negative bacteria, including
*E. coli*, carry plasmids encoding **colicins** — toxins — and the only way a cell releases its
colicin is by lysing: bursting open and dying. The same plasmid also encodes an **immunity
protein**, so a cell that lyses kills competing bacteria that lack the plasmid, while other cells
that *do* carry the plasmid (and are therefore protected by the immunity protein) are unharmed.
This is kin selection in a strict, mechanistic sense: "relatedness" here means sharing that
particular plasmid, not genealogical kinship in the usual sense.

For the plasmid to spread, lysis has to be **stochastic and rare** — that's a strict requirement,
not an incidental detail. If every plasmid-carrying cell always lysed, the plasmid would simply
extinguish itself; it can never propagate. But if only a small fraction of the carriers — a
lecture's example is around 1% — lyse and release colicin at any given time, that fraction kills
off competing, non-carrying bacteria while the surviving majority of carriers, protected by the
immunity protein, benefits from the reduced competition. The plasmid spreads through the
population even though a minority of its own carriers dies to make that happen: altruistic
self-sacrifice, with the beneficiaries being the individual's genetic relatives in the relevant
sense — other carriers of the same toxin/immunity plasmid.

## Three explanations, one observation

Put together, phenotypic heterogeneity in a clonal population can arise from at least three
distinct evolutionary logics, and they are not interchangeable even though they can look similar
under a microscope:

- **Bet hedging** is a response to an *unpredictable environment*: it maximizes the long-run
  geometric growth rate of a single lineage and requires no interaction between individuals at all.
- **Mixed strategies** arise from a *game among individuals in the same population*: the
  equilibrium is set by negative frequency-dependent selection, and it need not maximize the
  population's total fitness.
- **Altruistic self-sacrifice** trades an individual's fitness for the fitness of its genetic
  relatives, via a mechanism (like a toxin/immunity plasmid) that only works if the sacrifice is
  rare.

Each makes different, falsifiable, experimentally distinguishable predictions — about who benefits,
about whether the observed mixture maximizes population growth or only individual payoff, about
whether the effect depends on environmental fluctuation at all. The lecture's parting point is a
methodological one: seeing heterogeneity and reaching immediately for "bet hedging" is a common
reflex in the field, but the other two explanations are, as far as anyone can tell, just as general
and just as common — which means the heterogeneity itself is never enough evidence on its own, and
distinguishing between the three requires designing the measurement, not just making the
observation.

## Sources

Recording `bjxcf6pfrha` (MIT 8.591J *Systems Biology*, Fall 2014). Transcript only — nothing
written on the board was captured, so the direct-sensing / symmetric / asymmetric diagram above is
reconstructed from the spoken description of the arrows between $S_1, S_2, R_1, R_2$.

- Anticipatory regulation, the Pavlovian frame, direct sensing vs. symmetric vs. asymmetric
  regulation, the Tagkopoulos and Mitchell papers, and the note on figure design: 00:00–46:50.
  - Referred to but not contained in this transcript: Kussell & Leibler, *Science* (2005) — the
    formal, information-theoretic treatment of switching among $n$ phenotypes and environments that
    this lecture treats as backdrop (named repeatedly, e.g. 01:09, 56:44); Tagkopoulos et al.,
    *Science* (2008), on symmetric anticipatory regulation of temperature/oxygen response (10:10–
    17:18); Mitchell et al., *Nature* (2009), the paper this half of the lecture works through
    (02:13–46:50), including a follow-up PNAS paper by Amir Mitchell developing its timing model in
    more detail (23:53); Bang Wong's series of articles in *Nature Methods* on figure and color
    design (42:25); the second half of the Mitchell et al. paper, on a parallel cross-protection
    story in yeast during fermentation, which the lecturer explicitly skipped (44:34).
- Phenotypic heterogeneity, its three evolutionary explanations, bet hedging, seed germination,
  the geometric mean, and persister cells: 47:54–1:04:30.
- Mixed strategies, Hawk–Dove, negative frequency-dependent selection, rock–paper–scissors, and the
  glucose/galactose foraging-game reading: 1:04:30–1:14:34.
  - Builds on an earlier class session on game theory ("about two weeks" prior) not included in
    this transcript; the glucose/galactose interpretation is attributed to the lecturer's own
    (unpublished, as presented here) group work (1:12:21).
- Altruism, division of labor, and colicin production: 1:14:34–1:17:56.
  - Flagged as a topic with a dedicated future reading not included here ("we're going to read more
    about this later," 1:15:47).

---

[← 6. Evolutionary Paths and Game Theory](06-evolutionary-paths-and-game-theory.md) · [Contents](index.md) · [8. Virulence Evolution and the Red Queen →](08-virulence-evolution-and-the-red-queen.md)
