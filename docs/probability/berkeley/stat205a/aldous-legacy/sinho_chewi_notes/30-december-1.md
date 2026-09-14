---
title: December 1
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# December 1

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **28.1 Explicit Calculations with Brownian Motion**

Last class:


#### **28.1.1 Consequences of Formula** (28.3)

_Special Cases_ .

1. _d_ = 0, _c >_ 0.


We can invert this to get the formula for the density.

2.


We know 0 _< T ≤∞_ . As _λ ↓_ 0, exp( _−λT_ ) _↑_ 1( _T <∞_ ), so the expectation converges to _P_ ( _T < ∞_ ) by monotone convergence.

Define _Md_ def= sup _t≥_ 0 ( _Bt − dt_ ), which is BM with drift _−d_ . The event _{Md ≥ c}_ = _{Tc,d < ∞}_ , so _P_ ( _Md ≥ c_ ) = exp( _−_ 2 _dc_ ) (for _d >_ 0). Therefore, the distribution of _Md_ is Exponential(2 _d_ ),


#### **28.1.2 Reflection Principle Formula & Consequences**

**Theorem 28.1** (Reflection Principle) **.** _For a, b >_ 0 _, t >_ 0 _,_


Condition on _Ta_ = _s_ , say. The future process _B_<sup>˜</sup> _u_ = _Bs_ + _u − a_ , 0 _≤ u < ∞_ , is distributed as BM.


102

_LECTURE 28. DECEMBER 1_

103


This implies (by integration)


The standard Normal density for _Z_ is


and _Bt_ =d _t_ 1 _/_ 2 _Z_ .

_P_ ( _Ta ≤ t_ ) = 2 _P_ ( _Z ≥ at_<sup>_−_1</sup><sup>_/_2</sup> ) = 2Φ(<sup>¯</sup> _at_<sup>_−_1</sup><sup>_/_2</sup> )

_Ta_ has density


Check that this is consistent with _E_ exp( _−λTa_ ) = exp( _−a√_ 2 _λ_ ). Because _fTa_ ( _t_ ) _≈ t_<sup>_−_3</sup><sup>_/_2</sup> as _t →∞_ , _ETa_ = _∞_ .

Consider _Mt_ = sup0 _≤s≤t Bs_ . Then the event _{Mt ≥ a}_ equals the event _{Ta ≤ t}_ , so


by (28.4). Therefore, _Mt_ =d _|Bt|_ , for each 0 _< t < ∞_ , but they are not the same as processes.

We can use the Reflection Principle 28.1 formula to find the joint distribution of ( _Mt, Bt_ ). We know that _P_ ( _Ta ≤ t, Bt ≥ a_ + _b_ ) = _P_ ( _Bt ≥ a_ + _b_ ), so _P_ ( _Bt ≥ a_ + _b_ ) = _P_ ( _Mt ≥ a, Bt ≤ a − b_ ). Replace _b_ by _a − b_ .


(for _a >_ 0, _a > b_ ). Hence,


So, ( _Mt, Bt_ ) has joint density


_LECTURE 28. DECEMBER 1_

104


using _φ_<sup>_′_</sup> ( _x_ ) = _−xφ_ ( _x_ ).

_Special Cases of_ (28.5) _with t_ = 1.


The conditional density of _M_ 1 given _B_ 1 = 0 is


since


Therefore,


**Brownian bridge** ( _Bt_<sup>0</sup><sup>_,_0</sup><sup>_≤t≤_1)isdefinedas(</sup><sup>_Bt,_0</sup><sup>_≤t≤_1),conditionedon(</sup><sup>_B_1=0).</sup> Hence, _P_ ( _M_<sup>0</sup> _≥ a_ ) = exp( _−_ 2 _a_<sup>2</sup> ) for _M_<sup>0</sup> = sup0 _≤t≤_ 1 _Bt_<sup>0.</sup>

_Another Special Case: a_ = 0. Consider


Therefore,


_M_ 1 =d _|B_ 1 _|_ implies _fM_ 1(0) = 2 _φ_ (0). **Brownian meander** ( _Bt_<sup>(</sup><sup>_m_)</sup> _,_ 0 _≤ t ≤_ 1) is defined as BM conditioned on ( _Bt ≥_ 0 _,_ 0 _≤ t ≤_ 1). The calculation gives the distribution of _B_ 1<sup>(</sup><sup>_m_)</sup> .

---

[← November 29](29-november-29.md) · [Up: contents](index.md)
