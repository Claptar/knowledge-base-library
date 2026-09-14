---
title: 2.1.3 Debye screening by salt ions
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2.1.3 Debye screening by salt ions

**Source:** `lectures/09-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We expect physically that counterions will accumulate near regions of opposite charge to lower the electrostatic energy. As a result a charged macroion will be surrounded by a cloud of counterions, shielding and reducing its net charge. This effect is easily captured in a linearized version of Eq. (2.12). Linearizing the Boltzmann weight is actually a quite good approximation when the Coulomb interaction between macroions is screened by a high concentration of salt ions. The first step is to expand the exponential such that the local counterion charge density is


We note that at this order the local variations in counterion charge density and potential are simply proportional. Since the salt ions are overall neutral, we can then identify n¯α with the overall particle density of species α at this order. The condition of charge neutrality, �α<sup>zαn¯α= 0,thenleadsto</sup>


where


This is the Debye-H¨uckel equation, and the parameter λ is the Debye screening length. In a typical biological environment λ is around 1nm.

For the case of a point charge Q = ze, i.e. for


30

the solution is the exponentially damped version of the Coulomb potential


Since Eq. (2.14) is linear, its solution for a general distribution of charges is obtained by simple superposition, leading to the interaction energy

---

[← 2.1.2 The Poisson–Boltzmann Equation](03-2-1-2-the-poisson-boltzmann-equation.md) · [Up: contents](index.md) · [2.1.4 Dissociation from a plate →](05-2-1-4-dissociation-from-a-plate.md)
