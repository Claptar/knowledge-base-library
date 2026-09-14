---
title: January 24
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# January 24

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **3.1 Transforms**

There are three variants of the same idea.

1. Let _X_ take values in _{_ 0 _,_ 1 _,_ 2 _, . . . }_ . The **probability generating function** is


for 0 _≤ z ≤_ 1.

2. If _X_ takes values in [0 _, ∞_ ), the **Laplace transform** is _LX_ ( _θ_ ) = _Ee_<sup>_−θX_</sup> = �0 _∞ e_<sup>_−θx_</sup> _fX_ ( _x_ ) d _x_ if _X_ has density _fX_ ( _x_ ). If _X_ has distribution _µ_ , then _LX_ ( _θ_ ) = �0 _∞ e_<sup>_−θx_</sup> _µX_ (d _x_ ). The Laplace transform is finite for 0 _≤ θ < ∞_ .

3. For _X_ , an arbitrary R-valued random variable, the **characteristic function** (Fourier transform) is _φX_ ( _t_ ) = _Ee_<sup>_itX_</sup> = _E_ cos( _tX_ ) + _iE_ sin( _tX_ ). If _X_ has a density, then _φX_ ( _t_ ) = � _−∞∞_<sup>_eitxfX_(</sup><sup>_x_) d</sup><sup>_x_.</sup>

_Point_ . If _S_ = _X_ 1 + _X_ 2 for independent _X_ 1, _X_ 2, then


since


by the product rule.

_Notation_ . _t, x, y ∈_ R. _z ∈_ C, _z_ = _x_ + _iy_ . _|z|_ = � _x_<sup>2</sup> + _y_<sup>2</sup> , _|z_ 1 _z_ 2 _|_ = _|z_ 1 _||z_ 2 _|_ . �� _eitx_ �� = 1. For a C-valued RV _Z_ = _X_ + _iY_ , _EZ_ = _EX_ + _iEY_ . _|EZ| ≤ E|Z|_ . _φX_ ( _t_ ) = _Ee_<sup>_itX_</sup> , where _φX_ : R _→_ C. The modulus is

_|φX_ ( _t_ ) _|_ = �� _EeitX_ �� _≤ E_ �� _eitX_ �� = 1 _._

_φX_ ( _t_ + _h_ ) _− φX_ ( _t_ ) = _E_ [ _e_<sup>_i_(</sup><sup>_t_+</sup><sup>_h_)</sup><sup>_X_</sup> _− e_<sup>_itX_</sup> ] = _E_ [ _e_<sup>_itX_</sup> ( _e_<sup>_ihX_</sup> _−_ 1)], so


say. As _h ↓_ 0, then _e_<sup>_ihX_</sup> _−_ 1 _→_ 0. Use bounded convergence to see that _t �→ φX_ ( _t_ ) is uniformly continuous.

11

_LECTURE 3. JANUARY 24_

12

### **3.2 Inversion**

**Theorem 3.1** (Inversion Formulas) **.** _Let φ_ ( _t_ ) _be the CF of a PM µ. (a)_


so the modulus is at most _b − a_ .

_Proof._ By Fubini,


The inner integral contains a term

since _e_<sup>_it_</sup> = cos _t_ + _i_ sin _t_ . The first term is


Here,


_LECTURE 3. JANUARY 24_

13


_Comments_ .

1. If _φµ_ ( _t_ ) _≡ φν_ ( _t_ ) _∀t_ , then _ν_ = _µ_ . ( _Uniqueness_ )

2. In principle, we can calculate the distribution of _Sn_ = _X_ 1 + _X_ 2 + _· · ·_ + _Xn_ for independent _Xi_ using _φSn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_φX_</sup> _i_<sup>(</sup><sup>_t_).</sup>

**Example 3.2.** If _X_ has Normal(0 _, σ_<sup>2</sup> ) distribution, then _φX_ ( _t_ ) = exp( _−σ_<sup>2</sup> _t_<sup>2</sup> _/_ 2).

So, if _X_ 1, _X_ 2 are independent Normal(0 _, σi_<sup>2),then</sup><sup>_S_=</sup><sup>_X_1 +</sup><sup>_X_2has</sup>

_φS_ ( _t_ ) = _φX_ 1( _t_ ) _φX_ 2( _t_ ) = exp( _−σ_ 1<sup>2</sup><sup>_t_2</sup><sup>_/_2</sup><sup>_−σ_</sup> 2<sup>2</sup><sup>_t_2</sup><sup>_/_2) = exp(</sup><sup>_−_(</sup><sup>_σ_</sup> 1<sup>2+</sup><sup>_σ_</sup> 2<sup>2)</sup><sup>_/_2)</sup> = CF of Normal(0 _, σ_ 1<sup>2+</sup><sup>_σ_</sup> 2<sup>2)</sup><sup>_._</sup>

_LECTURE 3. JANUARY 24_

14


For _c >_ 0, _φcX_ ( _t_ ) = _φX_ ( _ct_ ) = _Ee_<sup>_ictX_</sup> .

**Example 3.4.** _Y_ has density Since which implies that


### **3.3 Parseval Identity**

**Theorem 3.5** (Parseval Identity) **.** _Let µ and ν be PMs with CFs φµ and φν. Then_


_Proof._ Take _X_ , _Y_ independent, dist( _X_ ) = _µ_ , dist( _Y_ ) = _ν_ . _E_ [ _e_<sup>_iXY_</sup> _| Y_ = _y_ ] = _Ee_<sup>_iyX_</sup> = _φµ_ ( _y_ ) _,_

so Also,


By choice of “simple” _ν_ , we get general identities between _µ_ and _φ_ ( _µ_ ).

**Example 3.6.** _ν_ is uniform on [ _−c, c_ ].


For any _µ_ ,


_LECTURE 3. JANUARY 24_

15


## **Lecture 4**

---

[← January 19](04-january-19.md) · [Up: contents](index.md) · [January 26 →](06-january-26.md)
