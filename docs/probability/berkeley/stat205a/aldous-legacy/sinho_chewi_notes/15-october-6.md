---
title: October 6
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# October 6

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **13.1 Conditional Distributions**

Consider two measurable spaces ( _S_ 1 _, S_ 1) and ( _S_ 2 _, S_ 2). Then


Consider two RVs, _X_ : (Ω _, F, P_ ) _→_ ( _S_ 1 _, S_ 1) and _Y_ : (Ω _, F, P_ ) _→_ ( _S_ 2 _, S_ 2). ( _X, Y_ ) is one RV with values in _S_ 1 _× S_ 2. ( _X, Y_ ) has a distribution _µ_ , a PM on _S_ 1 _× S_ 2. _X_ has a distribution _µ_ 1, a PM on _S_ 1. What is the conditional distribution of _Y_ given _X_ ?

Suppose that _S_ 1 = _S_ 2 = _S_ is countable. Then _P_ ( _Y_ = _y | X_ = _x_ ) = _f_ ( _y | x_ ) has the following properties:


- <sup>�</sup> _y_<sup>_f_(</sup><sup>_y | x_) = 1</sup><sup>_∀x_</sup>

These properties define a stochastic matrix. The joint distribution is


(b) for fixed _B ∈S_ 2, _s_ 1 _�→ Q_ ( _s_ 1 _, B_ ) is a measurable function _S_ 1 _→_ R.

For _S_ 1 = _S_ 2 = _S_ countable, we have a 1-1 correspondence between _Q_ and _f_ ( _y | x_ ) given by


_Warning_ . If _h_ : _S_ 1 _× S_ 2 _→_ R, consider:

1. _h_ is measurable.

2. _∀s_ 1, _s_ 2 _�→ h_ ( _s_ 1 _, s_ 2) is measurable _S_ 2 _→_ R and _∀s_ 2, _s_ 1 _�→ h_ ( _s_ 1 _, s_ 2) is measurable _S_ 1 _→_ R.

_Fact_ . 1 implies 2, but 2 does not imply 1.

49

_LECTURE 13. OCTOBER 6_

50

**Example 13.2.** Let _S_ 1 = _S_ 2 = [0 _,_ 1], with some non-measurable _A ⊂_ [0 _,_ 1], and consider


_Comment_ . We interpret _P_ ( _Y ∈ B | X_ = _s_ 1) = _Q_ ( _s_ 1 _, B_ ).

**Proposition 13.3.** _Given a PM µ on S_ 1 _× S_ 2 _, a PM µ_ 1 _on S_ 1 _, and a kernel Q from S_ 1 _to S_ 2 _, the following are equivalent:_


_Here, Ds_ 1 = _{s_ 2 : ( _s_ 1 _, s_ 2) _∈ D}._


_where_ **s** = ( _s_ 1 _, s_ 2) _, provided that h is measurable with h ≥_ 0 _or h is µ-integrable._

First, a technical lemma.

**Lemma 13.4.** _For each D ∈S_ 1 _⊗S_ 2 _, (i) Ds_ 1 _∈S_ 2 _∀s_ 1 _∈S_ 2 _(ii) The map s_ 1 _�→ Q_ ( _s_ 1 _, Ds_ 1) _is measurable._

_Proof._ Let _D_ be the collection of all _D_ satisfying (i) and (ii). The rectangles _A × B_ are in _D_ . Apply the _π_ - _λ_ Theorem. If _D_<sup>_n_</sup> _↑ D_ , then _Ds_<sup>_n_</sup> 1<sup>_↑Ds_</sup> 1<sup>,whichimpliesthat</sup><sup>_Q_(</sup><sup>_s_1</sup><sup>_, D_</sup> _s_<sup>_n_</sup> 1<sup>)</sup><sup>_↑Q_(</sup><sup>_s_1</sup><sup>_, Ds_</sup> 1<sup>).Wecheck</sup> the _λ_ -class property for _D_ .

_Outline Proof._ (BR1) _⇒_ (BR2): Consider _D_<sup>_′_</sup> , the collection of _D_ where (BR2) holds. Use the _π_ - _λ_ Theorem.

(BR2) _⇒_ (BR3): Use a monotone class argument.

**Theorem 13.5** (Easy Theorem) **.** _Given a PM µ_ 1 _on S_ 1 _, given a kernel Q from S_ 1 _to S_ 2 _, the definition_


_defines a PM µ on S_ 1 _× S_ 2 _._

_Proof._ The proof follows from the definitions and the properties of integrals.

**Theorem 13.6** (Hard Theorem) **.** _Given a PM µ on S_ 1 _× S_ 2 _, define the marginal PM µ_ 1 _on S_ 1 _by µ_ 1( _A_ ) = _µ_ ( _A × S_ 2) _. If S_ 2 _is a Borel space, then there exists a kernel Q from S_ 1 _to S_ 2 _such that_ (BR1)

_LECTURE 13. OCTOBER 6_

51

_to_ (BR3) _hold._

_Proof._ Fix _B ∈S_ 2. Consider _ν_ ( _A_ ) def= _µ_ ( _A × B_ ), _A ∈S_ 1. _ν_ is a (sub-probability) measure on _S_ 1. Also,

_ν_ ( _A_ ) _≤ µ_ ( _A × S_ 2) = _µ_ 1( _A_ )

This implies that _ν ≪ µ_ 1. Consider the Radon-Nikodym density


which has the properties: _s_ 1 _�→ Q_ ( _s_ 1 _, B_ ) is measurable (requirement for a kernel), and


which is (BR1). Repeat for every _B ∈S_ 2 to set _Q_ ( _s_ 1 _, B_ ) defined. We need the second property of a “kernel”, which is: _∀s_ 1, the map _B �→ Q_ ( _s_ 1 _, B_ ) is a PM on _S_ 2.

_Issue_ . If _h_ 1 = _h_ 2 a.e. (with respect to _µ_ 1), then


Take the case where _S_ 2 = R. For each rational _r ∈_ R, do the construction for _B_ = ( _−∞, r_ ]. Write _F_ ( _s_ 1 _, r_ ) = _Q_ ( _s_ 1 _,_ ( _−∞, r_ ]). This has the properties: _s_ 1 _�→ F_ ( _s_ 1 _, r_ ) is measurable, and


Given _r_ 1 _< r_ 2,


which implies that _F_ ( _s_ 1 _, r_ 2) _≥ F_ ( _s_ 1 _, r_ 1) a.e. in _S_ 1.

Redefine _F_ ( _s_ 1 _, r_ ) = Φ( _r_ ) _∀r_ for _s_ 1 in the null set. Repeat for all pairs ( _r_ 1 _, r_ 2). We now have a version of ( _F_ ( _s_ 1 _, r_ )) such that _r �→ F_ ( _s_ 1 _, r_ ) is monotone on rational _r_ , for all _s_ 1 (Property A).

_Easy_ . Modify _F_ again to make


(Property B). Consider _rn ↓ r_ (for all rationals). Then _µ_ ( _A ×_ ( _r, rn_ ]) _→_ 0 _∀A_ , so _F_ ( _s_ 1 _, rn_ ) _↓ F_ ( _s_ 1 _, r_ ) a.e. Modify _F_ again so that (Property C) _rn ↓ r_ (for all rationals) implies that _F_ ( _s_ 1 _, rn_ ) _↓ F_ ( _s_ 1 _, r_ ) _∀s_ 1.

_Deterministic Fact_ . If _r �→ F_ ( _r_ ), where _r_ is rational, has the properties A, B, and C, then


_LECTURE 13. OCTOBER 6_

52

is a distribution function, with _F_<sup>ˆ</sup> ( _r_ ) = _F_ ( _r_ ).

Use the fact to define _F_<sup>ˆ</sup> ( _s_ 1 _, x_ ) = lim _r↓x F_ ( _s_ 1 _, r_ ) _∀x ∈_ R. Here, _S_ 1 _�→ F_<sup>ˆ</sup> ( _s_ 1 _, x_ ) is measurable, and _x �→ F_<sup>ˆ</sup> ( _s_ 1 _, x_ ) is a distribution function. Define _Q_ by _Q_ ( _s_ 1 _, ·_ ) is the PM with distribution function _F_ ( _s_ 1 _, x_ ).

## **Lecture 14**

---

[← October 4](14-october-4.md) · [Up: contents](index.md) · [October 11 →](16-october-11.md)
