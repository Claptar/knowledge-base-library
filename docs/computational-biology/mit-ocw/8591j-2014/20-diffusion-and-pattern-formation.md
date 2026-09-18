---
title: "20. Diffusion and Pattern Formation"
course: "MIT 8.591J 2014"
chapter: 20
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 20. Diffusion and Pattern Formation

## What this covers

Diffusion is usually thought of as the process that erases structure. This chapter asks when it
can instead build structure, and works through three settings from the lecture where that question
matters in developmental and cell biology: how a single diffusing morphogen sets up positional
information (and why the simplest version of that mechanism is fragile), how two diffusing,
reacting species can spontaneously form a spatial pattern (Turing's mechanism, and a noisy variant
of it), and how a bacterium locates the middle of itself to divide (the Min system). It assumes
Fick's law for diffusive flux and comfort with ordinary steady-state ODEs; nothing beyond that is
needed.

## Diffusion: what sets the flux, and what sets the rate of change

Fick's law says the diffusive flux of a chemical at concentration $C(x,t)$ in one dimension is

$$J = -D\frac{\partial C}{\partial x},$$

proportional to minus the local slope of the concentration profile, not to the concentration
itself. That single fact resolves a question that is easy to get backwards: if a profile falls
off in a straight line from $c_1$ down to $c_2$ over some length, the flux is the *same* at every
point along it, even though the concentration itself is different at each point — because the
slope is constant along a straight line. The direction of that flux is set by the sign of the
slope: a positive $dC/dx$ gives a flux in the negative direction.

It is tempting to think a net flux at a point means the concentration there is changing, but that
conflates two different things. Conservation of mass gives

$$\frac{\partial C}{\partial t} = -\frac{\partial J}{\partial x},$$

so it is not the flux itself but the *difference* between the flux arriving and the flux leaving —
the divergence of the flux — that changes the local concentration. Substituting Fick's law gives
the diffusion equation (Fick's second law),

$$\frac{\partial C}{\partial t} = D\,\frac{\partial^2 C}{\partial x^2}.$$

On the straight-line profile above, the flux is the same at every interior point, so nothing there
is changing at all — even though particles are flowing steadily to one side. The concentration only
starts moving at the two ends of the domain, and even then the profile does not develop a kink; it
curves in smoothly from the edges on its way to the flat, uniform steady state.

The point sharpens further on a profile with a bump in it. What determines $\partial C/\partial t$
at a given point is the local *curvature* $\partial^2 C/\partial x^2$ — not the concentration
there and not the flux there.

<figure>
<svg viewBox="0 0 380 220" role="img" aria-label="A bumpy concentration profile with a trough, an inflection point, and a peak, showing that the rate of change tracks curvature">
  <line x1="40" y1="180" x2="340" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <text x="345" y="184" font-size="12" fill="currentColor">x</text>
  <path d="M40,130 C70,150 90,158 100,155 C120,150 150,125 170,110 C190,95 210,65 230,55 C255,45 280,90 300,120 C315,138 330,132 340,130"
        fill="none" stroke="currentColor" stroke-width="2"/>
  <circle cx="100" cy="155" r="3.5" fill="currentColor"/>
  <text x="95" y="172" font-size="12" fill="currentColor">A</text>
  <text x="70" y="172" font-size="11" fill="currentColor">concave up: filling in</text>
  <circle cx="170" cy="110" r="3.5" fill="currentColor"/>
  <text x="176" y="108" font-size="12" fill="currentColor">C</text>
  <text x="176" y="122" font-size="11" fill="currentColor">inflection: momentarily fixed</text>
  <circle cx="230" cy="55" r="3.5" fill="currentColor"/>
  <text x="236" y="52" font-size="12" fill="currentColor">D</text>
  <text x="236" y="38" font-size="11" fill="currentColor">concave down: flattening</text>
  <circle cx="300" cy="120" r="3.5" fill="currentColor"/>
  <text x="284" y="105" font-size="12" fill="currentColor">B</text>
</svg>
<figcaption>The rate of change at a point tracks the local curvature, not the concentration or the
flux there: the trough at A is filling in, the peak at D is flattening, and the inflection point C
is unchanged for this next instant — even though it is not the flattest or most extreme point on
the curve.</figcaption>
</figure>

That is the sense in which only the *next* instant is simple: if $C(x,t)$ is known now, then
$C(x, t+\Delta t) \approx C(x,t) + \Delta t\,\partial C/\partial t$ is fixed purely by the curvature
at $x$ right now. What happens over a longer stretch of time is a different, harder question — a
sharp local peak is exactly the kind of feature that curvature erases quickly, so the profile that
was fastest-changing a moment ago need not stay that way for long.

## Morphogen gradients and the French flag model

A recurring problem in development: an embryo starts as a collection of genetically identical
cells with no positional information — no way to know whether to become head, body, or tail. One
classical solution is the **French flag model**: a single diffusing protein (a *morphogen*) is
produced at one end (often from maternally deposited mRNA) and diffuses outward, producing a
concentration profile along the embryo. A cell then reads its fate purely from the local morphogen
concentration it feels: below some threshold $M_1$ it becomes one tissue type, between $M_1$ and
$M_2$ another, and so on — dividing the tissue into stripes, as on a flag, from nothing but a
concentration gradient and a set of thresholds.

The shape of that gradient depends entirely on what happens to the morphogen once it is out in the
tissue. Two extreme cases:

**No degradation in the interior**, only at the far boundary (e.g. the morphogen is destroyed the
moment it reaches the far end). Then the steady-state profile solves $D\,d^2M/dx^2 = 0$, whose
general solution is linear:

$$M(x) = Ax + B.$$

**First-order degradation everywhere** in the interior, at rate $\alpha M$. The steady state
solves $D\,d^2M/dx^2 - \alpha M = 0$, giving an exponential profile

$$M(x) = M_0\,e^{-x/L}.$$

The decay length $L$ can be pinned down before solving anything, by dimensional analysis: $D$ has
units of length$^2$/time and $\alpha$ has units of 1/time, so the only combination of the two with
units of length is $\sqrt{D/\alpha}$ — and solving the equation confirms $L = \sqrt{D/\alpha}$
exactly. The same ratio shows up whenever a first-order process (degradation, uptake, absorption)
competes with diffusion — nutrients diffusing into a biofilm and being taken up by cells follow the
same form.

The production rate needed to sustain this profile is exactly the flux right at the source:
$J(0) = -D\,dM/dx\big|_{0} = D M_0/L$. Differentiating $M_0 e^{-x/L}$ and evaluating at $x=0$ gives
$dM/dx|_0 = -M_0/L$, so the source has to supply morphogen at rate $D M_0/L$ to hold the boundary
concentration at $M_0$.

This is clean, but it has a robustness problem. What a cell actually controls at the source is
typically the **production rate**, not the concentration $M_0$ directly — a fixed $M_0$ is a
convenient boundary condition for the mathematics, but biologically the thing set by (say) one or
two copies of a gene is the rate morphogen is made, and $M_0$ is whatever concentration that
production rate happens to produce. Because there is no positional information anywhere in the
interior of the embryo except what is imposed at the boundary, changing $M_0$ (or the production
rate that sets it) does not change the *shape* of the profile — it just slides the whole thing up
or down. Nothing inside corrects for the change. So a profile generated this way is not robust to
the natural variation in production rate that comes from things like gene copy number.

## Building in robustness: self-enhanced degradation

One proposal (from the reading referred to in the lecture as the "Eldar" model) for making the
gradient more robust is to replace plain first-order decay with a general degradation function
$F(M)$ that depends on the morphogen concentration $M$ itself, but crucially **not on position $x$
directly**. Allowing $F$ to depend on $x$ would already assume the positional information the
gradient is supposed to generate — that would be solving the problem by assuming it solved.

The concrete phenomenological choice is **self-enhanced degradation**: a degradation rate that
grows faster than linearly in $M$, for example $F(M) \propto M^2$. Biologically this need not mean
the morphogen degrades itself directly; the lecture's examples were indirect, via a receptor —
the morphogen binds a receptor, and the bound receptor then activates degradation of the morphogen
(seen in a couple of different receptor systems in Drosophila development, in the wing as well as
elsewhere).

Two consequences:

- **The far-field shape changes.** Instead of an exponential tail, the profile falls off at large
  $x$ as a power law, $M(x) \sim A/x^2$ (this particular exponent, for degradation exactly
  proportional to $M^2$, is one of the exercises in Murray's book). A power-law tail decays more
  gently far from the source than an exponential one does — the same contrast as between a
  power-law and an exponential degree distribution in a network: the exponential makes large values
  vanishingly rare, while the power law keeps a long tail. So positional information can, in
  principle, be read out further from the source.
- **The near-field profile becomes self-correcting.** The intuitive reason, from the lecture's own
  discussion: if $M_0$ is perturbed upward, the higher $M$ drives degradation that grows faster
  than $M$ itself, so the excess is removed disproportionately fast, and the profile relaxes back
  toward roughly where it started. A plain first-order decay has no such restoring force — doubling
  $M_0$ just doubles the profile everywhere.

## A worked example: protease, inhibitor, morphogen, complex

The lecture worked through a more detailed model — from the same reading, describing patterning in
the dorsal region of an early Drosophila embryo — as an exercise in reading assumptions out of a
model's equations. The setup: a morphogen needs to end up confined to a well-defined region; an
inhibitor diffuses in from outside that region; a protease is present, uniformly distributed
(and, being uniform, is not tracked as its own diffusing variable); and the inhibitor and morphogen
bind to form a complex.

The equations (for the inhibitor $I$, the complex $C$, and the morphogen $M$, each diffusing) encode
several distinct assumptions, and the exercise is to read them straight off the terms:

- The complex forms by mass-action binding, at a rate proportional to $I \cdot M$ — with no reverse
  term included, i.e. the model assumes binding is effectively irreversible on the relevant
  timescale.
- The protease cleaves the complex at a rate proportional to the protease concentration times $C$.
  This term appears as $-\alpha C$ in the complex's equation and as $+\alpha C$ in the morphogen's
  equation — the morphogen comes out intact — but there is *no* matching $+\alpha C$ restoring free
  inhibitor. The absence of that term is itself a modelling statement: it says the protease
  destroys the inhibitor as it cleaves the complex, rather than simply releasing both halves.
- Separately, the protease can also degrade free, uncomplexed inhibitor directly, at its own rate —
  a term that "always occurs at some rate" in principle, and whose size relative to the other terms
  is exactly the kind of assumption a model has to be explicit about.

The authors then searched numerically over a wide range of parameters (total concentrations of
inhibitor, morphogen, and protease) for where a robust morphogen pattern emerges — robust meaning
insensitive to those overall concentrations. Robustness appeared specifically when two things were
true: the direct "protease degrades free inhibitor" term vanishes (protease degrades the inhibitor
only when it is part of the complex — a conclusion that already had independent experimental
support, so it was not an unmotivated assumption), and the free morphogen's diffusion coefficient is
very small compared to the complex's diffusion coefficient.

That second condition is genuinely strange. Simple physical diffusion (Stokes drag) says a bigger
object diffuses *more slowly*, not faster — so a large morphogen–inhibitor complex diffusing faster
than the small free morphogen cannot be ordinary thermal diffusion. It has to be additional biology:
active transport of the complex, or some other binding dynamic. The lecture noted that later
experimental work did find evidence for something along these lines. The broader moral, stated
explicitly: a computational parameter scan like this is not a proof that this is what the biology
does — the model could be missing terms entirely — but it generates a testable hypothesis, and
being able to read a model's assumptions straight off its equations is a basic skill for anyone
using someone else's model.

## Reaction–diffusion (Turing) patterns

Diffusion is generally the thing that removes spatial structure: push concentration up somewhere
and diffusion pulls it back down; push it down and diffusion fills it back in. So it is a genuinely
surprising fact — due to Turing, from late in his life — that a system of reacting chemicals which
would settle to one uniform steady state if simply mixed in a well-stirred tube can instead form a
*persistent spatial pattern* once diffusion is switched on.

The rough heuristic offered for when this happens is **local activation together with global
inhibition** — but the lecture was explicit that this is only a form of words to guide intuition;
what actually decides it is the sign structure of the derivatives around the relevant fixed point,
and that can be subtle: something that looks like an "activator" or "inhibitor" by name need not
play that role once you check what its derivatives actually do near the steady state in question.

**The Levin–Segel model (1976).** Originally proposed as an ecological model of plankton (prey,
$\psi$) and a herbivore that eats them (predator, $\varphi$) — a predator–prey pair, in the
notation later used by Butler and Goldenfeld. Its ingredients: the herbivore depends on and preys
on the plankton (and dies at some rate in its absence); the plankton has an ordinary exponential
self-growth term, *plus* a second, faster-than-exponential growth term (something like a $\psi^2$
term), reflecting individuals benefiting from each other's presence — historically motivated by
"predator satiation" and known generally as the **Allee effect**; and each species diffuses, the
prey with coefficient $\mu$, the predator with coefficient $\nu$.

In a well-mixed (non-spatial) system, this has a stable coexistence steady state. The Turing
question is what happens to a small spatial perturbation of that steady state, decomposed into
wavelengths (wavenumbers $k$): linearising the reaction–diffusion equations gives a growth rate
(eigenvalue) $\lambda(k)$ for each wavenumber, and if $\lambda(k) > 0$ over some band of $k$, those
modes grow — setting the spacing of the resulting pattern.

Concretely, the local activation is the plankton's self-reinforcing $\psi^2$ term: a patch with a
little extra plankton grows itself further. That growth also drives up the predator locally, but
because the predator diffuses much faster ($\nu \gg \mu$), it spreads away from the patch and
suppresses the *neighbouring* regions — the global inhibition. For a particular choice of the
model's other parameters, the lecture gave the threshold as

$$\frac{\nu}{\mu} > 27.8$$

for Turing patterns to appear, and the general lesson (not tied to that particular number) is that
the inhibiting species must diffuse much faster than the activating one.

That ratio is uncomfortably large for ordinary molecular diffusion. In the low-Reynolds-number
regime relevant to molecules, $D \sim k_BT/\gamma$ and Stokes drag $\gamma$ scales linearly with
particle radius, so $D$ scales as $1/\text{radius}$ — *linearly*, not with the square or cube of
radius. Producing a diffusivity ratio of $\sim 28$ from size alone would then require the activator
to have a radius roughly 30 times that of the inhibitor, which is not a typical range for real
protein sizes. That is the practical limitation of the mean-field Turing mechanism as a
stand-alone explanation for real patterns.

## Demographic noise can also make patterns

Even when the deterministic condition above is not satisfied, explicit stochastic simulation of the
same underlying birth–death events — a prey being born, a predator eating a prey, exactly the kind
of random events tracked in a Gillespie-type simulation — can produce pattern-like structure on its
own. This is sometimes called a quasi- or pseudo-Turing pattern, and the threshold for it is far
less demanding: with demographic noise included, $\nu/\mu$ only needs to be about $2.48$ (work by
Butler and Goldenfeld using field-theoretic methods, papers from around 2008–2009 and 2011).

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Growth rate versus wavenumber for a true Turing instability compared with a noise-driven near-instability">
  <line x1="40" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <text x="305" y="184" font-size="12" fill="currentColor">k</text>
  <line x1="40" y1="100" x2="300" y2="100" stroke="currentColor" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="15" y="104" font-size="12" fill="currentColor">0</text>
  <text x="8" y="40" font-size="12" fill="currentColor">&#955;(k)</text>
  <rect x="140" y="55" width="70" height="125" fill="currentColor" fill-opacity="0.15"/>
  <path d="M40,140 C90,130 120,80 145,65 C165,53 185,53 205,65 C230,80 260,130 300,140"
        fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M40,155 C90,150 120,130 145,120 C165,113 185,113 205,120 C230,130 260,150 300,155"
        fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="212" y="70" font-size="11" fill="currentColor">Turing: unstable band</text>
  <text x="212" y="132" font-size="11" fill="currentColor">noise-driven: slow decay only</text>
</svg>
<figcaption>The solid curve is a genuine Turing dispersion relation: over a band of wavenumbers
the growth rate crosses above zero, and those modes grow into a mean-field pattern. The dashed
curve never crosses zero — nothing is truly unstable — but it comes close over roughly the same
band, and demographic noise keeps re-exciting every wavenumber; the ones in that band decay so
slowly that they build up into pattern-like structure anyway.</figcaption>
</figure>

The same logic applies to patterns in time as well as in space — a preview of the noise-induced
predator–prey oscillations covered later in the course: a system sitting near a stability boundary
can be kept visibly "excited" by its own demographic fluctuations, whether the near-critical
direction is a spatial wavenumber or a temporal frequency.

Asked directly whether real plankton–herbivore spatial patterns are actually due to this mechanism,
the lecture's answer was candid: it is not established. It would require the herbivore to move away
from a patch distinctly faster than the plankton does — plausible in direction, since plankton
mostly drift with currents while herbivores can swim directedly, but the lecture was explicit about
not knowing whether the actual numbers work out.

## Finding the middle: the Min system in E. coli

A rod-shaped E. coli cell, roughly six microns long, has to divide into two before it gets too
large, and it needs to divide near the middle. Division happens when a ring of a polymerising
protein (the "Z-ring") forms around the cell's midpoint and constricts, pinching the membrane into
two daughter cells. The problem is how the cell locates that midpoint without any obvious way to
measure "the middle" directly.

The system responsible was found, as usual in bacterial genetics, through mutants: get the division
site wrong — place it near a pole instead of the centre — and the result is one long daughter cell
carrying both copies of the genome, plus a small cell with no DNA at all, a "minicell." (Minicells
can survive for a while and even keep making protein, which has made them of some interest for
synthetic biology, but they have no long-term future without DNA.) The genes responsible are named
for this phenotype: the **Min system**. Two of the originally proposed genes, MinA and MinB, turned
out on closer inspection not to be the real players; the three that matter are MinC, MinD, and
MinE.

- **MinC** directly blocks Z-ring formation wherever it is present.
- **MinD** binds the membrane and recruits MinC to wherever MinD itself is.
- **MinE** binds MinD and ejects it from the membrane.

Imaging fluorescently labelled MinD (and MinE) in living cells shows a striking oscillation: MinD
accumulates at one pole, MinE arrives and knocks it back off the membrane there, MinD then
accumulates at the *other* pole, MinE follows it there too, and so on — a pole-to-pole oscillation
with a period of the order of minutes. MinC is not needed to generate this oscillation at all; it
simply follows wherever MinD happens to be.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Time-averaged MinD concentration along the length of a rod-shaped cell, high at both poles and dipping at midcell">
  <path d="M40,30 C80,26 130,50 170,58 C210,50 260,26 300,30" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="10" y="28" font-size="11" fill="currentColor">MinD</text>
  <text x="10" y="42" font-size="11" fill="currentColor">(time-avg.)</text>
  <rect x="40" y="70" width="260" height="40" rx="20" ry="20" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="170" y1="58" x2="170" y2="90" stroke="currentColor" stroke-width="1" stroke-dasharray="4,3"/>
  <ellipse cx="170" cy="90" rx="10" ry="14" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="130" y="130" font-size="12" fill="currentColor">Z-ring forms only where MinC is absent</text>
  <text x="45" y="150" font-size="11" fill="currentColor">pole</text>
  <text x="280" y="150" font-size="11" fill="currentColor">pole</text>
</svg>
<figcaption>MinD (and MinC, which follows it) spends its time oscillating between the two poles, so
averaged over the oscillation period its concentration is lowest at midcell — the one place left
free for the Z-ring, without anything ever having measured "the middle" directly.</figcaption>
</figure>

Because MinD — and therefore MinC — spends nearly all its time near one pole or the other, its
time-average over the oscillation period is depleted specifically at midcell. Midcell becomes,
without any component measuring distance, simply the point that is least often visited by MinC —
and so the one place the Z-ring is free to form. The cell finds its middle as the point equidistant
from two oscillating ends, not by measuring the distance to either end.

**In vitro.** Purified, fluorescently labelled MinD and MinE, added to a supported lipid bilayer (a
membrane laid down on glass) with no other cellular components present, reproduce travelling-wave
patterns closely resembling the reaction–diffusion waves seen inside the cell (work from Martin
Loose, in Petra Schwille's lab in Dresden). That two purified proteins plus a membrane are
sufficient to generate the pattern shows the mechanism does not need the rest of the cell. As the
MinE concentration is varied in this system, the wave velocity changes measurably, making it a
directly trackable experimental system. The waves require ATP — a general feature of Turing-type
pattern formation is that it is inherently a non-equilibrium, energy-consuming process, not
something that can happen at thermodynamic equilibrium.

A photobleaching experiment makes a subtle point about what the "wave" actually is. Locally bleach
(erase the fluorescence of) a patch of the pattern, and ask whether that bleached spot travels along
with the wave or stays where it is: it stays fixed. The travelling pattern is not a matter of
individual labelled molecules being carried along together — there is no directed-motion term for
any molecule in these models at all, only diffusion. The apparent wave motion is a purely collective
effect of local reaction and diffusion happening throughout the system, not the trajectory of any
particular molecule.

## Sources

All of this chapter is from the transcript of the recorded lecture at
`docs/computational-biology/mit-ocw/8591j-2014/recordings/recordings/onl-uf4flvm.md` (MIT OCW
8.591J, Systems Biology, Fall 2014). No slides, problem sets, or written notes were supplied for
this lecture; it is transcript-only, so anything drawn on the board is not reproduced here — only
described where the spoken discussion makes its content clear enough to state (the flux/curvature
clicker profiles, the morphogen boundary-value sketches, the protease–inhibitor–morphogen–complex
equations, the Levin–Segel terms).

By section:

- Diffusion review and clicker exercises: 00:00–18:28.
- French flag model, linear vs. exponential morphogen profiles, robustness problem: 18:28–32:53.
- Self-enhanced degradation and the protease/inhibitor/morphogen/complex model: 32:53–50:06.
- Turing patterns, the Levin–Segel model, the diffusivity-ratio plausibility check: 50:06–1:04:45.
- Demographic-noise-induced patterns: 1:04:45–1:09:24.
- The Min system, in vivo and in vitro: 1:09:24–end (1:20:37).

Named but not contained here, and referred to by the lecture rather than supplied:

- The diffusion notes by Alexander Van Oudenaarden, used as the assigned background reading for the
  diffusion review.
- A reading on robust mechanisms for pattern formation, attributed in the lecture to the "Eldar"
  model/chapter (the source's title is not given in the transcript, and one further name given for
  a related reading is transcribed only as "Noori's book" — uncertain in the source audio and not
  otherwise identifiable).
- Murray's book (J.D. Murray, *Mathematical Biology*, referred to by name), including the exercise
  on the power-law tail of a self-enhanced-degradation profile decaying as $M^n$.
- Butler and Goldenfeld's papers on demographic-noise-enhanced Turing patterns (field-theoretic
  approach; referenced as roughly 2008–2009 and 2011, no titles given).
- The in vitro MinD/MinE reconstitution work of Martin Loose in Petra Schwille's lab (Dresden), and
  the accompanying movie of the reaction–diffusion waves, shown in class but not present in this
  transcript.
- Mehran Kardar's course *Statistical Physics in Biology*, recommended in the lecture for more
  depth on the Turing/noise-induced pattern material.
- All board drawings referenced by the clicker questions (the concentration profiles for the
  flux/curvature exercises, and the sketched steady-state morphogen profiles) — described in the
  text above from what the discussion of them establishes, but not themselves in the source.

---

[← 19. Relaxation Oscillators and Scale-Free Networks](19-relaxation-oscillators-and-scale-free-networks.md) · [Contents](index.md) · [21. Autoregulation and Molecular Titration →](21-autoregulation-and-molecular-titration.md)
