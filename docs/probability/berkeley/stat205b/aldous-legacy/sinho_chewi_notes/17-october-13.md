---
title: October 13
source: https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# October 13

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **15.1 More “RVs & Distributions”**

**Corollary 15.1.** _Given a PM µ on S ×_ R _, given a RV X_ : Ω _→ S where_ dist( _X_ ) = _µ_ 1 _is the marginal of µ, given a RV U_ : Ω _→_ [0 _,_ 1] _, where_ dist( _U_ ) _is_ Uniform(0 _,_ 1) _and U is independent of X, then ∃f_ : _S ×_ [0 _,_ 1] _→_ R _such that, writing Y_ = _f_ ( _X, U_ ) _,_ dist( _X, Y_ ) = _µ._

_Proof._ Let _Q_ be the kernel _S →_ R associated with _µ_ . Let _f_ ( _s, u_ ) be the inverse distribution function of the PM _Q_ ( _s, ·_ ). _f_ ( _s, U_ ) has the distribution _Q_ ( _s, ·_ ).

Check this _f_ works. The above statement is equivalent to _Q_ ( _s, B_ ) = _λ{u_ : _f_ ( _s, u_ ) _∈ B}_ .


Consider the map


for 1 _≤ m < n < ∞_ . _πm,n_ is the associated map _P_ (R<sup>_n_</sup> ) _→P_ (R<sup>_m_</sup> ) given by


**Theorem 15.2** (Kolmogorov Extension (Consistency) Theorem) **.** _Given PMs µn on_ R<sup>_n_</sup> _,_ 1 _≤ n < ∞, which are consistent in the sense that πn,mµn_ = _µm,_ 1 _≤ m < n < ∞, then there exists a PM µ∞ on_ R<sup>_∞_</sup> _such that π∞,mµ∞_ = _µm,_ 1 _≤ m < ∞._

To define ( _xi,_ 1 _≤ i < ∞_ ), it is enough to define _xi_ for each _i_ .

To define ( _Xi,_ 1 _≤ i < ∞_ ), it is enough to define each _Xi_ .

_Proof._ Take _U_ 1 _, U_ 2 _, . . ._ , independent U[0 _,_ 1]. Define _X_ 1 = _Fµ_<sup>_−_</sup> 1<sup>1(</sup><sup>_U_1).</sup> Inductively, suppose we have defined **X** _n_ = ( _X_ 1 _, . . . , Xn_ ) as functions of ( _U_ 1 _, . . . , Un_ ), such that dist( **X** _n_ ) = _µn_ . We will show that there exists _fn_ +1 such that, defining _Xn_ +1 = _fn_ +1( **X** _n, Un_ +1), we have

dist( **X** _n_ +1 = ( **X** _n, Xn_ +1)) = _µn_ +1

57

_LECTURE 15. OCTOBER 13_

58

This constructs an infinite sequence ( _Xn,_ 1 _≤ n < ∞_ ). Define _µ∞_ = dist( _Xn,_ 1 _≤ n < ∞_ ). Use 15.1 with _S_ = R<sup>_n_</sup> , _X_ = **X** _n_ , _U_ = _Un_ +1, and _µ_ = _µn_ +1 on R<sup>_n_</sup> _×_ R.

**Example 15.3.** Given a measurable _h_ : R _→_ R, and a PM _µ_ that is invariant under _h_ (dist( _X_ ) = _µ_ implies that dist( _h_ ( _X_ )) = _µ_ ), for each _n_ , take dist( _Xn_ ) = _µ_ . Define _Xi_ = _h_ ( _Xi_ +1), 1 _≤ i ≤ n −_ 1. Let _µn_ = dist( _X_ 1 _, . . . , Xn_ ). (This is a separate construction for different _n_ .) Then 15.2 implies that _∃µ∞_ = dist( _Y_ 1 _, Y_ 2 _, . . ._ ) such that dist( _Y_ 1 _, . . . , Yn_ ) = dist( _X_ 1 _, . . . , Xn_ ) _∀n_ , where _Yi_ = _h_ ( _Yi_ +1) for all 1 _≤ i < ∞_ .

### **15.2 Intermission: Example Relevant to Data**

_Hypothesis_ : Probabilities from gambling odds are indistinguishable from “true probabilities” as formalized in math.

Does this hypothesis make predictions that can be checked against data?

Consider _P_ (home team wins), which starts off at 50%. The probability fluctuates over time, eventually reaching 0% or 100%. Suppose there is a half-time break. The perceived probability at half-time will change from game to game.

_Model_ . Let _Z_ 1 be the point difference at half-time (home team _−_ away team) in the first half. Let _Z_ 2 be the point difference in the second half. The home team wins if and only if _Z_ 1 + _Z_ 2 _>_ 0. Assume _Z_ 1 =d _−Z_ 1 (symmetric), with _Z_ 1 and _Z_ 2 independent. Suppose that _Z_ 1 has a continuous distribution.


### **15.3 Conditional Expectation in a Measure Theory Setting**

_Undergraduate Version_ . Let _X, Y_ be R-valued and _A_ be an event. _EX_ is a number. _E_ [ _X | A_ ] is a number. _E_ [ _X | Y_ = _y_ ] is a number depending on _y_ (is a function of _y_ ), which equals _h_ ( _y_ ), say. Write _E_ [ _X | Y_ ] = _h_ ( _Y_ ), which we view as a RV. This is useful because _EE_ [ _X | Y_ ] = _EX_ .

_MT Setup_ . _X_ is a map from (Ω _, F, P_ ) to R, with _E|X| < ∞_ . Consider a sub- _σ_ -field _G ⊆F_ . We will define _E_ [ _X | G_ ] to be a certain _G_ -measurable RV.

_G_ is “information”.

_EX_ is the _fair stake_ now to get the payoff _X_ tomorrow. The gain is _X − a_ , and in order for the stake to be fair, _E_ [gain] = 0 means that _a_ = _EX_ .

Suppose that we know the information in _G_ . The fair stake now is _Y_ , say.

Strategy: Choose _G ∈G_ . Bet if _G_ happens, not if _G_<sup>_c_</sup> happens. We gain ( _X − Y_ )1 _G_ . The stake is fair if _E_ [gain] = 0 for all stakes, which is equivalent to _E_ ( _X − Y_ )1 _G_ = 0 _∀G_ .

_LECTURE 15. OCTOBER 13_

59

Define _E_ [ _X | G_ ] to be the RV _Y_ satisfying:


#### **15.3.1 Existence**

For _G ∈G_ , define _ν_ ( _G_ ) = _EX_ 1 _G_ . If _P_ ( _G_ ) = 0, then _ν_ ( _G_ ) = 0, which says that _ν ≪ P_ as measures on (Ω _, G_ ). The Radon-Nikodym Theorem says that there is a density


which is _G_ -measurable. The defining property of the Radon-Nikodym density is (15.2). (This works when _ν_ is a signed measure.)

#### **15.3.2 Uniqueness**

**Lemma 15.4.** _If Y is G-measurable, if E|Y | < ∞, if E_ [ _Y_ 1 _G_ ] _≥_ 0 _∀G ∈G, then Y ≥_ 0 _a.s._

_Proof._ If not, _G_ def= _{Y <_ 0 _}_ has _P_ ( _G_ ) _>_ 0 and _EY_ 1 _G <_ 0. Contradiction.

**Corollary 15.5.** _If Y_ 1 _and Y_ 2 _each satisfy_ (15.1) _and_ (15.2) _, then Y_ 1 = _Y_ 2 _a.s._

_Proof. E_ ( _Y_ 1 _− Y_ 2)1 _G_ = 0 _∀G_ , which by 15.4 implies that _Y_ 1 _≥ Y_ 2 a.s. and _Y_ 1 _≤ Y_ 2 a.s.

**Lemma 15.6** (Technical Lemma) **.** _(a) If Z_ = _E_ [ _X | G_ ] _, then E_ [ _V Z_ ] = _E_ [ _V X_ ] _for all bounded G- measurable V . Use the definition for V_ = 1 _G and the Monotone Class Theorem._

_(b) If Z is G-measurable, then to prove that Z_ = _E_ [ _X | G_ ] _, it is enough to prove_

_EZ_ 1 _A_ = _EX_ 1 _A ∀A ∈A_

_where A is a π-class, G_ = _σ_ ( _A_ ) _. (Dynkin π-λ Lemma)_

## **Lecture 16**

---

[← October 11](16-october-11.md) · [Up: contents](index.md) · [October 18 →](18-october-18.md)
