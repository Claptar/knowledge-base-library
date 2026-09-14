---
title: November 15
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# November 15

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **24.1 Examples Using “Method of Bounded Differences”**

Last class: **Theorem** . Suppose _ξ_ 1 _, ξ_ 2 _, . . . , ξn_ are independent, _Z_ = _f_ ( _ξ_ 1 _, . . . , ξn_ ), where _f_ has the property


whenever _|{i_ : _xi̸_ = _yi}|_ = 1. Then _P_ ( _|Z − EZ| ≥ λ_<sup>_√_</sup> _<u>n</u>_ <u>)</u> _≤_ 2 _e_<sup>_−λ_2</sup><sup>_/_2</sup> for _λ >_ 0.

**Example 24.1.** Put _n_ balls “at random” into _m_ boxes. Consider _Z_ ( _n, m_ ), the number of empty boxes. _EZ_ ( _n, m_ ) = _m_ (1 _−_ 1 _/m_ )<sup>_n_</sup> . There is a complicated formula for the distribution. However, we can apply the theorem to _ξi_ , the box containing ball _i_ , for 1 _≤ i ≤ n_ . Then (24.1) holds.

**Example 24.2.** Take two independent Bernoulli(1 _/_ 2) sequences of length _n_ (e.g. 10100110 and 01101000). Let _Zn_ be the length of the longest common subsequence.

_Fact_ . _Zn/n −−→_<sup>a.s.</sup> _c_ as _n →∞_ , but there is no formula for _c_ .

Take _ξi_ to be the pair of digits in the two strings at position _i_ . Any change **x** _�→_ **y** has _f_ ( **y** ) _− f_ ( **x** ) _≥−_ 2, which also implies that _f_ ( **y**<sup>_′_</sup> ) _− f_ ( **x**<sup>_′_</sup> ) _≤_ 2 for any **x**<sup>_′_</sup> _,_ **y**<sup>_′_</sup> . Therefore, _Zn/_ 2 satisfies (24.1).

_Recall_ : A _c_ **-coloring** of _G_ means assigning one of _c_ colors to each vertex such that color( _v_ ) _̸_ = color( _v_<sup>_′_</sup> ) whenever ( _v, v_<sup>_′_</sup> ) is an edge. The **chromatic number** is _χ_ ( _G_ ) = min _{c_ : _∃c_ -coloring _}_ .

_Recall_ : An Erd˝os–Renyi random graph model _G_ ( _n, p_ ) has _n_ vertices and each of the � _n_ 2� possible edges is present with probability _p_ .

Let _Z_ = _χ_ ( _G_ ( _n, p_ )). Order the vertices as 1 _,_ 2 _,_ 3 _, . . . , n_ . For _i ≥_ 2, let

_ξi_ = (1( _i,_ 1) is an edge _, . . . ,_ 1( _i,i−_ 1) is an edge)

Then (24.1) holds for _Z_ = _f_ ( _ξ_ 2 _, ξ_ 3 _, . . . , ξn_ ).

(To check (24.1), we are using the trick sup _i̸_ = _j |xi − xj|_ = sup _i̸_ = _j_ ( _xi − xj_ ).)

**Example 24.3.** Put _n_ points IID uniform in the unit square. Fix 0 _< c <_ 1. Let _Z_ ( _n, c_ ) be the maximum number of disjoint _c × c_ squares containing 0 points. Let _ξi_ be the position of the _i_ th point. (24.1) holds.

89

_LECTURE 24. NOVEMBER 15_

90

### **24.2 Reversed MGs**

Consider sub- _σ_ -fields _G_ 0 _⊇G_ 1 _⊇G_ 2 _⊇· · ·_ , where _G∞_ =<sup>�</sup> _n_<sup>_Gn_.Wesaythat(</sup><sup>_Xn_)isa</sup><sup>**reversedMG**if:</sup> _E|Xn| < ∞_ , _E_ [ _Xm | Gn_ ] = _Xn_ , for _m ≤ n_ , and ( _Xn_ ) is adapted to ( _Gn_ ). (In Durrett, _Gn_ = _F−n_ .) The definition implies that _Xn_ = _E_ [ _X_ 0 _| Gn_ ].

**Theorem 24.4.** _For a reversed MG, Xn → E_ [ _X_ 0 _| G∞_ ] _a.s. and in L_<sup>1</sup> _._

_Proof._ ( _XN , XN −_ 1 _, . . . , X_ 0) is a MG. If _UN_ is the number of upcrossings of the martingale over [ _a, b_ ], the upcrossing inequality says


(As in the proof for MGs:) _UN ↑ U∞_ , where


which implies that _U∞ < ∞_ a.s., which implies that _Xn → X∞ ∈_ [ _−∞, ∞_ ] a.s. However, we have _Xn_ = _E_ [ _X_ 0 _| Gn_ ], so ( _Xn_ ) is UI, so _Xn → X∞_ in _L_<sup>1</sup> (also), with _E|X∞| < ∞_ .

We need to show _X∞_ = _E_ [ _X_ 0 _| G∞_ ]. _Xn ∈Gn ⊆GK_ for _n > K_ . Take _n →∞_ , so _X∞ ∈GK_ . Take _K →∞_ , so _X∞ ∈G∞_ . We need to show _EX∞_ 1 _G_ = _EX_ 01 _G_ for _G ∈G∞_ . _Xn_ = _E_ [ _X_ 0 _| Gn_ ] implies that _EXn_ 1 _G_ = _EX_ 01 _G_ for _G ∈G∞_ . _Xn → X∞_ in _L_<sup>1</sup> implies that _EXn_ 1 _G → EX∞_ 1 _G_ , so _EX_ 01 _G_ = _EX∞_ 1 _G_ .

### **24.3 Exchangeable Sequences**

A sequence of RVs ( _X_ 1 _, X_ 2 _, X_ 3 _, . . ._ ) is called **exchangeable** if


for all _n_ and all permutations _π_ of (1 _,_ 2 _, . . . , n_ ).

Clearly, IID implies exchangeable.

**Theorem 24.5.** _Suppose_ ( _Xi,_ 1 _≤ i < ∞_ ) _are exchangeable and_ R _-valued and E|X_ 1 _| < ∞. Write Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi.ThenSn/n →E_[</sup><sup>_X_1</sup><sup>_| τ_]</sup><sup>_a.s.andinL_1</sup><sup>_,whereτ_= tail(</sup><sup>_Xi, i ≥_1)</sup><sup>_._</sup>

**Corollary 24.6.** _If_ ( _Xi_ ) _are IID, E|X_ 1 _| < ∞, then τ is trivial, which implies that E_ [ _X_ 1 _| τ_ ] = _EX_ 1 _and 24.5 implies that Sn/n → EX_ 1 _._

_Fact_ . If ( _Z_ 1 _, W_ ) = (d _Z_ 2 _, W_ ) and _E|Z_ 1 _| < ∞_ , then _E_ [ _Z_ 1 _| W_ ] = _E_ [ _Z_ 2 _| W_ ] a.s.

_Proof._ Let _Q_ be the kernel associated with the distribution ( _Z_ 1 _, W_ ). _E_ [ _Z_ 1 _| W_ ] = _φ_ ( _W_ ), where the function _φ_ ( _w_ ) = � _zQ_ ( _ω,_ d _z_ ), and _E_ [ _Z_ 2 _| W_ ] = _φ_ ( _W_ ).

_Exercise_ . Let _E|X| < ∞_ . If _X_ =d _E_ [ _X | G_ ], then _X_ = _E_ [ _X | G_ ] a.s.

_Comment_ . The proof is easy if _EX_<sup>2</sup> _< ∞_ .

_LECTURE 24. NOVEMBER 15_

91

_Proof of 24.5._ Define


_Gn ⊇Gn−_ 1 _⊇· · ·_ are decreasing. Then


by 24.7. Therefore, _Sn/n_ = _E_ [ _X_ 1 _| Gn_ ] _→ E_ [ _X_ 1 _| G∞_ ] a.s. and in _L_<sup>1</sup> . Note that _G∞ ⊇ τ_ . However, lim _Sn/n_ is _τ_ -measurable. Therefore, _E_ [ _X_ 1 _| G∞_ ] is _τ_ -measurable, so


**Lemma 24.7.** _E_ [ _Xi | Gn_ ] = _E_ [ _X_ 1 _| Gn_ ] _a.s.,_ 1 _≤ i ≤ n._

_Proof._ Take a permutation _π_ of (1 _, . . . , n_ ).

( _Xπ_ (1) _, . . . , Xπ_ ( _n_ ) _, Xn_ +1 _, Xn_ +2 _, . . ._ ) = (d _X_ 1 _, . . . , Xn, Xn_ +1 _, Xn_ +2 _, . . ._ ) Set _W_ = ( _Sn, Xn_ +1 _, Xn_ +2 _, . . ._ ). Then ( _Xπ_ ( _i_ ) _, . . . , Xπ_ ( _n_ ) _, W_ ) =d ( _X_ 1 _, . . . , Xn, W_ ), which implies that ( _Xπ_ ( _i_ ) _, W_ ) = (d _X_ 1 _, W_ ), which implies that ( _Xi, W_ ) = (d _X_ 1 _, W_ ) for 1 _≤ i ≤ n_ . By the Fact proven above, _E_ [ _Xi | W_ ] = _E_ [ _X_ 1 _| W_ ], and _Gn_ = _σ_ ( _W_ ).

## **Lecture 25**

---

[← November 10](25-november-10.md) · [Up: contents](index.md) · [November 17 →](27-november-17.md)
