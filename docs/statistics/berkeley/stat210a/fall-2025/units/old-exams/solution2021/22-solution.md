---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2021.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/solution2021.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`units/old-exams/solution2021.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2021.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Again the distribution only depends on _X_ 1 _, . . . , Xk_ , so we need to find the asymptotic distribution of


Let _Zk_ = ( _α_ + _β_ ) _/k_ + _X_ ~~(~~ 0); then


Let _µ_ = E _X_ 1 = _mγ_ 0 _/_ (1 _− γ_ 0); then by Slutsky’s theorem,


The first term tends to _N_ (0 _, σ_<sup>2</sup> ) where _σ_<sup>2</sup> = Var( _X_ 1) = _mγ_ 0 _/_ (1 _− γ_ 0)<sup>2</sup> , and the second tends deterministically (and therefore in probability) to 0. Hence by Slutsky’s theorem we have _√k_ ( _Zk − µ_ ) _⇒ N_ (0 _, σ_<sup>2</sup> ). By the delta method, then, for the differentiable function _f_ ( _z_ ) = _z/_ ( _m_ + _z_ ), we have


where _f_<sup>˙</sup> ( _z_ ) = _m/_ ( _m_ + _z_ )<sup>2</sup> , so


Finally, the second term in (1) tends to 0 as well, since the numerator tends to zero and the denominator tends to _m_ + _µ >_ 0, so by Slutsky’s theorem we have


- (d) Next, we relax the assumption that _k_ is known. Instead assume _n_ = 10 and all we know is that _k ∈{_ 4 _,_ 5 _,_ 6 _}_ . Find a minimal sufficient statistic for the three-parameter model with _γ_ 0 _, γ_ 1 _∈_ (0 _,_ 1) and _k ∈{_ 4 _,_ 5 _,_ 6 _}_ . You do not need to prove it is minimal, as long as you give the right answer.

14

---

[← Solution](21-solution.md) · [Up: contents](index.md) · [Solution →](23-solution.md)
