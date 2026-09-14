---
title: October 4
source: https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# October 4

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **12.1 Large Deviations Theorem (Durrett)**

If _an ∼ ce_<sup>_βn_</sup> as _n →∞_ , then (1 _/n_ ) log _an → β_ , where _β_ is the asymptotic growth (decrease) rate. Today, _β <_ 0.

_Assumptions_ . Let ( _Xi_ ) be IID, with _Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi_,</sup><sup>_EX_=</sup><sup>_µ_.</sup> Fix _a > µ_ , _P_ ( _X ≥ a_ ) _>_ 0. Define _φ_ ( _θ_ ) = _E_ exp( _θX_ ), and assume _θ_<sup>_∗_</sup> = sup _{θ_ : _φ_ ( _θ_ ) _< ∞} >_ 0.

Consider _P_ ( _Sn/n ≥ a_ ). We know that _P_ ( _Sn/n ≥ a_ ) _→_ 0 as _n →∞_ by the WLLN. How fast? Our general LD inequality gives


Therefore,


On the other hand,


This implies:


**Theorem 12.1.** _As n →∞,_


There are three steps in the proof.

> _•_ analysis of _φ_ ( _θ_ )

45

_LECTURE 12. OCTOBER 4_

46

- tilting lemma

- put it together

**Lemma 12.2.** _φ_<sup>_′_</sup> (0+) = _µ_

We believe this because


Taking _θ_ = 0, _φ_<sup>_′_</sup> (0+) = _EX_ .


By hypothesis, there exists _θ_ 1 such that _Ee_<sup>_θ_1</sup><sup>_X_</sup> _< ∞_ . Choose _θ_ 0 _< θ_ 1, so that _E_ [ _|X|_ max(1 _, e_<sup>_θ_0</sup><sup>_X_</sup> )] _< ∞_ . Now, the RVs are bounded by (12.2). Apply the DCT.

The same argument applies to


**Lemma 12.3.** _φ_<sup>_′_</sup> (0+) = _µ, and for_ 0 _< θ < θ_<sup>_∗_</sup> _,_


Suppose _X_ is discrete. Fix _θ_ . Define a distribution for _X_<sup>ˆ</sup> by


Fix _θ_ . Then


_LECTURE 12. OCTOBER 4_

47

Also,


and


For general _X_ , define the distribution of _X_<sup>ˆ</sup> by the Radon-Nikodym density


**Lemma 12.4** (Tilting Lemma) **.** _and_


Now, we study _G_ ( _θ_ ) = log _φ_ ( _θ_ ) _− aθ_ .


It is easy to see that _G_ ( _θ_ ) _→∞_ as _θ →∞_ . _G_ is strictly convex.

Find inf _θ G_ ( _θ_ ) by solving _G_<sup>_′_</sup> ( _θ_ ) = 0, or


**Case 1** . There exists a solution _θa ∈_ (0 _, θ_<sup>_∗_</sup> ) of the equation _φ_<sup>_′_</sup> ( _θ_ ) _/φ_ ( _θ_ ) = _a_ .

**Bad Case** . Take the density _f_ ( _x_ ) _∼ x_<sup>_−_2</sup> _e_<sup>_−λx_</sup> as _x →∞_ . Then _φ_ ( _λ_ ) _< ∞_ , but _φ_ ( _λ_ +) = _∞_ . Assume case 1. Choose _θ ∈_ ( _θa, θ_<sup>_∗_</sup> ). Consider the tilted distribution _X_<sup>ˆ</sup> = _X_<sup>ˆ</sup> _θ_ .


because _EX_<sup>ˆ</sup> _θ > a_ and _EX_<sup>ˆ</sup> _θ ↓ a_ as _θ ↓ θa_ . (Check!)

_LECTURE 12. OCTOBER 4_

48

Fix _b > EX_<sup>ˆ</sup> _θ_ . The trick is to apply the WLLN to the tilted ( _X_<sup>ˆ</sup> _i_ ). Since


we have _PP_ <u>((</u> _XX_<sup>ˆ</sup> 11 == _x x_ 11 _<u>,, . . . , X . . . ,</u> X_<sup>ˆ</sup> _nn_ == _x xnn_ ))<sup>=</sup><sup>_eθ_</sup> _φ_ which gives _P_ <u>(</u> _S_<sup>ˆ</sup> _n_ = _s_ <u>)</u> _e_<sup>_θs_</sup> _P_ ( _Sn_ = _s_ )<sup>=</sup> _φ_<sup>_n_</sup> ( _θ_ ) Therefore, _PP_ <u>((</u> _<u>yy</u>_ 11 _≤≤ SS_<sup>ˆ</sup> _nn ≤≤_ _<u>yy</u>_ 22))<sup>_≤_</sup> _φ_<sup>_enθy_</sup> ( _θ_<sup>2</sup> )


with _y_ 1 = _an_ , _y_ 2 = _bn_ , so


Hence,


(Let _θ ↓ θa_ . Since this is true for all _b > a_ , let _b ↓ a_ .)

### **12.2 Conditional Distributions**

_Undergraduate Version_ . Consider ( _X, Y_ ):

discrete continuous _p_ ( _x, y_ ) = _P_ ( _X_ = _x, Y_ = _y_ ) _f_ ( _x, y_ ) joint density marginal distribution _pX_ ( _x_ ) = _P_ ( _X_ = _x_ ) _fX_ ( _x_ ) = density of _X_

conditional distribution of _Y_ given _X_ = _x_ conditional density of _Y_ given _X_ = _x pY | X_ ( _y | x_ ) = _P_ ( _Y_ = _y | X_ = _x_ ) _y �→ fY | X_ ( _y | x_ ) _p_ ( _x, y_ ) = _pX_ ( _x_ ) _pY | X_ ( _y | x_ ) _f_ ( _x, y_ ) = _fX_ ( _x_ ) _fY | X_ ( _y | x_ )

## **Lecture 13**

---

[← September 29](13-september-29.md) · [Up: contents](index.md) · [October 6 →](15-october-6.md)
