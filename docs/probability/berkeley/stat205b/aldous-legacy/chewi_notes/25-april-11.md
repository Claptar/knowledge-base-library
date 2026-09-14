---
title: April 11
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# April 11

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **23.1 Law of Iterated Logarithm**

Let _B_ ( _t_ ) _,_ 0 _≤ t < ∞_ be standard Brownian motion.

_Curious Fact_ : _B_ ˆ( _t_ ) = _tB_ (1 _/t_ ) is also standard BM (calculate the covariance E[ ˆ _B_ ( _s_ ) ˆ _B_ ( _t_ )]). So, limits as _t →∞_ are “equivalent” to limits as _t →_ 0.


We will prove (23.1). Recall:

**Lemma 23.2.** _If c >_ 0 _, d >_ 0 _,_


89

_LECTURE 23. APRIL 11_

90

23.2 implies


Borel-Cantelli 1 implies

Consider small _t_ , say _θ_<sup>_n_+1</sup> _< t < θ_<sup>_n_</sup> , _n > n_ 0( _ω_ ). Then,

since _h_ ( _t_ ) _≥ h_ ( _θ_<sup>_n_+1</sup> ) _≥ θ_<sup>1</sup><sup>_/_2</sup> _h_ ( _θ_<sup>_n_</sup> ) for _n_ large (check). Hence,

Let _δ ↓_ 0 and _θ ↑_ 1.

_Lower Bound_ . Fix _θ >_ 0. Suppose we prove

P( _B_ ( _θ_<sup>_n_</sup> ) _− B_ ( _θ_<sup>_n_+1</sup> ) _>_ (1 _− θ_ )<sup>1</sup><sup>_/_2</sup> _h_ ( _θ_<sup>_n_</sup> ) infinitely often) = 1 _._ (23.2)

Then, by the upper bound (applied to _−B_ ( _t_ )), _−B_ ( _θ_<sup>_n_+1</sup> ) _≤_ 2 _h_ ( _θ_<sup>_n_+1</sup> ) ultimately. Combining these two facts, _B_ ( _θ_<sup>_n_</sup> ) _≥_ (1 _− θ_ )<sup>1</sup><sup>_/_2</sup> _h_ ( _θ_<sup>_n_</sup> ) _−_ 2 _h_ ( _θ_<sup>_n_+1</sup> ) infinitely often. But,


since _h_ ( _t_ ) =<sup>_√_</sup> 2 _t_ log log _t_ , so _B_ ( _θ_<sup>_n_</sup> ) _≥_ ((1 _− θ_ )<sup>1</sup><sup>_/_2</sup> _−_ 4 _θ_<sup>1</sup><sup>_/_2</sup> ) _h_ ( _θ_<sup>_n_</sup> ) infinitely often. Hence,


Let _θ ↓_ 0.

_Proof of_ (23.2): For _Z_ , Normal(0 _,_ 1),


So,


Since the summation<sup>�</sup> _n_<sup>(</sup><sup>_·_) =</sup><sup>_∞_,Borel-Cantelli2implies(23.2).</sup>

_LECTURE 23. APRIL 11_

91

### **23.2 Embedding Distributions into BM**

Consider _B_ ( _t_ ). Take _U ≤_ 0 _≤ V_ (dependent), but independent of _B_ ( _t_ ) with E _U_ + E _V_ = 0. Let


(205A) Conditional on ( _U_ = _u, V_ = _v_ ), E _BT_<sup>2= E</sup><sup>_T_=</sup><sup>_−uv_,E</sup><sup>_BT_= 0.</sup>


( _B_<sup>2</sup> ( _t_ ) _− t_ is a MG.) Since E[ _BT_<sup>2</sup><sup>_| UV_] = E[</sup><sup>_T| UV_],thenE</sup><sup>_B_</sup> _T_<sup>2= E</sup><sup>_T_,E</sup><sup>_BT_= 0.</sup>


**Proposition 23.3.** _Given_ dist( _X_ ) _with_ E _X_ = 0 _, there exists a joint distribution_ ( _U, V_ ) _such that BT_ =d _X._

_Proof._ We prove the case where _X_ has some density _f_ ( _x_ ). Recall _x_ = _x_<sup>+</sup> _− x_<sup>_−_</sup> . Then,


Take the joint density for ( _U, V_ )


Check that the total mass is 1.


The inner integral is

So

Also,


The Morters-Peres book section 5.3 gives other embeddings _B_ ( _T_ ) = givend _X_ .

_LECTURE 23. APRIL 11_

92

### **23.3 Donsker’s Invariance Principle**

**Donsker’s Invariance Principle** says that BM is the scaling limit of random walks.

_Set-Up_ : We have IID ( _Xi_ ), E _X_ = 0, E _X_<sup>2</sup> = 1, _Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi_.Interpolatetocontinuous</sup><sup>_S_(</sup><sup>_t_).</sup> _S_ ( _t_ ) = _S⌊t⌋_ + ( _t −⌊t⌋_ )( _S⌈t⌉ − S⌊t⌋_ ) _._

Rescale time and space.


We can regard _Sn_<sup>_∗_asarandomfunction,aRVtakingvaluesinthespace</sup><sup>_C_[0</sup><sup>_,_1]ofcontinuousfunctions</sup> _f_ : [0 _,_ 1] _→_ R. We can consider ( _B_ ( _t_ ) _,_ 0 _≤ t ≤_ 1) as a RV _B_ taking values in _C_ [0 _,_ 1].

The theory of weak convergence on metric spaces formalizes the idea “ _Sn_<sup>_∗_</sup> _−→_ d _B_ ”.

The assertion _Sn_<sup>_∗_(1)</sup> _−→_ d _B_ (1) is the assertion


which is the CLT.

## **Lecture 24**

---

[← April 6](24-april-6.md) · [Up: contents](index.md) · [April 13 →](26-april-13.md)
