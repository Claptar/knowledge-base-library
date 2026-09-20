---
title: "6. Fluctuating and Interacting Polymers"
course: "MIT 8.592J"
chapter: 6
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 6. Fluctuating and Interacting Polymers

## What this covers

This chapter asks how a long, flexible molecule — DNA, a protein, a synthetic homopolymer —
turns local, bond-scale flexibility into large-scale statistical behaviour: how far along its
backbone does a polymer "remember" which way it was pointing, how big is its typical
end-to-end size, why does stretching it feel like compressing a spring, and what happens once
monomers are allowed to interact with each other and with the solvent around them. It assumes
comfort with the Boltzmann distribution and partition functions, with random-walk statistics and
the central limit theorem, and with the idea (from earlier in the course) that an effective
potential between two solute particles can be obtained by integrating out the solvent.

## Homopolymers as statistical objects

The molecules of life — DNA, RNA, proteins — are *hetero-polymers*: sequences of different
monomer types (nucleic acids, amino acids) joined by covalent bonds. A *homo-polymer* repeats a
single monomer $N$ times, as in polyethylene, $|-\text{CH}_2-|_N$. The number of repeat units, the
*degree of polymerization*, ranges from a few hundred for proteins, through $10^4$–$10^5$ for
polyethylene, up to $10^9$ for some DNA.

The covalent bonds along the backbone are strong and do not break at room temperature, but
successive monomers can bend and rotate relative to one another. That freedom is what makes a
polymer a genuinely statistical object: with $N$ large, the number of accessible configurations is
enormous, and a single configuration tells you almost nothing — averages and fluctuations are the
right language. One general fact sets the frame for what follows: at high enough temperature every
polymer is swollen, since entropy — the sheer number of extended configurations — dominates
whatever weak interactions favour compact shapes, and the fact that a real chain is a *sequence* of
different monomers stops mattering. That is why it makes sense to start with a homopolymer's
fluctuations before asking what interactions and sequence do.

## Local flexibility: rotational isomers and the persistence length

Look first at a single joint in the backbone. In polyethylene, a carbon–carbon bond can sit in a
low-energy *trans* conformation, keeping successive bonds roughly parallel, or in one of two
higher-energy *gauche* conformations, which bend the chain by an angle of $2\pi/3$. If the energy
gap between trans and gauche is $\Delta$, the Boltzmann weights give

$$\frac{\text{prob.}(g)}{\text{prob.}(t)} = 2e^{-\beta\Delta}, \qquad \beta = \frac{1}{k_BT}.$$

For $(\text{CH}_2)_N$ the gap is small — about 500 cal/mole, or roughly $\tfrac13 k_BT$ — so the
chain is very flexible at room temperature. Stiffer polymers have $\Delta \gg k_BT$, and the two
gauche states are individually rare:

$$p(g_+) = p(g_-) = \frac{e^{-\beta\Delta}}{1+2e^{-\beta\Delta}}.$$

A typical configuration is then a long, nearly straight trans run, interrupted occasionally by a
kink. The probability of an uninterrupted run of $n$ trans bonds is $p_t^n(1-p_t)$, with
$p_t = 1-2p(g)$ the probability of a trans bond, and this survival probability decays over a
characteristic run length

$$\langle n\rangle = -\frac{1}{\ln p_t} = \big[\ln(1+2e^{-\beta\Delta})\big]^{-1}. \qquad (2.28)$$

The length of these straight runs, $\langle n\rangle a$ with $a$ the bond length, is the seed of a
more general idea: the *persistence length*, which measures how far along the chain the
*direction* of the backbone survives.

To make that precise, write the backbone as a set of bond vectors $\vec t_1,\dots,\vec t_N$ with
$\vec t_i\cdot\vec t_i = a^2$, and suppose a gauche kink bends the bond by an angle $\phi$. The
correlation between neighbouring bonds is

$$\langle \vec t_1\cdot\vec t_2\rangle = a^2\,\frac{1+2\cos\phi\, e^{-\beta\Delta}}{1+2e^{-\beta\Delta}}
\;\approx\; a^2\exp\!\big[-2(1-\cos\phi)e^{-\beta\Delta}\big],$$

the last step valid when $\beta\Delta\gg1$, so a gauche kink is rare. Keeping only configurations
with a single gauche kink somewhere between them, the correlation between bonds $n$ apart is,
to the same order,

$$\langle \vec t_1\cdot\vec t_{n+1}\rangle \approx a^2\exp\!\big[-2n(1-\cos\phi)e^{-\beta\Delta}\big].$$

So the loss of orientation is exponential in the contour length $\ell = na$, decaying as
$e^{-\ell/\xi_p}$ with

$$\xi_p \approx \frac{a\,e^{\beta\Delta}}{2(1-\cos\phi)}. \qquad (2.29)$$

The persistence length grows exponentially with the kink energy $\Delta$: a chain that resists
bending much more strongly than $k_BT$ forgets its orientation only after a very long contour
length.

## From bond angles to a continuum: the worm-like chain

For a stiff polymer like double-stranded DNA, a *discrete* kink of a fixed angle costs far too
much energy to occur; instead the direction drifts through the accumulation of many small bends,
one per monomer. A convenient continuous model of this is the energy

$$\mathcal H = -J\sum_{i=1}^{N-1}\vec t_i\cdot\vec t_{i+1}, \qquad (2.30)$$

which rewards alignment of neighbouring bond vectors, much like a ferromagnetic chain of unit
spins. Because a typical configuration changes direction slowly, it pays to pass to a continuum
description: replace the discrete index $i$ by the arc length $s\in[0,L=Na]$, and use
$(\vec t_i-\vec t_{i+1})^2 = 2-2\,\vec t_i\cdot\vec t_{i+1}$ to rewrite the energy, up to the
constant ground-state term, as

$$\mathcal H \approx -JN + \frac{\kappa}{2}\int_0^L ds\left(\frac{d\vec t}{ds}\right)^2, \qquad (2.31)$$

with bending rigidity $\kappa = J/a$. (Since $|d\vec t/ds| = 1/R(s)$ for the local radius of
curvature $R(s)$, this is exactly the elastic energy of a bent rod.) Dropping the constant and
writing the energy in dimensionless form,

$$\beta\mathcal H = -\frac{\xi_p}{2}\int_0^L ds\left(\frac{d\vec t}{ds}\right)^2, \qquad \beta\kappa = \xi_p, \qquad (2.32)$$

anticipates that the same length, $\xi_p$, controls both the bending stiffness and the decay of
orientation. That identification can be made exact: for the discrete model (2.30), a
transfer-matrix calculation gives

$$\langle \vec t_m\cdot\vec t_n\rangle \approx \left(\coth(\beta J) - \frac1{\beta J}\right)^{|m-n|}
\quad\text{for } |m-n|\gg1, \qquad (2.33)$$

which in the continuum limit becomes the same exponential decay as before,

$$\langle \vec t(s)\cdot\vec t(s+\ell)\rangle \approx e^{-\ell/\xi_p}, \qquad \xi_p\approx\beta\kappa \ \ (\beta J\gg1). \qquad (2.34)$$

This *worm-like chain* is the standard model of double-stranded DNA, whose persistence length is
in the range $\xi_p \approx 50$–$100$ nm.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="A wiggly curve representing a polymer backbone, with tangent vectors marked at two points a distance ell apart along the arc">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <polygon points="0,0 10,5 0,10" fill="currentColor"/>
    </marker>
  </defs>
  <path d="M20,110 C60,70 90,150 130,110 C170,70 200,150 240,100 C270,65 300,130 330,95 C350,75 365,100 380,90"
        fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="130" y1="110" x2="158" y2="80" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="330" y1="95" x2="354" y2="68" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="160" y="75" font-size="12" fill="currentColor">t(s)</text>
  <text x="300" y="60" font-size="12" fill="currentColor">t(s+ell)</text>
  <line x1="130" y1="130" x2="130" y2="192" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="330" y1="130" x2="330" y2="192" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="130" y1="188" x2="330" y2="188" stroke="currentColor" stroke-width="1.5"/>
  <text x="230" y="206" text-anchor="middle" font-size="12" fill="currentColor">arc length ell</text>
</svg>
<figcaption>The worm-like chain treats the backbone as a smooth curve with a unit tangent vector
t(s) at each arc-length position s. The direction drifts as s advances, and the correlation
between two tangents a distance ell apart decays like exp(-ell / xi_p): xi_p is the arc length
over which the chain still "remembers" which way it was pointing.</figcaption>
</figure>

## Entropic elasticity: the size and stiffness of a random coil

Zoom out from individual bonds to the whole chain, and ask about its *end-to-end vector*,

$$\vec R = \vec t_1+\vec t_2+\cdots+\vec t_N = \sum_{i=1}^N \vec t_i.$$

Rotational symmetry — there is no energetic cost to rotating the whole polymer — gives
$\langle\vec R\rangle = 0$, so the interesting quantity is the variance:

$$\langle R^2\rangle = \sum_{i,j=1}^N\langle\vec t_i\cdot\vec t_j\rangle = Na^2 + 2\sum_{i<j}\langle\vec t_i\cdot\vec t_j\rangle. \qquad (2.35)$$

Approximating the bond correlation as a pure exponential in the monomer separation (only
asymptotically exact, but sufficient here),

$$\langle\vec t_i\cdot\vec t_j\rangle = a^2 e^{-a|i-j|/\xi_p}, \qquad (2.36)$$

and using that there are $(N-k)$ pairs at every separation $k$,

$$\langle R^2\rangle = Na^2 + 2a^2\sum_{k=1}^N (N-k)e^{-ak/\xi_p}. \qquad (2.37)$$

Summing the geometric series and keeping, for $N\gg1$, only the term proportional to $N$,

$$\langle R^2\rangle = Na^2\coth\!\left(\frac{a}{2\xi_p}\right) \approx 2Na\xi_p = (2\xi_p)^2\left(\frac{Na}{2\xi_p}\right), \qquad (2.38)$$

the last approximations relying on $\xi_p\gg a$. Read the final form as a statement about
*effective* degrees of freedom: it is the same variance you would get from $N_K \equiv Na/(2\xi_p)$
completely independent, freely-jointed rods of length $2\xi_p$ — the *Kuhn length*. All of the
microscopic bookkeeping about bond angles and persistence length collapses into this one number,
$N_K$, the number of statistically independent segments; it, not the chemical degree of
polymerization $N$, is what governs how many configurations the chain can explore. Because
correlations between separate Kuhn segments are weak, for $N_K\gg1$ the central limit theorem
applies to $\vec R$ as a sum of near-independent pieces, giving a Gaussian end-to-end distribution

$$p(\vec R) = \left(\frac{3}{2\pi\langle R^2\rangle}\right)^{3/2}\exp\!\left[-\frac{3R^2}{2\langle R^2\rangle}\right]
= \frac{1}{(4\pi Na\xi_p/3)^{3/2}}\exp\!\left[-\frac{3R^2}{4Na\xi_p}\right]. \qquad (2.40)$$

This Gaussian has exactly the shape of a Boltzmann weight for a Hookean spring joining the two
ends of the chain, $\propto \exp[-\beta\cdot\tfrac12 J_{\text{polymer}}R^2]$. Matching exponents
identifies the spring constant:

$$J_{\text{polymer}} = \frac{3k_BT}{\langle R^2\rangle} = \frac{3k_BT}{2Na\xi_p}. \qquad (2.41)$$

There is no literal spring anywhere in the model — pulling the ends apart does not stretch any
bond. What resists the pulling is pure entropy: stretching the chain removes configurations, and
the resulting free-energy cost happens to be quadratic in $R$, exactly like an elastic bond. The
formula for $J_{\text{polymer}}$ makes the entropic character explicit: it is *proportional* to
temperature, the opposite of an ordinary mechanical spring, because the restoring force is bigger
whenever there is more thermal energy available to explore configurations.

## Beyond ideal chains: excluded volume and solvent quality

Everything so far came from the flexibility of the covalent bonds joining *adjacent* monomers. Real
monomers also interact with each other — and with the solvent — no matter how far apart they sit
along the backbone, typically through hydrogen bonds; it is exactly such interactions, competing
against thermal fluctuations, that let a protein fold into a specific shape rather than exploring
every configuration a bare flexible chain would.

The simplest setting for this competition is a chain confined to a lattice. Random walks on a
square lattice that never immediately step back to where they came from number about $3^N$ after
$N$ steps. A first, purely geometric consequence of monomer-monomer interaction is that two
monomers simply cannot occupy the same site: the *excluded volume* constraint prunes these walks
down to *self-avoiding walks*, whose count still grows exponentially, as $g^N$, but with $g<3$
(numerically $g\approx2.64$).

Energetics can be layered on top of this by counting nearest-neighbour contacts of three kinds —
monomer–monomer, monomer–solvent, solvent–solvent — with energies $\epsilon_{mm}$,
$\epsilon_{ms}$, $\epsilon_{ss}$ and multiplicities $N_{mm}$, $N_{ms}$, $N_{ss}$:

$$E = \epsilon_{mm}N_{mm} + \epsilon_{ms}N_{ms} + \epsilon_{ss}N_{ss}.$$

Bringing two previously separated monomers into contact removes two monomer–solvent contacts and
creates one monomer–monomer and one solvent–solvent contact, changing the energy by
$\delta\epsilon = \epsilon_{mm}+\epsilon_{ss}-2\epsilon_{ms}$. The tendency of monomers to
aggregate is captured by the dimensionless *Flory–Huggins parameter*

$$\chi \equiv -\frac{\beta}{2}\delta\epsilon = \beta\left(\epsilon_{ms} - \frac{\epsilon_{mm}+\epsilon_{ss}}{2}\right). \qquad (2.42)$$

Negative $\chi$ favours monomers staying apart, dissolved among solvent molecules; positive $\chi$
favours monomers aggregating with each other.

Real interactions vary continuously with separation and orientation rather than living on a
lattice: hydrogen bonding is strongly orientation-dependent, while van der Waals attraction depends
mainly on separation. As with the effective potential between two solutes obtained earlier in the
course by integrating out solvent degrees of freedom, an effective potential $\mathcal V(r)$
between two monomers can in principle be built the same way. When the monomers are larger than the
solvent molecules, this effective potential generically has a hard repulsive core at short range
and an attractive tail at longer range. A weak net potential describes a *good solvent*, in which
the chain stays swollen; a strongly attractive one describes a *bad solvent*, which favours
monomers collapsing onto each other. Because the balance is set partly by the solvent's own
entropy, solvent quality typically shifts toward "good" as temperature rises.

## A mean-field free energy for an interacting homopolymer

To decide whether an interacting homopolymer is swollen or collapsed at a given temperature
requires its free energy — the partition function of chain plus solvent — and computing that
exactly is hard even for the toy models above. A tractable route is a variational mean-field
estimate: assume the polymer's typical configurations occupy a ball of some radius $R$, treated as
a variational parameter, and build an approximate partition function for $N$ monomers confined to
that ball out of three pieces.

$$Z(N,R) \approx g^N \times \frac{\exp\!\left(-\dfrac{3R^2}{4Na\xi_p}\right)}{(4\pi Na\xi_p/3)^{3/2}}
\times\Big\{[1-(a/R)^3][1-2(a/R)^3]\cdots[1-(N-1)(a/R)^3]\Big\}\times e^{-\beta E_{\text{att.}}}. \qquad (2.43)$$

The first factor, $g^N$, is the exponential growth in configurations of an unconstrained flexible
chain — its precise value will not matter below. The Gaussian factor is exactly the end-to-end
distribution (2.40), reused here as the entropic cost of squeezing the chain's natural random-coil
size down to a ball of radius $R$: it behaves like the Hookean spring found above. The product in
braces is the reduction in available configurations from excluded volume, built up one monomer at
a time: the first monomer has the whole volume $V\sim R^3$ available, the second has a fraction
$(a/R)^3$ of it excluded by the first, the third has a fraction excluded by both already placed,
and so on. Taking the log of that product and expanding,

$$\delta\ln Z_{EV} = \sum_{i=1}^{N-1}\ln\!\left[1-i\left(\frac aR\right)^3\right]
\approx -\left(\frac aR\right)^3\sum_i i - \frac12\left(\frac aR\right)^6\sum_i i^2 - \cdots
\approx -\frac{N^2}{2}\left(\frac aR\right)^3 - \frac{N^3}{6}\left(\frac aR\right)^6 - \cdots, \qquad (2.44)$$

a leading term scaling as $N^2$, as expected of an effect built from pairwise overlaps.

The attractive part is treated in the same mean-field spirit. For a homopolymer, summing the
pairwise potential and replacing the sum by an integral over a smooth density $n(\vec r)$,

$$E_{\text{att.}} = \frac12\sum_{i\neq j}\mathcal V(\vec r_i-\vec r_j)
= \frac12\int d^3\vec r\, d^3\vec r'\, n(\vec r)n(\vec r')\,\mathcal V(\vec r-\vec r'). \qquad (2.45)$$

Taking the density uniform inside the confining ball, $n=N/V$ with $V=\tfrac{4}{3}\pi R^3$, and
integrating over the centre of mass of each pair (ignoring surface effects) gives

$$E_{\text{att.}} = \frac{n^2}{2}V\int_a d^3\vec r\,\mathcal V(\vec r), \qquad (2.46)$$

the integral excluding the short-range hard core. Packaging the strength of the attraction into the
same dimensionless $\chi$ as before, via

$$\int_a d^3\vec r\,\mathcal V(\vec r) \equiv -\frac{4\pi}{3}a^3\,k_BT\,(2\chi), \qquad (2.47)$$

turns the attractive-energy term into

$$-\beta E_{\text{att.}} = N^2\left(\frac aR\right)^3\chi. \qquad (2.48)$$

Collecting the entropic, excluded-volume, and attractive pieces gives one free energy, a function
of the variational size $R$ for fixed chain length $N$:

$$\ln Z(N,R) = N\ln g - \frac32\ln\!\left[\frac{4\pi Na\xi_p}{3}\right] - \frac{3R^2}{4Na\xi_p}
-\frac{N^2}{2}\left(\frac aR\right)^3 - \frac{N^3}{6}\left(\frac aR\right)^6 - \cdots + \chi N^2\left(\frac aR\right)^3. \qquad (2.49)$$

Each term pulls $R$ in a recognisable direction: the elastic term $-3R^2/(4Na\xi_p)$ grows with
$R$ and so penalises stretching the chain out; the excluded-volume terms blow up as $R\to0$ and so
penalise squeezing the monomers together; and the $\chi N^2(a/R)^3$ term favours small $R$ exactly
when $\chi>0$ (a bad solvent), pulling in the opposite direction from excluded volume. Balancing
these competing terms — finding the $R$ that maximizes (2.49) as a function of $N$, $\xi_p$, and
$\chi$ — is what the lecture turns to next, to map out the swollen and collapsed phases of an
interacting homopolymer; that analysis is not part of the material given here.

## Sources

Both sections of this chapter come from the same two-part slide set for MIT 8.592J/HST.452J,
*Statistical Physics in Biology* (Spring 2011): `10-slides.pdf`, reconstructed as
`lectures/10-slides/01-2-2-fluctuating-polymers.md` (course section 2.2, covering rotational
isomers, the worm-like chain, and entropic elasticity) and
`lectures/10-slides/02-2-3-interacting-polymers.md` (course section 2.3 through 2.3.1, covering
excluded volume, the Flory–Huggins parameter, and the mean-field free energy). No transcript,
written notes, or exercise set was supplied for this lecture.

Both source files carry a fidelity warning worth repeating: the original PDF had no extractable
text layer, so the markdown was reconstructed by a model reading the page images, and every
equation in it is unverified against the original. One likely artefact of that reconstruction was
corrected here: the source renders the normalization of equation (2.40) as a product rather than a
quotient, which is inconsistent with the right-hand side the same line gives; the quotient form
used in this chapter is the one consistent with (2.38) and with that right-hand side.

The interacting-polymers slide explicitly refers to "Eq. (2.8)" for the general method of building
an effective potential between two solutes by integrating out solvent degrees of freedom — that
derivation was given earlier in the course and is not part of the material supplied for this
chapter. The mean-field free energy of section 2.3.1 is also explicitly a stepping stone: the
slide ends by noting the result "will next be used to explore the phases of the interacting
homopolymer," an analysis that belongs to a later lecture not included here.

---

[← 5. The Charge Environment of the Cell](05-the-charge-environment-of-the-cell.md) · [Contents](index.md) · [7. Coil-Globule Transition and Folding →](07-coil-globule-transition-and-folding.md)
