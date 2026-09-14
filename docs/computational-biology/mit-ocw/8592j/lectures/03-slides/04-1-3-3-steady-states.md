---
title: 1.3.3 Steady states
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.3.3 Steady states

**Source:** `lectures/03-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

While it is usually hard to solve the Kolmogorov equation as a function of time, it is relatively easy to find the steady state solution to which the population settles after a long time. Let us denote the steady-state probability distribution by p<sup>∗</sup> (x), which by definition must satisfy


Therefore, setting the right-hand side of Eq. (1.35) to zero, we get


The most general solution admits steady states in which there is an overall current and the integral over x of the last equation leads to a constant flow in probability. It is not clear how such a circumstance may arise in the context of population genetics, and we shall therefore focus on circumstances where there is no probability current, such that


We can easily rearrange this equation to


This equation can be integrated to


such that


with the proportionality constant set by boundary conditions.

Let us examine the case of the dynamics of a fixed population, including mutations, and reproduction with selection. Adding the contributions in Eqs. (1.38), (1.39) and (1.54), we have


while


The last approximation of ignoring the contribution from mutations to diffusion is common to population genetics and we shall follow it here without further justification. It enables a closed form solution to the steady state, as


resulting in


In the special case of no selection, s = 0 and (for convenience) µ1 = µ2 = µ, the steadystate solution (1.63) simplifies to


The shape of the solution is determined by the parameter 4Nµ. If 4Nµ > 1, then the distribution has a peak at x = 1/2 and diminishes to the sides. On the other hand, if the population is small and 4Nµ < 1, then p<sup>∗</sup> (x) has peaks at either extreme—a situation where genetic drift is dominant.


14

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 1.3.2 Chemical analog & Selection](03-1-3-2-chemical-analog-selection.md) · [Up: contents](index.md)
