---
title: 2.1.4 Dissociation from a plate
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2.1.4 Dissociation from a plate

**Source:** `lectures/09-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let us now consider the full Poisson–Boltzmann equation for the simple geometry of a flat plate, e.g. describing a membrane. Upon dissociation the membrane is negatively charged; its charge density denoted by σ = −e/d<sup>2</sup> (i.e. ignoring discreteness effects, the negative charges are on average a distance d apart). The neutralizing counterions, of charge +e are present in the solution on both sides of the membrane. Due to translational symmetry, the average charge density (and potential) only depend on the separation from the plate, indicated by the coordinate y, and Eq. (2.12) now reads


The following trick allows us to guess the solution to Eq. (2.19). We first make a transformation to


such that


Multiplying both sides by W<sup>2</sup> , Eq. (2.19) can be recast as


While still non-linear, it is easy to see that a linear function of y satisfies the above equation, and we set


where we have arbitrarily set φ(y → 0) = 0, such that W (0) = 1, and y0<sup>−2</sup> = 2πβe<sup>2</sup> n/ǫ¯ . Note, however that n¯ is simply a parameter that needs to be set by the requirement of charge neutrality. It is easier to trade in this parameter for y0 and constrain the latter. The electrostatic potential thus has the form


The undetermined length y0, clearly sets the scale at which the counterion density changes significantly. It can be determined by examining the limit y ≪ y0, for which Eq. (2.23) becomes


Indeed, at distances close enough to the surface that screening is unimportant, we expect the electric field to be (e.g. by appealing to a Gaussian pillbox)


and a corresponding potential


Comparing this result with Eq. (2.24) indicates that


This characteristic scale is known as the Guoy-Chapman length, characterizing the thickness of the “diffusive boundary layer” of ions that shields a charged membrane.

Retracing the steps of algebra, it is easy to check that


and


At large separations, y ≫ y0 from the plate, the counterion density falls off as (2πlBy<sup>2</sup> )<sup>−1</sup> . The corresponding potential behaves as φ(y) ≈ 2 ln(y)/(βe), very different from the linear potential in vacuum, and also quite distinct from an exponential decay that may have been surmised based on Debye-Huckel screening. Clearly this type of screening will lead to a quite

32

different interaction between charged plates, a question that will be taken up in the next problem set. In connection to that, we note that Eq. (2.21) also admits solutions of the form cos(y/y1 + θ) with parameters y1 and θ that can be adjusted to conform to the boundary conditions corresponding to parallel charged plates.

While the solutions to the Poisson-Boltzmann equation are interesting and informative, they do not capture the entire physics of the problem. Fluctuations in charge density can be important in lowering the free energy. Indeed at high temperatures the correlated fluctuations around two similarly charged macroions further reduce the repulsion through a dipole-dipole interaction reminiscent of the van der Waals force. If strong enough these fluctuations can entirely reverse the sign of the force, leading to an attractive interaction between like-charged macroions. Such phenomena, not captured by the Poisson-Boltzmann equation, have received considerable attention in recent years.

33

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 2.1.3 Debye screening by salt ions](04-2-1-3-debye-screening-by-salt-ions.md) · [Up: contents](index.md)
