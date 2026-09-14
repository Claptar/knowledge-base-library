---
title: 2.1.2 The Poisson–Boltzmann Equation
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2.1.2 The Poisson–Boltzmann Equation

**Source:** `lectures/09-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We know that proteins bind to one another, and that some proteins bind to DNA. In principle, an effective interaction between such macroions can be obtained by holding them at fixed separation (and orientation). A constrained partition function is then evaluated by integrating over all the other degrees of freedom, e.g. the positions of the more mobile counterions, as


In addition to steric constraints (the excluded volume around each atom), the Hamiltonian Hc includes the direct Coulomb interactions between the macroions, their interactions with the counterions, as well as the interactions amongst counterions. The restricted partition function is too hard to compute directly, and we shall instead resort to a “mean-field” approximation in which each counterion is assumed to experience an effective potential φ(⃗r) due to the macroion, as well as all the other counterions. The effective potential is then computed self-consistently.

In this approximation, the position-dependent density of counterion species α adjusts to the potential through the Boltzmann weight, as


Note that n¯α is in general not the particle density, but an overall parameter that needs to be adjusted so that the integral over⃗r leads to the correct number of counterions. The potential φ(⃗r) is in turn determined by the charge distribution, and satisfies the Poisson equation.


The charge density at each point has a contribution from the macroions, and from the

29

(fluctuation averaged) counterion density, and thus


Self-consistency then leads to the Poisson-Boltzmann Equation


This equation, while a drastic simplification of the original problem, is commonly used. It is a non-linear partial differential equation, and exact solutions are available only for a few simple geometries. It does have the virtue of being at least numerically solvable.

---

[← 2.1.1 Charge dissociation in solution](02-2-1-1-charge-dissociation-in-solution.md) · [Up: contents](index.md) · [2.1.3 Debye screening by salt ions →](04-2-1-3-debye-screening-by-salt-ions.md)
