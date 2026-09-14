---
title: Spatially inhomogeneous solutions
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/15-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Spatially inhomogeneous solutions

**Source:** `lecture-outlines/15-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Now consider the full system of equations [VIII.8] and explore stability of the system around the homogeneous solution [VIII.10]:

_A_ ( _s_ ,τ) = _A_ + _A_ (' _s_ ,τ) _I_ ( _s_ ,τ) = _I_ + _I_ (' _s_ ,τ)


Based on [VIII.8] we can write:


To find the solutions of [VIII.14] we start by guessing a trial function:


This trial function makes sense since the second derivative of the cosine is the cosine itself times a constant. Substituting the trial function gives:


Again this is system of two linear ordinary differential equations that we can test for stability:


The latter inequality holds since we impose stability of the homogeneous solution (see inequality [VIII.12]). The former inequality can be written as:


For any wavelength l this is satisfied if:

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– November 2004

46

**[VIII.19]**

_<u>Q</u> R_ −1 _P_ > _R_ + 1

Both [VIII.19] and [VIII.12] will certainly hold if P < 1. In other words if the activator diffuses faster than the inhibitor. In the opposite way, spatial nonuniformity and the possibility of pattern formation requires the inhibitor to diffuse faster than the activator (long range inhibition, short range activation).

---

[← Spatially homogeneous solutions](03-spatially-homogeneous-solutions.md) · [Up: contents](index.md) · [Conditions for inhomogeneous instability →](05-conditions-for-inhomogeneous-instability.md)
