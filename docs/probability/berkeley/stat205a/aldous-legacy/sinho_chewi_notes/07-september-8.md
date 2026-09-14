---
title: September 8
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# September 8

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **5.1 Expectation (Undergraduate Version)**

1. _EX_ is the limit of ( _X_ 1 + _X_ 2 + _· · ·_ + _Xn_ ) _/n_ for IID RVs. _We will prove this later as the SLLN._

2. _EX_ is the fair stake for a random payoff _X_ . _This is the conceptual basis of martingale theory._

3. _EX_ =<sup>�</sup> _i_<sup>_iP_(</sup><sup>_X_=</sup><sup>_i_)or</sup> � _xf_ ( _x_ ) d _x_ .

4. _Eh_ ( _X_ ) =<sup>�</sup> _i_<sup>_h_(</sup><sup>_i_)</sup><sup>_P_(</sup><sup>_X_=</sup><sup>_i_)or</sup> � _h_ ( _x_ ) _f_ ( _x_ ) d _x_ . _We checked these in MT (last class)._

5. Abstract rules: _E_ ( _X_ + _Y_ ) = _EX_ + _EY_ , even if _X_ and _Y_ are dependent.

### **5.2 Expectation & Inequalities (MT Version)**

If _X_ : (Ω _, F, P_ ) _→_ R, then


_EX_ is well-defined if

1. _E|X|< ∞_ ( _−∞ < EX < ∞_ ),

2. or 0 _≤ X ≤∞_ , where 0 _≤ EX ≤∞_ .

From the definition (5.1), we can use the properties of the abstract integral.

- _E_ 1 _A_ = _P_ ( _A_ )

- _E_ ( _c_ 1 _X_ 1 + _c_ 2 _X_ 2) = _c_ 1 _EX_ 1 + _c_ 2 _EX_ 2

- **Monotone convergence** : If 0 _≤ X_ 1 _≤ X_ 2 _≤ X_ 3 _≤· · ·_ , so _Xn ↑ X∞_ a.s. (holds for all _ω_ outside some _A_ , _P_ ( _A_ ) = 0), then _EXn ↑ EX∞ ≤∞_ . Consider 0 _≤ X_ 11 _Ac ≤ X_ 21 _Ac ≤· · ·_ . Then _Xn_ 1 _Ac ↑ X∞_ 1 _Ac ∀ω_ and _EXn_ = _EXn_ 1 _A_<sup>_c_</sup> .

- If _X ≥_ 0, if _EX < ∞_ , then _P_ ( _X < ∞_ ) = 1. If _P_ ( _X < ∞_ ) = 1, it may not be true that _EX < ∞_ . For example, consider _P_ ( _X_ = _i_ ) _∼ ci_<sup>_−_3</sup><sup>_/_2</sup> .

Let _X_ , _Y_ be R-valued RVs.

**Markov’s Inequality** : If _X ≥_ 0, _EX < ∞_ , then


17

_LECTURE 5. SEPTEMBER 8_

18

**Chebyshev’s Inequality** : If _EX_<sup>2</sup> _< ∞_ , then var( _X_ ) def= _EX_<sup>2</sup> _−_ ( _EX_ )<sup>2</sup> = _E_ ( _X −EX_ )<sup>2</sup> and 0 _≤_ var( _X_ ) _< ∞_ . If var( _X_ ) _< ∞_ , then


**Theorem 5.1** (General Form of Markov’s Inequality) **.** _Let φ_ : R _→_ [0 _, ∞_ ) _be increasing. Then_


_provided that the quantity is not_ 0 _/_ 0 _._

_Proof._ Define


so _h_ ( _y_ ) = _φ_ ( _x_ )1( _y≥x_ ). Then _h_ ( _y_ ) _≤ φ_ ( _y_ ) _∀y_ . Therefore,


The “special” Markov’s inequality is the case of _φ_ ( _x_ ) = _x_<sup>+</sup> = max(0 _, x_ ).

To prove Chebyshev: set _Y_ = _|X − EX|_ and _φ_ ( _x_ ) = ( _x_<sup>+</sup> )<sup>2</sup> .


Another case is to take _φ_ ( _x_ ) = _e_<sup>_θx_</sup> for a parameter _θ >_ 0.


This is called the **Basic Large Deviation Inequality** . The inequality is only useful if _P_ ( _X > x_ ) _→_ 0 exponentially fast.

Suppose _X ∼_ Poisson( _λ_ ). Then _EX_ = _λ_ and var _X_ = _λ_ . Taking _x > λ_ , Markov gives _P_ ( _X > x_ ) _≤ λ/x_ and Chebyshev gives _P_ ( _X > x_ ) _≤ λ/_ ( _x − λ_ )<sup>2</sup> . We have


Minimizing this, we obtain 0 = _−x_ + _λe_<sup>_θ_</sup> . Take _θ_ with _λe_<sup>_θ_</sup> = _x_ .


**Theorem 5.2** (Cauchy-Schwarz Inequality) **.**


_LECTURE 5. SEPTEMBER 8_

19


Since _b_<sup>2</sup> _≤ ac_ , we are done.

_Note_ : Given _x_ 1 _, x_ 2 _, . . . , xn, y_ 1 _, y_ 2 _, . . . , yn ∈_ R, take _P_ ( _X_ = _xi, Y_ = _yi_ ) = 1 _/n,_ 1 _≤ i ≤ n_ . C-S says


Similarly for the next inequalities.

**Definition 5.3.** _φ_ is **convex** if _∀x < y, ∀_ 0 _≤ λ ≤_ 1 _, φ_ ( _x_ + _λ_ ( _y − x_ )) _≤ φ_ ( _x_ ) + _λ_ ( _φ_ ( _y_ ) _− φ_ ( _x_ )).

In practice: _φ_<sup>_′′_</sup> ( _x_ ) _≥_ 0 = _⇒ φ_ is convex.

**Theorem 5.4** (Jensen’s Inequality) **.** _Consider an interval I ⊆_ R _. Let φ_ : _I →_ R _be convex. Suppose P_ ( _X ∈ I_ ) = 1 _. Then φ_ ( _EX_ ) _≤ Eφ_ ( _X_ ) _provided both expectations are well-defined._

_Proof._ Given _x_ and convex _φ_ , there exists a “tangent line” _l_ ( _y_ ) _≤ φ_ ( _y_ ) _∀y_ such that _l_ ( _x_ ) = _φ_ ( _x_ ). Set _x_ = _EX_ , take the tangent _l_ ( _·_ ) at _x_ .


Consider the distribution of ( _X, φ_ ( _X_ )). Then


**Example 5.5.** Take _φ_ ( _x_ ) = _|x|_<sup>_p_</sup> , 1 _≤ p_ . Jensen’s inequality says _|EY |_<sup>_p_</sup> _≤ E|Y |_<sup>_p_</sup> . Apply the inequality with 0 _≤ a < b < ∞_ , _Y_ = _|X|_<sup>_a_</sup> , _p_ = _b/a_ . Then ( _E|X|_<sup>_a_</sup> )<sup>_b/a_</sup> _≤ E|X|_<sup>_b_</sup> , so


_Notation_ . The “ _L_<sup>_p_</sup> norm” is _∥x∥p_ def= ( _E|X|_<sup>_p_</sup> )<sup>1</sup><sup>_/p_</sup> _,_ 1 _≤ p < ∞_ and (5.2) says that _p �→∥x∥p_ is increasing on 1 _≤ p < ∞_ .

**Example 5.6.** Let


or


with 0 _< x < ∞_ . If _X >_ 0, then _Eφ_ ( _X_ ) _≥ φ_ ( _EX_ ). 1.


_LECTURE 5. SEPTEMBER 8_

20

2. _−E_ log _X ≥−_ log _EX ⇔ EX ≥_ exp( _E_ log _X_ )

Consider _x_ 1 _, x_ 2 _, . . . , xn >_ 0, _P_ ( _X_ = _xi_ ) = 1 _/n_ , 1 _≤ i ≤ n_ .


## **Lecture 6**

---

[← September 6](06-september-6.md) · [Up: contents](index.md) · [September 13 →](08-september-13.md)
