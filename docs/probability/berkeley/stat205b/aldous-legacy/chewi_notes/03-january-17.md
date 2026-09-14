---
title: January 17
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# January 17

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **1.1 Convergence in Distribution**

We have two definitions:

- Probability measure (PM) _µ_ on R,

- Distribution function _F_ on R.

Given _µ_ , _F_ ( _x_ ) def= _µ_ ( _−∞, x_ ] is a distribution function.

Given _F_ , there exists a _µ_ such that _F_ ( _x_ ) = _µ_ ( _−∞, x_ ].

_x_ is a **continuity point** of _F_ if _F_ ( _x_ ) = _F_ ( _x−_ ), which means _µ{x}_ = 0.

**Theorem 1.1.** _For PMs_ ( _µn,_ 1 _≤ n < ∞_ ) _and µ on_ R _, the following are equivalent._

_1. Fµn_ ( _x_ ) _→ Fµ_ ( _x_ ) _as n →∞ for all continuity points x of F ._

_n→∞ 2._ � _−∞∞_<sup>_g_(</sup><sup>_x_)</sup><sup>_µn_(d</sup><sup>_x_)</sup> _−−−−→_ � _−∞∞_<sup>_g_(</sup><sup>_x_)</sup><sup>_µ_(d</sup><sup>_x_)</sup><sup>_forallboundedcontinuousg_: R</sup><sup>_→_R</sup><sup>_._</sup>

_3. There exist, on some probability space, RVs_ ( _X_<sup>ˆ</sup> _n,_ 1 _≤ n < ∞_ ) _and_ ( _X_<sup>ˆ</sup> ) _such that for all_ 1 _≤ n < ∞,_ dist( _X_<sup>ˆ</sup> _n_ ) = dist( _Xn_ ) _,_ dist( _X_<sup>ˆ</sup> ) = dist( _X_ ) _, and X_<sup>ˆ</sup> _n → X_<sup>ˆ</sup> _a.s. as n →∞._

_Note_ : 2 and 3 make sense for PMs on a metric space _S_ and define “weak convergence” on _S_ . In fact, 2 _⇔_ 3 on general _S_ (“Skorohod representation theorem”). The theorem shows that 1 is not just arbitrary.

dist( _X_ ) is often written as _L_ ( _X_ ) (for “law”). Write _Xn −→_ d _X_ “in distribution” to mean dist( _Xn_ ) _→_ dist( _X_ ). Call this “weak convergence” _µn → µ_ .

_Proof._ 3 = _⇒_ 2: _X_ ˆ _n → X_ ˆ a.s. implies that _g_ ( ˆ _Xn_ ) _→ g_ ( ˆ _X_ ) a.s. ( _g_ is continuous), which implies that _Eg_ ( _X_<sup>ˆ</sup> _n_ ) _→ Eg_ ( _X_<sup>ˆ</sup> ) ( _g_ is bounded), which implies that _Eg_ ( _Xn_ ) _→ Eg_ ( _X_ ). 2 is equivalent to saying _Eg_ ( _Xn_ ) _→ Eg_ ( _X_ ) for all bounded, continuous _g_ .

2 = _⇒_ 1: Fix _x_ 0 and define _fj_ ( _x_ ) by 1 when _x ≤ x_ 0, 0 when _x ≥ x_ 0 + 1 _/j_ , and linear in between.


4

_LECTURE 1. JANUARY 17_

5


by 2. Let _j →∞_ to obtain


Define _gj_ ( _x_ ) by 1 when _x ≤ x_ 0 _−_ 1 _/j_ , 0 when _x ≥ x_ 0, and linear in between.


Let _j →∞_ .


If _x_ 0 is a continuity point, we have shown _Fµn_ ( _x_ 0) _→ Fµ_ ( _x_ 0). 1 = _⇒_ 3: Recall the inverse function of _Fµ_ .

_Fµ_<sup>_−_1(</sup><sup>_y_)</sup> def= sup _{x_ : _Fµ_ ( _x_ ) _< y}_ = inf _{x_ : _Fµ_ ( _x_ ) _≥ y}_ If _U_ is uniform on [0 _,_ 1], then _Fµ_<sup>_−_1</sup> is a RV whose distribution is _µ_ . _Exercise_ . 1 implies _Fµ_<sup>_−_</sup> _n_<sup>1(</sup><sup>_y_)</sup><sup>_→F −_</sup> _µ_<sup>1(</sup><sup>_y_)forall</sup><sup>_y_suchthat</sup><sup>_{x_:</sup><sup>_Fµ_(</sup><sup>_x_)=</sup><sup>_y}_iseitheremptyorasingle</sup> point _x_ . The other case is when _{x_ : _Fµ_ ( _x_ ) = _y}_ is a non-trivial interval. This can only happen for countably many _y_ . _Fµ_<sup>_−_</sup> _n_<sup>1(</sup><sup>_U_)</sup><sup>_→F −_</sup> _µ_<sup>1(</sup><sup>_U_)a.s.(all</sup><sup>_U_outsideacountableset).Thisis3.</sup>

### **1.2 Elementary Examples**

Here are elementary examples where we show 1 by calculation.

**Example 1.2.** If _Xn_ has the uniform distribution on _{_ 1 _,_ 2 _, . . . , n}_ , then _Xn/n −→_ d _U_ , which is uniform on [0 _,_ 1].

**Example 1.3.** _Xθ_ has the Geometric( _θ_ ) distribution. _P_ ( _X > i_ ) = (1 _− θ_ )<sup>_i_</sup> , _i_ = 0 _,_ 1 _,_ 2 _, . . ._ . Then, _θXθ −→_ d _Y_ with the Exponential(1) distribution, _P_ ( _Y > y_ ) = _e−y_ , 0 _≤ y < ∞_ .

**Example 1.4.** _Bn_ is the “birthday RV”, min _{j_ : _ξj_ = _ξi_ for some 1 _≤ i < j}_ for IID _ξi_ uniform on _{_ 1 _,_ 2 _, . . . , n}_ . Then _n_<sup>_−_1</sup><sup>_/_2</sup> _Bn −→_ d _R_ with Rayleigh distribution _P_ ( _R > x_ ) = exp( _−x_ 2 _/_ 2).

#### **1.2.1 Artificial Examples**

**Example 1.5.** For any _X_ : _X_ + 1 _/n −→_ d _X_ as _n →∞_ .

_LECTURE 1. JANUARY 17_

6

Note: _FX_ +1 _/n_ ( _x_ ) = _FX_ ( _x −_ 1 _/n_ ) _→ FX_ ( _x_ ) iff _FX_ ( _x_ ) = _FX_ ( _x−_ ).

**Example 1.6.** If _Xn_ is uniform on the interval [ _x_ 0 _−_ 1 _/n, x_ 0 + 1 _/n_ ], then _Xn −→_ d _x_ 0. Above, we had examples of discrete distributions converging to continuous distributions. This example shows that continuous distributions can converge to discrete distributions.

**Example 1.7.** _Xn_ has density _fn_ ( _x_ ) = (1 _/_ 2)(1 + sin(2 _πnx_ )) on 0 _≤ x ≤_ 1. _Xn −→_ d _U_ , uniform on [0 _,_ 1], with _fU_ ( _x_ ) _≡_ 1. Here, it is _not_ true that _fXn_ ( _x_ ) _→ fU_ ( _x_ ).

### **1.3 Consequences of Weak Convergence**

For a function _g_ : R _→_ R, write _Dg_ = _{x_ : _g_ is not continuous at _x}_ and assume _Dg_ is measurable.

**Corollary 1.8.** _If Xn −→_ d _X, if P_ ( _X ∈ Dg_ ) = 0 _, then g_ ( _Xn_ ) _−→_ d _g_ ( _X_ ) _. Then, if g is bounded, we have Eg_ ( _Xn_ ) _→ Eg_ ( _X_ ) _._

_Proof._ Use 3. There exist _X_<sup>ˆ</sup> _n → X_<sup>ˆ</sup> a.s. (outside some Ω0, _P_ (Ω0) = 0), so _g_ ( _X_<sup>ˆ</sup> _n_ ) _→ g_ ( _X_<sup>ˆ</sup> ) a.s. (outside Ω0 _∪{X ∈ Dg}_ ), which by 3 implies _g_ ( _Xn_ ) _−→_ d _g_ ( _X_ ). By bounded convergence, _Eg_ ( _Xn_ ) _→ Eg_ ( _X_ ).

If _Xn −→_ d _X_ , then 1 _/Xn −→_ d 1 _/X_ , provided _P_ ( _X_ = 0) = 0.

**Corollary 1.9.** _If Xn ≥_ 0 _, if Xn −→_ d _X, then EX ≤_ lim inf _n EXn._

_Proof._ This is Fatou’s Lemma for _X_<sup>ˆ</sup> _n → X_<sup>ˆ</sup> a.s., _X_<sup>ˆ</sup> _n ≥_ 0. Apply 3.

**Theorem 1.10** (Scheffe’s Theorem) **.** _Let θ be a σ-finite measure on_ ( _S, S_ ) _. Suppose that measurable hn, h_ : _S →_ [0 _, ∞_ ] _are such that_ � _S_<sup>_hn_d</sup><sup>_θ_=1</sup><sup>_foralln,_</sup> � _S_<sup>_h_d</sup><sup>_θ_=1</sup><sup>_,andhn_(</sup><sup>_s_)</sup><sup>_→h_(</sup><sup>_s_)</sup><sup>_a.e.(θ).Then_</sup> � _S_<sup>_|hn_(</sup><sup>_s_)</sup><sup>_−h_(</sup><sup>_s_)</sup><sup>_|θ_(d</sup><sup>_s_)</sup><sup>_→_0</sup><sup>_._</sup>

_Proof._


but 0 _≤_ ( _h − h_ 0)<sup>+</sup> _≤ h_ and ( _h − hn_ )<sup>+</sup> _→_ 0 a.e. The Dominated Convergence Theorem implies the result.

## **Lecture 2**

---

[← Contents](02-contents.md) · [Up: contents](index.md) · [January 19 →](04-january-19.md)
