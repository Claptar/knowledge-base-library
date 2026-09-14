---
title: 3.2.2 Force of a Brownian Motor
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/21-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.2.2 Force of a Brownian Motor

**Source:** `lectures/21-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

To find out how efficiently the energy input from ATP is converted to work, we need to know the force exerted by the motor in traveling a distance a at each step. This is not an easy task as it is not possible to directly measure all dissipative and other forces acting on the small molecule. The following procedures have been used to estimate forces on the motor.


The stall force is obtained by pulling the motor back with an optical tweezer. The motor must now also climb up against the potential from the external force F , resulting in


Clearly the motor stalls (v = 0) when F = Fs = Fmax = ∆Gh/a. This makes sense, as there are no dissipative forces acting on a stationary motor.

The Einstein force is obtained by analogy to Brownian particles from a ratio of velocity and diffusion coefficients. A particle in solution experiences a drag force proportional to its velocity, such that v = µF where µ is its mobility. In the absence of an external force, the particle diffuses in solution with diffusion constant D. Diffusion originates in collisions with thermally excited atoms in the fluid, and to ensure proper thermal equilibrium the mobility and diffusion constant must be related by the Einstein relation, D = µkBT . From these relations we can define an Einstein force


where we have used the values for drift and diffusion of the motor along its track from the two-state hopping model. Since (ru)/(ld) = e<sup>β∆Gh</sup> , in the limit β∆Gh → 0


while for β∆Gh ≫ 1, FE ≈ 2kBT/a. Thus the Einstein force is always less than the maximum possible force, and limited by thermal fluctuations.

69

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 3.2.1 Asymmetric Hopping](02-3-2-1-asymmetric-hopping.md) · [Up: contents](index.md)
