---
title: "9. Genetic Toggle Switch and Oscillator"
course: "MIT 8.591J 2004"
chapter: 9
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 9. Genetic Toggle Switch and Oscillator

## What this covers

Lecture 11 works through the linear-stability set-up behind a designed *E. coli* gene circuit
that the same wiring diagram can run either as a bistable toggle switch or as a sustained
oscillator, depending on its parameters — Atkinson, Savageau, Myers & Ninfa, *Development of
Genetic Circuitry Exhibiting Toggle Switch or Oscillatory Behavior in Escherichia coli*, *Cell*
**113**, 597–607 (2003). It is the second of two circuit studies the lecture takes up; the first is
not in the material supplied for this chapter. The chapter assumes the reader can already write
mRNA/protein kinetics as first-order production–decay ODEs, normalize a variable to its
steady-state value, and read stability off the Jacobian of a linearized system.

The supplied lecture outline stops partway through the calculation — mid-way through writing down
the Jacobian matrix, before the characteristic polynomial and before the stability diagram that was
the announced target. This chapter goes exactly as far as the source does and says plainly where it
stops, rather than completing the derivation from scratch.

## A circuit with two feedback loops of opposite sign

The paper's design combines two feedback loops of *opposite* sign on the same promoter. In the
diagram reproduced from the paper's Figure 1A, an mRNA $X_1$ is translated into $X_2$, the
phosphorylated (active) form of the regulatory protein NRI; $X_2$ in turn activates transcription
of a second mRNA $X_3$, which is translated into $X_4$, the LacI protein. The diagram marks the
promoter driving $X_1$ with both a $-$ and a $+$: $X_2$ activates that promoter *directly*, a
short positive loop, while $X_4$ represses it through the longer path $X_2 \to X_3 \to X_4$, a
negative loop closing one step further around. Downstream of $X_4$ the circuit continues to a
third mRNA/protein pair, $X_5$ and $X_6$ (LacZ, the $\beta$-galactosidase reporter used to read the
circuit out experimentally), with nothing looping back — which is exactly why the stability
analysis below only needs the first four of the six equations.

<figure>
<svg viewBox="0 0 480 320" role="img" aria-label="Block diagram of the feedback circuit: X2 and X4 both feed back onto X1's promoter with opposite sign, while X5 and X6 sit downstream with no feedback">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <text x="90" y="30" font-size="12" fill="currentColor" text-anchor="middle">mRNA $X_1$</text>
  <line x1="90" y1="42" x2="90" y2="105" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="90" y="120" font-size="12" fill="currentColor" text-anchor="middle">NRI~P $X_2$</text>

  <line x1="118" y1="112" x2="222" y2="112" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="170" y="103" font-size="12" fill="currentColor" text-anchor="middle">+ $g_{32}$</text>
  <text x="250" y="120" font-size="12" fill="currentColor" text-anchor="middle">mRNA $X_3$</text>

  <line x1="250" y1="130" x2="250" y2="190" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="250" y="205" font-size="12" fill="currentColor" text-anchor="middle">LacI $X_4$</text>

  <line x1="278" y1="197" x2="358" y2="197" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="380" y="205" font-size="12" fill="currentColor" text-anchor="middle">mRNA $X_5$</text>

  <line x1="380" y1="215" x2="380" y2="270" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="380" y="285" font-size="12" fill="currentColor" text-anchor="middle">LacZ $X_6$</text>

  <path d="M 75,108 C 20,90 20,55 78,43" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="20" y="76" font-size="12" fill="currentColor" text-anchor="middle">+ $g_{12}$</text>

  <path d="M 222,202 C 120,285 -5,225 60,55" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="55" y="245" font-size="12" fill="currentColor" text-anchor="middle">- $g_{14}$</text>

  <line x1="335" y1="10" x2="335" y2="310" stroke="currentColor" stroke-width="1" stroke-dasharray="4 4" opacity="0.5"/>
  <text x="345" y="24" font-size="11" fill="currentColor" text-anchor="start">no feedback</text>
  <text x="345" y="38" font-size="11" fill="currentColor" text-anchor="start">beyond $X_4$</text>
</svg>
<figcaption>$X_2$ activates its own promoter directly (short positive loop, exponent $g_{12}$) and,
via $X_3 \to X_4$, represses the same promoter through a longer path (negative loop, exponent
$g_{14}$). $X_5$/$X_6$, the LacZ reporter, sit downstream of $X_4$ with nothing looping back, so
they drop out of the stability calculation.</figcaption>
</figure>

The paper backs this up experimentally with $\beta$-galactosidase reporter time courses under
different induction conditions, and a $\beta$-galactosidase-versus-IPTG dose-response curve on a
log scale — the kind of switch-like, hysteretic dose-response used to demonstrate bistability,
alongside time traces used to demonstrate the alternative, oscillatory behavior. Their captions did
not survive the conversion of the scanned paper, so they are noted here only as the motivation for
building the model below, not as data this chapter can read off.

## From single-step kinetics to a normalized ODE system

The lecture builds the six-variable model out of one repeated module. Take ordinary translation of
an mRNA $X_1$ into a protein $X_2$:

$$\frac{dX_2}{dt} = k_p X_1 - \beta_2 X_2 \tag{VII.17}$$

with $k_p$ the translation rate constant and $\beta_2$ the protein's decay/dilution rate. Normalizing
both variables to their steady-state values, using $X_2^{ss} = \frac{k_p}{\beta_2} X_1^{ss}$, turns
this into a dimensionless deviation-variable equation with no rate constant left in it except the
decay rate:

$$\frac{dx_2}{dt} = \beta_2 (x_1 - x_2) \tag{VII.18}$$

Every equation in the full circuit has exactly this shape, $\dot x_i = \beta_i(\text{input}_i - x_i)$:
each normalized species relaxes toward its current input at a rate set only by its own $\beta_i$.
Odd subscripts are mRNAs, even subscripts are the proteins translated from them, and the full system
for the circuit in the figure above is

$$\begin{aligned}
\frac{dx_1}{dt} &= \beta_1 (f_1 - x_1) \\
\frac{dx_2}{dt} &= \beta_2 (x_1 - x_2) \\
\frac{dx_3}{dt} &= \beta_3 (f_3 - x_3) \\
\frac{dx_4}{dt} &= \beta_4 (x_3 - x_4) \\
\frac{dx_5}{dt} &= \beta_5 (f_5 - x_5) \\
\frac{dx_6}{dt} &= \beta_6 (x_5 - x_6)
\end{aligned} \tag{VII.19}$$

For a translation step (the $x_2$, $x_4$, $x_6$ equations) the input is simply the normalized
upstream mRNA. For a transcription step (the $x_1$, $x_3$, $x_5$ equations) the input is instead a
nonlinear function of whichever proteins regulate that promoter — $f_1$, $f_3$, $f_5$. All of the
model's nonlinearity, and so all of the interesting dynamics, lives in these three functions; the
six differential equations themselves are as linear as they could be.

## The regulatory functions: a floor, a power law, and a ceiling

$f_1$ and $f_3$ (the two functions the outline gives explicitly) are three-piece, power-law
functions of their regulators — a constant floor $B$ (basal, leaky expression) below a threshold, a
power-law middle branch, and a constant ceiling $M$ (fully saturated expression) above a second
threshold:

$$f_1 = \begin{cases}
B & : x_2^{g_{12}} x_4^{g_{14}} < B \\
x_2^{g_{12}} x_4^{g_{14}} & : B < x_2^{g_{12}} x_4^{g_{14}} < M \\
M & : x_2^{g_{12}} x_4^{g_{14}} > M
\end{cases} \tag{VII.20a}$$

$$f_3 = \begin{cases}
B & : x_2^{g_{32}} < B \\
x_2^{g_{32}} & : B < x_2^{g_{32}} < M \\
M & : x_2^{g_{32}} > M
\end{cases} \tag{VII.20b}$$

Reading the exponents' signs off the circuit diagram: $g_{12} > 0$ ($X_2$ activates its own
promoter) and $g_{14} < 0$ ($X_4$ represses the same promoter), while $g_{32} > 0$ ($X_2$ activates
$X_3$'s promoter). $f_3$ has no $x_4$-dependence at all — it only sees $X_2$. $f_5$, which regulates
the reporter branch, is not given in the outline; it does not enter the stability calculation, so
the lecture never writes it down. Only the middle, power-law branch of $f_1$ and $f_3$ has any
local slope — on the two constant pieces the derivative is zero — which is what makes the
linearization below tractable.

## The fixed point and its (partial) linearization

When the parameters put the power-law branch through the point where every normalized variable
equals 1, the system has a single fixed point at

$$x_1 = x_2 = x_3 = x_4 = 1.$$

(Elsewhere in the paper's parameter space the same promoter has *multiple* fixed points instead —
the source of the switch's bistability. The derivation the lecture carries through here is for the
single-fixed-point case, the one that can lose stability to sustained oscillation rather than to a
second stable state.)

To read off stability, linearize the first four equations of (VII.19) about that point. Because
every equation has the relaxation form $\dot x_i = \beta_i(\text{input}_i - x_i)$, differentiating
is mechanical: the diagonal entry is always $-\beta_i$, and an off-diagonal entry is $\beta_i$ times
the local slope of $x_i$'s input with respect to whichever $x_j$ appears in it. On the power-law
middle branch, $\partial f_1/\partial x_2 = g_{12}\, f_1/x_2$, which at the fixed point ($x_2 = 1$,
$f_1 = 1$) is just $g_{12}$ — the kinetic exponent *is* the local elasticity of the promoter at that
point. The same holds for $g_{14}$ and $g_{32}$. Working this out for $x_1$, $x_2$, and $x_3$
reproduces the rows the outline writes down for the Jacobian $A$:

$$A = \begin{bmatrix}
-\beta_1 & \beta_1 g_{12} & 0 & \beta_1 g_{14} \\
\beta_2 & -\beta_2 & 0 & 0 \\
0 & \beta_3 g_{32} & -\beta_3 & \cdots
\end{bmatrix}$$

The first row is $x_1$'s equation: zero effect from $x_3$ (which $f_1$ doesn't see), $\beta_1 g_{12}$
from $x_2$, $\beta_1 g_{14}$ from $x_4$. The second row is $x_2$'s translation equation, identical in
form to (VII.18). The third row is $x_3$'s equation: zero from $x_1$ (which $f_3$ doesn't see either),
$\beta_3 g_{32}$ from $x_2$, $-\beta_3$ on the diagonal.

**This is where the source stops.** The scanned outline page ends mid-row, before the fourth entry of
row three and before the fourth row (for $x_4$) are written down, and well before the characteristic
polynomial of $A$, the stability conditions that would come from it, and the stability diagram
itself — Fig. 1B, the derivation the lecture announces as its goal — are reached. That figure
survives in the converted material only as a badly garbled scan: legible enough to see that it is a
two-parameter diagram, plotted against $g_{12}$ on one axis and the product $g_{32}g_{14}$ on the
other, cut into several numbered regions by a handful of boundary curves, but not reliably enough to
redraw or to say which region is the switch and which is the oscillator. Completing the calculation
— finding $\det(A - \lambda I)$ for the full $4\times4$ matrix and asking which sign patterns of
$g_{12}, g_{14}, g_{32}$ keep every eigenvalue in the stable half-plane — is the natural next step,
but it is not part of what the outline actually contains, so it is not reconstructed here. Anyone
wanting the finished derivation needs the original lecture outline PDF or the paper's Supplementary
Information, which the outline cites directly.

## Sources

- **Lecture outline**, `lecture-outlines/11-outline.md` (lecture 11, MIT 8.591J *Systems Biology*,
  Fall 2004): the citation to Atkinson, Savageau, Myers & Ninfa (2003); equations (VII.17)–(VII.19)
  for the normalized ODE system; the tri-phasic regulatory functions (VII.20a)–(VII.20b); the
  single-fixed-point statement; and the Jacobian $A$, as given verbatim up to the point where the
  source PDF is truncated (after the third row's diagonal entry). The outline's own note that "a
  second study" is discussed implies a first study earlier in the same lecture; that material was
  not supplied and is not covered here.
- **Lecture 11 notes**, `lectures/11-notes.md`: a reconstruction of the Atkinson et al. (2003) *Cell*
  paper itself (title, authors, and figures), used here for the circuit topology of Fig. 1A (the
  $+/-$ signs on the promoter driving $X_1$) and for the existence and rough layout of the Fig. 1B
  stability diagram; also for the reporter-assay figure types (time courses, IPTG dose-response)
  mentioned as experimental context.
- Both source files carry the conversion note that they were reconstructed by a model from PDFs with
  no usable text layer, that every equation is unverified, and that they should be treated as a
  pointer into the original rather than a citable source in their own right — which is why this
  chapter stops exactly where the source stops rather than completing the algebra.

---

[← 8. Biological Oscillators](08-biological-oscillators.md) · [Contents](index.md) · [10. Stochastic Chemical Kinetics →](10-stochastic-chemical-kinetics.md)
