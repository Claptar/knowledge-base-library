---
title: 3 Stationary and Causality for AR( p ), p ≥ 2
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyOne153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyOne153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Stationary and Causality for AR( p ), p ≥ 2

**Source:** [`LectureTwentyOne153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyOne153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Similar to AR(1), it is possible to characterize parameter regimes which ensure existence of stationary (and also causal/non-causal) solutions of AR( _p_ ) for _p ≥_ 1. Recall that the AR( _p_ ) model is given by the equation:


In terms of the Backshift Notation, we can write the model as:


where _φ_ ( _B_ ) is the result of the following polynomial applied to the Backshift operator:


This polynomial is called the AR( _p_ ) polynomial or the AR( _p_ ) characteristic polynomial. This polynomial will have _p_ roots _z_ 1 _, . . . , zp_ . Some of these roots may be complex.

1. Suppose all the roots _zi_ have modulus distinct from one: _|zi|̸_ = 1 for every _i_ . Then there exists a unique stationary solution to (5). Backshift calculus can be used to write the stationary solution _yt_ explicitly in terms of _{ϵt}_ . We shall see how to do this in the next lecture.

2. Suppose all the roots _zi_ have modulus strictly larger than one: _|zi| >_ 1 for every _i_ . Then the unique stationary solution is of the form _yt_ = _µ_ + _ψ_ 0 _ϵt_ + _ψ_ 1 _ϵt−_ 1+ _ψ_ 2 _ϵt−j_ + _· · ·_ = _µ_ +<sup>�</sup><sup>_∞_</sup> _j_ =0<sup>_ψjϵt−j_,forsome</sup><sup>_µ_and</sup><sup>_{ψj, j≥_0</sup><sup>_}_.Inotherwords,onlythecurrentand</sup> past _ϵt_ values ( _ϵt, ϵt−_ 1 _, . . ._ ) determine _yt_ . Therefore, this stationary solution is causal.

3. Suppose at least one of the roots _zi_ has modulus strictly smaller than 1 while all other roots have moduli strictly larger than 1. In this case, the unique stationary solution will involve _ϵt_ -terms from both in the past and future: _yt_ = _µ_ +<sup>�</sup><sup>_∞_</sup> _j_ = _−∞_<sup>_ψjϵt−j_(note</sup> that the sum is now going from _−∞_ to _∞_ ). This stationary solution is non-causal.

4. Suppose at least one root _zi_ has modulus exactly equal to 1. Then there is no stationary solution to (5).

When _p_ = 1, the AR(1) polynomial is _φ_ ( _z_ ) = 1 _− φ_ 1 _z_ with root 1 _/φ_ 1. So the root having magnitude more than 1 is equivalent to _|φ_ 1 _| <_ 1. Then the above assertions are equivalent to the assertions made in the previous two sections for AR(1).

We will see more details and examples in the next lecture.

5

---

[← 2 On the formulae for stationary AR(1)](02-2-on-the-formulae-for-stationary-ar-1.md) · [Up: contents](index.md) · [4 Additional Optional Reading →](04-4-additional-optional-reading.md)
