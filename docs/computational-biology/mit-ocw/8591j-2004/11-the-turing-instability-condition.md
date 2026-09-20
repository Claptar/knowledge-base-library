---
title: "11. The Turing Instability Condition"
course: "MIT 8.591J 2004"
chapter: 11
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 11. The Turing Instability Condition

## What this covers

This chapter answers a single question: under what conditions does a uniform mixture of a
diffusible activator and a diffusible inhibitor spontaneously break into a spatial pattern,
rather than settling back to a flat, featureless state? It sets up the Turing-Gierer-Meinhardt
activator-inhibitor reaction-diffusion model and carries a full linear-stability calculation
through to a precise, checkable condition on the two molecules' diffusion ranges. This is the
first of three lectures on this model; it builds the machinery that the next two lectures use.

It assumes comfort with a pair of coupled ordinary differential equations, the trace/determinant
test for the stability of a linear $2\times2$ system, and the diffusion equation
$\partial c/\partial t = D\,\partial^2 c/\partial x^2$ from earlier in the course.

## The activator-inhibitor model

Many patterns in development — stripes, spots, evenly spaced structures — look as though they
emerged from a uniform starting state that broke its own symmetry. Turing was the first to give
this a mathematical formulation; Gierer and Meinhardt turned it into a concrete model built from
a named activator and a named inhibitor. The pairing is often called the Turing-Gierer-Meinhardt
model, and it is the object of this lecture.

Let $a(x,t)$ and $i(x,t)$ be the concentrations of the activator and the inhibitor along one
spatial dimension. The model is

$$
\frac{\partial a}{\partial t} = r_a + k_a\frac{a^2}{i} - \gamma_a a + D_a\frac{\partial^2 a}{\partial x^2},
\qquad
\frac{\partial i}{\partial t} = k_i a^2 - \gamma_i i + D_i\frac{\partial^2 i}{\partial x^2}.
\tag{1}
$$

Reading term by term: $r_a$ is a constant, "leaky" production of activator (a promoter that is
never fully off); $k_a a^2/i$ is autocatalytic production of activator that is switched on by
activator itself and switched off by inhibitor; $\gamma_a a$ and $\gamma_i i$ are ordinary
first-order decay; $D_a\partial^2a/\partial x^2$ and $D_i\partial^2 i/\partial x^2$ are diffusion.
The inhibitor's production, $k_i a^2$, is driven by the activator but has no term of its own to
switch it off other than decay.

Where does the odd term $a^2/i$ come from? Write the probability that an activator dimer is bound
and no inhibitor monomer is bound as a saturating function of both species:

$$
Y = \frac{K_a a^2}{1+K_a a^2}\left(1 - \frac{K_i i}{1+K_i i}\right)
  = \frac{K_a a^2}{1+K_a a^2}\cdot\frac{1}{1+K_i i}
  \;\approx\; \text{const}\times\frac{a^2}{i}.
\tag{2}
$$

The activator must dimerize before it can act — hence $a^2$ and $K_a$ — while a single bound
inhibitor monomer is enough to block it — hence the plain $K_i i$. The approximation on the right
holds when $a$ is small enough that $K_aa^2\ll1$ and $i$ is large enough that $K_ii\gg1$: the first
factor is then just $K_aa^2$, the second is just $1/(K_ii)$, and the product is a constant times
$a^2/i$ — the term that appears in $(1)$. The same dimer/monomer asymmetry shows up in the
inhibitor's own production, $k_ia^2$: this is a Hill function of order $n_H=2$ in the activator,
because it is again the activator dimer that drives it.

## Reducing nine parameters to three

Equation $(1)$ carries nine independent constants ($r_a,k_a,k_i,\gamma_a,\gamma_i,D_a,D_i$, and the
two concentration scales needed to state initial conditions). Before asking anything about
stability it pays to non-dimensionalize, both to simplify the algebra and to see how many
genuinely independent knobs the problem has.

Measure time in units of the activator's own decay time, and space in units of the distance the
activator diffuses in that time:

$$
\tau \equiv \gamma_a t, \qquad s \equiv \frac{x}{\sqrt{D_a/\gamma_a}}.
\tag{3}
$$

Substituting $(3)$ into $(1)$ leaves the concentrations dimensional but the independent variables
dimensionless. There is still freedom left to rescale $a$ and $i$ themselves; write

$$
A \equiv \frac{a}{a_0}, \qquad I \equiv \frac{i}{i_0}.
\tag{4}
$$

Two of the remaining constants can be absorbed by choosing $a_0$ and $i_0$ so that the constant
production term and the coupling term both come out with coefficient one:

$$
a_0 = \frac{r_a}{\gamma_a}, \qquad i_0 = \frac{k_ia_0^2}{\gamma_i} = \frac{k_ir_a^2}{\gamma_i\gamma_a^2}.
\tag{5}
$$

What is left, after all the dust settles, is a system with only three parameters:

$$
\frac{\partial A}{\partial \tau} = 1 + R\frac{A^2}{I} - A + \frac{\partial^2 A}{\partial s^2},
\qquad
\frac{\partial I}{\partial \tau} = Q(A^2 - I) + P\frac{\partial^2 I}{\partial s^2},
\tag{6}
$$

$$
P \equiv \frac{D_i}{D_a}, \qquad Q \equiv \frac{\gamma_i}{\gamma_a}, \qquad R \equiv \frac{k_a\gamma_i}{r_ak_i}.
\tag{7}
$$

$P$ compares the two diffusion constants, $Q$ compares the two decay rates, and $R$ compares the
strength of the activator's self-catalysis $k_a$ to its leaky, constant baseline $r_a$ — how
strongly the activator's own production depends on itself rather than on a fixed background rate.
Everything that follows is a statement about these three numbers.

## The spatially uniform steady state

Set $\partial/\partial s = 0$ and look for a constant solution $(A,I)=(\bar A,\bar I)$ of $(6)$.
The second equation gives $\bar I = \bar A^2$ directly; substituting into the first,
$1+R-\bar A=0$, so

$$
\bar A = R+1, \qquad \bar I = (R+1)^2.
\tag{8}
$$

This is the pattern-free state: the same concentration of activator and inhibitor everywhere.
Whether it can persist is a separate question from whether it exists, and it is answered by
linearizing $(6)$ about $(8)$ and computing the Jacobian. Differentiating the right-hand sides of
$(6)$ with respect to $A$ and $I$ and evaluating at $(\bar A,\bar I)$ gives

$$
J = \begin{pmatrix} \dfrac{R-1}{R+1} & -\dfrac{R}{(R+1)^2} \\[2mm] 2Q(R+1) & -Q \end{pmatrix}.
\tag{9}
$$

A linear system is stable against a perturbation that is uniform in space exactly when the trace
of $J$ is negative and its determinant is positive. The determinant works out to exactly $Q$,
which is positive by the definition in $(7)$ regardless of anything else — so it imposes no new
condition. The trace gives the one condition that matters:

$$
\frac{R-1}{R+1} < Q.
\tag{10}
$$

If $(10)$ holds, nudging the whole system away from $(\bar A,\bar I)$ everywhere at once relaxes
back. It says nothing yet about a perturbation that is uneven across space — that is the question
the rest of the lecture is built around.

## Perturbing the uniform state in space

Write $A(s,\tau)=\bar A+A'(s,\tau)$ and $I(s,\tau)=\bar I+I'(s,\tau)$ and linearize $(6)$ in the
small quantities $A',I'$. The reaction part reproduces the Jacobian $(9)$ term for term; the
diffusion terms survive unchanged because they are already linear:

$$
\frac{\partial A'}{\partial \tau} = \frac{R-1}{R+1}A' - \frac{R}{(R+1)^2}I' + \frac{\partial^2 A'}{\partial s^2},
\qquad
\frac{\partial I'}{\partial \tau} = 2Q(R+1)A' - QI' + P\frac{\partial^2 I'}{\partial s^2}.
\tag{11}
$$

This is a linear, constant-coefficient system, translation-invariant in $s$, so any perturbation
can be built by superposing single spatial frequencies, and by linearity each frequency evolves on
its own. It is enough, then, to test one at a time:

$$
A'(s,\tau) = \hat A(\tau)\cos(s/\ell), \qquad I'(s,\tau) = \hat I(\tau)\cos(s/\ell).
\tag{12}
$$

The trial function is exactly suited to $(11)$ because $\partial^2/\partial s^2$ turns
$\cos(s/\ell)$ back into itself, times $-1/\ell^2$: differentiating twice does not change the
spatial shape, only its overall size. Substituting $(12)$ into $(11)$ and cancelling the common
factor $\cos(s/\ell)$ converts the perturbation PDE into a pair of ODEs for the amplitude of a
single wavelength $\ell$:

$$
\frac{d\hat A}{d\tau} = \left(\frac{R-1}{R+1} - \frac1{\ell^2}\right)\hat A - \frac{R}{(R+1)^2}\hat I,
\qquad
\frac{d\hat I}{d\tau} = 2Q(R+1)\hat A - \left(Q+\frac{P}{\ell^2}\right)\hat I.
\tag{13}
$$

Diffusion has turned into an extra decay term, $1/\ell^2$ on the activator and $P/\ell^2$ on the
inhibitor: a mode of short wavelength (large $1/\ell^2$) is damped harder by diffusion than a mode
of long wavelength. The system $(13)$ is stable against this particular $\ell$ when its own trace
is negative and determinant positive. The trace condition,

$$
\frac{R-1}{R+1} - Q - \frac1{\ell^2} - \frac{P}{\ell^2} < 0,
$$

holds automatically whenever $(10)$ does, since it only subtracts more from an already-negative
quantity — diffusion never destabilizes the trace. The determinant condition is where all the
content is:

$$
-\left(\frac{R-1}{R+1}-\frac1{\ell^2}\right)\left(Q+\frac{P}{\ell^2}\right) + \frac{2QR}{R+1} > 0.
\tag{14}
$$

Multiplying out and collecting powers of $\ell$ turns $(14)$ into a quartic-in-$\ell$ inequality
(equivalently, quadratic in $\alpha\equiv\ell^2$):

$$
\frac{Q}{P}\ell^4 + \left(\frac{Q}{P} - \frac{R-1}{R+1}\right)\ell^2 + 1 > 0.
\tag{15}
$$

If $Q/P > (R-1)/(R+1)$, every coefficient in $(15)$ is non-negative and the sum of three
non-negative terms cannot be negative, so the inequality holds for *every* wavelength $\ell$:

$$
\frac{Q}{P} > \frac{R-1}{R+1}
\tag{16}
$$

is enough, on its own, to guarantee that no spatial mode grows. Both $(10)$ and $(16)$ certainly
hold whenever $P<1$ — activator diffusing faster than inhibitor. The uniform state is then safe no
matter how strongly autocatalytic the activator is. Pattern formation, if it happens at all, needs
the opposite arrangement: the inhibitor diffusing faster than the activator. This is the "long-range
inhibition, short-range activation" condition the lecture is named for.

## Locating the actual instability

Genuine instability needs $(16)$ to fail for *some* wavelength, i.e.

$$
f(\alpha) \equiv \frac{Q}{P}\alpha^2 + \left(\frac{Q}{P}-\frac{R-1}{R+1}\right)\alpha + 1 < 0
\qquad\text{for some } \alpha=\ell^2>0.
\tag{17}
$$

*(The reconstructed slide deck for this lecture writes the middle coefficient of the quadratic in
$(15)$/$(17)$ as $(R+1)/(R-1)$ rather than $(R-1)/(R+1)$; that reciprocal is inconsistent with the
sufficient condition $(16)$ stated immediately around it and with the threshold and $R_c$ derived
below, both of which only close up correctly with $(R-1)/(R+1)$. The form used here is the one that
is self-consistent with the rest of the derivation.)*

$f$ is an upward-opening parabola in $\alpha$ ($Q/P>0$), so it dips below zero only if it has two
real roots, and only between them. The roots solve

$$
\alpha = \frac{\left(\dfrac{R-1}{R+1}-\dfrac{Q}{P}\right) \pm \sqrt{\left(\dfrac{R-1}{R+1}-\dfrac{Q}{P}\right)^2 - 4\dfrac{Q}{P}}}{2Q/P}.
\tag{18}
$$

We are asking this question precisely in the regime where $(16)$ has failed, i.e. $Q/P <
(R-1)/(R+1)$, so the sum of the two roots (proportional to $(R-1)/(R+1) - Q/P$) is positive and
their product ($=P/Q$) is positive too: if the roots are real at all, both are positive, and there
is automatically a genuine band of unstable wavelengths, not just a single stray root. So the whole
condition for instability reduces to requiring the discriminant to be positive:

$$
\left(\frac{R-1}{R+1}-\frac{Q}{P}\right)^2 > 4\frac{Q}{P}
\quad\Longleftrightarrow\quad
\frac{R-1}{R+1} > 2\sqrt{\frac{Q}{P}} + \frac{Q}{P}.
\tag{19}
$$

This is the instability condition. It defines a critical value $R_c$, above which $(19)$ holds:

$$
R_c = \frac{1+\left(2\sqrt{Q/P}+Q/P\right)}{1-\left(2\sqrt{Q/P}+Q/P\right)}.
\tag{20}
$$

For a strongly autocatalytic activator ($R\gg1$), the left side of $(19)$ approaches $1$, and the
condition collapses to a statement about $P$ and $Q$ alone:

$$
\frac{Q}{P} + 2\sqrt{\frac{Q}{P}} < 1
\quad\Longrightarrow\quad
\sqrt{\frac{Q}{P}} = \sqrt{\frac{D_a/\gamma_a}{D_i/\gamma_i}} \lesssim 0.4.
\tag{21}
$$

## What the condition means

The quantity $\sqrt{D/\gamma}$ has units of length: it is the typical distance a molecule diffuses
before it decays, so it is natural to call it that molecule's *range*. Condition $(21)$ says the
activator's range must be no more than about $0.4$ of the inhibitor's range — equivalently, the
inhibitor's range must be at least about $2.5$ times the activator's. Diffusion alone breaking a
uniform state into a pattern is not automatic; it needs this specific separation of length scales.

<figure>
<svg viewBox="0 0 360 210" role="img" aria-label="A narrow activator spike sits inside a much broader inhibitor cloud centred on the same point">
  <line x1="20" y1="185" x2="345" y2="185" stroke="currentColor" stroke-width="1.2"/>
  <text x="350" y="189" font-size="12" fill="currentColor">s</text>
  <path d="M 45 183 Q 180 95 315 183 L 315 185 L 45 185 Z" fill="currentColor" fill-opacity="0.12" stroke="none"/>
  <path d="M 45 183 Q 180 95 315 183" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="6 4"/>
  <path d="M 150 183 Q 180 30 210 183" fill="none" stroke="currentColor" stroke-width="2.2"/>
  <text x="212" y="45" font-size="12" fill="currentColor">activator</text>
  <text x="240" y="118" font-size="12" fill="currentColor">inhibitor</text>
</svg>
<figcaption>A single activator spike (solid, narrow) sits inside the much broader pool of
inhibitor it drives (dashed, shaded). Because the inhibitor's diffusion range is several times
the activator's, the cloud suppresses new spikes from forming nearby while the narrow spike itself
mostly escapes its own inhibition — the geometric picture behind condition (21).</figcaption>
</figure>

This is the sense in which the model is "local excitation, global inhibition": a molecule that
turns itself on nearby and turns everything off far away is what it takes, in this model, for a
featureless field of activator and inhibitor to spontaneously organize into a spaced-out pattern of
spikes.

## Sources

- All four slide files for this lecture, `lecture-outlines/15-outline/01`-`04` in
  `computational-biology/mit-ocw/8591j-2004`: the model and the saturation function $(1)$-$(2)$
  from `01-viii-local-excitation-global-inhibition-model.md`; the non-dimensionalization and the
  homogeneous steady state $(3)$-$(10)$ from `02-dimensionless-variables.md`; the spatial
  perturbation analysis $(11)$-$(16)$ from `03-spatially-inhomogeneous-solutions.md`; the
  instability threshold and range condition $(17)$-$(21)$ from
  `04-conditions-for-inhomogeneous-instability.md`.
- No transcript, written notes or exercise set was supplied for this lecture.
- The source markdown for all four files is itself flagged as machine-reconstructed from a PDF
  with no text layer, with every equation marked unverified. The polynomial-in-$\ell$ equations in
  the third and fourth files display the fraction $(R+1)/(R-1)$ where the surrounding argument
  requires $(R-1)/(R+1)$; this chapter uses the latter throughout, since it is the form that
  reproduces the stated sufficient condition, the final threshold, and $R_c$ consistently — see
  the note after equation $(17)$.
- The lecture is the first of three (numbered 15, 16 and 17 in the course) on this model; later
  lectures were not part of the material supplied for this chapter.

---

[← 10. Stochastic Chemical Kinetics](10-stochastic-chemical-kinetics.md) · [Contents](index.md) · [12. Stability of the Homogeneous Solution →](12-stability-of-the-homogeneous-solution.md)
