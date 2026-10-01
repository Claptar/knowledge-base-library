---
title: "20. Master Equation for Gene Expression"
course: "MIT 8.591J 2004"
chapter: 20
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 20. Master Equation for Gene Expression

## What this covers

A genetic network — a gene making mRNA, mRNA making protein, both being degraded — is a chemical
reaction network in which the "concentrations" are small integer copy numbers, so its state is a
probability distribution rather than a deterministic trajectory. This chapter builds the tool for
handling that: the **chemical master equation**, and the trick of rewriting it as a single
differential equation for the **probability generating function**, from which the mean and
variance of copy number can be read off by differentiation instead of by solving for the full
distribution. It works through the master equation, in generating-function form, for the three
elementary reactions that a gene-expression network is built from. It assumes familiarity with
elementary chemical reaction notation (a reaction and its rate constant) and with generating
functions or moment generating functions from probability.

## The master equation

A genetic network is described by $N$ state variables $n_1, \dots, n_N$ — copy numbers of
chemical species such as mRNAs or proteins — and $M$ rate constants $k_1, \dots, k_M$ for the
reactions that convert them into one another. Because copy numbers are small and reactions fire
at random times, the state of the system at time $t$ is not a number but a probability
distribution $p(n_1, \dots, n_N, t)$ over all the states the system could be in.

The **master equation** is the statement that this distribution changes because probability
flows between states: the probability of being in a given state increases at the rate that other
states transition *into* it, and decreases at the rate that the state transitions *out of* it.
Written out for a specific reaction, it is a differential equation for $p$ with one loss term per
way of leaving the state and one gain term per way of entering it.

In principle the master equation determines the full distribution $p(n_1,\dots,n_N,t)$. In
practice it can rarely be solved outright, so the working strategy is to give up on the full
distribution and settle for its moments — the mean, the variance, the covariances between
species. These are most easily reached through the **probability generating function**

$$F(z_1, z_2, \dots, z_N, t) = \sum_{n_1, n_2, \dots, n_N} z_1^{n_1} z_2^{n_2} \cdots z_N^{n_N}\, p(n_1, n_2, \dots, n_N, t),$$

where each $n_i$ ranges over the states that species $i$ can occupy (here, $0$ to $\infty$).
Evaluated and differentiated at $z_1 = \dots = z_N = 1$, $F$ hands back the quantities that matter
without ever exhibiting $p$ itself:

$$F\big|_1 = 1, \qquad \left.\frac{\partial F}{\partial z_i}\right|_1 = \langle n_i \rangle, \qquad
\left.\frac{\partial^2 F}{\partial z_i^2}\right|_1 = \langle n_i(n_i-1)\rangle, \qquad
\left.\frac{\partial^2 F}{\partial z_i\, \partial z_j}\right|_1 = \langle n_i n_j\rangle.$$

The first identity is just normalisation ($\sum p = 1$). The rest are why $F$ earns the name
"generating function": the mean, the (factorial) second moment, and the cross-correlation between
two species are all partial derivatives of $F$ evaluated at the single point $z=1$.

The plan for the rest of the chapter is to take the master equation for each elementary reaction
that a genetic network is built from, multiply it by $z_1^{n_1} z_2^{n_2}\cdots$, sum over all
states, and use the identities above to turn it into a differential equation for $F$ itself — a
single PDE in place of an infinite system of coupled equations for $p(n_1,\dots,n_N,t)$.

## Building block 1: synthesis from a template

Transcription and translation both have this shape: a template (DNA for transcription, mRNA for
translation) produces copies of a product without being consumed itself.

$$A \xrightarrow{\;k\;} A + B$$

Molecule $A$ produces a copy of $B$ at rate $k$; the number of $A$ molecules is unaffected. Let
$n_1$ be the number of $A$ and $n_2$ the number of $B$. The master equation for this reaction is

$$\dot p(n_1, n_2, t) = -k n_1\, p(n_1, n_2, t) + k n_1\, p(n_1, n_2 - 1, t).$$

The first term is the state $[n_1,n_2]$ transitioning *away*, to $[n_1, n_2+1]$, at rate $kn_1$ —
it drains probability out of $p(n_1,n_2,t)$. The second term is the state $[n_1,n_2-1]$
transitioning *into* $[n_1,n_2]$ at the same rate — it feeds probability in.

To convert this into an equation for $F$, multiply both sides by $z_1^{n_1}z_2^{n_2}$ and sum over
all $n_1,n_2$. Two identities do the work. First, differentiating $F$ directly,

$$\frac{\partial F}{\partial z_1} = \sum_{n_1} n_1 z_1^{n_1-1}\, p(n_1,n_2,t)
\quad\Longrightarrow\quad
z_1\frac{\partial F}{\partial z_1} = \sum_{n_1} n_1 z_1^{n_1}\, p(n_1,n_2,t),$$

which handles the loss term directly. Second, the gain term needs an index shift: writing
$n_2' = n_2 - 1$,

$$\sum_{n_1,\, n_2} n_1 z_1^{n_1} z_2^{n_2}\, p(n_1, n_2-1, t)
= z_1 z_2 \sum_{n_1,\, n_2'} n_1 z_1^{n_1-1} z_2^{n_2'}\, p(n_1, n_2', t)
= z_1 z_2 \frac{\partial F}{\partial z_1},$$

where shifting the lower limit of the $n_2$-sum is free because $p(n_1,-1,t)=0$ — there is no such
state. Putting the two pieces together,

$$\dot F(z_1, z_2, t) = k z_1 (z_2 - 1) \frac{\partial F}{\partial z_1}.$$

If the template number is fixed at $n_1 = n$ (constant), $F$ no longer depends on $z_1$ and this
collapses to a single first-order equation in $z_2$ alone:

$$\dot F(z_2, t) = kn(z_2 - 1) F.$$

This special case is solvable on its own, but it only describes production from a template whose
own copy number never changes. In the gene-expression cascade below, the "template" for the
second step (mRNA producing protein) does *not* have a fixed copy number — so it is the general
equation, not the special case, that is needed to assemble the full network.

## Building block 2: degradation

$$B \xrightarrow{\;\gamma\;} 0$$

This single reaction stands for two distinct physical processes: true degradation, in which $B$
is converted into a species outside the subset of interest, and dilution, in which $B$ is removed
by growth of the volume it sits in (e.g. cell division). Either way $\gamma$ is the rate constant
and $\ln 2/\gamma$ the corresponding half-life. The master equation is again a birth–death balance,
now with $B$ molecules disappearing rather than appearing:

$$\dot p(n_1, t) = -\gamma n_1\, p(n_1, t) + \gamma (n_1+1)\, p(n_1+1, t).$$

Carrying out the same multiply-and-sum procedure as above (the loss term gives $z_1\partial
F/\partial z_1$ directly; the gain term needs the analogous shift, now with the lower limit moving
the other way) gives

$$\dot F(z_1, t) = -\gamma (z_1 - 1) \frac{\partial F}{\partial z_1}.$$

## Building block 3: conversion at fixed total number

$$A \xrightarrow{\;k\;} B$$

Here $A$ is converted into $B$ rather than producing it, so the total $n_0 + n_1 = n$ is
conserved and only one variable is needed to describe the state — take it to be $n_2$, the number
of $B$ molecules (equivalently: $n - n_2$ molecules of $A$ remain). The master equation is

$$\dot p(n_2, t) = -k(n-n_2)\, p(n_2, t) + k(n - n_2 + 1)\, p(n_2 - 1, t).$$

The same procedure applies, with one extra subtlety flagged in the lecture: because $n_2$ ranges
only from $0$ to $n$ rather than to $\infty$, the sums that define $F$ and its derivatives are
finite. The boundary terms this produces when shifting the index (as in the derivation above)
cancel against each other, so the result has the same form as before:

$$\dot F(z_2, t) = kn(z_2 - 1) F - k z_2(z_2 - 1) \frac{\partial F}{\partial z_2}.$$

## The three results together

$$
\begin{array}{c|c|c}
\text{Reaction} & \text{Type} & \dot F = \\\hline
A \xrightarrow{k} A + B & \text{synthesis from a template} & k z_1(z_2-1)\dfrac{\partial F}{\partial z_1} \\[2mm]
B \xrightarrow{\gamma} 0 & \text{degradation / dilution} & -\gamma(z_1-1)\dfrac{\partial F}{\partial z_1} \\[2mm]
A \xrightarrow{k} B,\ \ n_0+n_1=n & \text{conversion, fixed total} & kn(z_2-1)F - k z_2(z_2-1)\dfrac{\partial F}{\partial z_2}
\end{array}
$$

Each is linear in $F$ and its first derivatives — a consequence of the underlying reactions being
first-order in copy number — which is exactly what makes the generating-function equation
tractable where the master equation for $p$ itself was not. The stated purpose of assembling
these three is that larger chemical networks are built up out of them.

## Where the building blocks are heading

The network the lecture is aiming at is the simplest model of gene expression: a gene (DNA) is
transcribed into mRNA, and the mRNA is translated into protein, with both mRNA and protein subject
to degradation.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="DNA is transcribed into mRNA, mRNA is translated into protein, and both mRNA and protein degrade">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <rect x="30" y="165" width="140" height="16" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="100" y="177" text-anchor="middle" font-size="11" fill="currentColor">DNA</text>

  <line x1="100" y1="164" x2="100" y2="128" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="112" y="148" font-size="12" fill="currentColor">$k_R$</text>

  <text x="100" y="112" text-anchor="middle" font-size="12" fill="currentColor">mRNA</text>

  <line x1="100" y1="100" x2="100" y2="55" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="112" y="80" font-size="12" fill="currentColor">$k_P$</text>

  <text x="100" y="38" text-anchor="middle" font-size="12" fill="currentColor">Protein</text>

  <line x1="140" y1="112" x2="220" y2="112" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="180" y="105" text-anchor="middle" font-size="12" fill="currentColor">$\gamma_R$</text>
  <text x="235" y="117" font-size="13" fill="currentColor">&#8709;</text>

  <line x1="140" y1="38" x2="220" y2="38" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="180" y="31" text-anchor="middle" font-size="12" fill="currentColor">$\gamma_P$</text>
  <text x="235" y="43" font-size="13" fill="currentColor">&#8709;</text>
</svg>
<figcaption>The gene-expression cascade the master-equation machinery is being built for: DNA is
an unconsumed template producing mRNA at rate $k_R$, mRNA is an unconsumed template producing
protein at rate $k_P$, and mRNA and protein each degrade at rates $\gamma_R$ and $\gamma_P$.</figcaption>
</figure>

Structurally, each arrow in this picture is one of the three building blocks above: mRNA
production from the DNA template and protein production from the mRNA template are both instances
of the synthesis reaction $A \to A+B$; mRNA and protein removal are both instances of the
degradation reaction $B \to 0$. The system has $N=2$ state variables (mRNA copy number, protein
copy number) and $M=4$ rate constants ($k_R,\gamma_R,k_P,\gamma_P$), matching the general
$N$-variable, $M$-constant description the chapter opened with. The one point worth holding onto
from building block 1 is that mRNA is *not* a fixed-copy-number template for translation — its own
count fluctuates under its own production and decay — so combining the blocks into a joint
generating-function equation for (mRNA, protein) needs the general form of the synthesis equation,
not the fixed-$n$ special case.

The transcript breaks off at this point — after stating that larger networks are assembled from
these building blocks, and before actually carrying out that assembly for the cascade above (which
would mean writing the joint master equation for the pair (mRNA copies, protein copies), combining
the corresponding generating-function equations, and extracting the mean, variance, and noise of
protein number from the result).

## Sources

- Transcript: `recordings/stochastics-transcript.md` in `computational-biology/mit-ocw/8591j-2004`
  (MIT 8.591J, Fall 2004, "Systems Biology," material credited to Alexander van Oudenaarden and
  Juan Pedraza), section "1. The master equation approach" — the master equation setup, the
  generating-function identities, and the derivations for all three elementary reactions.
- Figure: page 4 of the source PDF (`stochastics-transcript/figures/p004-1.png`) — the DNA/mRNA/
  protein cascade with rates $k_R,\gamma_R,k_P,\gamma_P$, redrawn above as an SVG.
- The transcript is machine-reconstructed from a PDF with no text layer ("fidelity:
  reconstructed" in the file's front matter); every equation in it, and hence in this chapter, is
  flagged there as unverified against the original. The source's own summary table ("Table 1") is
  garbled/truncated after its first row in the converted file; the table given here is
  reconstructed from the three equations derived in the body text rather than copied from that
  table.
- Not contained in the supplied transcript, and not reconstructed here: the combination of the
  three building blocks into the joint generating-function equation for the mRNA/protein cascade,
  and the resulting expressions for mean, variance and noise. No slides, notes or exercises were
  supplied for this lecture.

---

[← 19. Linear Stability of Fixed Points](19-linear-stability-of-fixed-points.md) · [Contents](index.md)
