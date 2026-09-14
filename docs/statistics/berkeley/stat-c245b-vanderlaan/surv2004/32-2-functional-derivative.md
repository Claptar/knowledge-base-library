---
title: 2 Functional Derivative
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Functional Derivative

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

( _T_<sup>�</sup> = _Min_ ( _T, C_ ) _,_ ∆= _I_ ( _T ≤ C_ ))


Then, _S_ ( _t_ 0) = _ϕ_ ( _P_ 1 _, P_ ) _, Sn_ ( _t_ 0) = _ϕ_ ( _P_ 1 _n, P n_ )


Here, we use functional delta-method, which is a generalization of delta-method. **Review: Delta-method:** This is a first-order approximation.

39


where


We would like to define a derivative of _ϕ_ in the direction h. Example1: _f_ : **R** _→_ **R**


This is the simplest case (Linear mapping). Example2: 2-dim case. _f_ : **R**<sup>**2**</sup> _→_ **R**

Define

Similarly,


Thus, by linearity of _ϕ_ ˙1( _P_ 1 _, P_ ) _,_


A mapping _ϕ_ ˙ is linear :

_ϕ_ ˙ ( _αh_ 1 + _βh_ 2) = _α · ϕ_ ˙ ( _h_ 1) + _β · ϕ_ ˙ ( _h_ 2) For example, Is _ϕ_ ˙ ( _h_ )( _t_ ) = �0 _t_<sup>_h_(</sup><sup>_s_)</sup><sup>_s_2</sup><sup>_ds_linear?——–Yes,itis.</sup>

Similarly,


40


Thus,


In this way, we can get IC. Once we get IC, we can compute 95-confidence interval, simultaneous confidence region, and so on. Now, we would like to find _ϕ_ ˙1 and _ϕ_ ˙2. Example: ( _T_<sup>�</sup> _i,_ ∆ _i_ ) _, i_ = 1 _,_ 2 _, . . . , n_


41

Thus,


Now, we could get IC of cumulative hazard. Next time, we will apply chain rule for functional derivative, and get influence curve of survival function.

#### **Estimation of Influence Curve of Kaplan Meier using functional derivative 3/15/04**

#### **Joseph Poj Gavinlertvatana**

#### **Objective:**

Derive the influence curve for Kaplan-Meier estimate by writing Kaplan-Meier minus truth as functional derivative of empiral minus truth in first order

Recall setup:

Observe: ( _T_<sup>˜</sup> = _min_ ( _T, c_ ) _,_ ∆= _I_ ( _T ≤ c_ )), assume _T ⊥ c_

Parameter of interest: _S_ ( _t_ ) = _P_ ( _T ≥ t_ ) =<sup>�</sup> _s∈_ (0 _,t_ )<sup>(1</sup><sup>_−∂_</sup> _p_ ¯<sup>_<u>p</u>_</sup> ( _s_<sup>1</sup><sup>_−_</sup><sup><u>(</u></sup><sup>_s_</sup> )<sup><u>)</u>)</sup> where _p_ 1( _t_ ) = _P_ ( _T_<sup>˜</sup> _≤ t,_ ∆= 1) and _p_ ¯( _t_ ) = _P_ ( _T_<sup>˜</sup> _> t_ ) _S_ ( _t_ ) = Φ( _p_ 1 _, pn_ ) estimated by _Sn_ ( _to_ ) = Φ( _p_ 1 _n,_ ¯ _pn_ )

Recall when we did directional derivative last time: Φ( _p_ 1 _, pn_ ) = Φ2[Φ1( _p_ 1 _, pn_ )] where Φ1( _p_ 1 _, pn_ ) = �0 _. ∂p_ ¯ _<u>p</u>_ ( _s_ 1<sup>_−_</sup> <u>(</u> _s_ ))<sup>= Λ(</sup><sup>_·_)</sup> and Φ2(Λ) =<sup>�</sup> _s∈_ (0 _,t_ 0)<sup>(1</sup><sup>_−∂_Λ(</sup><sup>_s_))</sup> Φ( _p_ 1 _, pn_ ) maps data into cumulative hazard Φ2(Λ) maps cumulative hazard into survival

For influence curve, we need to find the directional deriv: ˙Φ( _h_ 1 _,_ ¯ _h_ ) = _∂ϵ∂_<sup>Φ(</sup><sup>_p_1 +</sup><sup>_ϵh_1</sup><sup>_,_¯</sup><sup>_p_+</sup><sup>_ϵh_¯)</sup>

Since Φ( _p_ 1 _, pn_ ) is a composite function, we use the chain rule: ˙Φ( _h_ 1 _,_ ¯ _h_ ) = ˙Φ2[ ˙Φ1( _h_ 1 _,_ ¯ _h_ )] where Φ<sup>˙</sup> 1( _h_ 1 _, h_<sup>¯</sup> ) = _∂ϵ∂_<sup>Φ1(</sup><sup>_p_1 +</sup><sup>_ϵh_1</sup><sup>_,_¯</sup><sup>_p_+</sup><sup>_ϵh_¯)</sup><sup>_|ϵ_=0=</sup> �0 _t hp_ ¯1(( _s∂s−_ ))<sup>_−_</sup> �0 _t h_ ¯($$¯ _sp−_ ( _s_ <u>)</u> _−p_ 1)$$( _∂s_<sup>2</sup> <u>)</u> and Φ<sup>˙</sup> 2( _g_ ) = _∂ϵ∂_<sup>Φ2(Λ +</sup><sup>_ϵg_)</sup><sup>_|ϵ_=0</sup>

To get Φ<sup>˙</sup> 2( _g_ ), we use a telescoping trick e.g.

_a_ 1 _a_ 2 _− b_ 1 _b_ 2 = ( _a_ 1 _− b_ 1) _b_ 2 + _a_ 1( _a_ 2 _− b_ 2) _a_ 1 _a_ 2 _a_ 3 _− b_ 1 _b_ 2 _b_ 3 = ( _a_ 1 _− b_ 1) _b_ 2 _b_ 3 + _a_ 1( _a_ 2 _− b_ 2) _b_ 3 + _a_ 1 _a_ 2( _a_ 3 _− b_ 3) In general:


� _kj_ =1<sup>_aj−_�</sup><sup>_k_</sup> _j_ =1<sup>= �</sup><sup>_k_</sup> _j_ =1<sup>[(�</sup> _l_<sup>_j_</sup> =1<sup>_−_1</sup><sup>_al_)(</sup><sup>_aj−bj_)(�</sup><sup>_k_</sup> _l_ = _j_ +1<sup>_bl_)]</sup> Continuing, we get: ˙Φ2( _g_ ) = lim _s→_ 0 Φ2(Λ+ _ϵgϵ_ <u>)</u> _−_ Φ2(Λ) <u>�</u> _sϵ_ <u>(0</u> _<u>,t</u>_ <u>0)</u><sup>[1</sup><sup>_−_(Λ+</sup><sup>_ϵg_)(</sup><sup>_s_)]</sup><sup>_−_</sup><sup><u>�</u></sup> _sϵ_ <u>(0</u> _<u>,t</u>_ <u>0)</u><sup>[1</sup><sup>_−∂_Λ(</sup><sup>_s_)]</sup> = lim _ϵ→_ 0 _ϵ_ (using telescoping) <u>�</u> _sϵ_ <u>(0</u> _<u>,t</u>_ <u>0)</u><sup>[�</sup> _uϵ_ (0 _,s_ )<sup>(1</sup><sup>_−∂_(Λ+</sup><sup>_ϵg_)(</sup><sup>_u_))][1</sup><sup>_−∂_(Λ+</sup><sup>_ϵg_)(</sup><sup>_s_)</sup><sup>_−_1+</sup><sup>_∂_(Λ)(</sup><sup>_s_)][�</sup> _uϵ_ ( _s,t_ <u>0)</u><sup>(1</sup><sup>_−∂_Λ(</sup><sup>_u_))]</sup> = lim _ϵ→_ 0 _ϵ_ = lim _ϵ→_ 0 _−_ <u>�</u> _sϵ_ (0 _,t_ 0)<sup>[�</sup> _uϵ_ (0 _,s_ )<sup>(1</sup><sup>_−∂_(Λ +</sup><sup>_ϵg_)(</sup><sup>_u_))][</sup><sup>_∂g_(</sup><sup>_s_)][�</sup> _uϵ_ ( _s,t_ 0)<sup>(1</sup><sup>_−∂_Λ(</sup><sup>_u_))]</sup> = _−_ � _sϵ_ (0 _,t_ 0)<sup>[�</sup> _uϵ_ (0 _,s_ )<sup>(1</sup><sup>_−∂_(Λ)(</sup><sup>_u_))][</sup><sup>_∂g_(</sup><sup>_s_)][�</sup> _uϵ_ ( _s,t_ 0)<sup>(1</sup><sup>_−∂_Λ(</sup><sup>_u_))]</sup> <u>(1</u> _−∂_ <u>(Λ)(</u> _u_ <u>))</u> = _−_ � _sϵ_ (0 _,t_ 0) � _uϵ_ (0 _,t_ 0) (1 _−∂_ (Λ)( _s_ ))<sup>_∂g_(</sup><sup>_s_)</sup> = _−_<sup>�</sup> _uϵ_ (0 _,t_ 0)<sup>(1</sup><sup>_−∂_(Λ)(</sup><sup>_u_))</sup> �0 _t_ 0 (1 _−∂∂g_ (Λ)(( _s_ <u>)</u> _s_ )) = _−S_ ( _t_ 0) �0 _t_ 0 (1 _−∂∂g_ (Λ)(( _s_ <u>)</u> _s_ )) If Λ( _s_ ) is continuous, then _∂_ Λ( _s_ ) = 0, so = _−S_ ( _t_ 0) _g_ ( _t_ 0)


Lecture notes March 29, 2004 Vera Klimkovsky klimkovsky@yahoo.com

### **QUANTILE ESTIMATION BASED ON RIGHT-CENSORED DATA**

<u>Data:</u>

( _T_<sup>�</sup> = min( _T, C_ ) _,_ ∆= _I_ ( _T ≤ C_ ))

where _C ⊥ T_ ( _C_ and _T_ are independent), _C ∼ G_ , _T ∼ F_

43

#### <u>Parameter of interest:</u>

_θ_ ( _F_ ) = _F_<sup>_−_1</sup> ( _p_ ) _,_ where _p ∈_ (0 _,_ 1) and _F_<sup>_−_1</sup> ( _p_ ) = inf _{x_ : _F_ ( _x_ ) _≥ p}_

<u>Estimation:</u>

_Fn_ = 1 _− Sn,_ and _Sn_ is Kaplan-Meier estimator. _θn_ = _θ_ ( _Fn_ ) = _Fn_<sup>_−_1(</sup><sup>_p_)</sup>

Now, how do we do the inference? We need to estimate IC. _θn − θ_ = _θ_ ( _Fn_ ) _− θ_ ( _F_ )<sup>_∼_</sup> = _θ_<sup>˙</sup> ( _Fn − F_ ) (using Delta Method) Take a directional derivative: _θ_ ˙ = _dεd_<sup>_θ_(</sup><sup>_F_+</sup><sup>_ε · h_)</sup> �� _ε_ =0 For simplicity, let _Fε_ = _F_ + _εh_ , _θε_ = _θ_ ( _Fε_ ), and _y_ = _F_ ( _θε_ ). Also, note that _Fε_ ( _θε_ ) = _F_ ( _θε_ )+ _εh_ ( _θε_ ) Then,


Substituting _y_ into the expression of limit, and using the fact that


, we get


Note: Above we differentiated the inverse function. What is the derivative of _F_<sup>_−_1</sup> ? Recall:


Differentiate both sides with respect to _y_ :


Applying Chain Rule:

44


So,

Thus,


**Now we are ready for the influence curve.** Applying the first order Taylor expansion:


(Another way to construct confidence interval is to use bootstrap method. However, there are situations when the bootstrap method fails.)

### **SELF-CONSISTENCY EQUATION FOR CENSORED DATA**

_X ∼ Fn, C|X ∼ G_ ( _·|X_ ) where distribution function _G_ is called a censoring mechanism. We observe: _Y_ = _ϕ_ ( _C, X_ ) _∼ PFX ,G_

A random set _C_ ( _Y_ ) is called a coarsening of _X_ if _Pr_ ( _X ∈ C_ ( _Y_ )) = 1 (1)


45

(2)


We say _C_ ( _Y_ ) satisfies _coarsening at random_ (CAR) if _Pr_ ( _X_ = _x|Y_ = _y_ ) = _Pr_ ( _X_ = _x|X ∈ C_ ( _y_ )). Equivalenty, _Pr_ ( _Y_ = _y|X_ = _x_ ) is constant for _x ∈ C_ ( _y_ ). Suppose we have n iid: _Y_ 1 _, . . . , Yn_ . We want to estimate _FX_ ( _A_ ) = _Pr_ ( _X ∈ A_ ). <u>Full data:</u>


<u>Censored data:</u>


Or


Thus,


If we enforce _FX,n_ to be discrete on _{X_ 1 _, . . . , Xm}_ with point masses _p_ 1 _n . . . pmn_ , then _pj,n_ = _PFX,n_ ( _X_ = _xj_ )


for _j_ = 1 _, . . . , m_

The following algorithm can be used to solve this equation:


46

**Truncation** Notes by Keith Betts March 17, 2004

---

[← Simulation](31-simulation.md) · [Up: contents](index.md) · [Situation →](33-situation.md)
