---
title: Stat210b Part 31 —
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stat210b Part 31 —

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Example 1.6. (Repeated measures data with right-censoring; continuation of Example ??)** In the previous coverage of this example, we explained that, in the full data world, globally efficient estimators are not practical but that attractive locally efficient estimators exist. The latter was shown by showing that the orthogonal complement of the nuisance tangent space in the full data model, which identifies all estimating functions, was given by functions _h_ ( _X_<sup>_∗_</sup> ) _ϵ_ ( _α_ ), which thus do not depend on nuisance parameters. In the observed data model _M_ ( _CAR_ ), defined by the restrictions ( **??** ) and ( **??** ), we claim that it is even impossible to construct any practical estimators at all.

In order to show this, we need to find the orthogonal complement of the nuisance tangent space in the model _M_ ( _CAR_ ) and show that each of the elements of this space depends on nuisance parameters that are very hard to estimate with normal sample sizes. Note that in the observed data model _M_ ( _CAR_ ), the nuisance parameter consists of the full data nuisance parameter _η_ and _G_ .

32

Let ∆= _I_ ( _C ≥ p_ ) be the indicator that the subject does not drop out of the study before _p_ . We have that


where _G_<sup>¯</sup> ( _t | X_ ) _≡ P_ ( _C ≥ t | X_ ). To begin with, we consider the inverse of probability of censoring weighted estimating functions that are obtained by inverse weighting any full data structure estimating function _Dh_ ( _X | α_ ) _≡ h_ ( _X_<sup>_∗_</sup> ) _ϵ_ ( _α_ ):


Thus, given an estimator of the nuisance parameter _G_<sup>¯</sup> ( _p | X_ ), one could use as estimating equation for _α_ :


However, under the sole restriction CAR ( **??** ), estimation of _G_<sup>¯</sup> requires fitting nonparametrically a multinomial regression of very high dimension. As a consequence, these Horvitz–Thompson types of estimating functions do not result in practical estimators that are consistent and asymptotically normal (CAN) over the whole model _M_ ( _CAR_ ). We have that (21) is a subset of the orthogonal complement of the nuisance tangent space of _η_ in the observed data model with _G_<sup>¯</sup> known. However, by CAR, the tangent space _TCAR_ ( _PFX ,G_ ) of _G_ only assuming ( **??** ) (i.e, CAR) is also contained in the orthogonal complement of the nuisance tangent space of _η_ in the observed data model with _G_ known. In fact, our representation theorem (Theorem 1.1) shows that adding the tangent space _TCAR_ ( _PFX ,G_ ) to (21) yields the complete orthogonal complement of the nuisance tangent space of _η_ in the model with _G_ known. The tangent space _TCAR_ ( _PFX ,G_ ) of the conditional distribution _G_ of _C_ , given _X_ , consists of all functions of _Y_ with conditional mean zero, given _X_ , w.r.t. _G_ .

We will now derive a representation of the tangent space _TCAR_ ( _PFX ,G_ ) and determine the projection onto _TCAR_ ( _PFX ,G_ ). Our derivation yields an elegant (and easyto-understand) proof of a very important fundamental result used throughout this book. We will do this in the general situation where we have observed data ( _T_<sup>˜</sup> = min( _T, C_ ) _,_ ∆= _I_ ( _C ≥ T_ ) _, X_<sup>¯</sup> ( _T_<sup>˜</sup> )) and the full data structure _X_<sup>¯</sup> ( _T_ ) = _{X_ ( _s_ ) : _s ≤ T }_ , where _T_ is possibly random: in the current example, we have _T_ = _p_ fixed. We define _C_ = _∞_ if _C ≥ T_ so that _C_ is always observed. In the current example this implies that _C_ can never take value _p_ and _A_ ( _p_ ) is a deterministic function of _A_ ( _p −_ 1). Let _A_ ( _j_ ) = _I_ ( _C ≤ j_ ) so that _dA_ ( _j_ ) = _I_ ( _C_ = _j_ ), _j_ = 0 _, . . . , p_ . Let _F_ ( _j_ ) = ( _A_<sup>¯</sup> ( _j −_ 1) _, X_<sup>¯</sup> (min( _j, C_ ))) be the history observed up and including time _j_ . Let _α_ ( _j | F_ ( _j_ )) = _E_ ( _dA_ ( _j_ ) _| F_ ( _j_ )) be the probability that _C_ = _j_ , given the history _F_ ( _j_ ). Note that


33

where _λC_ ( _j | X_<sup>¯</sup> ( _j_ )) is the hazard of _C_ , given _X_ at time _j_ , which by CAR only depends on _X_ through _X_<sup>¯</sup> ( _j_ ). Under CAR, the _G_ part of the likelihood of _Y_ is given by


Since _α_ ( _j | F_ ( _j_ ))<sup>_dA_(</sup><sup>_j_)</sup> _{_ 1 _− α_ ( _j | F_ ( _j_ )) _}_<sup>1</sup><sup>_−dA_(</sup><sup>_j_)</sup> is just a Bernoulli likelihood for the random variable _dA_ ( _j_ ) with probability _α_ ( _j | F_ ( _j_ )), it follows that the tangent space of _α_ ( _j | F_ ( _j_ )) is the space of all functions of ( _dA_ ( _j_ ) _, F_ ( _j_ )) with conditional mean zero, given _F_ ( _j_ ). Straightforward algebra shows that any such function can be written as


Thus, the tangent space of the parameter _α_ ( _j | F_ ( _j_ )) equals


where _H_ ranges over all functions of _F_ ( _j_ ) for which each element of _TCAR,j_ has finite variance. By factorization of the likelihood (22), we have that


Equivalently,


where


Note that _I_ ( _C_ = _j_ ) = _I_ ( _C_ = _j,_ ∆= 0) for _j < p_ .

Thus, the complete orthogonal complement of the nuisance tangent space of _η_ in the observed data model with _G_ known is given by:


This shows that in the observed data model with _G_ known we have access to a rich class (25) of estimating functions for _α without_ a nuisance parameter, namely any choice of _h, H_ provides an estimating function for _α_ .

The orthogonal complement of the nuisance parameter ( _η, G_ ) in _M_ ( _CAR_ ) is the subspace of (25) consisting of the functions in (25) which are _also_ orthogonal to _G_ . Thus this space is given by:


34

where _Hopt,h_ is chosen so that<sup>�</sup><sup>_p_</sup> _j_ =0<sup>_Hopt,h_(</sup><sup>_j,X_¯(</sup><sup>_j_))</sup><sup>_dMG_(</sup><sup>_j_)equalstheprojectionof</sup> _h_ ( _X_<sup>_∗_</sup> ) _ϵ_ ( _α_ ) _G_ <u>¯(</u> _p_ <u>∆</u> _|X_ )<sup>onto</sup><sup>_T_</sup> _CAR_<sup>(</sup><sup>_P_</sup> _FX ,G_<sup>)intheHilbertspace</sup><sup>_L_</sup> 0<sup>2(</sup><sup>_PF_</sup> _X_<sup>_,G_).</sup> We will now derive this projection. By representation (24) of _TCAR_ , we have that


The projection onto _TCAR,j_ is obtained by first projecting on all functions of ( _dA_ ( _j_ ) _, F_ ( _j_ )) and subsequently subtracting its conditional expectation, given _F_ ( _j_ ),


where we used short hand notation for _IC_ 0( _Y | G, D_ ). By (23), this can be written as


Finally, we note that _E_ ( _IC_ 0( _D_ ) _| dA_ ( _j_ ) = 1 _, F_ ( _j_ )) = 0 since _dA_ ( _j_ ) = 1 implies ∆= 0 for _j ≤ p −_ 1. This proves that


This can be represented as<sup>�</sup><sup>_p_</sup> _j_ =0<sup>_−_1</sup><sup>_Hopt,D_(</sup><sup>_j, F_(</sup><sup>_j_))</sup><sup>_dMG_(</sup><sup>_j_)with</sup>


where, by definition, _G_<sup>¯</sup> ( _j_ + 1 _| X_ ) = _P_ ( _C > j | X_ ). We also note that by CAR _QX,h ≡ E_ ( _Dh_ ( _X | α_ ) _| X_<sup>¯</sup> ( _j_ ) _, C > j_ ) = _E_ ( _Dh_ ( _X | α_ ) _| X_<sup>¯</sup> ( _j_ )) which is thus a parameter of the full data distribution _FX_ .

We conclude that the orthogonal complement of the nuisance parameter ( _η, G_ ) in the model _M_ ( _CAR_ ) is given by


Each of the elements, indexed by _h_ , in this orthogonal complement of the nuisance tangent space implies an estimating function for _α_ (and a corresponding influence curve) with nuisance parameters being _G_ and the full data parameter _QX,h_ . Without additional assumptions on the full data model and censoring mechanism, neither of these two nuisance parameters can be reasonably well-estimated in practice. This shows that no practical estimators exist in model _M_ ( _CAR_ ).

Above, we formally proved the following fundamental results for the general rightcensored data structure ( _T,_<sup>˜</sup> ∆ _, X_<sup>¯</sup> ( _T_<sup>˜</sup> )) for the case where censoring is discrete:

35

**Theorem 1.2.** _Let R_ ( _t_ ) = _I_ ( _T ≤ t_ ) _for a time variable T . Let X_ ( _t_ ) _be a timedependent process including R_ ( _t_ ) _. Let X_ = _X_<sup>¯</sup> ( _T_ ) _be the full data. We have observed data Y_ = ( _T_<sup>˜</sup> = min( _C, T_ ) _,_ ∆= _I_ ( _T ≤ C_ ) _, X_<sup>¯</sup> ( _T_<sup>˜</sup> )) _, where C is a univariate discrete variable with conditional distribution G_ ( _· | X_ ) _, given X. Let A_ ( _t_ ) = _I_ ( _C ≤ t_ ) _, where we define C_ = _∞ if C ≥ T so that C is always observed. Let F_ ( _t_ ) = ( _A_<sup>¯</sup> ( _t−_ ) _, X_<sup>¯</sup> (min( _t, C_ ))) _be the history observed up to time t._

_Assume CAR on G: E_ ( _dA_ ( _t_ ) _| A_<sup>¯</sup> ( _t−_ ) _, X_ ) = _E_ ( _dA_ ( _t_ ) _| F_ ( _t_ )) _or equivalently, for t ≤ T ,_

_λC|X_ ( _t | X_ ) _≡ P_ ( _C_ = _t | C ≥ t, X_ ) = _m_ ( _t, X_<sup>¯</sup> ( _t_ ))

_for some measurable function m. Then, the tangent space TCAR_ ( _PFX ,G_ ) _of G is given by_


_where dMG_ ( _u_ ) = _I_ ( _C ∈ du,_ ∆= 0) _− I_ ( _T_<sup>˜</sup> _≥ u_ ) _λC|X_ ( _du | X_ ) _. For any function V_ ( _Y_ ) _, we have that_ Π( _V | TCAR_ ) _is given by_


**Remark:** For the data structure _Y_ of theorem 1.2 any variable _V_ ( _Y_ ) can be written as ∆ _d_ 1( _X_ ) + (1 _−_ ∆) _V_ 2( _X_<sup>¯</sup> ( _C_ ) _, C_ ) for some functions _d_ 1 and _V_ 2. It follows that _E_ [ _V_ ( _Y_ ) _| dA_ ( _u_ ) = 1 _, F_ ( _u_ )] = _V_ 2( _X_<sup>¯</sup> ( _u_ ) _, u_ ) is actually a deterministic function of _V_ ( _Y_ ).

If _G_ is actually continuous, then the _G_ part of the likelihood of _Y_ is defined as the partial likelihood of _A_ ( _t_ ), w.r.t. the left-continuous history _F_ ( _t−_ ) as in Andersen, Borgan, Gill and Keiding (1993), if in theorem 1.2 we replace _F_ ( _u_ ) and _F_ ( _t_ ) by _F_ ( _u−_ ) and _F_ ( _t−_ ).

The formulas for _TCAR_ and the projection onto _TCAR_ in Theorem 1.2 can be applied to the continuous case as well, but the proof of the representation of _TCAR_ involves calculating the scores from this partial likelihood, and the projection formula needs to be formally defined and proved, taking into account possible measurability conditions needed to define the conditional expectations. A formal treatment of the continuous case is given in van der Vaart (2001). Since the latter is beyond the scope and purpose of this book, we will avoid stating these continuous projection results as theorems, but still use them to define the corresponding estimating functions. □

---

[← What’s so great about Tnuis⊥(P)?](30-what-s-so-great-about-tnuis-p.md) · [Up: contents](index.md) · [2 Robustness of Estimating Functions →](32-2-robustness-of-estimating-functions.md)
