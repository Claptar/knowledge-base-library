---
title: 23 Lecture 23
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 23 Lecture 23

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The main goal of this lecture is to prove the following theorem (from Van der Vaart [24, Theorem 5.23]) which proves asymptotic normality of _M_ -estimators under some general conditions. To simplify the proof slightly, I have made some simplifications to the theorem (such as assuming that the criterion functions are indexed by R; the full theorem in Van der Vaart [24, Theorem 5.23] applies to the case where the criterion functions are indexed by an open set in R<sup>_k_</sup> for a fixed _k_ ).

## **23.1 An abstract** _M_ **-estimation result**

**Theorem 23.1.** _Suppose {mθ, θ ∈_ R _} be a class of functions indexed by_ R _. Given i.i.d observations X_ 1 _, . . . , Xn having distribution P , we consider the estimator θ_<sup>ˆ</sup> _n defined as any maximizer of Pnmθ over θ ∈_ R _. Let θ_ 0 _be the population analogue of θ_<sup>ˆ</sup> _n defined as any maximizer of Pmθ over θ ∈_ R _. Suppose that the following assumptions hold:_

_1. Assume that θ �→ mθ_ ( _x_ ) _is differentiable at θ_ 0 _with derivative m_ ˙ _θ_ 0( _x_ ) _for almost sure x (w.r.t P )._

_2. Assume that there exists a function_ Γ( _x_ ) _with P_ Γ<sup>2</sup> _< ∞ (i.e.,_ Γ _∈ L_<sup>2</sup> ( _P_ ) _) such that_


_for all θ_ 1 _, θ_ 2 _and x._

122

_3. Suppose that θ �→ M_ ( _θ_ ) := _Pmθ is twice continuously differentiable at θ_ 0 _with M_<sup>_′′_</sup> ( _θ_ 0) _<_ 0 _. 4. θ_<sup>ˆ</sup> _n is consistent for θ_ 0 _i.e., θ_<sup>ˆ</sup> _n→P θ_ 0 _as n →∞._

_Then the following two conclusions holds:_

_1. The rate of convergence of θ_<sup>ˆ</sup> _n to θ_ 0 _is n_<sup>_−_1</sup><sup>_/_2</sup> _i.e., |θ_<sup>ˆ</sup> _n − θ_ 0 _|_ = _OP_ ( _n_<sup>_−_1</sup><sup>_/_2</sup> ) _._

_2. The following holds:_


Before proceeding to the proof of this Theorem, let us first look at the following remarks.

1. The conditions of the theorem hold when _mθ_ ( _x_ ) = _−|x − θ|_ and thus this theorem can be viewed as a generalization of our limiting distribution result for the sample median from last class.

2. Note that the criterion function _θ �→ mθ_ ( _x_ ) is only assumed to be once differentiable with respect to _θ_ at _θ_ 0 (almost surely with respect to _x_ ). But the limit function _M_ ( _θ_ ) = _Pmθ_ is assumed to be twice differentiable. If we insist on the criterion function to be twice differentiable, then the theorem will no longer be applicable to functions such as _mθ_ ( _x_ ) = _−|x − θ|_ . However, classical proofs for asymptotic normality of _M_ -estimators will do Taylor expansions to second order and these arguments require existence of second derivatives (and some additional regularity).

3. _θ_ 0 is not assumed to be a unique maximum of _M_ ( _θ_ ) _, θ ∈_ R. Instead of this, it is assumed that _θ_<sup>ˆ</sup> _n_ is consistent for _θ_ 0 i.e., it converges in probability to _θ_ 0. This means that _θ_<sup>ˆ</sup> _n_ will be close to _θ_ 0 and to get detailed the asymptotic picture for _θ_<sup>ˆ</sup> _n_ , we can focus on local regions of _θ_ 0. This theorem is therefore a local result where all attention is focussed on local regions of _θ_ 0.

We shall now prove Theorem 23.1. It will use several ideas and results that we have seen so far in this course.

_Proof of Theorem 23.1._ The first task is to prove that the rate of convergence is _n_<sup>_−_1</sup><sup>_/_2</sup> . For this, we can directly use the rate theorem. Letting _Mn_ ( _θ_ ) := _Pnmθ_ and _d_ ( _θ, θ_ 0) = _|θ − θ_ 0 _|_ , it is easy to check that the conditions of the rate theorem hold (the key assumption is that _M_ ( _θ_ 0) _− M_ ( _θ_ ) ≳ _d_<sup>2</sup> ( _θ, θ_ 0)) which follows from the assumption that _M_<sup>_′′_</sup> ( _θ_ 0) _<_ 0. To determine the rate, we have to bound


and then equate the bound to _δ_<sup>2</sup> . The above quantity equals


To control the above expected supremum, we use the bracketing bound (from Lecture 12):


The relevant class _H_ here is _{mθ − mθ_ 0 : _|θ − θ_ 0 _| ≤ δ}_ and its envelope (by the Lipschitz condition (215)) can be taken to be _H_ ( _x_ ) := Γ( _x_ ) _δ_ . We thus have


123

To control the bracketing numbers above, we use this result from Lecture 12: If Θ _⊆_ R<sup>_d_</sup> is contained in a ball of radius _R_ and if _{gθ_ : _θ ∈_ Θ _}_ is a function class which satisfies _|gθ_ 1( _x_ ) _− gθ_ 2( _x_ ) _| ≤_ Υ( _x_ ) _∥θ_ 1 _− θ_ 2 _∥_ for all _x_ and _θ_ 1 _, θ_ 2 _∈_ Θ. If Υ _∈ L_<sup>2</sup> ( _P_ ), then


Using this result with the class _{gθ_ : _|θ − θ_ 0 _| ≤ δ}_ with _gθ_ := _mθ − mθ_ 0 and Υ = Γ, we obtain


We thus obtain


because _∥_ Γ _∥L_ 2( _P_ ) is finite. Therefore to get a rate upper bound for _|θ_<sup>ˆ</sup> _n − θ_ 0 _|_ , we can solve _δn_<sup>_−_1</sup><sup>_/_2</sup> = _δ_<sup>2</sup> which gives _δ_ = _n_<sup>_−_1</sup><sup>_/_2</sup> . We have thus proved that _|θ_<sup>ˆ</sup> _n − θ_ 0 _|_ = _OP_ ( _n_<sup>_−_1</sup><sup>_/_2</sup> ).

Now we shall attempt to prove (216). For this, we consider the process


indexed by _h ∈_ R which can be decomposed as _M_<sup>˜</sup> _n_ ( _h_ ) = _An_ ( _h_ ) + _Bn_ ( _h_ ) where


and _Bn_ ( _h_ ) = _n_ � _M_ ( _θ_ 0 + _hn_<sup>_−_1</sup><sup>_/_2</sup> ) _− M_ ( _θ_ 0)�. By a second order Taylor expansion of _M_ around _θ_ 0 (note that we have assumed that _M_ ( _θ_ ) is twice continuously differentiable at its point of maximum _θ_ 0 with _M_<sup>_′′_</sup> ( _θ_ 0) _<_ 0; this also implies that _M_<sup>_′_</sup> ( _θ_ 0) = 0), it can be proved that _Bn_ ( _h_ ) converges to


for each fixed _h ∈_ R. We will now show that _An_ converges to a stochastic process _A_ ( _h_ ) in _ℓ_<sup>_∞_</sup> [ _−K, K_ ] for each fixed _K_ . To prove this, the first step is to establish finite dimensional converges i.e., that ( _An_ ( _h_ 1) _, . . . , An_ ( _hk_ )) converges in distribution for a fixed _k_ and _h_ 1 _, . . . , hk_ . For this, we shall use the Lindeberg-Feller CLT. Observe that


where

_Yni_ = � _mθ_ 0+ _h_ 1 _n−_ 1 _/_ 2( _Xi_ ) _− mθ_ 0( _Xi_ ) _, mθ_ 0+ _h_ 2 _n−_ 1 _/_ 2( _Xi_ ) _− mθ_ 0( _Xi_ ) _, . . . , mθ_ 0+ _hkn−_ 1 _/_ 2( _Xi_ ) _− mθ_ 0( _Xi_ ) _._ � _._ Because _X_ 1 _, . . . , Xn_ are i.i.d, we have Cov(<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Yni_) =</sup><sup>_n_Cov(</sup><sup>_Yn_1).Nowforeachfixed</sup><sup>_h ∈_R,</sup> _n_ var � _mθ_ 0+ _hn−_ 1 _/_ 2( _X_ 1) _− mθ_ 0( _X_ 1)� = E � _√n_ � _mθ_ 0+ _hn−_ 1 _/_ 2( _X_ 1) _− mθ_ 0( _X_ 1)��2 _−_ �E<sup>_√_</sup> _n_ � _mθ_ 0+ _hn−_ 1 _/_ 2( _X_ 1) _− mθ_ 0( _X_ 1)��2 Now by the almost sure first order derivative assumption on the criterion function _mθ_ ( _x_ ) at _θ_ 0, we have _√n_ � _mθ_ 0+ _hn−_ 1 _/_ 2( _X_ 1) _− mθ_ 0( _X_ 1)� _→ hm_ ˙ _θ_ 0( _X_ 1) almost surely _._

Also by the Lipschitz assumption (215), we have


124

Thus by the dominated convergence theorem, we obtain

_n_ var � _mθ_ 0+ _hn−_ 1 _/_ 2( _X_ 1) _− mθ_ 0( _X_ 1)� _→ h_<sup>2</sup> var( _m_ ˙ _θ_ 0( _X_ 1)) as _n →∞._

Similarly, for every fixed _h_ 1 and _h_ 2, we have

_n_ Cov � _mθ_ 0+ _h_ 1 _n−_ 1 _/_ 2( _X_ 1) _− mθ_ 0( _X_ 1) _, mθ_ 0+ _h_ 2 _n−_ 1 _/_ 2( _X_ 1) _− mθ_ 0( _X_ 1)� _→_ E _h_ 1 _h_ 2 ( ˙ _mθ_ 0( _X_ 1))<sup>2</sup> _− h_ 1 _h_ 2 (E _m_ ˙ _θ_ 0( _X_ 1))<sup>2</sup> = _h_ 1 _h_ 2var( ˙ _mθ_ 0( _X_ 1)) _._

Therefore

where


Further, note that


Therefore


which converges to zero as _n →∞_ by the Dominated Convergence theorem (note that we have assumed that EΓ<sup>2</sup> ( _X_ 1) _< ∞_ ). The assumptions of the Lindeberg-Feller CLT are all satisfied and we can thus conclude that


for every fixed _k ≥_ 1 and _h_ 1 _, . . . , hk ∈_ R.

To convert this finite-dimensional convergence to process level convergence in _ℓ_<sup>_∞_</sup> [ _−K, K_ ] for each fixed _K_ , we need to prove stochastic equicontinuity for which we need to bound


where


By the Lipschitz assumption (215), it is clear that the function _x �→ ηn_<sup>_−_1</sup><sup>_/_2</sup> Γ( _x_ ) is an envelope for _Gη_ . Thus the bound (217) gives


It is easy to see that for a small enough positive constant _c_ ,


125

Thus by using (218) to control the bracketing numbers on the right hand side above, we obtain


We thus obtain


where _CK_ is a constant that only depends on _K_ . The right hand side above clearly goes to zero as _η →_ 0. This proves stochastic equicontinuity of _{An_ ( _h_ ) _, −K ≤ h ≤ K}_ . Together with the finite dimensional convergence result established earlier, we can deduce that _An→L A_ in _ℓ∞_ [ _−K, K_ ] for every _K ≥_ 0.

It can also be proved that the earlier convergence of _Bn_ ( _h_ ) to _B_ ( _h_ ) for each fixed _h ∈_ R can be improved to uniform convergence on [ _−K, K_ ]. This is a consequence of twice continuous differentiability of _M_ at _θ_ 0.

Using _An→L A_ in _ℓ∞_ [ _−K, K_ ] and _Bn → B_ uniformly on [ _−K, K_ ], we can deduce that _M_ ˜ _n_ = _An_ + _Bn→L M_ ˜ := _A_ + _B_ in _ℓ_<sup>_∞_</sup> [ _−K, K_ ]. We can therefore use the argmax continuous mapping theorem (all of whose conditions are met) to conclude that


This completes the proof of Theorem 23.1.

## **23.2 Application to MLE**

Theorem 23.1 applies to maximum likelihood estimators. Suppose _P_ = _{Pθ, θ ∈_ Θ _}_ denote a class of probability measures where Θ is an open subset of R and assume that _X_ 1 _, . . . , Xn_ are i.i.d observations from _Pθ_ 0. Assume that each _Pθ_ has a density _pθ_ with respect to a common dominating measure _µ_ . In this setting, Theorem 23.1 applies to _mθ_ ( _x_ ) = log _pθ_ ( _x_ ) and _P_ = _Pθ_ 0. If the assumptions of Theorem 23.1 hold, then it follows that every MLE _θ_<sup>ˆ</sup> _n_ has<sup>_√_</sup> _<u>n</u>_ rate of convergence and


The advantage of this result is that it only requires that log _pθ_ is once differentiable at _θ_ 0 for almost sure _x_ (the function _m_ ˙ _θ_ 0( _x_ ) is called the score function). In comparison, traditional results on the asymptotic normality of the MLE require the existence of at least two derivatives of log _pθ_ at _θ_ 0. The asymptotic variance is given by


The numerator here is the Fisher information _I_ ( _θ_ 0). Under additional smoothness assumptions on _m_ ˙ _θ_ 0( _x_ ), it can be shown that _M_<sup>_′′_</sup> ( _θ_ 0) = _−I_ ( _θ_ 0) so that the asymptotic variance is the familiar 1 _/I_ ( _θ_ 0). The cleanest assumption involving the extra smoothness is Le Cam’s differentiability in quadratic mean.

**Definition 23.2** (Differentiability in Quadratic Mean (DQM)) **.** _We say that {Pθ, θ ∈_ Θ _} is differentiable in quadratic mean at θ_ 0 _∈_ Θ _if there exists a function ℓ_<sup>˙</sup> _θ_ 0 _∈ L_<sup>2</sup> ( _Pθ_ 0) _such that_


126

Under the DQM assumption, the function _ℓ_<sup>˙</sup> _θ_ 0 plays the role of the score function and Fisher information will be defined by _I_ ( _θ_ 0) = var _Pθ_ 0 ( _ℓ_<sup>˙</sup> _θ_ 0( _X_ 1)) (more details will be given in the next lecture). The next result asserts the _N_ (0 _,_ 1 _/I_ ( _θ_ 0)) asymptotic distribution of the MLE under DQM and an additional Lipschitz assumption on log _pθ_ . This is Van der Vaart [24, Theorem 5.39].

**Theorem 23.3.** _Suppose_ Θ _is an open set with θ_ 0 _∈_ Θ _. Assume that {Pθ, θ ∈_ Θ _} satisfies DQM at θ_ 0 _. Assume also that_


_for all x and θ_ 1 _, θ_ 2 _in a neighborhood of θ_ 0 _with Pθ_ 0Γ<sup>2</sup> _< ∞. If I_ ( _θ_ 0) _>_ 0 _and if θ_<sup>ˆ</sup> _n is consistent for θ_ 0 _, then_


A crucial ingredient in the proof of Theorem 23.3 is the fact that the DQM property implies another propery known as Local Asymptotic Normality (LAN). We say that _{Pθ, θ ∈_ Θ _}_ satisfies LAN at _θ_ 0 if


where _Sn_ converges in distribution to _N_ (0 _, I_ ( _θ_ 0)) under _Pθ_ 0. It will be shown in the next lecture that DQM at _θ_ 0 implies the LAN with _I_ = _I_ ( _θ_ 0). It should be clear that (220) along with the additional Lipschitz assumption (219) as well as the consistency of _θ_<sup>ˆ</sup> _n_ implies (23.3). Indeed note first that the left hand side of (220) is _M_<sup>˜</sup> _n_ ( _h_ ). If we define _M_<sup>˜</sup> ( _h_ ) = _hZ√I − h_<sup>2</sup> _I/_ 2 where _Z ∼ N_ (0 _,_ 1) and _I_ = _I_ ( _θ_ 0), then the (220) implies that the finite dimensional distributions of _M_<sup>˜</sup> _n_ converge in distribution to those of _M_<sup>˜</sup> . Under the Lipschitz assumption (219), this finite dimensional convergence can be supplemented with process convergence to yield convergence in _ℓ_<sup>_∞_</sup> [ _−K, K_ ] for every fixed _K ≥_ 0. One can then use the argmax continuous mapping theorem to yield (23.3). This will complete the proof of Theorem 23.3. Therefore establishing (220) under the DQM assumption is key for the proof of Theorem 23.3. We shall prove this important fact (that DQM implies LAN) in the next lecture.

---

[← 22 Lecture 22](23-22-lecture-22.md) · [Up: contents](index.md) · [24 Lecture 24 →](25-24-lecture-24.md)
