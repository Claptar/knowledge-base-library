---
title: 8 Lecture 8
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8 Lecture 8

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **8.1 Dudley’s Metric Entropy Bound**

The main goal for today is to state and prove Dudley’s entropy bound for the suprema of subgaussian processes. The proof involves an idea called chaining. Before we start with chaining, let us recall the following basic result from last class.

**Proposition 8.1.** _Let T be a finite set and let {Xt, t ∈ T } be a stochastic process. Suppose that for every t ∈ T and u ≥_ 0 _, the inequality_


_holds. Here_ Σ _is a fixed positive real number. Then, for a universal positive constant C, we have_


As we remarked in the last lecture, the bound (49) can be tight (up to a multiplicative constant) in some situations. For example, this is the case when _Xt, t ∈ T_ are i.i.d _N_ (0 _,_ Σ<sup>2</sup> ). Because of this example, Proposition 8.1 cannot be improved without imposing additional conditions on the process _{Xt, t ∈ T }_ . It is also easy to construct examples where (49) is quite weak. For example, if _Xt_ = _X_ 0 + _ηZt_ for some

39

_X_ 0 _∼ N_ (0 _,_ Σ<sup>2</sup> ) and _Zt, t ∈ T ∼_<sup>_i.i.d_</sup> _N_ (0 _,_ 1) and _η_ is very very small, then it is clear that max _t∈T |Xt| ≈ X_ 0 so that (49) will be loose by a factor of log(2 _|T |_ ). In order to improve on (49), we need to make assumptions on how _close_ to each other the _Xt_<sup>_′s_are.Dudley’sentropyboundmakessuchanassumptionexplicitand</sup> provides improved upper bounds for E max _t∈T |Xt|_ .

We shall first state Dudley’s bound when the index set _T_ is finite and subsequently improve it to the case when _T_ is infinite.

**Theorem 8.2** (Dudley’s Metric Entropy Bound for finite _T_ ) **.** _Suppose_ ( _T, d_ ) _is a finite metric space and {Xt, t ∈ T } is a stochastic process such that for every s, t ∈ T and u ≥_ 0 _,_


_Then, for a universal positive constant C, the following inequality holds for every t_ 0 _∈ T :_


The following remarks mention some alternative forms of writing the inequality (51) and also describe some implications.

1. Let _D_ denote the diameter of the metric space _T_ (i.e., _D_ = max _s,t∈T d_ ( _s, t_ )). Then the packing number _M_ ( _ϵ, T, d_ ) clearly equals 1 for _ϵ ≥ D_ (it is impossible to have two points in _T_ whose distance is strictly larger than _ϵ_ when _ϵ > D_ ). Therefore


Moreover


because _M_ ( _ϵ_ + ( _D/_ 2) _, T, d_ ) _≤ M_ ( _ϵ, T, d_ ) for every _ϵ_ . We can thus state Dudley’s bound as


where the _C_ above equals twice the constant _C_ in (51). Similarly, again by splitting the above integral in two parts (over 0 to _D/_ 4 and over _D/_ 4 to _D/_ 2), we can also state Dudley’s bound as


The constant _C_ above now is 4 times the constant in (51).

2. The left hand side in (51) is bounded from below (by triangle inequality) by E max _t∈T |Xt| −_ E _|Xt_ 0 _|_ . Thus, (51) implies that


40

3. If _Xt, t ∈ T_ have mean zero and are jointly Gaussian , then _Xt − Xs_ is a mean zero normal random variable for every _s, t ∈ T_ so that (50) holds with


4. The advantages of Theorem 8.2 over Proposition 8.1 is clear from the following example. Suppose _Xt, t ∈ T_ are given by


for some positive but very very small _η_ and _X_ 0 _∼ N_ (0 _,_ Σ<sup>2</sup> and _Zt, t ∈ T ∼_<sup>_i.i.d_</sup> _N_ (0 _,_ 1). We have seen before that in this case E max _t∈T |Xt|_ should behave like _C_ Σ but Proposition 8.1 will give an extra factor of log(2 _|T |_ ). On the other hand, because


the packing number _M_ ( _ϵ, T, d_ ) will equal 1 for all but extremely small values of _ϵ_ (say for _ϵ > ϵ_ 0). Thus Dudley’s bound will give Σ + _C_ (log _|T |_ ) _ϵ_ 0 which is much smaller than the bound given by Proposition 8.1 (because _ϵ_ 0 is small).

We shall now give the proof of Theorem 8.2. The proof will be based on an idea called _chaining_ . Specifically, we shall split max _t∈T_ ( _Xt − Xt_ 0) in chains and use the bound given by Proposition 8.1 within the links of each chain.

_Proof of Theorem 8.2._ Recall that _D_ is the diameter of _T_ . For _n ≥_ 1, let _Tn_ be a maximal _D_ 2<sup>_−n_</sup> -separated subset of _T_ i.e., min _s,t∈Tn_ : _s̸_ = _t d_ ( _s, t_ ) _> D_ 2<sup>_−n_</sup> and _Tn_ has maximal cardinality subject to the separation restriction. The cardinality of _Tn_ is given by the packing number _M_ ( _D_ 2<sup>_−n_</sup> _, T, d_ ). Because of the maximality,


Because _T_ is finite and _d_ ( _s, t_ ) _>_ 0 for all _s̸_ = _t_ , the set _Tn_ will equal _T_ when _n_ is large. Let


For each _n ≥_ 1, let _πn_ : _T �→ Tn_ denote the function which maps each point _t ∈ T_ to the point in _Tn_ that is closest to _T_ (if there are multiple closest points to _T_ in _Tn_ , then choose one arbitrarily). In other words, _πn_ ( _t_ ) is chosen so that


As a result, from (52), we have


Note that _πN_ ( _t_ ) = _t_ . Finally let _T_ 0 := _{t_ 0 _}_ and _π_ 0( _t_ ) = _t_ 0 for all _t ∈ T_ .

We now note that


The sequence


can be viewed as a chain from _t_ 0 to _t_ . This is what gives the argument the name _chaining_ .

By (54), we obtain


41

so that


Now to bound E max _t∈T |Xπn_ ( _t_ ) _− Xπn−_ 1( _t_ ) _|_ for each 1 _≤ n ≤ N_ , we shall use the elementary bound given by Proposition 8.1. For this, note first that by (50), we have


Now

_d_ ( _πn_ ( _t_ ) _, πn−_ 1( _t_ )) _≤ d_ ( _πn_ ( _t_ ) _, t_ ) + _d_ ( _πn−_ 1( _t_ ) _, t_ ) _≤ D_ 2<sup>_−n_</sup> + _D_ 2<sup>_−_(</sup><sup>_n−_1)</sup> = 3 _D_ 2<sup>_−n_</sup> _._

Thus Proposition 8.1 can be applied with Σ := 3 _D_ 2<sup>_−n_</sup> so that we obtain ( **note that the value of** _C_ **might change from occurrence to occurrence** )


Plugging the above bound into (55), we deduce


Note now that for _ϵ ≤ D/_ 4, the packing number _M_ ( _ϵ, T, d_ ) _≥_ 2 so that

log(2 _M_ ( _ϵ, T, d_ )) _≤_ log 2 + log _M_ ( _ϵ, T, d_ ) _≤_ 2 log _M_ ( _ϵ, T, d_ ) _._

We have thus proved that


which proves (51).

## **8.2 Dudley’s bound for infinite** _T_

We shall next prove Dudley’s bound for the case of infinite _T_ . This requires a technical assumption called _separability_ which will always be satisfied in our applications.

**Definition 8.3** (Separable Stochastic Process) **.** _Let_ ( _T, d_ ) _be a metric space. The stochastic process {Xt, t ∈ T } indexed by T is said to be separable if there exists a null set N and a countable subset T_<sup>˜</sup> _of T such that for all ω ∈/ N and t ∈ T , there exists a sequence {tn} in T_<sup>˜</sup> _with_ lim _n→∞ d_ ( _tn, t_ ) = 0 _and_ lim _n→∞ Xtn_ ( _ω_ ) = _Xt_ ( _ω_ ) _._

42

Note that the definition of separability requires that _T_<sup>˜</sup> is a dense subset of _T_ which means that the metric space ( _T, d_ ) is separable (a metric space is said to be separable if it has a countable dense subset).

The following fact is easy to check: **If** ( _T, d_ ) **is a separable metric space and if** _Xt, t ∈ T_ **has continuous sample paths (almost surely), then** _Xt, t ∈ T_ **is separable** . The statement that _Xt, t ∈ T_ has continuous sample paths (almost surely) means that there exists a null set _N_ such that for all _ω ∈/ N_ , the function _t �→ Xt_ ( _ω_ ) is continous on _T_ .

The following fact is also easy to check: If _{Xt, t ∈ T }_ is a separable stochastic process, then


for every _t_ 0 _∈ T_ . Here _T_<sup>˜</sup> is a countable subset of _T_ which appears in the definition of separability of _Xt, t ∈ T_ .

In particular, the statement (56) implies that sup _t∈T |Xt − Xt_ 0 _|_ is measurable (note that uncountable suprema are in general not guaranteed to be measurable; but this is not an issue for separable processes).

We shall now state Dudley’s theorem for separable processes. This theorem does not impose any cardinality restrictions on _T_ (it holds for both finite and infinite _T_ ).

**Theorem 8.4.** _Let_ ( _T, d_ ) _be a separable metric space and let {Xt, t ∈ T } be a separable stochastic process. Suppose that for every s, t ∈ T and u ≥_ 0 _, we have_


_Then for every t_ 0 _∈ T , we have_


_where D is the diameter of the metric space_ ( _T, d_ ) _._

_Proof of Theorem 8.4._ Let _T_<sup>˜</sup> be a countable subset of _T_ such that (56) holds. We may assume that _T_<sup>˜</sup> contains _t_ 0 (otherwise simply add _t_ 0 to _T_<sup>˜</sup> ). For each _k ≥_ 1, let _T_<sup>˜</sup> _k_ be the finite set obtained by taking the first _k_ elements of _T_<sup>˜</sup> (in an arbitrary enumeration of the entries of _T_<sup>˜</sup> ). We can ensure that _T_<sup>˜</sup> _k_ contains _t_ 0 for every _k ≥_ 1.

Applying the finite index set version of Dudley’s theorem (Theorem 8.2) to _{Xt, t ∈ T_<sup>˜</sup> _k}_ , we obtain


Note that the right hand side does not depend on _k_ . Letting _k →∞_ on the left hand side, we use the Monotone Convergence Theorem to obtain


The proof is now completed by (56).

## **8.3 Application of Dudley’s Bound to Rademacher Averages**

Suppose _T ⊆_ R<sup>_n_</sup> and consider the stochastic process _Xt, t ∈ T_ given by


43

where _ϵ_ 1 _, . . . , ϵn_ are i.i.d Rademacher random variables.

Let us define the following norm on R<sup>_n_</sup> :


In other words, _∥t∥n_ is the usual Euclidean norm of _t_ divided by<sup>_√_</sup> _<u>n</u>_ <u>.</u> Also let _dn_ ( _s, t_ ) := _∥s − t∥n_ be the corresponding metric on R<sup>_n_</sup> .

By Hoeffding’s inequality, for every _u ≥_ 0,


so that _Xt, t ∈ T_ satisfies the assumptions in Dudley’s theorems with the metric _dn_ . Also note that _T_ = R<sup>_n_</sup> is trivially separable and that the map


is linear (and hence continuous in _t_ ). This means that _Xt, t ∈ T_ is separable. We can therefore apply Dudley’s theorem. We apply Theorem 8.4 with _t_ 0 = (0 _, . . . ,_ 0) (since this vector may not be contained in _T_ , we shall apply Theorem 8.4 to _T ∪{_ 0 _}_ ) to obtain


where the diameter and packing numbers above are with respect to the _dn_ metric. It is now easy to see that


We thus obtain the following upper bound:


In the next class, we shall combine the above bound with the technique of symmetrization which will give us an important upper bound on the suprema of empirical processes.

---

[← 7 Lecture 7](08-7-lecture-7.md) · [Up: contents](index.md) · [9 Lecture 9 →](10-9-lecture-9.md)
