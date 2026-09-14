---
title: 6. The Fokker-Planck equation
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/12-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6. The Fokker-Planck equation

**Source:** `lecture-outlines/12-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For intermediate molecule numbers, when the difference between _n_ and _n_ +1 may be neglected but fluctuations must still be taken into account, there is a useful approximation to the Master Equation which provides some physical insight. We replace _n_ by a continuous variable, and use the notation _h_ ( _n_ ) in place of the _hn_ used previously. Any function of _n_ can be Taylor expanded:


Thus,


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004

Substituting this into Eq. 2, we obtain the Fokker Planck equation:


where _J_ represents a probability flux. This can be thought of as a diffusion equation: every particle represents a system in our ensemble; the particle position is analogous to the number of molecules in the system; and _J_ is the flux of particles across any boundary. In steady state, _J_ must be a constant; however, the flux at _n_ = 0 must be zero (no system can pass to having negative particle number), so the flux must be zero everywhere. This gives us the following equation:


Setting _q_ = ( _f_ + _g_ ) _p_ ,


Therefore,


That is, the reaction is analogous to a thermodynamic system in some potential ϕ .

---

[← 5. The limit of large numbers](06-5-the-limit-of-large-numbers.md) · [Up: contents](index.md) · [7. Steady state of a bistable system →](08-7-steady-state-of-a-bistable-system.md)
