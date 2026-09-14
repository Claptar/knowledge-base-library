---
title: 13 Lecture 13
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 13 Lecture 13

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **13.1 Rigorous Derivation of Rates of Convergence of** _M_ **-estimators**

Let us recall the setup. Θ is an abstract parameter space. We have two processes (one stochastic and one deterministic) that are indexed by _θ ∈_ Θ. The stochastic process will usually depend on a “sample” size _n_ and will be denoted by _Mn_ ( _θ_ ) _, θ ∈_ Θ. The deterministic process will usually not depend on _n_ and will simply be denoted by _M_ ( _θ_ ) _, θ ∈_ Θ. We expect _Mn_ to be close to _M_ for large _n_ .

Let _θ_<sup>ˆ</sup> _n_ denote a maximizer of _Mn_ ( _θ_ ) over _θ ∈_ Θ and let _θ_ 0 denote a maximizer of _M_ ( _θ_ ) over _θ ∈_ Θ. Let _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) be a nonnegative discrepancy measure gauging the gap between _θ_<sup>ˆ</sup> _n_ and _θ_ 0. We shall assume that


for every _θ ∈_ Θ. Here the notation _a_ ≳ _b_ means that _a ≥ Cb_ for a universal positive constant _C_ (the notation _a_ ≲ _b_ is defined analogously). In light of (105), the canonical choice for _d_ will be


When _d_ is not the canonical choice above, it usually happens that (105) holds only in a neighbourhood of _θ_ 0. We shall come back to this situation later.

We shall now rigorously find upper bounds for the rate of convergence of _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0). Formally, we say that _δn_ is a rate of convergence of _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) to zero if for every _ϵ >_ 0, there exists a constant _Cϵ_ such that


Note that this is equivalent to


It should be noted that (107) and (108) are nonasymptotic statements (they hold for each finite _n_ ). They imply, in particular, the asymptotic rate statement: _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) = _OP_ ( _δn_ ) which means the following: For every _ϵ >_ 0, there exists _Cϵ_ and an integer _Nϵ_ such that


66

The difference between the (109) and (107) is that (109) holds for all _n ≥ Nϵ_ while (107) holds for all _n_ . Let us now study the probability


for fixed _δn_ and large _M_ . We need to understand for which _δn_ does this probability become small as _M →∞_ .

Write


We shall now use the basic inequality (together with the condition (105)):


This clearly gives


Suppose that the function _φn_ ( _·_ ) is such that


We thus get


for every _j_ . As a consequence,


The following assumption on _φn_ ( _·_ ) is usually made to simplify the expression above: There exists _α <_ 2 such that


Under this assumption, we get


The quantity<sup>�</sup> _j>M_<sup>2</sup><sup>_j_(</sup><sup>_α−_2)convergestozeroas</sup><sup>_M→∞_.Thereforeif</sup><sup>_δn_issuchthat</sup>


then


where _uM →_ 0 as _M →∞_ .

This gives us the following nonasymptotic rate of convergence theorem:

**Theorem 13.1.** _Assume the condition_ (105) _and that the function φn_ ( _·_ ) _satisfies_ (110) _and_ (111) _. Then for every M >_ 0 _, we get d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) _≤_ 2<sup>_M_</sup> _δn with probability at least_ 1 _− uM provided φn_ ( _δn_ ) ≲ _δn_<sup>2</sup><sup>_.Here_</sup> _uM_ =<sup>�</sup> _j>M_<sup>2</sup><sup>_j_(</sup><sup>_α−_2)</sup><sup>_→_0</sup><sup>_asM→∞._</sup>

67

## **13.2 Application to Bounded Lipschitz Regression**

Suppose _f_ 0 is an unknown function on [0 _,_ 1]. We observe data _Y_ 1 _, . . . , Yn_ on _f_ 0 that are generated according to the model:


where _ϵ_ 1 _, . . . , ϵn_ are i.i.d _N_ (0 _,_ 1) random variables.

Suppose that we assume that _f_ 0 is 1-Lipschitz on and that it is bounded by 1 on [0 _,_ 1]. In other words we assume that _f_ 0 _∈F_ where _F_ is the collection of all functions on [0 _,_ 1] that are bounded in absolute value by 1 and that are 1-Lipschitz. Under this assumption, it is reasonable to estimate _f_ 0 by


_f_ ˆ _n_ is clearly an _M_ -estimator and we can use Theorem 13.1 to study some aspects of its behavior. For this, we first write (using _Yi_ = _f_ 0( _i/n_ ) + _ϵi_ ):


As a result


In order to use Theorem 13.1, we can thus take


It is then natural to take


For the discrepancy _d_ , we can use the canonical choice (106):


To find the rate, we need to control


For this, we can use Dudley’s entropy bound. Let


68

and note that


This implies that


Dudley’s entropy bound then immediately gives


We have previously noted that


This gives


We can thus take _φn_ ( _δ_ ) := � _δ/n_ in Theorem 13.1. Note that this clearly satisfies the condition _φn_ ( _cx_ ) _≤ c_<sup>_α_</sup> _φn_ ( _x_ ) with _α_ = 1 _/_ 2 _<_ 2. The critical rate determining equation then becomes:


which gives _δn_ ≳ _n_<sup>_−_1</sup><sup>_/_3</sup> . Thus Theorem 13.1 is valid here with _δn_ = _n_<sup>_−_1</sup><sup>_/_3</sup> which allows us to deduce the following:

or, more specifically,


We have therefore proved that the rate of convergence in Lipschitz regression is _n_<sup>_−_2</sup><sup>_/_3</sup> . We shall prove later that, in a minimax or worst case sense (worst case over all functions _f_ 0 _∈F_ ), this _n_<sup>_−_2</sup><sup>_/_3</sup> rate cannot be improved by any other estimator. In other words, _n_<sup>_−_2</sup><sup>_/_3</sup> is the minimax optimal rate of convergence for Lipschitz functions on [0 _,_ 1].

More generally, suppose we now assume that _f_ 0 is in the smoothness class _Sα_ that we previously defined. In that case, the same argument as above leads to the inequality:


69

Suppose now that _α >_ 1 _/_ 2. In that case the integral above is finite and we get


We can thus take


so that the critical inequality for determining the rate becomes


which gives


leading us to the conclusion


It turns out that _n_<sup>_−_2</sup><sup>_α/_(2</sup><sup>_α_+1)</sup> is indeed the minimax optimal rate of estimation of functions in _Sα_ .

Suppose now that _α ≤_ 1 _/_ 2. In this case, the integral in (112) is infinite so Dudley’s bound in the form that we used does not give us anything useful. In this case, one can use a modification of Dudley’s bound where the lower limit in the integral is not _zero_ but strictly positive (this is Problem 6 Homework 3). However the resulting rate for _d_<sup>2</sup> ( _f_<sup>ˆ</sup> _n, f_ 0) will be slower than _n_<sup>_−_2</sup><sup>_α/_(2</sup><sup>_α_+1)</sup> . It is not known if the least squares estimator over _Sα_ is minimax optimal for _α ≤_ 1 _/_ 2.

## **13.3 Back to the rate theorem**

Now let us get back to Theorem 13.1. For proving the theorem, we assumed that


for all _θ ∈_ Θ. We also assumed that


for all _u >_ 0. Here _φn_ ( _u_ ) is some function on (0 _, ∞_ ) which satisfies _φn_ ( _cx_ ) _≤ c_<sup>_α_</sup> _φn_ ( _x_ ) for some _α <_ 2.

Under these two assumptions, Theorem 13.1 asserted that _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) = _OP_ ( _δn_ ) for every _δn_ that satisfies _φn_ ( _δn_ ) ≲ _δn_<sup>2.</sup>

In some situations, it is not possible to ensure that (113) holds for all _θ ∈_ Θ. It is also not possible to ensure that (114) holds for all _u >_ 0. On the contrary, it is usually possible to ensure the existence of a positive real number _u_<sup>_∗_</sup> (not depending on _n_ ) such that (113) holds for all _θ ∈_ Θ with _d_ ( _θ, θ_ 0) _≤ u_<sup>_∗_</sup> and such that (114) holds for all _u ≤ u_<sup>_∗_</sup> . In that case, it is still possible to assert that _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) = _OP_ ( _δn_ ) under the additional assumption that _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) converges in probability to 0. This is the content of the following theorem (which is Theorem 3.2.5 in Van der Vaart and Wellner [25]).

**Theorem 13.2.** _Let u_<sup>_∗_</sup> _be a strictly positive real number (not depending on n) such that_ (113) _holds for all θ ∈_ Θ _with d_ ( _θ, θ_<sup>_∗_</sup> ) _≤ u_<sup>_∗_</sup> _. Let φn be a function on_ (0 _, ∞_ ) _which satisfies the condition for some α <_ 2 _: φn_ ( _cx_ ) _≤ c_<sup>_α_</sup> _φn_ ( _x_ ) _for all c >_ 1 _and x >_ 0 _. Suppose that_ (114) _holds for all_ 0 _< u ≤ u_<sup>_∗_</sup> _. Assume that d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) = _OP_ (1) _. Then d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) = _OP_ ( _δn_ ) _for every δn satisfying φn_ ( _δn_ ) ≲ _δn_<sup>2</sup><sup>_._</sup>

70

_Proof._ Write


The first term can be bounded in exactly the same way as in the proof of Theorem 13.1. This gives


If _δn_ is chosen such that _φn_ ( _δn_ ) ≲ _δn_<sup>2, the first term above converges to zero as</sup><sup>_M→∞_.The second term, on</sup> the other hand, converges to 0 as _n →∞_ by the assumption that _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) converges to zero in probability. This concludes the proof of Theorem 13.2.

---

[← 12 Lecture 12](13-12-lecture-12.md) · [Up: contents](index.md) · [14 Lecture 14 →](15-14-lecture-14.md)
