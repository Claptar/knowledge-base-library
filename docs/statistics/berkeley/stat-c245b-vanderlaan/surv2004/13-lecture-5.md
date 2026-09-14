---
title: Lecture 5
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 5

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### February 2, 2004 Jessica G. Young

#### **ASYMPTOTICALLY LINEAR ESTIMATORS (CONT’D)**

Suppose we have _X_ 1 _, ..., Xn_ i.i.d observations of X _∼ fθ_ : _θ ∈_ **Θ** _⊂_ **R**<sup>_k_</sup> _θn_ is an asymptotically linear estimator of _θ_ with influence curve


if


We estimate the _k × k_ -covariance matrix Σ by


where **ICˆ** ( _Xi_ ) is the estimated influence curve. A typical estimate is the substitution estimate obtained by replacing _θ_ by _θn_ : **IC**<sup>**ˆ**</sup> ( _X_ ) = **IC** ( _X|θn_ ).

8

Alternatively,


_<u>√</u>_ Σ _n_ <u>(</u> _j,j_ <u>)</u> The asymptotic 0.95 confidence interval for _θj_ is given by: _θjn ±_ 1 _._ 96 _~~√~~ n_ . That is, the _<u>√</u>_ Σ _n_ <u>(</u> _j,j_ <u>)</u> _<u>√</u>_ Σ _n_ <u>(</u> _j,j_ <u>)</u> probability that _θj ∈_ [ _θjn −_ 1 _._ 96 _~~√~~ n , θjn_ + 1 _._ 96 _~~√~~ n_ ] _n−→→∞_<sup>0</sup><sup>_._95,whichisequivalentwith</sup>


As an aside, we can use the complete estimated multivariate limit distribution _N_ (0 _,_ Σ _n_ ) to _<u>√</u>_ Σ _n_ <u>(</u> _j,j_ <u>)</u> construct a simultaneous confidence interval of the type _θjn ± δ_ _~~√~~ n_ , wherer _δ_ is chosen so that _<u>√</u>_ Σ _n_ <u>(</u> _j,j_ <u>)</u> the simultaneous probability that _θj ∈ θjn ± δ_ _~~√~~ n_ converges to 0.95 for _n →∞_ . Hypothesis testing = _⇒ H_ 0 : _θj_ = _θj_ 0


#### **Relative Efficiency**

Suppose we have _θn_ 1 _, θn_ 2, which are two asymptotically linear estimators of _µ ∈_ **R** with influence curves _IC_ 1( _X_ ) _, IC_ 2( _X_ ). Let _σj_<sup>2= VAR</sup><sup>_ICj_(</sup><sup>_X_),</sup><sup>_j_= 1</sup><sup>_,_2.</sup>

Then the asymptotic relative efficiency _R_ of the two estimators is defined as


To interpret this relative efficiency, we consider its relation to the width of the confidence intervals for _θ_ based on these two estimators respectively. The half-width of a 0.95-confidence interval _θnj ±_ 1 _._ 96 _∗_ _~~√~~_<sup>_σj_</sup> _n_<sup>basedon</sup><sup>_ICj_isgivenby1</sup><sup>_._96</sup> _~~√~~_<sup>_σj_</sup> _n_<sup>,</sup><sup>_j_=1</sup><sup>_,_2.Thus,ifonewishesthiswidthtobeequalto</sup> _ε_ , then one obtains the following corresponding required sample size:


So the sample size needed to get precision _ε_ will depend on _σ_ 1 and _σ_ 2. Specifically,


For example, if _R_ = 3, you would need 3 times the sample size to get the same precision using the ’bad’ versus ’good’ estimator.

**Examples of influence curves using standard** _δ_ **-method:**

#### **_Example_**

9

_x_ ¯ = _n_<sup><u>1</u></sup> � _ni_ =1<sup>_xi_isanasymptoticallylinearestimatorof</sup><sup>_µ_=</sup><sup>_EX_with</sup><sup>_IC_(</sup><sup>_X_) = (</sup><sup>_x −µ_).</sup> Why is this the influence curve for _x_ ¯? Because if we take the average of this function over all values of X, we get<sup>_√_</sup> _<u>n</u>_ <u>(</u> _x_ ¯ _− µ_ ); that is we get _x_ ¯ minus the parameter it is estimating. Specifically,


#### **_Example_**

_X_ 1 _, . . . , Xn ∼ fλ_ ( _x_ ) = _λe_<sup>_−λx_</sup> <u>¯</u> _λn_ = _X_<sup><u>1</u>and</sup><sup>_λ_=</sup> _µ_<sup><u>1</u>,where</sup><sup>_µ_=</sup><sup>_EX_.</sup>

First, we can write _λn − λ_ = _f_ (¯ _x_ ) _− f_ ( _µ_ )<sup>_∼_</sup> = _f ′_ ( _µ_ ) _×_ (¯ _x − µ_ ) (Delta method)

The Delta method states that for a given real-valued function _f_ : IR _→_ IR _f_ ( _x_ + _h_ ) _−f_ ( _x_ )<sup>_∼_</sup> = _f ′_ ( _x_ ) _h_ if h is small.

This allows us to write _f_ ( _xn_ ) _− f_ ( _x_ )<sup>_∼_</sup> = _f ′_ ( _x_ )( _xn − x_ ) if _xn_ is close to _x_ . In words, if we have a function of an estimator minus a function of the parameter it’s estimating, we can always approximate this difference as the derivative of the function of the parameter (at the true parameter value) multiplied by the difference between the estimator and the truth. In our example, _λn_ = _f_ (¯ _x_ ), _λ_ = _f_ ( _µ_ ), where _f_ ( _y_ ) = _y_<sup><u>1</u>.So,</sup>


We have now shown that _λn − λ_ is an empirical mean of i.i.d. random variables 1 _/µ_<sup>2</sup> ( _X − µ_ ) in the first order.

Thus, the influence curve of _λn_ is given by


so,


The asymptotic variance of _λn_ can be obtained by:


So _λn ±_ 1 _._ 96 _~~√~~_<sup>_<u>σn</u>_</sup> _n_<sup>isanasymptotic0.95confidenceintervalfor</sup><sup>_λ_.</sup>

_λn_ is a maximum likelihood estimator and should be efficient so _var_ ( _λn_ ) should be equal to _I_ ( _λ_ )<sup>_−_1</sup> .

What if we want to estimate _µ_ = _E_ ( _X_<sup>_k_</sup> )?

10

_µn_ = _n_<sup><u>1</u></sup> � _ni_ =1<sup>_x_</sup> _i_<sup>_k_so</sup><sup>_IC_(</sup><sup>_X|µ_) =</sup><sup>_xk_</sup> _i_<sup>_−µ_</sup> (this is because, as in the first example, we can write:<sup>_√_</sup> _<u>n</u>_ <u>(</u> _µn − µ_ ) = _~~√~~_ <u>1</u> _n_ � _ni_ =1<sup>(</sup><sup>_x_</sup> _i_<sup>_k−µ_)).</sup> So, in general, if _µ_ = _E_ [ _h_ ( _X_ )], for some h, then _µn_ = _n_<sup><u>1</u></sup> � _ni_ =1<sup>_h_(</sup><sup>_xi_)isasymptoticallylinearand</sup> _IC_ ( _X|µ_ ) = _h_ ( _x_ ) _− µ_ .

#### **_Example_**

_X_ 1 _, . . . .Xn_ i.i.d X, _σ_<sup>2</sup> = _var_ ( _X_ ) = _EX_<sup>2</sup> _−_ ( _EX_ )<sup>2</sup> = _µ_ 2 _−_ ( _µ_ 1)<sup>2</sup> where _µj_ = _EX_<sup>_j_</sup> _, j_ = 1 _,_ 2


where


Again by the Delta method,


For this example it follows,


We can further write,


Thus,


By the above, _σn_<sup>2is an asymptotically linear estimator of</sup><sup>_σ_2with influence curve</sup><sup>_IC_(</sup><sup>_X|µ_1</sup><sup>_, µ_2) =</sup> _−_ 2 _µ_ 1( _x − µ_ 1) + _x_<sup>2</sup> _− µ_<sup>2</sup> .

We can then get the variance of _σ_<sup>2</sup> using the techniques illustrated above.


11

---

[← Lecture 4, January 28, 2004](12-lecture-4-january-28-2004.md) · [Up: contents](index.md) · [1 Censored Data and Model Selection →](14-1-censored-data-and-model-selection.md)
