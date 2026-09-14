---
title: January 31
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# January 31

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **5.1 Characteristic Function Proofs**

**Convergence Theorem** : _Xn_ has CF _φn_ . If _φn_ ( _t_ ) _→ φ∞_ ( _t_ ) as _n →∞_ , for each _t_ , if _φ∞_ ( _t_ ) is the CF of some _X∞_ , then _Xn −→_ d _X∞_ .

Suppose _E|X|_<sup>_n_</sup> _< ∞_ . Then


**Theorem 5.1** (Weak Law of Large Numbers) **.** _Let X_ 1 _, X_ 2 _, . . . be IID with EX_ = _θ, Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi,_</sup> _then Sn/n → θ in distribution, and hence convergence in probability._

_Proof._ The PM _σθ_ has CF _e_<sup>_iθt_</sup> . It is enough to prove _φSn/n_ ( _t_ ) _→ e_<sup>_iθt_</sup> as _n →∞_ , for a fixed _t_ . Since _φSn_ ( _t_ ) = ( _φX_ ( _t_ ))<sup>_n_</sup> ,


If _zn → z ∈_ C, then (1 + _zn/n_ )<sup>_n_</sup> _→ e_<sup>_z_</sup> . It is enough to prove


The bound for _n_ = 1 gives _|φX_ ( _s_ ) _−_ (1 + _isθ_ ) _|_ = _o_ ( _|s|_ ). Apply the bound with _s_ = _t/n_ . Then, we know


_Remarks_ . The proof shows that

_φ_<sup>_′_</sup> _X_<sup>(0) =</sup><sup>_θ_</sup>


is sufficient for the WLLN 5.1.

_Fact_ . In fact, (5.1) is also necessary. The property _EX_ = _θ_ implies _φ_<sup>_′_</sup> _X_<sup>(0) =</sup><sup>_θ_,but</sup><sup>_not_conversely.</sup>

20

_LECTURE 5. JANUARY 31_

21

### **5.2 Central Limit Theorems**

**Theorem 5.2** (IID Central Limit Theorem) **.** _Let_ ( _Xi, i ≥_ 1) _be IID, EX_ = _µ,_ var( _X_ ) = _σ_<sup>2</sup> _< ∞. Then,_


_Proof._ WLOG take _µ_ = 0. It is enough to show


Also,


It is enough to show _n_ ( _φX_ ( _t/_<sup>_√_</sup> _<u>n</u>_ <u>)</u> _−_ 1) _→ σ_<sup>2</sup> _t_<sup>2</sup> _/_ 2. The bound for _n_ = 2 and _EX_ = 0 is

Then, with _s_ = _t/_<sup>_√_</sup> _<u>n</u>_ <u>,</u>

**Theorem 5.3** (Lindeberg’s Theorem) **.** _For each n, let Xn,_ 1 _, Xn,_ 2 _, . . . , Xn,n be independent, EXn,m_ = 0 _,_ var _Xn,m_ = _σn,m_<sup>2</sup><sup>_< ∞.WriteSn_= �</sup> _m_<sup>_n_</sup> =1<sup>_Xn,m,σ_</sup> _n_<sup>2= �</sup><sup>_n_</sup> _m_ =1<sup>_σ_</sup> _n,m_<sup>2= var(</sup><sup>_Sn_)</sup><sup>_,ESn_= 0</sup><sup>_.Suppose_</sup> _(i) σn_<sup>2</sup><sup>_→σ_2</sup><sup>_< ∞asn →∞,_</sup> _(ii)_ lim _n→∞_ � _nm_ =1<sup>_E_[</sup><sup>_X_</sup> _n,m_<sup>21</sup> ( _|Xn,m|>ε_ )<sup>]=0</sup><sup>_,foreachε>_0</sup><sup>_.Thisisknownasthe_</sup><sup>**_Lindebergcondi-_**</sup> **_tion_** _: UAN = uniformly asymptotically negligible. Then, Sn −→_ d Normal(0 _, σ_ 2) _._

_Proof. φn,m_ ( _t_ ) is the CF of _Xn,m_ . The more precise bound is


_Cheap_ : If _|x| ≤ ε_ , then _|x|_<sup>3</sup> _≤ εx_<sup>2</sup> .

_LECTURE 5. JANUARY 31_

22


_LECTURE 5. JANUARY 31_

23

_Proof. |z_ 1 _z_ 2 _· · · ziwi_ +1 _· · · wn − z_ 1 _· · · zi_ +1 _wi_ +2 _· · · wn|_ = _|_ ( _zi_ +1 _− wi_ +1) _· A| ≤|zi_ +1 _− wi_ +1 _|,_ where _|A| ≤_ 1.

**Lemma 5.5.** _Let an,m ∈_ R _. If (i)_<sup>�</sup> _m_<sup>_an,m→aasn →∞,_</sup> _(ii)_<sup>�</sup> _m_<sup>_a_2</sup> _n,m_<sup>_→_0</sup><sup>_._</sup> _Then,_<sup>�</sup><sup>_n_</sup> _m_ =1<sup>(1</sup><sup>_−an,m_)</sup><sup>_→e−a._</sup>

_Proof._ We know that max _m|an,m| →_ 0 by (ii). Since _|_ log(1 _− x_ ) + _x| ≤ Cx_<sup>2</sup> for _|x| ≤_ 1 _/_ 2,


Hence, log<sup>�</sup><sup>_n_</sup> _m_ =1<sup>(1</sup><sup>_−an,m_)</sup><sup>_→−a_.</sup>


This is the previous theorem 5.3 applied with _X_<sup>ˆ</sup> _n,m_ = _Xn,m/sn_ . Now, it looks more like the IID version.

## **Lecture 6**

---

[← January 26](06-january-26.md) · [Up: contents](index.md) · [February 2 →](08-february-2.md)
