---
title: October 20
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# October 20

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **17.1 Two Final “Conditioning” Topics**

Recall Jensen’s inequality: _Eφ_ ( _X_ ) _≥ φ_ ( _EX_ ) if _φ_ is convex, if _E|X| < ∞_ and _E|φ_ ( _X_ ) _| < ∞_ .

(n) Conditional Jensen’s inequality: _E_ [ _φ_ ( _X_ ) _| G_ ] _≥ φ_ ( _E_ [ _X | G_ ]) a.s.

#### **17.1.1 Conditional Independence**

Recall that in MT, independence is a property of _G_ 1 and _G_ 2. The RVs _X_ 1 and _X_ 2 are independent if _σ_ ( _X_ 1) and _σ_ ( _X_ 2) are independent. Recall that for _X_ : (Ω _, F, P_ ) _→_ ( _S, S_ ), _σ_ ( _X_ ) _⊆F_ . Independence is also equivalent to _E_ [ _h_ 1( _X_ 1) _h_ 2( _X_ 2)] = ( _Eh_ 1( _X_ 1))( _Eh_ 2( _X_ 2)) for all _hi_ : _Si →_ R which are bounded and measurable. This is also equivalent to _E_ [ _h_ 1( _X_ 1) _| X_ 2] = _Eh_ 1( _X_ 1) a.s. for all _h_ 1.

_Undergraduate Setting_ . Given a discrete RV _V_ , define _P_ ( _X_ 1 = _x_ 1 _| V_ = _v_ ) and define _P_ ( _X_ 2 = _x_ 2 _| V_ = _v_ ). Then, we can construct ( _X_ 1 _, X_ 2 _, V_ ) such that


We can replace _X_ 1 with a _σ_ -field _H_ 1, and _h_ 1( _X_ 1) with a bounded _H_ 1-measurable RV.

_Homework (Later)_ . This is equivalent to _E_ [ _h_ 1( _X_ 1) _| G, X_ 2] = _E_ [ _h_ 1( _X_ 1) _| G_ ] a.s. for all _h_ 1. Once you know _G_ , knowing also _X_ 2 gives no _extra_ info about _X_ 1.

#### **17.1.2 Conditional Probability & Conditional Expectation**

_Undergraduate_ . We define a conditional _P_ by


and a conditional _E_ by


and the two concepts are related.

64

_LECTURE 17. OCTOBER 20_

65

From ( _X, Y_ ) : (Ω _, F, P_ ) _→ S_ 1 _×S_ 2, we get a kernel _Q_ from _S_ 1 to _S_ 2, where _Q_ ( _x, B_ ) means _P_ ( _Y ∈ B |X_ = _x_ ). Given _W_ : (Ω _, F, P_ ) _→_ R, _E|W | < ∞_ , _G ⊆F_ , we defined _E_ [ _W | G_ ] = _Z_ , specified by _E_ [ _Z_ 1 _G_ ] = _E_ [ _W_ 1 _G_ ] for all _G ∈G_ . What is the relationship between these two concepts?

Write _W_ = _h_ ( _Y_ ), where _h_ : _S_ 2 _→_ R. Write _G_ = _σ_ ( _X_ ). Write _I_ : (Ω _, F_ ) _→_ (Ω _, G_ ), the identity function. We have ( _I, Y_ ) : Ω _→_ (Ω _, G_ ) _×_ ( _S_ 2 _, S_ 2). Write _α_ ( _ω, B_ ) for the kernel associated with ( _I, Y_ ). Then _α_ ( _ω, B_ ) means _P_ ( _Y ∈ B | G_ )( _ω_ ).

We can start from conditional expectation: let _P_ ( _A_ ) = _E_ [1 _A_ ]. Define _P_ ( _A | G_ )( _ω_ ) = _E_ [1 _A | G_ ](https://www.stat.berkeley.edu/~aldous/205A/_ω_). Then _α_ ( _·, B_ ) = _P_ ( _Y ∈ B | G_ ). This is the **regular conditional distribution for** _Y_ **given** _G_ . It is “regular” in the sense that _B �→ α_ ( _ω, B_ ) is a PM.

What is this in MT?


(Homework)

### **17.2 Martingales**

A _σ_ -field _G_ is a collection of events: _A ∈G_ , where _A_ is an event. For a RV _X_ , “ _X_ is _G_ -measurable” means _σ_ ( _X_ ) _⊆G_ . We use the shorthand _X ∈G_ . (This can, in principle, cause confusion: consider _J ∈F_ ?)

#### **17.2.1 General Setup** (Ω _, F, P_ )

Sub- _σ_ -fields _F_ 0 _⊆F_ 1 _⊆F_ 2 _⊆· · · ⊆F_ form a **filtration** . We interpret _Fn_ as the “information known at time _n_ ”.

A sequence ( _Xn, n ≥_ 0) is **adapted** to ( _Fn_ ) means _Xn ∈Fn ∀n_ .

**Definition 17.2.** A R-valued process ( _Xn,_ 0 _≤ n < ∞_ ) is a **martingale** (MG) if (i) _E|Xn| < ∞∀n_ (ii) ( _Xn_ ) is adapted to ( _Fn_ ) (iii) _E_ [ _Xn_ +1 _| Fn_ ] = _Xn,_ 0 _≤ n < ∞_

In condition (iii), if we have _E_ [ _Xn_ +1 _| Fn_ ] _≥ Xn_ , we have a **submartingale** . If _E_ [ _Xn_ +1 _| Fn_ ] _≤ Xn_ , we have a **supermartingale** .

Note that (iii) can be rewritten as _E_ [ _Xn_ +1 _− Xn | Fn_ ] = 0 _∀n_ .

_Typical Use of Theory_ : We have a complicated system ( _Yn_ ) and we look for _h_ such that _h_ ( _Yn_ ) is a MG. Take _Fn_ = _σ_ ( _Y_ 0 _, Y_ 1 _, . . . , Yn_ ). If we take _Xn_ = _h_ ( _Yn_ ), then ( _Xn_ ) _is_ adapated to ( _Fn_ ).

If we define _Xn_ and we say “ _Xn_ is a MG”, then we are taking _Fn_ = _σ_ ( _X_ 0 _, X_ 1 _, . . . , Xn_ ), the **natural filtration** for ( _Xn_ ).

**17.2.2 Examples Based on Independent RVs** _ξ_ 1 _, ξ_ 2 _, ξ_ 3 _, . . ._ **,** _Fn_ = _σ_ ( _ξ_ 1 _, . . . , ξn_ )

_LECTURE 17. OCTOBER 20_

66

**Example 17.3.** If _E|ξi| < ∞_ and _Eξi_ = 0 _∀i_ , then _Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_ξi_isaMG.</sup> _E_ [ _Sn_ +1 _| Fn_ ] = _E_ [ _Sn_ + _ξn_ +1 _| Fn_ ] = _Sn_ + _E_ [ _ξn_ +1 _| Fn_ ] = _Sn_ + _Eξn_ +1 = _Sn_ <u>�</u> �� <u>�</u> 0 because _Sn ∈Fn_ and _Sn_ +1 is independent of _Fn_ .


**Example 17.6.** Suppose that ( _ξi_ ) are independent. Fix _t_ , _Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_ξi_,andsupposethatwehave</sup> _φi_ ( _t_ ) def= _E_ exp( _tξi_ ) _< ∞_ . Then


is a MG. By independence, the expectation is 1.


**Example 17.7.** Take ( _ξi_ ) IID. Take density functions _f_ and _g >_ 0. Define the likelihood ratio _n_ _<u>g</u>_ <u>(</u> _<u>ξi</u>_ <u>)</u> _Ln_ = � _i_ =1 _f_ ( _ξi_ ) (a) If the ( _ξi_ ) have density _f_ , then ( _∀g_ ) ( _Ln_ ) is a MG.


_LECTURE 17. OCTOBER 20_

67


(b) If the ( _ξi_ ) have density _g_ , then, provided that _ELn < ∞_ , ( _Ln_ ) is a sub-MG. (a) implies that (1 _/Ln, n ≥_ 0) is a MG.


by Conditional Jensen’s Inequality. Therefore, _E_ [ _Ln_ +1 _| Fn_ ] _≥ Ln_ , so this is a sub-MG.

## **Lecture 18**

---

[← October 18](18-october-18.md) · [Up: contents](index.md) · [October 25 →](20-october-25.md)
