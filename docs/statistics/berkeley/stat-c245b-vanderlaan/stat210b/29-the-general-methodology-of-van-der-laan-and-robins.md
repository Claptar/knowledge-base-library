---
title: The general methodology of van der Laan and Robins
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The general methodology of van der Laan and Robins

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The general methodology of van der Laan and Robins for estimating regular Euclidean parameters with (or without) censored data can be summarized as follows.

Setup: _O_ 1 _, ..., On ∼ P ∈M_ are _n_ i.i.d. observations, the parameter of interest is the pathwise differentiable _ψ_ ( _P_ ), for _ψ_ : _M →R_<sup>_k_</sup> . The support for _X_ and _C_ in the model _M_ are denoted _X_ and _C_ . The full (unobserved) data is stored in _X_ , and _O_ = Φ( _X, C_ ) for _C_ a censoring variable that satisfies _coarsening at random_ , so for _C_ ( _o_ ) = _{x ∈X_ : _o_ = Φ( _x, c_ ) for some _c ∈C}_ , _dP_ ( _o|X_ = _x_ 1) = _dP_ ( _o|X_ = _x_ 2) for _x_ 1 _, x_ 2 _∈ C_ ( _o_ ).

i: Find _Tnuis_<sup>_⊥_(</sup><sup>_FX_)inthefull-dataworld.</sup>

ii: Map this into _Tnuis_<sup>_⊥_(</sup><sup>_P_)intheobserved-dataworld.</sup>

iii: Estimate _ψ_ ( _P_ ) by solving an estimating equation from _Tnuis_<sup>_⊥_(</sup><sup>_P_)</sup>

iv: If possible, look for the efficient estimate, so use the efficient score as the estimating equation

Care needs to be taken in step (iii). Typically an estimating function can be written as _U_ ( _O|ψ_ ( _P_ ) _, η_ ( _P_ )), for _η_ ( _P_ ) a nuisance parameter. We usually estimate this with _ηn_ from the data, and solve 0 = _n_<sup><u>1</u></sup> � _ni_ =1<sup>_U_(</sup><sup>_Oi|ψn, ηn_).Inordertoshowthattheresulting</sup> estimate _ψn_ is asymptotically linear for _ψ_ ( _P_ ), we must typically show that the nuisance parameter is estimated sufficiently quickly so that _n_<sup><u>1</u></sup> � _ni_ =1<sup>_U_(</sup><sup>_Oi|ψn, η_(</sup><sup>_P_)) =</sup><sup>_oP_(</sup><sup>_n−_1</sup><sup>_/_2).</sup> Of course, we still need to check the usual regularity conditions of estimating equations to show asymptotic linearity of the resulting estimate. That is, we must show _ψn_ is consistent, the map _θ → EP_ [ _U_ ( _O|θ, η_ ( _P_ )] from _R_<sup>_k_</sup> to _R_<sup>_k_</sup> should have an invertible derivative at _θ_ = _ψ_ ( _P_ ), and there is also an empirical process condition to check for the functions _{U_ ( _·|θ, η_ ( _P_ )) : _∥θ − ψ_ ( _P_ ) _∥ < ϵ}_ . The point is, obviously not every function in _Tnuis_<sup>_⊥_(</sup><sup>_P_)canbeusedasanestimatingequationtogiveanasymptotically</sup> linear estimate (eg. the zero vector is in this space), and we still have to verify the regularity conditions after deciding to use a particular estimating equation.

31

---

[← How do the ideas from the course interact?](28-how-do-the-ideas-from-the-course-interact.md) · [Up: contents](index.md) · [What’s so great about Tnuis⊥(P)? →](30-what-s-so-great-about-tnuis-p.md)
