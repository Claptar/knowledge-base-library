---
title: 19 Lecture 19
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 19 Lecture 19

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The next topic of the class is convergence of stochastic processes. Our main motivation for studying this is to prove limiting distribution results for _M_ -estimators. We shall start with two classical examples.

## **19.1 Limiting Distribution of Sample Median**

Suppose _X_ 1 _, . . . , Xn_ are i.i.d observations from the normal density _f_ with mean _θ_ 0 and variance 1. Actually, it will be clear that results below hardly require normality and hold more generally but let us assume that _f_ is _N_ ( _θ_ 0 _,_ 1) for simplicity. Let _θ_<sup>ˆ</sup> _n_ denote a sample median based on _X_ 1 _, . . . , Xn_ defined as any minimizer of


over _θ ∈_ R. Also let _M_ ( _θ_ ) := E _|X_ 1 _− θ|_ and note that _θ_ 0 uniquely minimizes _M_ ( _θ_ ) over _θ ∈_ R.

99

We have seen in one of the homeworks that _θ_<sup>ˆ</sup> _n_ converges to _θ_ 0 in probability i.e., _θ_<sup>ˆ</sup> _n_ is a consistent estimator of _θ_ 0. Our general rate theorem can also be applied directly here to deduce that _θ_<sup>ˆ</sup> _n − θ_ 0 = _OP_ ( _n_<sup>_−_1</sup><sup>_/_2</sup> ) i.e., the rate of convergence of _θ_<sup>ˆ</sup> _n_ to _θ_ 0 is _n_<sup>_−_1</sup><sup>_/_2</sup> . We shall now address the question of finding the limiting or asymptotic distribution of<sup>_√_</sup> _<u>n</u> θ_ ˆ _n − θ_ 0 . There are many approaches for finding this limiting distribution � � but we shall follow the standard empirical processes approach which easily generalizes to other _M_ -estimators. This approach also highlights the need to study convergence of stochastic processes.

Our approach for finding the limiting distribution of<sup>_√_</sup> _<u>n</u> θ_ ˆ _n − θ_ 0 is based on the following _localized,_ � � _centered_ and _rescaled_ stochastic process:


This is a stochastic process that is indexed by _h ∈_ R. Its important property (easy to see) is that _h_<sup>ˆ</sup> _n_ := _√n_ <u>(</u> _θ_<sup>ˆ</sup> _n − θ_ 0) minimizes _M_<sup>˜</sup> _n_ ( _h_ ) _, h ∈_ R i.e.,


This _M_ ˜ _n_ ( _h_ suggests) _, h ∈_ R theandfollowingargue thatapproachit convergesto findasthe _n →∞_ limitingto somedistributionlimit processof<sup>_√_</sup> _<u>n</u>_ <u>(</u> _θM_<sup>ˆ˜</sup> _n −_ ( _h_ ) _θ, h_ 0). _∈_ WeR instudyan appropriatethe process sense. If this process convergence is strong enough, then we can hopefully argue that


It is actually not too hard to understand the behavior of _M_<sup>˜</sup> _n_ ( _h_ ) as _n →∞_ for each fixed _h ∈_ R. For this, we can write


Let us now analyze _An_ and _Bn_ separately. Clearly, _Bn_ is a deterministic sequence. To understand this, we shall use a second order Taylor explansion for _M_ ( _θ_ 0 + _n_<sup>_−_1</sup><sup>_/_2</sup> _h_ ) around _θ_ 0. Note that _M_ ( _θ_ ) := E _|X_ 1 _− θ|_ is a smooth function. Also note that _M_<sup>_′_</sup> ( _θ_ 0) = 0 because _θ_ 0 maximizes _M_ ( _θ_ ) _, θ ∈_ R. We thus get


where _θ_<sup>˜</sup> _n_ is some number between _θ_ 0 and _θ_ 0 + _n_<sup>_−_1</sup><sup>_/_2</sup> _h_ . Clearly _θ_<sup>˜</sup> _n → θ_ 0 as _n →∞_ so that


Let us now come to the mean zero random variable _An_ . To understand it, let us first compute its variance:


where I have ignored the contribution from _X_ 1 lying between _θ_ 0 and _θ_ 0 + _n_<sup>_−_1</sup><sup>_/_2</sup> _h_ (should not matter for large _n_ ; verify this). This gives


100

Now because P _{X_ 1 _< θ_ 0 _}_ = P _{X_ 1 _> θ_ 0 _}_ ( _θ_ 0 is a population median), it is easy to check that the variance of _I{X_ 1 _< θ_ 0 _} − I{X_ 1 _> θ_ 0 _}_ appearing above equals 1. We have therefore obtained


It is actually possible to prove that


For this, we can use the Lindeberg-Feller Central Limit Theorem (stated next).

## **19.2 Lindeberg-Feller Central Limit Theorem**

**Theorem 19.1.** _For each n, let Yn_ 1 _, . . . , Ynkn be kn independent random vectors with_ E _∥Yni∥_<sup>2</sup> _< ∞ for each i_ = 1 _, . . . , kn. Suppose the following two conditions hold:_


_where_ Cov( _Yni_ ) _denotes the covariance matrix of the random vector Yni and_


_Then_


For a proof of this result, see, for example, Pollard [20, Page 181]. It is easy to see that this result generalizes the usual CLT. Indeed, the usual CLT states that for i.i.d random variables _X_ 1 _, X_ 2 _, . . ._ with E _Xi_ = _µ_ , E _∥Xi∥_<sup>2</sup> _< ∞_ and Cov( _Xi_ ) = Σ, we have


Indeed this can be proved by applying Theorem 19.1 to


The condition (175) is obvious while for (176) note that


which clearly converges to zero by the Dominated Convergence Theorem (under the assumption E _∥X_ 1 _∥_<sup>2</sup> _< ∞_ ).

## **19.3 Back to the Limiting Distribution of Sample Median**

Recall the random variables _An_ from (174). The Lindeberg-Feller CLT can be used to prove that _An→L N_ (0 _, h_ 2). Note first that


101

where


we obtain


The conditions of Theorem 19.1 therefore hold and we obtain


Thus if we define


where _Z ∼ N_ (0 _,_ 1), then we have shown that


It turns out that the process _M_<sup>˜</sup> _n_ converges to _M_<sup>˜</sup> in a stronger sense than convergence in distirbution for each fixed _h ∈_ R. We shall see this later. This stronger convergence allows us to deduce that


where _F_ is the cdf corresponding to _f_ . This gives

_M_<sup>_′_</sup> ( _θ_ ) = 2 _θf_ ( _θ_ ) + 2( _F_ ( _θ_ ) _−_ 1) _−_ 2 _θf_ ( _θ_ ) = 2( _F_ ( _θ_ ) _−_ 1)

and _M_<sup>_′′_</sup> ( _θ_ ) = 2 _f_ ( _θ_ ). We thus have


To make this argument rigorous, we have to prove that the stochastic process _M_<sup>˜</sup> _n_ converges to _M_<sup>˜</sup> in a strong enough sense so that their argmins also converge.

102

## **19.4 Limiting Distribution of Sample Mode**

The general method given in the preceding section to derive the limiting distribution of sample median is quite broad and can be used for other _M_ -estimators as well. To illustrate this, let us apply this to determine the limiting distribution of sample model. Let _X_ 1 _, . . . , Xn_ de i.i.d observations from the normal density _f_ with mean _θ_ 0 and variance 1. Again the results do not require normality (and also hold if, for example, _f_ is the Cauchy density centered at _θ_ 0) but let us assume _f_ is _N_ ( _θ_ 0 _,_ 1) for simplicity.

Let _θ_<sup>ˆ</sup> _n_ denote any sample mode which is defined as any maximizer of


over _θ ∈_ R. Also let


We have previously seen that _θ_<sup>ˆ</sup> _n_ is a consistent estimator of _θ_ 0 and that


We shall now heuristically determine the limiting distribution of _n_<sup>1</sup><sup>_/_3</sup> ( _θ_<sup>ˆ</sup> _n − θ_ 0). The necessary process convergence results needed to rigorize the argument will be given later. To study _h_<sup>ˆ</sup> _n_ := _n_<sup>1</sup><sup>_/_3</sup> ( _θ_<sup>ˆ</sup> _n − θ_ 0), it is natural to define the process


and note that _h_<sup>ˆ</sup> _n_ maximizes _M_<sup>˜</sup> _n_ ( _h_ ) over _h ∈_ R. Let us try to understand the behavior of _M_<sup>˜</sup> _n_ ( _h_ ) as _n →∞_ for each fixed _h ∈_ R. First write


The expectation term _Bn_ is handled exactly as in the median case by a second order Taylor expansion of the smooth function _M_ ( _θ_ 0 + _n_<sup>_−_1</sup><sup>_/_3</sup> _h_ ) at _θ_ 0 (note that _M_<sup>_′_</sup> ( _θ_ 0) = 0) to obtain


For the stochastic term _An_ , let us, as before, start by computing its variance:

var( _An_ ) = _n_<sup>1</sup><sup>_/_3</sup> var � _I{θ_ 0 + _n_<sup>_−_1</sup><sup>_/_3</sup> _h −_ 1 _≤ X_ 1 _≤ θ_ 0 + _n_<sup>_−_1</sup><sup>_/_3</sup> + 1 _} − I{θ_ 0 _−_ 1 _≤ X_ 1 _≤ θ_ 0 + 1 _}_ � _._

If _h >_ 0 and _n_ is large, it is easy to see that


where


103

As a result


For _h <_ 0, one would have to replace _h_ by _−h_ above. Therefore, for every _h ∈_ R, we have

var( _An_ ) _→|h|_ ( _f_ ( _θ_ 0 + 1) + _f_ ( _θ_ 0 _−_ 1)) as _n →∞._

In fact, by the Lindeberg-Feller CLT (as in the case of the median), it can be shown that (this is left as homework)


Combining this with (179), we obtain


as _n →∞_ for every _h ∈_ R. Suppose now that _{Bh, h ∈_ R _}_ is a two-sided Brownian motion starting at zero i.e. _B_ 0 = 0 and _{Bh, h ≥_ 0 _}_ is a standard Brownian motion and _{B−h, h ≥_ 0 _{_ is another standard Brownian motion that is independent of _{Bh, h ≥_ 0 _}_ . Note that _Bh ∼ N_ (0 _, |h|_ ) for every _h ∈_ R. If we now define


we have


Our arguments above can be strengthened to argue that ( _M_<sup>˜</sup> _n_ ( _h_ 1) _, . . . , M_<sup>˜</sup> _n_ ( _hk_ )) converge in distribution to ( _M_<sup>˜</sup> ( _h_ 1) _, . . . , M_<sup>˜</sup> ( _hk_ )) for every fixed points _h_ 1 _, . . . , hk ∈_ R. This is a consequence of the Lindeberg-Feller CLT and left as an exercise. We shall see later that _M_<sup>˜</sup> _n_ converges to _M_<sup>˜</sup> in a much stronger sense than just for every fixed _k ≥_ 1 and points _h_ 1 _, . . . , hk ∈_ R. This stronger convergence allows us to conclude that


Because of (178), it is easy to see that _M_<sup>_′′_</sup> ( _θ_ 0) = _f_<sup>_′_</sup> ( _θ_ 0 + 1) _− f_<sup>_′_</sup> ( _θ_ 0 _−_ 1). We have therefore deduced _θ_ ˆ _n − θ_ 0 is given by (non-rigorously) that the limiting distribution of _n_<sup>1</sup><sup>_/_3 �</sup> �


Note that _f_<sup>_′_</sup> ( _θ_ 0 _−_ 1) _− f_<sup>_′_</sup> ( _θ_ 0 +1) _>_ 0. The distribution of the random variable above is related to the Chernoff distribution (see `https://en.wikipedia.org/wiki/Chernoff%27s_distribution` ).

In the next lecture, we shall see more examples of process convergence and move toward understanding and formalizing this notion more rigorously.

---

[← 18 Lecture 18](19-18-lecture-18.md) · [Up: contents](index.md) · [20 Lecture 20 →](21-20-lecture-20.md)
