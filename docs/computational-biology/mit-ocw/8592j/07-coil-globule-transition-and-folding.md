---
title: "7. Coil-Globule Transition and Folding"
course: "MIT 8.592J"
chapter: 7
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 7. Coil-Globule Transition and Folding

## What this covers

This chapter finishes what the previous one set up: a mean-field trial free energy for a polymer
interacting with itself and its solvent (Eq. 2.49). It asks what shape that free energy predicts in
a good solvent versus a bad one, and then pushes further — once the polymer is a *heteropolymer*
with many chemically distinct monomers, like a protein, can it freeze into one preferred compact
shape? Answering that needs a new tool, the random energy model, and a "designed" version of it
that resolves a real puzzle: the plain model predicts folding as slow as glass formation, while
real proteins fold fast. Assumes the entropic-elasticity result for an ideal chain, the
excluded-volume expansion, and the Flory–Huggins parameter $\chi$, all from the previous chapter's
construction of $\ln Z(N,R)$.

## Where the last chapter left off

The trial free energy for $N$ monomers of size $a$ and persistence length $\xi_p$ confined to a
sphere of radius $R$ was (Eq. 2.49)

$$\ln Z(N,R) = N\ln g - \frac32\ln\!\Big[\frac{4\pi Na\xi_p}{3}\Big] - \frac{3R^2}{4Na\xi_p} - \frac{N^2}{2}\Big(\frac aR\Big)^3 - \frac{N^3}{6}\Big(\frac aR\Big)^6 - \cdots + \chi N^2\Big(\frac aR\Big)^3,$$

where $g$ sets the growth rate of the number of configurations of the free chain and $\chi$ is the
Flory–Huggins parameter: positive $\chi$ favours monomer–monomer contact over monomer–solvent
contact. Every term here has a definite sign except one combination: the excluded-volume repulsion
and the $\chi$-driven attraction sit inside the same power of $(a/R)$ and combine as
$-\tfrac12(1-2\chi)N^2(a/R)^3$. Repulsion and attraction compete inside this single term, and its
sign — set by whether $\chi$ is above or below $1/2$ — decides between two qualitatively different
equilibrium shapes. That competition is the subject of this chapter.

## Good solvent: the swollen coil

For $\chi<1/2$ the repulsive part dominates, and the only thing opposing indefinite swelling is the
entropic cost of stretching, the spring term $-3R^2/(4Na\xi_p)$. Keeping just these two competing
terms — one can check afterwards that the terms dropped really are smaller in this regime — gives

$$\ln Z(N,R) = \text{const} - \frac{3R^2}{4Na\xi_p} - \frac{1-2\chi}{2}N^2\Big(\frac aR\Big)^3 + \cdots \tag{2.50}$$

Extremising over $R$,

$$\frac{\partial\ln Z}{\partial R} = -\frac{3R}{2Na\xi_p} + \frac{3(1-2\chi)}{2}N^2\frac{a^3}{R^4} = 0 \;\Longrightarrow\; \overline R^{\,5} = (1-2\chi)a^4\xi_pN^3,$$

$$\overline R = (1-2\chi)^{1/5}(a^4\xi_p)^{1/5}N^{3/5}. \tag{2.51}$$

Compare this with the non-interacting chain, where $\overline{R^2}\approx 2Na\xi_p$, i.e.
$\overline R\propto N^{1/2}$ (previous chapter, Eq. 2.39). Excluded volume does not just rescale the
prefactor — it changes the *exponent*. Writing $R\propto N^\nu$, the ideal chain has $\nu=1/2$; the
swollen, self-avoiding coil has $\nu=3/5$ in this variational treatment, the **Flory exponent**. A
larger exponent means each added monomer buys more volume: a self-avoiding chain fills space more
generously than a random walk that is free to cross itself.

Going beyond this mean-field argument is genuinely hard, but one of the successes of
renormalization group theory is an essentially exact value, $\nu = 0.591\ldots$, remarkably close
to the crude variational estimate of $3/5$.

### The exponent in other dimensions

The same extremisation goes through for a self-avoiding walk confined to $d$ spatial dimensions —
e.g. a polymer stuck to a $d=2$ surface — dropping the attractive part of the interaction and
keeping only the repulsive core. The free energy of Eq. (2.50) generalises to

$$\ln Z(N,R) = \text{const} - \frac{dR^2}{4Na\xi_p} - \frac{N^2}{2}\Big(\frac aR\Big)^d, \tag{2.52}$$

and extremising exactly as before gives

$$\overline R = \big(a^{d+1}\xi_p\big)^{\frac1{d+2}}N^{\frac3{d+2}}, \qquad \nu_F(d) = \frac{3}{d+2}. \tag{2.53}$$

This generalised Flory exponent is *exact* at $d=1,2,4$, giving $\nu=1,\,3/4,\,1/2$ respectively —
an unusual case of a mean-field estimate landing exactly right outside its naive regime of
validity. Above four dimensions the excluded-volume constraint stops mattering altogether and $\nu$
stays pinned at the ideal-chain value $1/2$: in high enough dimension two strands of the same walk
essentially never meet anyway.

## Bad solvent: collapse at the theta point

Lowering the temperature typically increases $\chi(T)$ — the solvent loses less by staying pure
than the monomers gain by aggregating. The sign of $(1-2\chi)$ flips at the **theta point**,
$\chi(\theta)=1/2$, and for $T<\theta$ attraction wins: the polymer collapses into a compact
**globule** with a finite monomer density $\rho = N(a/R)^3$, rather than the vanishing density of
the swollen coil. Keeping terms in $\rho$ to the order needed, the free energy per monomer is

$$-\frac{\ln Z(\rho)}{N} = -\ln g + \frac{1-2\chi}{2}\rho + \frac{\rho^2}{6} + \cdots \tag{2.54}$$

Minimising over $\rho$,

$$-\frac1N\frac{d\ln Z}{d\rho} = \Big(\frac12-\chi\Big) + \frac{\overline\rho}{3} + \cdots = 0 \;\Longrightarrow\; \overline\rho = 3\Big(\chi-\frac12\Big) + \cdots, \tag{2.55}$$

so the equilibrium density grows *linearly* from zero just below the theta temperature (the
higher-order terms in $\rho$ are what eventually saturate this growth, since $\rho$ cannot exceed 1
— a fully packed globule).

The attractive interactions contribute an energy per monomer

$$\frac{E_{\text{att.}}}{N} = -\overline\rho\,\chi\,k_BT, \tag{2.56}$$

using the previous chapter's $-\beta E_{\text{att.}} = \chi N^2(a/R)^3$, and the entropy per monomer
follows from $S = (E-F)/T$:

$$\frac{S}{Nk_B} = \frac{\ln Z}{N} - \overline\rho\,\chi = \ln g + \frac32\Big(\chi-\frac12\Big)^2 + \cdots - \overline\rho\,\chi \;\approx\; \ln g - \frac{\overline\rho}{2} + \mathcal O(\overline\rho^2), \tag{2.57}$$

keeping only the leading term as $\chi\to1/2$. Entropy is reduced, at first linearly, as the
globule condenses — exactly the mean-field picture of a gas condensing into a liquid, where the
liquid retains many configurations, just fewer than the gas did. Cooling an ordinary liquid further
eventually freezes it into a low-entropy solid. That analogy is what motivates the rest of the
chapter: is there a freezing transition for a compact polymer too, and — since a protein is a
*hetero*polymer — can it freeze into one particular shape rather than a disordered solid?

## Compact heteropolymers and the random energy model

Deep in the globular phase, the accessible configurations are the maximally compact ones. On a
lattice these are **Hamiltonian walks** — self-avoiding walks that visit every site, leaving none
empty. Their number also grows exponentially, as $g'^N$, but $g'\ll g$: full compactness is a much
more severe constraint than mere self-avoidance.

For a homopolymer every Hamiltonian walk has the same energy, so all $g'^N$ compact configurations
are equally likely. A heteropolymer — built from chemically distinct monomers, as a protein is from
its amino acids — breaks that symmetry: different folds bring different pairs of monomers into
contact, so different compact configurations $\alpha$ carry different energies,

$$E_\alpha = \sum_{\langle ab\rangle} V_{ab}, \tag{2.58}$$

summed over non-covalent nearest-neighbour contacts, giving a partition function

$$Z = \sum_\alpha e^{-\beta E_\alpha} \tag{2.59}$$

over the $g'^N$ compact states. Real biomolecules combine non-specific attractions that pull all
monomers together (driving the collapse of the previous section) with *specific* interactions that
could in principle select one particular compact shape — the question is whether, and at what
temperature, they actually do.

Summing over $g'^N$ configurations of a fixed, specific sequence is intractable directly. The
**random energy model (REM)** makes it tractable with a drastic simplification: treat the bond
energies $V_{ab}$ as independent random variables. Each $E_\alpha$ is then a sum of
$N_B = (z-1)N$ such terms ($z$ the lattice coordination number, minus the one bond that is
polymeric), so for large $N$ it is approximately Gaussian, with

$$\langle E_\alpha\rangle = N_B\langle V_{ab}\rangle \equiv N\varepsilon_0, \qquad \langle E_\alpha^2\rangle_c = N_B\langle V_{ab}^2\rangle_c \equiv N\sigma^2, \tag{2.60}$$

$$p(E) = \frac{1}{\sqrt{2\pi N\sigma^2}}\exp\Big[-\frac{(E-N\varepsilon_0)^2}{2N\sigma^2}\Big]. \tag{2.61}$$

The REM's key idealisation is treating the energies of *different* configurations as statistically
independent of one another — it throws away any correlation between similar folds — which turns
the counting problem into an extreme-value problem in disguise.

## The REM's entropy, and its glass transition

The density of states is the number of configurations, $g'^N$, times the probability that a given
one lands at energy $E$, so $\Omega(E) = g'^Np(E)$, and the entropy follows:

$$S(E) = k_B\ln\Omega(E) = k_B\Big[N\ln g' - \frac{(E-N\varepsilon_0)^2}{2N\sigma^2}\Big] - \frac{k_B}{2}\ln(2\pi N\sigma^2). \tag{2.62}$$

The last term is sub-extensive and can be dropped. What remains is an inverted parabola in $E$, but
two thermodynamic constraints cut down how much of it is physical:

- **Positive temperature.** $T^{-1} = dS/dE$ must be positive, restricting attention to
  $E < N\varepsilon_0$, the branch below the mean energy.
- **Non-negative entropy.** $S(E)$ cannot go below zero. The parabola would formally go negative
  below some energy; instead the true entropy sticks at $S=0$ for $E<E_c$, where

$$S(E_c) = 0 \;\Longrightarrow\; \frac{E_c}{N} = \varepsilon_0 - \sigma\sqrt{2\ln g'}. \tag{2.63}$$

($E_c$ is exactly the extreme-value answer for the mean of the lowest of $g'^N$ independent draws
from $p(E)$ — the connection to extreme-value statistics referred to, but not re-derived, here.)

Below $E_c$ there are essentially no compact states left in a typical sequence — not a continuum
with small but positive entropy, but a genuine cliff, and a kink in the entropy signals a phase
transition. Its temperature is read off from the slope of the parabola exactly at $E_c$:

$$\frac1{T_c} = \frac{dS}{dE}\Big|_{E_c} = k_B\frac{\sqrt{2\ln g'}}{\sigma} \;\Longrightarrow\; k_BT_c = \frac{\sigma}{\sqrt{2\ln g'}}. \tag{2.64}$$

For $T\le T_c$ the system is confined to the handful of states near $E_c$: a transition into a
**glass** — not a unique ground state, but a small, disordered pool of nearly-degenerate low-energy
configurations that the chain freezes into.

## Why real proteins are not typical random heteropolymers

It is tempting to identify this glass transition with protein folding, but the REM's transition has
the wrong character for that. As $T\to T_c^+$ the number of accessible states collapses drastically,
and the handful of states surviving near $E_c$ have no particular reason to resemble one another —
reaching a different one typically means rearranging many monomers at once, climbing a large energy
barrier in the process. So the REM polymer's kinetics should slow down sharply on approaching
$T_c$, the signature of an ordinary structural glass. Real proteins do the opposite: most fold
quickly and reliably, on laboratory rather than glassy timescales.

The resolution is that proteins are not typical random heteropolymers: evolution has "designed"
real sequences both for function and, apparently, for ease of folding. The REM can mimic this
design with one small addition — alongside the Gaussian continuum of $g'^N$ random compact states,
add a single distinguished state at energy $E_n$, with $E_n < E_c$, representing the native fold.

## Designed REM: the tangent construction

With the native state added, the system has somewhere better than the glass to go: a folding
transition to this state at a temperature $T_f$ that sits *above* $T_c$ — high enough that there
are still many competing states left to explore on the way there, avoiding the glassy kinetics of
the previous section.

$T_f$, and the energy $E_f$ of the competing continuum states right at the transition, are pinned
down by equating the free energy of the native state to that of the continuum. Geometrically this
is a common-tangent construction on the entropy curve: a straight line from the point $(E_n,0)$ (a
single state has zero entropy, $\ln 1 = 0$) drawn tangent to the curve $S(E)$ at $(E_f, S(E_f))$:

$$\beta_f = \frac{S(E_f)/k_B}{E_f - E_n} = \frac{N\ln g' - (E_f - N\varepsilon_0)^2/(2N\sigma^2)}{E_f - E_n}. \tag{2.65}$$

<figure>
<svg viewBox="0 0 400 240" role="img" aria-label="Entropy of the random energy model against energy, with the tangent line from the native state that fixes the folding temperature">
  <defs>
    <marker id="arrow-rem" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="40" y1="200" x2="380" y2="200" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow-rem)"/>
  <line x1="40" y1="200" x2="40" y2="24" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow-rem)"/>
  <text x="384" y="204" font-size="12" fill="currentColor">E</text>
  <text x="28" y="20" font-size="12" fill="currentColor">S</text>

  <path d="M140,200 Q200,40 340,40" fill="none" stroke="currentColor" stroke-width="1.6"/>

  <line x1="70" y1="200" x2="300" y2="16" stroke="currentColor" stroke-width="1.1" stroke-dasharray="5 3"/>

  <circle cx="70" cy="200" r="3.2" fill="currentColor"/>
  <circle cx="140" cy="200" r="3.2" fill="currentColor"/>
  <circle cx="220" cy="80" r="3.2" fill="currentColor"/>

  <text x="60" y="218" font-size="12" fill="currentColor">Eₙ</text>
  <text x="133" y="218" font-size="12" fill="currentColor">Ec</text>
  <text x="226" y="70" font-size="12" fill="currentColor">Ef</text>
  <text x="320" y="218" font-size="12" fill="currentColor">Nε₀</text>
  <text x="238" y="52" font-size="12" fill="currentColor">S(E)</text>
</svg>
<figcaption>The REM entropy is zero for $E<E_c$ and rises as a parabola from $E_c$ to its maximum
at $E=N\varepsilon_0$. Adding one native state at $E_n<E_c$, the line from $(E_n,0)$ tangent to the
curve at $(E_f,S(E_f))$ fixes the folding energy $E_f$ and, through its slope, the folding
temperature $T_f$.</figcaption>
</figure>

To see why this tangent condition is the right one, work in the canonical ensemble. The probability
of finding the system in the native state is

$$p_n = \frac{e^{-\beta E_n}}{Z(\beta)}, \qquad Z(\beta) = e^{-\beta E_n} + \int dE\,\Omega(E)e^{-\beta E}. \tag{2.66}$$

In the thermodynamic limit ($N\to\infty$, with $E_n\propto N$ so the model has a well-defined
extensive limit), the integral is dominated by a single saddle-point energy. That saddle sits above
$E_f$ for $\beta\le\beta_f$ — the continuum wins — and switches to $E=E_n$ for $\beta>\beta_f$ — the
native state wins. The switch is a genuine discontinuity, $p_n$ jumping from 0 to 1, occurring
exactly where the two contributions to $Z$ are equal:

$$e^{-\beta_fE_n} = \Omega(E_f)e^{-\beta_fE_f}, \tag{2.67}$$

which after taking logarithms is precisely the tangent condition, Eq. (2.65).

Solving for $\beta_f$ needs two more relations: the saddle-point energy at inverse temperature
$\beta$, from $dS/dE = k_B\beta$ applied to the parabola, is $E(\beta) = N\varepsilon_0 -
N\sigma^2\beta$, and Eq. (2.64) can be rewritten $\ln g' = (\beta_c\sigma)^2/2$. Writing
$\beta_n \equiv (N\varepsilon_0 - E_n)/(N\sigma^2)$ for the same construction applied formally to
the native energy — the reconstructed slide prints this definition with the opposite sign,
$(E_n - N\varepsilon_0)/(N\sigma^2)$, but only the sign used here is consistent with Eq. (2.64)'s
convention and reproduces Eqs. (2.69)–(2.70) below, which is the check available without a
transcript or the original PDF to compare against — Eq. (2.65) reduces to a quadratic in $\beta_f$
(a rearrangement of Eq. 2.68),

$$\beta_f^2 - 2\beta_n\beta_f + \beta_c^2 = 0 \;\Longrightarrow\; \beta_f = \beta_n - \sqrt{\beta_n^2 - \beta_c^2}, \tag{2.69}$$

and hence

$$\frac{T_f}{T_c} = \frac{\beta_c}{\beta_f} = \frac{\beta_n}{\beta_c} + \sqrt{\Big(\frac{\beta_n}{\beta_c}\Big)^2 - 1}. \tag{2.70}$$

Since $E_n < E_c$ makes $\beta_n>\beta_c$, this ratio is always $\ge 1$: the folding temperature
sits at or above the glass temperature, and the gap between them grows with $\beta_n$ — that is,
with how far below $E_c$ the designed native energy sits. Push the native energy far enough below
the glassy states and folding happens at a comfortably high temperature, where the continuum of
unfolded states is still large and easy to explore, rather than at the sluggish glass transition
itself.

## Sources

- Slides: `lectures/11-slides/01-2-3-2-swollen-coil-polymers-in-good-solvents.md` through
  `04-2-3-5-designed-rem-for-protein-folding.md` (course `computational-biology/mit-ocw/8592j`,
  MIT 8.592J/HST.452J *Statistical Physics in Biology*, Spring 2011, MIT OpenCourseWare), covering
  textbook sections 2.3.2–2.3.5. These files are flagged in the library as reconstructed by a model
  from a PDF with no text layer, with "every equation... unverified" — treat the displayed
  equations here as a pointer back to the original PDF rather than a checked transcription. One
  internal inconsistency was found and resolved by hand: the printed sign of $\beta_n$ in slide
  04's Eq. (2.68) does not reproduce the printed Eqs. (2.69)–(2.70); the opposite sign, used above,
  does.
- Continues directly from the previous chapter's slides (`lectures/10-slides/01-2-2-fluctuating-polymers.md`, `02-2-3-interacting-polymers.md`, same course): the entropic-elasticity
  result $\overline{R^2}\approx 2Na\xi_p$ (Eq. 2.39), the end-to-end distribution (Eq. 2.40), and
  the trial free energy Eq. (2.49) are used here without re-derivation.
- No transcript, written notes, or exercises were supplied for this lecture; nothing in this
  chapter is drawn from spoken commentary, and no exercises are given.
- The slides refer to, but do not contain, "the extreme value problem studied earlier" (in
  connection with Eq. 2.63) and the renormalization-group calculation behind the exact value
  $\nu=0.591\ldots$ of the Flory exponent; neither is part of the supplied material.

---

[← 6. Fluctuating and Interacting Polymers](06-fluctuating-and-interacting-polymers.md) · [Contents](index.md) · [8. The Poland-Scheraga Melting Model →](08-the-poland-scheraga-melting-model.md)
