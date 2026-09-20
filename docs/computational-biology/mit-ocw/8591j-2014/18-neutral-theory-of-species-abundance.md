---
title: "18. Neutral Theory of Species Abundance"
course: "MIT 8.591J 2014"
chapter: 18
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 18. Neutral Theory of Species Abundance

## What this covers

This is the last lecture of the semester, and it is deliberately a change of scale: everywhere
else the course worked from enzyme kinetics and molecular binding up to stochastic gene
expression, all at the scale of one cell. Here the same master-equation machinery is pointed at a
50-hectare plot of rainforest, to ask why some tree species are common and some are rare. The
chapter assumes the birth-death master equation and the trick of solving a one-step chain at
steady state by balancing probability fluxes — both used earlier in the course for stochastic
mRNA counts — and asks what happens when the birth rate, instead of being constant, is
proportional to how many individuals are already there.

The question it answers is: what do two very different families of model — one that assumes
species are ecologically different, one that assumes they are identical — actually predict about
the pattern of relative species abundance (RSA), and how much can fitting that pattern to data
tell you about which family is right?

## The data: a fifty-hectare census

The paper under discussion analyses a single data set: Barro Colorado Island (BCI), a 50-hectare
plot in the Panama Canal — an island only because the canal was built around it about a hundred
years ago, and close enough to the mainland that cougars swim across. A hectare is $10^4\,\text{m}^2$,
so 50 hectares is a $100\,\text{m}\times 100\,\text{m}$ square repeated fifty times, roughly half a
square kilometre.

On this plot, biologists identified every tree with diameter greater than 10 cm at breast height
(DBH) — the threshold you need so the counting is well defined — and assigned each one a species.
That gave 21,457 trees sorted into 225 distinct species. The point of restricting to one trophic
level (here, canopy trees, elsewhere beetles, or birds) is that the species in it are plausibly
competing with each other for the same kind of resource, which is exactly the situation the models
below are trying to describe.

## Reading the abundance histogram

The paper has one figure, and it is worth being careful about what it actually shows, because most
people misread it. The figure plots the number of species that have a given number of individuals,
binned on a $\log_2$ scale of individuals. Read naively, the tallest bar sits around 30
individuals, and it is tempting to call that the mode — the "typical" abundance of a species.

That is wrong, and the reason is the binning. On a log scale the bins grow geometrically: the
first bar covers essentially one integer value, but a bar far to the right covers a whole range —
everything from roughly 20-something individuals up to 50. So the height of a bar out there is
already a sum over many true abundance values, and a tall bar there does not mean any single
abundance value is common. To find the real mode you have to undo the binning.

The paper actually tells you how: the first bar is not the number of species with one individual,
$\phi_1$, but $\phi_1/2$. Reading that bar as 9 gives $\phi_1 = 18$. The next plotted bar is
$(\phi_1+\phi_2)/2$, and unwinding the arithmetic bar by bar recovers the true, linearly-binned
counts: 18 species with exactly one individual, 19 with two, 13 with three, 9 with four, 6 with
five, and falling off from there — 5, then 4, then 3, and so on, becoming too sparse to pin down
exactly. Nothing in that sequence looks anything like a bump at 30. The **mode of the distribution
is 1**.

<figure>
<svg viewBox="0 0 380 230" role="img" aria-label="Reconstructed raw counts of species by number of individuals, showing a sharp fall from many rare species to a single very abundant one">
  <line x1="30" y1="180" x2="360" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="180" x2="30" y2="40" stroke="currentColor" stroke-width="1.5"/>
  <rect x="40" y="72" width="20" height="108" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="66" y="66" width="20" height="114" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="92" y="102" width="20" height="78" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="118" y="126" width="20" height="54" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="144" y="144" width="20" height="36" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="170" y="150" width="20" height="30" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="196" y="156" width="20" height="24" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="222" y="162" width="20" height="18" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="50" y="62" font-size="11" text-anchor="middle" fill="currentColor">18</text>
  <text x="76" y="56" font-size="11" text-anchor="middle" fill="currentColor">19</text>
  <text x="102" y="92" font-size="11" text-anchor="middle" fill="currentColor">13</text>
  <text x="128" y="116" font-size="11" text-anchor="middle" fill="currentColor">9</text>
  <text x="154" y="134" font-size="11" text-anchor="middle" fill="currentColor">6</text>
  <text x="180" y="140" font-size="11" text-anchor="middle" fill="currentColor">5</text>
  <text x="206" y="146" font-size="11" text-anchor="middle" fill="currentColor">4</text>
  <text x="232" y="152" font-size="11" text-anchor="middle" fill="currentColor">3</text>
  <text x="140" y="205" font-size="12" text-anchor="middle" fill="currentColor">individuals per species (1, 2, 3, ...)</text>
  <text x="300" y="140" font-size="12" text-anchor="middle" fill="currentColor">long, sparse tail</text>
  <rect x="330" y="174" width="14" height="6" fill="currentColor" fill-opacity="0.4" stroke="currentColor"/>
  <text x="337" y="163" font-size="11" text-anchor="middle" fill="currentColor">1 species,</text>
  <text x="337" y="151" font-size="11" text-anchor="middle" fill="currentColor">~2,000+</text>
</svg>
<figcaption>The reconstructed linear counts behind the BCI figure. On a log2-binned axis the
geometrically widening bins make a bar around 30 individuals look tallest; on the true, linear
count the tallest bar is at 1, and the distribution falls away quickly except for one lone species
far out in the tail.</figcaption>
</figure>

The mean, by contrast, is $21457/225 \approx 95$, just under 100 — pulled far above the mode by a
handful of extremely abundant species (a couple with well over a thousand individuals). The median
sits close to where the log-binned figure's visually tallest bar actually is, which is presumably
why that bar gets mistaken for the mode. So mean, median and mode are wildly different numbers for
this distribution: roughly 100, 30, and 1. A distribution this skewed cannot even be plotted
sensibly on a linear axis — which is the honest reason to use the log-binned figure — but plotting
it that way leaves you with the false mental picture that most species have a moderate,
similar-sized population. The correct one-line summary, worth holding onto: **rare species are
common, and common species are rare.** This is not particular to BCI; it is what people have found
wherever they have counted, for hundreds of years (Darwin himself remarked on it), regardless of
exactly how fast the tail falls off or whether the plot is an island or a mainland.

## The species-area relationship

A second robust empirical pattern: if you count species in a larger area, you find more of them,
but sublinearly. If $S$ is the number of species observed and $A$ the area sampled,
$$
S \propto A^{z}, \qquad z \approx \tfrac14 .
$$
$z<1$ has to hold — if it were 1, doubling the area would double the species count, meaning a
second identical plot shares essentially no species with the first, which is not plausible. Both
of the model families below reproduce a power law of roughly this shape from quite different
microscopic pictures, which is a first hint of the chapter's real theme: a macroscopic pattern
being explained by a model does not mean the model's assumptions are the reason nature looks that
way. Many different microscopic processes generate power laws.

## Niche models: breaking the resource axis

The niche-theory account starts from MacArthur's 1957 broken-stick model. Picture a single,
homogeneous resource axis — some scarce thing that limits how many individuals a species can
support — and imagine dividing it among $N$ species, with each species' abundance proportional to
the length of axis it captures.

The naive way to divide it is to drop $N-1$ points uniformly at random on the stick and let the
gaps between them be the species' shares. Class discussion talked through why this does **not**
give a log-normal-shaped abundance distribution: uniform random points cannot produce either a very
long gap or a very short one with any appreciable frequency, so the resulting shares are far less
spread out than the real, heavily skewed data. A single random partition is the wrong generative
picture.

What does work is **sequential, hierarchical** breaking — the same axis broken multiple times,
each break acting only on the piece produced by the break before it. The motivating example given
in class: a bird community first divides its foraging resource between ground foragers and tree
foragers (say 30% versus 70%); within tree foraging, the resource divides again between trunk and
branch feeders; within branch feeding, it divides again between surface grubs and grubs under the
bark — and so on, at whatever level actually corresponds to real speciation events.

<figure>
<svg viewBox="0 0 380 200" role="img" aria-label="A resource axis broken sequentially into ground versus tree, then trunk versus branch, then surface versus sub-bark, rather than cut once into many pieces">
  <rect x="40" y="20" width="300" height="18" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <line x1="130" y1="20" x2="130" y2="38" stroke="currentColor" stroke-width="1.5"/>
  <text x="80" y="33" font-size="11" text-anchor="middle" fill="currentColor">ground 30%</text>
  <text x="235" y="33" font-size="11" text-anchor="middle" fill="currentColor">tree 70%</text>
  <line x1="130" y1="38" x2="130" y2="70" stroke="currentColor" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="340" y1="38" x2="340" y2="70" stroke="currentColor" stroke-width="1" stroke-dasharray="3,2"/>
  <rect x="130" y="70" width="210" height="18" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <line x1="250" y1="70" x2="250" y2="88" stroke="currentColor" stroke-width="1.5"/>
  <text x="190" y="83" font-size="11" text-anchor="middle" fill="currentColor">trunk</text>
  <text x="295" y="83" font-size="11" text-anchor="middle" fill="currentColor">branch</text>
  <line x1="250" y1="88" x2="250" y2="120" stroke="currentColor" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="340" y1="88" x2="340" y2="120" stroke="currentColor" stroke-width="1" stroke-dasharray="3,2"/>
  <rect x="250" y="120" width="90" height="18" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <line x1="295" y1="120" x2="295" y2="138" stroke="currentColor" stroke-width="1.5"/>
  <text x="270" y="133" font-size="11" text-anchor="middle" fill="currentColor">surface</text>
  <text x="318" y="133" font-size="11" text-anchor="middle" fill="currentColor">sub-bark</text>
  <text x="190" y="170" font-size="12" text-anchor="middle" fill="currentColor">each split re-divides only the piece it acts on</text>
</svg>
<figcaption>The niche hierarchy model: the resource axis is not cut once into many pieces, but
broken sequentially, each break acting only on the share produced by the break before it.</figcaption>
</figure>

Repeated enough times, this sequential breaking is exactly the process that gives a log-normal
distribution — and it has nothing special to do with biology. If you take a stone and crush it,
weigh the resulting fragments, the mass distribution is log-normal, for the same structural reason:
a piece breaks into smaller pieces, those break again, and a quantity built by successive
multiplicative shrinkage is log-normal by the same logic that a sum of independent random
quantities is normal (central limit theorem, but in log space, since multiplying corresponds to
adding logs). So a log-normal-shaped RSA distribution is evidence for *some* multiplicative
breaking process having gone into the abundances — but it is not, by itself, evidence for any
particular biological story about what did the breaking, or how many times, or according to what
probability rule. All of that is a separate, harder empirical question — and it was flagged in
class that a fair amount of work goes into asking what distribution actually governs each break
(uniform, or tilted, e.g. because whoever arrives at a resource first can monopolize a
disproportionate share of it).

## Neutral theory: an island fed by a metacommunity

The competing account, neutral theory, makes an almost absurdly minimal assumption: **every
individual is identical**, regardless of species. Same birth rate, same death rate, no advantage or
disadvantage from being a member of a large or small population (no Allee effect), no
species-specific competition. The claim is not that this is biologically true — it obviously is
not — but that it may already be sufficient to reproduce the observed pattern, which is itself an
important thing to learn if true.

The setup: a large **metacommunity** and a small **island** of fixed size $J$ individuals (the
island stands in for the 50-hectare plot). Each cycle, the process is a Moran process: pick one
random individual on the island and remove it. With probability $m$, replace it with an individual
drawn at random from the metacommunity (so migrants arrive in proportion to how abundant a species
already is on the mainland); with probability $1-m$, replace it by copying another individual
already on the island (a birth event local to the island). The island's total size never changes.
As $m \to 0$ this is pure ecological drift and one species eventually takes over the island
entirely, exactly as in genetic drift; as $m$ grows large, the island's composition increasingly
mirrors the metacommunity's.

Speciation — new species appearing — is assumed to happen only in the metacommunity, at some small
constant rate, and to be negligible on the island itself, because the island is small.

## The metacommunity distribution: Fisher's log series

The metacommunity's own steady-state abundance distribution can be solved exactly, by the same
detailed-balance argument used earlier in the course for one-step birth-death chains: at
equilibrium, the probability flux up from state $n$ must equal the flux down into it,
$$
P_n\, b_n = P_{n+1}\, d_{n+1}.
$$
Here the birth and death rates are, respectively,
$$
b_0 = \text{(constant speciation rate)}, \qquad b_n = b\,n \ (n\ge 1), \qquad d_n = d\,n,
$$
i.e. a species with $n$ individuals gains new members at a rate proportional to $n$ and loses them
at a rate proportional to $n$ — every individual can give birth and every individual can die — plus
a constant trickle of brand-new species entering at $n=1$. Telescoping the flux balance,
$$
P_n = P_0\left(\frac{b_0}{d}\right)\left(\frac{b}{d}\right)^{n-1}\prod_{k=1}^{n-1}\frac{k}{k+1}
    = P_0\,\frac{b_0}{b}\cdot\frac{x^n}{n}, \qquad x \equiv \frac{b}{d},
$$
using $\prod_{k=1}^{n-1} k/(k+1) = 1/n$. This is **Fisher's log series**: the expected number of
species with $n$ individuals in the metacommunity is proportional to $x^n/n$.

It is worth pausing on why this differs from the mRNA steady state solved earlier in the course,
which came out Poisson from the same kind of balance argument. There, the birth rate (transcription)
was a *constant*, independent of how much mRNA was already present, while the death rate
(degradation) was proportional to the amount present. Here it is the opposite: the birth rate is
proportional to how many individuals already exist — a species with twice as many members gains
new members twice as fast — while the death rate is also proportional. Constant-birth against
linear-death gives Poisson; linear-birth against linear-death gives the much heavier-tailed
$x^n/n$ instead. Convergence requires $x = b/d < 1$, i.e. death rates exceed birth rates for every
species individually — which sounds like it should drive everything extinct, and would, if there
were no constant speciation term $b_0$ continually replenishing the pool of species at $n=1$. Every
individual species does go extinct eventually; the metacommunity distribution is stationary only
because new ones are constantly created to replace them.

## Metacommunity versus island

The metacommunity's Fisher log series and the island's realized abundance distribution are not the
same object, and it is worth asking which falls off faster in the tail. Because of the extra $1/n$
factor, $x^n/n$ already decays faster than a plain geometric series would. But the island
distribution, built from the metacommunity by migration plus local drift, turns out to be *more*
heavy-tailed — more skewed toward abundant species — than the metacommunity itself. The mechanism:
migration onto the island samples the metacommunity in proportion to abundance there, so abundant
metacommunity species keep getting reinforced on the island, while rare species on the island are
constantly at risk of drifting to local extinction and are replaced disproportionately often by
migrants from the metacommunity's already-abundant species. The net effect is that the island ends
up with relatively more frequent, abundant species than the mainland it is fed from — the migration
process itself pushes the island's distribution toward the abundant end.

## Can the shape of the data tell the models apart?

Both families — the niche hierarchy (log-normal) and the neutral island-metacommunity model — give
curves that fit the BCI abundance data about equally well; nothing resembling a decisive
chi-squared verdict is available, partly because with counts this small the sampling noise on each
bin (of order $\sqrt{n}$) is already comparable to the difference between the two fitted curves.

Nor does a naive count of free parameters settle it. Both papers claim to have *fewer* free
parameters than their competitor, which cannot both be right, and the disagreement comes down to
bookkeeping: the neutral model's authors do not count the community size $J$ as free, because it is
externally measured from the data (the number of individuals sampled) rather than fit. But by the
same logic, the log-normal fit's overall amplitude is *also* fixed by the measured number of
individuals rather than truly free — so if $J$ doesn't count as a parameter, the amplitude
shouldn't either, and the two models end up with the same effective parameter count.

The lesson, stated plainly in class: writing down a model that is consistent with an observation
does not prove that model's assumptions are correct. When two models built on essentially opposite
assumptions — species are ecologically different, versus species are identical — both reproduce
the same static abundance pattern and the same species-area scaling, that pattern is telling you
less about the underlying microscale process than it might seem to.

What *does* discriminate between them is dynamics, not the static snapshot. Neutral theory predicts
that today's abundant species are only transiently abundant — since no species is intrinsically
better suited than any other, dominance should drift and turn over. Niche-based models predict that
an abundant species is abundant because it is actually well-matched to its niche, and so should
stay abundant. The observation reported in class is that, empirically, abundant species tend to
persist for longer than the neutral model predicts — evidence against strict neutrality. That does
not make the neutral model useless; on the contrary, the fact that a model with no
species-level differences at all can nonetheless reproduce the RSA pattern and the species-area
law is itself the valuable, surprising result. It shows how little of the macroscopic pattern
actually depends on species being different — and, as with the physical crushed-stone analogy,
is a caution about reading biological content into a shape a model produces for purely
mathematical reasons.

## Sources

- MIT 8.591j *Systems Biology* (Fall 2014), final lecture, transcript
  `recordings/m41dwardioc.md` (converted from `m41dwardioc-captions.srt`). This chapter draws on
  the whole transcript; timestamps for the main threads: BCI data description **[04:45–11:49]**;
  reading the abundance figure and reconstructing the true histogram **[12:55–30:57]**;
  species-area relationship **[47:09–51:44]**; niche/broken-stick models **[33:25–47:09]**; neutral
  theory setup **[51:44–59:23]**; Fisher log series derivation **[59:23–1:09:22]**;
  metacommunity-versus-island comparison **[1:09:22–1:11:40]**; model comparison and free
  parameters **[1:11:40–1:17:07]**.
- **Not supplied, referred to only**: the assigned paper the lecture discusses — described as
  giving a closed-form (semi-analytic) alternative to simulating the neutral model, and containing
  the single figure being reconstructed — is not named in the transcript and is not in this
  source set. Its Figure 1, and the professor's board redrawing of it, are likewise not captured
  here; the histogram values in this chapter are the professor's own verbal reconstruction of the
  underlying linear counts, not a reproduction of the figure. An email Q&A sent to students before
  class about how to read the figure is mentioned but not reproduced. MacArthur's 1957 broken-stick
  paper is referred to by author and year only. The classic RSA data sets used as points of
  comparison (beetles on the Thames, Fisher's original data) and comparative mainland-versus-island
  abundance measurements are mentioned as existing but not detailed.
- No slides, written notes, or exercises were supplied for this lecture (transcript-only source).

---

[← 17. Binding, Kinetics, and Ultrasensitivity](17-binding-kinetics-and-ultrasensitivity.md) · [Contents](index.md) · [19. Relaxation Oscillators and Scale-Free Networks →](19-relaxation-oscillators-and-scale-free-networks.md)
