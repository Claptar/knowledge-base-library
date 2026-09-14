---
title: April 4
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# April 4

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **21.1 Entropy**


is the **entropy** of _π_ .

_Easy_ : 0 _≤ H_ ( _π_ ) _≤_ log _|S|_ . _H_ (uniform distribution on _S_ ) = log _|S|_ .

( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ) is a _S_ -valued process. _p_ ( _x_ 0 _, x_ 1 _, . . . , xn−_ 1) = P( _X_ 0 = _x_ 0 _, X_ 1 = _x_ 1 _, . . . , Xn−_ 1 = _xn−_ 1). Then, _Ln_ def= _p_ ( _X_ 0 _, X_ 1 _, . . . , Xn−_ 1) is the empirical likelihood.

For IID ( _Xi_ ), dist( _Xi_ ) = _π_ , then


where _m_ ( _n, s_ ) =<sup>�</sup><sup>_n_</sup> _i_ =0<sup>_−_11(</sup><sup>_x_</sup> _i_<sup>=</sup><sup>_s_),</sup>


Informally, for a typical realization _x_ 0 _, x_ 1 _, . . . , xn−_ 1, _p_ ( _x_ 0 _, x_ 1 _, . . . , xn−_ 1) _≈_ exp( _−nH_ ( _π_ )).

**Theorem 21.2** (Shannon-McMillan-Breiman Theorem) **.** _If_ ( _Xi, i ≥_ 0) _is stationary and ergodic, then_


_for a constant_ 0 _≤ H < ∞._

The proof uses:

_•_ MG convergence

81

_LECTURE 21. APRIL 4_

82

- Ergodic Theorem

- _K_ -step Markov process

_Proof._ Embed ( _Xi, i ≥_ 0) into a doubly-infinite process ( _Xi, −∞ < i <_ + _∞_ ), which is stationary and ergodic. Write _p_ ( _xn | xn−_ 1 _, . . . , x_ 0) = P( _Xn_ = _xn | Xn−_ 1 = _xn−_ 1 _, . . . , X_ 0 = _x_ 0). Con- _n→∞_ sider _p_ ( _x_ 0 _| X−_ 1 _, X−_ 2 _, . . . , X−n_ ) _−−−−→ p_ ( _x_ 0 _| F∞_ ) since _p_ ( _x_ 0 _| X−_ 1 _, X−_ 2 _, . . . , X−n_ ) is a MG. Here, a.s. _F∞_ = _σ_ ( _X−_ 1 _, X−_ 2 _, . . ._ ). Define _Hk_ = E[ _−_ log _p_ ( _X_ 0 _| X−_ 1 _, . . . , X−k_ )]. Then,


(as _k →∞_ , by MG convergence)


The Ergodic Theorem says


for bounded measurable _F_ . Apply the Ergodic Theorem to _F_ ( _X_ 0 _, X_ 1 _, . . ._ ) = _−_ log _p_ ( _X_ 0 _|X−_ 1 _, X−_ 2 _, . . ._ ).


Elementary: _p_ ( _x_ 0 _, x_ 1 _, . . . , xn−_ 1 _| x−_ 1 _, . . . , x−k_ ) =<sup>�</sup> _m_<sup>_n−_</sup> =0<sup>1</sup><sup>_p_(</sup><sup>_xm | xm−_1</sup><sup>_, xm−_2</sup><sup>_, . . . , x_0</sup><sup>_, . . . , x−k_).Substitute</sup> in ( _X−_ 1 _, . . . , X−k_ ), let _k →∞_ , and use MG convergence.


Substitute _X_ 1 _, . . . , Xn−_ 1, take (1 _/n_ ) log( _·_ ), and apply (21.1).


Given a distribution ( _Y_ 0 _, Y_ 1) with dist( _Y_ 0) = dist( _Y_ 1) on _S_<sup>_∗_</sup> , we can construct a stationary Markov ( _X_<sup>ˆ</sup> 0 _, X_<sup>ˆ</sup> 1 _, X_<sup>ˆ</sup> 2 _, . . ._ ) with ( _X_<sup>ˆ</sup> _n, X_<sup>ˆ</sup> _n_ +1) =d ( _Y_ 0 _, Y_ 1). Take _X_ ˆ0 = _Y_ 0 and for the transitions, use the kernel _Q_ ( _x_ 0 _, x_ 1) = P( _Y_ 1 = _x_ 1 _| Y_ 0 = _x_ 0).

Given stationary _S_ -valued ( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ), set _S_<sup>_∗_</sup> = _S_<sup>_k_</sup> . Set _Y_ 0 = ( _X_ 0 _, . . . , Xk−_ 1), _Y_ 1 = ( _X_ 1 _, . . . , Xk_ ). We can construct ( _Y_<sup>ˆ</sup> _i, i ≥_ 0) as above which is stationary. The process ( _Y_<sup>ˆ</sup> 0 _, Y_<sup>ˆ</sup> 1 _, Y_<sup>ˆ</sup> 2 _, . . ._ ) has the Markov property P( _Y_<sup>ˆ</sup> _m_ = _· | Ym−_ 1 _, Ym−_ 2 _, . . ._ ) depends only on _Ym−_ 1. Extract the coordinates: ( _X_<sup>ˆ</sup> 0 _, X_<sup>ˆ</sup> 1 _, . . ._ ) is a stationary sequence with the “ _k_ -step Markov” property. P( _X_<sup>ˆ</sup> _m_ = _xm | X_<sup>ˆ</sup> _m−_ 1 = _xm−_ 1 _, . . ._ ) depends

_LECTURE 21. APRIL 4_

83

only on _xm−_ 1 _, . . . , xm−k_ and ( _X_<sup>ˆ</sup> _m, . . . , X_<sup>ˆ</sup> _m_ + _k−_ 1) = (d _X_ 0 _, X_ 1 _, . . . , Xk−_ 1).

Fix _k_ . Apply the Ergodic Theorem to _F_ ( _x_ 0 _, x−_ 1 _, . . . , x−k_ ) = _−_ log _p_ ( _x_ 0 _| x−_ 1 _, . . . , x−k_ ).


Write _p_<sup>(</sup><sup>_k_)</sup> ( _x_ 0 _, x_ 1 _, . . . , xn−_ 1) = _p_ ( _x_ 0 _, . . . , xk−_ 1)<sup>�</sup><sup>_n_</sup> _m_<sup>_−_</sup> =<sup>1</sup> _k_<sup>_p_(</sup><sup>_xm |xm−_1</sup><sup>_, . . . , xm−k_).This is the distribution of</sup> the _k_ -step Markov process.


Because the _Hk → H_ , to prove the theorem, it is enough to prove


and


Check: Given 21.3,


**Lemma 21.3.** _(a) If Wn ≥_ 0 _,_ E _Wn ≤_ 1 _, then_ lim sup _n n_<sup>_−_1</sup> log _Wn ≤_ 0 _a.s. (b)_ E<sup>_<u>p</u>_(</sup><sup>_k_)(</sup><sup>_X_0</sup><sup>_<u>, . . . , Xn−</u>_1)</sup> = 1 _. p_ ( _X_ 0 _, . . . , Xn−_ 1) _(c)_


_Proof._ (a)


Use Borel-Cantelli.

(c) To prove (21.7), it is enough to prove


_LECTURE 21. APRIL 4_

84


## **Lecture 22**

---

[← March 23](22-march-23.md) · [Up: contents](index.md) · [April 6 →](24-april-6.md)
