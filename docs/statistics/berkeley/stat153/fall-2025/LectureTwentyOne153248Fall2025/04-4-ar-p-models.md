---
title: 4 AR( p ) models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyOne153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyOne153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 AR( p ) models

**Source:** [`LectureTwentyOne153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyOne153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The AR(p) model is:


Unlike the MA( _q_ ) model, the AR( _p_ ) model can be stationary or not depending on the specific values of the parameters _ϕ_ 1 _, . . . , ϕp_ . If _ϕ_ 1 _, . . . , ϕp_ are such that every root of the AR polynomial:

_ϕ_ ( _z_ ) = 1 _− ϕ_ 1 _z −· · · − ϕpz_<sup>_p_</sup> _._

has modulus strictly larger than 1, then (3) has a causal stationary solution. This solution can be written in the form:


for some _µ_ and coefficients _ψ_ 1 _, ψ_ 2 _, . . ._ satisfying<sup>�</sup> _j_<sup>_|ψj| < ∞_.Thereareinbuiltfunctionsin</sup> `statsmodels` which output values of _µ, ψ_ 0 _, ψ_ 1 _, . . ._ given _ϕ_ 0 _, ϕ_ 1 _, . . . , ϕp_ .

The representation (4) resembles the MA equation (1) except now _q_ = _∞_ . However the coefficients _ψj_ are all explicit functions of only the _p_ + 1 parameters _ϕ_ 0 _, . . . , ϕp_ .

---

[← 3 On Parameter Estimation in MA( q )](03-3-on-parameter-estimation-in-ma-q.md) · [Up: contents](index.md) · [5 The Box-Jenkins Modeling Philosophy →](05-5-the-box-jenkins-modeling-philosophy.md)
