---
title: General approach for constructing an estimator
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# General approach for constructing an estimator

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Consider the following Observations


Full data: _T_<sup>�</sup> _i_ = _min_ ( _Ti, Ci_ ) _Xi_ = ( _Ti, Wi_ ) _i_ = 1 _, . . . , n_ ( _T, W_ ) _∼ Fx C | X ∼ G_ ( _· | X_ ) _≡ P_ ( _C ≤· | X_ ) _O ≡ PFx,G_

Now, the parameter of interest is _ϕ_ 0 = _E_ [ _T | W_ ] or equivalent _E_ [log _T | W_ ]

Coarsening at random on the censoring mechanism: _T ⊥C | W_

Set _k_ : # of bins. From previous results we have


Notice that if _k_ = 1 then the previous equation reduces to _n_<sup><u>1</u></sup> � _ni_ =1<sup>_Ti_</sup>

There is a problem with the used model. It only considers observed dat and acctually that is not the case we want to approach, since we also have censored data. It turns out that we do not have an estimator if we want to do histogram regression.

Assume for a second that we do have such estimators and want to choose among them using crossvalidation as we did before.

**Choosing among estimators** . Consider the following set up _ϕ_ 1( _· | Pn_ ) _, . . . , ϕk_ ( _· | Pn_ ) 1 _, . . . , k_ bins _L_ ( _X | ϕ_ ) = [ _T − ϕ_ ( _w_ )]<sup>2</sup> _θ_ ( _k_ ) = _EFX L_ ( _X | ϕ_ ) _Bn ∈{_ 0 _,_ 1 _}_<sup>_n_</sup> random vector _i_ : _Bn_ ( _i_ ) = 1 validation sample _i_ : _Bn_ ( _i_ ) = 0 training sample

_Pn,B_<sup>0</sup> _n_<sup>_, p_1</sup> _n,Bn_

25

The estimators would be of the form


This does not work for censoring data because the equation needs all _Ti_ , which we don’t observe. The problems arrise within the Loss function.

Consider the following set up _X_ 1 _, . . . , Xn i.i.d. X ∼ Fx_ Then _µ ≡ µ_ ( _Fx_ ) and _η ≡ η_ ( _Fx_ )

Definition: _D_ ( _X | µη_ ) _EFxD_ ( _X | µ_ ( _Fx_ ) _, η_ ( _Fx_ )) = 0

Then the estimating equation looks like: _n_ <u>1</u> � _ni_ =1<sup>_D_(</sup><sup>_Xi| µη_�) = 0</sup> _⇒ µ_ �

**example 1** : _T_ 1 _, . . . , Tn T ∼ FX i.i.d. µ_ = _S_ ( _t_ ) = _P_ ( _T > t_ ) _D_ ( _X | µ_ ) = _I_ ( _T > t_ ) _− µ_

this is the estimating function we are claiming and it clearly depends on the observed values and the parameter of interest. Now we need to prove that its expected value equals zero


**example 2** : _µ_ = _E_ [ _T_ ] _D_ ( _X | µ_ ) = _T − µ_


26

_D_ ( _X | µ_ ) is known as the full data estimating function.

Now let us move to right censored data Observed data : _O_ 1 _, . . . , On i.i.d Oi ≡ T_<sup>�</sup> _i_ = min( _Ti, Ci_ ) ∆1 _, . . . ,_ ∆ _n_ ∆ _i_ = _I_ ( _Ti ≤ Ci_ ) _T ∼ FX C ∼ G O ∼ PFX ,G_ _<u>µ</u>_ = _I_ ( _T > t_ ) _G_ ( _· | X_ ) = _P_ ( _C > · | X_ ) _D_ ( _X | µ_ ) = _I_ ( _T > t_ ) _− µ_

**Inverse probability of censoring weighted mapping (IPCW mapping)** _D_ ( _X | µ_ ) = _I_ ( _T t_ ) _−_

_µ IC_ ( _O | D, µ, G_ ) =<sup>_D_</sup><sup><u>(</u></sup><sup>_X|µ_</sup><sup><u>)</u></sup><sup>_·_∆</sup> which is the observed data estimating function _G_ ( _T |X_ ) This estimating function equals zero if censoring occured, and, it equals _D_ ( _X | µ_ ) _/G_<sup>¯</sup> ( _T | X_ ) if censoring did not occur.

Now we have to see if this estimating function has _E_ [ _IC_ ] = 0 under the true distribution of the data


Notice _E_ (∆ _| X_ <u>) = 0</u> _· P_ (∆= 0 _| X_ ) + 1 _· P_ (∆= 1 _| X_ ) = _P_ ( _C ≥ T | X_ ) = _G_ ( _T | X_ )

Thus the last term of the previous expectation reduces to _EFX_ [ _D_ ( _X | µ_ )] = 0. One regularity condition we need for all the previous work is


Now, obtaining an estimator for _G_ ( _T | X_ ) we get the following


we will get a consistent estimator as long as we get a consistent estimator _Gn_ .

The new histogram regression estimator for censored data looks like


27

_ϕ_ 0 = _E_ [ _T | wϵ_ [ _wi, wi_ +1]] _D_ ( _X_ ) = _I_ ( _wϵ_ [ _wi, wi_ +1]) _T − ϕ_ 0


The questions that arrieses naturally is if we can get a cross-valitadion risk estimator with censored data. In order to do so, we need to find a new Loss function. Remember that _L_ ( _X, ϕ_ ) = [ _T − ϕ_ ( _w_ )]<sup>2</sup> is the full data Loss function. Now we need the corresponding to the observed data


Then


notice that this new cross-validation risk depends again on _G_ .


Let _X_ 1 _, X_ 2 _, ..., Xn_ be i.i.d. observations having distribution _fθ_ where _θ ∈_ Θ _⊂ R_<sup>_K_</sup>

_H_ 0 : _θ_ = _θ_ 0

I. Likelihood Ratio Test:


Let _θn_ be the maximum likelihood estimator for this parametric model. Then the test statistic is given by


Under regularity conditions,


Proof:

Second order Taylor series expansion is given by


28

where _f_ : _R_<sup>_K_</sup> _→R_

We apply this to _f_ ( _θ_ ) = _log Ln_ ( _θ_ ) with _x ⇔ θ_ 0, _x_ 0 _⇔ θn_ . Thus,


II. Score Test:


so that


III. Chi Square Test:


as<sup>_√_</sup> _<u>n</u>_ <u>(</u> _θ_ 0 _− θn_ ) _H∼_ 0 _N_ (0 _, I_<sup>_−_1</sup> ( _θ_ 0)) We could use _I_ ( _θn_ ) or another estimate of _I_ ( _θ_ ) (the true information matrix).

E.g.: _H_ 0 : _P_ = _P_ 0 Test Statistic usually used


estimates standard error incorrectly. Test Statistic


estimates standard error correctly.

29

Which has more power ?

#### **Right Censored Data**

Let _T_ 1 _, T_ 2 _, ..., Tn_ be i.i.d. observations of _T ∼ F_ 0 ( _cdf_ ) and censoring times _C_ 1 _, C_ 2 _, ..., Cn_ be i.i.d. observations of _C ∼ G_ 0


Only assumption: C and T are independent. We are interested in estimating _S_ 0. We observe that


That is, distribution of ( _T,_<sup>�</sup> ∆) is indexed by _F_ 0 _, G_ 0

This is a semi-parametric model as there are some assumptions like C and T are independent but _F_ 0 and _G_ 0 can be any cdfs.


Likelihood:


This is the factorization of likelihood into relevant F-part and irrelevant G-part.


Maximization of F does not depend on G-part. Relevant log likelihood is given by the function


30

Let the non-parametric maximum likelihood estimate,


F is any cdf. Can we calculate this in closed form ?

Step 1: Show that _F → ln_ ( _F_ ) is maximized at a discrete F with support _t_ 1 _< t_ 2 _< ... < tm_ , _m≤n_ , where the _tj_<sup>_′_</sup> _s_ are the distinct observed failure times.

Step 2:


Re-parameterize _ln_ ( _F_ ) in terms of hazard function: The number of failures at _tj_ is given by


So,


Let _⃗λn_ = ( _λ_ 1 _n, λ_ 2 _n, ..., λmn_ ) be the set of _λ_ ’s that gives the maximum of _ln_ ( _λ_ 1 _, λ_ 2 _, ..., λm_ ).


31


This is the MLE of _ln_ ( _λ_ 1 _, λ_ 2 _, ..., λm_ ).

**Class Notes: February 25, 2004**

( _T_<sup>˜</sup> _i_ = _min_ ( _Ti, Ci_ ) _, △i_ = _I_ ( _Ti ≤ Ci_ )) i=1 _. . . n T ∼ Fo So_ ( _t_ ) = 1 _− Fo_ ( _t_ ) = _P_ ( _T > t_ )

Log likelihood:


F is discrete on _ti < . . . < tn_ , these represent failure times _dF_ ( _T_<sup>˜</sup> _i_ ) = _S_ ( _T_<sup>˜</sup> _i_<sup>_−_)</sup><sup>_λ_( ˜</sup><sup>_Ti_),*everyFhasacorrespondinghazard*</sup>

Note:


_dF_ ( _T_<sup>˜</sup> _i_ ) = _S_ ( _T_<sup>˜</sup> _i_<sup>_−_)</sup><sup>_λ_( ˜</sup><sup>_Ti_) = Π(1</sup><sup>_−λj_)</sup> _S_ ( _t_ ) = Π(1 _− d_ Λ( _s_ )), from before

Thus, we have _ln_ ( _F_ ) =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_log_(</sup><sup>_λ_( ˜</sup><sup>_Ti_))</sup><sup>_△i_+</sup><sup>_log_[Π(1</sup><sup>_−λi_)</sup> _{j_ : _tj <T_<sup>˜</sup> _j }_ =<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_log_(</sup><sup>_λj_)</sup><sup>_dj_+ �</sup> _i_<sup>_n_</sup> =1 � _j_ : _tj <T_<sup>˜</sup> _j_<sup>_log_(1</sup><sup>_−λj_)</sup> = _ln_ ( _λ_ 1 _. . . λm_ )

We can find the maximum likelihood estimator by maximizing: ( _λ_ 1 _. . . λm_ ) _→ ln_ ( _λ_ 1 _. . . λm_ )

Setting _dλd j_<sup>_ln_(</sup><sup>_λ_1</sup><sup>_. . . λm_) = 0j=1tom</sup>

32

give us the closed form solutions (score equations)

_λjn_ = _dj_ +<sup><u>�</u></sup><sup>_<u>m</u>_</sup> _i_ =1 _dj_<sup>_I_( ˜</sup> _Ti>tj_ )<sup>=</sup> _n_<sup>_dj_</sup> _j_ represents number of people at risk at time _tj_ The corresponding MLE of _So_ ( _t_ ): _Sn_ ( _t_ ) = Π _j_ : _tj ≤t_ (1 _− λjn_ ) = Π _j_ : _tj ≤t_ (1 _− n_<sup>_dj_</sup> _j_<sup>)</sup> - the Kaplan-Meier estimate

Use Greenwoods Formula to find estimate of variance - Derivation uses the delta-method:

Working model: F is discrete on fixed points _t_ 1 _< . . . < tm λn_ = ( _λ_ 1 _n . . . λmn_ ) is the MLE of _λ_ in this parametric model _Sn_ ( _t_ ) = Π _j_ : _tj <t_ (1 _− λjn_ ) = _g_ ( _λn_ ) _Sn_ ( _t_ ) = Π _j_ : _tj <t_ (1 _− λjo_ ) = _g_ ( _λo_ ) Delta-method - use Taylor expansion: _Sn_ ( _t_ ) _− So_ ( _t_ ) = _g_ ( _λn_ ) _− g_ ( _λo_ ) = _a_ ( _λo_ )<sup>_T_</sup> ( _λn − λo_ ) _m×_ 1 _a_ ( _λo_ ) = gradient of g at _λo a_ ( _λo_ )<sup>_T_</sup> = _dλd_ 1<sup>_g_(</sup><sup>_λ_)</sup><sup>_, . . . ,_</sup> _dλdm_<sup>_g_(</sup><sup>_λ_)</sup><sup>_|λ_=</sup><sup>_λo_</sup> In this working model:<sup>_√_</sup> _<u>n</u>_ <u>(</u> _λn − λo_ ) _→ N_ (0 _, I_ ( _λo_ )<sup>_−_1</sup> ) Now use: var _a_ ( _λo_ )<sup>_T_</sup> (<sup>_√_</sup> _<u>n</u>_ <u>(</u> _λn − λo_ )) = _a_ ( _λo_ )<sup>_T_</sup> _I_ ( _λo_ )<sup>_−_1</sup> _a_ ( _λo_ ) So, var<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Sn_ ( _t_ ) _− So_ ( _t_ )) _≈ a_ ( _λo_ )<sup>_T_</sup> _I_ ( _λo_ )<sup>_−_1</sup> _a_ ( _λo_ ) –Greenwood’s Formula–

Note: We needed the gradient and the information matrix. Step 1: Find _a_ ( _λo_ )<sup>_T_</sup> Step 2: Find _I_ ( _λo_ ) log _P_ ( _T_<sup>˜</sup> = _t, △_ = _δ_ ) = log ( _d_ Λ( _t_ )) _δ_ + log _S_ ( _t_<sup>_−_</sup> ) =<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_I_(</sup><sup>_t_=</sup><sup>_tj_)log(</sup><sup>_λj_)</sup><sup>_δ_+ �</sup> _j_ : _tj <t_<sup>log(1</sup><sup>_−λj_)</sup> Another derivative or cov of scores gives the information matrix. Note: the information matrix is diagonal, all cross derivatives are 0. i.e. _dλd_ 1 _λd_ 2<sup>= 0</sup> _Uj_ ( _λ_ ) = _dλd j_<sup>log</sup><sup>_Pλ_( ˜</sup><sup>_T, △_)=</sup><sup>_I_</sup><sup><u>( ˜</u></sup><sup>_T_=</sup> _λj_<sup>_tj_</sup><sup><u>)</u></sup><sup>_△_</sup> +<sup>_I_</sup><sup><u>(</u></sup> 1<sup>˜</sup><sup>_T >t_</sup> _−λj_<sup>_<u>j</u>_</sup><sup><u>)</u>.Additionally,forj=k</sup><sup>_̸_</sup> _dλjddλ_<sup>2</sup> _k_<sup>log</sup><sup>_Pλ_( ˜</sup><sup>_T, △_)=0.</sup> _Ijj_ ( _λ_ ) = _−E_ ( _dλ_<sup>_<u>d</u>_</sup> _j_<sup>_Uj_(</sup><sup>_λ_)( ˜</sup><sup>_T, △_))=</sup><sup>_E_(</sup><sup>_I_</sup><sup><u>( ˜</u></sup><sup>_T_=</sup> _λ_<sup>2</sup> _j_<sup>_tj_</sup><sup><u>)</u></sup><sup>_△_</sup> +<sup>_I_</sup> (1<sup><u>( ˜</u></sup><sup>_T >t_</sup> _−λj_ )<sup>_<u>j</u>_2))</sup> Thus, _I_ ( _λ_ ) = diag ( _I_ 11( _λ_ ) _. . . Imm_ ( _λ_ )) or _I_<sup>_−_1</sup> = _diags_ <u>1</u><sup>,i.e.inverseofeachdiagonalelement</sup>

33

_dλdgj_<sup>=</sup><sup>_−I_(</sup><sup>_tj≤t_)</sup> 1<sup>_S_</sup> _−_<sup><u>(</u></sup> _λ_<sup>_t_</sup><sup><u>)</u></sup> _j_ Gradient, _a_ ( _λo_ )<sup>_T_</sup> = _−_ ( _I_ ( _t_ 1 _≤ t_ ) 1<sup>_S_</sup> _−_<sup><u>(</u></sup> _λ_<sup>_t_</sup><sup><u>)</u></sup> 1<sup>_, . . . , I_(</sup><sup>_tm≤t_)</sup> 1<sup>_S_</sup> _−_<sup><u>(</u></sup> _λ_<sup>_t_</sup><sup><u>)</u></sup> _m_<sup>)</sup> Some algebra gives, _σ_<sup>2</sup> = _S_<sup>2</sup> ( _t_ )<sup>�</sup> _tj ≤t_<sup>_I_</sup> _jj_<sup>_−_1(</sup><sup>_λo_)</sup> (1 _−λ_ <u>1</u> _oj_ )<sup>2</sup> To estimate _σ_<sup>2</sup> use Kaplan-Meier, _σ_ ˆ2 = _n_ 2( _Sn_ ( _t_ )2)<sup>�</sup> _tj ≤t nj_ ( _ndjj−dj_ ) var _Sn_ ( _t_ ) _≈ nSn_ ( _t_ )<sup>�</sup> _tj ≤t nj_ ( _ndjj−dj_ )

This suggests that C.I.’s will be ’wider at the tails’.

C.I. = _Sn_ ( _t_ ) _±_ 1 _._ 96 _~~√~~_<sup>_<u>σ</u>_ˆ</sup> _n_<sup>isaymptotic0.95C.I.for</sup><sup>_So_(</sup><sup>_t_)</sup>

Need Influence Curve to get simultaneous C.I.’s - more about this next time!

---

[← Right Censored Data: Kaplan-Meier as a substitute estimator](17-right-censored-data-kaplan-meier-as-a-substitute-estimator.md) · [Up: contents](index.md) · [Locally efficient estimation when death is reported with delay, Alan Hubbard →](19-locally-efficient-estimation-when-death-is-reported-with-del.md)
