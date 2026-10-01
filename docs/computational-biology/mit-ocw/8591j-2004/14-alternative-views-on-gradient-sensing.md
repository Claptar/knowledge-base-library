---
title: "14. Alternative views on gradient sensing"
course: "MIT 8.591J 2004"
chapter: 14
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 14. Alternative views on gradient sensing

## What this covers

This chapter looks at two published alternatives to the reaction–diffusion (Turing-type,
local-excitation/global-inhibition) model of chemotactic gradient sensing from the preceding
lecture, and asks the question that motivates them: how can a cell read a shallow external
gradient without becoming irreversibly polarized? It assumes the activator–inhibitor model from
that lecture — a pair of reaction–diffusion equations for a local activator and a diffusing
inhibitor, their homogeneous steady state, and the idea that this system can undergo a Turing
instability and lock into a spatial pattern — together with ordinary one-dimensional diffusion.

## Why look for an alternative

The two papers behind this lecture are Postma and van Haastert, "A diffusion-translocation model
for gradient sensing by chemotactic cells" (*Biophys. J.* **81**, 1314, 2001), and Levchenko and
Iglesias, "Models of eukaryotic gradient sensing: applications to chemotaxis of amoeba and
neutrophils" (*Biophys. J.* **82**, 50, 2002). The lecture states the shared motivation for both up
front: **how to prevent cells from polarizing irreversibly**. A Turing-type activator–inhibitor
system, once it has broken symmetry and settled into a polarized pattern, has no particular reason
to leave it — the instability that produced the pattern is a genuine bifurcation of the homogeneous
state. Real chemotactic cells, in contrast, reorient when the direction of an external gradient
changes. So the models below are built around a different property: instead of a pattern-forming
instability, they rely on *adaptation* — a steady state that tracks the current signal and relaxes
back to it whenever the signal changes — and ask whether adaptation alone is enough to read a
spatial gradient.

## Confining the readout to where the receptor is

The first model treats the cell as producing a second messenger $m$ on the membrane, at rate $P$,
decaying at rate $k_{-1}$, and diffusing with membrane diffusion constant $D_m$:

$$\frac{dm}{dt} = D_m \frac{\partial^2 m}{\partial x^2} - k_{-1} m + P$$

Two very different values of $D_m$ matter here, because the point is to compare a membrane-bound
signalling molecule against a cytosolic one:

$$D_m \sim 1\ \mu\text{m}^2\text{s}^{-1}\ \text{(membrane protein, lipid)}, \qquad D_m \sim
100\ \mu\text{m}^2\text{s}^{-1}\ \text{(cytosolic small molecule)}$$

For $m$ to hold a spatial pattern at all — for the messenger produced more strongly on one side of
the cell to stay more concentrated there than on the other side — diffusion must not have time to
spread it across the whole cell before it decays. Balancing the diffusion and decay terms gives the
natural length scale over which $m$ spreads before decaying:

$$\lambda = \sqrt{\frac{D_m}{k_{-1}}}$$

and the condition for a usable gradient is $\lambda \ll L$, the cell size. With $k_{-1} = 1\
\text{s}^{-1}$ and $L = 10\ \mu\text{m}$: a membrane-bound messenger gives $\lambda = 1\ \mu\text{m}
\ll L$ — it stays local. A cytosolic messenger with $D_m \sim 100\ \mu\text{m}^2\text{s}^{-1}$ gives
$\lambda = 10\ \mu\text{m} \sim L$: diffusion has time to spread it across the whole cell before it
decays, and whatever spatial information the receptor put into it is gone. This is the argument for
why the molecule that is supposed to carry gradient information has to be slow-diffusing: a
fast-diffusing cytosolic species averages itself out before it can be read as a gradient.

## From a receptor gradient to a messenger gradient — and losing gain

Now let the *production* of $m$ itself be graded across the cell, following the local fraction of
activated receptor:

$$\frac{dm}{dt} = D_m \frac{\partial^2 m}{\partial x^2} - k_{-1} m + P(x), \qquad P(x) = k_R\left(
\bar{R}^* - \Delta R^* \frac{x}{r}\right)$$

so $P(x)$ is largest where receptor occupancy is highest and falls off linearly across the cell
radius $r$. Even with $\lambda < L$, diffusion still flattens this imposed profile somewhat before
$m$ reaches steady state, so the resulting gradient in $m$ is shallower than the gradient in
$P(x)$ that drove it. The lecture calls this a *gain* less than 1, and notes that the gain gets
worse — smaller — the larger $D_m$ is: more diffusion, more flattening, as expected. That leaves an
open question, since real chemotactic cells respond to gradients only a few percent steep across
their length: something has to turn a sub-unity gain into an amplified readout.

## Amplifying with positive feedback

The lecture's answer is a translocation loop between a cytosolic and a membrane pool of an
"effector" protein, $E_c$ and $E_m$:

- **A.** Before receptor stimulation, only a small number of (inactive) effectors sit on the
  membrane.
- **B.** After receptor stimulation, the membrane-bound effectors are stimulated to produce more of
  a phospholipid second messenger.
- **C.** The local increase in phospholipid recruits more effector from the cytosol to the
  membrane — translocation.
- **D.** With more effector now on the membrane, the receptor can drive even more phospholipid
  production there, further depleting the cytosolic effector pool.

That loop is a positive feedback: local receptor activity recruits the very molecule that amplifies
local receptor activity. It replaces the fixed production term above with one that depends on the
membrane-bound effector concentration $E_m(x)$ itself:

$$\frac{dm}{dt} = D_m \frac{\partial^2 m}{\partial x^2} - k_{-1} m + P(x), \qquad P(x) = k_0 + k_E
R^*(x) E_m(x)$$

Concretely, in the eukaryotic chemotaxis system this loop maps onto a specific pathway: receptor
binding activates a G-protein, which activates PI3K (the activator, producing the phospholipid
PIP3) and PTEN (the inhibitor, removing it); the steady-state PIP3 level then tracks $R^*$ locally
and is read out by proteins with PH domains that bind it.

## An abstract module: perfect adaptation

Rather than track specific molecules, the lecture strips the mechanism down to a minimal circuit —
an output $R$, a node $A$, and a node $I$ — all driven by one input signal $S$, with $A$ and $I$
each toggling between an inactive and an active (starred) form:

$$\frac{dR^*}{dt} = -k_{-R} I^* R^* + k_R A^* R$$
$$\frac{dA^*}{dt} = -k_{-A} A^* + k_A' S A = -k_{-A} A^* + k_A' S (A_{tot} - A^*)$$
$$\frac{dI^*}{dt} = -k_{-I} I^* + k_I' S I = -k_{-I} I^* + k_I' S (I_{tot} - I^*)$$

$S$ drives $A \to A^*$ and $I \to I^*$; $A^*$ drives $R \to R^*$ and $I^*$ drives $R^* \to R$ back
down, so $A$ excites the output and $I$ inhibits it.

<figure>
<svg viewBox="0 0 420 260" role="img" aria-label="Three linked switches: signal S drives A and I between active and inactive forms, and A, I drive R in opposite directions">
  <defs>
    <marker id="arr1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <rect x="110" y="20" width="60" height="30" fill="none" stroke="currentColor"/>
  <text x="140" y="40" text-anchor="middle" font-size="13" fill="currentColor">R</text>
  <rect x="250" y="20" width="60" height="30" fill="none" stroke="currentColor"/>
  <text x="280" y="40" text-anchor="middle" font-size="13" fill="currentColor">R*</text>
  <line x1="170" y1="30" x2="248" y2="30" stroke="currentColor" marker-end="url(#arr1)"/>
  <text x="210" y="20" text-anchor="middle" font-size="10" fill="currentColor">k_R A*</text>
  <line x1="248" y1="44" x2="170" y2="44" stroke="currentColor" marker-end="url(#arr1)"/>
  <text x="210" y="58" text-anchor="middle" font-size="10" fill="currentColor">k_-R I*</text>

  <rect x="18" y="90" width="55" height="30" fill="none" stroke="currentColor"/>
  <text x="45" y="110" text-anchor="middle" font-size="13" fill="currentColor">A*</text>
  <rect x="18" y="150" width="55" height="30" fill="none" stroke="currentColor"/>
  <text x="45" y="170" text-anchor="middle" font-size="13" fill="currentColor">A</text>
  <line x1="35" y1="148" x2="35" y2="122" stroke="currentColor" marker-end="url(#arr1)"/>
  <text x="8" y="136" text-anchor="middle" font-size="10" fill="currentColor">k_A'S</text>
  <line x1="58" y1="122" x2="58" y2="148" stroke="currentColor" marker-end="url(#arr1)"/>
  <text x="88" y="136" text-anchor="middle" font-size="10" fill="currentColor">k_-A</text>

  <rect x="347" y="90" width="55" height="30" fill="none" stroke="currentColor"/>
  <text x="374" y="110" text-anchor="middle" font-size="13" fill="currentColor">I*</text>
  <rect x="347" y="150" width="55" height="30" fill="none" stroke="currentColor"/>
  <text x="374" y="170" text-anchor="middle" font-size="13" fill="currentColor">I</text>
  <line x1="362" y1="148" x2="362" y2="122" stroke="currentColor" marker-end="url(#arr1)"/>
  <text x="332" y="136" text-anchor="middle" font-size="10" fill="currentColor">k_I'S</text>
  <line x1="385" y1="122" x2="385" y2="148" stroke="currentColor" marker-end="url(#arr1)"/>
  <text x="412" y="136" text-anchor="middle" font-size="10" fill="currentColor">k_-I</text>

  <rect x="168" y="210" width="55" height="28" fill="none" stroke="currentColor"/>
  <text x="195" y="228" text-anchor="middle" font-size="13" fill="currentColor">S</text>
  <line x1="182" y1="210" x2="55" y2="182" stroke="currentColor" stroke-dasharray="3,3" marker-end="url(#arr1)"/>
  <line x1="210" y1="210" x2="368" y2="182" stroke="currentColor" stroke-dasharray="3,3" marker-end="url(#arr1)"/>

  <line x1="73" y1="100" x2="138" y2="50" stroke="currentColor" stroke-dasharray="2,4" marker-end="url(#arr1)"/>
  <line x1="347" y1="100" x2="282" y2="50" stroke="currentColor" stroke-dasharray="2,4" marker-end="url(#arr1)"/>
</svg>
<figcaption>The perfect-adaptation module: S turns A into A* and I into I*; A* pushes R toward R*,
I* pushes R* back toward R. The dashed diagonals show A* and I* feeding the R switch in opposite
directions.</figcaption>
</figure>

$R^*$ itself only ever reacts to the ratio of the other two nodes. Writing $R + R^* = R_{tot}$ for
the fixed total amount of $R$, and setting $dR^*/dt = 0$:

$$k_{-R} I^* R^*_{ss} = k_R A^*_{ss} (R_{tot} - R^*_{ss}) \ \Longrightarrow\ \frac{R^*_{ss}}{R_{tot}}
= \frac{k_R A^*_{ss}/I^*_{ss}}{k_R A^*_{ss}/I^*_{ss} + k_{-R}}$$

a saturating, Michaelis–Menten-shaped function of the single lumped variable $\rho \equiv
A^*_{ss}/I^*_{ss}$. Nothing else about $A^*$ or $I^*$ individually reaches $R^*$ — only their
ratio does.

The **main assumption** is that deactivation is fast relative to activation, $k_{-A}, k_{-I} \gg
k_A', k_I'$, so only a small fraction of each pool is ever active ($A_{tot} \gg A^*$, $I_{tot} \gg
I^*$). Replacing $A \approx A_{tot}$ and $I \approx I_{tot}$ linearizes the equations in $S$:

$$\frac{dA^*}{dt} = -k_{-A} A^* + k_A S, \qquad \frac{dI^*}{dt} = -k_{-I} I^* + k_I S, \qquad k_A' =
k_A A_{tot},\ \ k_I' = k_I I_{tot}$$

with steady states

$$A^*_{ss} = \frac{k_A}{k_{-A}} S, \qquad I^*_{ss} = \frac{k_I}{k_{-I}} S, \qquad R^*_{ss} =
\frac{k_R A^*_{ss}/I^*_{ss}}{k_R A^*_{ss}/I^*_{ss} + k_{-R}}$$

Both $A^*_{ss}$ and $I^*_{ss}$ are proportional to $S$ with the same $S$-dependence, so the ratio
$\rho = A^*_{ss}/I^*_{ss} = (k_A k_{-I})/(k_{-A} k_I)$ is a constant, independent of $S$ — and so is
$R^*_{ss}$. That is **perfect adaptation**: a step in $S$ moves $R^*$ transiently, but the steady
state it settles back to does not depend on the size of the step at all. From here on the lecture
drops the stars — writing $A$, $I$ for what were $A^*$, $I^*$ — since in this linear regime the free
pools barely move and only the active amounts matter.

## Making the adaptation module spatial

Take this module and place it in a one-dimensional cell of length $1$ (position $x \in [0,1]$),
imposing a signal that varies linearly in space,

$$S(x) = s_0 + s_1 x$$

and — the one modelling choice that turns a purely *temporal* adaptation circuit into a *spatial*
gradient sensor — let only $I$ diffuse; $A$ (and the readout node fed by it) stays local. The
lecture makes this explicit by redrawing the same module with $A$ and $R$ marked "fixed in space"
and $I$ marked "diffuses."

Because $A$ does not diffuse, it is a bare rescaling of the local signal:

$$A(x) = \frac{k_A}{k_{-A}}(s_0 + s_1 x)$$

— wherever $x$ is, $A(x)$ tracks $S(x)$ exactly. $I$, in contrast, obeys a reaction–diffusion
equation,

$$\frac{\partial I(x,t)}{\partial t} = -k_{-I} I(x,t) + k_I S(x,t) + D \frac{\partial^2
I(x,t)}{\partial x^2}$$

with no-flux (zero-derivative) boundary conditions at the two ends of the interval:

$$\frac{\partial I(0,t)}{\partial x} = \frac{\partial I(1,t)}{\partial x} = 0$$

At steady state this reduces to a linear, constant-coefficient ODE,

$$\frac{\partial^2 I(x)}{\partial x^2} = \frac{k_{-I}}{D} I(x) - \frac{k_I}{D}(s_0 + s_1 x) \equiv a
I(x) - b - cx$$

which the slide solves symbolically (MATLAB's `dsolve`, with the physical position relabelled to
the solver's default independent variable), giving the closed form

$$I(x) = \frac{k_I}{k_{-I}}\left(s_0 + s_1\left(x - \frac{\sinh \sigma x}{\sigma} +
\frac{\cosh\sigma x}{\sigma}\,\frac{\cosh\sigma - 1}{\sinh\sigma}\right)\right), \qquad \sigma
\equiv \sqrt{\frac{k_{-I}}{D}}$$

the same construction as $\lambda$ earlier, now for the inhibitor: $1/\sigma$ is the length over
which $I$ equilibrates by diffusion before it decays. For the values on the slide ($k_I/k_{-I}=1$,
$s_0 = 1\ \mu\text{M}$, $s_1 = 0.1\ \mu\text{M}$, $\sigma = 0.25\ \mu\text{m}^{-1}$, a diffusion
length of $4\ \mu\text{m}$) this is a specific profile, flatter than $A(x)$ because part of the
imposed gradient has diffused away before $I$ settles.

## Reading the ratio: local excitation, global inhibition

The output only ever sees the ratio $A(x)/I(x)$ — recall $R^*_{ss}$ above depended on
$A^*_{ss}/I^*_{ss}$ alone — and dividing the two profiles gives

$$\frac{A(x)}{I(x)} = \frac{k_A k_{-I}}{k_{-A} k_I}\left(1 + \frac{s_1}{s_0+s_1 x}\left(
\frac{\cosh\sigma x}{\sigma}\,\frac{\cosh\sigma - 1}{\sinh\sigma} - \frac{\sinh\sigma
x}{\sigma}\right)\right)^{-1}$$

The prefactor $k_A k_{-I}/(k_{-A} k_I)$ is exactly the $S$-independent constant found for the
well-mixed adaptation module: set the gradient $s_1$ to zero and the bracket collapses to $1$, and
$A(x)/I(x)$ sits at the flat, perfectly-adapted baseline. Turning the gradient back on
($s_1 \neq 0$) makes the bracket $x$-dependent — the module is no longer exactly at its adapted
value, and the size and sign of that deviation is what carries the gradient information.

The cleanest limit is small $\sigma$: a diffusion length long compared with the cell (the slide
takes $\sigma \sim 0.4$ on a cell of size $1$). Then $I$ has time to average itself over the whole
cell before it decays — it stops tracking the local $x$ and instead settles at the value set by the
**spatial mean** of the signal, $\bar S$:

$$I(x) \to I(\bar S) = \text{const.}, \qquad A(x) = A(S(x)), \qquad R^*(x) \approx
\frac{A(S(x))}{I(\bar S)}$$

That is local excitation, global inhibition, read directly off this construction rather than
assumed from the start: $A$ answers to the signal exactly where it sits; $I$, because it diffuses
fast relative to its own decay, answers to the signal everywhere at once. Comparing the two at each
point is what can turn a signal varying by only $s_1/s_0 = 10\%$ across the cell into a much more
sharply graded output.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="Schematic profiles across the cell: the local activator tracks the signal exactly while the diffusing inhibitor is flattened toward the spatial average">
  <line x1="50" y1="180" x2="310" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="50" y1="180" x2="50" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <text x="180" y="202" text-anchor="middle" font-size="12" fill="currentColor">position across the cell, 0 to 1</text>

  <line x1="60" y1="150" x2="300" y2="100" stroke="currentColor" stroke-width="1.5"/>
  <text x="304" y="98" font-size="11" fill="currentColor">S(x)</text>

  <line x1="60" y1="156" x2="300" y2="106" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="304" y="114" font-size="11" fill="currentColor">A(x)</text>

  <path d="M60,140 Q180,132 300,128" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="304" y="130" font-size="11" fill="currentColor">I(x)</text>

  <line x1="60" y1="134" x2="300" y2="134" stroke="currentColor" stroke-width="1" stroke-dasharray="1,3"/>
  <text x="44" y="137" text-anchor="end" font-size="11" fill="currentColor">S̄</text>
</svg>
<figcaption>Schematic, not a plot of the closed form above: the external signal S(x) rises gently
across the cell; A(x) is a bare rescaling of it, since A does not diffuse. I(x) obeys the same
production law but diffuses, so it is pulled toward the spatial average S̄ instead of following the
local value. Because R* depends only on the ratio A(x)/I(x), the readout sits above the adapted
baseline on the high side of the gradient and below it on the low side.</figcaption>
</figure>

## Back to the motivating question

This module's steady state is a single point for any fixed $S(x)$: nothing here creates two stable
polarized states for the same input, the way a Turing instability in the earlier activator–inhibitor
system can. So the polarized profile of $R^*(x)$ this network produces is not something the cell
gets locked into — it is a readout the network is always relaxing toward, given whatever gradient
is currently present. If the gradient reverses, $A(x)$ reverses instantly (it does not diffuse),
$I$ catches up to the new spatial mean over its own relaxation time, and $R^*(x)$ follows — which is
the property the two cited papers were built to have, against the "how to prevent cells from
polarizing irreversibly" concern that opens the lecture.

## Sources

- Slides: `lectures/20-notes/01-alternative-views-on-gradient-sensing.md` and
  `lectures/20-notes/02-now-introduce-diffusion.md` (MIT OCW 8.591J, *Systems Biology*, Fall 2004,
  lecture 20 notes). Both are model reconstructions of a PDF slide deck with no text layer; the
  source banner on each file flags every equation as unverified, so the algebra above follows the
  slides' own presentation but has not been independently checked against the original PDF or the
  papers it cites.
- No transcript, written notes, or problem set were supplied for this lecture.
- The lecture cites, but this chapter does not otherwise draw on, two papers: Postma, M. and P. J.
  M. Van Haastert, "A diffusion-translocation model for gradient sensing by chemotactic cells,"
  *Biophys. J.* 81(3), 1314–1323 (2001); and Levchenko, A. and P. A. Iglesias, "Models of eukaryotic
  gradient sensing: application to chemotaxis of amoebae and neutrophils," *Biophys. J.* 82(1 Pt
  1), 50–63 (2002). Several figures from those papers are referenced on the slides but were removed
  from the conversion for copyright reasons, and so are not reproduced here either.
- Background assumed: the activator–inhibitor (local-excitation/global-inhibition) reaction–
  diffusion model, its homogeneous steady state, and the Turing instability, from the preceding
  lecture in the same course (`lectures/16-notes/`, `lectures/17-notes.md`) — named here for context
  only, not as a source this chapter draws content from.

---

[← 13. The LEGI Dispersion Relation](13-the-legi-dispersion-relation.md) · [Contents](index.md) · [15. Quorum Sensing and Cell-Cell Communication →](15-quorum-sensing-and-cell-cell-communication.md)
