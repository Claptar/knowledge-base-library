---
title: "16. Tipping Points and Species Competition"
course: "MIT 8.591J 2014"
chapter: 16
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 16. Tipping Points and Species Competition

## What this covers

This chapter asks when a population — or, by the same argument, a whole ecosystem — responds to a
slowly changing environment by tracking it smoothly, and when instead it can suddenly collapse, with
little warning and no easy way back. It builds the answer from the two simplest one-population growth
models, logistic growth and the Allee effect, works out their bifurcation structure as a death rate is
turned up, and asks what an observer could measure *before* the collapse to see it coming. It then
turns to a second population and develops the Lotka–Volterra competition model by the same
geometric method — nullclines in the plane — used earlier in the course for predator–prey dynamics.
It assumes you can already find and classify fixed points of a one-dimensional ODE by linearizing
around them; the vocabulary of transcritical and fold (saddle-node) bifurcations is built here from
scratch.

## Logistic growth and the Allee effect

Write the population size as $N$ and ask how it grows. The crudest model is exponential growth,
$\dot N = rN$: the per-capita growth rate $\gamma(N) = \dot N/N$ is just the constant $r$, and
$N\to\infty$ regardless of where you start.

Logistic growth adds the simplest correction that keeps the population bounded: at low density the
population still grows at rate $r$, but the per-capita rate decreases linearly with density,

$$\dot N = rN\left(1 - \frac{N}{K}\right), \qquad \gamma(N) = r\left(1-\frac N K\right).$$

$\gamma(N)$ is a straight line, starting at $r$ when $N=0$, crossing zero at the carrying capacity
$N=K$, and going negative beyond it — which is why a population started above $K$ still comes back
down to it.

The reason to divide by $N$ and look at $\gamma$ rather than $\dot N$ itself is that $\gamma$ is the
"happiness" of a single individual: it is the rate at which *that individual* can expect to
reproduce. For logistic growth, $\gamma$ is monotonically decreasing — more individuals always means
less space, resources, or mates for you, so crowding is always bad, for every individual, at every
density.

The Allee effect is what happens when that is no longer true: over some range of $N$, an additional
individual actually *helps* everyone else, so $\gamma$ is increasing there ($d\gamma/dN > 0$ for some
$N$). The lecture's convention is to distinguish a **strong** Allee effect, where $\gamma(0) < 0$ —
the population declines even at vanishingly low density — from a weak one, where $\gamma$ stays
positive near $N=0$ but still has a range of positive slope. The strong case is the interesting one,
because it produces a second, positive fixed point beneath $K$: a minimum population size $n_{\min}$
below which the population is doomed, and above which it grows back up to the stable size $K$.

<figure>
<svg viewBox="0 0 340 230" role="img" aria-label="Per-capita growth rate against population size, comparing logistic growth to the strong Allee effect">
  <defs>
    <marker id="ar1" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="45" y1="15" x2="45" y2="210" stroke="currentColor" stroke-width="1.2" marker-end="url(#ar1)"/>
  <line x1="45" y1="210" x2="315" y2="210" stroke="currentColor" stroke-width="1.2" marker-end="url(#ar1)"/>
  <text x="20" y="20" font-size="12" fill="currentColor">&#947;(N)</text>
  <text x="300" y="225" font-size="12" fill="currentColor">N</text>
  <line x1="45" y1="140" x2="310" y2="140" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 3"/>
  <text x="315" y="143" font-size="11" fill="currentColor">0</text>
  <rect x="45" y="15" width="65" height="195" fill="currentColor" fill-opacity="0.1" stroke="none"/>
  <text x="47" y="200" font-size="10.5" fill="currentColor">N &#60; n_min: declines</text>
  <line x1="45" y1="50" x2="300" y2="175" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/>
  <text x="120" y="90" font-size="12" fill="currentColor">logistic</text>
  <path d="M45,170 C70,150 90,140 110,140 C130,140 150,90 170,75 C190,90 210,130 230,140 C250,150 270,170 300,185"
        fill="none" stroke="currentColor" stroke-width="1.8"/>
  <text x="185" y="55" font-size="12" fill="currentColor">Allee effect</text>
  <line x1="110" y1="140" x2="110" y2="210" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 2"/>
  <line x1="230" y1="140" x2="230" y2="210" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 2"/>
  <text x="95" y="222" font-size="12" fill="currentColor">n_min</text>
  <text x="222" y="222" font-size="12" fill="currentColor">K</text>
</svg>
<figcaption>Logistic growth: crowding is always bad, so &#947; decreases monotonically to zero at K.
The strong Allee effect: &#947; is negative below a threshold n_min (shaded), rises through a range
where extra individuals help, and falls back to zero at the stable size K. Below n_min the
population is doomed; above it, it recovers to K.</figcaption>
</figure>

The lecture asked, and the class supplied, several concrete mechanisms that produce an Allee effect:

- **Sexual reproduction** — below some density, individuals cannot reliably find mates. Whether this
  matters in practice is a quantitative question about how large $n_{\min}$ actually is: if
  $n_{\min}\sim 2$ it is no constraint at all; if a species needs on the order of a hundred
  individuals (the example raised was the California condor) to be viable, it is a serious one.
- **Group hunting** — wolves can bring down bison that no single wolf could; the same logic applies
  to primates and, at the microbial scale, to organisms that break food down with a secreted enzyme
  outside the cell, so that no single cell benefits from breaking down food alone.
- **Predator avoidance** — herding in land animals, schooling in fish: an individual in a crowd is
  less likely to be the one caught.
- **Predator satiation**, an example of what the lecture called *effective* cooperation: nobody
  intends to cooperate, but if there are enough individuals present the predator gets full before it
  can eat everyone, so being one of many raises your own odds of surviving. All four mechanisms are
  naturally described as some form of cooperative growth, whether on the hunting side or the
  protection side.

## Two different bifurcations from the same knob

Now add a death rate $\delta$ — standing for anything that removes individuals independently of
density: hunting, fishing, a pollutant. The question the lecture poses is whether turning $\delta$ up
slowly can produce a *sudden* transition — the kind of tipping point described in early-warning-
indicator studies of ecosystems, climate regimes, and other complex systems responding to a slowly
changing external parameter.

**Logistic plus death** gives $\dot N = N\big(r(1-N/K) - \delta\big)$, with fixed points $N=0$ and

$$N^*(\delta) = K\left(1 - \frac{\delta}{r}\right).$$

As $\delta$ increases from $0$, the stable equilibrium $N^*$ decreases *linearly* and smoothly to
zero, reaching it exactly at $\delta = r$. At that point the two fixed points — $N^*$ and $N=0$ — meet
and *exchange stability*: for $\delta<r$, $N^*$ is stable and $N=0$ is unstable; for $\delta>r$ it is
the reverse (the algebraic continuation of $N^*$ becomes negative, which is unphysical, and simply
tracks the now-unstable branch). This is a **transcritical bifurcation**: the number of fixed points
never changes, they just swap stability as they pass through each other. There is no jump — the
population runs down smoothly to extinction as $\delta\to r$, so plain logistic growth has no tipping
point.

**The Allee effect plus death** is different. Subtracting $\delta N$ shifts the whole $\gamma(N)$
curve down uniformly, which pulls the stable fixed point (starting at $K$ when $\delta=0$) and the
unstable one (starting at $n_{\min}$) *towards each other*. At a critical death rate $\delta_c$ they
meet and annihilate — not exchanging stability, but disappearing entirely, "folding over on
themselves." Beyond $\delta_c$ the only fixed point left is $N=0$: the population collapses to
extinction. This is a **fold** (or saddle-node) bifurcation, and it is exactly the pattern of a
sudden transition: a smooth, slow change in the environmental knob $\delta$ produces a
discontinuous jump in the population once $\delta_c$ is crossed.

<figure>
<svg viewBox="0 0 660 240" role="img" aria-label="Bifurcation diagrams of population size against death rate, contrasting a transcritical bifurcation with a fold bifurcation">
  <defs>
    <marker id="ar2" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
      <polygon points="0,0 7,3.5 0,7" fill="currentColor"/>
    </marker>
  </defs>
  <g>
    <line x1="40" y1="20" x2="40" y2="210" stroke="currentColor" stroke-width="1.2" marker-end="url(#ar2)"/>
    <line x1="40" y1="210" x2="290" y2="210" stroke="currentColor" stroke-width="1.2" marker-end="url(#ar2)"/>
    <text x="14" y="30" font-size="12" fill="currentColor">N*</text>
    <text x="270" y="226" font-size="12" fill="currentColor">&#948;</text>
    <text x="90" y="235" font-size="11" fill="currentColor">transcritical (logistic)</text>
    <line x1="40" y1="60" x2="190" y2="210" stroke="currentColor" stroke-width="2"/>
    <line x1="40" y1="210" x2="190" y2="210" stroke="currentColor" stroke-width="2" stroke-dasharray="5 4"/>
    <line x1="190" y1="210" x2="270" y2="210" stroke="currentColor" stroke-width="2"/>
    <line x1="190" y1="20" x2="190" y2="210" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 2"/>
    <text x="180" y="222" font-size="11" fill="currentColor">r</text>
    <text x="45" y="55" font-size="11" fill="currentColor">K</text>
    <text x="200" y="140" font-size="10.5" fill="currentColor">stable and unstable branch</text>
    <text x="200" y="153" font-size="10.5" fill="currentColor">cross at N=0, &#948;=r</text>
  </g>
  <g transform="translate(360,0)">
    <line x1="40" y1="20" x2="40" y2="210" stroke="currentColor" stroke-width="1.2" marker-end="url(#ar2)"/>
    <line x1="40" y1="210" x2="290" y2="210" stroke="currentColor" stroke-width="1.2" marker-end="url(#ar2)"/>
    <text x="14" y="30" font-size="12" fill="currentColor">N*</text>
    <text x="270" y="226" font-size="12" fill="currentColor">&#948;</text>
    <text x="115" y="235" font-size="11" fill="currentColor">fold (Allee effect)</text>
    <path d="M40,60 C120,70 175,100 200,140" fill="none" stroke="currentColor" stroke-width="2"/>
    <path d="M40,170 C100,160 160,150 200,140" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="5 4"/>
    <line x1="40" y1="210" x2="290" y2="210" stroke="currentColor" stroke-width="2"/>
    <line x1="200" y1="140" x2="200" y2="210" stroke="currentColor" stroke-width="1.4" stroke-dasharray="3 3" marker-end="url(#ar2)"/>
    <text x="205" y="185" font-size="10.5" fill="currentColor">collapse</text>
    <line x1="200" y1="20" x2="200" y2="210" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2 2"/>
    <text x="188" y="222" font-size="11" fill="currentColor">&#948;_c</text>
    <text x="45" y="55" font-size="11" fill="currentColor">K</text>
    <text x="45" y="165" font-size="11" fill="currentColor">n_min</text>
  </g>
</svg>
<figcaption>Left: adding a death rate to logistic growth is a transcritical bifurcation — the stable
and unstable branches cross and swap roles, and N* runs smoothly to zero. Right: adding a death rate
to the Allee effect is a fold — the stable branch (from K) and unstable branch (from n_min) approach
each other and annihilate at &#948;_c, at which point the population that was tracking the stable
branch has nowhere to go but N = 0.</figcaption>
</figure>

The qualitative difference matters beyond the shape of the jump. In the fold case the system is
**hysteretic** — it has memory. Once $\delta$ has been pushed past $\delta_c$ and the population has
collapsed to $N=0$, simply lowering $\delta$ back below $\delta_c$ does not bring the population
back, because $N=0$ is a fixed point (of the underlying growth model) at every $\delta$: nothing in
the dynamics reintroduces individuals. Recovery requires an actual reintroduction, or an environment
good enough to overcome the basin boundary again. The transcritical case has no such asymmetry:
turning $\delta$ back down brings $N^*$ back up along the same curve it came down on. The lecture
gave two real-world instances of the fold pattern: the historical collapse of the Monterey Bay
sardine fishery, and the eutrophication transitions observed in some lake ecosystems, where nutrient
runoff pushes a clear lake into a persistent algae-dominated state that is hard to reverse even after
the runoff stops. It is worth noting that a transcritical bifurcation can also look dramatic — a
modest change in $\delta$ can still produce a large change in $N^*$ if the exchange point sits away
from the origin — so "sudden-looking" is not by itself evidence of a fold; what distinguishes the two
is whether reversing the environmental change actually recovers the population.

## Seeing the transition coming: critical slowing down

The assigned review argued that, near either kind of transition, the dominant eigenvalue governing
the *linearized* dynamics goes to zero — a phenomenon called **critical slowing down** — and that
this leaves measurable fingerprints before the transition happens. Linearizing around an equilibrium
$N_{\rm eq}$, write $N = N_{\rm eq}+\epsilon$; substituting into the growth equation gives
$\dot\epsilon = \lambda\epsilon$, so $\epsilon$ decays as $e^{\lambda t}$ with $\lambda<0$ at a stable
fixed point and $\lambda>0$ at an unstable one.

The lecture put this to a vote: does $\lambda$ go to zero at a *transcritical* bifurcation, or only at
a fold? The class split roughly 50/50. The resolution: yes, at both. In the transcritical case, the
stable branch has $\lambda<0$ for $\delta<r$ and the unstable branch (algebraically the same fixed
point, continued) has $\lambda>0$ for $\delta>r$; since the two branches meet at exactly $\delta=r$,
$N=0$, their eigenvalues must meet there too, and the only way for a continuously varying $\lambda$ to
be negative on one side and positive on the other of the same point is to pass through zero exactly
there. The fold, the transcritical, and the Hopf bifurcation (where a stable point turns into
sustained oscillations) are all, in this sense, "zero-eigenvalue" bifurcations, and critical slowing
down is a feature of all of them in principle — though what actually matters physically is the
eigenvalue of the branch the system is *sitting on*, not of some other fixed point that also happens
to cross zero at the same parameter value.

A useful way to picture this for any one-dimensional system $\dot N = f(N)$ is to write it as motion
of an overdamped particle in an effective potential, $\dot N = -dU/dN$. Near a stable fixed point,
$U$ looks like a well, and the analogy the lecture used is a bead trapped in an optical (laser) trap:
turning down the laser power weakens the trap's effective spring constant, which broadens and
shallows the well. For a bead at fixed temperature, a shallower well means (i) larger-amplitude
thermal fluctuations and (ii) a longer relaxation time — the time for the bead to drift back after
being nudged, which is also the correlation time of its ambient fluctuations. As $\delta\to\delta_c$
in the Allee-effect model, the local minimum of $U$ around the population's equilibrium broadens the
same way, right up until the minimum disappears entirely at the fold — which is exactly the moment
the population has nowhere stable to sit and rolls off toward extinction.

This gives two flavours of temporal early-warning signal:

- **Recovery time after an explicit perturbation.** Pull the population away from its equilibrium (a
  drought, a bad season) and watch how long it takes to relax back. That recovery time grows as the
  bifurcation is approached. There is a second effect layered on top of slower recovery: the same
  size of perturbation that was easily survived at low $\delta$ can, at higher $\delta$, push the
  population past the (now much closer) unstable branch — because the gap between the stable and
  unstable branches, a direct measure of the population's *resilience*, shrinks as $\delta\to
  \delta_c$.
- **Ambient fluctuations, with no deliberate perturbation.** Even a population in a constant
  environment has natural fluctuations. Their variance, and the autocorrelation time over which they
  decay, both grow as the transition is approached — the same phenomenon as the bead's thermal
  jiggling growing as the trap weakens.

One caveat raised in discussion: this picture assumes a noise source of fixed strength, added
independently of the state — like a constant-temperature bath. If the randomness is instead
*demographic* (arising from the discreteness of individual birth and death events, so its strength
scales with population size itself), then as the population shrinks toward the transition the noise
strength can shrink too, which complicates the simple "fluctuations must grow" prediction. Critical
slowing down is expected in principle near any such transition, but that does not guarantee it is
observable in practice — it can be masked by noise, by other confounds, or (as with demographic
noise) by the noise strength itself changing with the state.

The lecture reported that this had been tested directly: a laboratory yeast population engaging in a
form of group-level cooperative growth (secreting an enzyme that breaks sugar down outside the cell)
showed measurable growth in exactly these signatures — increasing variance, autocorrelation time,
and recovery time — as the population was pushed toward its own Allee-type collapse.

*Aside, from a student question:* does any of this apply to human societies? The lecturer's answer
was that the qualitative mechanism — strong enough feedback loops producing abrupt regime shifts — is
probably a fairly general and robust phenomenon, and pointed to concerns about climate feedbacks such
as the North Atlantic Oscillation, and to a recent article speculating about a possible tipping point
in global agricultural productivity around the year 2050. But he was explicit that establishing the
mechanism qualitatively is a very different problem from being able to *quantitatively* predict
whether or when a specific real system will tip, and that deciding what to do given that uncertainty
is a judgment call the model itself cannot make.

## A spatial analogue: recovery length

The same idea has a static, spatial counterpart, previewed here ahead of a fuller treatment of
spatially extended populations. Instead of tracking $N(t)$ in a uniform environment, consider a
population density $n(x)$ in a spatially varying one. If the environment quality changes only slowly
with position, the local population density simply tracks the local quality and there is nothing
extra to measure — the spatial analogue of the earlier caveat that a slowly drifting $\delta$ gives
you no clean signal either.

But if there is a sharp boundary — a hunted region next to a protected one, or any abrupt step in
quality — the population density near the boundary is depleted *below* its local equilibrium value
even on the good side of the boundary, and it takes a characteristic distance, a **recovery length**,
to relax back up to the equilibrium set by the local (good) environment. This recovery length is a
direct measure of the quality of the good region, and it is often much easier to measure in practice
than the temporal signals above: it is a static profile, not a time series, so there is no need to
wait for a rare event like a drought or to gather a long enough run of data to see the fluctuations
grow. The lecture mentioned a field collaboration studying algal-mat communities in intertidal zones
on Mediterranean islands, where the experimenters deliberately create a controlled poor-quality patch
(by chipping away the rock over some area) and then measure how the mat's density recovers with
distance away from it.

## Two-species competition: the Lotka–Volterra competition model

The last topic turns to two interacting populations, using the same phenomenological style as the
Lotka–Volterra predator–prey model but for **competitive** rather than predator–prey interactions:

$$\dot N_1 = r_1 N_1\left(1 - \frac{N_1 + \beta_{12}N_2}{K_1}\right), \qquad
\dot N_2 = r_2 N_2\left(1 - \frac{N_2 + \beta_{21}N_1}{K_2}\right),$$

with $r_1, r_2 > 0$, so that in the absence of the other species each population simply grows
logistically to its own carrying capacity. The new ingredient is the cross term $\beta_{12}N_2$
(respectively $\beta_{21}N_1$) inside species 1's (2's) own carrying-capacity term: it says that
individuals of the *other* species also eat into the same limited resource, at some exchange rate
$\beta$ relative to a member of your own species. For the interaction to be genuinely competitive,
the class reasoned, both $\beta$'s must be positive: an individual of the other species can never
*help* you in this model, only hurt you more, less, or the same as one of your own kind. $\beta<1$
means the other species is a weaker competitor for the resource than your own kind (more niche
separation); $\beta>1$ means it is a stronger one.

The standard way to analyse this is geometrically, via **nullclines** in the $(N_1,N_2)$ plane — the
curves along which one of the two derivatives vanishes. These are not fixed points: a fixed point
needs *both* derivatives to vanish simultaneously, which (away from the axes) happens only where the
two nullclines actually cross.

$$\dot N_1 = 0 \iff N_1 = 0 \text{ or } N_1 + \beta_{12}N_2 = K_1, \qquad
\dot N_2 = 0 \iff N_2 = 0 \text{ or } N_2 + \beta_{21}N_1 = K_2.$$

Away from the axes, each is a straight line: the $N_1$-nullcline runs from $(K_1,0)$ to
$(0,K_1/\beta_{12})$, and the $N_2$-nullcline from $(0,K_2)$ to $(K_2/\beta_{21},0)$.

Two straight lines, each with both intercepts positive, can sit relative to one another in exactly
four qualitatively distinct ways: one line can lie entirely above the other (two cases, depending on
which one), or the two lines can cross inside the positive quadrant (two more cases, depending on the
order of the intercepts). When the lines don't cross, there is no interior fixed point at all, so
coexistence is impossible and the outcome is exclusion — one species wins regardless of the (nonzero)
starting numbers of both. When the lines do cross, there is an interior fixed point, but whether it
is stable (coexistence) or unstable (bistability — a history-dependent outcome in which either species
can win, depending on where you start) depends on which line has the larger intercept on which axis.
The lecture worked through one of the four cases in detail before running out of time, deferring the
remaining three to the next lecture.

<figure>
<svg viewBox="0 0 340 240" role="img" aria-label="Nullclines of the Lotka-Volterra competition model in the case where species 1 always wins">
  <defs>
    <marker id="ar3" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto">
      <polygon points="0,0 7,3.5 0,7" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="40" y1="20" x2="40" y2="210" stroke="currentColor" stroke-width="1.2" marker-end="url(#ar3)"/>
  <line x1="40" y1="210" x2="310" y2="210" stroke="currentColor" stroke-width="1.2" marker-end="url(#ar3)"/>
  <text x="14" y="30" font-size="12" fill="currentColor">N2</text>
  <text x="295" y="226" font-size="12" fill="currentColor">N1</text>
  <line x1="250" y1="210" x2="40" y2="50" stroke="currentColor" stroke-width="2"/>
  <text x="60" y="48" font-size="11" fill="currentColor">N1' = 0</text>
  <text x="243" y="222" font-size="11" fill="currentColor">K1</text>
  <text x="16" y="53" font-size="11" fill="currentColor">K1/&#946;12</text>
  <line x1="180" y1="210" x2="40" y2="110" stroke="currentColor" stroke-width="2" stroke-dasharray="5 4"/>
  <text x="140" y="140" font-size="11" fill="currentColor">N2' = 0</text>
  <text x="170" y="222" font-size="11" fill="currentColor">K2/&#946;21</text>
  <text x="16" y="113" font-size="11" fill="currentColor">K2</text>
  <circle cx="250" cy="210" r="4" fill="currentColor"/>
  <text x="220" y="196" font-size="10.5" fill="currentColor">stable: species 1 wins</text>
  <line x1="110" y1="150" x2="150" y2="180" stroke="currentColor" stroke-width="1.3" marker-end="url(#ar3)"/>
  <line x1="150" y1="90" x2="200" y2="130" stroke="currentColor" stroke-width="1.3" marker-end="url(#ar3)"/>
  <line x1="220" y1="175" x2="245" y2="205" stroke="currentColor" stroke-width="1.3" marker-end="url(#ar3)"/>
</svg>
<figcaption>The N1-nullcline lies entirely above the N2-nullcline: the two lines never cross in the
positive quadrant, so there is no interior fixed point. Trajectories starting anywhere with both
species present flow toward (K1, 0) &#8212; species 1 always wins.</figcaption>
</figure>

This is the case where the $N_1$-nullcline sits entirely above the $N_2$-nullcline (formally,
$K_1/\beta_{12} > K_2$, and correspondingly $K_1 > K_2/\beta_{21}$), and it was identified as the case
in which species 1 wins regardless of starting condition. The sanity check offered in the lecture:
take the limit $\beta_{12}\to 0$, so that species 2 does nothing at all to inhibit species 1's growth
while species 1 goes on strongly inhibiting species 2. In that limit the $N_1$-nullcline's
$N_2$-intercept, $K_1/\beta_{12}$, goes to infinity — the line swings up and away from the origin —
which is exactly the geometric picture above, confirming that this configuration is the one in which
the less-inhibited species (species 1) is guaranteed to win.

## Sources

This chapter is built entirely from the transcript of one MIT OpenCourseWare 8.591J (*Systems
Biology*, Fall 2014) lecture, `recordings/lc3xswq62iw.md` in `ocw-8591j-2014`. No slides, notes, or
problem set were supplied for this session, and the transcript captures speech only — everything that
was written on the board (the exact drawn shape of the $\gamma(N)$ curves, the bifurcation diagrams,
the effective-potential sketches, and the nullcline plots) is described here from what the lecturer
said about it, not from an image of the board; the figures above are reconstructions from that verbal
description, not reproductions.

By section: single-population growth and the Allee effect, transcript 00:00–23:14; the two
bifurcations and hysteresis, 23:14–31:04; critical slowing down, the effective-potential picture, and
the two flavours of early-warning signal, 31:04–50:31; the spatial recovery length, 50:31–53:45; the
aside on human-scale tipping points, 53:45–55:59 (continued to 58:16); the Lotka–Volterra competition
model and its nullclines, 59:29–end.

Referred to but not contained in the supplied material:

- **The assigned review article** on early-warning indicators for sudden transitions in ecosystems,
  climate regimes, and other complex systems — described throughout as "the review that you read" but
  neither titled nor supplied.
- **A Science or Nature article** (title and authors not given) speculating about a possible
  human-society tipping point around 2050 tied to agricultural productivity.
- **The Monterey Bay sardine fishery / Monterey Bay Aquarium display**, offered as a real historical
  example of a fold-type collapse, and the lake **eutrophication** literature, offered as an example
  of ecosystem-level hysteresis — neither cited by name.
- **The lecturer's own lab's yeast experiments**, measuring critical-slowing-down signatures in a
  population that cooperatively breaks down sugar via a secreted enzyme, and the **field
  collaboration with a University of Pisa researcher** measuring recovery lengths in intertidal
  algal-mat communities on Mediterranean islands — mentioned but not otherwise documented here.
- **Rock–paper–scissors (non-transitive) interactions** — lizard mating strategies in the California
  mountains, and Benjamin Kerr's bacterial toxin-production experiments — explicitly deferred to the
  next lecture and not covered in this one.
- **The remaining three geometric cases** of the Lotka–Volterra competition model (species 2 wins,
  stable coexistence, and unstable bistability/mutual exclusion), and a fuller treatment of **spatially
  extended populations** — both explicitly deferred to the next lecture.
- A preview mention of **neutral theory in ecology** and species diversity, flagged as the topic of a
  later class and not developed here.

---

[← 15. The Moran Process and Fixation](15-the-moran-process-and-fixation.md) · [Contents](index.md) · [17. Binding, Kinetics, and Ultrasensitivity →](17-binding-kinetics-and-ultrasensitivity.md)
