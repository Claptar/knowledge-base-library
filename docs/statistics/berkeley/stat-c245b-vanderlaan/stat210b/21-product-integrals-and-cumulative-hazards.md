---
title: Product Integrals and Cumulative Hazards
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Product Integrals and Cumulative Hazards

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We first prove the Hadamard differentiability of a very simple map.

**Theorem 0.12.** _Let D_<sup>_⋆_</sup> [ _a, b_ ] _denote the subset of functions in D_ [0 _, b_ ] _that are bounded below by constant ϵ >_ 0 _, where ϵ is fixed. Then φ_ : ( _D_ [0 _, b_ ] _, ∥· ∥∞_ ) _→_ ( _D_ [0 _, b_ ] _, ∥· ∥∞_ ) _is Hadamard differentiable at B ∈ D_<sup>_⋆_</sup> [ _a, b_ ] _with Hadamard derivative dφB_ ( _β_ ) = _− B_<sup>_<u>β</u>_2</sup><sup>_._</sup>

**proof** : Consider a scalar sequence _tn →_ 0, and _βn ∈ D_ [0 _, b_ ] _→ β ∈ D_ [0 _, b_ ].

Note that for _|b_ ( _s_ ) _− B_ ( _s_ ) _| ≤ tn|βn_ ( _s_ ) _|_ that _|b_ ( _s_ ) _− B_ ( _s_ ) _| ≤ tn|βn_ ( _s_ ) _| ≤ tn∥βn∥∞ ≤ tn∥βn − β∥∞_ + _tn∥β∥∞ →_ 0. For the real-valued function _f_ ( _x_ ) = 1 _/x_ , note that _f_<sup>_′_</sup> ( _x_ ) = _−_ 1 _/x_<sup>2</sup> is uniformly continuous for 0 _< ϵ ≤ x ≤∥B∥∞_ , so as _B_ ( _s_ ) is bounded away from _ϵ >_ 0, _f_<sup>_′_</sup> ( _b_ ( _s_ )) _→− B_ <u>1(</u> _s_ )<sup>uniformlyfor0</sup><sup>_≤s ≤b_.</sup>

Then by a first order Taylor expansion of _f_ ( _x_ ) = 1 _/x_ about _B_ ( _s_ ),<sup>_<u>φ</u>_</sup><sup><u>(</u></sup><sup>_B_</sup><sup><u>+</u></sup><sup>_tnβn_</sup> _tn_<sup><u>)(</u></sup><sup>_s_</sup><sup><u>)</u></sup><sup>_−φ_</sup><sup><u>(</u></sup><sup>_B_</sup><sup><u>)</u></sup> + _Bb_<sup>2(</sup><sup>_s_)=</sup> _t_ <u>1</u> _n_<sup>(</sup> _B_ ( _s_ )+ _t_ <u>1</u> _nβn_ ( _s_ )<sup>_−_</sup> _B_ <u>1(</u> _s_ )<sup>) +</sup> _Bb_<sup>2</sup> <u>(</u> _s_ ( _s_ <u>))</u><sup>=</sup> _t_ <u>1</u> _n_<sup>(</sup><sup>_tnβn_(</sup><sup>_s_))</sup><sup>_f ′_(</sup><sup>_b_(</sup><sup>_s_)) +</sup> _Bβ_<sup>2</sup> <u>((</u> _ss_ <u>))</u><sup>=</sup><sup>_βn_(</sup><sup>_s_)</sup><sup>_f ′_(</sup><sup>_b_(</sup><sup>_s_)) +</sup> _Bβ_<sup>2</sup> <u>((</u> _ss_ <u>))</u><sup>_→_0uniformlyfor0</sup><sup>_≤s ≤b_,byabove,andthefactthat</sup><sup>_∥βn −β∥∞→_0.□</sup>

We can now prove the Hadamard differentiability of the so-called cumulative hazard.

**Theorem 0.13.** _Let E denote the space {_ ( _A, B_ ) : _A, B ∈ D_ [0 _, b_ ] _, A ∈ BVM , B ≥ ϵ >_ 0 _}. The map φ_ : _D_ [0 _, b_ ]<sup>2</sup> _→ D_ [0 _, b_ ] _given by φ_ ( _A, B_ ) = �0 _· B_ <u>1</u><sup>_dAisHadamard_</sup> _differentiable (using the supremum norm for the domain and range spaces) for_ ( _A, B_ ) _∈ E with Hadamard derivative dφ_ ( _A,B_ )( _α, β_ ) = �0 _·_<sup>(1</sup><sup>_/B_)</sup><sup>_dα −_</sup> �0 _·_<sup>(</sup><sup>_β/B_2)</sup><sup>_dA._</sup>

**proof** : We write the map as ( _A, B_ ) _→_ ( _A,_ 1 _/B_ ) _→_ �0 _· B_ <u>1</u><sup>_dA_.Fromthepreviousthe-</sup> orem, the map ( _A, B_ ) _→_ ( _A,_ 1 _/B_ ) has derivative map at ( _A, B_ ) given by ( _α, β_ ) _→_ ( _α, −β/B_<sup>2</sup> ). From the Homework 1 question on the Wilcoxin statistic, ( _A,_ 1 _/B_ ) _→_ �0 _· B_ <u>1</u><sup>_dA_hasderivativemapat(</sup><sup>_A,_1</sup><sup>_/B_)givenby(</sup><sup>_α, −β/B_2)</sup><sup>_→_</sup> �0 _· B_ <u>1</u><sup>_dα−_</sup> �0 _· Bβ_<sup>2</sup><sup>_dA_.</sup> The result now follows by the chain rule. □

We can now consider composing comulative hazard functions and product integrals.

**Theorem 0.14.** _Let E denote the space {_ ( _A, B_ ) : _A, B ∈ D_ [0 _, b_ ] _, A ∈ BVM , B ≥ ϵ >_ 0 _}. Consider the map φ_ : _D_ [0 _, b_ ]<sup>2</sup> _→ D_ [0 _, b_ ] _defined by_ ( _P_ 1 _, P_ 2) _→_ (Λ = <u>�0</u> _· P_ <u>12</u><sup>_dP_1)</sup><sup>_→_</sup> Π0 _<s≤·_ (1 _− d_ Λ( _s_ )) _. Then if ψ_ (Λ)( _t_ ) _≡_ Π0 _<s≤t_ (1 + _d_ Λ( _s_ )) _for_ Λ( _t_ ) = �0 _t P_ <u>12</u><sup>_dP_1)</sup><sup>_,φis_</sup> _Hadamard differentiable (using the supremum norm for the domain and range spaces) at_ ( _A, B_ ) _∈ E with Hadamard derivative given by:_ ( _α, β_ ) _→_ �0 _·_<sup>_ψ_(Λ)(</sup><sup>_u_)</sup><sup>_ψ_(Λ)(</sup><sup>_u, ·_](</sup> _B_ (1 _u_ )<sup>_dα_(</sup><sup>_u_)</sup><sup>_−_</sup> _Bβ_ (( _uu_ ))<sup>2</sup><sup>_dA_(</sup><sup>_u_))</sup><sup>_._</sup>

**proof** : This is just the chain rule, applied to the previously given Hadamard derivatives of the cumulative hazard and product integral maps. □

14

---

[← Product Integrals](20-product-integrals.md) · [Up: contents](index.md) · [Survival Analysis →](22-survival-analysis.md)
