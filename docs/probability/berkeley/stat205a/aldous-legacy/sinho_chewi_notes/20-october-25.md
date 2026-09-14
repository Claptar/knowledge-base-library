---
title: October 25
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# October 25

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **18.1 General Constructions of MGs**

Consider a filtration ( _Fn,_ 0 _≤ n < ∞_ ) on (Ω _, F, P_ ). Recall that ( _Xn,_ 0 _≤ n < ∞_ ) is **adapted** to ( _Fn_ ) means _Xn ∈Fn_ , 0 _≤ n < ∞_ .

We can define _F∞_ = _σ_ (<sup>�</sup> _n_<sup>_Fn_)</sup><sup>_⊆F_.Weareusually</sup><sup>_not_givenaRV</sup><sup>_X∞_.Whenweconsider</sup><sup>_XT_fora</sup> stopping time _T_ , we need to care about _{T_ = _∞}_ .

**Example 18.1.** Consider any _X_ with _E|X| < ∞_ , then _Xn_ = _E_ [ _X | Fn_ ], 0 _≤ n < ∞_ is a MG. _E_ [ _Xn | Fn−_ 1] = _E_ [ _E_ [ _X | Fn_ ] _| Fn−_ 1] = _E_ [ _X | Fn−_ 1] = _Xn−_ 1

by the Tower Property, since _Fn−_ 1 _⊆Fn_ .

Similarly, for any event _A_ , _Yn_ = _P_ ( _A | Fn_ ) is a MG.

_Notation_ . For any _X_ = ( _Xn_ ), define ∆<sup>_X_</sup> _n_<sup>=</sup><sup>_Xn−Xn−_1,</sup><sup>_n≥_1.Then(</sup><sup>_Xn, n≥_0)isaMGifandonlyif</sup> ∆<sup>_X_</sup> _n_<sup>_∈Fn_for</sup><sup>_n ≥_1,</sup><sup>_E_</sup> ��∆ _nX_ �� _< ∞_ for _n ≥_ 1, _E_ [∆ _nX_<sup>_| Fn_] = 0a.s.for</sup><sup>_n ≥_1,and</sup><sup>_X_0</sup><sup>_∈F_0,</sup><sup>_E|X_0</sup><sup>_| < ∞_.Call</sup> (∆<sup>_X_</sup> _n_<sup>_, n≥_1)a</sup><sup>**martingaledifferencesequence**.Togetthesub-MGproperty,</sup><sup>_E_[∆</sup><sup>_X_</sup> _n_<sup>_| Fn−_1]</sup><sup>_≥_0a.s.for</sup> _n ≥_ 1.

**Example 18.2.** Consider any ( _Xn, n ≥_ 0), adapted to ( _Fn_ ) and _E|Xn| < ∞∀n_ . Define ( _Yn_ ) by _Y_ 0 = _X_ 0, ∆<sup>_Y_</sup> _n_<sup>= ∆</sup><sup>_X_</sup> _n_<sup>_−E_[∆</sup><sup>_X_</sup> _n_<sup>_| Fn−_1].Define(</sup><sup>_Zn_)by</sup><sup>_Z_0= 0,∆</sup><sup>_Z_</sup> _n_<sup>=</sup><sup>_E_[∆</sup><sup>_X_</sup> _n_<sup>_| Fn−_1].Then</sup> (i) _Xn_ = _Yn_ + _Zn_ (ii) ( _Yn_ ) is a MG. (iii) _Zn ∈Fn−_ 1, for _n ≥_ 1 and _Zn_ = 0. ( _Zn_ ) is **predictable** and _E|Zn| < ∞_ . This is the _unique_ decomposition with these properties.

Why is this unique?


68

_LECTURE 18. OCTOBER 25_

69

since ( _Yn_ ) is a MG and _Z_ is predictable.

This is called the **Doob decomposition** .

If ( _Xn_ ) is a MG, then ( _Xn − X_ 0 _, n ≥_ 0) is a MG. We often say “WLOG assume _X_ 0 = 0”.

For a MG, _E_ [ _Xn | Fn−_ 1] = _Xn−_ 1 implies that _EXn_ = _EXn−_ 1, which implies that _EXn_ = _EX_ 0 _∀n_ . For a sub-MG, _E_ [ _Xn | Fn−_ 1] _≥ Xn−_ 1, which implies that _EXn ≥ EXn−_ 1, which implies that _EXn ≥ EX_ 0 _∀n_ .

**Theorem 18.3** (Convexity Theorem) **.** _Let_ ( _Xn_ ) _be adapted to_ ( _Fn_ ) _, φ be convex, and E|φ_ ( _Xn_ ) _| < ∞. (a) If_ ( _Xn_ ) _is a MG, then φ_ ( _Xn_ ) _is a sub-MG. (b) If_ ( _Xn_ ) _is a sub-MG and if φ is increasing, then φ_ ( _Xn_ ) _is a sub-MG._


where we used Conditional Jensen, ( _Xn_ ) is a sub-MG, and _φ_ is increasing. Hence, _φ_ ( _Xn_ ) _is_ a sub-MG. We have equality if ( _Xn_ ) is a MG.

**Example 18.4.** If ( _Xn_ ) is a MG, then (provided integrable) (i) _|Xn|_<sup>_p_</sup> ( _p ≥_ 1) is a sub-MG, because _x �→|x|_<sup>_p_</sup> is convex (ii) _Xn_<sup>2isasub-MG</sup> (iii) exp( _θXn_ ), ( _−∞ < θ < ∞_ ) is a sub-MG, because _x �→ e_<sup>_θx_</sup> is convex (iv) max( _Xn, c_ ) is a sub-MG, because _x �→_ max( _x, c_ ) is convex (v) min( _Xn, c_ ) is a super-MG

### **18.2 Stopping Times**


_LECTURE 18. OCTOBER 25_

70

##### This is the **pre-** _T σ_ **-field** .

There are many “obvious” properties.

1. If ( _Xn_ ) is adapted, if _T_ is a stopping time, _T < ∞_ , then _XT_ is _FT_ -measurable.

_Proof. Want_ : _{XT ∈ B} ∈FT ∀B_ .

_Want_ : _{XT ∈ B} ∩{T_ = _n} ∈Fn_ . This is the same as _{Xn ∈ B} ∩{T_ = _n}_ . _{Xn ∈ B} ∈Fn_ since _Xn_ is adapted. _{T_ = _n} ∈Fn_ by the definition of a stopping time.

2. If _T_ 1 _≤ T_ 2 are stopping times, then _FT_ 1 _⊆FT_ 2.

3. If _S_ and _T_ are stopping times, then _{S_ = _T } ∈FS ∩FT_ , and for _A ⊆{S_ = _T }_ ,


Given an adapted ( _Xn_ ) and a stopping time _T_ , the process _X_<sup>ˆ</sup> _n_ = _X_ min( _n,T_ ) is adapted. Call _X_<sup>ˆ</sup> the “ **stopped process** ”.

_Story_ . _Fn_ is the information at the end of day _n_ . You can buy a stock at the end of any day _n_ . _Xn_ is the price of 1 share at the end of day _n_ . _Hn_ is the number of shares I hold during day _n_ (they must be bought at day _n −_ 1 or earlier). Therefore, _Hn ∈Fn−_ 1. _Yn_ is my accumulated profit at the end of day _n_ . What is the relation? ∆<sup>_Y_</sup> _n_<sup>=</sup><sup>_Hn_∆</sup><sup>_X_</sup> _n_<sup>.Also,</sup><sup>_Y_0= 0.Write</sup><sup>_Y_=</sup><sup>_H· X_,a“</sup><sup>**martingaletransform**”ora“</sup><sup>**discrete-time**</sup> **stochastic integral** ”.

**Theorem 18.7** (Durrett 2.7) **.** _Suppose_ ( _Xn_ ) _is adapted and_ ( _Hn_ ) _is predictable. Consider Y_ = _H · X (for simplicity, assume Hn is bounded)._


_(ii) If_ ( _Xn_ ) _is a sub-MG and Hn ≥_ 0 _, then_ ( _Yn_ ) _is a sub-MG._


since ( _Xn_ ) is a sub-MG. Therefore, ( _Yn_ ) is a sub-MG.

**Corollary 18.8.** _If_ ( _Xn_ ) _is a (sub-)MG, if T is a stopping time, then X_<sup>ˆ</sup> _n_ = _X_ min( _n,T_ ) _is a (sub-)MG._

_Proof._ Buy 1 share at the end of day 0 and sell at the end of day _T_ .


( _Hn_ ) is _predictable_ because _{n ≤ T }_ = _{T ≤ n −_ 1 _}_<sup>_c_</sup> _∈Fn−_ 1. The process _Y_ = _H · X_ is explicitly

_LECTURE 18. OCTOBER 25_

71

_Yn_ = _X_ min( _n,T_ ) _− X_ 0. Apply 18.7.

## **Lecture 19**

---

[← October 20](19-october-20.md) · [Up: contents](index.md) · [October 27 →](21-october-27.md)
