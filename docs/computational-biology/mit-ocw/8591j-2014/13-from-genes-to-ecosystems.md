---
title: "13. From Genes to Ecosystems"
course: "MIT 8.591J 2014"
chapter: 13
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 13. From Genes to Ecosystems

## What this covers

This is the opening lecture of MIT's 8.591J *Systems Biology* (Fall 2014, taught by Jeff Gore, a
physicist), and it is not itself a piece of course content so much as a trailer for the whole
semester. After some administrative matters (stripped here, since none of it is science), the
lecture is a guided tour of the questions the course will spend the rest of the term on, in
roughly the order it will meet them. It answers two things: what "systems biology" means in this
course's sense of the term, and what arc of topics — from a single gene switching another on or
off, up to the collapse of a fishery — that meaning is going to be unpacked across. Nothing here is
derived in full; each idea is introduced at the level the lecture introduced it, and the fuller
treatment is left to the lectures that follow. The chapter assumes only ordinary scientific
literacy; the course itself assumes comfort with differential equations and probability, but none
of that machinery is actually used in this particular lecture.

## Two things called "systems biology"

The term is used by two communities that do not entirely overlap. This course sits in what Gore
calls the *physics-inspired* branch: simple models — from nonlinear dynamics or from stochastic
processes — combined with quantitative experiments, often on single cells, aimed at understanding
how a cell's decision-making actually works mechanistically. A second, *data-driven* branch, more
influenced by computer science and engineering, instead uses complex models and machine-learning
techniques to extract signal from large data sets; it is also trying to understand how global
cellular behavior emerges from many interactions, but the aesthetic and the daily practice are
different enough that the lecture explicitly points students toward parallel classes (taught the
same term, and the following spring) if that is the branch they actually want. Two textbooks anchor
the two halves of *this* course: Uri Alon's *An Introduction to Systems Biology* for the first part,
and Martin Nowak's *Evolutionary Dynamics* for the part on evolution.

## The question the course keeps coming back to

The organizing question, stated directly: how does interesting, complicated function arise from the
interaction of relatively simple parts at a lower level? The lecture motivates this with a piece of
1950s film of a neutrophil — an innate-immune cell, the body's first line of defense — chasing down
and eating a bacterium. Watching it, the striking thing is not just that the cell finds the
bacterium: it reads chemical cues to work out where the target is, ignores irrelevant red blood
cells in its path, pushes them aside, changes direction when the target moves, and eventually
catches it. All of that is sophisticated information processing — sensing, deciding, and then
converting the decision into mechanical force — and it happens with no nervous system at all, inside
a single cell. Humans do this kind of thing too, but we have $10^{12}$ or so neurons to do it with;
what is remarkable is that a single cell manages a version of it with none.

The course's answer to *how* is to work up the length scales: first the molecular interactions
inside one cell, then evolution acting on populations of cells over many generations, then whole
ecosystems of interacting species. This is a deliberate choice, and the lecture flags an opposing
one: Bill Bialek's *Biological Physics* explicitly avoids organizing bottom-up, because doing so
risks implying that we already understand how to get from the small scale to the large one, which
we do not. Gore's response is that the point of the whole effort is to try anyway — because,
whether or not the connection can yet be fully derived, lower-level interactions really are how
nature builds higher-level function, and refusing to attempt the connection does not make it any
less real.

## Part I — decision-making inside a single cell

### A gene turning another on or off

The simplest possible circuit is one gene's product, $X$, regulating a second gene, $Y$: $X$ can
either activate $Y$ (turn its expression up) or repress it (turn it down). The lecture fixes a
notational convention that recurs all semester: a plain arrowhead is used loosely and can be
ambiguous, but a dedicated bar-headed symbol is reserved specifically for repression. A concrete
example given is a repressor (called "10R" in the lecture) that represses expression of a gene
encoding GFP, green fluorescent protein.

GFP matters here for a reason beyond convenience: fusing it to a gene turns the abstract idea of
"how much of this protein is being made" into something you can actually watch, in a single living
cell, over time. The lecture makes the point that new ideas in this field often followed new
technique rather than the other way around — it was the spread of GFP and its relatives that made
concepts like intrinsic cell-to-cell noise concrete enough to have real data behind them, rather
than being purely theoretical possibilities.

### Why a cell can't respond instantly: dilution sets a floor

Take a cell that starts out repressing that fluorescent gene, so its protein concentration sits at
zero, and then remove the repressor. How long does it take the protein concentration to climb to
its new steady state? The answer the lecture gives is that the relevant timescale is generally the
cell's own generation (division) time. The reasoning has two parts. First, if a cell stops making a
protein, its concentration decays simply because the cell keeps growing and dividing, diluting
whatever is already there — and that dilution happens on the timescale of a generation. Second, and
less obviously, the *same* timescale bounds how fast a cell can turn something *on* via new gene
expression, not only how fast something already present decays away. A bacterium in rich media at a
good temperature — E. coli, for instance — can divide roughly every 20 minutes, and that number is
itself a small marvel given everything a dividing cell has to build and coordinate; but it also
means that if a cell's only way of responding to a new signal is expressing a new gene, the response
necessarily takes on the order of tens of minutes, whatever the urgency.

### Breaking the floor: negative autoregulation

A gene product that represses its own expression is called negative autoregulation, and the
lecture notes that this circuit turns up surprisingly often in real regulatory networks — which is
itself a hint (not a proof) that it might be doing something evolution favors. Two specific effects
are named: negative autoregulation speeds up a gene's response to a new signal, beating the
generation-time floor above; and it increases robustness — the extent to which the resulting protein
level holds steady against environmental perturbations (temperature, say) or against ordinary
stochastic fluctuation.

### Building circuits to find out if the models are right

The logic behind the next two experiments is Feynman's: if you cannot build it, you do not
understand it. If the simple regulatory pictures above are actually right, it should be possible to
physically assemble genetic parts predicted to behave a certain way and watch that behavior appear.
Two founding papers, both appearing back to back in the same issue of *Nature* in 2000, did exactly
this, using biological parts that had never previously interacted with one another — an early,
striking demonstration of the modularity of biological components, and, in the lecture's telling,
close to the joint starting point of both systems biology and synthetic biology as fields.

- The **toggle switch** (Gardner, Cantor and Jim Collins's group): two genes that mutually repress
  each other, built onto a plasmid and inserted into *E. coli*. Whichever gene happens to be "on"
  keeps the other one repressed, and that arrangement is self-sustaining — so the circuit has two
  distinct stable states, and functions as the simplest possible memory module: it can hold on to
  which state it was pushed into, long after the pushing has stopped.
- The **repressilator** (Michael Elowitz and Stanislas Leibler): three genes, again mutually
  repressing, but wired in a cycle rather than a mutual pair. A three-gene repression cycle has no
  stable fixed point analogous to the switch's two — each gene's level is chasing the one ahead of
  it around the loop — so instead of settling down, the circuit oscillates.

<figure>
<svg viewBox="0 0 640 210" role="img" aria-label="A single repression edge, closed into a two-gene loop, and closed into a three-gene loop">
  <defs>
    <marker id="bar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <line x1="8" y1="0" x2="8" y2="10" stroke="currentColor" stroke-width="2"/>
    </marker>
  </defs>

  <circle cx="60" cy="105" r="18" fill="none" stroke="currentColor"/>
  <text x="60" y="109" text-anchor="middle" font-size="12" fill="currentColor">X</text>
  <circle cx="170" cy="105" r="18" fill="none" stroke="currentColor"/>
  <text x="170" y="109" text-anchor="middle" font-size="12" fill="currentColor">Y</text>
  <line x1="78" y1="105" x2="152" y2="105" stroke="currentColor" stroke-width="1.5" marker-end="url(#bar)"/>
  <text x="115" y="150" text-anchor="middle" font-size="11" fill="currentColor">one repression</text>

  <circle cx="290" cy="65" r="18" fill="none" stroke="currentColor"/>
  <text x="290" y="69" text-anchor="middle" font-size="12" fill="currentColor">X</text>
  <circle cx="290" cy="145" r="18" fill="none" stroke="currentColor"/>
  <text x="290" y="149" text-anchor="middle" font-size="12" fill="currentColor">Y</text>
  <path d="M 276,80 C 245,105 245,105 276,130" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#bar)"/>
  <path d="M 304,130 C 335,105 335,105 304,80" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#bar)"/>
  <text x="290" y="190" text-anchor="middle" font-size="11" fill="currentColor">toggle switch: two mutual stable states</text>

  <circle cx="480" cy="55" r="18" fill="none" stroke="currentColor"/>
  <text x="480" y="59" text-anchor="middle" font-size="12" fill="currentColor">X</text>
  <circle cx="425" cy="150" r="18" fill="none" stroke="currentColor"/>
  <text x="425" y="154" text-anchor="middle" font-size="12" fill="currentColor">Y</text>
  <circle cx="535" cy="150" r="18" fill="none" stroke="currentColor"/>
  <text x="535" y="154" text-anchor="middle" font-size="12" fill="currentColor">Z</text>
  <line x1="471" y1="71" x2="434" y2="134" stroke="currentColor" stroke-width="1.5" marker-end="url(#bar)"/>
  <line x1="443" y1="150" x2="517" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#bar)"/>
  <line x1="526" y1="134" x2="489" y2="71" stroke="currentColor" stroke-width="1.5" marker-end="url(#bar)"/>
  <text x="480" y="195" text-anchor="middle" font-size="11" fill="currentColor">repressilator: no stable state, sustained oscillation</text>
</svg>
<figcaption>The same repression symbol, closed into a loop of two genes and into a loop of three.
Two mutual repressors settle into whichever stable state they are pushed toward — the toggle
switch. Three mutual repressors have no stable state to settle into, and instead take turns rising
and falling — the repressilator.</figcaption>
</figure>

The repressilator did oscillate, which was itself not obvious in advance — wiring three repressors
together was not guaranteed to do anything coherent at all. But watched under a microscope, a colony
grown up from a single starting cell loses synchrony quickly: neighboring cells end up bright and
dim at the same time rather than staying in phase with each other, so the oscillator is much less
clean than the two-gene switch. (Later work, credited in the lecture to Jeff Hasty's group, showed
that engineering principles could be used to design more robust, tunable versions.)

### Is the network's wiring itself patterned?

Zooming out from single circuits to the whole regulatory network of a cell, the lecture poses two
different questions about its structure. One, associated with Barabási, asks a purely statistical
question: how many other genes does a typical gene interact with, and what is the shape of that
distribution across the whole network? (This is previewed as leading to power-law-type
distributions, from a simple underlying mechanism.) The other, due to Uri Alon, asks whether small
wiring patterns recur far more often than a random-wiring model would predict. Autoregulation — a
gene regulating itself — is one such recurring pattern, or **motif**. Another is the
**feed-forward loop**: gene $X$ regulates a second gene $Y$, and both $X$ and $Y$ regulate a third
gene $Z$ directly. A pattern that appears more than chance predicts is a hint that it survived
because it does something useful — in the feed-forward loop's case, the lecture points at (without
deriving) an asymmetric response to a brief, transient input compared to a sustained one.

### Noise: doing the exact same thing twice and getting different answers

The repressilator's imperfect synchrony turns out to be the entry point for a second major
discovery, made about two years later by the same lab. Take a single cell and give it two identical
sets of instructions: a promoter driving a red fluorescent reporter, and an exact copy of the same
promoter driving a green one. If a cell executed its instructions deterministically, red and green
levels should track each other. What Elowitz found instead was substantial cell-to-cell
heterogeneity between the two colors — some cells came out redder, some greener — even though the
DNA sequence driving each color was identical. Because the instructions really are identical, this
rules out "different instructions" as an explanation, and stands as a genuine limit on what a cell
can guarantee to do reliably, not an artifact of imprecise measurement.

The explanation the lecture points toward, developed further in a later paper: DNA is typically
present at only one or a few copies per cell, so whether that stretch of DNA has an RNA polymerase
bound to it at a given moment is intrinsically an on/off, stochastic event — and this low-copy-number
randomness at the level of a single DNA molecule can propagate into substantial variability in
protein level. Sunney Xie's group (2006) made this direct by combining single-molecule fluorescence
with live-cell imaging in *E. coli*, so that each individual transcription event showed up as its
own small burst of fluorescence, watched happening in real time inside a living cell.

### Physical limits on what a cell can sense and do

Diffusion and viscosity, not only chemistry, bound what a cell can do in its environment. The
lecture introduces the **Reynolds number** as a measure of the relative importance of viscous
versus inertial forces for a swimming organism, and makes the qualitative point that how something
our size swims is not simply a scaled version of how a bacterium swims — the physics that dominates
is different at very small scales. This sets up the specific problem of **chemotaxis**: how does a
cell as small as *E. coli* tell "toward more food" from "away from it" at all, given that it cannot
simply sense a gradient across its own body the way a larger organism might. The lecture points at a
specific, robust mechanism bacteria use to solve this, without deriving it here.

### Pattern formation without a blueprint

A related demonstration of self-organization: take the proteins responsible for locating the center
of an *E. coli* cell — needed so the cell can divide roughly in half rather than off-center — and
reconstitute them outside the cell entirely, on a flat, two-dimensional membrane. There is no
external observer inside a cell telling it where the middle is; the cell has to generate that
information itself. These **Min proteins** do so by binding to the membrane and being ejected from
it again in a way that produces traveling wave patterns, of the same general character as a Turing
pattern, and the resulting oscillation is what lets the cell locate its own center.

## Part II — evolution as a decision process running over generations

### Cost and benefit set an expression level

Evolving *E. coli* populations for hundreds of generations at different fixed concentrations of the
sugar lactose (an experiment from Uri Alon's group), the amount of the lactose-digesting enzyme the
population ends up expressing tracks the lactose concentration it evolved in: more lactose in the
environment, more enzyme; less lactose, less enzyme. The reasoning is a cost-benefit trade-off, a
Goldilocks problem: making the enzyme costs the cell resources it could otherwise spend elsewhere,
so making as much as possible is not automatically better, and the amount actually observed
reflects a balance between that cost and the benefit of the sugar the enzyme unlocks — a balance
that can be watched shifting, in real time, by changing the environment.

### Why noise still matters when the population is a billion strong

A population even in a modest test tube can hold on the order of $10^9$ cells — which sounds like
far too large a number for randomness at the level of individuals to matter to evolution at the
population scale. The resolution the lecture gives: whatever its eventual fate, every new mutation
starts out as exactly one individual, no matter how large the surrounding population is. So every
evolutionary process, regardless of overall population size, passes through a regime where the fate
of a single lineage is a small-number, genuinely stochastic question — and that is precisely the
regime in which fluctuations dominate. A simple statement, but with real consequences for how
evolution has to be modeled.

### The distribution of mutations that actually spread doesn't reveal the distribution they came from

Introduce a population into a new environment, and many different mutations suddenly become
available, with a range of effects on fitness — some strongly beneficial, some barely so — and the
shape of that underlying distribution of possible effects is not obvious in advance. What Roy
Kishony's group showed is that the mutations which actually go on to spread and take over the
population (fix) come out looking similarly shaped — peaked around some characteristic value —
across a broad range of assumptions about what the underlying distribution of possible mutations
looked like. The implication: observing which mutations actually fixed in a population tells you
surprisingly little about the underlying distribution they were drawn from, because the process of
fixation itself erases much of that information. This is offered as an instance of a difficulty that
recurs throughout the course — figuring out which microscopic details actually matter for a
higher-level pattern, and which simply wash out.

### Fitness landscapes constrain the order evolution can take

By analogy with a potential-energy landscape, where a ball rolls downhill: picture the height of a
landscape as a measure of fitness — say, a bird's ability to fly — and the two horizontal axes as
two phenotypic traits, say wing length and wing width. If the shape of that landscape requires
crossing a ridge — a wider wing has to evolve before a longer wing becomes advantageous, say — then
the shape of the landscape constrains not just which combination of traits is eventually reached,
but the *order* in which they can be acquired.

The same idea can be applied to genotypes rather than phenotypes. Daniel Weinreich's experiment
constructed every combination of five point mutations in a gene encoding an enzyme that breaks down
penicillin — all $2^5 = 32$ genotypes — and measured fitness directly for each of the 32 resulting
constructs. The landscape that came out was rugged in a way that restricts which of the many
possible orders of acquiring the five mutations are actually accessible to evolution: some paths
across the landscape pass only through increasingly fit intermediates, and most do not.

### When fitness depends on what everyone else is doing

Everything so far treats fitness as a property of a genotype (or phenotype) on its own. That
assumption breaks down when a strategy's fitness depends on which other strategies are present in
the population — at which point a fixed landscape is the wrong picture, and genuine **game theory**
is needed instead. Examples pointed at, to be developed later: a rock-paper-scissors dynamic
constructed among different strains of *E. coli*, and a naturally occurring rock-paper-scissors
interaction among the mating strategies of male lizards; and cooperative interactions among
microbes in which a "cheater" strategy can arise, spread through the population, and in some cases
drive the whole population toward collapse — a genuine tension between what benefits an individual
and what benefits the group.

### Can a population "learn"?

The neutrophil chasing a bacterium is one kind of information processing — an individual cell
responding to something immediately present in its environment. A different kind, pointed at here
but not developed, is learning at the level of a population, over evolutionary rather than
individual time. *E. coli* passing through a mammalian gut, and yeast fermenting wine, each
typically encounter their available carbon sources in a fairly consistent order. Populations
evolved in these settings were found to start preparing to digest the *next* typical carbon source
as soon as they detect the current one — an anticipation of a typical environmental sequence that is
encoded not in any individual cell's own experience, but in the population's evolutionary history.

### The paradox of sex

Asexual reproduction gives simple exponential growth: one cell becomes two, two become four, at a
rate set only by the population's own division rate. Obligate sexual reproduction pays what the
lecture calls a **twofold cost of sex**: if offspring require both a male and a female, and males
do not themselves give birth, the exponential growth *rate* itself is cut by a factor of two relative
to the asexual case — not merely a fixed loss, but a loss compounding every generation. Given a cost
this large, why is sexual reproduction still the norm among "higher" organisms? The leading
hypothesis named is the **Red Queen hypothesis** (from the Lewis Carroll line: the Red Queen has to
run as fast as she can just to stay in the same place) — that sex persists because it lets a host
population evolve fast enough to keep pace with a co-evolving, continually adapting population of
parasites. Pointed at but not developed here: experiments in worms comparing reproductive
strategies in the presence and absence of parasites.

## Part III — ecological systems biology

### Predator and prey don't oscillate quite the way the textbook model says

Classical predator-prey models, over a century old, predict sustained oscillations with predator
and prey population sizes roughly 90 degrees out of phase. Long-running laboratory (chemostat)
experiments instead found oscillation periods longer than predicted, and prey and predator running
roughly 180 degrees out of phase — a genuine discrepancy from the standard model. The explanation
pursued: modeling suggested the discrepancy came from ongoing evolution *within* the prey
population itself, so that the prey was not a fixed type but was itself evolving on the same
timescale as the population dynamics. Experiments that suppressed that evolution — by reducing
heterogeneity within the prey population — made both anomalies, the longer period and the phase
shift, disappear. The lecture holds this up as a model instance of the back-and-forth it wants
throughout the course: a model motivates an experiment, the experiment's surprise motivates new
modeling, and the two together teach more than either alone.

### Expanding into new territory strongly amplifies genetic drift

When a population expands into previously unoccupied territory, the population size relevant to
**genetic drift** — the role of pure chance in which variants survive — is not the size of the whole
population, but only the much smaller population actually at the expanding front. Because it is
only the front that matters, drift is strongly enhanced relative to what the total population size
alone would suggest.

### Tipping points, and the same feedback logic as the toggle switch

The Newfoundland cod fishery was productive for centuries; improved fishing technology through the
1960s and 70s drove a sharp rise in catch, which was followed by a sudden, catastrophic collapse of
the population in the early 1990s (similar collapses are cited off Monterey and elsewhere). The
lecture frames this with the same feedback logic that gave the toggle switch its two stable states:
interactions within a population can create two alternative states — healthy, and locally extinct —
with feedback that holds the population near a healthy state under moderate stress, until the
stress exceeds what the feedback can counteract, at which point the state suddenly flips. This
raises a practical question: can the approach of such a tipping point be detected in advance? A
result attributed to the lecturer's own group: in laboratory populations, the *fluctuations* of a
population change in a characteristic way before a collapse — a possible general early-warning
signature, not tied to the specifics of any one system.

### A cautionary tale: matching a pattern is not confirming a mechanism

A concrete dataset poses the closing question: on Barro Colorado Island, a long-censused island in
Panama where thousands of individual trees have been counted and identified, some species are far
more common than others. The natural first answer is that the common ones are simply better adapted
to the environment — and the lecture allows that this is often right. But a complication is raised: a
purely **neutral model** of ecology — one in which every species is assumed dynamically identical,
and all abundance differences arise only from random birth-death dynamics, with no species better
adapted than any other — can reproduce many of the same species-abundance patterns actually observed
in nature. The methodological point drawn out explicitly: fitting a model whose output matches an
observed pattern is not, by itself, evidence that the model's assumptions are correct, because here
two models built on essentially opposite assumptions (species differ in fitness, versus species are
identical) can produce the same pattern. The lecture names this as an easy trap to fall into even
while trying to do careful science — collecting real quantitative data does not by itself protect
against it.

## Sources

All material in this chapter is from the transcript of the opening lecture of 8.591J *Systems
Biology* (MIT OCW, Fall 2014), `recordings/gc3o2skisx4.md`, lecturer Jeff Gore. No slides, written
notes or problem set were supplied for this lecture; administrative content (grading, deadlines,
prerequisites, the flipped-classroom format) has been omitted as boilerplate. Approximate
transcript timestamps by section:

- Two traditions of "systems biology," and the two assigned textbooks — [04:18]-[07:44], [17:24]-[18:31]
- The guiding question, the neutrophil film, and Bialek's opposing organization — [01:06]-[03:13], [22:03]-[23:07]
- Regulation symbols, GFP, response time and the generation-time floor, negative autoregulation — [23:07]-[28:38]
- The toggle switch and the repressilator — [28:38]-[34:19]
- Network degree distributions and motifs (Barabási, Alon) — [34:19]-[36:41]
- Noise in gene expression and single-molecule imaging (Elowitz, Xie) — [36:41]-[41:09]
- Physical constraints (Reynolds number, chemotaxis) — [41:09]-[42:20]
- Pattern formation (Min proteins) — [42:20]-[44:45]
- Cost-benefit evolution of enzyme expression (Alon) — [44:45]-[46:55]
- Stochasticity in evolution despite large population size — [46:55]-[48:03]
- Distribution of fixed beneficial mutations (Kishony) — [48:03]-[50:16]
- Fitness landscapes, phenotypic and genotypic (Weinreich) — [50:16]-[52:24]
- Game-theoretic fitness, rock-paper-scissors, cheating — [52:24]-[54:38]
- Evolutionary anticipation of environmental sequence — [54:38]-[56:43]
- The paradox of sex and the Red Queen hypothesis — [56:43]-[57:57]
- Predator-prey oscillation experiments — [57:57]-[1:00:08]
- Range expansion and genetic drift — [1:00:08]-[1:01:13]
- Tipping points and the cod fishery — [1:01:13]-[1:03:32]
- Early-warning signals before collapse — [1:03:32]-[1:04:35]
- Neutral theory of ecology, Barro Colorado Island — [1:04:35]-end

Named but not contained in this transcript, and not developed further here: the 1950s film of a
neutrophil chasing a bacterium (described but not shown in a transcript); Uri Alon's *An
Introduction to Systems Biology* and Martin Nowak's *Evolutionary Dynamics* (the course's two
assigned textbooks); Bill Bialek's *Biological Physics* (referred to for its introduction's
discussion of how to organize a systems-biology course); the Barabási paper on network degree
distributions; Alon's paper(s) on network motifs and the feed-forward loop; Gardner, Cantor and
Collins's 2000 toggle-switch paper and Elowitz and Leibler's 2000 repressilator paper (both in the
same issue of *Nature*); Elowitz's later paper on intrinsic noise in gene expression; Sunney Xie's
2006 single-molecule imaging paper; Jeff Hasty's work on engineered oscillators; Alon's lactose
cost-benefit evolution paper; Roy Kishony's paper on the distribution of fixed beneficial mutations;
Daniel Weinreich's beta-lactamase fitness-landscape paper; and unnamed papers, described but not
attributed by title, on rock-paper-scissors dynamics in microbes and lizards, on cooperation and
cheating in microbial populations, on evolutionary anticipation of carbon-source order in *E. coli*
and yeast, on tests of the Red Queen hypothesis in worms, on predator-prey phase and period
anomalies in chemostats, on genetic drift at expanding population fronts, and on the neutral theory
of ecology applied to Barro Colorado Island.

---

[← 12. Three Views of Stochastic Kinetics](12-three-views-of-stochastic-kinetics.md) · [Contents](index.md) · [14. Toggle Switches and Stability Analysis →](14-toggle-switches-and-stability-analysis.md)
