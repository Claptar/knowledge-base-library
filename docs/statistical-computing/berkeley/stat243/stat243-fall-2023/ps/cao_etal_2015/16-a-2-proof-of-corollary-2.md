---
title: A.2. Proof of corollary 2
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/ps/cao_etal_2015.pdf
source_file: sources/berkeley-stat243/stat243-fall-2023/ps/cao_etal_2015.pdf
licence: BSD-3-Clause
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# A.2. Proof of corollary 2

**Source:** [`ps/cao_etal_2015.pdf`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/ps/cao_etal_2015.pdf) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We next show the consistency of the variance estimate. To begin with, we have


Using a similar argument to that to obtain equation (17), we show that


is a _P_ -Glivenko–Cantelli class. Therefore,


in probability. Since _β_<sup>ˆ</sup> is consistent for _β_ 0, by the continuous mapping theorem, @Un. _β_ /=@ _β_ | _β_ = ˆ _β_ converges in probability to −A. _β_ 0/: Similarly, let


then sup| _β_ − _β_ 0|<" | Σ<sup>˜</sup> . _β_ / − E _{_ Σ<sup>˜</sup> . _β_ / _}_ |→ 0 in probability. However,


After a change of variables, and by condition 3,


Therefore,


The consistency of the variance estimate follows.

_Analysis of Asynchronous Data_ 773

_A.3. Proof of theorem 2_ Denote G.s1, s2/ = E[X.t + s1/ _g{_ X.t + s2/<sup>T</sup> _β_ 0.t + s2/ _}_ − X.t + s1/ _g{_ X.t + s1/<sup>T</sup> _β_ .t/ _}_ ]: We first establish the relationship


where B _{β_ 0.t/, t _}_ is defined in theorem 2,


and


To obtain equation (24), first, using _P_ n and _P_ to denote the empirical measure and true probability measure respectively, we have


For the second term on the right-hand side of equation (25), we have


Recall that G.s1, s2/ = E[X.t + s1/ _g{_ X.t + s2/<sup>T</sup> _β_ 0.t + s2/ _}_ − X.t + s1/ _g{_ X.t + s1/<sup>T</sup> _β_ .t/ _}_ ] and we can do a Taylor series expansion of G around .0, 0/: Taking into account conditions 3<sup>′</sup> and 4<sup>′</sup> , and after a change of variables, we obtain


774 _H. Cao, D. Zeng and J. P. Fine_

where we did another Taylor series expansion of function _g{_ X.t/<sup>T</sup> _β_ .t/ _}_ at X.t/<sup>T</sup> _β_ 0.t/ for any fixed t. For any fixed t, if _γ_<sup>T</sup> B _{β_ 0.t/, t _}γ_ = 0, then _γ_<sup>T</sup> X.t/ = 0, so _γ_ = 0 from condition 2<sup>′</sup> . Thus B _{β_ 0.t/, t _}_ is a non-singular matrix. For term I, we consider the class of functions


for a given constant ". Similarly to the proof in theorem 1, we can show that this is a _P_ -Donsker class for any fixed time point t by the Jain–Marcus theorem. We therefore obtain that the first term on the right-hand side of equation (25) for | _β_ .t/ − _β_ 0.t/| <M.nh1h2/<sup>−1=2</sup> is equal to


Combining equations (25), (26) and (27) and, by condition 4<sup>′</sup> , we obtain equation (24). Therefore,


Now we show that .nh1h2/<sup>1=2</sup> Un _{β_ 0.t/ _}_ follows the central limit theorem. In other words, we wish to derive the distribution of


For convenience, we denote the above sum as n<sup>1=2</sup> n<sup>−1</sup> Σ<sup>n</sup> i=1<sup>Wi.t/, where</sup>


Since this is an independent and identically distributed sum, we need to calculate only Σ<sup>Å</sup> .t/ = var _{_ W1.t/ _}_ . We have


Similarly to calculation of the order of Σ, we obtain

E[var _{_ W1.t/|X.s/, s ∈ [0, _τ_ ]; N.t, s/, .t, s/ ∈ [0, _τ_ ]<sup>⊗2</sup> _}_ ]


_Analysis of Asynchronous Data_ 775


by conditions 4<sup>′</sup> and 5<sup>′</sup> and a change of variables. Similarly to the proof of theorem 1, we have


Therefore, we have


Similarly, we have


which verifies that the Lyapunov condition holds. Thus


Combining with equation (24), the conclusion of theorem 2 holds.

---

[← A.1. Proof of theorem 1](15-a-1-proof-of-theorem-1.md) · [Up: contents](index.md) · [A.4. Proof of corollary 4 →](17-a-4-proof-of-corollary-4.md)
