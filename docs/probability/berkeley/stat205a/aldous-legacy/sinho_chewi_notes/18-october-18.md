---
title: October 18
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# October 18

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **16.1 Conditional Expectation**

Let _X_ : (Ω _, F, P_ ) _→_ R, _E|X| < ∞_ , and _G ⊆F_ . _E_ [ _X | G_ ] is the RV _Z_ such that

- (i) _Z_ is _G_ -measurable.

- (ii) _E_ [ _Z_ 1 _G_ ] = _E_ [ _X_ 1 _G_ ] _∀G ∈G_

Conditional expectation is only unique up to a null set. For example, if we write _Z_ = _Z_ 1 + _Z_ 2 (where these are RVs as in the definition of conditional expectation), then the statement is implicitly qualified as _Z_ = _Z_ 1 + _Z_ 2 a.s.

**Lemma 16.1.** _For Z_ = _E_ [ _X | G_ ] _, we have E_ [ _V Z_ ] = _E_ [ _V X_ ] _for all bounded G-measurable RVs V ._

#### **16.1.1 General Properties of Conditional Expectation**

_Setting_ : Take a fixed _G_ .

_Idea_ : The general properties of CE mimic the general properties of ordinary expectation, but with _G_ - measurable RVs playing the role of constants.

Properties of expectation:

- _E_ [ _X_ 1 + _X_ 2] = _E_ [ _X_ 1] + _E_ [ _X_ 2]

- _E_ [ _cX_ ] = _cE_ [ _X_ ]

- _|EX| ≤ E|X|_

- _E_ [ _c_ ] = _c_

Properties of conditional expectation:

- (a) _E_ [ _X_ 1 + _X_ 2 _| G_ ] = _E_ [ _X_ 1 _| G_ ] + _E_ [ _X_ 2 _| G_ ]

- (b) _E_ [ _V X | G_ ] = _V E_ [ _X | G_ ] for all bounded _G_ -measurable _V_

- (c) If 0 _≤ Xn ↑ X_ a.s., then _E_ [ _Xn | G_ ] _↑ E_ [ _X | G_ ] a.s.

- (d) If _X ≥_ 0 a.s., then _E_ [ _X | G_ ] _≥_ 0 a.s.

- (e) _|E_ [ _X | G_ ] _| ≤ E_ [ _|X| | G_ ] a.s.

- (f) _E_ [ _E_ [ _X | G_ ]] = _EX_ (use _G_ = Ωin the definition)

60

_LECTURE 16. OCTOBER 18_

61

- (g) If _X_ is _G_ -measurable, then _E_ [ _X | G_ ] = _X_ by definition. If _G_ is trivial, then _E_ [ _X | G_ ] = _EX_ ( _G_ trivial implies that _E_ [ _X | G_ ] is constant, which equals _EX_ ).

- (h) If _G ⊆H_ , then _E_ [ _X | G_ ] = _E_ [ _E_ [ _X | H_ ] _| G_ ]. This is called the **tower property** .

In fact, the properties above are true provided that _E|V Z| < ∞_ .

_Proofs._ (a) Write _Zi_ = _E_ [ _Xi | G_ ]. We need to show that _Z_ def= _Z_ 1 + _Z_ 2 = _E_ [ _X_ 1 + _X_ 2 _| G_ ]. Is _Z G_ -measurable? Yes, since _Zi_ is _G_ -measurable. For the second part of the definition,

_E_ [ _Z_ 1 _G_ ] = _E_ [ _Z_ 11 _G_ ] + _E_ [ _Z_ 21 _G_ ] = _E_ [ _X_ 11 _G_ ] + _E_ [ _X_ 21 _G_ ] = _E_ [( _X_ 1 + _X_ 2)1 _G_ ] _∀G ∈G_

- (b) Define _Z_ = _V E_ [ _X | G_ ]. We need to show _Z_ = _E_ [ _V X | G_ ]. Is _Z G_ -measurable? Yes, since _V_ and _E_ [ _X | G_ ] are _G_ -measurable.

_E_ [ _E_ [ _X | G_ ] _V_ 1 _G_ ] = _E_ [ _XV_ 1 _G_ ] _∀G ∈G_

The equality is true by 16.1 applied to _V_ 1 _G_ , since _V_ 1 _G_ is _G_ -measurable.

(c) Easy exercise.

- (d) Easy exercise.

- (e) Easy exercise.

- (h) Write _Z_ = _E_ [ _X | G_ ]. We need to check:


by the definition of _Z_ . The second equality is because of the definition of _E_ [ _X | H_ ] and _G ⊆H_ , so _G ∈G_ implies that _G ∈H_ .

#### **16.1.2 Orthogonality**

_X �→ E_ [ _X | G_ ] is an orthogonal projection in Hilbert space. Recall from 16.1 that


for _V G_ -measurable and _EV_<sup>2</sup> _< ∞_ . (By the Cauchy-Schwarz Inequality, _E|V X| ≤_ ~~�~~ ( _EX_<sup>2</sup> )( _EV_<sup>2</sup> ) _< ∞_ .)

(i) _X − E_ [ _X | G_ ] and _V_ are orthogonal for all _G_ -measurable _V_ .

#### **16.1.3 Conditional Variance**

Recall that var( _X_ ) = _E_ [ _X − E_ [ _X_ ]]<sup>2</sup> .

**Definition 16.2.** Define **conditional variance** by


- (j) If _Y_ is _G_ -measurable, _EY_<sup>2</sup> _< ∞_ , then _E_ [( _X − Y_ )<sup>2</sup> _| G_ ] = var( _X | G_ ) + ( _E_ [ _X | G_ ] _− Y_ )<sup>2</sup> .

_Proof._


_LECTURE 16. OCTOBER 18_

62

Expand the square. We have _E_ [ _ab|G_ ] = _bE_ [ _a|G_ ] = 0, so the cross-terms vanish. Since _b_ is _G_ -measurable, _E_ [ _a_<sup>2</sup> + _b_<sup>2</sup> _| G_ ] = var( _X | G_ ) + _b_<sup>2</sup> .

The constant _c_ that minimizes _E_ ( _X − c_ )<sup>2</sup> is _c_ = _EX_ .

(k) The _G_ -measurable RV that minimizes _E_ ( _X − Y_ )<sup>2</sup> is _Y_ = _E_ [ _X | G_ ].

Take the expectation of (j). Then


- (l) var( _X_ ) = _E_ var( _X | G_ ) + var _E_ [ _X | G_ ]

_Proof._ Replacing _X_ by _X − c_ changes no terms, so we can assume _EX_ = 0.


since _E_ [ _ab | G_ ] = 0 and _E_ [ _E_ [ _X | G_ ]] = _EX_ = 0.

#### **16.1.4 Independence**

What is the connection with independence?

(m) _X_ is independent of _G_ iff


Here, _X_ can be _S_ -valued.

_Proof._ Suppose _X_ is independent of _G_ . We need to show:


This holds by independence.

Suppose that (16.1) holds. Take _h_ = 1 _B_ for _B ⊆ S_ . (16.1) implies (by the same argument as above) _P_ ( _X ∈ B, G_ ) = _E_ [ _h_ ( _X_ )1 _G_ ] = _E_ [ _h_ ( _X_ )] _E_ [1 _G_ ] = _P_ ( _X ∈ B_ ) _P_ ( _G_ )

for all _B_ and _G_ , which implies that _X_ and _G_ are independent.

Recall that _X_ and _Y_ are independent if and only if _E_ [ _h_ 1( _X_ ) _h_ 2( _Y_ )] = ( _Eh_ 1( _X_ ))( _Eh_ 2( _Y_ )) _∀h_ 1 _, h_ 2.

### **16.2 Background to Conditional Independence**

There are three general contexts in which this idea arises.

_LECTURE 16. OCTOBER 18_

63

1. Bayes

   - (a) Take a random Θ, which takes values in _{_ PMs on R<sup>1</sup> _}_ = _P_ (R).

   - (b) Conditional on Θ = _θ ∈P_ (R), take _X_ 1 _, X_ 2 _, X_ 3 _, . . ._ which are IID _θ_ .

The ( _Xi_ ) are conditionally independent given Θ.

2. The simple Markov property for ( _Xn, n ≥_ 0)

      - _P_ ( _Xn_ +1 = _xn_ +1 _| Xn_ = _xn, Xn−_ 1 = _xn−_ 1 _, . . . , X_ 0 = _x_ 0) = _P_ ( _Xn_ +1 = _xn_ +1 _| Xn_ = _xn_ )

   - ( _Xn_ +1) and ( _Xn−_ 1 _, Xn−_ 2 _, . . . , X_ 0) are conditionally independent given _Xn_ .

3. Given ( _W_ **x** _,_ **x** = ( _x_ 1 _, x_ 2) _∈_ Z<sup>2</sup> ), let _N_ ( **x** ) be the neighbors of **x** . The idea is that _W_ **x** depends only on _{W_ **y** _,_ **y** _∈ N_ ( **x** ) _}_ and not on the other _W_ s. We formalize the idea as _W_ **x** and ( _W_ **z** _,_ **z** _∈/ N_ ( **x** ) _∪{_ **x** _}_ ) are conditionally independent given _{W_ **y** _,_ **y** _∈ N_ ( **x** ) _}_ .

## **Lecture 17**

---

[← October 13](17-october-13.md) · [Up: contents](index.md) · [October 20 →](19-october-20.md)
