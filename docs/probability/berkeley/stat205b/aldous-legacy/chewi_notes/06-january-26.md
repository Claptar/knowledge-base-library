---
title: January 26
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# January 26

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 Applications of Inversion Formula**

**Inversion Formula** : If a PM _µ_ has CF _φ_ such that � _−∞∞_<sup>_|φ_(</sup><sup>_t_)</sup><sup>_|_d</sup><sup>_t<∞_,then</sup><sup>_µ_hasaboundedcontinuous</sup> density


In general, _φaW_ ( _t_ ) = _φW_ ( _at_ ).

**Corollary 4.1.** _Given a PM µ with CF φ and density f , suppose φ is_ R _-valued, φ ≥_ 0 _, and_


_Then,_


_is a density function, and its CF is f_ ( _t_ ) _/f_ (0) _. Here, f and g are called_ **_dual pairs_** _._

_Proof._ By the inversion formula,


For _y_ = 0,


**Example 4.2** (Last Class) **.** If


16

_LECTURE 4. JANUARY 26_

17


the standard Cauchy distribution, and this has CF _f_ ( _t_ ) _/f_ (0) = _e_<sup>_−|t|_</sup> , for _−∞ < t < ∞_ . Write _W_ for a RV with the standard Cauchy distribution. Take _W_ 1 _, W_ 2 _, . . ._ , IID copies of _W_ .

_φW_ 1+ _W_ 2+ _···_ + _Wn_ ( _t_ ) = ( _e_<sup>_−|t|_</sup> )<sup>_n_</sup> = _e_<sup>_−n|t|_</sup> = _φnW_ ( _t_ ) _._ By uniqueness,<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Wi_</sup> =d _nW_ , so


The LLN does not hold. _E|W |_ = _∞_ .

### **4.2 Another Proof of Inversion**

_Exercise_ : If _Yn −→_ d _c_ , then _Yn → c_ in probability. If _Yn −→_ d _c_ , then _X_ + _Yn −→_ d _X_ + _c_ (for any _X_ ).

_2nd Proof of Inversion Formula._ Take _X_ with dist( _X_ ) = _µ_ . Take _Zσ_ =d Normal(0 _, σ_ 2), independent of _X_ . _X_ + _Zσ −→_ d _X_ as _σ ↓_ 0. Note: _X_ + _Zσ_ has density


Use Parseval’s Identity for the normal distribution, _θ_ = 1 _/σ_ .


Then, _φX−x_ ( _t_ ) = _e_<sup>_−ixt_</sup> _φX_ ( _t_ ). Applying the above to _X − x_ instead of _X_ , we have


Let _σ ↓_ 0. Appeal to bounded convergence.


Final detail:


_LECTURE 4. JANUARY 26_

18

at continuity points _a_ , _b_ of _X_ . The limit is � _ab_<sup>_f_(</sup><sup>_x_) d</sup><sup>_x_.Thisisenoughtoprovethat</sup><sup>_f_isthedensityof</sup> _X_ .

### **4.3 Continuity Theorem**

**Theorem 4.3** (Continuity Theorem) **.** _Suppose Xn has CF φn._

- _(a) If Xn −→_ d _X∞, then φn_ ( _t_ ) _→ φ∞_ ( _t_ ) _, for each t. (b) Suppose_ lim _n→∞ φn_ ( _t_ ) _exists (_ = _φ_ ( _t_ ) _, say), for each t. If either (1) φ is a CF, or (2) φ_ ( _t_ ) _→_ 1 _as t →_ 0 _, or (3)_ ( _Xn, n ≥_ 1) _are tight,_

- _then Xn −→_ d _X∞, and X∞ has CF φ._

_Proof._ (a) _Xn −→_ d _X∞_ implies that _Eg_ ( _Xn_ ) _→ Eg_ ( _X∞_ ) for bounded, continuous _g_ . Take _g_ ( _x_ ) = _eitx_ , which shows that _φn_ ( _t_ ) _→ φ∞_ ( _t_ ) as _n →∞_ , for _t_ fixed.

- (b) Suppose (3). Helly’s Theorem implies that there exists a subsequence _Xnj −→_ d some _X_ ˆ . By (a) and the hypothesis, _X_<sup>ˆ</sup> has CF _φ_ . By a previous lemma (every convergent subsequence has the same limit distribution) implies that the whole sequence _Xn −→_ d _X_ ˆ with CF _φ_ , which is a proof of (b). _Claim_ : (1) = _⇒_ (2). A CF _φ_ is continuous, with _φ_ (0) = 1. We need to prove that (2) and the hypothesis imply (3). Fix _K_ , put _c_ = 2 _/K_ . (Trick)


because sin _y ≤_ 1 and


Use the Parseval Identity for the Uniform[ _−c, c_ ] distribution.


Use bounded convergence as _n →∞_ .


On the LHS, we can take the limit as _K ↑∞_ . On the RHS, we can take the limit as _c ↓_ 0. Then, the RHS is 0 by (2), which gives tightness.

_LECTURE 4. JANUARY 26_

19

### **4.4 CFs & Moments**


This suggests that the CF _φ_ of _X_ is


However, _EX_<sup>_m_</sup> may be infinite.

**Lemma 4.4** (Technical Lemma, Durrett 3.3.7) **.**


Apply this to _y_ = _tX_ .


**Corollary 4.5.** _Suppose E|X|_<sup>_n_</sup> _< ∞. Then,_


_Proof. Zt →_ 0 a.s. as _t →_ 0, and is dominated by 2 _|X|_<sup>_n_</sup> which is integrable. Hence, _EZt →_ 0 as _t →_ 0.

## **Lecture 5**

---

[← January 24](05-january-24.md) · [Up: contents](index.md) · [January 31 →](07-january-31.md)
