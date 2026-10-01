---
title: "14. Toggle Switches and Stability Analysis"
course: "MIT 8.591J 2014"
chapter: 14
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 14. Toggle Switches and Stability Analysis

## What this covers

This chapter reconstructs a lecture from MIT's *Systems Biology* course (8.591J, Fall 2014) built
around one running example, the genetic toggle switch. It answers two questions the lecture treats
as one skill: how a pair of mutually repressing genes can hold two stable states and act as a
memory, and how to read a model's hidden assumptions and its connection to real, measurable
quantities directly off a dimensionless equation, without having seen the derivation. It closes
with the machinery the rest of the course leans on repeatedly: how to decide, from a fixed point of
a system of ODEs, whether nearby trajectories run toward it or away from it. It assumes familiarity
with ordinary differential equations, Hill-function repression, and the definition of an eigenvalue,
but not with nondimensionalization or linear stability analysis, which are built up from scratch.

Only the spoken lecture is available here — whatever the professor drew on the board (the circuit
diagrams, the four polling diagrams, the trace-determinant sketch, the phase portraits) is not in
the source and is described in words rather than reconstructed as a picture, except where the
underlying algebra is enough to draw the diagram honestly.

## The toggle switch as a bistable memory module

### A Boolean cartoon of bistability

Take two genes, $A$ and $B$, whose protein products each repress the other's expression — "$A$
represses $B$, $B$ represses $A$." Written this abstractly, the two players don't have to be genes
at all; they could be any pair of things that suppress each other, chemical species or competing
populations.

To see why such a pair should have *two* stable states rather than one, the lecture first strips
the model down to a Boolean cartoon: each of $A$ and $B$ is either "low" (0) or "high" (1), and the
rule is that being repressed pushes you toward 0, while being unrepressed lets you drift up to 1.
Check each of the four combinations for self-consistency:

- $(0,0)$: neither gene is repressed, so both should drift up. Not a resting state.
- $(1,1)$: both genes are repressing each other, so both should fall. Not a resting state.
- $(1,0)$ and $(0,1)$: the high one keeps the low one suppressed, and the low one isn't repressing
  the high one, so nothing changes. These are the resting states.

<figure>
<svg viewBox="0 0 320 260" role="img" aria-label="Boolean state diagram of the toggle switch showing the two mixed states are stable and the two matched states are not">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="60" y1="200" x2="260" y2="200" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="200" x2="60" y2="40" stroke="currentColor" stroke-width="1"/>
  <text x="260" y="218" font-size="12" fill="currentColor" text-anchor="end">u (A high)</text>
  <text x="45" y="45" font-size="12" fill="currentColor" text-anchor="end">v (B high)</text>

  <circle cx="60" cy="200" r="6" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="60" y="222" font-size="12" text-anchor="middle" fill="currentColor">0,0</text>

  <circle cx="260" cy="40" r="6" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="260" y="30" font-size="12" text-anchor="middle" fill="currentColor">1,1</text>

  <circle cx="260" cy="200" r="6" fill="currentColor"/>
  <text x="260" y="222" font-size="12" text-anchor="middle" fill="currentColor">1,0</text>

  <circle cx="60" cy="40" r="6" fill="currentColor"/>
  <text x="60" y="30" font-size="12" text-anchor="middle" fill="currentColor">0,1</text>

  <line x1="75" y1="196" x2="235" y2="196" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="66" y1="185" x2="66" y2="55" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>

  <line x1="245" y1="55" x2="245" y2="185" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="235" y1="44" x2="75" y2="44" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
</svg>
<figcaption>Open circles are the self-undermining states (0,0) and (1,1): both drift away, toward
one of the two mixed states. Filled circles are the two mixed states, where the repressor in
charge keeps the other one down — these are where the switch rests.</figcaption>
</figure>

This Boolean picture doesn't prove anything about the real, continuous system — it's a cartoon for
building intuition, not an argument — but it is exactly the reasoning the lecture reuses on
Thursday to motivate why a loop of three repressors ($A \dashv B \dashv C \dashv A$, the
repressilator) can oscillate instead of settling down.

### Wiring a real circuit: a shared transcript, independent translation

Concretely, one gene ($A$) sits on a piece of DNA and represses expression of a second gene ($B$);
$B$ comes back and represses $A$. In the version discussed in class, $B$ is co-transcribed with a
green fluorescent protein (GFP) reporter from a single promoter: one RNA polymerase makes one long
transcript covering both $B$ and GFP, and two separate, independently-loading ribosome sites
translate it into the two separate proteins. This is a bacterial trick — eukaryotic transcripts
typically don't support multiple independent ribosome-loading sites on one mRNA — and it is the
reason GFP is a usable proxy for $B$: the two are made from the same transcript, so GFP level
tracks $B$ level, even though the two proteins are translated independently and needn't be
produced in equal numbers. (As a tangent, the lecture points to a recent conference talk, by an
incoming faculty member, on the $F_OF_1$ ATP synthase: because that motor has many different
subunits encoded on one long polycistronic transcript, translation rates at the different
ribosome-loading sites can differ enough to produce the correct final stoichiometry — for instance
twelve copies of one subunit for every one of another — straight from one transcript. The point
carried over to the toggle switch is only that co-transcription does not force co-translation.)

To reset such a switch — to use it as a memory rather than a fixed outcome — you need a way to
relieve one repressor's grip without touching the DNA. In the design discussed, one repressor is
lac I, relieved by the small molecule IPTG; the other repressor is relieved by a second small
molecule (heard in the lecture as "ATCN," almost certainly the compound paired with lac I in
designs of this kind); in yet another realization the same role is played by heat, because the
repressor there is a temperature-sensitive mutant that simply stops binding DNA above some
threshold. The lecture's mnemonic for all of these: "minus, minus is equal to plus" — inhibiting a
repressor is equivalent to activating whatever it represses.

### Flipping the switch, and why it stays flipped

Suppose the circuit is sitting in the state with high GFP — high $B$ (here, lac I) and low $A$. To
flip it to low GFP, you have to relieve $B$'s repression of $A$, i.e., add IPTG. Two very different
timescales are at work in what happens next, and separating them is the point of the example:

- IPTG crosses the cell membrane and binds lac I in **seconds**. Binding is fast, so lac I is
  inactivated almost immediately — but the lac I *protein* is still there; it has not gone away,
  only stopped working.
- Only after lac I is inactivated can $A$ start to accumulate, and only after $A$ has accumulated
  enough does it start repressing $B$ and GFP. Both of those steps run on the timescale of protein
  turnover and cell growth — in the example, division roughly every half hour — so the visible
  change, GFP actually falling, takes **hours**, not seconds.

This is the separation of timescales: the molecular event (IPTG binding lac I) is fast, but the
consequence for protein levels is slow, because it has to wait on synthesis and dilution.

The circuit earns the name "memory module" because, once flipped, the state persists even after
the input is removed: IPTG can be taken away again, and the switch stays in the new state. A
transient input produces a permanent (until deliberately reset) change of state — exactly the
property a memory needs, and the reason the two mixed Boolean states from the cartoon above matter:
each is a basin the system falls into and stays in.

### Why the result mattered

The lecture's other point about this circuit is not mathematical: the repressors and promoters that
were wired together to build it had, in at least one case, never been combined with each other
before. The gene network was assembled because a model predicted it should work — predicted, in
particular, that if the two repressors multimerize enough to repress cooperatively, the circuit
would be bistable. That predictive step is presented as the real contribution: modeling cannot make
the wet-lab construction painless, but it can tell you which of the many things that could be tried
are worth trying, before you spend months discovering that a component doesn't behave the way you
assumed.

## Nondimensionalizing the toggle-switch equations

### The equations, and what writing them down already assumes

The lecture works from the pair of dimensionless equations produced by nondimensionalizing the real
toggle-switch model (the derivation itself was the pre-class reading, not repeated here):

$$\dot u = \frac{\alpha_1}{1+v^{\beta}} - u, \qquad \dot v = \frac{\alpha_2}{1+u^{\gamma}} - v$$

Here $u$ tracks the (rescaled) level of one repressor and $v$ the other; $\alpha_1,\alpha_2$ are
maximal (dimensionless) production rates; $\beta,\gamma$ are cooperativity exponents (Hill
coefficients) — larger than 1 captures the fact that repression here comes from a multimerized
repressor, which is exactly the cooperativity the circuit was designed around. The two terms in
each equation are a production term (first) and an effective decay term (second): "the more $v$ you
have, the less production of $u$, and vice versa" is the whole mechanism of mutual repression,
carried by the $1/(1+v^\beta)$ factor.

Four parameters completely specify this dynamical system — deliberately fewer than the real
circuit has knobs, for two independent reasons: this is already a simplified model of a complex
system, and even that simple model has been compressed further by nondimensionalizing it. The
lecture's central warning is that both compressions hide real content, and you're expected to
recover that content by staring at the equations themselves, not by rereading the derivation:

- **The two decay terms, $-u$ and $-v$, both have coefficient exactly 1.** Turn off production
  (set $\dot u = -u$) and both $u$ and $v$ decay exponentially at the *same* rate in whatever units
  time is measured in here. That is only true because the nondimensionalization divided time by a
  single degradation rate, shared between the two equations — which is only legitimate if the real
  effective lifetimes of the two proteins (lifetime meaning the combination of true degradation and
  dilution by cell growth) are actually equal. If you wanted a toggle switch out of two proteins with
  different stabilities, these equations would not describe it; you would need to add an extra
  parameter (a $\delta$ multiplying one of the two decay terms) to capture the mismatch.
- **$\beta$ and $\gamma$ are allowed to differ.** The two repressors can have different effective
  cooperativities. That wasn't forced — the equations could just as well have used $\beta$ in both
  places, which would have silently assumed the two repression cooperativities were equal. Whether
  an equation like this shares a parameter between two roles or gives them separate letters is
  itself a modeling choice, and reading it off correctly is part of understanding the model.

### What $u=1$ means

Nondimensionalizing also erases the units, and the lecture insists that a dimensionless variable
still has to correspond to *something* recognizable in the lab. Concretely: the real concentration
of $u$ was divided by $K$, the concentration of $u$ that produces half of the maximum possible
repression of $v$'s promoter — so $u=1$ means "at the point of half-maximal repression," not any
particular number of molecules. Because the two repressors can have different binding constants for
their respective promoters, $u=1$ and $v=1$ need not correspond to the same absolute protein count
— they're only guaranteed to mean the same *thing*, namely each protein's own half-repression
threshold.

There is also a purely formal check available, with no biology at all: in $\alpha/(1+v^\beta)$, the
"$1$" is being added to $v^\beta$. Added quantities must share units — you can never add a
concentration to a pure number — so the mere fact that $1$ appears added to $v^\beta$ already tells
you $v$ must be dimensionless. Nothing about the rescaling shows up explicitly in the equation, but
the presence of that added constant proves it happened.

## Reading experimental changes back out of the model

Because the four parameters absorb so much, a natural and recurring exercise is: if you make one
specific change at the bench, which of $\alpha_1,\alpha_2,\beta,\gamma$ actually moves? The lecture
works through raising the degradation rate of both transcription factors:

- $\beta$ and $\gamma$ **do not change.** They encode the cooperativity of repression — a property
  of how the repressor binds its promoter — and that molecular fact doesn't care how fast the
  protein is degraded.
- $\alpha_1$ and $\alpha_2$ **go down.** The clean way to see this: raising the degradation rate
  shrinks the real, steady-state concentration of the repressor. A lower real concentration is a
  less effective repressor at any fixed threshold $K$, and that drop in effectiveness is exactly
  what a smaller dimensionless $\alpha$ represents. (An equally valid way to see it, offered in
  class: raising the degradation rate shrinks the unit of dimensionless time itself, since that
  unit *is* the effective lifetime; in a shorter unit of time, a fixed real production rate simply
  produces less protein per unit of dimensionless time.)

The general lesson the lecture wants drawn from this: essentially every piece of biology that isn't
the pure cooperativity exponent — promoter strength, the repression threshold $K$, the protein's
effective lifetime — has been rolled into the single parameter $\alpha$. That's the appeal of the
dimensionless form: once you understand how these four parameters govern the equations, you
understand everything the model can do, because there's no separate knob left to turn into some
untested regime. The cost is that the mapping from "what I changed in the lab" to "which parameter
moved, and in which direction" is no longer visible in the equations — it has to be rederived, as
just done, every time.

## Stability of fixed points

### One dimension

For $\dot x = ax$, the fixed point $x=0$ is stable if and only if $a<0$: nudge $x$ positive, and
you need $\dot x<0$ to pull it back; nudge it negative, and you need $\dot x>0$. In one dimension,
$a$ is the (only) eigenvalue of the system, and the general rule the lecture then states for any
number of dimensions is the direct generalization: **a fixed point is stable iff every eigenvalue
has negative real part.**

It's worth contrasting this with a *discrete* map, $x_{t+1} = a x_t$, where the stability condition
is $|a|<1$ rather than $a<0$ — the boundary sits at $1$, not $0$, because a negative $a$ with
magnitude less than 1 still shrinks $x$ toward zero, just while flipping its sign at each step
("hopping") rather than decaying monotonically. Confusing the two conditions is a natural mistake,
which is presumably why the lecture pauses on it before generalizing.

### $n$ dimensions and linearization

For a linear system $\dot{\mathbf x} = A\mathbf x$, the origin is stable iff every eigenvalue
$\lambda_i$ of $A$ has $\mathrm{Re}(\lambda_i) < 0$. The systems that come up in this course are
mostly *nonlinear*; the standard move, used repeatedly for the rest of the semester, is to locate a
fixed point of the nonlinear system and linearize around it (replace the dynamics near that point
by its Jacobian), reducing the local stability question to exactly this linear eigenvalue test.

### Two dimensions: the trace–determinant test

Write the 2D linear system as

$$\dot x = ax+by, \qquad \dot y = cx+dy, \qquad A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$$

with $\mathrm{tr}(A)=a+d$ and $\det(A)=ad-bc$. The origin is stable iff

$$\mathrm{tr}(A) < 0 \quad\text{and}\quad \det(A) > 0.$$

This is not meant to be memorized as a black box — the lecture's advice for recovering a
half-remembered rule like this one is to test it against a system you already know is stable. Take
$A = -I$ (so $\dot x=-x,\ \dot y=-y$): $x$ and $y$ decouple and each decays exponentially on its
own, so the origin is obviously stable. Here $\mathrm{tr}(A)=-2<0$ and $\det(A) = (-1)(-1)-0 = 1>0$,
which confirms the direction of both inequalities.

The two eigenvalues of $A$ are

$$\lambda_{1,2} = \frac{\mathrm{tr}(A) \pm \sqrt{\mathrm{tr}(A)^2 - 4\det(A)}}{2},$$

and the trace–determinant test is exactly the condition that both roots of this quadratic have
negative real part.

### Nodes and spirals

Whether the eigenvalues under the square root come out real or complex changes what stability
*looks like*, not just whether it holds:

- If $\mathrm{tr}(A)^2 > 4\det(A)$, the eigenvalues are real, and trajectories run in (or out)
  along two straight eigendirections — a generic starting point decomposes into a component along
  each eigenvector, shrinking or growing exponentially along each independently. If both
  eigenvalues are negative this is a **stable node**: trajectories collapse quickly along the
  eigendirection with the more negative eigenvalue and then slide in more slowly along the other,
  so a generic trajectory ends up hugging the *slower* eigendirection as it approaches the fixed
  point.
- If $\mathrm{tr}(A)^2 < 4\det(A)$, the eigenvalues are a complex-conjugate pair, and trajectories
  spiral rather than run in straight lines — a **stable spiral** if the real part is negative, an
  unstable spiral if positive.

<figure>
<svg viewBox="0 0 320 260" role="img" aria-label="The trace-determinant plane, showing which combinations of trace and determinant give a stable node, stable spiral, unstable node, unstable spiral, or saddle">
  <defs>
    <marker id="axArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <rect x="20" y="20" width="140" height="120" fill="currentColor" fill-opacity="0.15" stroke="none"/>

  <path d="M 20,140 Q 160,20 300,140" fill="none" stroke="currentColor" stroke-width="1.3"/>

  <line x1="15" y1="140" x2="305" y2="140" stroke="currentColor" stroke-width="1" marker-end="url(#axArrow)"/>
  <line x1="160" y1="245" x2="160" y2="15" stroke="currentColor" stroke-width="1" marker-end="url(#axArrow)"/>
  <text x="298" y="155" font-size="12" fill="currentColor" text-anchor="end">tr A</text>
  <text x="168" y="25" font-size="12" fill="currentColor">det A</text>

  <text x="90" y="115" font-size="12" text-anchor="middle" fill="currentColor">stable node</text>
  <text x="90" y="45" font-size="12" text-anchor="middle" fill="currentColor">stable spiral</text>
  <text x="228" y="115" font-size="12" text-anchor="middle" fill="currentColor">unstable node</text>
  <text x="228" y="45" font-size="12" text-anchor="middle" fill="currentColor">unstable spiral</text>
  <text x="160" y="200" font-size="12" text-anchor="middle" fill="currentColor">saddle — unstable (det A &#60; 0)</text>
</svg>
<figcaption>The trace of A on the horizontal axis, its determinant vertical. Below the axis
(det A &#60; 0) the eigenvalues are real with opposite sign and the fixed point is always an
unstable saddle, whatever the trace. Above it, the parabola tr(A)^2 = 4 det A separates real
eigenvalues (below it: a node) from complex ones (above it: a spiral); the shaded quadrant, trace
negative and determinant positive, is the only place the fixed point is stable.</figcaption>
</figure>

### A worked matrix: cross-terms can rescue an unstable pair

Finally, a case designed to look wrong at first glance. Take $a=-2$, $d=+1$: on its own, $y$ is
unstable ($\dot y = y$ grows), while $x$ is stable. Can the full 2D system still have a stable
origin? The trace is $a+d=-1<0$, which is promising — $x$'s stability is "more stable" than $y$ is
unstable, so the sum is still negative — but the trace condition alone is necessary, not
sufficient. The determinant is $ad-bc = -2-bc$, and stability additionally needs $\det(A)>0$, i.e.
$-bc>2$: $b$ and $c$ must have **opposite signs**, and the product $|bc|$ has to be large enough.
So a self-repressing $x$ paired with a self-activating $y$ *can* still be stable overall, but only
if there is cross-regulation between them (one activating the other, the other repressing back, or
some such asymmetric pair) strong enough to compensate — confirming, with a concrete matrix, that
whether a fixed point is stable is a property of the whole coupled system, not of each variable's
one-dimensional behavior in isolation.

## Sources

- Transcript: `hfq1t9windg` (MIT 8.591J *Systems Biology*, Fall 2014), the sole input for this
  chapter. Section correspondence: Boolean cartoon of the toggle switch, [01:17]–[04:46]; circuit
  wiring, GFP reporter, and the polycistronic-transcript aside (Gene-Wei Li's talk on $F_OF_1$ ATP
  synthase), [04:46]–[08:58]; IPTG/heat switching and the separation of timescales, [08:58]–[13:40];
  significance of the synthetic construction, [13:40]–[16:06]; philosophy of dimensionless
  equations, [16:06]–[18:26]; the toggle-switch equations and the assumptions embedded in them,
  [18:26]–[34:06]; the meaning of $u=1$ and the dimensional-consistency check, [35:21]–[43:01];
  mapping a degradation-rate change onto $\alpha,\beta,\gamma$, [43:01]–[50:20]; one-dimensional
  and discrete-map stability, and the $n$-dimensional eigenvalue criterion, [50:20]–[58:29]; the
  trace–determinant test for 2D systems, [58:29]–[1:03:55]; eigenvectors, nodes versus spirals, and
  the trace–determinant plane, [1:03:55]–[1:14:44]; the worked $a=-2,\,d=1$ example,
  [1:14:44]–end.
- Named but not contained in this source, and not otherwise supplied: the pre-class reading — a
  review covering the toggle switch experimentally, and a separate set of notes deriving the
  dimensionless equations above and the trace–determinant stability rule from the underlying
  mass-action model (referred to in the lecture only as "that review" and "your notes"); the
  original toggle-switch paper, referred to as "the Collins Lab paper," which the lecture credits
  with predicting bistability from cooperative mutual repression before the circuit was built;
  Strogatz's *Nonlinear Dynamics and Chaos*, recommended by name and title as a reference for
  stability analysis; the repressilator, flagged as the subject of the following lecture.
- Whatever was drawn on the board — the circuit diagrams (including the GFP/lac I construct and the
  four-way IPTG/heat switching diagram used for the in-class poll), the specific phase-portrait
  sketch used to ask which eigenvalue was closer to zero, and the trace–determinant sketch itself —
  is not in the transcript. The Boolean-state and trace–determinant diagrams above are redrawn from
  the algebra and reasoning as narrated, not from the board images.

---

[← 13. From Genes to Ecosystems](13-from-genes-to-ecosystems.md) · [Contents](index.md) · [15. The Moran Process and Fixation →](15-the-moran-process-and-fixation.md)
