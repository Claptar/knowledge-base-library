---
title: 3.1.2 Microtubule Growth and Regulation
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/20-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.1.2 Microtubule Growth and Regulation

**Source:** `lectures/20-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

To study the dynamic behavior of a microtubule (MT), we examine a simple two state model:<sup>1</sup> The MT is either slowly growing with velocity v+, or rapidly shrinking with velocity v−. Assuming that one end of the MT is attached to a stationary support at z = 0, the growing (+) end can be at a distance z at time t. With probability p+(z, t) the MT is growing, while with probability p−(z, t) it has lost its GTP cap and is shrinking. There is a probability that a catastrophe occurs, switching from a growing to a shrinking MT, at a rate f+−, while the converse rescue events occur at rate f−+.


The two probability functions evolve according to the coupled equations


For simplicity, we have assumed a continuously variable length z; a more microscopic representation would describe the evolution of p±(n, t) for n tubulin units, with rates for addition/subtraction of units. The above coupled partial differential equations are linear, and hence easily solved by Fourier transforming in space and time. Effectively this amounts to the replacements


which after simple manipulations lead to the matrix equation


For the matrix equation to have non-zero solutions, the determinant of the 2 ×2 matrix must be zero. This condition leads to a dispersion equation of the form


The term linear in k represents the net drift velocity, while the quadratic term describes an effective diffusion due to the switchings between the two states. The details of this calculation

> 1M. Dogterom and S. Leibler, Phys. Rev. Lett. 70, 1347 (1993).

61

are left to the problem sets. We shall instead derive expressions for v and D by appealing to physical arguments.

Consider the limit where exchanges between + and − states take place rapidly. This quickly leads to an equilibrium between the two states such that


The evolution of the net probability p(z, t) = p+(z, t) + p−(z, t) for MTs of length z is then obtained by adding the two evolution Eqs. (3.1), as


which using Eq. (3.5) turns into


The solution to the above equation is a traveling wave p(z, t) = p(z − vt) describing a net probability that drifts to higher z with a velocity


Of course, given the barrier at z = 0, the above solution only makes sense as long as v is positive. When the value of v from Eq. (3.8) is negative, the MTs tend to shrink towards zero. In this case fluctuations lead to a time independent steady state in which


This can be verified by substituting Eq. (3.9) into Eqs. (3.1) to obtain the matrix form


Once again, the determinant of the matrix must be zero to allow non-zero solutions, leading to


The probability to find a MT of length z in this state is a simple exponential with


while the fraction of time the MT is in the growing/shrinking state is easily observed to be


62

---

[← 3.1.1 Dynamic Instability of Microtubules](02-3-1-1-dynamic-instability-of-microtubules.md) · [Up: contents](index.md) · [3.1.3 Caps & Catastrophes →](04-3-1-3-caps-catastrophes.md)
