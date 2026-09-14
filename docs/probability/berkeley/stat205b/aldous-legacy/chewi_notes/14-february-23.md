---
title: February 23
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# February 23

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **12.1 Classification of States**


It is aways the case that


Define the relation _x ∼ y_ by _x_ = _y_ or ( _ρx,y >_ 0 and _ρy,x >_ 0). The equivalence class _C_ is a “SCC”. Define _C_ is open if _∃x ∈ C, y ∈/ C, ρx,y >_ 0, and _C_ is closed if not.

_Fact_ . Given a SCC “ _C_ ”, either _x_ is transient for all _x ∈ C_ or _x_ is recurrent for all _x ∈ C_ . Call _C_ transient or recurrent respectively.

**Theorem** . If _x_ is recurrent and _ρx,y >_ 0, then _y_ is recurrent and _ρy,x_ = 1.


_Proof._ (a) follows from 11.7. If _C_ is open, then _∃x ∈ C, y ∈/ C ρx,y >_ 0. If _x_ is recurrent, by the Theorem, _ρy,x >_ 0 implies _x ∼ y_ , which implies _y ∈ C_ , which is a contradiction.

46

_LECTURE 12. FEBRUARY 23_

47

(b): Fix _x ∈ C_ . For a chain started at _x_ , since _C_ is closed,


If _C_ is finite, then E _xN_ ( _y_ ) = _∞_ for some _y ∈ C_ , so _y_ is recurrent, so _C_ is recurrent.

(c): Fix _x_ . Consider a transient _y_ . Then, E _xN_ ( _y_ ) _< ∞_ , so


_Note_ : At _TR_ , we are at state _XTR_ , which is some closed _C_ , which implies that _Xn ∈ C ∀n ≥ TR_ .

**Definition 12.2.** A chain is **irreducible** if _ρx,y >_ 0 _∀x, y_ .

12.1 implies: if _S_ is finite and irreducible, then the chain is recurrent. If _S_ is infinite and irreducible, then the chain may be recurrent or transient.

### **12.2 Birth-and-Death Chains**

Let _S_ = Z<sup>+</sup> = _{_ 0 _,_ 1 _,_ 2 _, . . . }_ , _p_ ( _i, i_ + 1) = _pi >_ 0, _p_ ( _i, i −_ 1) = _qi >_ 0 (for _i ≥_ 1), _p_ ( _i, i_ ) = _ri_ = 1 _− pi − q_ 1 _≥_ 0. Set _q_ 0 = 0.

Write _τj_ = min _{n ≥_ 0 : _Xn_ = _j}_ .

_Analysis_ . Fix _m ≥_ 1. Study _f_ ( _i_ ) = P _i_ ( _τm < τ_ 0), 0 _≤ i ≤ m_ , _f_ (0) = 0, _f_ ( _m_ ) = 1. Condition on the first step: for 1 _≤ i ≤ m −_ 1, _f_ ( _i_ ) = _pif_ ( _i_ + 1) + _qif_ ( _i −_ 1) + _rif_ ( _i_ ). Solve: _pi_ ( _f_ ( _i_ + 1) _− f_ ( _i_ )) = _qi_ ( _f_ ( _i_ ) _− f_ ( _i −_ 1)), or


We know 1 = _f_ ( _m_ ) = _f_ (1) _φ_ ( _m_ ), so _f_ (1) = 1 _/φ_ ( _m_ ). Hence,


Can we say


_LECTURE 12. FEBRUARY 23_

48

Make the chain absorbing at 0 and _m_ . The states _{_ 1 _, . . . , m −_ 1 _}_ are transient, so P _i_ ( _τ_ 0 or _τm < ∞_ ) = 1. Is the chain recurrent or transient? recurrent _⇐⇒ ρ_ 0 _,_ 0 = 1 _⇐⇒ ρ_ 1 _,_ 0 = 1.


Thus,


For a simple RW, _pi_ = _p >_ 0, _qi_ = _q_ = 1 _− p_ . Then, the chain is recurrent if _p ≥_ 1 _/_ 2, transient if _p >_ 1 _/_ 2. _More Delicate Case_ . Fix _C_ , take


Then,


Then, if _C >_ 1 _/_ 4, the chain is transient, and if _C <_ 1 _/_ 4, the chain is recurrent.

### **12.3 Invariant Measures**

_Setting_ . We have an irreducible **P** on a countable _S_ .


_Note_ : We may have _µ_ ( _S_ ) = _∞_ . Ignore the trivial case _µ ≡_ 0.

If _µ_ is invariant, then _cµ_ is invariant, 0 _< c < ∞_ .

If invariant _µ_ has _µ_ ( _S_ ) = 1, call it **stationary** .

If invariant _µ_ has 0 _< µ_ ( _S_ ) _< ∞_ , then


is stationary.

_LECTURE 12. FEBRUARY 23_

49


If ( _Xn, n ≥_ 0) is a MC and dist( _X_ 0) is a stationary distribution, then the process ( _Xn, n ≥_ 0) is stationary.

_Aside_ . If _µ_ is invariant, _µ_ ( _S_ ) = _∞_ , take (at time 0) independent Poisson( _µ_ ( _i_ )) particles at _i_ and run each particle as an independent MC. This particle process is stationary.

_µn_ = dist( _Xn_ ) always evolves as **_µ_** _n_ = **_µ_** _n−_ 1 **P** .

_Two Special Settings_ . _µ_ ( _S_ ) _≤∞_ .

1. _µ ≡_ 1 is invariant _⇐⇒_<sup>�</sup> _i_<sup>_pi,j_= 1</sup><sup>_∀j⇐⇒_</sup><sup>**doublystochasticmatrix**.</sup>

2. If _µ_ ( _x_ ) _p_ ( _x, y_ ) = _µ_ ( _y_ ) _p_ ( _y, x_ ) _∀x, y_ , then _µ_ is invariant ( **reversible** case).


**Example 12.5** (Simple RW on Z = _{. . . , −_ 1 _,_ 0 _,_ 1 _, . . . }_ ) **.**


What is an invariant _µ_ ? **P** _is_ doubly stochastic: _µ_ ( _i_ ) _≡_ 1 is invariant. _µ_ ( _x_ ) = ( _p/q_ )<sup>_x_</sup> is a reversible invariant measure. For _p̸_ = 1 _/_ 2, the chain is transient and has 2 different _σ_ -finite invariant measures.

**Example 12.6** (Birth-Death Chain on Z<sup>+</sup> = _{_ 0 _,_ 1 _,_ 2 _, . . . }_ ) **.**


This has the reversible invariant measure


Check:


This is the _unique_ invariant measure (up to scaling). Looking at **_µ_** = **_µ_ P** at 0:

_µ_ (0) = _µ_ (0) _p_ (0 _,_ 0) + _µ_ (1) _p_ (1 _,_ 0) _µ_ (1) = _µ_ (0) _p_ (0 _,_ 1) + _µ_ (1) _p_ (1 _,_ 1) + _µ_ (2) _p_ (2 _,_ 1) _._

_LECTURE 12. FEBRUARY 23_

50

The first equation determines _µ_ (1) in terms of _µ_ (0), and the second equation determines _µ_ (2) in terms of _µ_ (0), and so forth.

## **Lecture 13**

---

[← February 21](13-february-21.md) · [Up: contents](index.md) · [February 28 →](15-february-28.md)
