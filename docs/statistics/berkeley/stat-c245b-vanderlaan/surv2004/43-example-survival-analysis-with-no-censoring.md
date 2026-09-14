---
title: 'Example: Survival Analysis with no Censoring'
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Example: Survival Analysis with no Censoring

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let _T ∼ F_ be a survival time, where M is a completely nonparametric model. Here F can be any cdf of a nonnegative random variable. Let _µ_ ( _F_ ) = _F_ ( _t_ ) be the parameter of interest, for fixed t. In this example there is no nuisance parameter _η_ . Consider the parametric submodel _fϵ_ ( _T_ ) = (1 + _ϵh_ ( _T_ )) _f_ ( _T_ ), where � _h_ ( _T_ ) _dF_ ( _T_ ) = 0 but h is otherwise arbitrary. Note that the score of this submodel is h(T), so the tangent space is all of _L_<sup>2</sup> 0<sup>(</sup><sup>_T_),whichimmediatelytellsusthatany</sup> asymptotically linear estimate is efficient because its influence curve must be in this tangent space. We now formally calculate _TNUIS_<sup>_⊥_,theorthogonalcomplementofthenuisancetangentspace.</sup>

_dϵd_<sup>_µ_(</sup><sup>_Fϵ_)</sup><sup>_|ϵ_=0=</sup><sup>_limϵ→_0 1</sup> _ϵ_<sup>(</sup><sup>_µ_(</sup><sup>_Fϵ_)</sup><sup>_−µ_(</sup><sup>_F_)) =</sup><sup>_limϵ→_0 1</sup> _ϵ_ �0 _t_<sup>(</sup><sup>_fϵ_(</sup><sup>_T_)</sup><sup>_−f_(</sup><sup>_T_))</sup><sup>_dT_</sup> = _limϵ→_ 0<sup><u>1</u></sup> _ϵ_ �0 _t_<sup>_ϵh_(</sup><sup>_T_)</sup><sup>_f_(</sup><sup>_T_)</sup><sup>_dT_=</sup> �0 _t_<sup>_h_(</sup><sup>_T_)</sup><sup>_dF_(</sup><sup>_T_) =</sup> � ( _I_ ( _T ≤ t_ ) _− F_ ( _t_ )) _h_ ( _T_ ) _dF_ ( _T_ ) = _⟨I_ ( _T ≤ t_ ) _− F_ ( _t_ ) _, h_ ( _T_ ) _⟩_

Setting this derivative to zero and solving for h gives the nuisance tangent space. Thus, _TNUIS_ = _{h_ ( _T_ ) _∈ L_<sup>2</sup> 0<sup>(</sup><sup>_T_):</sup><sup>_h_(</sup><sup>_T_)</sup><sup>_⊥I_(</sup><sup>_T≤t_)</sup><sup>_−F_(</sup><sup>_t_)</sup><sup>_}_.Takingtheorthogonalcomplementofthisspacegives</sup> that _TNUIS_<sup>_⊥_= [</sup><sup>_I_(</sup><sup>_T≤t_)</sup><sup>_−F_(</sup><sup>_t_)],where[</sup><sup>_•_]denotesthelinearspan.Hence,</sup><sup>_D_(</sup><sup>_T|µ_) =</sup><sup>_I_(</sup><sup>_T≤t_)</sup><sup>_−µ_is</sup> in _TNUIS_<sup>_⊥_, and it is an estimating function because it clearly has mean zero under the truth.Because</sup> _TNUIS_<sup>_⊥_is the span of a single random variable, we can check that using any estimating function from</sup> this space gives the same estimator, which is just _µn_ = _n_<sup><u>1</u></sup> � _ni_ =1<sup>_I_(</sup><sup>_Ti≤t_).Weconcludefromour</sup> previous results that _µn_ is asymptotically linear (which we already could see without any efficiency theory), and it is efficient because it is the unique estimating function estimate over all estimating functions in _TNUIS_<sup>_⊥_.</sup>

Notes by Melinda Teng April 14, 2004

#### **Estimating functions in regression**

54

Suppose

_Y_ = _m_ ( _Z | B_ ) + _ϵ_

where _Y_ denote the outcome, _Z_ is the vector of covariates, and _B_ denote the regression parameters. Rewriting as _ϵ_ ( _B_ ) = _Y − m_ ( _Z | B_ ), we assume that _E_ [ _K_ ( _ϵ | B_ ) _| Z_ ] = 0 for a given monotone increasing function _x −→ K_ ( _x_ ). For example, when _K_ ( _ϵ_ ) = _ϵ_ , we have _m_ ( _Z | B_ 0) = _E_ [ _Y | Z_ ]; when _K_ ( _ϵ_ ) = _I_ ( _ϵ >_ 0) _−_ 1 _/_ 2, we have _m_ ( _Z | B_ 0) = _Med_ [ _Y | Z_ ]; when _K_ ( _ϵ_ ) = _I_ ( _ϵ >_ 0) _−_ (1 _− p_ ), we have _m_ ( _Z | B_ 0) = _p − th_ quantile of _Y | Z_ .

Let us now define


to be the class of all estimating functions for _B_ , and _Bn_ ( _h_ ) be a solution of


where _h_ ( _._ ) can be any vector function.

Now,


where _C_ ( _h_ ) = _−_ � _δBδ_<sup>_E_0[</sup><sup>_h_(</sup><sup>_Z_)</sup><sup>_K_(</sup><sup>_ϵ_(</sup><sup>_B_))]</sup> �.

Let


and _hn_ be an estimator of _hopt_ according to a (guessed) model of _E_ [ _K_ ( _ϵ_ )<sup>2</sup> _| Z_ ]. If _Bn_ is a solution of


then _Bn − B_ 0 _≈ n_<sup><u>1</u></sup> � _ni_ =1<sup>_C−_1(</sup><sup>_h⋆_)</sup><sup>_h⋆_(</sup><sup>_Zi_)</sup><sup>_K_(</sup><sup>_ϵi_(</sup><sup>_B_))where</sup><sup>_h⋆_isthelimitof</sup><sup>_h_.Inaddition,notethat</sup> _Bn_ is asymptotically linear, and is an efficient estimator of _B_ 0 if _hn −→ hopt_ .

#### **Right-censored data structure**

Let _X_ ( _t_ ) denote a time-dependent full data structure process of interest, and _T_ denote the endpoint of this process. A _full data structure_ is defined as _X_ = _X_<sup>¯</sup> ( _T_ ) = ( _X_ ( _t_ ) : _t ≤ T_ ). The _observed data structure_ (what we can observe) is defined as _O_ = ( _T_<sup>˜</sup> = _min_ ( _T, C_ ) _, △_ = _I_ ( _T ≤ C_ ) _, X_<sup>¯</sup> ( _T_<sup>˜</sup> )) where _C_ is a censoring variable. We denote the distribution of the observed data structure by _PFX ,GC|X_ where _GC|X_ represents the distribution of the censoring mechanism.

Under _CAR_ (Coarsening At Random) assumption, for _t < T_ , we have


55

for some function _m_ .

Lecture of April 19, 2004, Zheng Yin

---

[← Relationship Between Estimating Functions and Tangent Spaces](42-relationship-between-estimating-functions-and-tangent-spaces.md) · [Up: contents](index.md) · [4 Right Censored Data Structure (Cont’d) →](44-4-right-censored-data-structure-cont-d.md)
