---
title: September 6
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# September 6

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 Abstract Integration (MT Version)**

_Setting_ . Let _µ_ be a measure (finite or _σ_ -finite) on ( _S, S_ ).

Let _H_ + be the set of measurable _h_ : _S →_ [0 _, ∞_ ].

**Theorem 4.1** (Basic Theorem) **.** _There exists a unique map I_ : _H_ + _→_ [0 _, ∞_ ] _such that 1. I_ (1 _A_ ) = _µ_ ( _A_ ) _, ∀A ∈S_

_2. I_ ( _h_ 1 + _h_ 2) = _I_ ( _h_ 1) + _I_ ( _h_ 2) _, ∀hi ∈H_ + _3. I_ ( _ch_ ) = _cI_ ( _h_ ) _, ∀h ∈H_ + _, ∀c ≥_ 0 _4. If_ 0 _≤ hn ↑ h ∈H_ + _, then I_ ( _hn_ ) _↑ I_ ( _h_ ) _≤∞_

_Background_ . _h �→_ � _−∞∞_<sup>_h_(</sup><sup>_x_) d</sup><sup>_x_willbethecase</sup><sup>_S_= R1,</sup><sup>_µ_istheLebesguemeasure.</sup> In practice, we write


These are _definite integrals_ . We associate integrals with the area under curves. The area of a rectangle of height _c_ and length _µ_ ( _A_ ) is _cµ_ ( _A_ ) = _c_ � _S_<sup>1</sup><sup>_A_d</sup><sup>_µ_.</sup>

Steps:

1. Define _I_ (1 _A_ ) = _µ_ ( _A_ ).


3. For 0 _≤ h ≤ m_ , for _m_ a constant, we can write _h_ = lim _n hn_ , with _hn_ simple (2.9) and define _I_ ( _h_ ) = lim _n I_ ( _hn_ ).

4. For general _h ∈H_ +, set _hm_ = min( _h, m_ ), so _hm ↑ h_ . Define _I_ ( _h_ ) = lim _m↑∞ I_ ( _hm_ ).

_Note_ : Consider


13

_LECTURE 4. SEPTEMBER 6_

14

where _µ_ ( _A_ ) = 0. Here, _hm_ ( _s_ ) = min( _h_ ( _s_ ) _, m_ ) = _m_ 1 _A_ , so _I_ ( _hm_ ) = _m · µ_ ( _A_ ) = 0. Then


_Notation_ . (Almost Everywhere)

_h_ 1 = _h_ 2 a.e.

means _{s_ : _h_ 1( _s_ ) _̸_ = _h_ 2( _s_ ) _}_ has _µ_ -measure 0.

_Notation_ . For _x ∈_ R, _x_<sup>+</sup> = max( _x,_ 0) and _x_<sup>_−_</sup> = max( _−x,_ 0). Thus, _x_ = _x_<sup>+</sup> _− x_<sup>_−_</sup> , _|x|_ = _x_<sup>+</sup> + _x_<sup>_−_</sup> , and _|x − y| ≤|x|_ + _|y|_ .

**Definition 4.2.** A measurable _h_ : _S →_ R<sup>¯</sup> is **integrable** (w.r.t. _µ_ ) if � _S_<sup>_|h|_d</sup><sup>_µ<∞_.Forintegrable</sup><sup>_h_,</sup> define _I_ ( _h_ ) = _I_ ( _h_<sup>+</sup> ) _− I_ ( _h_<sup>_−_</sup> ) (but finite). **Lemma 4.3.** _Suppose h_ 1 _, h_ 2 _are integrable. 1. (Linearity) For c_ 1 _, c_ 2 _∈_ R _, h_ def= _c_ 1 _h_ 1+ _c_ 2 _h_ 2 _, then h is integrable and_ � _h_ d _µ_ = _c_ 1 � _h_ 1 d _µ_ + _c_ 2 � _h_ 2 d _µ. 2. If h_ 1 = 0 _a.e., then_ � _h_ 1 d _µ_ = 0 _. 3. If h_ 1 _≥_ 0 _a.e., then_ � _h_ 1 d _µ ≥_ 0 _. 4. If h_ 1 _≤ h_ 2 _a.e., then_ � _h_ 1 d _µ ≤_ � _h_ 2 d _µ. 5._ ��� _h_ d _µ_ �� _≤_ � _|h|_ d _µ._

_Proof._ 5.


### **4.2 Probability Theory (MT Version)**

_Freshman Version_ . A RV _X_ is a quantity with a range of possible values, the actual value of which is determined somehow by chance.

_P_ ( _X ≤_ 4) is “the chance it turns out that _X ≤_ 4”.

A **probability space** is


Events _A ∈F_ have probabilities _P_ ( _A_ ).

A **random variable** (RV) is a measurable function _X_ : Ω _→_ ( _S, S_ ) or often R.

For a measurable set _B ∈S_ , _{ω_ : _X_ ( _ω_ ) _∈ B}_ is an event in _F_ and so has a probability

_P_ ( _{ω_ : _X_ ( _ω_ ) _∈ B}_ ) = _P_ ( _X ∈ B_ )

_LECTURE 4. SEPTEMBER 6_

15

A given RV _X_ : Ω _→_ ( _S, S_ ) has a **distribution** (or **law** ) _µ_ , defined by _µ_ ( _B_ ) = _P_ ( _X ∈ B_ ). Given a PM _P_ and the RV _X_ , we obtain the push-forward PM _µ_ .

_Notation_ . By example: If _X_ , _Y_ , _Z_ are R-valued RVs, we define **almost surely** (a.s.):


Given R-valued RVs _Xn_ , _X_ ,

_Xn → X_ a.s. means _P_ ( _{ω_ : _Xn_ ( _ω_ ) _→ X_ ( _ω_ ) as _n →∞}_ ) = 1

_Note_ : Given arbitrary R-valued _Xn_ , 1 _≤ n < ∞_ , we can deifne _X_<sup>_∗_</sup> = lim sup _n Xn_ ( _X_<sup>_∗_</sup> ( _ω_ ) = lim sup _n→∞ Xn_ ( _ω_ )) and _X_<sup>_∗_</sup> is a RV.

Take a RV _Y_ : (Ω _, F, P_ ) _→_ R. Then


provided _E|Y | ≡_ �Ω<sup>_|Y |_d</sup><sup>_P< ∞_.“YisΩ-integrable.”</sup>

#### **4.2.1 “Change of Variable” Lemmas**

Consider _X_ : (Ω _, P_ ) _→_ ( _S, S_ ) and _h_ : ( _S, S_ ) _→_ R.

**Lemma 4.4.** _If h_ ( _X_ ) _is integrable, then Eh_ ( _X_ ) = � _S_<sup>_h_d</sup><sup>_µforµ_=</sup><sup>_distributionofX._</sup>

**Lemma 4.5.** _If ν is a PM on_ R _with density f , then_ �R<sup>_h_d</sup><sup>_ν_=</sup> � _−∞∞_<sup>_h_(</sup><sup>_x_)</sup><sup>_f_(</sup><sup>_x_) d</sup><sup>_x,providedhisν-_</sup> _integrable._

_Proof._ Consider the collection of _h_ for which the stated equality is true.

1. Consider _h_ = 1 _B_ , _B ∈S_ .


2. Consider _h_ = 1 _B_ , _B ⊆_ R.


Go through the steps of the sketch proof of 4.1. Both sides of the equalities are integrals. Then:

true for 1 _B_ = _⇒_ true for simple _h_ = _⇒_ true for bounded measurable _h_ = _⇒_ true for integrable _h_ See the textbook: “monotone class theorem”.

We can combine 4.4 and 4.5.

**Lemma 4.6.** _Suppose X is_ R _-valued, and its distribution has density f . Then Eh_ ( _X_ ) = � _h_ ( _x_ ) _f_ ( _x_ ) d _x, provided that h_ ( _X_ ) _is integrable._

_LECTURE 4. SEPTEMBER 6_

16


etc.

## **Lecture 5**

---

[← September 1](05-september-1.md) · [Up: contents](index.md) · [September 8 →](07-september-8.md)
