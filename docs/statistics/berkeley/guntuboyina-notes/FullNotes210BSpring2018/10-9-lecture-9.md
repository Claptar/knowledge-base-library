---
title: 9 Lecture 9
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 9 Lecture 9

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let us start by recalling Dudley’s entropy bound from the last class: Suppose ( _T, d_ ) is a metric space and _{Xt, t ∈T }_ is a separable stochastic process satisfying


Then for every _t_ 0 _∈ T_ , we have


where _D_ denotes the diameter of the metric space ( _T, d_ ).

44

We applied this bound to control the expected suprema of Rademacher averages. Suppose _T_ is a subset of R<sup>_n_</sup> . Then


where


Note that if _T_ is finite, then

log _M_ ( _ϵ, T ∪{_ 0 _}, dn_ ) _≤_ 1 + log _|T |_

and hence the bound (57) implies that


Note that we had proved the above bound earlier by the elementary bound on the expected maxima of subgaussian random variables.

We shall now apply (57) together with symmetrization to obtain our main bound for the Expected suprema of an empirical process.

## **9.1 Main Bound on the Expected Suprema of Empirical Processes**

Consider the usual Empirical Process setup. Our goal is to obtain upper bounds on ∆where


Note the presence of the<sup>_√_</sup> _<u>n</u>_ in the supremums above. We have seen that symmetrization gives


We write the expectation in two parts conditioning on _X_ 1 _, . . . , Xn_ to get


The inner expectation above can be controlled via the bound (57). This gives


where _F_ ( _X_ 1 _, . . . , Xn_ ) := _{_ ( _f_ ( _X_ 1) _, . . . , f_ ( _Xn_ )) : _f ∈F}_ is a subset of R<sup>_n_</sup> ,


and _dn_ is the Euclidean metric on R<sup>_n_</sup> scaled by<sup>_√_</sup> _<u>n</u>_ <u>.</u>

45

We shall now write


where _L_<sup>2</sup> ( _Pn_ ) refers to the pseudometric on _F_ given by


Note the trivial inequality


We thus obtain


Taking expectations, we obtain


This is our first bound on the expected supremum of an empirical process. We can simplify this bound further using _envelopes_ . We say that a nonnegative valued function _F_ : _X →_ [0 _, ∞_ ) is an envelope for the class _F_ if


It is clear then that sup _f ∈F_ � _Pnf_<sup>2</sup> _≤_<sup>_√_</sup> _PnF_<sup>2</sup> so that


In the above chain of inequalities, the supremum is over all probability measures _Q_ supported on a set of cardinality at most _n_ in _X_ . Also _PF_<sup>2</sup> stands for E _F_<sup>2</sup> ( _X_ 1).

We have therefore proved the following result.

46

**Theorem 9.1.** _Let F be an envelope for the class F such that PF_<sup>2</sup> _< ∞. Then_

_where_


## **9.2 Application to Boolean Function Classes with finite VC dimension**

Let _F_ be a Boolean function class with finite VC dimension and let _D_ denote its VC dimension. Recall that the VC dimension is defined as the maximum cardinality of a set in _X_ that is shattered by the class _F_ . An important fact about the VC dimension is the Sauer-Shelah-Vapnik-Chervonenkis lemma which states that


for every _n ≥_ 1 and _x_ 1 _, . . . , xn ∈X_ where


Note that � _nk_ � in (58) is taken to be 0 if _n < k_ . The right hand of (58) equals 2<sup>_D_</sup> if _n ≤ D_ and is bounded from above by ( _en/D_ )<sup>_D_</sup> if _n ≥ D_ .

We have seen previously that


and this bound was proved by symmetrization and the elementary bound on the Rademacher averages. This elementary bound involved the cardinality of _F_ ( _X_ 1 _, . . . , Xn_ ) which we bounded via (58).

It turns out however that the logarithmic factor is redundant in (59) and one actually has the bound


This can be deduced as a consequence of Theorem 9.1 as we shall demonstrate in this section. Since Theorem 9.1 gives bounds in terms of packing numbers, it becomes necessary to relate the packing numbers of _F_ to its VC dimension. This is done in the following important result due to Dudley.

**Theorem 9.2.** _Suppose F is a Boolean function class with VC dimension D. Then_


_Here c_ 1 _and c_ 2 _are universal positive constants and the supremum is over all probability measures Q on X ._

Note that Theorem 9.2 gives upper bounds for the _ϵ_ -packing numbers when _ϵ ≤_ 1. Since the functions in _F_ take only the two values 0 and 1, it is clear that _M_ ( _ϵ, F, L_<sup>2</sup> ( _Q_ )) = 1 for all _ϵ ≥_ 1.

_Proof of Theorem 9.2._ Fix 0 _< ϵ ≤_ 1 and a probability measure _Q_ on _X_ . Let _N_ = _M_ ( _ϵ, F, L_<sup>2</sup> ( _Q_ )) and let _f_ 1 _, . . . , fN_ be a maximal _ϵ_ -separated subset of _F_ in the _L_<sup>2</sup> ( _Q_ ) metric. This means therefore that for every 1 _≤ i̸_ = _j ≤ N_ , we have


47

Now let _Z_ 1 _, Z_ 2 _, . . ._ be i.i.d observations from _Q_ . By the above, we have


By the independence of _Z_ 1 _, Z_ 2 _, . . ._ , we deduce then that for every _k ≥_ 1,


In words, this means that the probability that _fi_ and _fj_ agree on every _Z_ 1 _, . . . Zk_ is at most _e_<sup>_−kϵ_2</sup> . By the union bound, we have


This immediately gives

Thus if we take


then

P _{|F_ ( _Z_ 1 _, . . . , Zk_ ) _| ≥ N } ≥_<sup>1</sup> 2<sup>_._</sup>

Thus for the choice (62) of _k_ , there exists a subset _{z_ 1 _, . . . , zk}_ of cardinality _k_ such that


We now apply the Sauer-Shelah-VC lemma and deduce that


We now split into two cases depending on whether _k ≤ D_ or _k ≥ D_ .

**Case 1:** _k ≤ D_ : Here (63) gives


which proves (61).

**Case 2:** _k ≥ D_ : Here (63) gives


so that (using (62))


where we have used log _x ≤ x_ . This immediately gives


The proof of Theorem 9.2 is complete.

The bound (60) immediately follows from Theorem 9.1 and Theorem 9.2 as shown below.

48

**Theorem 9.3.** _Suppose F is a Boolean class of functions with VC dimension D, then_


_Proof._ Since _F_ is a Boolean class, we can apply Theorem 9.1 with _F_ ( _x_ ) = 1 for all _x_ . This gives


The packing numbers above can be bounded by Theorem 9.2 which gives


This completes the proof of Theorem 9.3.

The following are immediate applications of Theorem 9.3.

**Example 9.4.** _Suppose X_ 1 _, . . . , Xn are i.i.d real valued observations having a common cdf F . Let Fn denote the empirical cdf of the data X_ 1 _, . . . , Xn. Then Theorem 9.3 immediately gives_


_This is because the Boolean class F_ := _{I_ ( _−∞,x_ ] : _x ∈_ R _} has VC dimension 1._

_One can also obtain a high probability upper bound on_ sup _x |Fn_ ( _x_ ) _− F_ ( _x_ ) _| using the Bounded Differences concentration inequality that we discussed previously. This (together with_ (65) _) gives_


**Example 9.5** (Classification with VC Classes) **.** _Consider the classification problem where we observe i.i.d data_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _with Xi ∈X and Yi ∈{_ 0 _,_ 1 _}. Let C be a class of functions from X to {_ 0 _,_ 1 _} (these are classifiers). For a classifier g, we define its test error and training error by_


_respectively. The ERM (Empirical Risk Minimizer) classifier is given by_


_It is usually of interest to understand the test error of g_ ˆ _n relative to the best test error in the class C i.e.,_


49

_If g_<sup>_∗_</sup> _minimizes L_ ( _g_ ) _over g ∈C, then we can bound the discrepancy above as_


_The last inequality above can be quite loose (we shall look at improved bounds later). The term above can be written as_ sup _f ∈F |Pnf − Pf | where_


_Pn is the empirical distribution of_ ( _Xi, Yi_ ) _, i_ = 1 _, . . . , n and P is the distribution of_ ( _X_ 1 _, Y_ 1) _._

_Using the bounded differences concentration inequality and the bound given by Theorem 9.3, we obtain (for every α ∈_ (0 _,_ 1) _)_


_with probability ≥_ 1 _− α._

_It can now be shown that V C_ ( _F_ ) _≤ V C_ ( _C_ ) _. To see this, it is enough to argue that if F can shatter_ ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ) _, then C can shatter x_ 1 _, . . . , xn. For this, let η_ 1 _, . . . , ηn be arbitary in {_ 0 _,_ 1 _}. We need to obtain a function g ∈C for which g_ ( _xi_ ) = _ηi. Define δ_ 1 _, . . . , δn by_


_Because F can shatter_ ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ) _, there exists a function f ∈F with f_ ( _xi, yi_ ) = _δi for i_ = 1 _, . . . , n. If f_ ( _x, y_ ) = _I{g_ ( _x_ ) _̸_ = _y} for some g ∈C, then it is now easy to verify that g_ ( _xi_ ) = _ηi. This proves that C shatters x_ 1 _, . . . , xn. The proof of V C_ ( _F_ ) _≤ V C_ ( _C_ ) _is complete._

_We thus obtain from_ (66) _,_


_Thus, as long as V C_ ( _C_ ) = _o_ ( _n_ ) _, the test error of g_ ˆ _n relative to the best test error in C converges to zero as n →∞._

---

[← 8 Lecture 8](09-8-lecture-8.md) · [Up: contents](index.md) · [10 Lecture 10 →](11-10-lecture-10.md)
