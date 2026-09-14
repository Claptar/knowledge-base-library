---
title: 18 Lecture 18
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 18 Lecture 18

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The main topic for study is to complete the discussion of the performance of the LASSO, in terms of prediction risk, for the case of exact sparsity. Let us first recap the ideas from the previous couple of lectures and present the main problem of interest.

## **18.1 Recap: linear regression with exact sparsity**

We observe a data vector _Y ∈_ R<sup>_n_</sup> that we model as


91

_X_ is a deterministic _n × p_ matrix and _θ_<sup>_∗_</sup> is a vector in R<sup>_p_</sup> . The dimension _p_ can be larger than the sample size _n_ . We shall work with the assumption of exact sparsity where _θ_<sup>_∗_</sup> is supported on a subset _S ⊂{_ 1 _, . . . , p}_ with _|S|_ = _k_ and _k_ is assumed to be smaller than both _p_ and _n_ . The prediction error of an estimator _θ_<sup>ˆ</sup> is defined as


We shall study the prediction error of the LASSO defined as


Before proceeding, let us first recall the following observations:

1. If we know the support _S_ of _θ_<sup>_∗_</sup> , then one can simply estimate _θ_<sup>_∗_</sup> by linear regression of _Y_ on _XS_ (where _XS_ is the matrix obtained from _X_ by dropping columns not present in _S_ ). It is elementary to check that this _Oracle_ estimator will satisfy the prediction error bound:


in expectation and in high probability. It is important to note that there are no assumptions on the _X_ matrix here and the bound above is independent of scaling. If I change _X_ by multiplying each column by a constant, then the bound will not change.

2. We have seen in the last class that the BIC estimator defined by


achieves the prediction error bound


with high probability and in expectation provided that the tuning parameter _λ_ is chosen as _c_ 1 ~~�~~ log( _ep_ ) for a large enough _c_ 1. Therefore compared to the Oracle estimator described above, the BIC estimator only pays a price that is logarithmic in _p_ . However, even though efficient computation of _θ_<sup>ˆ</sup> _λ_<sup>BIC</sup> is possible for certain special design matrices _X_ (e.g., when _X_ = _In_ or when _X_ ( _i, j_ ) = _I{i ≥ j}_ for 1 _≤ i, j ≤ n_ ), in most cases, it is computationally intractable.

In light of the above two observations, it is most interesting to see if _θ_<sup>ˆ</sup> _λ_<sup>LASSO</sup> satisfies


Indeed, unlike _θ_<sup>ˆ</sup> _λ_<sup>BIC</sup> , the lasso estimator is computationally tractable and can be obtained efficiently by convex optimization for fairly large values of _n_ and _p_ . It is therefore of interest to see if any price is to be paid in terms of prediction risk performance (compared to _θ_<sup>ˆ</sup> _λ_<sup>BIC</sup> ) for this computational tractability.

We shall see below that (154) will be true **under some assumptions on** _X_ . These assumptions are unfortunately quite restrictive and cannot usually be checked in practice. At a high level, these assumptions can be understood to be saying that _X_ behaves like an identity matrix in a certain sense. Note that we already know that (154) is true when _X_ is the identity matrix (in this case, _θ_<sup>ˆ</sup> _λ_<sup>LASSO</sup> is the soft thresholding estimator).

92

## **18.2 Prediction Error of the LASSO under Exact Sparsity**

We shall complete the argument that we started in the last class to establish (154) under some assumptions on _X_ .

As a simple consequence of the basic inequality for the LASSO, we proved, in the last class, the following inequality (where we write _θ_<sup>ˆ</sup> for _θ_<sup>ˆ</sup> _λ_<sup>LASSO</sup> for simplicity):


We now take the tuning parameter _λ_ to be such that


The following analysis can be done with _λ ≥_ (1+ _η_ ) �� _X T ϵ_ �� _∞_<sup>for any</sup><sup>_η>_0 but it is customary to take</sup><sup>_η_= 1.</sup> The choice (156) for _λ_ immediately implies that �� _X T ϵ_ �� _∞_<sup>_≤λ/_2.Usingthisontherighthandsidein(155),</sup> we obtain


which readily simplifies to

Note that this inequality simultaneously implies the following two inequalities:

The first inequality in (157) above can be rewritten as


because _θS_<sup>_∗c_= 0(notethat</sup><sup>_S_isthesupportof</sup><sup>_θ∗_).Thismeansthat</sup><sup>_θ_ˆ</sup><sup>_−θ∗∈CS_where</sup>

_CS_ := _{_ ∆ _∈_ R<sup>_p_</sup> : _∥_ ∆ _Sc ∥_ 1 _≤_ 3 _∥_ ∆ _S∥_ 1 _} ._

Note that the set _Cs_ is a convex cone.

The second inequality in (157) is obviously more relevant for proving the prediction risk bound (154) of _θ_ ˆ _λ_<sup>LASSO</sup> . Indeed, dividing both sides by _n_ , we obtain


We shall now plug in an explicit value for _λ_ . Indeed by the assumption that _ϵ ∼ N_ (0 _, In_ ), the assumption (156) will be satisfied with high probability for


for a sufficiently large value of _c_ 1. Here _X_ 1 _, . . . , Xp_ denote the columns of _X_ . Plugging this value of _λ_ in the bound above, we obtain


for a constant _C_ depending on _c_ 1. We shall now impose a particular scaling on the columns of _X_ . Specifically, we assume that


93

For this scaling, the above bound becomes

which we can rewrite as


From here, it is obvious that the required bound (154) holds provided


is bounded from above by a constant. This is exactly the standard assumption under which (154) is proved. To make the assumption seem less blatant, one usually bounds the above quantity as:


where the infimum can be taken over any set in R<sup>_p_</sup> which contains _θ_<sup>ˆ</sup> _− θ_<sup>_∗_</sup> . Because we know that _θ_<sup>ˆ</sup> _− θ_<sup>_∗_</sup> _∈CS_ when _λ_ satisfies (156) (see (158)), we can take the infimum above over ∆ _∈CS_ which gives


The quantity


is called the _compatibility factor_ . We thus have proved that


with high probability and expectation when _λ_ is chosen as in (159). If we now make the assumption that


for a constant _φ_ 0, then we have proved that (154) holds. The assumption (162) above is called the _compatibility condition_ . It is a property of the design matrix _X_ and the set _S_ (which is the support of _θ_<sup>_∗_</sup> ). Because it depends on the unknown _θ_<sup>_∗_</sup> , it cannot be verified in practice. One therefore replaces it by the assumption that


This is, in principle, verifiable because it only depends on the design matrix _X_ and the sparsity level _k_ of the unknown _θ_<sup>_∗_</sup> . But, unfortunately, even if _k_ is known, verifying (163) requires going over all subsets of _{_ 1 _, . . . , p}_ of size _≤ k_ which is computationally intractable.

Let us now quickly go over _restricted eigenvalues_ which are closely related to compatibility factors. By the Cauchy-Schwarz inequality, we have


94

As a result


This quantity _γ_ ( _S_ ) is called a restricted eigenvalue of _X_ . Clearly because _γ_ ( _S_ ) is smaller than _φ_ ( _S_ ), inequality (161) also holds if _φ_ ( _S_ ) is replaced by _γ_ ( _S_ ) which means that (154) holds under the assumption that


for a constant _γ_ 0. This is called the restricted eigenvalue (RE) conditon which implies (and hence weaker than) the compatibility condition. Unfortunately, checking (164) is also computationally intractable and hopeless in practice.

## **18.3 A simple sufficient condition for checking the RE and compatibility conditons**

The following lemma presents a simple sufficient condition for checking the assumptions (163) and (164). The condition (165) on _X_ that appears in this lemma is sometimes referred to by the phrase: “ _X_ is _ρ_ -incoherent”.

**Lemma 18.1.** _Suppose X is an n × p matrix such that_


_Then for every S ⊆{_ 1 _, . . . , p} with cardinality k, we have_


Note that the first assumption in (165) just means that each column of _X_ is normalized to have norm equal to<sup>_√_</sup> _<u>n</u>_ <u>.</u> Also the conclusion (166) is non-trivial only when _ρ <_ 1 _/_ (16 _k_ ). For example, when _ρ ≤_ 1 _/_ (32 _k_ ), then (166) says that _γ_ ( _S_ ) _≥_ 1 _/√_ 2.

_Proof of Lemma 18.1._ We need to prove that


for every ∆ _∈_ R<sup>_p_</sup> satisfying _∥_ ∆ _Sc ∥_ 1 _≤_ 3 _∥_ ∆ _S∥_ 1. Fix such a ∆and write


Note now that _∥_ ∆ _∥_ 1 = _∥_ ∆ _Sc ∥_ 1 + _∥_ ∆ _S∥_ 1 _≤_ 4 _∥_ ∆ _S∥_ 1 under the assumption that _∥_ ∆ _Sc ∥_ 1 _≤_ 3 _∥_ ∆ _S∥_ 1. We therefore obtain


which completes the proof.

95

## **18.4 The Restricted Isometry Property**

The Restricted Isometry Property (RIP) is related to the RE and compatibility conditions. It is defined as follows.

**Definition 18.2** (RIP) **.** _Let X be an n×p matrix. For δ ∈_ (0 _,_ 1) _and k ≤ p, we say that X has the RIP_ ( _δ, k_ ) _property if_


_for all_ ∆ _∈_ R<sup>_p_</sup> _with ∥_ ∆ _∥_ 0 _≤ k._

For _S ⊆{_ 1 _, . . . , p}_ , let _XS_ denote the _n ×|S|_ submatrix of _X_ formed by dropping all the columns _Xi_ of _X_ for _i ∈/ S_ . With this notation, it is easy to see that the above definition of RIP is equivalent to the following definition.

**Definition 18.3** (Alternative Definition of RIP) **.** _Let X be an n × p matrix. For δ ∈_ (0 _,_ 1) _and k ≤ p, we say that X has the RIP_ ( _δ, k_ ) _property if_


_for every subset S ⊆{_ 1 _, . . . , p} with |S| ≤ k. Here λ_ min _and λ_ max _refer to the smallest and largest eigenvalue respectively._

From (168), it is clear that for _Xn×p_ to satisfy the _RIP_ ( _δ, k_ ) property, it is necessary that _n ≥ k_ . The following result shows that the RIP property implies the RE condition.

**Lemma 18.4.** _Suppose X satisfies RIP_ ( _δ, k_ + _m_ ) _. Then for every S ⊆{_ 1 _, . . . , p} with |S| ≤ k, we have_


From (169), it is trivial to deduce the following:

This means


For example, by taking _δ_ = 1 _/_ 4 and _u_ = 1 _/_ 5, we obtain


Thus, using Lemma 18.4, we can deduce a positive lower bound on inf _S⊆{_ 1 _,...,p}_ : _|S|≤k γ_ ( _S_ ) provided _RIP_ ( _δ, m_ ) holds for a small constant _δ_ and _m_ equal to a constant (depending on _δ_ ) multiple of _k_ .

_Proof of Lemma 18.4._ We need to prove that


96

for every ∆ _∈_ R<sup>_p_</sup> satisfying _∥_ ∆ _Sc ∥_ 1 _≤_ 3 _∥_ ∆ _S∥_ 1. Fix such a vector ∆. Let _I_ 1 consist of the indices in _S_<sup>_c_</sup> corresponding to the _m_ largest (in absolute value) entries of ∆. Also, let _I_ 2 consist of the indices in ( _S ∪ I_ 1)<sup>_c_</sup> corresponding to the _m_ largest (in absolute value) entries of ∆. Continue this way to define a partition _I_ 1 _, . . . , Il_ of _S_<sup>_c_</sup> with


We now write


so that


We now use the fact that _X_ satisfies _RIP_ ( _δ, k_ + _m_ ) which gives (note that _|S ∪ I_ 1 _| ≤ k_ + _m_ and _|Ii| ≤ m_ for all _i_ )


Now, by construction, the absolute value of every entry in ∆ _Ii_ is smaller than the absolute value of every entry in ∆ _Ii−_ 1. This implies, in particular, that the absolute value of every entry in ∆ _Ii_ is smaller than the average of the absolute values of entries in ∆ _Ii−_ 1. This gives


As a result, we obtain


Using the cone condition _∥_ ∆ _Sc ∥_ 1 _≤_ 3 _∥_ ∆ _S∥_ 1, we further deduce


which completes the proof.

An important fact is that the RIP will be satisfied by certain kinds of random matrices _X_ with high probability. It then means (by the above lemma) that for such matrices _X_ , the RE condition will hold with high probability. The simplest example of this is when the entries of _X_ are i.i.d standard Gaussian. This is proved below (the proof is taken from Baraniuk et al. [1]; see the paper for extensions to some other random ensembles).

**Theorem 18.5.** _Suppose that the entries of the n × p matrix X are independent and identically distributed as N_ (0 _,_ 1) _. Then X satisfies RIP_ ( _δ, k_ ) _with probability at least_ 1 _−_ exp( _−nδ_<sup>2</sup> _/_ 64) _provided_


_Proof._ It is easy to see that because the entries of _X_ are i.i.d _N_ (0 _,_ 1), we have


97

Now _χ_<sup>2</sup> _n_<sup>randomvariablessatisfythestandardconcentrationinequality(whoseproofisleftasexercise):</sup>


This immediately gives that for every ∆ _∈_ R<sup>_p_</sup> and _δ ∈_ (0 _,_ 1)


Because 1 + _δ/_ 2 _≤_ (1 + _δ/_ 2)<sup>2</sup> and 1 _− δ/_ 2 _≥_ (1 _− δ/_ 2)<sup>2</sup> , we also have

Now let ∆1 _, . . . ,_ ∆ _M_ be a maximal _δ/_ 4-packing subset (in the usual Euclidean metric) of the set

_{_ ∆: _∥_ ∆ _∥_ = 1 and _∥_ ∆ _∥_ 0 _≤ k} ._

By a standard volumetric argument, it can be shown that


By the union bound, it follows from (170) that the probability

satisfies the bound


Suppose now that _n ≥ c_ 1 _k_ log( _ep/k_ ) for some constant _c_ 1. Then

Thus when

we have

so that

To complete the proof therefore, we only need to argue that


98

implies that


The argument for proving this implication is the following. Let _A_ be the smallest number for which


We shall show that _A ≤ δ_ . Note first that _A < ∞_ because _λ_ max( _X_<sup>_T_</sup> _X/n_ ) _< ∞_ . Now fix ∆such that _∥_ ∆ _∥_ = 1 and _∥_ ∆ _∥_ 0 _≤ k_ . By the packing property and construction of _{_ ∆1 _, . . . ,_ ∆ _M }_ , there will exist 1 _≤ j ≤ M_ such that _∥_ ∆ _−_ ∆ _j∥≤ δ/_ 4 and _∥_ ∆ _−_ ∆ _j∥_ 0 _≤ k_ . Write


where to get the final inequality we used (171) and (173) with ∆replaced by ∆ _−_ ∆ _j_ . Because _∥_ ∆ _j∥_ = 1 and _∥_ ∆ _−_ ∆ _j∥≤ δ/_ 4, we obtain


Comparing this with (173), we deduce that (by the definition of _A_ )


which gives _A ≤ δ_ . This proves the upper inequality in (172). To prove the lower inequality, write


Using (171) and (173) with _A_ = _δ_ (note that we can choose ∆ _j_ so that _∥_ ∆ _−_ ∆ _j∥_ 0 _≤ k_ ), we get


This proves the lower bound in (172) and completes the proof of the theorem.

---

[← 17 Lecture 17](18-17-lecture-17.md) · [Up: contents](index.md) · [19 Lecture 19 →](20-19-lecture-19.md)
