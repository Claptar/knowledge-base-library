---
title: "22. Diffusion, Uptake, and Bacterial Chemotaxis"
course: "MIT 8.591J 2014"
chapter: 22
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 22. Diffusion, Uptake, and Bacterial Chemotaxis

## What this covers

How does a bacterium find food? This chapter builds up to an answer almost entirely through
dimensional analysis: given only the units of the quantities that could plausibly matter, how far
can you get toward the physical law before you need something more? It works through diffusion
across a punctured membrane, nutrient uptake by a cell modeled as a perfect absorber, the
statistical noise in measuring a concentration by counting molecules, and why a bacterium runs and
tumbles instead of measuring a spatial gradient directly. It assumes the definitions of a diffusion
coefficient and of a Poisson process, and treats the Reynolds number as background from an assigned
reading rather than deriving it here.

## Salt through a hole in a membrane

Set the scene: a non-permeable membrane in water separates a salty solution (concentration $c$) on
the right from pure water on the left. Puncture a hole of radius $a$ in the membrane. What is the
net flow of salt — number of molecules per unit time — from right to left?

The first move in any dimensional-analysis problem is to list every quantity that could plausibly
enter, and pin down its units. Here that list is short: the concentration $c$, the pore radius $a$,
and the diffusion coefficient $D$ of the salt, which by the Einstein relation is $D = kT/\gamma$ for
some friction coefficient $\gamma$ — this is also where temperature enters, since raising the
temperature raises $D$.

If you don't remember the units of a quantity like $D$ (or viscosity, which is notoriously hard to
remember), the trick is to find some equation already in your head where the symbol is used
correctly, and read the units off that. For $D$, the relevant fact is the mean-squared diffusion
distance, $\langle x^2\rangle \sim Dt$, which fixes $D$ as a length squared over time — for salt in
water, something like microns squared per second.

The answer we want has units of $1/\text{time}$ (a number of molecules, which carries no units, per
unit time). Only one of the three ingredients — $D$ — carries a unit of time at all, so $D$ must
enter linearly: any other power would leave a stray $\sqrt{\text{time}}$ or $\text{time}^2$ with
nothing to cancel it against.

That's as far as pure dimensional analysis goes on its own, and — as a question from the room
pointed out — it does not go far enough by itself. Because $c$ has units of $1/\text{length}^3$ and
$a$ has units of length, the combination $ca^3$ is already dimensionless, and dimensional analysis
alone would let you multiply the answer by any power of $ca^3$ and it would still come out with the
right units. Something more is needed to fix that freedom. The extra fact is that the salt molecules
are *non-interacting*: they diffuse independently of each other, and if you double the concentration
on the right, you double the flow — no interference between molecules to complicate that. So the
flow has to be proportional to $c$ itself, i.e. $c$ enters to the first power. Once that's fixed,
dimensional balance leaves only one possibility left for the pore radius:

$$ \text{flow} \;\propto\; D\,c\,a. $$

That is a strange answer: the flow through the hole scales with the *radius* of the pore, not its
area, even though the amount of membrane you've opened up grows like $a^2$. Ask a room of people to
predict how the flow changes when you double $a$, and the overwhelming answer — even from people
who have just walked through the derivation above — is still "goes up by 4," because it feels like
an area. That's worth sitting with: knowing the derivation doesn't automatically fix the intuition,
and the whole point of doing the dimensional analysis carefully is to catch a case where intuition
is wrong.

### Why radius, and not area

The naive picture treats crossing the pore like bullets hitting a target: hit rate proportional to
target area. That picture is right for a beam of independent particles flying in straight lines,
but diffusion doesn't work that way. Diffusion moves down a *gradient* of concentration, and the
moment you puncture the hole, a depletion zone forms around it: the concentration doesn't stay flat
at $c$ right up to the edge of the pore and then drop suddenly — it tapers off gradually as
molecules are drawn toward the hole from progressively farther away. As you make the pore bigger,
the new flow through the middle of it is competing with the flow already established near the
edges, because both are drawing on the same depleted region. The pore is, in a sense, competing
with itself.

That competition is easiest to see by comparing one pore to two. Two pores of the same size $a$,
placed far apart, give exactly double the flow of one, because their depletion zones don't overlap
and a molecule that diffuses into one pore's zone was never a candidate for the other's. Bring the
two pores close together, though, and the zones start to overlap: a molecule that would have gone
through one might just as easily have gone through the other, so adding the second pore buys less
than a full doubling. Growing a single pore is the continuous version of the same effect.

This is also a timescale-dependent statement. The instant after you puncture the membrane, before
any depletion zone has had time to form, the flow really does scale as the area: it's just "how
many molecules happen to be sitting within reach of the hole," and that count is proportional to
$a^2$. That transient settles down — typically in a microsecond or so — into the steady, depleted
state where the flow scales as $a$, and stays there for as long as the reservoir lasts.

## How much food can a cell eat?

The same reasoning answers a directly related question: what is the maximum possible rate at which
a cell can take up a nutrient by diffusion? Model the cell as a sphere of radius $a$ that is a
*perfect absorber* — the instant a nutrient molecule touches the cell's surface, it is imported and
consumed. No real membrane is a perfect absorber, but it sets an upper bound, and it is the same
dimensional-analysis problem as the punctured membrane: an uptake rate (molecules per unit time), a
concentration $c$ far from the cell, a diffusion coefficient $D$, and a length scale $a$. By exactly
the argument above, the maximum uptake rate scales linearly with the cell's radius, not its surface
area. The exact prefactor is not something dimensional analysis alone can hand you — that takes
solving the actual diffusion equation around a sphere — but for a full sphere it works out to

$$ \text{uptake rate} = 4\pi D c a. $$

### The surface is mostly wasted, and that's useful

Because uptake only grows as $a$ and not $a^2$, a fully-absorbing cell surface has a lot of spare
capacity: most of that area contributes little beyond what a much smaller absorbing patch already
would. That suggests replacing the whole absorbing surface with a sparse scatter of small,
independently-absorbing patches — transporters, perhaps a nanometer across — and asking how the
total uptake rate depends on the fraction of the surface those patches cover.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Uptake rate rises far faster than the fraction of the cell surface covered by transporters, and saturates near the maximum while most of the surface is still bare, unlike the naive linear guess.">
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="212" text-anchor="middle" font-size="12" fill="currentColor">fraction of surface covered by transporters</text>
  <text x="16" y="105" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 16 105)">uptake / maximum</text>

  <line x1="40" y1="190" x2="300" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="150" y="140" font-size="11" fill="currentColor">naive: uptake &#8733; area covered</text>

  <path d="M40,190 C44,70 65,35 110,26 C170,22 240,20 300,20" fill="none" stroke="currentColor" stroke-width="2"/>

  <line x1="42.6" y1="190" x2="42.6" y2="105" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
  <line x1="40" y1="105" x2="42.6" y2="105" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
  <circle cx="42.6" cy="105" r="2.5" fill="currentColor"/>
  <text x="52" y="100" font-size="11" fill="currentColor">~1% coverage, ~50% of maximum uptake</text>

  <text x="300" y="206" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="40" y="206" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="30" y="24" text-anchor="end" font-size="11" fill="currentColor">1</text>
</svg>
<figcaption>Sketch of the uptake-versus-coverage curve described in the lecture. Because sparse,
far-apart patches barely compete with each other, uptake rises almost linearly at first and is
already near its ceiling while most of the surface is still bare — not tracking the area covered,
as the naive guess would have it.</figcaption>
</figure>

The mechanism is the same competition-for-depletion-zone argument as the two-pore case: when the
patches are far apart relative to their own size, each one absorbs at close to its own independent
rate (something like $Dca_{\text{patch}}$, up to a numerical prefactor the lecture left unresolved
between $1$, $2\pi$, and $4\pi$, depending on the exact geometry of a patch on a sphere versus a
patch on a plane), and the total is just the sum over patches. Only once the patches are packed
densely enough that their depletion zones start to overlap does the curve bend over and saturate.
The number quoted in lecture: covering roughly 1% of a cell's surface with small, well-separated
absorbing patches can already recover about half of the fully-covered maximum uptake rate.

This is also why a cell can afford to specialize: it needs to import many different things — carbon
sources, nitrogen, various trace metals — and since a small area devoted to one kind of transporter
already captures most of the uptake that area could ever give, the cell can tile its surface with
many different transporter types, each covering a small fraction of the area, and get near-optimal
uptake of several nutrients at once rather than trading one off against another.

## How precisely can a cell measure a concentration?

Suppose a cell measures a concentration the only way a perfect absorber can: by counting the
molecules it absorbs over some time $t$. The mean number absorbed is $n = (4\pi Dca)\,t$, and
because absorption events happen independently and at random, the actual count on any one occasion
is Poisson-distributed with that mean; the waiting time between successive absorption events is
exponentially distributed; and once the mean count is large, the distribution looks Gaussian, by
the central limit theorem.

The relevant measure of how good this measurement is, is not the absolute error but the
*fractional* error, $\sigma_c/c$, since that tells you how many significant figures of the
concentration you can trust. Because the count you actually measure, $n$, and your estimate of $c$
are related by a fixed proportionality constant, that constant cancels out of the fractional error:

$$ \frac{\sigma_c}{c} = \frac{\sigma_n}{n}. $$

For a Poisson-distributed count, the variance equals the mean, so $\sigma_n = \sqrt{n}$, and

$$ \frac{\sigma_c}{c} = \frac{1}{\sqrt{n}} = \frac{1}{\sqrt{4\pi D c a\,t}}. $$

Longer measurement times, higher concentrations, and faster diffusion all reduce the fractional
error — which makes sense, since all three mean more molecules counted.

One trap surfaced in the discussion and is worth recording. A student asked whether, since $n$ is
Poisson, the cell's *estimate* of $c$ — which is $n$ multiplied by some conversion constant — is
also Poisson. It is not: multiplying a Poisson random variable by a constant $k$ scales its mean by
$k$ but its variance by $k^2$, so mean and variance are no longer equal, and the result is not
Poisson at all. What is true is only that the estimate of $c$ inherits the *same fractional* error
as the count $n$ — it is the Poisson structure of the underlying count, not the Poisson property
itself, that survives the rescaling.

### Absorbing beats monitoring

A perfect absorber is provably the best a cell can do — better, in particular, than a "perfect
monitor," a hypothetical detector that registers a hit every time a molecule touches it but does
not remove the molecule from solution. The monitor turns out to be substantially worse (something
like a factor of ten), and the reason is that it can register the same molecule bouncing off it
several times, with no way to tell that it's the same molecule come back — adding extra counts that
look independent but are not really new information. Tagging an absorbed molecule and never
counting it again, rather than physically removing it, gives back exactly the absorber's
performance: because the molecules are non-interacting, whether you remove one or merely mark it
makes no difference to the statistics. There is no missing "local depletion" effect to worry about
here, unlike the multi-pore geometry above — a non-interacting molecule carries no information
about any other, whether or not it is still physically present.

## Why a bacterium doesn't just measure the gradient

Knowing the concentration precisely at one instant doesn't tell a cell which way to swim — for that
it needs the *gradient*. One way to get it: compare the concentration sensed on two sides of the
cell, separated by roughly the cell's own diameter, $2a$. The difference in molecules counted on the
two sides scales as $2a\,(dc/dx)$ — a genuine, if small, amplification of the underlying gradient by
the cell's own size. Some eukaryotic cells (the lecture names *Dictyostelium* as an example) are
large enough to do exactly this: sense the gradient directly across the body.

A bacterium is not. At a cell size of order one to a few microns, the signal from comparing two
sides of the body is too small to be useful. Instead, a bacterium measures the concentration at one
point but at two different *times*, as it swims: is the concentration higher now than it was a
moment ago? If things are improving, it keeps swimming in the same direction (a "run"); if not, it
randomizes its direction (a "tumble") and tries again. This implements a biased random walk toward
food, and it effectively substitutes a long *run length* (E. coli runs are on the order of 30
microns, taking about a second) for the short *body length* as the baseline over which the
concentration difference is measured — a much longer antenna than the cell's own size would allow,
built out of time rather than space.

## Why the run doesn't just get longer

If a longer run gives a more reliable measurement of the gradient, why not run ten or a hundred
times longer? Two separate physical facts cap the useful run length, and both come out of the low
Reynolds number regime the assigned reading described.

**Coasting is negligible.** In everyday life, something moving at high speed keeps drifting for a
while after the driving force stops, because momentum carries it forward. Not for a bacterium. A
cell about 3 microns across, swimming at 30 microns per second — ten body lengths per second —
coasts only about $10^{-5}$ microns (a tenth of an angstrom) after its flagellar motor stops. That
number is absurdly small by human standards, and it is a direct consequence of the Reynolds number
being far below 1: viscous forces so dominate inertial ones that the moment the driving force is
removed, motion simply stops. There is no momentum left to exploit by running longer.

**Orientation itself randomizes.** Independent of the concentration measurement, a swimming cell
loses track of its own heading through rotational diffusion — the rotational analogue of the
ordinary translational diffusion discussed above. The same dimensional-analysis exercise applies:
by the Einstein relation, a rotational diffusion coefficient $D_r = kT/\gamma_r$ exists, where
$\gamma_r$ is now a *rotational* friction coefficient (torque per unit angular velocity, rather than
force per unit velocity). For a sphere, Stokes' law gives the translational drag $\gamma =
6\pi\eta a$ and the rotational drag $\gamma_r = 8\pi\eta a^3$ — an extra factor of $a^2$, which is
exactly the unit gap between the two diffusion coefficients: $D$ (translational) has units of
length$^2$/time, while $D_r$ (rotational) has units of just $1/\text{time}$, since an angle is
dimensionless. That extra length$^2$ is what turns a linear-in-$a$ drag into a cubic-in-$a$ drag.

Setting the mean-squared reorientation angle to order 1 radian$^2$, $2D_r\tau \sim 1$, gives the
correlation time over which a cell's heading randomizes:

$$ \tau \;\sim\; \frac{1}{2D_r} = \frac{\gamma_r}{2kT} = \frac{4\pi\eta a^3}{kT}. $$

Plugging in numbers in piconewton-nanometer-second units ($kT \approx 4.1\ \text{pN·nm}$, water
viscosity $\eta \approx 10^{-9}$ in these units, and a bacterial radius $a \approx 1\ \mu\text{m} =
10^3\ \text{nm}$, so $a^3 = 10^9\ \text{nm}^3$) gives $\tau$ of order a few seconds — the
back-of-the-envelope calculation in lecture landed close to $\pi$ seconds, with "order 1 to 10
seconds" being the honest precision of an estimate like this. That is squarely the same order as
the observed run length of about a second. A bacterium doesn't run longer than this because, by the
time it would, it has already forgotten which direction it was supposed to be going — extending the
run buys no more usable information about the gradient once the memory of heading is gone.

One more feature of this drag is worth keeping: it is dominated by an object's *longest* dimension,
almost regardless of shape or orientation. A rod with an aspect ratio of 1000-to-1 (a nanometer by a
micron) still has $\gamma_\parallel$ and $\gamma_\perp$ differing by only about a factor of two,
because in the viscous, low-Reynolds regime what matters is how much fluid the whole length of the
object drags along with it as it moves, not the cross-sectional area it presents to the flow —
unlike the aerodynamic drag on, say, a skydiver, where cross-section is what counts.

## Sources

All content is from the lecture transcript
`docs/computational-biology/mit-ocw/8591j-2014/recordings/recordings/tuxfwkrwqg8.md` (MIT 8.591J,
*Systems Biology*, Fall 2014, OCW, CC BY-NC-SA), by timestamp:

- **[00:00]–[02:24]** framing: bacteria finding food, life at low Reynolds number, dimensional
  analysis as the day's tool.
- **[02:24]–[26:00]** the punctured-membrane problem: setting up the variables, the class vote on
  the scaling, the resolution ($\text{flow}\propto Dca$), the depletion-zone intuition, the
  two-pore comparison, and the short-time transient.
- **[27:07]–[39:57]** the cell as a perfect absorber, the $4\pi Dca$ result, and the patch/coverage
  argument.
- **[39:57]–[53:44]** Poisson counting statistics, the fractional-error formula, and perfect
  absorber versus perfect monitor.
- **[53:44]–[1:03:55]** direct gradient sensing versus the temporal, run-and-tumble strategy.
- **[1:03:55]–[1:19:06]** coasting distance, the Reynolds number, and the rotational-diffusion
  derivation of the reorientation timescale.

This is a transcript-only lecture: everything the professor wrote on the board — the sketches of
the punctured membrane, the cell and its patches, the uptake-versus-coverage curve, and every
equation as it was actually written — is not in the source, and had to be reconstructed here from
what was said about it.

Two sources are pointed at but not contained in this lecture. The assigned reading on "life at low
Reynolds number" (Purcell's essay) is referred to at **[00:00]** and again at **[1:00:38]** for the
definition of the Reynolds number itself, and is not reproduced here. An unnamed paper describing
the bacterial biased random walk and its underlying gene network is referred to at **[53:44]** and
again at **[1:19:06]** as the subject of the following lecture (Tuesday).

---

[← 21. Autoregulation and Molecular Titration](21-autoregulation-and-molecular-titration.md) · [Contents](index.md) · [23. Predator-Prey Cycles and Their Fragility →](23-predator-prey-cycles-and-their-fragility.md)
