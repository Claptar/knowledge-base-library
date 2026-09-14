---
title: Identifiability and Estimation in Survival Analysis
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Identifiability and Estimation in Survival Analysis

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We first note that if censoring occurs before some time _b_ , then it should be very difficult to estimate the survival function after _b_ , because we have no data on _T_ conditional on _T > b_ . We therefore consider some _b_ such that _P_ ( _T_<sup>˜</sup> _> b_ ) _>_ 0, and will consider estimating the surival function _S_ on [0 _, b_ ].

Let _F_ 1 = _{f_ ( _O_ ) = 1( _T_<sup>˜</sup> _≤ u,_ ∆= 1) : 0 _≤ u ≤ b}_ . Let _F_ 2 = _{f_ ( _O_ ) = 1( _T_<sup>˜</sup> _≥ u_ ) : 0 _≤ u ≤ b_ ) _}_ . Let _F_ = _F_ 1 _∪F_ 2.

Then for _P_ 1( _t_ ) = _P_ ( _T_<sup>˜</sup> _≤ t,_ ∆= 1) and _P_ 2( _t_ ) = _P_ ( _T_<sup>˜</sup> _≥ t_ ), the map _P →_ ( _P_ 1 _, P_ 2) maps _l_<sup>_∞_</sup> ( _F_ ) (with the norm _∥· ∥F_ ) to the bivariate space on cadlag functions _D_ [0 _, b_ ]<sup>2</sup> (with the supreumum norm). Because this map is linear and continuous, it is equal to its own Hadamard derivative.

Because we’ve assumed that _P_ ( _T_<sup>˜</sup> _> b_ ) _>_ 0, _P_ 2 is bounded away from _O_ on [0 _, b_ ]. From our previous notes, this implies the map ( _P_ 1 _, P_ 2) _→_ �0 _· P_ 21( _u_ )<sup>_dP_1(</sup><sup>_u_)from</sup><sup>_D_[0</sup><sup>_, b_]2</sup> to _D_ [0 _, b_ ] is Hadamard differentiable (using the supremum norm in the domain and range spaces) at ( _P_ 1 _, P_ 2) with derivative map ( _α, β_ ) _→_ �0 _· B_ <u>1</u><sup>_dα −_</sup> <u>�0</u> _· Bβ_<sup>2</sup><sup>_dP_1.However,</sup> the independence of _T_ and _C_ implies that �0 _· P_ 21( _u_ )<sup>_dP_1(</sup><sup>_u_)=</sup> <u>�0</u> _·_ 1 _−F_ <u>1(</u> _u−_ )<sup>_dF_(</sup><sup>_u_)</sup><sup>_≡_Λ,the</sup> _cumulative hazard function_ . For _φ_ : _P →_ ( _P_ 1 _, P_ 2) _→_ �0 _· P_ 21( _u_ )<sup>_dP_1(</sup><sup>_u_)(mapping</sup><sup>_l∞_(</sup><sup>_F_)</sup> to _D_ [0 _, b_ ]), this suggests estimating Λ( _·_ ) = _φ_ ( _P_ )( _·_ ) with Λ _n_ ( _·_ ) _≡ φ_ ( _Pn_ )( _·_ ), and this is called the _Nelson-Aalen estimator_ .

15

For _n_ observations, let _t_ 1 _, ..., tm_ denote the ordered times at which failures occur (so ( _T_<sup>˜</sup> = _ti,_ ∆= 1), and let _ni_ denote the number of observations still at risk of failing at time _ti_ (so _ni_ =<sup><u>�</u></sup><sup>_n_</sup> _j_ =1<sup>1( ˜</sup><sup>_T≥ti_).ThentheNelson-Aalenestimatorcanbewrittenas</sup> Λ _n_ ( _t_ ) =<sup>�</sup> _{i_ : _ti≤t} ndii_<sup>.</sup> **Theorem 0.15.** _The Nelson-Aalen estimator_ Λ _n_ ( _t_ ) _is an asymptotically linear estimator of_ Λ( _t_ ) _for_ 0 _≤ t ≤ b with influence curve given by:_ <u>1</u> 1( _T_<sup>˜</sup> _<u>≥u</u>_ <u>)</u> _−P_ 2( _u_ <u>))</u> _IC_ ( _O|P_ ) = �0 _t P_ 2( _u_ )<sup>_d_(1( ˜</sup><sup>_T≤u,_∆= 1)</sup><sup>_−P_1(</sup><sup>_u_))</sup><sup>_−_</sup> �0 _t P_ 2( _u_ )<sup>2</sup> _dP_ 1( _u_ ) _._

**proof** : This follows from applying the functional delta method to _φ_ : _P →_ ( _P_ 1 _, P_ 2) _→_ �0 _t P_ 21( _u_ )<sup>_dP_1(</sup><sup>_u_)(mapping(</sup><sup>_l∞_(</sup><sup>_F_)</sup><sup>_, ∥· ∥F_)to</sup><sup>_R_),asitcanbeshownthat</sup><sup>_F_isaDonsker</sup> class. Technically we use the chain rule, but the mapping _P →_ ( _P_ 1 _, P_ 2) from _l_<sup>_∞_</sup> ( _F_ ) to _D_ [0 _, b_ ]<sup>2</sup> is equal to its own derivative. Consider _G ∈ l_<sup>_∞_</sup> ( _F_ ), and the functions _f_ 1 _,u_ = 1( _T_<sup>˜</sup> _≤ t,_ ∆= 1) _∈F_ 1 and _f_ 2 _,u_ = 1( _T_<sup>˜</sup> _≥ u_ ) _∈F_ 2. The previously given Hadamard differentiability of the cumulative hazard map tells us that the Hadamard derivative of _φ_ at _P_ , denoted by _dφP_ : _l_<sup>_∞_</sup> ( _F_ ) _→R_ , is given by _dφP_ ( _G_ ) = �0 _t P_ 2(1 _u_ ))<sup>_dG_(</sup><sup>_f_1</sup><sup>_,u_)</sup><sup>_−_</sup> �0 _t GB_ <u>(</u><sup>2</sup> _<u>f</u>_ (2 _u,u_ ))<sup>_dP_1(</sup><sup>_u_).Thedesiredresultfollowsfromthefunctionaldeltamethod,recall-</sup> ing the influence curve is _IC_ ( _O|P_ ) = _dφP_ ( _G_ 1 _,O_ ), where _G_ 1 _,_ 0 is the empirical process for the single observation _O_ , so _G_ 1 _,O_ ( _f_ 1 _,u_ ) = 1( _T_<sup>˜</sup> _≤ u,_ ∆= 1) _− P_ 1( _u_ ) and _G_ 1 _,O_ ( _f_ 2 _,u_ ) = 1( _T_<sup>˜</sup> _≥ u_ ) _− P_ 2( _u_ ). □ From the definition of Λ, 1 _−_ �0 _·_ 1 _−F_ <u>1(</u> _u−_ )<sup>_d_Λ(</sup><sup>_u_)=</sup><sup>_S_(</sup><sup>_·_).Fromtherepresentationofthe</sup> product integral in the previous notes as the unique solution of the Volterra equation, this implies that _S_ ( _·_ ) = Π0 _≤u≤·_ (1 _− d_ Λ( _u_ )), where Π here denotes the product integral. As Λ _∈ D_ [0 _, b_ ] was shown to be identifiable from _P_ through ( _P_ 1 _, P_ 2), this shows that _S ∈ D_ [0 _, b_ ] is also identifiable from _P_ . So for _ψ_ : _P →_ ( _P_ 1 _, P_ 2) _→→_ Π0 _≤u≤·_ (1 _− d_ Λ( _u_ )) (mapping _l_<sup>_∞_</sup> ( _F_ ) to _D_ [0 _, b_ ]), _S_ ( _·_ ) = _ψ_ ( _P_ )( _·_ ). This suggests estimating _S_ ( _·_ ) with _Sn_ ( _·_ ) _≡ ψ_ ( _Pn_ )( _·_ ), called the _Kaplan-Meier estimator_ . Using the previous notation, the Kapalan-Meier estimator can be written as _Sn_ ( _t_ ) = Π _{i_ : _ti≤t}_ (1 _− n_<sup>_<u>di</u>_</sup> _i_<sup>).</sup>


**proof** : We again apply the functional delta method to the map _ψ_ : _P →_ ( _P_ 1 _, P_ 2) _→_ Λ _→_ Π0 _≤s≤t_ (1 _− d_ Λ( _s_ )) = _S_ ( _t_ ) from ( _l_<sup>_∞_</sup> ( _F_ ) _, ∥· ∥F_ ) to _R_ , as it can be shown that _F_ is a Donsker class. In our use of the chain rule, the mapping _P →_ ( _P_ 1 _, P_ 2) from _l_<sup>_∞_</sup> ( _F_ ) to _D_ [0 _, b_ ]<sup>2</sup> is equal to its own derivative. Consider _G ∈ l_<sup>_∞_</sup> ( _F_ ), and the functions _f_ 1 _,s_ = 1( _T_<sup>˜</sup> _≤ s,_ ∆= 1) _∈F_ 1 and _f_ 2 _,s_ = 1( _T_<sup>˜</sup> _≥ s_ ) _∈F_ 2. The previously given Hadamard differentiability of the composition of the cumulative hazard function and the product integral gives that _ψ_ is Hadamard differentiable at _P_ , with Hadamard derivative denoted by _dψP_ : _l_<sup>_∞_</sup> ( _F_ ) _→R_ , given by:


16


Note that the _−_ enters trivially from the chain rule because we are applying the product integral map to _−_ Λ. The _S_ ( _t_ ) comes from the fact that Π0 _≤u<s_ (1 _− d_ Λ( _u_ ))Π _s<t_ (1 _− d_ Λ( _u_ )) = Π0 _≤u≤t_ (1 _− d_ Λ( _u_ )) = _S_ ( _t_ ) because we have assumed that _S_ is a continuous distribution. The desired result follows from the functional delta method, recalling the influence curve is _IC_ ( _O|P_ ) = _dφP_ ( _G_ 1 _,O_ ), where _G_ 1 _,_ 0 is the empirical process for the single observation _O_ , so _G_ 1 _,O_ ( _f_ 1 _,s_ ) = 1( _T_<sup>˜</sup> _≤ s,_ ∆= 1) _− P_ 1( _s_ ) and _G_ 1 _,O_ ( _f_ 2 _,s_ ) = 1( _T_<sup>˜</sup> _≥ s_ ) _− P_ 2( _s_ ). □

**Lecture of February 22, 2005**

#### **Functional** _δ_ **-method for analyzing Z-estimators**

The general methodology for analyzing Z-estimators discussed in the last lecture requires that the map _θ −→ U_ ( _θ, P_ ) be Frech´et differentiable. This requirement is easily met if _θ_ is finite-dimensional, but may be difficult to establish in the infinitedimensional case. We will now discuss another approach for analyzing the asympotic behavior of Z-estimators that is based on the functional _δ_ -method and that does not require the map _θ −→ U_ ( _θ, P_ ) to be Frech´et differentiable.

Suppose we observe _n_ i.i.d. copies _O_ 1 _, ..., On_ of _O ∼ P_ . Consider the parametef of interest _θ_ ( _P_ ) _∈_ ( _D_ 1 _, ∥∥_ 1). Let _P ∈_ ( _D_ 2 _, ∥∥_ 2), e.g. ( _D_ 2 _, ∥∥_ 2) = ( _l_<sup>_∞_</sup> ( _F_ ) _, ∥∥F_ ) for a sufficiently rich class of functions _F_ . Suppose there exists a mapping _U_ : ( _D_ 1 _, ∥∥_ 1 ) _×_ ( _D_ 2 _, ∥∥_ 2) _−→_ ( _D_ 3 _, ∥∥_ 3) such that _θ_ ( _P_ ) can be defined as the solution of _U_ ( _θ, P_ ) = 0. Typically, we will have that ( _D_ 3 _, ∥∥_ 3) = ( _D_ 1 _, ∥∥_ 1), although this is not required. Let _ϕ_ : ( _D_ 2 _, ∥∥_ 2) _−→_ ( _D_ 1 _, ∥∥_ 1) be the mapping that maps _P_ into the solution _θ_ of the equation _U_ ( _θ, P_ ) = 0. Now let the estimator _θn_ be defined as _θn_ = _ϕ_ ( _Pn_ ), i.e. let _θn_ be the solution of _U_ ( _θn, Pn_ ) = 0.

As before, we want to prove that<sup>_√_</sup> _<u>n</u>_ <u>(</u> _θn − θ_ ) =<sup>_√_</sup> _<u>n</u>_ <u>(</u> _ϕ_ ( _Pn_ ) _− ϕ_ ( _P_ )) = _D⇒_ Z in ( _D_ 1 _, ∥∥_ 1 _, B_ ) as _n →∞_ . To apply the functional _δ_ -method, we first use empirical process theory to verify that _Gn_ =<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Pn − P_ ) = _D⇒ G_ in ( _D_ 2 _, ∥∥_ 2). Next we need to establish that the map _ϕ_ is Hadamard differentiable tangentially to a subspace D<sup>_∗_</sup> 2<sup>=(</sup><sup>_D_</sup> 2<sup>_∗, ∥∥_2)</sup><sup>_⊆_(</sup><sup>_D_2</sup><sup>_, ∥∥_2)suchthat</sup><sup>_G∈_D</sup> 2<sup>_∗_,i.e.weneedtoshowthatfor</sup> any sequences _{hn_ =<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Pn_<sup>_′−P ′_)</sup><sup>_}n≥_1with</sup><sup>_hn→h_forsome</sup><sup>_h∈_D</sup> 2<sup>_∗_wehavethat</sup> _∥_<sup>_√_</sup> _<u>n</u>_ <u>(</u> _ϕ_ ( _Pn_<sup>_′_)</sup><sup>_−ϕ_(</sup><sup>_P ′_))</sup><sup>_−dϕ_(</sup><sup>_P ′_)(</sup><sup>_h_)</sup><sup>_∥_1</sup><sup>_→_0.Wewilllayoutaroadmapoffivesteps,</sup> A1-A5, to establish the required differentiability.

Consider the same setup as for the proof from last lecture:


17

To establish this continuity condition on _ϕ_ see for example the consistency proof from last lecture.


Here you can use that, by A1, _θn_<sup>_′→θ′_=</sup><sup>_ϕ_(</sup><sup>_P ′_).Now A2 implies that the right-hand</sup> side and hence also the left-hand side in (1) converges to _− dP_<sup>_<u>d</u>′U_(</sup><sup>_θ′, P ′_)(</sup><sup>_h_).</sup>

<u>A3:</u> Show that there exists a linear mapping _dfn_ : ( _D_ 1 _, ∥∥_ 1) _−→_ ( _D_ 3 _, ∥∥_ 3), possibly depending on _θn_<sup>_′_,</sup><sup>_θ′_,and</sup><sup>_P_,suchthat</sup><sup>_U_(</sup><sup>_θ_</sup> _n_<sup>_′, P ′_)</sup><sup>_−U_(</sup><sup>_θ′, P ′_) =</sup><sup>_dfn_(</sup><sup>_θn−θ_).</sup>

Write _U_ ( _θn_<sup>_′, P ′_)</sup><sup>_−U_(</sup><sup>_θ′, P ′_) =</sup><sup>_f_(</sup><sup>_θ_</sup> _n_<sup>_′_)</sup><sup>_−f_(</sup><sup>_θ′_).Considertheexample</sup>


Then


where _dfn_ ( _θn_<sup>_′−θ′_)dependson</sup><sup>_θ_</sup> _n_<sup>_′_,</sup><sup>_θ′_,and</sup><sup>_P_,butislinearin</sup><sup>_θ_</sup> _n_<sup>_′−θ′_.</sup> Note that this step does not require any Frech´et differentiability of the map _θ −→ U_ ( _θ, P_ ). Now A3 implies that _dfn_ (<sup>_√_</sup> _<u>n</u>_ <u>(</u> _θn_<sup>_′−θ′_))</sup><sup>_→−_</sup> _dP_<sup>_<u>d</u>′U_(</sup><sup>_θ′, P ′_)(</sup><sup>_h_),orequivalently</sup> that _dfn_ (<sup>_√_</sup> _<u>n</u>_ <u>(</u> _θn_<sup>_′−θ′_)) +</sup> _dPd_<sup>_′U_(</sup><sup>_θ′, P ′_)(</sup><sup>_h_)</sup><sup>_→_0</sup>

<u>A4:</u> Show that _dfn_ is 1-1 and onto for all _n_ and that lim sup _n ∥ dfn_<sup>_−_1</sup> _∥< ∞_ .

This type of continuous differentiability of _dfn_ and the linearity of _dfn_<sup>_−_1</sup> imply that


<u>A5:</u> Show that, for any _g_ , _θn_<sup>_′→θ′_=</sup><sup>_⇒df_</sup> _n_<sup>_−_1</sup> _− df_<sup>_−_1</sup> ( _g_ ) _→_ 0, where _df_<sup>_−_1</sup> ( _g_ ) = � _dθd_<sup>_U_(</sup><sup>_θ′, P ′_)</sup> � _−_ 1 ( _g_ ).

Now A5 implies that

18


■

Homework 3 Solution, prepared by Dan Rubin

---

[← Survival Analysis](22-survival-analysis.md) · [Up: contents](index.md) · [The Exponential with Censoring →](24-the-exponential-with-censoring.md)
