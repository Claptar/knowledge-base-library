---
title: March 21
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# March 21

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **19.1 Another MC Example**

_Setting_ . _Xn_ = _f_ ( _Xn−_ 1 _, ξn_ ) for prescribed _f_ and IID ( _ξi_ ).

Suppose we have a metric space ( _S, d_ ). For _f_ : _S → S_ ,


For a random function _f_ ( _x, ξ_ ), consider E log _∥f_ ( _·, ξ_ ) _∥_ Lip _≡ κ_ , say.

**Theorem 19.1** (Diaconis-Freedman Paper) **.** _For a MC of form Xn_ = _f_ ( _Xn−_ 1 _, ξn_ ) _, if κ <_ 0 _(and side conditions), then the “coupling from the past” method shows there exists a unique stationary distribution π and_ dist( _Xn_ ) _→ π weakly._

**Example 19.2.** _S_ = (0 _,_ 1). Given _X_ 0 = _x_ , flip a fair coin _{L, R}_ . If _L_ , take _X_ 1 to be Uniform[0 _, x_ ], and if _R_ , take _X_ 1 to be Uniform[ _x,_ 1].

Define


Take _ξ_ = ( _U, I_ ), _U_ is Uniform[0 _,_ 1], _I_ is Uniform _{L, R}_ , independent. This represents the chain as _Xn_ = _f_ ( _Xn−_ 1 _, ξn_ ).

_∥f_ ( _·, u, L_ ) _∥_ Lip = _u_ = _∥f_ ( _·, u, R_ ) _∥_ Lip = _⇒ κ_ = E log _U <_ 0 _._ 19.1 implies that a stationary _π_ exists. ( _Exercise_ ). Find _π_ explicitly.

### **19.2 Ergodic Theory**

#### **19.2.1 “Probability” Set-Up**

( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ) defined on (Ω _, F,_ P), R-valued, are **stationary** if


74

75

_LECTURE 19. MARCH 21_

This is equivalent to ( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ) = (d _X_ 1 _, X_ 2 _, X_ 3 _, . . ._ ) and equivalent to


Given stationary ( _Xn,_ 0 _≤ n < ∞_ ), there exists (Kolmogorov Extension Theorem) a two-sided stationary sequence ( _X_<sup>ˆ</sup> _n, −∞ < n < ∞_ ), such that ( _X_<sup>ˆ</sup> _n, n ≥_ 0) = (d _Xn, n ≥_ 0).

**Example 19.3.** IID random variables are stationary.

**Example 19.4.** Exchangeable random variables are stationary.

**Example 19.5.** A stationary Markov chain is stationary.

**Example 19.6** (“Moving Average”) **.** Let ( _ξi_ ) be IID. Fix _L ≥_ 2. Let


Then, ( _Ai, i ≥_ 0) is stationary.

**Theorem 19.7** (Easy) **.** _If_ ( _Xn,_ 0 _≤ n < ∞_ ) _is stationary, if g_ : R<sup>_∞_</sup> _→_ R _is measurable, then for Yn_ = _g_ ( _Xn, Xn_ +1 _, Xn_ +2 _, . . ._ ) _,_ ( _Yn,_ 0 _≤ n < ∞_ ) _is stationary._

This starts with very random ingredients.

#### **19.2.2 Ergodic Theory Set-Up**

A probability space ( _S, S, µ_ ) is “concrete”. For a measurable _φ_ : _S → S_ , the push-forward measure is _µ_ ˆ( _A_ ) = _µ_ ( _φ_<sup>_−_1</sup> ( _A_ )). Suppose _µ_ is invariant under _φ_ : _µ_ ( _A_ ) = _µ_ ( _φ_<sup>_−_1</sup> ( _A_ )) _∀A_ . [Given _µ_ , say _φ_ is a **measurepreserving transformation** .]

Now, for any measurable _f_ : _S →_ R, we can define


We can define RVs ( _Xn,_ 0 _≤ n < ∞_ ) on a probability space ( _S, S, µ_ ).

**Lemma 19.8.** _Given µ, φ as above, for any f , the sequence_ ( _Xn, n ≥_ 0) _is stationary._

_Proof._ To check (19.1), we need to check


_LECTURE 19. MARCH 21_

76


Here, we start with deterministic objects.


**Example 19.10** (Baker’s Transformation) **.** _S_ = [0 _,_ 1]<sup>2</sup> and _µ_ = Leb<sup>2</sup> .


Given stationary ( _X_<sup>ˆ</sup> _n, n ≥_ 0) defined on (Ω _, F,_ P), there is a “canonical” way to set it up in the ergodic theory set-up.

Define _S_ = R<sup>_∞_</sup> , _µ_ = dist( _X_<sup>ˆ</sup> _n, n ≥_ 0) on _S_ . Define _φ_ : _S → S_ by _φ_ ( _x_ 0 _, x_ 1 _, x_ 2 _, . . ._ ) = ( _x_ 1 _, x_ 2 _, . . ._ ). The function _f_ : _S →_ R is _f_ ( _x_ 0 _, x_ 1 _, . . ._ ) = _x_ 0. Then, define _Xn_ as in (19.5) gives _Xn_ ( _x_ 0 _, x_ 1 _, x_ 2 _, . . ._ ) = _xn_ and ( _Xn, n ≥_ 0) = ( ˆd _Xn, n ≥_ 0). The former are RVs on (R _∞, µ_ ) and the latter are RVs on (Ω _, F,_ P).

#### **19.2.3 Invariant Events**

**Definition 19.11.** In the ergodic theory set-up, an event _A_ is **invariant** if _φ_<sup>_−_1</sup> ( _A_ ) = _A_ a.s.

_Easy Fact_ : If _A_ = _φ_<sup>_−_1</sup> ( _A_ ) a.s., then _A_<sup>_∗_</sup> =<sup>�</sup><sup>_∞_</sup> _n_ =1 � _i>n_<sup>_φ−i_(</sup><sup>_A_) satisfies</sup><sup>_A∗_=</sup><sup>_A_a.s. and</sup><sup>_φ−_1(</sup><sup>_A∗_) =</sup><sup>_A∗_always.</sup> The collection of all invariant events forms the **invariant** _σ_ **-field** _I_ .

**Definition 19.12.** A measure-preserving transformation _φ_ on ( _S, S, µ_ ) is **ergodic** if _I_ is trivial. That is, _µ_ ( _A_ ) = 0 or 1 for each invariant _A_ .

Given a stationary ( _X_<sup>ˆ</sup> _n, n ≥_ 0), go to the canonical set-up to use these definitions. The notion of invariant _A ⊆_ R<sup>_∞_</sup> says that


The process ( _X_<sup>ˆ</sup> _n_ ) is ergodic _⇐⇒_ P(( _X_ 0 _, X_ 1 _, . . ._ ) _∈ A_ ) = 0 or 1 for each invariant _A_ .

_a.s._ **Lemma 19.13.** _For stationary_ ( _Xn, n ≥_ 0) _in the canonical set-up, I ⊆ τ_ = _tail σ-field of_ ( _Xn_ ) _._

_Proof._


(where _φ_ is the shift map ( _x_ 0 _, x_ 1 _, . . ._ ) _�→_ ( _x_ 1 _, x_ 2 _, . . ._ ))


_LECTURE 19. MARCH 21_

77

Therefore,


For example, consider alternating coin flips, _HTHTHTH . . ._ or _THTHTHT . . ._ . Then, _X_ 0 _∈ τ_ , but we have _X_ 0 _∈I/_ .

_Recall_ : **Theorem** . If ( _Xn, n ≥_ 0) is stationary, if _g_ : R<sup>_∞_</sup> _→_ R is measurable, then ( _Yn, n ≥_ 0) is stationary for _Yn_ = _g_ ( _Xn, Xn_ +1 _, . . ._ ) _and_ if ( _Xn_ ) is ergodic, then ( _Yn_ ) is ergodic.

If _B_ is invariant for ( _Yn_ ),


and this reduces to (19.9) for a certain _A_ depending on _B_ .

## **Lecture 20**

---

[← March 16](20-march-16.md) · [Up: contents](index.md) · [March 23 →](22-march-23.md)
