---
title: Terminology for Normed Spaces
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Terminology for Normed Spaces

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Definition: A (real) _linear space D_ is a set with addition and scalar multiplication defined such that if _d_ 1 _, d_ 2 _, d_ 3 _∈ D_ and _c_ 1 _, c_ 2 _∈R_ :

_c_ 1 _d_ 1 + _c_ 2 _d_ 2 _∈ D_ (closed under linear combination).

_d_ 1 + _d_ 2 = _d_ 2 + _d_ 1 (commutative). _d_ 1 + ( _d_ 2 + _d_ 3) = ( _d_ 1 + _d_ 2) + _d_ 3 (associative addition).

10

There exists 0 _∈ D_ such that _d_ 1 + 0 = _d_ 1 and _d_ 1 + ( _−d_ 1) = 0. 1 _d_ 1 = _d_ 1. _c_ 1( _c_ 2 _d_ 1) = ( _c_ 1 _c_ 2) _d_ 1 (associative multiplication). _c_ 1( _d_ 1 + _d_ 2) = _c_ 1 _d_ 1 + _c_ 1 _d_ 2 and ( _c_ 1 + _c_ 2) _d_ 1 = _c_ 1 _d_ 1 + _c_ 2 _c_ 1 (distributive).

Definition: A (real) _normed space_ (also called a normed linear space) ( _D, ∥· ∥_ ) is a real linear space _D_ and a function _∥· ∥_ : _D →R_ such that for _d_ 1 _, d_ 2 _∈ D_ and _c ∈R_ :

_∥d_ 1 _∥≥_ 0 and _∥d_ 1 _∥_ = 0 if and only if _d_ 1 = 0. _∥cd_ 1 _∥_ = _| c | ∥d_ 1 _∥_ . _∥d_ 1 + _d_ 2 _∥≤∥d_ 1 _∥_ + _∥d_ 2 _∥_ (triangle inequality).

Basic example: _R_<sup>_k_</sup> is normed space. For _p ≥_ 1, _∥_ ( _x_ 1 _, ..., xn_ ) _∥_ = (<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_|xi|p_)1</sup><sup>_/p_defines</sup> a norm. _p_ = 2 corresponds to the Euclidean norm.

More complicated examples: The space of cadlag functions ( _D_ ( _a, b_ ) _, ∥· ∥_ ), which is the space of all functions defined on ( _a, b_ ) that are right continuous with left limits, such that _∥d∥_ = sup _a≤t≤b | d_ ( _t_ ) _|_ . Also, ( _l_<sup>_∞_</sup> ( _F_ ) _, ∥· ∥F_ ), defined previously, is a normed space. Sets of random variables can also live in normed spaces. _L_<sup>_P_</sup> 0<sup>_≡{X_:</sup><sup>_EPX_=</sup> 0 _, EP |X|_<sup>_p_</sup> _< ∞}_ is a normed space for _p ≥_ 1 with _∥X∥_ = ( _E|X|_<sup>_p_</sup> )<sup>1</sup><sup>_/p_</sup> .

Definition: If _d_ 1 _, d_ 2 _, ..._ is a sequence in a normed space ( _D, ∥· ∥_ ), the sequence is said to converge to _d ∈ D_ if for all _ϵ >_ 0 there exists a positive integer _N_ such that _n ≥ N_ implies _∥dn − d∥≤ ϵ_ .

Definition: If _d_ 1 _, d_ 2 _, ..._ is a sequence in a normed space ( _D, ∥· ∥_ ), we say the sequence is _Cauchy_ if for all _ϵ >_ 0 there exists a positive integer _N_ such that _n ≥ N_ implies _supm,n≥N ∥dm − dn∥≤ ϵ_ .

Definition: We say that a normed space ( _D, ∥· ∥_ ) is a _Banach space_ if every Cauchy sequence in ( _D, ∥· ∥_ ) converges to some _d ∈ D_ .

Definition: If _f_ : ( _D, ∥·∥_ ) _→_ ( _E, ∥·∥_ ) is a mapping from one normed space to another, we say that _f_ is _continuous_ at _d ∈ D_ if for every sequence _d_ 1 _, d_ 2 _, ..._ in _D_ converging to _d_ we have that _f_ ( _x_ 1) _, f_ ( _x_ 2) _, ..._ converges to _f_ ( _d_ ) in ( _E, ∥· ∥_ ). If _f_ is continuous at all _d ∈ D_ , we say that _f_ is a continuous function.

Definition: If ( _D, ∥· ∥_ ) is a normed space, then for any _ϵ >_ 0 and _d ∈ D_ , the _open ball_ of radius _ϵ_ at _d_ is defined by _Bϵ_ ( _d_ ) = _{d_<sup>_′_</sup> _∈ D_ : _∥d_<sup>_′_</sup> _− d∥ < ϵ}_ .

Definition: If _D_ 0 _⊂ D_ for ( _D, ∥· ∥_ ) a normed space, we say that _D_ 0 is an _open set_ if for every _d_ 0 _∈ D_ 0 there exists _ϵ_ ( _d_ 0) such that _Bϵ_ ( _d_ 0)( _d_ 0) _⊂ D_ 0. A subset of _D_ is said to be _closed_ if its complement is open.

Definition: If _D_ 0 _⊂ D_ for ( _D, ∥· ∥_ ) a normed space, we say that _D_ 0 is _bounded_ if for

11

each _d_ 0 _∈ D_ 0 there exists _r_ ( _d_ 0) _>_ 0 such that _D_ 0 _⊂ Br_ ( _d_ 0)( _d_ 0).

Definition: If _D_ 0 _⊂ D_ for ( _D, ∥· ∥_ ) a normed space, a collection of sets is a _cover_ if _D_ 0 is a subset of the union of sets in the collection. If each set in the collection is open, the collection is said to be an _open cover_ . If the union of sets in a subcollection of the collection still contains _D_ 0, the subcollection is said to be a _subcover_ of _D_ 0. If every open cover of _D_ 0 contains a finite subcover, _D_ 0 is said to be _compact_ . A set _D_ 0 is compact if and only if every sequence _d_ 1 _, d_ 2 _, ... ∈ D_ 0 contains a subsequence converging to an element of _D_ 0.

Definition: If ( _D, ∥· ∥_ ) is a normed space, the normed space is said to be _separable_ if there exists a countable _dense_ subset _{d_ 1 _, d_ 2 _, ...}_ of _D_ such that for any _d ∈ D_ and any _ϵ >_ 0 there exists _dn_ in the countable subset such that _∥d − dn∥≤ ϵ_ . That is, the normed space can be approximated arbitrarily well by a countable set.

---

[← The Influence Curve and the Functional Delta Method](17-the-influence-curve-and-the-functional-delta-method.md) · [Up: contents](index.md) · [Note on Integration Theory →](19-note-on-integration-theory.md)
