---
title: April 6
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# April 6

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **22.1 Entropy Rate**

_Setting_ : ( _Xi, i ≥_ 0) is stationary, ergodic, _S_ -valued.

**Theorem** : _Ln_ = _p_ ( _X_ 0 _, X_ 1 _, . . . , Xn−_ 1), where _p_ ( _x_ 0 _, x_ 1 _, . . . , xn−_ 1) = P( _Xi_ = _xi,_ 0 _≤ i ≤ n −_ 1). Then, _− n_<sup>1log</sup><sup>_Ln_</sup> _−−→_<sup>a.s.</sup> _H_ (constant) as _n →∞._

Call _H_ the **entropy rate** of the process ( _Xi_ ).

Recall that for a PM _π_ on _S_ , _H_ ( _π_ ) def=<sup>�</sup> _s_<sup>_π_(</sup><sup>_s_) log</sup><sup>_π_(</sup><sup>_s_) =</sup><sup>_−_E[log</sup><sup>_π_(</sup><sup>_X_)]if</sup><sup>_X_</sup> _∼d π_ is the **entropy** of _π_ .

The proof of the Shannon-McMillan-Breiman Theorem 21.2 gave a formula for the entropy rate


in terms of the function _p_ ( _x_ 0 _| x−_ 1 _, x−_ 2 _, . . . , x−n_ ).

**Example 22.1.** If ( _Xi_ ) is IID( _π_ ), then _p_ ( _x_ 0 _| x−_ 1) = _π_ ( _x_ 0), so _H_ = _−_ E[log _π_ ( _X_ 0)] = _H_ ( _π_ ).

**Example 22.2.** Let ( _Xi_ ) be stationary Markov, P( _Xi_ = _x, Xi_ +1 = _y_ ) = _π_ ( _x_ ) _q_ ( _x, y_ ), where **Q** is the transition matrix.


so


**Corollary 22.3.** _Let H_<sup>ˆ</sup> _k_ = _H_ (dist( _X_ 0 _, X_ 1 _, . . . , Xk−_ 1)) _. Then,_


### **22.2 Asymptotic Equipartition Property**

_Different Viewpoint_ . What do we know about ( _Xi_ ) if we are told _H_ but don’t know _p_ ( _x_ 0 _, . . . , xn_ )?

85

_LECTURE 22. APRIL 6_

86

Consider _Bk ⊆ S_<sup>_k_</sup> .


In fact, (b) holds for


### **22.3 Subadditive Ergodic Theorem**

_Background_ :


2. If the ( _ξi_ ) are stationary, then for any fixed _k ≥_ 1,


_LECTURE 22. APRIL 6_

87

**Theorem 22.5** (Kingman’s Subadditive Ergodic Theorem) **.** _Suppose we have_ R _-valued random variables_ ( _Xm,n_ : 0 _≤ m < n < ∞_ ) _satisfy_ (22.1) _and_


_and Then_


The Durrett text gives an alternate “Liggett” version. See the text for the proof.

Often, it is useful to show limits exist without explicit calculation.

**Example 22.6** (Products of Random Matrices) **.** Let _A_ 1 _, A_ 2 _, . . ._ be a stationary sequence of random _s × s_ matrices, with entries _Am_ ( _i, j_ ) _>_ 0. Consider the random matrix _αm,n_ = _Am_ +1 _Am_ +2 _· · · An_ .

**Proposition 22.7.** _If_ E _|_ log _A_ 1( _i, j_ ) _| < ∞∀i, j, then_


_(some X)._

_Proof._ Define _Xm,n_ = _−_ log _αm,n_ (1 _,_ 1). _α_ 0 _,n_ = _α_ 0 _,mαm,n_ , so _α_ 0 _,n_ (1 _,_ 1) _≥ α_ 0 _,m_ (1 _,_ 1) _αm,n_ (1 _,_ 1). Therefore, _Xm,n_ has property (22.2) and property (22.1) follows from the fact that ( _Ai_ ) is stationary.


Note that _α_ 0 _,n_ (1 _,_ 1) is the sum of _s_<sup>_n−_1</sup> terms of the form _A_ 1(1 _, i_ 1) _A_ 2( _i_ 1 _, i_ 2) _· · · An_ ( _in−_ 1 _,_ 1), so


so


which is (22.3). 22.5 implies


For the general ( _i, j_ ) entry,


_LECTURE 22. APRIL 6_

88

so _−_<sup>1</sup> a.s. _n_<sup>log</sup><sup>_α_0</sup><sup>_,n_(</sup><sup>_i, j_)</sup><sup>_→−X_</sup>

**Example 22.8** (First Passage Percolation on Square Lattice) **.** Let ( _τe, e ∈ E_ ) be IID, 0 _< τe < ∞_ , E _τe < ∞_ , where _E_ is the edges of the Z<sup>2</sup> lattice. Define _Xm,n_ to be the time to travel from ( _m,_ 0) to ( _n,_ 0): _Xm,n_ = min _{_<sup>�</sup> _e∈π_<sup>_τe_:</sup><sup>_π_apathfrom(</sup><sup>_m,_0)to(</sup><sup>_n,_0)</sup><sup>_}_.</sup>

_Check Hypotheses_ . (22.1) holds because the ( _τe_ ) are invariant under translation by _k_ .

_Xm,n ≤_ minimum time route from (0 _,_ 0) to (0 _, n_ ) via ( _m,_ 0) = _X_ 0 _,m_ + _Xm,n,_ which checks (22.2). _X_ 0 _,_ 1 _≤ τe_ , so E _X_ 0<sup>+</sup> _,_ 1<sup>_< ∞_,whichchecks(22.3).22.5implies</sup> 1 _n_<sup>_X_0</sup><sup>_,n→_some</sup><sup>_X._</sup>

Note that changing a finite number of the _τe_ does not change _X_ . Therefore, _X ∈_ tail( _τe, e ∈ E_ ), which is trivial by the 0-1 Law, so _X_ is constant.

## **Lecture 23**

---

[← April 4](23-april-4.md) · [Up: contents](index.md) · [April 11 →](25-april-11.md)
