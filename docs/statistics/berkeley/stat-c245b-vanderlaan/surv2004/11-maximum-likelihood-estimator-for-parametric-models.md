---
title: Maximum Likelihood Estimator for Parametric Models
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Maximum Likelihood Estimator for Parametric Models

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let _x_ 1, _· · ·_ , _xn_ be i.i.d. observations of _X ∼ fθ ∈{fθ_ : _θ ∈_ Θ _⊂ R_<sup>_K_</sup> _}_ . _{fθ_ : _θ ∈_ Θ _⊂ R_<sup>_K_</sup> _}_ is the parametric model, _θ_ = ( _θ_ 1 _, · · · θK_ ) is a finite ( _K_ ) dimensional parameter, and Θ is the parameter space.

The maximum likelihood estimator is defined as follows:


If the log-likeihood is a differentiable function of _θ_ at the MLE _θn_ , then _θn_ solves the so called _K_ score equations:


is called the score function. Newton-Raphson Algorithm Define _H_ ( _θ_ ) = ( _H_ 1( _θ_ ) _, · · · , HK_ ( _θ_ )), and _θ_ = ( _θ_ 1 _, · · · , θK_ ).

5

The Newton-Raphson algorithm is an iterative algorithm which aims to solve the _K_ -dimensional equation _H_ ( _θ_ ) = 0. For example, in order to solve the score equations 1 _/n_<sup>�</sup> _i_<sup>_U_(</sup><sup>_θ_)(</sup><sup>_Xi_)=0,one</sup> sets _H_ ( _θ_ ) = 1 _/n_<sup>�</sup> _i_<sup>_U_(</sup><sup>_θ_)(</sup><sup>_Xi_).The</sup><sup>_k_-thNewton-Raphsonstepisdefinedby:</sup>


One starts this algorithm with a choice _θ_<sup>0</sup> , and iterates the above equation till convergence.

For example, in the special case that _H_ ( _θ_ ) = 1 _/n_<sup>�</sup> _i_<sup>_U_(</sup><sup>_θ_)(</sup><sup>_Xi_),wehave</sup>


It is general practice, to modify the NR algorithm for solving equations _H_ ( _θ_ ) = 0 with the so called line-search ingredient w.r.t. to a criteria (in the case of score equations, this would be the log-likelihood) one aims to maximize. Namely, one does not necessarily accept the update _θ_<sup>_k_+1</sup> , but first verifies if the update increases the wished criteria. For example, in the case of solving the score equations, we do the following: If _loglik_ ( _θ_<sup>_k_+1</sup> ) _̸ ≤ loglik_ ( _θ_<sup>_k_</sup> ), then take _αθ_<sup>_k_</sup> + (1 _− α_ ) _θ_<sup>_k_+1</sup> for an _α_ so that _loglik_ ( _αθ_<sup>_k_</sup> + (1 _− α_ ) _θ_<sup>_k_+1</sup> ) _> loglik_ ( _θ_<sup>_k_</sup> ).

---

[← Some Parametric Models for f 0](10-some-parametric-models-for-f-0.md) · [Up: contents](index.md) · [Lecture 4, January 28, 2004 →](12-lecture-4-january-28-2004.md)
