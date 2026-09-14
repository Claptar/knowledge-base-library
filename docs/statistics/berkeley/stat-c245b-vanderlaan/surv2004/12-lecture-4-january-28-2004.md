---
title: Lecture 4, January 28, 2004
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 4, January 28, 2004

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### **Properties of ML estimators**

#### Nisha Mulakken

_X ∼ fθ_ , _θ ⊂_ Θ _⊂ R_<sup>_K_</sup> where _θ_ is ( _θ_ 1 _, θ_ 2 _, ..., θk_ )

**Score function** :


**Property of Score function** :

_Efθ_ ( _θ_ )( _X_ ) = 0

proof:

Let _k_ = 1 � _U_ ( _θ_ )( _X_ ) _fθ_ ( _X_ ) _dx_ = <u>�</u> _dθd_<sup>_fθ_(</sup><sup>_X_)</sup><sup>_dx_</sup> _fθ_ ( _X_ ) _fθ_ ( _X_ ) _dx_ = _<u>d</u>_ <u>�</u> _dθ_<sup>_fθ_(</sup><sup>_X_)</sup><sup>_dx_</sup> = _<u>d</u> dθ_ � _fθ_ ( _X_ ) _dx_ = _dθd_<sup>1 = 0</sup>

**Information Matrix** :

_I_ ( _θ_ ) _kxk_ = _Efθ_ [ _U_ ( _θ_ )( _X_ ) _U_ ( _θ_ )( _X_ )<sup>_t_</sup> ]

Thus, _I_ ( _θ_ )( _j, l_ ) = _E_ [ _Uj_ ( _θ_ )( _X_ ) _Ul_ ( _θ_ )( _X_ )] = COV _fθ_ ( _Uj_ ( _θ_ )( _X_ ) _, Ul_ ( _θ_ )( _X_ )) We also have that _I_ ( _θ_ ) = _−E dθ_<sup>_<u>d</u>U_(</sup><sup>_θ_)(</sup><sup>_X_)</sup>

This follows from the identity:

_Efθ dθdj_<sup>_Ul_(</sup><sup>_θ_)(</sup><sup>_X_) =</sup><sup>_−Efθ_[</sup><sup>_Uj_(</sup><sup>_θ_)(</sup><sup>_X_)</sup><sup>_Ul_(</sup><sup>_θ_)(</sup><sup>_X_)]</sup>

6


**Cramer-Rao Lower Bound for assymptotic variance** :

Let _θjn_ be an uniformly unbiased estimator of _θj Eθθjn_ = _θj_ for all _θ ∈_ Θ

Then _var_ ( _θjn_ ) _≥_ ( _I_ ( _θ_ )<sup>_−_1</sup> ( _j, j_ )) _/n_ for any uniformly unbiased estimator. A generalization of this statement is the following: _var_ ( _a_<sup>_t_</sup> _θn_ ) _≥ a_<sup>_t_</sup> _I_ ( _θ_ )<sup>_−_1</sup> _a_ , where _a_<sup>_⊤_</sup> _θn ≡ a_ 1 _θ_ 1 _n_ + _a_ 2 _θ_ 2 _n_ + _..._ + _atθtn_ denotes a linear combination of the _j_ -specific estimators.

Example estimators: Consider the parametric family _N_ ( _µ, σ_<sup>2</sup> ). A possible estimator of the true _µ_ is given by _µn_ = 2. This is not a uniformly unbiased estimator Another estimator is _µn_ = _X_ = _n_<sup><u>1</u></sup> � _ni_ =1<sup>_xi_,whichisauniformlyunbiasedestimator:</sup> _Eµ,σ_ 2 _X_ = _µ_ under all normal densities _fµ,σ_ 2. Example: Consider the exponential family of densities _f_ ( _x_ ) = _λexp_ ( _−λx_ ) indexed by _λ_ . Given i.i.d. data _x_ 1 _, ..., xn_ , the maximum likelihood estimator of _λ_ is given by _λMLE_ = <u>1 1</u> _n_ <u>�</u> _<u>ni</u>_ =1<sup>_xi_</sup> This is shown as follows: _fλ_ ( _x_ ) = _λexp_ ( _−λx_ ) _logfλ_ ( _x_ ) = _logλ − λx Uλ_ ( _x_ ) = _dλd_<sup>_logfλ_(</sup><sup>_x_) =</sup> _λ_<sup><u>1</u></sup><sup>_−x_</sup> **Score Equation** � _ni_ =1<sup>_Uλ_(</sup><sup>_xi_) = 0issolvedby</sup><sup>_λn_=</sup> _<u>x</u>_<sup><u>1</u>,whichisthustheMLestimator</sup>

Do we have: _Efλ λn_ = _λ_ ? _Efλ_ ( _X_<sup><u>1</u>) =</sup> _λ_<sup><u>1</u>?</sup> Most likely not, since identities such as _E_ 1 _/Y_ = 1 _/EY_ for a given random variable _Y_ are rare.

Most ML estimators (with one well known exception the MLE of _µ_ in the Normal family) are not unbiased. What we want is for the estimator to be close to the truth. To do this, we want to minimize the mean squared error (MSE). This means both bias and variance are important to consider.

_MSE_ ( _θjn_ ) = _Efθ_ ( _θjn − Eθj_ )<sup>2</sup> + _Efθ_ ( _θjn − θj_ )<sup>2</sup> = _var_ ( _θjn_ ) + _bias_<sup>2</sup> ( _θjn_ )

**Asymptotically Linear Estimator**

data: _x_ 1 _, ..., xniid ∼ fθ,n_

7

An estimator _θn_ is an asymptotically linear estimator with influence curve _IC_ ( _X|θ_ ) where _Eθ_ [ _IC_ ( _X|θ_ )] = 0, and _IC_ ( _X|θ_ ) = _IC_ 1( _X|θ_ ) _, ..., ICk_ ( _X|θ_ ) if : _θn − θ_ = _− n_<sup><u>1</u></sup> � _ni_ =1<sup>_IC_[</sup><sup>_xi|θ_] +</sup><sup>_op_(</sup> _~~√~~_<sup><u>1</u></sup> _n_<sup>)</sup>

Definition: _Rn_ = _op_ ( _~~√~~_<sup><u>1</u></sup> _n_<sup>)if</sup><sup>_√_</sup> _<u>nRn</u> →_ 0 in probability for _n_ converging to infinity.

In general:


Note: _IC_ ( _Xi|θ_ ) measures influence of observation _Xi_ on the estimator

Thus,


By the CLT, this converges to the distribution _N_ (0 _,_ Σ = _E_ [ _IC_ ( _X|θ_ ) _IC_ ( _X|θ_ )<sup>_t_</sup> ]) Consequently, the influence curve can be used to estimate Σ and thereby provide confidence intervals and regions for the unknown parameter vector _θ_ .

Influence curves are very convenient for asymptotic inference of estimators. For example, given a _k_ -dimensional vector of influence curves corresponding with a set of _k_ estimators, the influence curve of a (e.g. non-linear) function of this set of estimators is given by the gradient of the function applied to the influence curves. In particular, the difference of two estimators of two parameters has as influence curve the difference of the two estimator-specific influence curves.

Given two asymptotically linear estimators, the relative efficiency of these two estimators is given by the ratio of the variances of their influence curves.

---

[← Maximum Likelihood Estimator for Parametric Models](11-maximum-likelihood-estimator-for-parametric-models.md) · [Up: contents](index.md) · [Lecture 5 →](13-lecture-5.md)
