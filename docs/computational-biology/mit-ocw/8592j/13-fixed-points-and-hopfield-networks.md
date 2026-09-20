---
title: "13. Fixed Points and Hopfield Networks"
course: "MIT 8.592J"
chapter: 13
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 13. Fixed Points and Hopfield Networks

## What this covers

This chapter asks what a network's dynamics can do once each node carries a continuously varying
state and a rate law coupling it to its neighbours. It assumes the reader already has the topology
of a network (nodes and the connections between them) and wants to know what riding a dynamical
system on top of that topology can produce. The chapter develops the fixed point as the basic
long-run outcome, shows when a system's convergence to a fixed point is guaranteed because the
dynamics is descent in a potential, and then works through the one case in the source material
where no such potential exists but a substitute — a Lyapunov function — still forces convergence:
Hopfield's model of a neural network, read as a model of associative memory. The source material
stops mid-sentence at the opening of the following topic (stability, bifurcation and cycles), so
this chapter does too.

## From topology to trajectories

Once a network's connections are fixed, assign each node $i$ a variable $x_i(t)$ whose evolution
depends on the values at the nodes connected to it:

$$\frac{dx_i}{dt} = F_i(\text{values of } x_j \text{ on sites connected to } i) .$$

Restricting to coupled first-order ODEs in time is a real modelling choice, but a good
approximation for many biological systems. A network of chemical reactions, or of interacting
proteins and mRNAs, is described in the mean-field limit by rate equations for concentrations
$C_i(t)$:

$$\frac{dC_i}{dt} = (\text{flux from reactions creating } i) - (\text{flux from reactions destroying } i).$$

For the reaction $\mathrm{A} + \mathrm{B} \rightleftharpoons \mathrm{C}$, with forward rate constant
$k_+$ (consuming A and B) and reverse rate constant $k_-$ (producing them back from C), this reads

$$\frac{d[\mathrm{A}]}{dt} = -k_+[\mathrm{A}][\mathrm{B}] + k_-[\mathrm{C}] .$$

The question the rest of the chapter answers: what long-run behaviours can such a system of
equations settle into? The two candidates named in the source are **stationary fixed points** and
**cycles**; this chapter covers fixed points, and the source breaks off just as it turns to the
question of which fixed points are actually attracting.

## One variable always settles: descent in a potential

With a single variable, convergence to a fixed point is the generic outcome, and there is a clean
reason why. Any one-dimensional equation $\dot x = F(x)$ can be read as descent in a potential:

$$\frac{dx}{dt} = F(x) = -\frac{\partial V}{\partial x}, \qquad V(x) = -\int^x dx'\, F(x') .$$

Given $F$, $V$ is just its antiderivative up to sign, so this is not an extra assumption in one
dimension — it is automatic. The trajectory $x(t)$ rolls downhill on $V$ and settles at a fixed
point, a solution of $F(x^*) = 0$, which is a local minimum of $V$.

Two caveats matter. First, a generic $F$ need not have a zero at all — nothing forces $V$ to have a
minimum on the whole real line. Second, in most biologically relevant cases $x$ is not free to roam
the whole line: a concentration must stay non-negative and below some maximum. Outside that allowed
interval $V$ is effectively infinite, which is exactly what guarantees a minimum exists somewhere
in the interval — possibly at one of its endpoints rather than in the interior.

<figure>
<svg viewBox="0 0 360 200" role="img" aria-label="A double-well potential V(x) with a ball rolling down its slope into the nearest minimum">
  <defs>
    <marker id="arrow1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="20" y1="170" x2="345" y2="170" stroke="currentColor" stroke-width="1"/>
  <path d="M20,20 C50,110 60,150 110,150 C140,150 150,90 180,60 C210,90 220,140 250,140 C280,140 300,110 340,20" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="110" cy="150" r="3.5" fill="currentColor"/>
  <circle cx="250" cy="140" r="3.5" fill="currentColor"/>
  <line x1="110" y1="170" x2="110" y2="174" stroke="currentColor" stroke-width="1"/>
  <line x1="250" y1="170" x2="250" y2="174" stroke="currentColor" stroke-width="1"/>
  <text x="110" y="187" text-anchor="middle" font-size="11" fill="currentColor">x*</text>
  <text x="250" y="187" text-anchor="middle" font-size="11" fill="currentColor">x*</text>
  <circle cx="75" cy="100" r="3" fill="none" stroke="currentColor" stroke-width="1.3"/>
  <path d="M77,104 Q95,132 107,144" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow1)"/>
  <text x="335" y="193" text-anchor="end" font-size="12" fill="currentColor">x</text>
  <text x="26" y="32" text-anchor="start" font-size="12" fill="currentColor">V(x)</text>
</svg>
<figcaption>A one-variable system descends its potential V(x) and settles at the nearest local
minimum, a fixed point x* of ẋ = -∂V/∂x. The steep rise at either edge stands for a physical
bound — a concentration cannot go negative or above some ceiling — that keeps a minimum from
escaping to infinity.</figcaption>
</figure>

The same potential controls the stochastic version of the equation. Add uncorrelated noise
$\eta(t)$, with $\langle \eta(t)\rangle = 0$ and $\langle \eta(t)\eta(t')\rangle = 2D\delta(t-t')$,
to get a Langevin equation. Its steady-state probability density is

$$p^*(x) \propto \exp\!\left[-\frac{V(x)}{D}\right] .$$

So the deterministic fixed points of the noiseless system are exactly the points the noisy system
spends most of its time near: probability concentrates where $V$ is lowest.

## Many variables: the same picture, but only sometimes

The natural generalisation to $N$ coupled variables is gradient descent in a multivariable
potential $V(x_1,\dots,x_N)$:

$$\frac{dx_i}{dt} = -\frac{\partial V(x_1,\dots,x_N)}{\partial x_i} \equiv F_i .$$

Unlike the one-variable case, this is now a genuine restriction on $F_i$, not an automatic
rewriting of it. Because mixed partial derivatives of $V$ commute, any $F_i$ arising this way must
satisfy

$$\frac{\partial F_i}{\partial x_j} = \frac{\partial F_j}{\partial x_i} .$$

For a linear system, $F_i = \sum_j W_{ij} x_j$, this condition forces the coupling matrix to be
symmetric: $W_{ij} = W_{ji}$. That is too strong a constraint for many real networks — a synapse
from neuron $j$ to neuron $i$ has no reason to carry the same strength as the synapse back from $i$
to $j$ — so the gradient-descent picture, and with it the automatic guarantee of convergence to a
fixed point, does not apply to networks with asymmetric interactions in general.

## A network with asymmetric couplings: the Hopfield model

Hopfield's model of a neural network with graded response is the source's example of exactly this
situation. Each neuron's activity (related to its spiking rate) is a variable $x_i$, evolving as

$$\frac{dx_i}{dt} = -\frac{x_i}{\tau} + f\!\left(\sum_j W_{ij} x_j + b_i\right),$$

with $\tau$ (set to $1$ here) the decay time of activity in the absence of input, $b_i$ an external
input (e.g. from sensory cells), and $W_{ij}$ a matrix of synaptic connection strengths from neuron
$j$ to neuron $i$ that need **not** be symmetric: $W_{ij} \neq W_{ji}$ in general. The function $f$
is the neuron's input–output response — monotonically increasing, typically a sigmoid switching
between a low and a high output around a threshold (which can be absorbed into $b_i$). A simplified
version assigns each neuron a discrete value in $\{-1, +1\}$ and updates a randomly chosen neuron
asynchronously by the sign of $\sum_j W_{ij}x_j + b_i$; Hopfield introduced the continuous version
to answer the criticism that the binary model was too far removed from real neurons.[^1]

[^1]: J.J. Hopfield, *Proc. Nat. Acad. Sci.* **81**, 3088 (1984).

Because $W_{ij}$ need not be symmetric,

$$\frac{\partial F_i}{\partial x_j} = -\delta_{ij} + f'\!\left(\sum_k W_{ik}x_k + b_i\right)W_{ij}$$

is in general not equal to the corresponding expression with $i$ and $j$ exchanged, so this system
is *not* gradient descent in any potential. The symmetry argument above no longer guarantees
convergence to a fixed point — and yet it turns out convergence still holds.

## A Lyapunov function stands in for the potential

Even without a potential, a substitute function that is guaranteed non-increasing along every
trajectory does the same job: it forces convergence to a fixed point. Define

$$\mathcal{L}(x_1,\dots,x_N) = \sum_{i=1}^N \big[G(x_i) - b_i x_i\big] - \frac{1}{2}\sum_{i,j} W_{ij}x_i x_j ,$$

where $G$ is chosen so that $G'(x) \equiv f^{-1}(x)$ — the derivative of $G$ is the *inverse* of the
neuron's response function $f$. Differentiating $\mathcal{L}$ along the flow and substituting the
equation of motion gives

$$\frac{d\mathcal{L}}{dt} = \sum_i \left[G'(x_i) - b_i - \sum_j W_{ij}x_j\right]\cdot\left[-x_i + f\!\left(b_i + \sum_j W_{ij}x_j\right)\right] = \sum_i (\alpha_i - \beta_i)\big[f(\beta_i) - f(\alpha_i)\big],$$

with the auxiliary quantities $\alpha_i \equiv f^{-1}(x_i)$ and $\beta_i \equiv b_i + \sum_j
W_{ij}x_j$. The argument that closes this off is short: $f$ is monotonically increasing, so
whenever $\alpha_i > \beta_i$ then $f(\alpha_i) > f(\beta_i)$, making the bracket negative while the
first factor is positive; and symmetrically when $\alpha_i < \beta_i$. Either way each term in the
sum is $\le 0$, so

$$\frac{d\mathcal{L}}{dt} \le 0$$

always, with equality only at a fixed point. This is the same proof template as Boltzmann's
$H$-theorem in statistical mechanics — monotonicity of a single function forcing a sign on a sum of
paired terms — and a parallel argument holds for the discrete binary version of the network.
Activity in the Hopfield network therefore proceeds monotonically toward fixed points, which solve
the self-consistency condition

$$x_i^* = f\!\left(b_i + \sum_j W_{ij}x_j^*\right).$$

## Fixed points as memories

Fixed points of the Hopfield network can be read as associative, or content-addressable, memories.
To imprint a pattern $\{x_i^*\}$, train the couplings by the Hebbian rule

$$\Delta W_{ij} = \eta\, x_i^* x_j^* ,$$

summarised as "neurons that fire together wire together." This changes the Lyapunov function to
$\mathcal{L} + \Delta\mathcal{L}$, and evaluated at the very pattern that was imprinted,

$$\Delta\mathcal{L}(\{x_i^*\}) = -\frac{1}{2}\sum_{i,j}\Delta W_{ij}\, x_i^* x_j^* = -\frac{\eta}{2}\sum_{i,j}(x_i^* x_j^*)^2 < 0 ,$$

so training strictly deepens the minimum at that pattern. If the network is then started from a
partial or corrupted version of a stored memory, the $d\mathcal{L}/dt \le 0$ dynamics carries it
downhill within whichever basin it started in — and if that basin belongs to the intended memory,
the network reconstructs it exactly. Many memories can be stored this way, each with its own basin
of attraction, though the source flags without quantifying that at some point stored patterns
start to interfere and the network's storage capacity is limited by its number of nodes.

<figure>
<svg viewBox="0 0 380 200" role="img" aria-label="A landscape with three wells, each a stored memory, with a corrupted pattern rolling into the nearest one">
  <defs>
    <marker id="arrow2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="15" y1="175" x2="365" y2="175" stroke="currentColor" stroke-width="1"/>
  <path d="M15,110 C40,150 55,160 70,160 C90,160 110,120 135,80 C160,120 180,155 200,160 C220,160 245,120 265,75 C290,120 310,155 330,160 C345,160 355,140 365,110" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="70" cy="160" r="3.5" fill="currentColor"/>
  <circle cx="200" cy="160" r="3.5" fill="currentColor"/>
  <circle cx="330" cy="160" r="3.5" fill="currentColor"/>
  <text x="70" y="180" text-anchor="middle" font-size="11" fill="currentColor">memory 1</text>
  <text x="200" y="180" text-anchor="middle" font-size="11" fill="currentColor">memory 2</text>
  <text x="330" y="180" text-anchor="middle" font-size="11" fill="currentColor">memory 3</text>
  <circle cx="170" cy="120" r="3" fill="none" stroke="currentColor" stroke-width="1.3"/>
  <text x="170" y="106" text-anchor="middle" font-size="11" fill="currentColor">corrupted input</text>
  <path d="M172,124 Q186,144 198,155" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow2)"/>
</svg>
<figcaption>Each stored pattern sits at a minimum of the Lyapunov function L. A partial or corrupted
version of a memory, used as the network's initial state, is carried downhill by the
dL/dt ≤ 0 dynamics into whichever basin it starts in — retrieving the nearest complete memory.</figcaption>
</figure>

## Where the source material stops

The slides open a new subsection, 4.4.2, on stability, bifurcation and cycles, with the general
setup: a bounded set of variables $\{x_i\}$ evolving as $\dot x_i = F_i(\{x_j\})$, whose fixed
points solve $F_i(\{x_j^*\}) = 0$ — but a fixed point is only a *candidate* attractor. The material
supplied breaks off at exactly that sentence, before saying what distinguishes an attracting fixed
point from one that repels trajectories or one that a bifurcation removes. No transcript was
supplied for this lecture to fill that gap, so this chapter stops here too, rather than
reconstructing the argument for stability or the treatment of cycles from nothing.

## Sources

- Slides: `01-introduction.md` (§4.4 Dynamics on Networks) — the network rate-equation setup and
  the chemical-kinetics example.
- Slides: `02-4-4-1-attractive-fixed-points.md` (§4.4.1 Attractive fixed points, and the opening
  sentence of §4.4.2 Stability, Bifurcation, and Cycles) — the one-variable potential argument, the
  symmetry condition for multivariable gradient descent, the Hopfield model, its Lyapunov function,
  and the associative-memory reading, ending mid-sentence at the start of §4.4.2.
- No transcript, written notes or exercises were supplied for this lecture.
- Both slide files are model reconstructions of a PDF with no extractable text layer (course
  ocw-8592j, MIT OCW 8.592J *Statistical Physics in Biology*, Spring 2011, CC BY-NC-SA 4.0); the
  conversion itself flags every equation as unverified against the original PDF, so anyone treating
  a specific coefficient or sign as load-bearing should check it against the original slide.
- The lecture cites, but this chapter does not reproduce beyond the citation: J.J. Hopfield, *Proc.
  Nat. Acad. Sci.* **81**, 3088 (1984).

---

[← 12. Molecular Motors as Brownian Ratchets](12-molecular-motors-as-brownian-ratchets.md) · [Contents](index.md) · [14. Synchronization and Turing Patterns →](14-synchronization-and-turing-patterns.md)
