---
title: 16 Lecture 16
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 16 Lecture 16

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last lecture, we studied the behavior of the soft thresholding estimator in the Gaussian sequence model _Y ∼ Nn_ ( _θ_<sup>_∗_</sup> _, In_ ). We noted that this estimator is just the same as LASSO and looked at bounds on its risk in the case where _θ_<sup>_∗_</sup> has exact sparsity and in the case of weak sparsity. We start this lecture with hard thresholding which has many similar properties to the soft thresholding estimator.

## **16.1 Hard Thresholding Estimator**

The hard thresholding function is defined as:


Let us fix on the first definition above for concreteness. In words, hard _λ_ ( _y_ ) equals 0 when _−λ ≤ y ≤ λ_ and equals _y_ otherwise. It is similar to soft _λ_ ( _y_ ) in that both equal 0 when _|y| ≤ λ_ . However, it is different in that it is discontinuous in _y_ while soft _λ_ ( _y_ ) is continuous.

The Hard Thresholding estimator _θ_<sup>ˆ</sup> _λ_<sup>_H_for</sup><sup>_θ∗_intheGaussiansequencemodel</sup><sup>_Y∼N_(</sup><sup>_θ∗, In_)isgivenby</sup>


It is easy to see that _θ_<sup>ˆ</sup> _λ_<sup>_H_isthesolutiontotheoptimizationproblem:</sup>


where _∥θ∥_ 0 :=<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_I{θi̸_= 0</sup><sup>_}_.</sup>

81

Note the similarity and dissimilarity of this optimization with the soft-thresholding (or LASSO) which is


Notice that the tuning parameter in _θ_<sup>ˆ</sup> _λ_<sup>_H_is</sup><sup>_λ_2whileitis</sup><sup>_λ_in</sup><sup>_θ_ˆ</sup> _λ_<sup>_S_.Alsothereisnofactorof1</sup><sup>_/_2forthesum</sup> of squares term in _θ_<sup>ˆ</sup> _λ_<sup>_H_.</sup>

The hard thresholding estimator _θ_<sup>ˆ</sup> _λ_<sup>_H_hasverysimilarpropertiestothesoftthresholdingestimatorin</sup> sparse settings. For example, we shall show below that when _θ_<sup>_∗_</sup> is _k_ -sparse (i.e., _∥θ_<sup>_∗_</sup> _∥_ 0 = _k_ ) with _k/n →_ 0,


To see this, write


where


Therefore


It is now easy to see that


where the integral above was computed by integration by parts. The standard Mills ratio bound now gives


It can also be shown (homework) that


Unlike soft thresholding, the function _µ �→ rH_ ( _λ, µ_ ) is not monotonically increasing in _µ >_ 0. Indeed, it is easy to see that lim _µ→∞ rH_ ( _λ, µ_ ) = 1 but the maximum is achieved at some finite _µ_ (near _λ_ ).

Because of the above facts, it follows that


The choice _λ_ = �2 log( _n/k_ ) now easily gives (132). It also follows that


It is also true that _θ_<sup>ˆ</sup> _λ_<sup>_H_workssimilarlytosoftthresholdingundertheassumption</sup><sup>_∥θ∗∥_</sup> 1<sup>_≤Cn_(thisishome-</sup> work).

82

## **16.2 Linear Regression**

We shall now study the linear regression model. Here we observe again a data vector _Y ∈_ R<sup>_n_</sup> that we shall model as


for some known deterministic _n × p_ matrix _X_ . The _p ×_ 1 parameter _θ_<sup>_∗_</sup> is the unknown parameter of interest.

Given an estimator _θ_<sup>ˆ</sup> of _θ_<sup>_∗_</sup> , we will be interested in the _prediction risk_ :


2 Depending on the particular context, it might be more or less natural to study E _/n_ but this will ��� _θ_ ˆ _− θ∗_ ��� usually require more assumptions on _X_ and we shall refrain from studying this loss function.

Both the hard and soft thresholding estimators can be extended in a straightforward manner to the case of Linear Regression. The extension of the hard thresholding estimator will be:


Note that when _X_ = _I_ , we used this estimator under sparse settings with _λ_ = �2 log( _n/k_ ) or _λ_ =<sup>_√_</sup> 2 log _n_ . Therefore the term multiplying _∥θ∥_ 0 in (134) will involve log _n_ . For this reason, we shall refer to this estimator as the BIC estimator (see, for example, `https://en.wikipedia.org/wiki/Bayesian_information_ criterion` ) and denote this by _θ_<sup>ˆ</sup> _λ_<sup>BIC</sup> .

The extension of the soft thresholding estimator directly gives the LASSO estimator:


We shall analyze both these estimators in terms of the prediction risk (133). We shall focus mainly on the exact sparsity setting where _k_ := _∥θ_<sup>_∗_</sup> _∥_ 0 is small compared to _p_ and _n_ . From the computational perspective, it is easy to see that (135) can be computed via convex optimization while (134) can be very hard to compute depending on _X_ (in the worst case, computing (134) is NP hard).

Let us start with the analysis for the BIC estimator (134).

## **16.3 The Prediction Risk of** _θ_<sup>ˆBIC</sup> _λ_

The key question is: when _θ_<sup>_∗_</sup> is _k_ -sparse, does the BIC estimator, properly regularized, have prediction risk bounded by a constant multiple of ( _k/n_ )(log( _ep/k_ ))? We shall see that this will be true **without any assumptions** on the design matrix _X_ .

Before answering this question, let us first analyze a simple estimator that is given by


This estimator simply minimizes the sum of squares over all _θ_ having at most _k_ entries. Remember that _k_ is the _L_ 0 norm of the true vector _θ_<sup>_∗_</sup> so that _∥θ_<sup>_∗_</sup> _∥_ 0 needs to be known for using this estimator. We shall prove that for this estimator,


83

for a universal constant _C_ . Let us first use the rate theorem to see why this should be true. We can write _θ_<sup>ˆ</sup> as


where Θ := _{θ ∈_ R<sup>_n_</sup> : _∥θ∥_ 0 _≤ k}_ and


We will use the rate theorem with this _Mn_ and


Thus to obtain the rate via the rate theorem, we need to bound


where _V_ consists of all vectors _v ∈_ R<sup>_n_</sup> with _∥v∥≤ u_ and which satisfy _v_ = _X_ ( _θ − θ_<sup>_∗_</sup> ) for some _θ_ with _∥θ∥_ 0 _≤ k_ . We shall use Dudley’s entropy bound to control the expected supremum above:


where _M_ ( _ϵ, V_ ) and diam( _V_ ) are the packing number and diameter in the usual Euclidean metric on R<sup>_n_</sup> .

Note now that for every _θ_ with _∥θ∥_ 0 _≤ k_ , we have _∥θ − θ_<sup>_∗_</sup> _∥_ 0 _≤_ 2 _k_ (because _∥θ_<sup>_∗_</sup> _∥_ 0 _≤ k_ ). As a result, we can write


(where _|S|_ denotes the cardinality of _S_ ) where _VS_ denotes the set of all vectors _v ∈_ R<sup>_n_</sup> for which _∥v∥≤ u_ and _v_ = _Xβ_ for some _β_ that is supported on _S_ (i.e., _{i_ : _βi̸_ = 0 _} ⊆ S_ ). Therefore, we deduce that


Because,


where _XS_ is the matrix formed by including only those columns of _X_ whose indices belong to _S_ and _C_ ( _XS_ ) denotes the column space of _XS_ . This means that _VS_ is a ball in a linear subspace of dimension at most 2 _k_ so that (by an earlier result on packing numbers of balls in linear spaces)


Plugging this in (136), we obtain


84

Equating this to _u_<sup>2</sup> , we would obtain


This suggests therefore that


As usual, our rate theorem is not strong enough to give this expectation control. To prove the above bound, we can argue as follows. The basic inequality corresponding to the _M_ -estimator _θ_<sup>ˆ</sup> is: _M_ ( _θ_<sup>_∗_</sup> ) _− M_ ( _θ_<sup>ˆ</sup> ) _≤_ ( _Mn − M_ )( _θ_<sup>ˆ</sup> _− θ_<sup>_∗_</sup> ) which is the same as

so that


where


This gives


Note that we have just rigorously proved that


From here and the fact that


is a Lipschitz function (with Lipschitz constant 2), one can prove that


which proves (137).

One way to see how (138) implies (139) is via the following important result on the concentration of Lipschitz functions of Gaussian random vectors.

**Theorem 16.1.** _Suppose f_ : R<sup>_n_</sup> _→_ R _is an L-Lipschitz function i.e., |f_ ( _x_ ) _− f_ ( _y_ ) _| ≤ L ∥x − y∥ and suppose Z ∼ N_ (0 _, In_ ) _. Then for all t ≥_ 0 _,_


85

Theorem 16.1 can be used to derive (139) from (138). Indeed, let


It is easy to see then that _f_ is 1-Lipschitz. Indeed,


Because every vector in _V_<sup>_∗_</sup> has norm at most 1, we conclude that _f_ is 1-Lipschitz. Thus, by (140),

so


As a result


This gives


This, combined with (138), allows us to deduce


which proves (139).

---

[← 15 Lecture 15](16-15-lecture-15.md) · [Up: contents](index.md) · [17 Lecture 17 →](18-17-lecture-17.md)
