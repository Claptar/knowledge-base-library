---
title: 4 Right Censored Data Structure (Cont’d)
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Right Censored Data Structure (Cont’d)

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let _X_ ( _t_ ) denote the time-dependent full data process of interest, and _T_ be an endpoint of this process. Then the full data structure is defined as


We observe data _O_ = ( _T_<sup>˜</sup> = min( _T, C_ ) _,_ ∆= _I_ ( _T ≤ C_ ) _, X_<sup>¯</sup> ( _T_<sup>˜</sup> )) = _φ_ ( _C, X_ ), where _C_ is a censoring variable for a known _φ_ . Then we have _O ∼ PFX ,GC|X_ . The full data model: _FX ∈ M_<sup>_F_</sup> .


Or if _M_<sup>_F_</sup> is nonparametric, _eg._ (2). _M_<sup>_F_</sup> = _{FX_ : _λT |Z_ ( _t|Z_ ) = _λ_ 0( _t_ ) _e_<sup>_βZ_</sup> _}_ .

To find the full data distribution, we need the parameter of interest: _µ_ : _M_<sup>_F_</sup> _→R_<sup>_k_</sup> , _eg._


CAR: for _t < T, λC|X_ ( _t|X_ ) = _m_ ( _t, X_<sup>¯</sup> ( _t_ )) for some function _m_ . Let _FX_ be part of _f_ ( _o_ ) = _LFX_ ( _o_ ) _g_ ( _o|X_ ), then the likelihood can be written as


The content in the square bracket is the probability of seeing _X_ ( _t_ ) given the past.

**Example:** Observed data _O_ : ( _T,_<sup>˜</sup> ∆ _, W_ ), where _W_ is baseline covariates. By CAR, _C ⊥ T |W_ . Let _M_<sup>_F_</sup> = _nonparametric, µ_ ( _FT,W_ ) _≡ P_ ( _T > t_ 0). Then we can use Kaplan-Meier estimator _P_<sup>ˆ</sup> ( _T > t_ 0 _|W_ = _w_ ): because _EW P_ ( _T > t_ 0 _|W_ ) = _P_ ( _T > t_ 0), then


when _W_ is discrete with outcome _x_ 1 _, . . . , xk_ .

However, when _W_ is continuous or has many categories, the situation will be much more complicated. By the curse of dimensionality, we can only construct sensible estimators of _µ_ ( _FX_ ) by making model assumptions on either _λC_ ( _t|X_ ) or _fX_ ( _x_ ).

Define _A_ ( _t_ ) = _I_ ( _T_<sup>˜</sup> _≤ t,_ ∆= 0) which is a counting process of censoring. Then the partial likelihood is given by


56

We can model the intensity of _A_ ( _t_ ) w.r.t. ( _X_<sup>¯</sup> _A_ ( _t_ ) _, A_<sup>¯</sup> ( _t−_ )). With a multiplicative intensity model:


where _λ_ 0( _t_ ) _e_<sup>_αL_(</sup><sup>_t_)</sup> = _Pr_ ( _C_ = _t|C ≥ t, X_<sup>¯</sup> ( _t_ )). Then _L_ ( _t_ ) = _f_ ( _X_<sup>¯</sup> ( _t_ )) for some function _f_ , _XA_ ( _t_ ) = _X_ (min( _t, T_<sup>˜</sup> )).

If censoring _A_ ( _t_ ) only jumps at discrete times _t_ 1 _< t_ 2 _< · · · < tM_ , then using logistic model


where _−f_ ( _L_ ( _tj_ ) _|α_ ) could be _−α_ 1( _tj_ ) + _α_ 2 _L_ ( _tj_ ). Note, by CAR, _E_ ( _∂A_ ( _t_ ) _|A_<sup>¯</sup> ( _t_ ) = 0 _, X_<sup>¯</sup> ( _t_ )) = _P_ ( _C_ = _t|C ≥ t, X_<sup>¯</sup> ( _t_ )) = _λC|X_ ( _t|X_ ).

Class Notes: Merrill Birkner, April 21, 2004

Observed data:


where _X_ ( _t_ ) = ( _I_ ( _T ≤ t_ ) _, L_ ( _t_ )).

The Full data model _M_<sup>_F_</sup> and let _µ_ ( _FX_ ) be the full data parameter. For example:

1. _M_<sup>_F_</sup> is nonparametric _µ_ ( _FX_ ) = _ρ_ ( _L_ 1 _, L_ 2)

2. _M_<sup>_F_</sup> = _{FX_ : _EFX_ ( _Y − m_ ( _Z|β_ 0) _|Z_ ) = 0 _}_ , _µ_ ( _FX_ ) = _β_ 0

This is equivalent to mean regression.

3. _M_<sup>_F_</sup> = _{FX_ : _EFX_ ( _K_ ( _Y − m_ ( _Z|β_ 0) _|Z_ ) = 0) _}_ , _µ_ ( _FX_ ) = _β_ 0. This is equivalent, for example, to median/quantile regression[depending on _K_ ]

4. _M_<sup>_F_</sup> = _{FX_ : _λT |Z_ ( _t|Z_ ) = _λ_ 0( _t_ ) _exp_ ( _β_ 0 _Z_ ) _}_ , _µ_ ( _FX_ ) = _β_ 0 This is the Cox proportional hazards model.

**What is Y?** It could be log survival, and therefore log(t).

In general _Y_ = _f_ ( _X_<sup>¯</sup> ( _T_ )) for some _f_

*********************************************************************

Question: If there is no censoring, what is the parameter of interest? What are full data estimating functions for the parameter of interest _µ_ ( _FX_ )?

Full data estimating functions _Dh_ ( _X, µ|η_ ), where _h ∈H_ is an index ranging over an index set.

We are looking for the orthoganol complement of the nuisance scores in _L_<sup>2</sup> 0<sup>(</sup><sup>_P_0).</sup> For example, if _M_<sup>_F_</sup> = _{FX_ : _EFX_ ( _K_ ( _ϵ_ ( _β_ 0)) _|Z_ ) = 0 _}_ and _β_ 0 is the paramter of interest, then the class of estimating functions is given by


where _h_ can be any function of _Z_ .

57

In a nonparametric model with _µ_ = _P_ ( _T > t_ ), there is only one estimating function _D_ ( _x, µ_ ) = _I_ ( _T > t_ ) _− µ_ . Similarly, if in the nonparametric model the paraeter of interest is given by _µ_ ( _Fx_ ) = _ρ_ ( _L_ 1 _, L_ 2) = � _E_ ( _L_ 1( _t_ ) _L_ 2( _t_ )) _w_ ( _t_ ) _dt_ , then we can find the single estimating function as the influence curve of an ad hoc (empirical) estimator of this parameter.


where _N_ ( _t_ ) = _I_ ( _T ≤ t_ ) Now, the class of estimating functions is given by


where _dM_ ( _t_ ) = _dN_ ( _t_ ) _−E_ ( _dN_ ( _t_ ) _|Z, N_<sup>¯</sup> ( _t_ )). This can be argued by noting that the model corresponds with a Bernoulli regression at each fixed _t_ .

In the above equation, the nuisance parameter is the baseline hazard _λ_ 0 Refer to Chapter 2 of van der Laan and Robins ******************************************************************* What do we do when there is censoring?

*First it is important to understand the parameter of interest in the full data world. We need the CAR assumption: _λC|X_ ( _t|X_ ) = _m_ ( _t, X_<sup>¯</sup> ( _t_ )) for a function _m_ . Why don’t we use this MLE based on a completely specified full data model? We are only interested in certain parameters and the MLE makes model assumptions. The person who does MLE did not model the parameter of interest. Putting down model of a small piece of data structure. Marginal distribution of t: _µ_ ( _Fx_ ) = _P_ ( _T > t_ 0)

#### **Notes re. Maximum Likelihood vs Previously Mentioned Method**

- The Maximum Likelihood method factorizes the full data and censoring, but it does not care about censoring. This is equivalent to a Bayesian point of view where one does not care about the other part of the likelihood.

- We also know that the censoring is independent of survival and covariates. One who performs only the maximum likelihood method cannot do KM on all of those levels.

- The maximum likelihood is asymptotically efficient if it works, but the MLE in this case (when taking into account censoring and multiple covariates [with potentially many levels]) it is biased. This is refered to as the curse of dimensionality.

- The ML tries to be globally efficient and therefore it breaks down when the model becomes too high dimensional.

- KM within every cell unbiased and very variable. You increase the variance when you increase the dimensions.

- A person who performs the maximum likelihood method needs to model the error distribution. We do not have to assume a parametric model for the error distribution.

- Double Robust: If either the censoring model or likelihood is correct you get a consistent locally efficient estimator.

58

#### **IPCW Estimating Functions:**


where _G_<sup>¯</sup> ( _t_<sup>_−_</sup> _|X_ ) = _exp_ ( _−_ �0 _t_<sup>_λ_(</sup><sup>_s|x_)</sup><sup>_ds_.Wecanestimatethecensoringmechanismbymodellingthe</sup> censoring intensity _E_ ( _dA_ ( _t_ ) _|Ft_ ) and fitting the corresponding partial likelihood Π _t_ ( _E_ ( _dA_ ( _t_ ) _|Ft_ )<sup>_dA_(</sup><sup>_t_)</sup> (1 _− E_ ( _dA_ ( _t_ )) _|Ft_ )<sup>1</sup><sup>_−dA_(</sup><sup>_t_)</sup> .

It is a function of the observed data but after taking the conditional expectation, given _X_ , you get back the estimating function of the full data. That is why it is unbiased, because it is unbiased in the full data world.

Estimating Functions for Right Censored Data, Keith Betts, April 23, 2004

Define the observed data structure as:


Model is just as Model Right Censored data


Define _µ_ ( _Fx_ ) as a paramter defined on _M_<sup>_F_</sup>

---

[← Example: Survival Analysis with no Censoring](43-example-survival-analysis-with-no-censoring.md) · [Up: contents](index.md) · [IPCW-estimating functions →](45-ipcw-estimating-functions.md)
