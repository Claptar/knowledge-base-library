---
title: 26 Lecture 26
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 26 Lecture 26

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last lecture, we saw the important minimax lower bound:


In this lecture, we shall look at two non-trivial examples where the above bound can be used to establish sharp asymptotic minimaxity of natural estimators. The first example involves sparse normal mean estimation. The second example involves estimation of a normal mean under a power ( _L_<sup>2</sup> norm) constraint (this result is known as a finite-dimensional Pinsker’s theorem).

139

## **26.1 Sparse Normal Mean Estimation**

Consider the problem of estimating a _k_ -sparse vector _θ ∈_ R<sup>_n_</sup> from the observation _Y ∼ Nn_ ( _θ, In_ ) under squared error loss. This estimation problem can be put in the decision-theoretic framework with Θ being the set of all _k_ -sparse vectors in R<sup>_n_</sup> , _A_ = R<sup>_n_</sup> and _L_ ( _θ, a_ ) = _∥θ − a∥_<sup>2</sup> . Also _Pθ_ is the probability measure _Nn_ ( _θ, In_ ). We shall assume throughout this section that the sparsity level _k_ satisfie _k_ = _o_ ( _n_ ) (i.e., _k/n →_ 0 as _n →∞_ ).

From our earlier results, we have seen that the LASSO (which is same as soft-thresholding) estimator with tuning parameter _λ_ = �2 log( _n/k_ ) satisfies


We shall now show that this estimator is sharp asymptotically minimax by proving that


The argument below is taken from Johnstone [11, Section 8.6].

We first work with _k_ = 1 (and then later argue for general _k_ = _o_ ( _n_ )). For _k_ = 1, the parameter Θ is particularly simple and consists of 1-sparse vectors in R<sup>_n_</sup> . Here a natural prior is the uniform prior on the finite parameter set _{τe_ 1 _, . . . , τen}_ where _ei_ is the usual standard unit vector and _τ ≥_ 0 will be chosen (depending on _n_ ) appropriately. Let us denote this prior by _w_ .

Let the posterior distribution be denoted by ( _p_ 1 _n_ ( _Y_ ) _, p_ 2 _n_ ( _Y_ ) _, . . . , pnn_ ( _Y_ )) (i.e., _pin_ ( _Y_ ) is the posterior probability associated with _τei_ ). It is easy to see that

and thus


The posterior mean (which is the Bayes estimator) is therefore given by ( _τp_ 1 _n_ ( _Y_ ) _, . . . , τpnn_ ( _Y_ )). The Bayes risk with respect to this prior is thus


By replacing the inner sum above by only the term corresponding to _i_ = _I_ , we obtain the lower bound


By symmetry each term above will take the same value and we therefore get


To compute the above expectation (note that _τ_ is not a constant but it changes with _n_ ), we switch to standard gaussian random variables _z_ 1 _, . . . , zn_ by taking _Y_ 1 = _τ_ + _z_ 1 and _Yi_ = _zi_ for _i ≥_ 2. Then we need to compute:


140

We shall show that for


the quantity _S_ converges to 1. This would then imply that


which will prove the required lower bound (240) for _k_ = 1.

For ease of notation, let us denote _λn_ =<sup>_√_</sup> 2 log _n_ so that exp( _−λ_<sup>2</sup> _n_<sup>_/_2) =</sup><sup>_n−_1.Toprovethat</sup><sup>_S_= 1 +</sup><sup>_o_(1)</sup> for _τn_ := _λn −_ log _λn_ , we only need to show that the sequence of random variables


converges to 0 in probability. Note that _An_ is precisely the posterior probability of _τe_ 1 (and we are working in the case when the truth is _τe_ 1). Thus _An_ converging to zero in probability means that the posterior probability of _τe_ 1 (when the truth is _τe_ 1) goes to zero which intuitively means that the spike will be missed.


where


It is easy to see that _Vn_ converges to + _∞_ in probability. To see this, write

Because _λ_ =<sup>_√_</sup> 2 log _n_ ,


Now


as _n →∞_ (almost surely) because _λn − τn →∞_ .

Therefore in order to prove that _An_ goes to 0 in probability, we only need to show that _Wn−_ 1 goes to 1 in probability. Reindex and call _n −_ 1 to be _n_ for simplicity.


This is just an average of i.i.d mean one random variables. But _τn_ depends on _n_ so we cannot apply the usual weak law of large numbers. We can use however the following version of the weak law.

**Theorem 26.1.** _For each n, let Xnk,_ 1 _≤ k ≤ n be independent random variables. Let bn >_ 0 _with bn →∞ and let X_<sup>˜</sup> _nk_ := _Xnk{|Xnk| ≤ bn}. Suppose that as n →∞_


141

_Let Sn_ := _Xn_ 1 + _· · ·_ + _Xnn and put an_ :=<sup>�</sup><sup>_n_</sup> _k_ =1<sup>E</sup><sup>_X_˜</sup><sup>_nk.Then_</sup>


We shall apply the above theorem with _Xnk_ := _e_<sup>_τnzk_</sup> and _bn_ = _e_<sup>_τnλn_</sup> (recall _λn_ :=<sup>_√_</sup> 2 log _n_ ). The first condition in Theorem 26.1 can be checked as follows. Note that _{|Xnk| ≤ bn}_ = _{zk ≤ λn}_ so that


To verify the second condition in Theorem 26.1, we need to compute E _X_<sup>˜</sup> _nk_<sup>_r_for</sup><sup>_r_= 2:</sup>


Observe that _λn_ will be smaller than 2 _τn_ eventually so that _λn −_ 2 _τn_ will be negative. Therefore

Thus


as _n →∞_ .

The two conditions of Theorem 26.1 have been verified so we can apply it now. We need to calculate _an_ for which we can simply use (241) with _r_ = 1. This will give


Theorem 26.1 therefore gives


which is the same as


Therefore


From (242), we have


Because _λn − τn →∞_ and _λn_ + _τn →∞_ , we have


142

which is what we wanted to prove. This proves (240) for _k_ = 1.

To prove (240) for general _k_ = _o_ ( _n_ ), the idea is to use an _independent blocks_ prior. Divide the indices _{_ 1 _, . . . , n}_ into _kn_ blocks each of size _m_ = _mn_ = _⌊n/kn⌋_ . On each block, use a single spike prior as in the case of _k_ = 1. The overall prior would then make these _kn_ blocks independent. Because of independence, the Bayes risk adds up and we obtain the overall lower bound of 2 _k_ log( _n/k_ )(1 + _o_ (1)). We would need the assumption that _k/n →_ 0 because in each block we need the number of observations _mn_ to go to infinity. This completes the proof of (240).

## **26.2 Normal Mean Estimation under Power Constraint (Finite-dimensional Pinsker’s Theorem)**

Consider the problem of estimating a vector _θ ∈_ R<sup>_n_</sup> from _Y ∼ Nn_ ( _θ, In_ ) in the loss function


under the following constraint:


Let Θ denote the class of all _θ ∈_ R<sup>_n_</sup> satisfying the above constraint (the constraint is often referred to as the Power Constraint in signal processing and information theory). Let _A_ = R<sup>_n_</sup> and as usual _Pθ_ is the _Nn_ ( _θ, In_ ) distribution. The risk of an estimator _θ_<sup>ˆ</sup> is given by


What are good candidate estimators for _θ_ under the power constraint (243)? The most natural estimator is the projection of _Y_ onto Θ. This is an _M_ -estimator which can be analyzed by our earlier techniques. In fact, in this case, the projection has the explicit form


Note that this is a non-linear estimator. It turns out that in this problem, simple linear estimators of the form _αY_ for appropriate _α >_ 0 perform very well. This will be demonstrated below. First of all, note that the risk of _αY_ is given by


Under the power constraint (243), we have


The value of _α_ that minimizes the right hand side is


and its risk is given by


143

It turns out that the linear estimator _α_<sup>_∗_</sup> _Y_ is sharp asymptotically minimax in this problem. To prove this, we shall show below that


The first step in proving (244) is to choose an appropriate prior _w_ on Θ. The most natural choice for _w_ might seem to be the uniform prior on Θ. However, it is slightly simpler to work with the following prior. Let _π_ denote the _Nn_ (0 _, δ_<sup>2</sup> _c_<sup>2</sup> _In_ ) distribution on R<sup>_n_</sup> where _δ ∈_ (0 _,_ 1). We shall take _w_ to be the conditional probability measure under _π_ conditioned to be in Θ i.e.,


for Borel subsets _A_ of R<sup>_n_</sup> . Let _θ_<sup>ˆ</sup> _B_ ( _w_ ) denote the Bayes estimator with respect to the prior _w_ . Note that because _w_ is supported on the convex set Θ, the estimator _θ_<sup>ˆ</sup> _B_ ( _w_ ) will belong to Θ with probability one. We then have


Because _π_ is the _Nn_ (0 _, δ_<sup>2</sup> _c_<sup>2</sup> _In_ ) prior, its Bayes risk can be easily computed in closed form as


so that we obtain


Note now that by the elementary inequality _∥a − b∥_<sup>2</sup> _≤_ 2 _∥a∥_<sup>2</sup> + 2 _∥b∥_<sup>2</sup> , we have

This gives


by the Cauchy-Schwarz inequality. Now under _π_ ,


so that


Putting things together, we obtain


144

because _π_ (Θ) _≤_ 1. We complete the argument, we just need lower bounds on _π_ (Θ<sup>_c_</sup> ). For this, note that


Using the chi-squared concentration inequality

we obtain


Thus for 0 _._ 5 _≤ δ_<sup>2</sup> _≤_ 1, we obtain


As a result, we have


which implies that


Since _δ_<sup>2</sup> _∈_ [0 _._ 5 _,_ 1] here is arbitrary, we can let _δ_<sup>2</sup> _→_ 1 to obtain (244). This completes the proof of the sharp asymptotic minimaxity of the linear estimator _α_<sup>_∗_</sup> _Y_ .

From the above two examples of sharp asymptotic minimaxity, it should be clear that the key to these arguments is the choice of an appropriate prior _w_ . Also once the prior _w_ is chosen, the argument is usually intricate because we do not even want to lose constant factors in _n_ .

We shall next study arguments for rate minimaxity where it will be okay to lose constant factors while bounding the minimax risk from below. These arguments are much simpler and one uses discrete priors (most often uniform priors on a finite subset of the parameter space). We shall study these (which are related to bounds in multi-hypothesis testing problems) next week.

---

[← 25 Lecture 25](26-25-lecture-25.md) · [Up: contents](index.md) · [27 Lecture 27 →](28-27-lecture-27.md)
