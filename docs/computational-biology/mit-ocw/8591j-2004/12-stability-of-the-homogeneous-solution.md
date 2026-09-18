---
title: "12. Stability of the Homogeneous Solution"
course: "MIT 8.591J 2004"
chapter: 12
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 12. Stability of the Homogeneous Solution

## What this covers

The previous lecture wrote down the Gierer–Meinhardt activator–inhibitor equations that give a
model of local excitation and global inhibition, and found the single steady state at which both
concentrations are uniform in space. This chapter asks the next question: is that uniform state
actually stable? It answers it twice — once for a disturbance that is the same everywhere, and once
for a disturbance that varies with position — using the trace/determinant test for a linear system
of two variables. It assumes the reaction–diffusion pair and the homogeneous solution already in
hand, and the standard eigenvalue criterion for a $2\times2$ linear system.

## The model and its uniform state

The activator $a(x,t)$ and inhibitor $i(x,t)$ satisfy

$$\begin{aligned}
\frac{\partial a}{\partial t} &= r_a + k_a \frac{a^2}{i} - \gamma_a a + D_a \frac{\partial^2 a}{\partial x^2} \\
\frac{\partial i}{\partial t} &= k_i a^2 - \gamma_i i + D_i \frac{\partial^2 i}{\partial x^2}
\end{aligned}$$

with $r_a$ a basal synthesis rate, $k_a,k_i$ rate constants, $\gamma_a,\gamma_i$ decay rates and
$D_a,D_i$ diffusion constants — seven constants in all. The activator promotes its own production
through the $a^2$ term, but that promotion is throttled by dividing by the inhibitor $i$; the
inhibitor is made in proportion to $a^2$ and otherwise just decays and diffuses. That mutual
arrangement is the "local excitation, global inhibition" of the title.

The lecture rescales concentration, time and space into dimensionless $A,I,\tau,s$, which absorbs
$r_a$ into the reference scale — the constant term becomes plain $1$ — and collects the remaining
constants into three dimensionless groups $R$, $Q$, $P$:

$$\begin{aligned}
\frac{\partial A}{\partial \tau} &= 1 + R\,\frac{A^2}{I} - A + \frac{\partial^2 A}{\partial s^2} \\
\frac{\partial I}{\partial \tau} &= Q(A^2 - I) + P\,\frac{\partial^2 I}{\partial s^2}
\end{aligned}$$

The slides do not show the substitution that turns the seven original constants into $R$, $Q$ and
$P$ — that step is missing here and should be checked against the original if it matters. What
matters for this chapter is just that $A$'s own diffusion coefficient has been normalised to $1$,
so $P$ plays the role of the inhibitor's diffusion constant *relative to* the activator's.

The homogeneous solution — the state with no dependence on $s$ or $\tau$ — solves the same two
equations with all derivatives set to zero. The second equation forces $I=A^2$; substituting into
the first collapses it to the linear equation $1+R-A=0$, so there is exactly one such state:

$$\bar A = R+1, \qquad \bar I = (R+1)^2.$$

## When does a uniform disturbance decay?

For a linear system $\dot{\mathbf x} = J\mathbf x$ in two variables, solutions grow like
$e^{\lambda t}$ with $\lambda$ a root of $\lambda^2 - (\operatorname{tr}J)\lambda + \det J = 0$.
Both roots have negative real part — so any small disturbance decays — exactly when
$\operatorname{tr}J<0$ and $\det J>0$. That is the test applied twice below.

Write the reaction terms (no diffusion) as $f(A,I)=1+RA^2/I-A$ and $g(A,I)=Q(A^2-I)$. Their
Jacobian, evaluated at $(\bar A,\bar I)=(R+1,(R+1)^2)$, is

$$J = \begin{pmatrix} \dfrac{2R\bar A}{\bar I}-1 & -\dfrac{R\bar A^2}{\bar I^2} \\[4pt] 2\bar A Q & -Q \end{pmatrix}
= \begin{pmatrix} \dfrac{R-1}{R+1} & -\dfrac{R}{(R+1)^2} \\[4pt] 2(R+1)Q & -Q \end{pmatrix}.$$

Its trace is $\dfrac{R-1}{R+1}-Q$, and its determinant works out to just $Q$: the two off-diagonal
products are $-\dfrac{R-1}{R+1}Q$ (from the diagonal) and $\dfrac{2RQ}{R+1}$ (from the
off-diagonal, with a sign flip), and $-\dfrac{R-1}{R+1}+\dfrac{2R}{R+1}=1$, leaving $\det J=Q$.

So the uniform state is stable to a spatially uniform disturbance exactly when

$$\det J>0 \iff Q>0, \qquad \operatorname{tr}J<0 \iff Q>\frac{R-1}{R+1}.$$

Both must hold; the second is the binding one whenever $R>1$, and the first is the binding one
otherwise.

## Perturbing in space

Now let the disturbance vary with position: write $A(s,\tau)=\bar A+A'(s,\tau)$ and
$I(s,\tau)=\bar I+I'(s,\tau)$, and drop products of the primed terms (the linear-stability
approximation). Substituting into the full PDE reproduces the reaction Jacobian above, plus each
variable's own diffusion term:

$$\begin{aligned}
\frac{\partial A'}{\partial \tau} &= \frac{R-1}{R+1}A' - \frac{R}{(1+R)^2}I' + \frac{\partial^2 A'}{\partial s^2} \\
\frac{\partial I'}{\partial \tau} &= 2Q(1+R)A' - QI' + P\frac{\partial^2 I'}{\partial s^2}
\end{aligned}$$

To test one spatial mode at a time, try a single cosine ripple of "wavelength" set by a scale
$\ell$:

$$A'(s,\tau) = \hat A(\tau)\cos\!\left(\frac{s}{\ell}\right), \qquad I'(s,\tau) = \hat I(\tau)\cos\!\left(\frac{s}{\ell}\right).$$

Because $\cos(s/\ell)$ is an eigenfunction of $\partial^2/\partial s^2$ with eigenvalue
$-1/\ell^2$, every term in the two PDEs above carries the same factor $\cos(s/\ell)$, which cancels
and leaves a pair of ordinary differential equations for the amplitudes:

$$\begin{aligned}
\frac{d\hat A}{d\tau} &= \left(\frac{R-1}{R+1}-\frac{1}{\ell^2}\right)\hat A - \frac{R}{(1+R)^2}\hat I \\
\frac{d\hat I}{d\tau} &= 2Q(1+R)\hat A - \left(Q+\frac{P}{\ell^2}\right)\hat I
\end{aligned}$$

which is exactly the reaction Jacobian $J$ from before, with $1/\ell^2$ subtracted from the
top-left entry and $P/\ell^2$ subtracted from the bottom-right one — each variable's own diffusive
decay, at the wavenumber set by $\ell$.

<figure>
<svg viewBox="0 0 340 180" role="img" aria-label="A flat baseline concentration with a single cosine ripple superimposed, the spatial disturbance being tested">
  <line x1="30" y1="150" x2="320" y2="150" stroke="currentColor" stroke-width="1.2"/>
  <text x="325" y="154" font-size="12" fill="currentColor">s</text>
  <line x1="40" y1="100" x2="300" y2="100" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="45" y="93" font-size="12" fill="currentColor">baseline (Ā or Ī)</text>
  <path d="M 40.0,78.0 L 45.4,78.7 L 50.8,80.9 L 56.2,84.4 L 61.7,89.0 L 67.1,94.3 L 72.5,100.0 L 77.9,105.7 L 83.3,111.0 L 88.8,115.6 L 94.2,119.1 L 99.6,121.3 L 105.0,122.0 L 110.4,121.3 L 115.8,119.1 L 121.2,115.6 L 126.7,111.0 L 132.1,105.7 L 137.5,100.0 L 142.9,94.3 L 148.3,89.0 L 153.8,84.4 L 159.2,80.9 L 164.6,78.7 L 170.0,78.0 L 175.4,78.7 L 180.8,80.9 L 186.2,84.4 L 191.7,89.0 L 197.1,94.3 L 202.5,100.0 L 207.9,105.7 L 213.3,111.0 L 218.8,115.6 L 224.2,119.1 L 229.6,121.3 L 235.0,122.0 L 240.4,121.3 L 245.8,119.1 L 251.2,115.6 L 256.7,111.0 L 262.1,105.7 L 267.5,100.0 L 272.9,94.3 L 278.3,89.0 L 283.8,84.4 L 289.2,80.9 L 294.6,78.7 L 300.0,78.0"
        fill="none" stroke="currentColor" stroke-width="1.8"/>
  <text x="245" y="70" font-size="12" fill="currentColor">A'(s,τ) = Â(τ)cos(s/ℓ)</text>
</svg>
<figcaption>The uniform state disturbed by one spatial mode of scale ℓ. Whether the ripple's
amplitude Â(τ), Î(τ) grows or decays is exactly the question the mode-ℓ Jacobian below answers.</figcaption>
</figure>

## When does a spatial ripple decay?

Apply the same trace/determinant test to this mode-$\ell$ Jacobian. The trace condition rearranges
cleanly:

$$\operatorname{tr}<0 \iff Q > \frac{R-1}{R+1} - \frac{1+P}{\ell^2},$$

which is a *weaker* requirement than the uniform-disturbance condition $Q>\frac{R-1}{R+1}$ — adding
diffusion only helps here, since $(1+P)/\ell^2>0$. The determinant condition is the more delicate
one and genuinely depends on $\ell$:

$$\det>0 \iff -\left(\frac{R-1}{R+1}-\frac{1}{\ell^2}\right)\left(Q+\frac{P}{\ell^2}\right) + \frac{2QR}{1+R} > 0,$$

and working out exactly which values of $\ell$ satisfy it — as opposed to the uniform case, where
there is no $\ell$ to range over — is a genuinely harder calculation than the one for the flat
disturbance. The slides do not carry it through mode by mode; they state a single comparison as
the conclusion, given twice in the same form:

$$\text{homogeneous stability: } Q > \frac{R-1}{R+1}, \qquad\qquad \text{spatial stability: } \frac{Q}{P} > \frac{R-1}{R+1}.$$

(This chapter's slides are a model's reconstruction of a scanned PDF, flagged by the source itself
as unverified equation-by-equation; the step from the boxed trace/determinant inequalities above to
this final $\ell$-independent line is one it does not fully preserve. The two boxed results
themselves are stated twice, identically, so they are taken here as the lecture's conclusion even
though the derivation between them and the general mode-$\ell$ conditions above is not fully
reconstructable from what survives.)

## Reading the comparison

The slides put the two conditions side by side and gloss them directly: a state is
*homogeneously* stable if $\bar I$ relaxes back to its previous value after a small uniform
disturbance, and *inhomogeneously* stable if $I'$ relaxes back to $\bar I$ after a small spatial
disturbance.

The two boxed thresholds are the same expression, $\dfrac{R-1}{R+1}$, compared against $Q$ on one
side and $Q/P$ on the other. If the inhibitor's relative diffusion constant $P$ exceeds $1$ — it
diffuses faster than the activator, which is exactly what "global" is supposed to mean in this
model's name — then $Q/P<Q$, so there is a band of $Q$ for which the flat state survives a uniform
nudge ($Q$ above the threshold) but not a spatially varying one ($Q/P$ below it). Whenever $R>1$
(so the threshold itself is positive) and $P>1$, that band is non-empty: a state that looks settled
under a uniform perturbation can still fail under a patterned one. That gap between the two
thresholds is the opening this course's account of pattern formation needs.

## Sources

- Both slide decks under `lectures/16-notes/` in the course's OCW materials: `01-local-excitation-global-inhibition.md`
  (the model, its nondimensionalisation, and the homogeneous solution) and
  `02-stability-of-homogeneous-solution.md` (the homogeneous and spatial stability analysis). No
  transcript, written notes or problem set were supplied for this lecture, so this chapter is built
  from those two files alone.
- This is genuinely thin material: the two slide files together are a handful of terse equation
  blocks with almost no connecting prose, converted by a model from a scanned PDF with no text
  layer. Both files carry the source's own flag that "every equation is unverified." Everywhere this
  chapter shows a derivation in full (the Jacobian entries, the trace and determinant, the
  cosine-mode substitution), it has been checked directly against the slide's stated results by
  recomputing it; the one place that could not be reconciled — the algebra between the general
  mode-$\ell$ trace/determinant conditions and the slides' final, $\ell$-independent comparison — is
  flagged in the text rather than papered over.
- The course runs this topic across three consecutive lectures (numbered 15–17 in the lecture
  sequence); this chapter covers only the middle one, the stability analysis of the homogeneous
  solution. What set up the model (the previous lecture) and what is built on this stability result
  (the next) are not part of what was supplied here.

---

[← 11. The Turing Instability Condition](11-the-turing-instability-condition.md) · [Contents](index.md) · [13. The LEGI Dispersion Relation →](13-the-legi-dispersion-relation.md)
