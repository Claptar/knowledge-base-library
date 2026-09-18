---
title: "3. Lotka-Volterra Dynamics and Population Waves"
course: "MIT 8.591J 2014"
chapter: 3
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 3. Lotka-Volterra Dynamics and Population Waves

## What this covers

This chapter finishes the two-species Lotka–Volterra competition story that the previous lecture
set up, then asks two questions that go beyond it: what happens with more than two competing
species, and what can *non-transitive* ("rock-paper-scissors") competition do for the maintenance
of diversity, in a well-mixed population and in a spatially structured one. It closes with a
different kind of question — not who wins a competition, but how fast a population's edge moves
outward when local growth is coupled to spatial spreading. It assumes the two-species
Lotka–Volterra competition equations and the practice of classifying fixed points by stability
and eigen-directions, both introduced in the previous lecture, together with the idea of a
nullcline.

## Two-species competition: the four outcomes

The model carried over from last time is

$$\dot N_1 = r_1 N_1\left(1-\frac{N_1+\beta_{12}N_2}{K_1}\right), \qquad
\dot N_2 = r_2 N_2\left(1-\frac{N_2+\beta_{21}N_1}{K_2}\right).$$

*Competition* means each species' presence lowers the other's growth, i.e. $\beta_{12},\beta_{21}>0$:
$\beta_{12}$ is how much a unit of species 2 reduces species 1's growth, and $\beta_{21}$ the
reverse. Depending on the relative sizes of $K_1$, $K_2$, $K_1/\beta_{12}$ and $K_2/\beta_{21}$,
there are exactly four possible long-run outcomes: species 1 always wins, species 2 always wins,
stable coexistence, or bistability (the only case in which the outcome depends on where you start,
provided you start with some of each species — obviously a species that starts at zero density
never appears).

The same four outcomes show up when analysing frequency-dependent selection between two strategies
within a single asexual population, in the sense used in Martin Nowak's *Evolutionary Dynamics*.
That is not a coincidence of notation: it is a real structural link between an ecological question
(different species competing) and an evolutionary one (allele or genotype frequencies changing
inside one species), even though the two settings model different biological processes.

Rule of thumb for which outcome you get: coexistence needs the competition to be *weak* — small
$\beta$'s — relative to the ratio of carrying capacities. If $K_1=K_2$, this reduces to simply
asking whether each $\beta$ is above or below 1, i.e. whether a member of the other species harms
you more or less than a member of your own species would.

## Reading a phase portrait from its nullclines

The nullcline $\dot N_1=0$ is the line $N_1+\beta_{12}N_2=K_1$: it meets the $N_1$-axis at $K_1$
and the $N_2$-axis at $K_1/\beta_{12}$. The nullcline $\dot N_2=0$ is $N_2+\beta_{21}N_1=K_2$,
meeting the axes at $K_2$ and $K_2/\beta_{21}$ respectively. The whole point of drawing them is a
simple rule: on the $\dot N_1=0$ line, $N_1$ is momentarily not changing, so the local flow can
only be vertical (only $N_2$ moves); on the $\dot N_2=0$ line the flow can only be horizontal.
Along the axes themselves the system reduces to ordinary single-species logistic growth, so the
flow there is easy: $N_1$ grows toward $K_1$ along the $N_1$-axis, $N_2$ toward $K_2$ along the
$N_2$-axis. Stitching these directions together across the plane — which is exactly what the class
did, pointing an arm to vote on "up or down" and then "left or right" at successive points — is
enough to read off the whole phase portrait without solving anything explicitly.

Take the case where the two nullclines do not cross inside the positive quadrant because
$K_1>K_2/\beta_{21}$ and $K_1/\beta_{12}>K_2$ (equivalently $\beta_{21}>K_2/K_1$ and
$\beta_{12}<K_1/K_2$: species 1 harms species 2 a lot, and species 2 does not harm species 1
enough to matter). There are exactly three fixed points: the origin, $(K_1,0)$, and $(0,K_2)$.

- The origin is an unstable node in **both** directions, with eigenvectors along the two axes.
  That is just the statement $r_1,r_2>0$: each species can grow from near-zero density on its own.
- $(K_1,0)$ is stable. One of its eigen-directions is along the $N_1$-axis (drop $N_2=0$ and it is
  pure logistic growth of species 1); the other is tilted into the interior, and it is the
  direction along which trajectories starting with a real mixture of both species curve in.
- $(0,K_2)$ is unstable transverse to the axis: species 2 alone sits at its own carrying capacity,
  but any amount of species 1 present grows and eventually displaces it.

<figure>
<svg viewBox="0 0 400 300" role="img" aria-label="Phase portrait of the two-species Lotka-Volterra competition model in the case where species 1 always wins">
<defs>
<marker id="arrowA" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
</marker>
</defs>
<line x1="50" y1="260" x2="370" y2="260" stroke="currentColor" stroke-width="1.5"/>
<line x1="50" y1="260" x2="50" y2="20" stroke="currentColor" stroke-width="1.5"/>
<text x="358" y="278" font-size="12" fill="currentColor">N1</text>
<text x="30" y="25" font-size="12" fill="currentColor">N2</text>
<line x1="290" y1="260" x2="50" y2="50" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5,4"/>
<line x1="180" y1="260" x2="50" y2="90" stroke="currentColor" stroke-width="1.3"/>
<text x="278" y="278" font-size="11" fill="currentColor">K₁</text>
<text x="150" y="278" font-size="11" fill="currentColor">K₂/β₂₁</text>
<text x="6" y="94" font-size="11" fill="currentColor">K₂</text>
<text x="-2" y="54" font-size="11" fill="currentColor">K₁/β₁₂</text>
<circle cx="50" cy="260" r="4" fill="none" stroke="currentColor" stroke-width="1.3"/>
<circle cx="290" cy="260" r="4" fill="currentColor"/>
<circle cx="50" cy="90" r="4" fill="none" stroke="currentColor" stroke-width="1.3"/>
<line x1="120" y1="260" x2="205" y2="260" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrowA)"/>
<line x1="50" y1="220" x2="50" y2="150" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrowA)"/>
<path d="M110,150 C180,190 240,230 283,257" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrowA)"/>
<path d="M60,130 C120,200 200,240 283,257" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrowA)"/>
</svg>
<figcaption>Nullclines dashed (N1 dot = 0) and solid (N2 dot = 0) for K1 &#62; K2/β21 and
K1/β12 &#62; K2. Every trajectory with some of species 1 present ends at (K1, 0), filled;
the origin and (0, K2), open circles, are both unstable. Reconstructed from the spoken
description of the board, not the board itself.</figcaption>
</figure>

A useful check the class ran on this case: does the outcome change if the growth rates $r_1,r_2$
change? No — a class vote confirmed it. Which species wins depends only on the $\beta$'s and $K$'s;
the $r$'s only change the *shape and speed* of the approach, not the destination. The example given
for why this matters is Strogatz's sheep-and-rabbits illustration of two competing species: rabbits
divide faster than sheep, so starting from a mix of both, the trajectory can rise up toward what
looks like a rabbit victory, before curving back and ending with the sheep displacing the rabbits.
This is *competitive exclusion*: two species competing for close to the same resource generically
end with only one of them surviving, however dramatic the transient looks along the way.

### A digression: does stochasticity change this?

A student asked whether stochastic extinction could break the deterministic picture — in
particular, whether a species being driven toward very low numbers near the unstable fixed point
could go extinct by chance before the deterministic dynamics ever "resolve" the competition. Several
points came out of the discussion:

- The Lotka–Volterra description here is continuous and deterministic: it allows fractional
  individuals and has no built-in randomness at all.
- In the case being analysed, the trajectories keep moving toward larger $N_1$ once the process has
  really got going, so stochastic loss of the losing species is most likely to matter right at the
  start, at low density — not partway through, near the unstable fixed point.
- Whether a *stochastic simulation* of this same equation can even produce extinction depends
  entirely on how you split the net growth term $rN(1-N/K)$ into an explicit birth rate and death
  rate before feeding it to something like a Gillespie algorithm. If you implement the whole
  expression as a birth rate and add no separate death process, extinction is impossible by
  construction — there is nothing that can reduce the population. A more faithful implementation
  writes the net rate as $B-D$ for some birth rate $B$ and death rate $D$; at the level of the
  ordinary differential equation the two choices are identical, but they are not identical once you
  build a Fokker–Planck approximation or an actual stochastic simulation, because the rate of
  stochastic extinction grows with the sizes of $B$ and $D$ individually — bigger birth and death
  rates mean bigger fluctuations even at a fixed net growth rate.

## Many competing species

Non-dimensionalising by carrying capacities — $x_i=N_i/K_i$ — converts the two-species equations
into a general $N$-species form

$$\dot x_i = r_i x_i\left(1-\sum_j \alpha_{ij}x_j\right), \qquad \alpha_{ii}=1 \text{ for all } i,$$

where the normalisation is chosen precisely so that each species alone follows simple logistic
growth with carrying capacity 1. Everything about the ecology is now carried by the off-diagonal
entries of the matrix $\alpha_{ij}$. Being fluent in moving between a model in its raw parameters
and this non-dimensionalised version is a skill in its own right — the kind of thing that showed
up repeatedly on the second exam, in questions about how a parameter changes when the strength of
some expression process changes.

Restrict to the purely competitive case, $\alpha_{ij}\ge0$ for all $i,j$ (some entries may be zero
— species need not all interact — but none can help another). Three facts about this system were
stated as known results to look up rather than derived in the lecture:

1. **The unit cube is invariant.** If every $x_i(0)\in[0,1]$, then $x_i(t)\in[0,1]$ for all later
   $t$. Staying non-negative is obvious; staying below 1 (i.e. below your own carrying capacity) is
   not, since nothing in the setup literally forbids starting or ending up above it — it is a
   genuine fact about this class of equations, not a triviality.
2. **The long-run dynamics live on an $(N-1)$-dimensional surface.** Specifying every possible
   trajectory still needs all $N$ coordinates, since the starting point can be anywhere in
   $N$-dimensional space — but the steady-state behaviour for given parameters (fixed points, limit
   cycles, chaotic attractors) is confined to one dimension fewer than the number of species. A
   student pushed back on this in the $N=2$ case, since with no oscillation at all the steady
   states there are just points, which trivially sit on a lower-dimensional set regardless; the
   claim is meant to bite once oscillatory or chaotic long-run behaviour is possible, and that is
   where the next two facts come in. (Whether there is some general conserved-quantity argument
   behind the claim was raised and left open.)
3. Consequently, a limit cycle needs two dimensions to close up without crossing itself, so
   getting one in this framework needs $N\ge3$ competing species; chaos needs three dimensions to
   fold without crossing, so it needs $N\ge4$. Both bounds are known to be tight: limit cycles occur
   already at $N=3$ and chaos already at $N=4$. A further result says that for $N\ge5$ essentially
   any dynamical behaviour is possible — including, apparently, a four-dimensional torus attractor,
   left as something to look into independently.

$N\ge4$ making chaos *possible* does not mean every four-species competitive system is chaotic —
only that some are. What makes this worth dwelling on is that pairwise Lotka–Volterra competition
is about the simplest model one could write down for species interacting, and it is already rich
enough to produce genuinely complicated dynamics.

The dimension-counting argument rests on one fact about continuous, deterministic systems:
trajectories cannot cross themselves (solutions are unique). A limit cycle is a closed loop that
never repeats a point except by returning to its start, and a line cannot do that without crossing
itself, so it needs a second dimension to curl into. Chaos additionally needs trajectories to
stretch and fold without ever touching, which a flat plane cannot support either — hence a third
dimension. This connects to, but should not be over-read from, the Poincaré–Bendixson theorem: an
unstable fixed point surrounded by a trapping region containing no other fixed point *does*
guarantee a limit cycle inside that region. The converse is not a theorem — a *stable* fixed point
does not, in general, rule out a limit cycle elsewhere. In the specific two-species predator–prey
model discussed earlier in the course, it happens that oscillations disappear exactly when the
interior fixed point becomes stable, but that is proved for that model by a separate
divergence-type argument, not read off from Poincaré–Bendixson. A related but distinct question —
raised by a student — is what separates chaos from a trajectory that merely spirals in toward a
limit cycle without ever crossing itself: that distinction is usually made with a Lyapunov exponent,
which measures whether a small blob of nearby initial conditions in phase space contracts (as it
does approaching a stable limit cycle) or stretches and folds while staying bounded (chaos); this
was flagged as belonging properly to a course in nonlinear dynamics rather than developed here.

## Non-transitive interactions: rock-paper-scissors

Three strategies or species $A,B,C$ interact *non-transitively* if $A$ beats $B$, $B$ beats $C$,
and $C$ beats $A$ in pairwise competition — "beats" meaning that whichever pair is put together,
one drives the other extinct. This is exactly rock-paper-scissors, and it can be encoded in the
Lotka–Volterra framework by an appropriate choice of the interaction coefficients.

Non-transitive competition has been proposed as a mechanism that can stabilise the coexistence of
several species or strategies through the kind of cyclic — even chaotic — dynamics discussed above.
How much of the diversity actually observed in nature this explains is an open question; what is
not in doubt is that it is a real, demonstrated phenomenon, and that spatial structure seems to
matter a great deal to whether it actually maintains diversity. Two studies were assigned as
readings and discussed at length.

### Side-blotched lizards: three male mating strategies

Sinervo and Lively's 1996 study of side-blotched lizards in the mountains of Merced County,
California, identified three genetically determined, heritable male morphs, distinguished by
throat colour:

- **orange-throat** — highly aggressive, defends a very large territory with many females, and
  fights off rival males;
- **blue-throat** — less aggressive, with a smaller, more defensible territory;
- **yellow-striped "sneaker"** — mimics the female's colouring and appearance, holds no territory
  at all, and instead sneaks into other males' territories to mate.

Pairwise, orange beats blue (a bigger territory simply passes on more genes). Sneakers beat orange:
an orange male's territory is too large to defend effectively against sneaking. Blue beats sneakers:
a smaller, well-defended blue territory keeps sneakers out. That closes the cycle orange → blue →
sneaker → orange. Tracking morph frequencies (and the number of females held per territory) over
roughly seven years, from about 1990 to 1996, showed the frequencies cycling around in
strategy-frequency space — a rock-paper-scissors dynamic actually observed unfolding in a wild,
spatially structured population.

### Bacterial colicin warfare

Kerr and colleagues (Nature, 2002) studied three strains of *E. coli* differing only by a mutation
or plasmid — a single species playing rock-paper-scissors through genotype rather than through
separate species:

- **C, colicinogenic** — carries a plasmid encoding colicin, a toxin that punches holes in the
  membranes of other bacteria. Colicin is released only when the producing cell itself lyses
  (bursts open), so producing it is unambiguously costly to the individual and can only be favoured
  by a kin- or group-selection argument: helping clone-mates, who share the plasmid and its
  immunity gene, outcompete rivals, at the cost of the producer's own life.
- **R, resistant** — resistant to colicin, at some smaller fitness cost.
- **S, sensitive** — ordinary bacteria, no cost, but no defence either.

Pairwise: R beats C (resistance is cheaper than suicide), S beats R (resistance carries a cost
that plain sensitivity avoids), and C beats S (colicin kills sensitive cells) — closing the cycle
C → S → R → C. It is worth noting how carefully the original paper phrases this: it says the
fitnesses are *such that* this ordering holds, rather than claiming it always will for any isolate
you might pick up — a real reminder to read a paper's hedges rather than over-generalise its claim.

Two environments were compared:

- **Well-mixed (test tube).** The three strains did **not** coexist. The sensitive strain died out
  first — killed fastest once colicin accumulated — leaving a straight two-strain contest between C
  and R, which R wins, so only the resistant strain survives long-term. (A caution attached to this:
  there is no reason these particular strain dynamics should be well described by a smooth
  Lotka–Volterra model at all — if colicin accumulates enough, sensitive cells can be wiped out en
  masse in a way a continuous model does not naturally capture.)
- **Spatially structured (agar plate).** Strains were arranged in a grid of patches and propagated
  for about a week by replica-plating with velvet stamps onto fresh plates each day. All three
  strains coexisted throughout, in a spatial pattern consistent with each strain chasing the one it
  beats around the plate — sensitive into resistant territory, resistant into colicinogenic
  territory, colicinogenic into sensitive territory — though the boundary between S and R
  specifically could not be seen directly, since the two grow to similar colony density; only the
  colicinogenic strain was visually distinct. Distinguishing S from R in practice meant scraping
  cells off and re-plating them to test directly for colicin sensitivity, rather than reading a
  visible boundary.

The conclusion drawn in lecture: for these three particular strains, non-transitive competition
alone is not enough to maintain three-way coexistence in a well-mixed environment, but local
dispersal is. That does **not** show non-transitive competition can never support coexistence
without spatial structure — reasonable rock-paper-scissors-type equations exist (of the kind
discussed in Nowak's book) that spiral inward to a stable coexistence fixed point in a perfectly
well-mixed setting. It only shows it does not happen for this system, under these conditions.

A practical aside: despite roughly 500 citations, this system has attracted very few follow-up
experimental papers, in part because it has never become a "domesticated" laboratory model — no
fluorescent markers, no clean cloning plasmid. The resistant strain, for instance, is obtained
simply by exposing sensitive cells to colicin-laden supernatant and seeing which cells grow, and
the underlying mutation (often in a surface receptor colicin uses to enter the cell) can differ
between isolates. The lecturer's own group has worked with these strains and found them, in his
words, "a little bit messy" — a case where the field could use cleaner, fluorescently labelled
strains of the same three-way system. A pointer was also given to computational work by Erwin Frey
varying the mobility of individual agents in a spatial rock-paper-scissors model: there is a
critical mobility below which spatial structure supports coexistence, and above which the system
behaves like the well-mixed case and loses diversity.

## Population waves

Spatial structure matters broadly in ecology and evolution, and a common, tractable way to model
the movement of organisms over length and time scales much larger than any individual step is to
treat it as an effective diffusion process. This is justified whenever the distribution of
individual step sizes is not long-tailed, so that the central limit theorem applies to the
accumulated displacement; step-size distributions that *are* long-tailed — as has been argued for
the spread of disease via modern air travel, where most people stay local but a small, non-decaying
fraction fly across the world — behave qualitatively differently and diffusion is the wrong picture
for them (Oskar Hallatschek's work on epidemic spread with long-tailed dispersal was given as a
pointer for that regime).

The model — due originally to Fisher in the 1920s, who introduced it to describe the spatial spread
of a beneficial allele rather than a population, another instance of the same mathematics
describing an evolutionary and an ecological process — adds a diffusive term to logistic growth:

$$\frac{\partial n}{\partial t} = rn\left(1-\frac{n}{K}\right) + D\,\frac{\partial^2 n}{\partial x^2},$$

where $n(x,t)$ is now a population *density*, $r$ the per-capita growth rate at low density, $K$
the local carrying capacity, and $D$ the diffusion coefficient. Starting from a single individual
at a point, the population divides up locally to saturation at $K$, and a front then spreads
outward whose *shape* stays fixed over time in a co-moving frame: $n(x,t)=f(x-vt)$ for a fixed
profile $f$ and velocity $v$. That stationarity of shape is what earns it the name "wave."

### The wave speed, by dimensional analysis

$r$ has units of one over time, $D$ has units of length squared over time, and $v$ must have units
of length over time. The only combination that works is $v\propto\sqrt{rD}$, and Fisher's exact
result fixes the constant:

$$v = 2\sqrt{rD}.$$

(A question raised in class about whether the derivatives themselves carry hidden units: they do
not — $\partial/\partial t$ and $\partial^2/\partial x^2$ are pure operators, and all the length and
time dimensions in the equation are already accounted for by $D$.) Both ingredients behave as
expected: faster individual growth and greater mobility each speed up the wave, and the velocity is
a genuinely *population-level* property — it is not simply "growth" or simply "motion," but a
result of the two coupled together. To leading order, in this deterministic treatment, the velocity
does **not** depend on the carrying capacity $K$ at all.

One subtlety raised in class: if growth is switched off entirely ($r\to0$) at some instant, the
population does not stop spreading — pure diffusion still spreads it. This does not contradict
$v=2\sqrt{rD}\to0$, because that formula describes the velocity of a genuine travelling wave with a
fixed, self-similar shape; switch off growth and the profile itself starts changing shape, so a
formula that assumes a fixed shape no longer applies.

### Pulled waves and pushed waves

Compare several different growth curves — the per-capita growth rate as a function of density —
that agree everywhere except very close to $n=0$ and very close to $n=K$. The wave speed depends
only on $r\equiv g(0)$, the growth rate exactly at zero density, regardless of how the curve behaves
at higher density. The reason is that the very leading edge of the wave is always at vanishingly
low density, growing essentially exponentially at rate $r$ with a characteristic decay length

$$\ell = \sqrt{D/r},$$

and it is this leading edge that "pulls" the rest of the front along at $v=2\sqrt{rD}$. Waves of
this kind are called **pulled waves** (Fisher waves): the entire wave's velocity and front-decay
length are set by the dynamics at the front, not by the bulk behind it.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Density profile of a travelling population wave, saturated behind the front and decaying ahead of it">
<defs>
<marker id="arrowB" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
</marker>
</defs>
<line x1="30" y1="160" x2="320" y2="160" stroke="currentColor" stroke-width="1.5"/>
<line x1="30" y1="160" x2="30" y2="20" stroke="currentColor" stroke-width="1.5"/>
<text x="305" y="178" font-size="12" fill="currentColor">x</text>
<text x="12" y="25" font-size="12" fill="currentColor">n</text>
<path d="M30,55 L120,55 C150,55 165,65 180,95 C195,125 205,145 230,153 C260,159 290,160 320,160" fill="none" stroke="currentColor" stroke-width="1.6"/>
<line x1="18" y1="55" x2="30" y2="55" stroke="currentColor" stroke-width="1.2"/>
<text x="2" y="59" font-size="11" fill="currentColor">K</text>
<line x1="195" y1="172" x2="245" y2="172" stroke="currentColor" stroke-width="1.2"/>
<line x1="195" y1="167" x2="195" y2="177" stroke="currentColor" stroke-width="1.2"/>
<line x1="245" y1="167" x2="245" y2="177" stroke="currentColor" stroke-width="1.2"/>
<text x="196" y="190" font-size="11" fill="currentColor">ℓ = √(D/r)</text>
<line x1="120" y1="35" x2="172" y2="35" stroke="currentColor" stroke-width="1.4" marker-end="url(#arrowB)"/>
<text x="112" y="27" font-size="11" fill="currentColor">v = 2√(rD)</text>
</svg>
<figcaption>A pulled (Fisher) wave: density saturates at K behind the front and decays over a
length ℓ = √(D/r) ahead of it. The low-density behaviour right at the front sets both ℓ and the
speed v of the entire wave.</figcaption>
</figure>

Now suppose growth has a strong Allee effect: the per-capita growth rate is *negative* — net death
— at low density, becoming positive only once density passes some threshold. A naive argument would
say such a population cannot expand at all, since the growth rate right at $n=0$ is negative and
the leading edge should die back rather than grow. Expansion is nonetheless possible: the front
itself is dying, but diffusion out of the healthy, growing bulk behind it pushes the population
forward. This is a **pushed wave** — qualitatively different from a pulled wave because it is
driven by the dense bulk rather than the sparse front.

The distinction has a genetic consequence, mentioned but not derived here (and pointed to further
in an assigned *Physics Today* reading on loss of heterozygosity during range expansions): pulled
waves have a smaller effective population size during expansion than pushed waves, because in a
pulled wave the population that matters for the front is the sparse one right at the edge, while in
a pushed wave it is the dense bulk.

## Sources

All content is from the transcript of one lecture in MIT 8.591J *Systems Biology* (Fall 2014),
`recordings/3eizij6qncy.md` (course `computational-biology/mit-ocw/8591j-2014`); administrative
boilerplate at the start was cut. This is a transcript-only recording — whatever was written on the
board (nullcline diagrams, the wave-profile sketch, the dimensional-analysis "cards") is not in the
source and is not shown here; the two figures above are reconstructions built from the verbal
description of what was drawn, not the board itself.

- Two-species competition recap, nullclines, worked "species 1 wins" case, and the stochastic
  extinction digression: 00:00–24:44. This continues a two-species Lotka–Volterra model set up in
  the *previous* lecture, which is referred to here but was not supplied as input.
- General $N$-species competition, the invariant cube, the two dimension theorems, and the
  Poincaré–Bendixson digression: 24:44–37:08.
- Rock-paper-scissors framing and the two case studies: 37:08–1:01:28.
- Population waves, dimensional analysis, and pulled vs. pushed waves: 1:01:28–end (1:20:37).

Referred to in the lecture but not supplied as input, and not reproduced here beyond what was said
aloud about them:

- Strogatz's textbook chapter on competing species (the sheep-and-rabbits example), ~17:48.
- Martin Nowak, *Evolutionary Dynamics* — the frequency-dependent-selection comparison, ~02:22 and
  ~54:42.
- Sinervo, B. and Lively, C. M. (1996), "The Rock-Paper-Scissors Game and the Evolution of
  Alternative Male Strategies," *Nature* — assigned reading, discussed ~41:42–47:35.
- Kerr, B. et al. (2002), "Local Dispersal Promotes Biodiversity in a Real-Life Game of
  Rock-Paper-Scissors," *Nature* — assigned reading, discussed ~47:35–1:01:28.
- Erwin Frey's computational study of rock-paper-scissors dynamics versus agent mobility, ~57:09.
- Oskar Hallatschek's work on epidemic spread with long-tailed dispersal kernels, ~1:03:39.
- An assigned *Physics Today* article on loss of heterozygosity in pulled versus pushed range
  expansions, ~1:19:32.

---

[← 2. Stochastic Gene Expression Bursts](02-stochastic-gene-expression-bursts.md) · [Contents](index.md) · [4. When Does Clonal Interference Matter →](04-when-does-clonal-interference-matter.md)
