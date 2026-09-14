---
title: 12 Lecture 12
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 12 Lecture 12

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **12.1 Bracketing Control**

Our main empirical process bound so far is the following. Under the usual notation:


where


Bracketing methods provide another upper bound for E sup _f ∈F |Pnf − Pf |_ which we shall describe next. This bound will be very similar to (95) except that sup _Q M_ ( _ϵ ∥F ∥L_ 2( _Q_ ) _, F, L_<sup>2</sup> ( _Q_ )) will be replaced by the _ϵ_ - **bracketing** number of _F_ in _L_<sup>2</sup> ( _P_ ). Before we state this result, let us first define the notion of bracketing numbers:

1. Given two real-valued functions _ℓ_ and _u_ on _X_ , the bracket [ _ℓ, u_ ] is defined as the collection of all functions _f_ : _X →_ R for which _ℓ_ ( _x_ ) _≤ f_ ( _x_ ) _≤ u_ ( _x_ ) for all _x ∈X_ .

2. Given a probability measure _P_ on _X_ , the _L_<sup>2</sup> ( _P_ )-size of a bracket [ _ℓ, u_ ] is defined as _∥u − ℓ∥L_ 2( _P_ ).

3. Let _F_ be a class of real-valued functions on _X_ . For _ϵ >_ 0, the bracketing number _N_ $$\]( _ϵ, F, L_<sup>2</sup> ( _P_ )) is defined as the smallest number of brackets each having _L_<sup>2</sup> ( _P_ )-size at most _ϵ_ such that every _f ∈F_ belongs to one of the brackets.

It is important to notice that the bracketing numbers are larger than covering numbers as shown below.

**Lemma 12.1.** _For every ϵ >_ 0 _,_


_Here Fall denotes the class of all real-valued functions on X ._

_Proof._ The first inequality is something we have already seen when discussing covering numbers. The second inequality is proved as follows. First get brackets [ _ℓi, ui_ ] _, i_ = 1 _, . . . , N_ each of _L_<sup>2</sup> ( _P_ )-size _ϵ_ which cover _F_ . Then it is obvious to see that the mid-point functions ( _ℓi_ + _ui_ ) _/_ 2 _, i_ = 1 _, . . . , N_ form an _ϵ/_ 2-net for _F_ in the _L_<sup>2</sup> ( _P_ ) metric.

61

Next, we provide an example where the bracketing numbers can be explicitly computed.

**Example 12.2.** _Let F_ := _{I_ ( _∞,t_ ] : _t ∈_ R _} and let P be a fixed probability measure on_ R _. Then we shall argue that_


_Here is an argument for_ (96) _. Let t_ 0 := _−∞ and recursively define_


_Then, for every δ >_ 0 _sufficiently small, it is clear that P_ ( _ti−_ 1 _, ti − δ_ ] _≤ ϵ (because otherwise ti − ϵ would be the supremum) and hence (by letting δ →_ 0 _), we deduce that P_ ( _ti−_ 1 _, ti_ ) _≤ ϵ. Also if ti < ∞, then for every δ >_ 0 _, we have P_ ( _ti−_ 1 _, ti_ + _δ_ ] _> ϵ so that (by letting δ ↓_ 0 _), P_ ( _ti−_ 1 _, ti_ ] _≥ ϵ._

_Let k ≥_ 1 _be the smallest integer for which tk_ = _∞. Then, by the above, we have P_ ( _ti−_ 1 _, ti_ ] _≥ ϵ for i_ = 1 _, . . . , k −_ 1 _so that_


_which gives k ≤_ 1 + _ϵ_<sup>_−_1</sup> _. Now consider the brackets_ [ _I_ ( _−∞,ti−_ 1] _, I_ ( _−∞,ti_ )] _for i_ = 1 _, . . . , k. These obviously cover F (i.e., each function in F belongs to one of these brackets) and their L_<sup>2</sup> ( _P_ ) _-size is_


_We have thus proved that_


_This, being true for all ϵ >_ 0 _, is the same as_ (96) _._

Before stating the analogue of (95) involving bracketing numbers, let us first state and prove a simple classical asymptotic result which shows that bracketing number bounds can be used to control E sup _f ∈F |Pnf − Pf |_ .

**Proposition 12.3.** _Suppose F is a function class such that N_ \[$$( _ϵ, F, L_<sup>2</sup> ( _P_ )) _< ∞ for every ϵ >_ 0 _. Then_


_Proof._ Fix _ϵ >_ 0. Let [ _ℓi, ui_ ] _, i_ = 1 _, . . . , N_ denote brackets of _L_<sup>2</sup> ( _P_ )-size _≤ ϵ_ which cover _F_ . We shall first argue that


Let us first complete the proof of (97) assuming that (98) is true. To see this, note that the right hand side above converges to 0 almost surely as _n →∞_ . This is because, by the strong law of large numbers, _|Pnui − Pui|_ and _|Pnℓi − Pℓi|_ converge to zero almost surely as _n →∞_ for each _i_ (note that the functions _ui_ and _ℓi_ do not change with _n_ ) and hence the finite maximum of these over _i_ = 1 _, . . . , N_ also converges to zero. Thus, from (98), we deduce that


Applying this for each _ϵ_ = 1 _/m_ and letting _m →∞_ , it is possible to deduce (97).

It remains therefore to prove (98). Fix _f ∈F_ and get a bracket [ _ℓi, ui_ ] which contains _f_ . This means that _ℓi_ ( _x_ ) _≤ f_ ( _x_ ) _≤ ui_ ( _x_ ) for every _x ∈X_ . Write


62

It can similarly be proved that _Pnf − Pf ≥ Pnℓi − Pℓi − ϵ_ . Both these inequalities together imply (98) which completes the proof of Proposition 12.3.

We shall now state the analogue of (95) involving bracketing numbers. This will be our second main result for bounding the expected suprema of empirical processes (the first main result being (95)).

**Theorem 12.4.** _Let F be an envelope for the class F such that PF_<sup>2</sup> _< ∞. Then_


_where_


The bound (99) is very similar to (95) the only difference being that the “uniform” covering numbers sup _Q M_ ( _ϵ ∥F ∥L_ 2( _Q_ ) _, F, L_<sup>2</sup> ( _Q_ )) are replaced by the bracketing numbers _N_ $$\]( _ϵ ∥F ∥L_ 2( _P_ ) _, F, L_<sup>2</sup> ( _P_ )) with respect to _L_<sup>2</sup> ( _P_ ). Importantly, note that there is supremum over _Q_ in (99) and the bracketing numbers involving only the measure _P_ . In contrast, the bound (95) would be false if sup _Q M_ ( _ϵ ∥F ∥L_ 2( _Q_ ) _, F, L_<sup>2</sup> ( _Q_ )) is replaced by _M_ ( _ϵ ∥F ∥L_ 2( _P_ ) _, F, L_<sup>2</sup> ( _P_ )).

**Example 12.5.** _Suppose X_ 1 _, . . . , Xn are i.i.d observations having cdf F and let Fn be the empirical cdf. We have seen previously that_


_for every n ≥_ 1 _. This was deduce as a consequence of_ (95) _. We shall show here that this can also be deduced via_ (99) _. Indeed for F_ := _{I_ ( _−∞,t_ ] : _t ∈_ R _}, we have obtained bounds for N_ \[$$( _ϵ, F, L_<sup>2</sup> ( _P_ )) _in_ (96) _. We deduce from these and_ (99) _that_


The following presents a situation where bounding the bracketing numbers is much more tractable compared to bounding the uniform covering numbers.

**Proposition 12.6.** _Let_ Θ _⊆_ R<sup>_d_</sup> _be contained in a ball of radius R. Let F_ := _{mθ_ : _θ ∈_ Θ _} be a function class indexed by_ Θ _. Suppose there exists a function M with ∥M ∥L_ 2( _P_ ) _< ∞ such that_


_for all x ∈X and θ_ 1 _, θ_ 2 _∈_ Θ _(here ∥·∥ denotes the usual Euclidean norm). Then for every ϵ >_ 0 _,_


_Proof._ Let _θ_ 1 _, . . . , θN_ be a maximal _ϵ/_ 2-packing subset of Θ in the Euclidean metric. Consider the brackets [ _mθi − ϵM/_ 2 _, mθi_ + _ϵM/_ 2] for _i_ = 1 _, . . . , N_ . Note that

1. These brackets cover _F_ . Indeed, for every _θ ∈_ Θ, there exists 1 _≤ i ≤ N_ with _∥θ − θi∥≤ ϵ/_ 2. Then by the condition (100),


which implies that _mθ_ lies in the bracket [ _mθi − ϵM/_ 2 _, mθi_ + _ϵM/_ 2].

2. The _L_<sup>2</sup> ( _P_ )-size of these brackets is at most _ϵ_ . This is obvious.

Because of these two observations, _N_ \[\]( _ϵ ∥M ∥L_ 2( _P_ ) _, F, L_<sup>2</sup> ( _P_ )) is bounded from above the Euclidean _ϵ/_ 2- packing number of Θ which we bounded previously. This completes the proof of Proposition 12.6.

63

## **12.2 M-estimation**

We shall now come to the first statistics topic of the course: _M_ -estimation. The basic abstract setting is the following.

Let Θ be an abstract parameter space. Usually, it is a subset of R<sup>_d_</sup> for parametric estimation problems or it is a function class for nonparametric estimation problems. We have two processes (one stochastic and one deterministic) that are indexed by _θ ∈_ Θ. The stochastic process will usually depend on a “sample” size _n_ and will be denoted by _Mn_ ( _θ_ ) _, θ ∈_ Θ. The deterministic process will usually not depend on _n_ and will simply be denoted by _M_ ( _θ_ ) _, θ ∈_ Θ. We expect _Mn_ to be close to _M_ for large _n_ .

Let _θ_<sup>ˆ</sup> _n_ denote a maximizer of _Mn_ ( _θ_ ) over _θ ∈_ Θ and let _θ_ 0 denote a maximizer of _M_ ( _θ_ ) over _θ ∈_ Θ. The goal in _M_ -estimation is to study the behavior of _θ_<sup>ˆ</sup> _n_ in relation to _θ_ 0.

Some concrete _M_ -estimators are described below.

1. **Classical Parametric Estimation** : The most classical _M_ -estimator is the Maximum Likelihood Estimator (MLE). Here one typically has data _X_ 1 _, . . . , Xn_ in _X_ that are i.i.d having distribution _P_ . One also has a class _{pθ, θ ∈_ Θ _}_ of densities over the space. The MLE maximizes _Mn_ ( _θ_ ) := _Pn_ log _pθ_ over _θ ∈_ Θ. The process _M_ ( _θ_ ) here is _M_ ( _θ_ ) := _P_ log _pθ_ and _θ_ 0 can then be taken to the parameter value in Θ for which _pθ_ is closest to _P_ in terms of the Kullback-Leibler divergence.

More generally, one can take _Mn_ ( _θ_ ) = _Pnmθ_ and _M_ ( _θ_ ) = _Pmθ_ for other functions _mθ_ . For example, _mθ_ ( _x_ ) := _|x−θ|_ corresponds to median estimation (here _θ_<sup>ˆ</sup> _n_ is the sample median and _θ_ 0 is the population median) and _mθ_ ( _x_ ) := _I{|x − θ| ≤_ 1 _}_ can be taken to correspond to mode estimation.

2. **Least Squares Estimators in Regression** : In regression problems, one observes data ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) with _Xi ∈X_ and _Yi ∈_ R which can be modeled as i.i.d observations having some distribution _P_ . Let Θ be a class of functions from _X_ to R. The least squares estimator over the class Θ corresponds to the maximizer of


over _θ ∈_ Θ. It is natural to compare this _θ_<sup>ˆ</sup> _n_ to _θ_ 0 which is the maximizer of


3. **Empirical Risk Minimization Procedures in Classification** : Here one observes data ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) where _Xi ∈X_ and _Yi ∈{−_ 1 _,_ +1 _}_ . We model the data as i.i.d having a distribution _P_ . Let Θ denote a class of functions from _X_ to R; we are thinking of the sign of _θ_ ( _x_ ) as the output of the classifier. It is natural to consider


In this case, _θ_<sup>ˆ</sup> _n_ will be the empirical minimizer of the misclassification rate and _θ_ 0 will be the minimizer of the test error, both in the class Θ. It is therefore natural to compare the performance of _θ_<sup>ˆ</sup> _n_ to that of _θ_ 0.

Note that it is difficult to compute _θ_<sup>ˆ</sup> _n_ as the minimization of _Mn_ ( _θ_ ) is a combinatorial problem. For this, one also studies other choices of _Mn_ ( _θ_ ) in classification. To motivate these other choices, let us first rewrite the above _Mn_ ( _θ_ ) as


For computational considerations, one often replaces _φ_ 0 by another loss function _φ_ that is _convex_ and _similar_ to _φ_ 0. Common choices of _φ_ include (a) Hinge loss: _φ_ ( _t_ ) := (1 + _t_ )+, (b) Exponential loss: _φ_ ( _t_ ) := exp( _t_ ), and (c) Logistic loss: _φ_ ( _t_ ) := log(1 + _e_<sup>_t_</sup> ). Note that these three functions are convex

64

on R and they are similar to _φ_ 0 (note that they also satisfy _φ_ ( _t_ ) _≥ φ_ 0( _t_ ) for al _t_ ). We shall study procedures _θ_<sup>ˆ</sup> _n_ which minimize


and compare their performance to _θ_ 0.

The theory of _M_ -estimation concerns itself usually with three questions: (a) Consistency, (b) Rate of Convergence, and (c) Limiting Behavior. Consistency asserts that the discrepancy between _θ_<sup>ˆ</sup> _n_ and _θ_ 0 converges to zero as _n →∞_ . Rate of convergence aims to characterize the precise rate of this convergence. The goal of the third question will be to give a precise characterization of the limiting distribution of the discrepancy in the asymptotic setting where _n →∞_ .

Consistency usually always holds and we have already seen a theorem last week on consistency. We shall mainly concentrate on the problem of rates of convergence. In many cases, a rate of convergence result automatically implies consistency. In other cases, one needs a preliminary consistency result so that attention can be focused in a local neighbourhood of _θ_ 0 in order to determine the rate of convergence. In cases where preliminary consistency is required and our consistency theorem last week is not sufficient, we shall provide a different argument for consistency. Let us ignore consistency for the time being and proceed directly to the rates. For studying limiting behavior, we need theory on uniform central limit theorems which we are yet to cover; we shall come back to these in a few weeks.

## **12.3 Rates of Convergence of** _M_ **-estimators**

It is cleanest to work in the abstract setting where _θ_<sup>ˆ</sup> _n_ maximizes a stochastic process _Mn_ ( _θ_ ) over _θ ∈_ Θ and _θ_ 0 maximizes a deterministic process _M_ ( _θ_ ) over _θ ∈_ Θ. The argument for deriving rates starts from the following basic inequaility:


We have already seen this inequality multiple times and it is a consequence of the simple inequality _Mn_ ( _θ_<sup>ˆ</sup> _n_ ) _≥ Mn_ ( _θ_ 0). For convenience, we shall denote the right hand side above by ( _Mn − M_ )( _θ_<sup>ˆ</sup> _n − θ_ 0) so that


We shall use this inequality to study rates of convergence of _θ_<sup>ˆ</sup> _n_ to _θ_ 0. We need to first fix a measure of discrepancy between _θ_<sup>ˆ</sup> _n_ and _θ_ 0. Let this be given by _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0). In cases where Θ is a subset of R<sup>_d_</sup> , it is natural to take _d_ ( _·, ·_ ) as the usual Euclidean metric. In general, we shall not require that _d_ ( _·, ·_ ) is a metric; at this stage, we only require it to be nonnegative.

Note that the discrepancy measure _d_ ( _·, ·_ ) is somewhat external to the problem and, therefore, to understand the behavior of _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0), we need to connect it to _M_ ( _θ_ ) or _Mn_ ( _θ_ ). The usual assumption for this is to assume that:


Here the notation _a_ ≳ _b_ means that _a ≥ Cb_ for a universal constant _C_ (the notation _a_ ≲ _b_ is defined analogously).

Let us assume that (103) is true for all _θ ∈_ Θ. In some situations, it is only true in a neighborhood of _θ_ 0 (we can come back to this later). Note that (103) is automatically true if we define _d_ as


This is the most natural choice for studying rates of _M_ -estimators. In parametric estimation problems, this usually does not correspond to the Euclidean metric so this choice is not usually used. However in function estimation problems, this is a very common choice.

65

Combining (102) and (103), we obtain


Let _δ_<sup>ˆ</sup> _n_ := _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0). Then the above inequality clearly implies


This suggests that _δ_<sup>ˆ</sup> _n_ ≲ _δn_ for any rate _δn_ that satisfies


We shall rigorize this intuition in the next class. The critical inequality (104) gives a nice way to determine the rate of convergence of _M_ -estimators in a variety of problems. The expectation on the right hand side can be controlled via the empirical process methods that we have studied in the past many weeks.

---

[← 11 Lecture 11](12-11-lecture-11.md) · [Up: contents](index.md) · [13 Lecture 13 →](14-13-lecture-13.md)
