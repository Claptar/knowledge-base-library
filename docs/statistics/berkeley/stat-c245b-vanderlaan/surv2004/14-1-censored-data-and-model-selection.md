---
title: 1 Censored Data and Model Selection
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Censored Data and Model Selection

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **1.1 Background**

**Survival data** Survival analysis is the collection of statistical procedures for data analysis for which the outcome variable of interest is _time until an event occurs_ . We have see the following type of survival data. _T_ 1 _, T_ 2 _, ...., Tn_ are i.i.d. observatios of _T_ . _T_ is typically time to occurrence of some event. Events include death, disease, relapse, recovery. Time _≡_ Survival time. Event _≡_ failure In practice, we may not observe each of the _Ti_ ’s. For example, at the end of the study we might only know that a subject is still alive. That is, the subject’s survival time is right-censored. In generally, there are three causes for censoring: 1) a person does not experience the event before _the study ends_ ; 2) a person is _lost to follow-up_ during the study period; 3) a person _withdraws from the study_ because of death or some other reason (e.g., adverse drug reaction, car accident). Note that the complete survival time interval has been cut off at the right side, although data can also be left-censored. Most survival data is right-censored. We will consider _right-censored_ data in this class.

**Right censored data structure** Observed Data structure: _O_ = ( _T_<sup>�</sup> = min( _T, C_ ) _,_ ∆) We observe _n_ i.i.d. observations ( _T_<sup>�</sup> 1 _,_ ∆1) _, ....,_ ( _T_<sup>�</sup> _n,_ ∆ _n_ ) of _O_ . We note that the observed data structure is a function of ( _T, C_ ). We will denote the marginal distribution functions of _T_ and _C_ with _F_ and _G_ , respectively.

### **1.2 Model**

Full Data Model: Model for _F_ . is called a _full data model_ . Censoring Mechanism model: Model for conditional distribution _G_ of _C | T_ is called the _censoring mechanism_ or _conditional censoring distribution._

Note: You can imagine that assumptions on full data model and censoring mechanism have a tremendous effect on the inference problems that we face.

**Example 1, Exponential density** Assume that _T_ follows an exponential distribution, and that _C_ is independent of _T_ with unspecified marginal distribution. We will now compute the likelihood for one observation:


where _fλ_ ( _t_ ) = _P_ ( _T_ = _t_ ), and _G_ ( _t_ ) = 1 _− G_ ( _t_ ). Similarly,


Thus the likelihood for _n_ observations is given by:


Thus, the loglikelihood for _n_ observations is given by:


12

The goal is to estimate the exponential parameter _λ_ . We need to solve _dλd_<sup>log</sup><sup>_L_(</sup><sup>_λ, G |_(</sup><sup>_T_�</sup><sup>_i,_∆</sup><sup>_i_)</sup><sup>_, i_=</sup> 1 _, ..., n_ ) = 0 w.r.t. _λ_ . Recall _fλ_ ( _T_<sup>�</sup> _i_ ) = _λ_ exp( _−λT_<sup>�</sup> _i_ ), _Sλ_ ( _T_<sup>�</sup> _i_ ) = exp( _−λT_<sup>�</sup> _i_ ). Thus, the solution of the <u>�</u> _<u>i</u>_<sup>∆</sup><sup>_i_</sup> score equations is given by: _λn_ = <u>�</u> _i T_<sup>�</sup> _i_<sup>.</sup>

_P_ <u>(∆=1)</u> We also note that the information is given by _I_ ( _λ_ ) = _λ_<sup>2</sup> . Thus, the Cramer-Rao lower bound is given by: _I_ ( _λ_ )<sup>_−_1</sup> = _P_ (∆=1) _<u>λ</u>_<sup>2.Asimpleestimateoftheinformationmatrixisgivenby:</sup>


**Example, Histogram regression with uncensored survival data** The full data structure is now _X_ = ( _T, W_ ), where _W_ is a vector of baseline covariates. The parameter of interest is the conditional expectation:


Suppose that we observe _n_ i.i.d. observations of _X_ .

Construction of histogram regression estimators of Ψ0: Let _K_ be the number of bins. For each bin, the estimator of the mean survival time is the empirical mean of the survival times with covariates _W_ in that bin. Give the number of bins _k_ , we have now a defined a histogram regression estimator of _ψ_ 0 which we will denote with Ψ _k_ ( _Pn_ ), _k_ = 1 _, ...., K_ .

How do we choose the number of bins? Choose among estimators Ψ1( _Pn_ ) _, .....,_ Ψ _k_ ( _Pn_ ) ?

**Cross-validation.** Let _L_ ( _X,_ Ψ) = [ _T −_ Ψ( _w_ ]<sup>2</sup> . Define _Bn ∈_ (0 _,_ 1 _}_<sup>_n_</sup> as an _n_ dimensional random vector. Let _{i_ : _Bn_ ( _i_ ) = 1 _}_ be the validation sample, and let _{i_ : _Bn_ ( _i_ ) = 0 _}_ be the training sample. Let _Pn,B_<sup>0</sup> _n_<sup>,</sup><sup>_P_</sup> _n,B_<sup>1</sup> _n_<sup>betheempiricaldistributionsofthetrainingsampleandvalidationsample,</sup> respectively.

If one would observe _X_ 1 _, . . . , Xn_ , then a cross-validated conditional risk estimate of the estimator _Pn →_ Ψ _k_ ( _Pn_ ) is defined as:


PH 240B Notes For Feb 9th 2004, Srikesh G. Arunajadai

**Theorem: Asymptotic Linearity of Maximum Likelihood Estimate (MLE)**

Let _X_ 1 _, . . . , Xn_ be i.i.d sample from the distribution _X ∼ fθ_ 0, _θ ∈_ Θ _⊂ R_<sup>_k_</sup> where Θ is the parameter space and _θ_ 0 denotes the true parameter value. Let _θn_ be the MLE:


The influence curve of _θn_ is given by


where


is the information matrix of dimension _k × k_ and


Under regularity conditions


Hence


for _n →∞_ : that is, the<sup>_√_</sup> _<u>n</u>_ <u>-standardized difference</u> _θn−θ_ 0 converges in distribution to the normal distribution with mean zero and variance equal to the variance of the influence curve _I_ ( _θ_ 0)<sup>_−_1</sup> _U_ ( _θ_ 0)( _X_ ) of _θn_ .

#### **Note**


#### **Proof**

Consistency of _θn_


where _Pθ_ denotes the probability distribution corresponding with the density _fθ_ so that _dPθ_ ( _x_ ) = _fθ_ ( _x_ ) _dλ_ ( _x_ ) in the case that _fθ_ denotes a density of _Pθ_ w.r.t. a measure _λ_ .

The function log is not a fixed function of _X_ but a random function of _X_ . Hence we � _ffθnθ_ <u>0((</u> _Xx_ <u>))</u> � cannot use the law of large numbers to prove that the first term converges to zero in probability. However, we can bound the first term by the supremum over the collection of functions _{X →_ log � _<u>ffθθ</u>_ <u>0((</u> _XX_ )) � : _θ}_ , and then employ a uniform law of large numbers, as established in empirical process theory (e.g., van der Vaart, Wellner, 1996). Also the second term is less then or equal to zero as it can be written as follows.


as the second integral uses the maximum likelihood estimate. Hence, we have


14

The latter term can be handled by empirical process theory.

**Definition** : A class _F_ = _{f_ : _x →_ R _}_ of real valued functions of X is called a uniform GlivencoCatelli (GC) class if


converges in probability to 0 when _n →∞_

Empirical process theory provides many examples of such classes. Thus if


is a GC class then we have shown that


when


**Example** Given a function _f_ : R<sup>2</sup> _→_ R we define the uniform sectional variation norm as follows


If there exists a _M_ such that


then _G_ is a GC class.

Thus, for example, if each of the functions in _F_ has uniform sectional variation norm bounded by a universal constant _M < ∞_ , then we have proved _dKL_ ( _fθn, fθ_ 0) _→_ 0 in probability for _n →∞_ . Since the _L_ 1( _Pθ_ 0)-norm _∥fθn − fθ_ 0 _∥θ_ 0 _,_ 1 _≡_ � _| fθn − fθ_ 0 _|_ ( _x_ ) _dPθ_ 0( _x_ ), and _L_ 2( _Pθ_ 0)-norm _∥fθn − fθ_ 0 _∥θ_ 0 _,_ 2 _≡_ �� ( _fθn − fθ_ 0)<sup>2</sup> _dPθ_ 0 can be bounded by the Kullback-Leibler divergence _dKL_ ( _fθn, fθ_ 0), under the condition that _fθ_ 0 is uniformly bounded away from zero, the converges in Kullback-Leibler divergence implies the convergence _L_ 1 and _L_ 2 norm of _fθn_ to _fθ_ 0. This proves consistency of _fθn_ to _fθ_ 0. In order to prove consistency of _θn_ to _θ_ 0 one needs to be able to write _θ_ as a continuous function of _fθ_ . **Lecture of February 11, 2004, Oliver Bembom**

Asymptotic Linearity of the MLE _θn_

Let _X_ 1 _, ..., Xn_ be i.i.d. with _X ∼ Pθ_ 0. Let _H_ ( _θ, P_ ) _≡ Ep_ [ _U_ ( _θ_ )( _X_ )] _∈_ IR<sup>_k_</sup> , with _U_ ( _θ_ )( _X_ ) = _dθd_<sup>log</sup><sup>_fθ_(</sup><sup>_X_)</sup><sup>_∈_IR</sup><sup>_k_.Thenweknow:</sup>


15


where (2) follows since _θn_ is defined as that _θ ∈_ Θ that maximizes<sup>�</sup><sup>_n_</sup> _i_ =1<sup>log</sup><sup>_fθ_(</sup><sup>_Xi_).An estimator</sup> that is defined as the solution under the empirical distribution of an equation that holds for the true _θ_ 0 under _fθ_ 0 is called an M-estimator. MLE are thus part of this class of M-estimators. The proof of asymptotic linearity given here applies in fact to any M-estimator.Using (1) and (2), we get


We will use a first-order Taylor series expansion for the term on the left, and results from empirical process theory for the term on the right. Since _H_ : IR<sup>_k_</sup> _→_ IR<sup>_k_</sup> , we review the definition of the derivative in this setting: We say that _g_ : IR<sup>_k_</sup> _→_ IR<sup>_k_</sup> is differentiable at _a ∈_ IR<sup>_k_</sup> if there exists a linear transformation _g_ ˙ : IR<sup>_k_</sup> _→_ IR<sup>_k_</sup> such that


where _∥x∥_ = �� _in_ =1<sup>_x_</sup> _i_<sup>2</sup> �1 _/_ 2 is the Euclidean norm. Note that _g_ ˙ can represented as a _k × k_ matrix. Note also that this definition implies that


i.e. _g_ ( _x_ ) _− g_ ( _a_ ) can be written as a linear approximation plus a remainder term which tends to 0 even when divided by _∥x − a∥_ .In our case, we have _H_ : IR<sup>_k_</sup> _→_ IR<sup>_k_</sup> with


Using that _θ → H_ ( _θ, Pθ_ 0) is thus differentiable at _θ_ 0 we can write

16


Substituting this into the left-hand side of (3) and writing out the right-hand side, we get


Assuming that _I_<sup>_−_1</sup> ( _θ_ 0) exists, we have that


For the term inside the outer square brackets, we use the following result from empirical process theory:

If _F_ = _{X → U_ ( _θ_ )( _X_ ) : _θ ∈_ **Θ** _}_ is a so-called Donsker class (this is for example true if _∃ M < ∞_ such that _∀ θ ∈_ **Θ** : _∥U_ ( _θ_ ) _∥v ≤ M_ ) and


then


Note that the proof of consistency of the MLE from last lecture implies the second assumption of this result. Hence under the assumption that _F_ is a Donsker class, we have


17


In order to prove asymptotic linearity of the MLE, we need to show that the last term _o_ ( _∥θn −θ_ 0 _∥_ ) is also _op_ � _~~√~~_ <u>1</u> _n_ �. Note that the above implies that


since the asymptotic normal distribution of


is bounded in probability. This implies that


and hence that


Thus we have proved that


Hence the MLE is asymptotically linear with influence curve given by

18

_IC_ ( _X_ ) = _I_<sup>_−_1</sup> ( _θ_ 0) _U_ ( _θ_ 0)( _X_ )

Explanation of _op_ and _Op_ notation

1. We say that a sequence of real numbers _f_ ( _n_ ) is _o_ (1) if _limn→∞f_ ( _n_ ) = 0, i.e. if


We say that a sequence of real numbers _f_ ( _n_ ) is _o_ ( _g_ ( _n_ )) if the sequence<sup>_<u>f</u>_</sup> _g_ (<sup><u>(</u></sup> _n_<sup>_n_</sup> )<sup><u>)</u>is</sup><sup>_o_(1).</sup>

2. We say that a sequence of real numbers _f_ ( _n_ ) is _O_ (1) if _f_ ( _n_ ) is bounded, i.e. if


We say that a sequence of real numbers _f_ ( _n_ ) is _O_ ( _g_ ( _n_ )) if the sequence<sup>_<u>f</u>_</sup> _g_ (<sup><u>(</u></sup> _n_<sup>_n_</sup> )<sup><u>)</u>is</sup><sup>_O_(1).</sup>

3. We say that a sequence of random variables _R_ ( _n_ ) is _op_ (1) if _R_ ( _n_ ) tends to 0 in probability as _n →∞_ , i.e. if


A sequence of random variables _R_ ( _n_ ) is _op_ ( _h_ ( _n_ )) if the sequence<sup>_R_</sup> _h_ (<sup><u>(</u></sup> _n_<sup>_n_</sup> )<sup><u>)</u>is</sup><sup>_op_(1).</sup>

4. We say that a sequence of random variables _R_ ( _n_ ) is _Op_ (1) if it is bounded in probability, i.e. if


We say that a sequence of random variables _R_ ( _n_ ) is _Op_ ( _h_ ( _n_ )) if the sequence<sup>_R_</sup> _h_ (<sup><u>(</u></sup> _n_<sup>_n_</sup> )<sup><u>)</u>is</sup><sup>_Op_(1).</sup>

19

Simultaneous confidence regions for _θ_ <u>0</u>

Definition: Let _A_ = _Q_ Λ _Q_<sup>_T_</sup> be the spectral decomposition of an n _×_ n matrix _A_ ( _Q_ is orthonormal and Λ diagonal). Then define the square-root of A as


Note:


Suppose<sup>_√_</sup> _<u>n</u>_ <u>(</u> _θn − θ_ 0) = _⇒ N_ ( **0** _,_ **Σ** ) in distribution. This implies that


where _σn_ is an estimate of ~~�~~ Σ( _j, j_ ) for _j_ = 1 _, ..., n_ , and _ρ_ is the correlation matrix corresponding to **Σ** . Let _ρ_<sup>_−_</sup><sup><u>1</u></sup> 2 be the square-root of _ρ_<sup>_−_1</sup> . Then


Proof: Let **Z** be a random _n_ -vector with covariance matrix **Σ** and **A** be an _n × n_ matrix of real numbers. Then


In particular, if **Z** _∼ N_ ( **0** _, ρ_ ) then **AZ** _∼ N_ ( **0** _,_ **A** _ρ_ **A**<sup>_T_</sup> ). For **A** = _ρ_<sup>_−_</sup><sup><u>1</u></sup> 2 we get


Thus _ρ_<sup>_−_</sup> 2<sup><u>1</u></sup> **Z** _∼ N_ ( **0** _,_ **I** ).

**Class Notes: February 18, 2004, Merrill Birkner**

20

_X_ 1 _, . . . , Xn_ i.i.d. _X ∼ fθ_ 0 _θ_ 0 _∈ θ ⊂ R_<sup>_k_</sup> _<u>√n</u>_ <u>(</u> _θn − θ_ 0) = _~~√~~_ <u>1</u> _n_ � _ni_ =1<sup>_IC_(</sup><sup>_Xi|θ_0) +</sup><sup>_op_(1)</sup> _⇒D N_ (0 _,_ Σ0 = _E_ [ _IC_ ( _X|θ_ 0) _IC_ ( _X|θ_ 0)<sup>_T_</sup> ]) _<u>√n</u>_ <u>(</u> _θσnn−θ_ <u>0)</u> _⇒D N_ (0 _, ρ_ 0 = _correlation_ (Σ)) where _σn_ = _var_ ˆ ( _IC_ ( _X|θ_ 0))

The above is a standardization, by dividing by the standard error.

#### **Elliptical Confidence Region**

Let _ρ_<sup>_−_</sup> 0<sup>1</sup> be the inverse of _ρ_ 0 Let _ρ_<sup>_−_</sup> 0<sup>1</sup> = _TDT_<sup>_T_</sup> be the eigenvalue decomposition: where T is a matrix of eigenvectors and D is a diagonal matrix. Define _ρ_<sup>_−_</sup> 0<sup>1</sup><sup>_/_2</sup> = _T √DT_ ** It is the square root of _ρ_<sup>_−_</sup> 0<sup>1.Then,</sup><sup>_ρ−_</sup> 0<sup>1</sup><sup>_/_2</sup> ( _<u>√n</u>_ <u>(</u> _θσnn−θ_ <u>0)</u> ) _⇒D N_ (0 _, I_ ). This implies that: Pr( _||ρ_<sup>_−_</sup> 0<sup>1</sup><sup>_/_2</sup> (<sup>_sqrtn_</sup> _σ_<sup><u>(</u></sup><sup>_θ_</sup> _n_<sup>_n−θ_</sup><sup><u>0)</u></sup> ) _||_<sup>2</sup> _≤Xk,_<sup>2</sup> 0 _._ 95<sup>)</sup><sup>_→_0</sup><sup>_._95,</sup> where _Xk,_<sup>2</sup> 0 _._ 95<sup>isthe0.95quantileofa</sup><sup>_X_2</sup> _k_<sup>.</sup> **and the Euclidian norm is defined as follows: _||x||_ = �� _kj_ =1<sup>_x_</sup> _j_<sup>2</sup> **Rectangular 0.95 Confidence Region** After standardization, we are looking for a constant **a** such that: _<u>√n</u>_ <u>(</u> _θn−θ_ <u>0)</u> _n→∞→ Pr_ ( _Maxj| σn | < a_ ) 0 _._ 95. Then, _Pr_ ( _θ_ 0 _j ∈_ ( _θnj ±_<sup>_aσ_</sup> _~~√~~_<sup>_n_</sup> _n_<sup>_<u>j</u>_)</sup><sup>_∀j_= 1</sup><sup>_...k_)</sup><sup>_→_0</sup><sup>_._95.</sup> Therefore, components with large standard errors will have wider confidence intervals. Thus, _θ_ : _θj ∈_ ( _θnj ±_<sup>_aσ_</sup> _~~√~~_<sup>_n_</sup> _n_<sup>_<u>j</u>_)</sup><sup>_, j_= 1</sup><sup>_...k→_0</sup><sup>_._95.</sup> This is a 0.95 Confidence Region for _θ_ 0

**How can we get this?** We can simulate from _N_ (0 _, ρ_ 0) distribution: By Simulation:

Choose **a** equal to the 0.95 quantile ( _q_ 0 _._ 95) of the _E ≡ Maxj_ =1 _..k|Wj|_ , where _W ∼ N_ (0 _, ρ_ 0) Simulate 20,000 vectors (size k) from _N_ (0 _, ρ_ 0)

Take the maximum value of each vector; therefore you end up with 20,000 maximum values. Now you want to take the 0.95 quantile of this vector, length 20,000, of maximums. We can do this by:

1. Simulate N=20,000 _⃗W_ 1 _,⃗W_ 2 _, ...,⃗WN ∼ N_ (0 _, ρ_ 0)

2. Create N: _E_ 1 = _Maxj|W_ 1 _j|, E_ 2 = _Maxj|W_ 2 _j|, ...EN_ = _Maxj|WNj|_

3. Compute 0.95 quantile of _E_ 1 _....EN_ . This is _q_ 0 _._ 95

How to Simulate from a MVN distribution.

Simulating from _N_ (0 _, ρ_ 0). Let _U_ be such that _U_<sup>_T_</sup> _U_ = _ρ_ 0. _U_ can be chosen to be equal to the Choleski decomposition.

- **Note: In R (chol( _ρ_ 0))

Then _UZ ∼ N_ (0 _, UU_<sup>_T_</sup> = _ρ_ 0) where _Z ∼ N_ (0 _, I_ )

#### **An Application:**

Suppose you want to find the confidence region of a survival function with probability 0.95. You want a simultaneous confidence region. With probability 0.95 you want the entire survival curve in that ’envelope’

Example: _T_ 1 _, ....., Tn_ i.i.d. _T ∼ f_ 0 _S_ 0( _t_ ) = _P_ ( _T > t_ ) Let _θ_ 0 = ( _S_ 0( _t_ 1) _....S_ 0( _tk_ )) be the parameter vector of interest.

21

#### **How to estimate this?**

_θn_ = ( _S_ 0( _t_ 1) _....S_ 0( _tk_ )) where _Sn_ ( _t_ ) = _n_<sup><u>1</u></sup> � _ni_ =1<sup>_I_(</sup><sup>_Ti> t_)</sup> _θn − θ_ 0 = _n_<sup><u>1</u></sup> � _ni_ =1<sup>_IC_(</sup><sup>_Ti|θ_0)</sup> where _IC_ ( _T |θ_ 0) = [ _I_ ( _T > t_ 1) _− S_ 0( _t_ 1) _, .....I_ ( _T > tk_ ) _− S_ 0( _tk_ )]<sup>_T_</sup> note: the vector IC has no remainder. Thus: **How to**<sup>_√_</sup> _<u>n</u>_ **estimate** <u>(</u> _θn − θ_ 0) _⇒_ **the** _D N_ **influence** (0 _,_ Σ0 = _E_ [ **curve?** _IC_ ( _T |θ_ 0First,) _IC_ ( _T_ estimate _|θ_ 0)<sup>_T_</sup> ]) the influence curve: _IC_ ˆ ( _T_ ) = _IC_ ( _T |θn_ ). Σ _n_ = _n_<sup><u>1</u></sup> � _ni_ =1 _IC_<sup>ˆ</sup> ( _Ti_ ) _IC_<sup>ˆ</sup> ( _Ti_ )<sup>_T_</sup> . Remember that: _IC_ ( _T |θn_ ) = [ _I_ ( _T > t_ 1) _− S_ 0( _t_ 1) _, .....I_ ( _T > tk_ ) _− S_ 0( _tk_ )]<sup>_T_</sup> For every person you are going to create an IC vector and take a sample standard covariance (Σ _n_ ) Then you will plot _θn_ : the survival curve. To find the cut-off **a** we need to standardize (and therefore work with a common cut-off) _ρ_ 0 _n_ = correlation matrix corresponding to Σ _n_ _<u>√n</u>_ <u>(</u> _θn−θ_ <u>0)</u> thus, _σn ∼ N_ (0 _, ρ_ 0 _n_ ) where _σn_<sup>2=</sup><sup>_var_(</sup> _IC_<sup>ˆ</sup> ( _T_ )) or the diagonal of Σ _n_ In order to find the constant, we need the 0.95 quantile (ˆ _q_ 0 _._ 95) of: _Maxj|Wj|_ where _W ∼ N_ (0 _, ρ_ 0 _n_ )

We then want to use the Cholesky decomposition of _ρ_ 0 _n_ (described earlier in notes) _UZ ∼ N_ (0 _, ρ_ 0 _n_ ): we want to find U

You will come up with a number for **a** . For example _q_ ˆ0 _._ 95 = 3 In a point wise calculation, this value would be equal to 1.96 (since that is the 0.95 quantile of a N(0,I).

Thus, _θnj ±_ ˆ _q_ 0 _._ 95 _σ_ _~~√~~ nnj_<sup>isasimultaneousconfidenceregion.(j=1...k)</sup>

One can plot the survival function (Survival versus Time) and then plot the simultaneous confidence ’envelope’ around the estimated survival function ( _θn_ or _Sn_ ). The confidence region should be closer to _θn_ on the two extremes of the plot and further away in the middle of the survival function. Since it is Bernoulli, it will not be equally placed and therefore thinner on the ends. The survival curve will lay in the envelope with probability 0.95.

Lecture 14, Kathryn Steiger, February 27, 2004.

---

[← Lecture 5](13-lecture-5.md) · [Up: contents](index.md) · [General Approach for Construction of an Estimator →](15-general-approach-for-construction-of-an-estimator.md)
