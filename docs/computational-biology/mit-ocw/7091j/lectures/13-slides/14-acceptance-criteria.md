---
title: Acceptance Criteria
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/13-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Acceptance Criteria

**Source:** `lectures/13-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Randomly choose neighboring state:

   - Alwa **y** s acce **p** t moves that reduce **p** otential

   - Go uphill (higher potential) based on odds ratio

_e_<sup></sup><sup>_Etest_/</sup><sup>_kT_</sup> _e_<sup></sup><sup>_En_/</sup><sup>_kT_</sup> _P_ <u>(</u> _Stest_ <u>)</u>  ( _Etest_  _E n_ ) / _kT_  **_P_ (** **_Sn_ )** **_Z_ (** **_T_ )** / **_Z_ (** **_T_ )**  _e_ 1


24

. **3 Metropolis sampling** Iterate for a fixed number of c **y** cles or until convergence:

**1** . **Start with a system in state S** n **with energy E** n 2. Choose a neighboring state at random; we will call it the proposed state : Stest with energy Etest **3** . **If E < E : S =S** test n n+1 test

4. Else set Sn+1= Stest with probability _P_  _e_<sup>(</sup><sup>_Etest_</sup><sup>_En_) /</sup><sup>_kT_</sup> – otherwise Sn+1= Sn

25


<!-- Start of picture text -->
1<br><!-- End of picture text -->

Minimization vs. simulated annealing


26


<!-- Start of picture text -->
4<br>P=e ‐ΔG/kT P=1<br>3 5<br>1<br>P=1<br>P=e ‐ΔG/kT<br>2<br><!-- End of picture text -->

27

---

[← Metropolis Algorithm](13-metropolis-algorithm.md) · [Up: contents](index.md) · [Acceptance Criteria →](15-acceptance-criteria.md)
