---
title: "7. Perfect Adaptation by Model Reduction"
course: "MIT 8.591J 2004"
chapter: 7
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 7. Perfect Adaptation by Model Reduction

## What this covers

Lectures 7–8 built the *E. coli* chemotaxis network out of its parts — the Tar receptor complex, its
phosphorylation and methylation states, and the pathway down to the flagellar motor — and then ran
into a puzzle: the resulting model does not reproduce *perfect adaptation*, the experimental fact that
after a step change in attractant concentration the internal signal eventually returns to exactly its
pre-stimulus value, whatever the size of the step. This chapter follows the sequence of four
reductions used to find out why, each one adding a single assumption backed — or explicitly not backed
— by an experiment, until what is left over adapts perfectly by construction rather than by luck. It
closes with the lecture's pivot to the next topic, biological oscillators, via a refresher on fixed
points and linear stability built around the autocatalysis example from Problem Set 1. It assumes the
biological cast introduced in L7 (Tar, CheA/CheW, CheB, CheR, CheY, CheZ) and the combinatorial
receptor-state model built in L8.

## The question inherited from L7–L8

L7 asked what each molecule in the pathway actually does. L8 assembled a model of *all* the reactions
available to the receptor — every combination of ligand-bound or not, phosphorylated or not, and
methylated to varying degrees — and found that it did not reproduce the observed perfect adaptation.
The project spanning L8 and this lecture is to strip that full model down to its essential reactions,
one assumption at a time, and see where the discrepancy actually comes from. The lecture is explicit
that the assumptions along the way are "experimentally justified (or sometimes not)" — worth keeping
in mind, because not every step in the reduction rests on the same strength of evidence, and the
chapter flags which is which as it goes.

The lecture re-shows the basic behavioural picture as a reminder of what perfect adaptation is a
property of: without an attractant, runs are interrupted by tumbles at random; with an attractant
gradient, the cell compares the concentration now to a few seconds ago (temporal sensing) and
suppresses tumbling while things are improving. A second recurring figure (Spiro, Parkinson & Othmer
1997, fig. 2) attaches timescales to the underlying chemistry: ligand binding and unbinding is fast,
phosphorylation ($Y\rightleftharpoons Y_p$ for CheY, $B \rightleftharpoons B_p$ for CheB) is
intermediate, and methylation is slow. That separation of timescales is what licenses folding ligand
binding into an effective, $L$-dependent rate constant everywhere below: by the time phosphorylation or
methylation matters, ligand binding has already equilibrated. The key player throughout, per Spiro et
al.'s model, is the Tar–CheA–CheW receptor–kinase complex.

## A two-state model, and the safe-zone problem

The starting point for this lecture — already the *first* of the four reductions — keeps only the two
highest methylation levels of the receptor, written $2$ and $3$, each of which can be phosphorylated or
not. Two processes act on a receptor: phosphorylation and dephosphorylation ($k_{\text{eff}1}(L)$ and
$k_{\text{eff}2}(L)$ going up, a constant phosphotransfer rate $k_{\text{pt}}$ coming down), and
methylation and demethylation ($k_{\text{eff}4}(L)$ toward higher methylation, $k_{\text{eff}3}(L)$
back). Every rate that carries an $(L)$ is an *effective* rate: because ligand binding has already
equilibrated, $k_{\text{eff}}(L)$ is really a bare rate averaged over how often the receptor happens to
be occupied at concentration $L$. Only $k_{\text{pt}}$, which by assumption does not care about
occupancy, stays a bare constant.

At whatever steady state the (comparatively fast) methylation reactions settle into, define the
fraction of receptors sitting at the higher methylation level:

$$\alpha \equiv \frac{[3]}{[2]+[3]}$$

The net phosphorylation rate seen by the rest of the pathway is the population average of the two
methylation states' own rates:

$$k_{\text{phos}} = (1-\alpha)\, k_{\text{eff}1}(L) + \alpha\, k_{\text{eff}2}(L)$$

Perfect adaptation means this net rate returns to its pre-stimulus value once the system has
re-settled at the new $L$ — that is, $k_{\text{phos}}$, evaluated with whatever $\alpha(L)$ the new
ligand concentration produces, is *flat* as a function of $L$. That is a question about the shapes of
$k_{\text{eff}1}(L)$ and $k_{\text{eff}2}(L)$, and it is not automatic.

<figure>
<svg viewBox="0 0 400 240" role="img" aria-label="Net phosphorylation rate against ligand concentration, with a band where the two methylation states trade off to keep the rate flat">
  <line x1="45" y1="205" x2="380" y2="205" stroke="currentColor" stroke-width="1.5"/>
  <line x1="45" y1="205" x2="45" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="212" y="228" text-anchor="middle" font-size="12" fill="currentColor">ligand concentration, K_B L</text>
  <text x="16" y="115" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 16 115)">net phosphorylation rate</text>
  <rect x="168" y="20" width="64" height="185" fill="currentColor" fill-opacity="0.15"/>
  <text x="200" y="35" text-anchor="middle" font-size="12" fill="currentColor">safe zone</text>
  <path d="M 55 55 C 110 58, 150 70, 175 100 C 200 130, 230 155, 280 165 C 320 172, 350 174, 370 175" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <text x="58" y="48" font-size="11" fill="currentColor">k_eff1 / k8</text>
  <path d="M 55 178 C 110 172, 150 155, 175 122 C 200 90, 230 62, 280 50 C 320 42, 350 40, 370 39" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <text x="300" y="34" font-size="11" fill="currentColor">k_eff2 / k8</text>
  <text x="95" y="198" font-size="11" fill="currentColor">adapts (small L)</text>
  <text x="255" y="198" font-size="11" fill="currentColor">adapts (large L)</text>
</svg>
<figcaption>Each curve is one methylation state's ligand-dependent phosphorylation rate. Where the
"safe zone" exists, the population trades off between the two states as $L$ changes and the weighted
average $k_{\text{phos}}$ stays flat — but this depends on the specific shapes of the two curves. For
another choice of the same two curves there is no such band anywhere, and the model never adapts
perfectly at all. Redrawn schematically from the lecture's plot.</figcaption>
</figure>

The lecture's own instruction for the working case is to "fine-tune... $k_{\text{eff}1}$ and
$k_{\text{eff}2}$ so that $\alpha$ falls in [the] safe zone" — which is exactly the fragility the rest
of the reduction sequence is trying to engineer away. A model that adapts only because its rate
constants happen to sit in the right range is not a satisfying account of a phenomenon the experiments
show is robust.

## Second reduction: CheB only demethylates active receptors

Additional assumption: CheB removes methyl groups only from *phosphorylated* receptors, never from
unphosphorylated ones. This is the weakest-supported step in the sequence — the lecture says plainly
that it is "not possible to directly measure" whether CheB really is restricted to active receptors.
The indirect evidence offered instead is that the rate of methylation drops immediately after ligand is
added, which is what would happen if the demethylating enzyme's substrate is the population that ligand
binding is suppressing. Structurally, the effect is to delete the demethylation arrow from the
unphosphorylated chain: unphosphorylated receptors can now only move *up* in methylation level, never
down.

## Third reduction: methylation at saturation

Additional assumption: $[\text{CheR}] \ll [\text{receptors}]$, so the methylating enzyme CheR is
working at saturation and its rate no longer depends on receptor concentration at all — call this
constant influx $r_{\text{in}}$. Unlike the last step, this one has a direct check: the Michaelis
constant for CheR binding its receptor is much smaller than the receptor concentration, so essentially
all of CheR is receptor-bound and $R_{\text{tot}} \sim R_{\text{bnd}}$. The lecture marks this "ok".
Structurally, the two separately-tracked methylation-level-2 states disappear from the model, replaced
by a constant flux $r_{\text{in}}$ feeding directly into methylation level 3.

## Fourth reduction: an exactly adapting module

Additional assumption: the demethylation rate itself does not depend on ligand occupancy or on
methylation level — $k_{\text{eff}4}$ becomes a genuine constant instead of a function of $L$. This is
also checked directly: demethylation kinetics turn out to be "almost independent of level of
methylation and ligand binding," and the lecture again marks it "ok". What survives all four steps is a
minimal two-state module.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="The surviving two-state module: active and inactive receptor linked by ligand-gated activation and constant deactivation, with a constant input into both and a constant leak out of the active state">
  <defs>
    <marker id="arrowhead" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="190" cy="55" r="28" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="190" y="60" text-anchor="middle" font-size="13" fill="currentColor">C*</text>
  <circle cx="190" cy="175" r="28" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="190" y="180" text-anchor="middle" font-size="13" fill="currentColor">C</text>

  <line x1="170" y1="147" x2="170" y2="85" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <text x="60" y="118" font-size="11" fill="currentColor">k_eff2(L)</text>

  <line x1="210" y1="85" x2="210" y2="147" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <text x="216" y="118" font-size="11" fill="currentColor">k_pt</text>

  <line x1="70" y1="55" x2="160" y2="55" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <text x="72" y="45" font-size="11" fill="currentColor">r_in</text>

  <line x1="70" y1="175" x2="160" y2="175" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <text x="72" y="165" font-size="11" fill="currentColor">r_in</text>

  <line x1="214" y1="41" x2="300" y2="10" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <text x="248" y="18" font-size="11" fill="currentColor">k_eff4</text>
</svg>
<figcaption>The module left after all four reductions. $C^*$ is the phosphorylated, high-methylation
receptor that feeds phosphate onward toward CheY; $C$ is its unphosphorylated counterpart. Both receive
the same constant input $r_{\text{in}}$; only $C^*$ leaks out, at the constant rate $k_{\text{eff}4}$.
The ligand-gated step $k_{\text{eff}2}(L)$ only moves receptor between $C$ and $C^*$ — it never appears
in their combined steady-state balance.</figcaption>
</figure>

Writing $C^*$ for the phosphorylated, high-methylation receptor and $C$ for its unphosphorylated
counterpart, the module's dynamics are linear:

$$\dot C^* = -(k_{\text{pt}}+k_{\text{eff}4})\,C^* + k_{\text{eff}2}(L)\,C + r_{\text{in}}$$
$$\dot C = k_{\text{pt}}\,C^* - k_{\text{eff}2}(L)\,C + r_{\text{in}}$$

Add the two equations. The $k_{\text{eff}2}(L)$ terms cancel exactly, and so do the $k_{\text{pt}}$
terms, leaving

$$\dot C^* + \dot C = -k_{\text{eff}4}\,C^* + 2r_{\text{in}}$$

At steady state this gives

$$[3_{\text{p}}] = C^* = \frac{2 r_{\text{in}}}{k_{\text{eff}4}}$$

— a result with no $L$ in it anywhere. Because $r_{\text{in}}$ was made $L$-independent by the third
reduction and $k_{\text{eff}4}$ was made $L$-independent by the fourth, the steady-state level of the
active receptor *cannot* depend on $L$, whatever the ligand-gated activation rate $k_{\text{eff}2}(L)$
is doing on its own. This is perfect adaptation for *any* value of $L$, not merely inside a fine-tuned
safe zone: the fragility from the first reduction is gone because the two rates that could have carried
$L$-dependence into the steady state have each, on separate experimental grounds, been argued to carry
none.

## From switches to oscillators

Having closed the chemotaxis question, the lecture turns to what comes next: biological oscillators,
motivated by the cell-division cycle and circadian rhythms. The question posed is deliberately informal
— what do you need to build an oscillator, and how is that different from the systems already met,
switches and the chemotactic network just finished? The answer flagged is not a result but a technique:
a graphical way of representing differential equations, to be developed in the next lecture under the
name of nullclines. What follows here is a refresher on the pieces that technique will need.

## Refresher: fixed points and linear stability

The running example, revisited from Problem Set 1, is autocatalysis:

$$A + X \underset{k_{-1}}{\overset{k_{+1}}{\rightleftharpoons}} 2X$$

With $x = [X]$ and $a = [A]$ held constant (an enormous surplus of $A$), the rate equation is a single
first-order ODE of the form $\dot x = f(x)$:

$$\dot x = k_1 a x - k_{-1}x^2$$

The lecture's recipe for any such equation is two steps: find the fixed points, then check their
stability.

**Fixed points.** Setting $f(x^*)=0$ and factoring, $f(x) = x(k_1 a - k_{-1}x)$, gives two roots:

$$x_1^* = 0 \qquad\qquad x_2^* = \frac{k_1 a}{k_{-1}}$$

**Stability.** Perturb slightly away from a fixed point, $\eta(t) = x(t) - x^*$, and Taylor-expand:

$$f(x^*+\eta) = f(x^*) + \eta f'(x^*) + O(\eta^2) \approx \eta f'(x^*)$$

Since $f(x^*)=0$, this leaves $\dot\eta \approx \eta f'(x^*)$, a linear equation with exponential
solution $\eta(t) \sim \exp(f'(x^*)\,t)$. So the sign of $f'(x^*)$ decides everything: the perturbation
grows if $f'(x^*)>0$ (unstable fixed point) and decays if $f'(x^*)<0$ (stable fixed point). For $f(x) =
k_1ax - k_{-1}x^2$, $f'(x) = k_1a - 2k_{-1}x$, so $f'(x_1^*) = k_1a > 0$ (unstable) and $f'(x_2^*) =
k_1a - 2k_1a = -k_1a < 0$ (stable): one unstable fixed point at the origin, one stable fixed point at
$x_2^*$.

<figure>
<svg viewBox="0 0 340 150" role="img" aria-label="Phase line for the autocatalysis equation, showing flow away from the unstable fixed point at zero and toward the stable fixed point">
  <text x="170" y="18" text-anchor="middle" font-size="12" fill="currentColor">f(x) = k1 a x - k-1 x^2</text>
  <line x1="30" y1="90" x2="310" y2="90" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="70" cy="90" r="5" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="230" cy="90" r="5" fill="currentColor"/>
  <line x1="82" y1="90" x2="205" y2="90" stroke="currentColor" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="300" y1="90" x2="242" y2="90" stroke="currentColor" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="70" y="112" text-anchor="middle" font-size="11" fill="currentColor">0 (unstable)</text>
  <text x="230" y="112" text-anchor="middle" font-size="11" fill="currentColor">x* = k1 a / k-1 (stable)</text>
</svg>
<figcaption>Flow along the phase line: any perturbation away from $x^*_1=0$ grows, and every trajectory
on either side of $x_2^*$ is carried back toward it — matching the lecture's "guestimate of dynamics"
sketch of $[X]$ against time for different starting conditions.</figcaption>
</figure>

## Setting up a two-variable system

The lecture's last move is to point out that the fourth-reduction module is itself already an example
of the next technique, just written in biological variables. Relabelling $x \equiv C^*$, $y\equiv C$,
the two equations above become a generic linear system in two variables:

$$\dot x = ax + by + r_{\text{in}} \qquad\qquad \dot y = cx + dy + r_{\text{in}}$$

with $a \equiv -(k_{\text{pt}}+k_{\text{eff}4})$, $b\equiv k_{\text{eff}2}$, $c \equiv k_{\text{pt}}$, and
$d \equiv -b$. Nothing new is being modelled here — it is the same chemotaxis module reused as the
worked example for the graphical, two-variable machinery (nullclines) that the next lecture builds.

## Sources

- Slides: *Wrapping up E. coli Chemotaxis (L7 & L8)*,
  `lectures/09-notes/01-wrapping-up-e-coli-chemotaxis-l7-l8.md` — the L7/L8 recap, the timescale figure
  (Spiro, Parkinson & Othmer 1997, fig. 2), the four-state box of the first reduction and its
  safe-zone plots, and the second and third reductions.
- Slides: *Fourth reduction*, `lectures/09-notes/02-fourth-reduction.md` — the fourth reduction and its
  exact steady state, the pivot to oscillators, the Problem Set 1 autocatalysis refresher, and the
  two-variable rewrite of the reduced module.
- No transcript, written notes, or exercise sheet was supplied for this lecture, so nothing from a
  spoken account or a problem set appears here beyond what the slides themselves state. "Problem Set 1"
  is named on the slide as the source of the autocatalysis example, but its actual questions were not
  supplied and are not reproduced; the next lecture's nullcline technique, referenced at the end, is
  likewise named but not covered here.
- Both source files are machine reconstructions of a PDF deck with no text layer (their own front
  matter reads "fidelity: reconstructed... every equation is unverified"); the reaction diagrams in
  particular have been read here for their qualitative structure — which reactions are present or
  absent at each step — rather than trusted digit-for-digit.
- Figures cited on the slides but not reproduced in the source markdown: Spiro, Parkinson & Othmer,
  "A model of excitation and adaptation in bacterial chemotaxis," *PNAS* 94 (1997): 7263–8; Mittal,
  Budrene, Brenner & Van Oudenaarden, "Motility of *Escherichia coli* cells in clusters formed by
  chemotactic aggregation," *PNAS* 100 (2003): 13259–63.

---

[← 6. Excitation and Adaptation in Chemotaxis](06-excitation-and-adaptation-in-chemotaxis.md) · [Contents](index.md) · [8. Biological Oscillators →](08-biological-oscillators.md)
