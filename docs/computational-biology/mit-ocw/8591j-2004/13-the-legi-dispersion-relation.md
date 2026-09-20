---
title: "13. The LEGI Dispersion Relation"
course: "MIT 8.591J 2004"
chapter: 13
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 13. The LEGI Dispersion Relation

## What this covers

This is a review lecture — the third of three consecutive sessions on local excitation, global
inhibition (LEGI) — and it is explicit about being one: it re-runs the Turing–Gierer–Meinhardt
(TGM) reaction–diffusion model from the start, re-derives its unique homogeneous steady state,
redoes the linear-stability calculation that decides whether that steady state survives a
spatially *uniform* disturbance, and then sets up the calculation for a spatially *varying* one.
It assumes the reader already has the activator/inhibitor kinetics and their biological motivation
— autocatalytic local excitation, a fast-diffusing global inhibitor — from the two lectures that
came before. What it adds, rather than a new step of algebra, is a picture: a plotted curve of how
fast a spatial disturbance of a given wavelength grows, which is the payoff the whole stability
calculation across the three lectures has been aimed at.

## The model, recapped

The TGM equations for an activator concentration $a$ and an inhibitor concentration $i$, both
functions of position $x$ and time $t$:

$$\frac{\partial a}{\partial t} = r_a + k_a \frac{a^2}{i} - \gamma_a a + D_a \frac{\partial^2 a}{\partial x^2}$$

$$\frac{\partial i}{\partial t} = k_i a^2 - \gamma_i i + D_i \frac{\partial^2 i}{\partial x^2}$$

| symbol | meaning |
|---|---|
| $a$, $i$ | activator, inhibitor concentration |
| $t$, $x$ | time, position |
| $r_a$ | basal activator synthesis rate |
| $k_a$, $k_i$ | rate constants for synthesis |
| $\gamma_a$, $\gamma_i$ | decay rates |
| $D_a$, $D_i$ | diffusion constants |

The term that makes the activator "local excitation" is $k_a a^2/i$: activator production is
autocatalytic (quadratic in $a$) but is throttled by the inhibitor sitting in the denominator.
The inhibitor is produced in proportion to $a^2$ with no such throttling, and — in the regime the
lecture is about — diffuses fast enough to act as a roughly global signal.

Choosing dimensionless variables absorbs the seven rate and diffusion constants above into three
dimensionless groups, here called $R$, $Q$, $P$, and rescales $a,i,t,x$ into $A,I,\tau,s$:

$$\frac{\partial A}{\partial \tau} = 1 + R\frac{A^2}{I} - A + \frac{\partial^2 A}{\partial s^2}$$

$$\frac{\partial I}{\partial \tau} = Q\left(A^2 - I\right) + P\frac{\partial^2 I}{\partial s^2}$$

(The source does not give $R$, $Q$, $P$ in terms of the original seven constants — only that the
rescaling produces them — so that bookkeeping is left as a pointer to the original lecture, not
reconstructed here.)

## The homogeneous steady state

Setting $\partial/\partial s = \partial/\partial \tau = 0$ asks for a state that is uniform in
space and constant in time. The second equation gives $A^2 = I$ directly (for $Q \neq 0$).
Substituting into the first,

$$0 = 1 + R\frac{A^2}{A^2} - A = 1 + R - A,$$

so

$$\bar{A} = R+1, \qquad \bar{I} = (R+1)^2.$$

This is the only fixed point with $A, I > 0$ — the only one with a biological reading, since a
concentration cannot be negative — which is why the lecture calls it *the* homogeneous solution
rather than one of several.

## Is it stable to a uniform disturbance?

Linearising the two nondimensional ODEs (dropping the diffusion terms, i.e. asking only whether a
disturbance that is the same everywhere in space grows or decays) gives the Jacobian at
$(\bar A,\bar I)$:

$$J = \begin{pmatrix} \dfrac{2R\bar A}{\bar I} - 1 & -\dfrac{R\bar A^2}{\bar I^2} \\[4pt] 2\bar A Q & -Q \end{pmatrix} = \begin{pmatrix} \dfrac{R-1}{R+1} & -\dfrac{R}{(R+1)^2} \\[4pt] 2(R+1)Q & -Q \end{pmatrix}.$$

Both entries follow from differentiating $1+RA^2/I-A$ and $Q(A^2-I)$ and substituting
$\bar A=R+1,\bar I=(R+1)^2$ — the algebra that turns the general entries in the left-hand matrix
into the specific ones on the right.

For a $2\times 2$ system, the fixed point is stable exactly when the trace is negative and the
determinant is positive — the specialisation, for two dimensions, of the general rule that every
eigenvalue of the Jacobian must have negative real part. Here:

$$\operatorname{tr} J = \frac{R-1}{R+1} - Q, \qquad \det J = Q,$$

(the determinant simplifies to $Q$ once the $\frac{R-1}{R+1}$ and $\frac{2R}{R+1}$ pieces are
combined), so stability to a *uniform* perturbation requires

$$Q > \frac{R-1}{R+1} \qquad \text{and} \qquad Q > 0.$$

## Allowing a spatial disturbance

The diffusion terms were dropped to ask the question above; putting them back asks whether the
same steady state survives a disturbance that varies with position. Write

$$A(s,\tau) = \bar A + A'(s,\tau), \qquad I(s,\tau) = \bar I + I'(s,\tau),$$

and linearise. The result is a linear system for the perturbations themselves, now carrying the
diffusion terms:

$$\frac{\partial A'}{\partial \tau} = \frac{R-1}{R+1}A' - \frac{R}{(1+R)^2}I' + \frac{\partial^2 A'}{\partial s^2}$$

$$\frac{\partial I'}{\partial \tau} = 2Q(1+R)A' - QI' + P\frac{\partial^2 I'}{\partial s^2}$$

The trial solution the lecture proposes separates space and time, putting all the spatial
dependence into a single cosine of wavelength set by $\ell$:

$$A'(s,\tau) = \hat A(\tau)\cos\!\left(\frac{s}{\ell}\right), \qquad I'(s,\tau) = \hat I(\tau)\cos\!\left(\frac{s}{\ell}\right).$$

Substituting turns the two linear PDEs above into two linear *ODEs* for the amplitudes
$\hat A(\tau)$ and $\hat I(\tau)$, with a coefficient matrix that depends on $\ell$ — so each choice
of wavelength $\ell$ (equivalently, wavenumber $k = 1/\ell$) gives its own $2\times 2$ stability
problem, of exactly the same trace-and-determinant kind as the uniform case above, but now with an
answer that can depend on $k$. This is the point at which the reconstructed source breaks off
mid-equation; the algebra that would give the resulting ODEs and their eigenvalues in closed form
is not recoverable from it. What is recoverable is the qualitative answer, in the form of a figure.

## The dispersion relation

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Growth rate of a spatial perturbation plotted against its wavenumber, showing a band of amplified wavelengths flanked by decay">
  <line x1="40" y1="140" x2="300" y2="140" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="20" x2="40" y2="205" stroke="currentColor" stroke-width="1"/>
  <path d="M40,140 C70,110 110,95 170,100 C210,108 215,130 217,140 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <path d="M40,140 C70,110 110,95 170,100 C210,108 215,130 217,140" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M217,140 C230,168 255,190 287,202" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="217" y1="140" x2="217" y2="205" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="217" y="216" text-anchor="middle" font-size="11" fill="currentColor">k*</text>
  <text x="42" y="15" font-size="12" fill="currentColor">growth rate</text>
  <text x="298" y="152" text-anchor="end" font-size="12" fill="currentColor">wavenumber k</text>
  <text x="95" y="88" font-size="11" fill="currentColor">amplified band</text>
  <text x="245" y="186" font-size="11" fill="currentColor">decays</text>
</svg>
<figcaption>The lecture's own growth-rate-versus-wavenumber curve (the source gives no axis
labels beyond this shape). The growth rate is zero at $k=0$ — the spatially uniform mode, whose
fate was decided above — positive over a band of intermediate wavenumbers, which grow, and
negative beyond a cutoff $k^*$, where a disturbance of that wavelength decays. This is the
dispersion relation that the trial-solution calculation was set up to produce.</figcaption>
</figure>

Read against the uniform-perturbation result, the shape of this curve is the whole point of the
three-lecture sequence: a steady state can satisfy $Q > \frac{R-1}{R+1}$ — stable against a
disturbance that is the same everywhere — and still be unstable against a disturbance of the right
wavelength, once the diffusion terms $\partial^2/\partial s^2$ are allowed to act. Local excitation
that would otherwise run away uniformly is instead organised into a pattern with a preferred
wavelength: the one at the peak of the curve, where the growth rate is largest.

## Sources

Slides only: `lectures/17-notes.md`, MIT OCW 8.591J *Systems Biology* (Fall 2004), lecture 17 —
titled "Review" in the original. No transcript, no separate notes and no exercise set were
supplied for this lecture. The equations above (the TGM model, its nondimensionalisation, the
homogeneous fixed point, both stability calculations, and the trial-solution ansatz) are all in
that file; the algebraic step that would follow the trial solution — the resulting ODEs for
$\hat A,\hat I$ and their eigenvalues as a function of $\ell$ — is not, because the source's own
reconstruction from the original PDF (which has no extractable text layer) breaks off mid-equation
right after the ansatz is stated. The dispersion-relation figure is the one image recovered from
that same file (`17-notes/figures/p025-1.jpeg`, page 25 of the original), read directly rather than
reconstructed. There genuinely is very little independent material in this lecture: as a review,
it mostly restates the model and the first stability argument, and the one thing it adds beyond
lecture 16 — the completed wavelength-dependent stability calculation — is exactly the part the
conversion did not recover. The definitions of $R$, $Q$, $P$ in terms of the original rate and
diffusion constants are referred to but not given in the source and are not reconstructed here.

---

[← 12. Stability of the Homogeneous Solution](12-stability-of-the-homogeneous-solution.md) · [Contents](index.md) · [14. Alternative views on gradient sensing →](14-alternative-views-on-gradient-sensing.md)
