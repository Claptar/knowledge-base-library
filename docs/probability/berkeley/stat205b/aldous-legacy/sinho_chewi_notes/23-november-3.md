---
title: November 3
source: https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# November 3

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **21.1 “Converge or Oscillate Infinitely”**

**Lemma 21.1.** _Let_ ( _Xn_ ) _be a MG such that |Xn − Xn−_ 1 _| ≤ K ∀n. Then P_ ( _C ∪ D_ ) = 1 _for the events_


_Proof._ WLOG _X_ 0 = 0. Fix _L >_ 0. Define _T_ = min _{n_ : _Xn < −L}_ . The stopped process ( _XT ∧n, n ≥_ 0) is a MG which is always at least _−L − K_ . By the (positive super-MG) convergence theorem, _XT ∧n_ converges to some finite limit a.s. as _n →∞_ . This implies _{_ inf _n Xn > −L}_ = _{T_ = _∞} ⊆ C_ . This is true for all _L_ , so let _L →∞_ . Therefore,


The same argument applied to ( _−Xn_ ) gives


so we are done because ( _A_ 1 _∩ A_ 2)<sup>_c_</sup> = _D_ .

### **21.2 Conditional Borel-Cantelli**

**Lemma 21.2** (Conditional Borel-Cantelli Lemma) **.** _Consider events_ ( _An_ ) _adapted to_ ( _Fn_ ) _. Define Bn_ =<sup>�</sup> _m≥n_<sup>_AmandB_= �</sup> _n_<sup>_Bn_=</sup><sup>_{Aninf.often}.Then_</sup> _(a) {An inf. often}_ = _{_<sup>�</sup><sup>_∞_</sup> _n_ =1<sup>_P_(</sup><sup>_An | Fn−_1) =</sup><sup>_∞}a.s._</sup> _(b) P_ ( _Bn_ +1 _| Fn_ ) _→_ 1 _B a.s. as n →∞._

_B_ 1 = _B_ 2 a.s. means _P_ ( _B_ 1 _△ B_ 2) = 0.

78

_LECTURE 21. NOVEMBER 3_

79

_Proof._ (b) Consider _K < n_ . Then _B ⊆ Bn ⊆ BK_ and _P_ ( _B | Fn_ ) _≤ P_ ( _Bn_ +1 _| Fn_ ) = _P_ ( _Bn_ +1 _| Fn_ ) _≤ P_ ( _BK | Fn_ )

Take the limit as _n →∞_ .


Let _K ↑∞_ . Then 1 _BK ↓_ 1 _B_ . (a) Consider _Xn_ =<sup>�</sup><sup>_n_</sup> _m_ =1<sup>(1</sup><sup>_Am−P_(</sup><sup>_Am | Fm−_1)),whichisaMG,and</sup><sup>_|Xn_+1</sup><sup>_−Xn|≤_1.Then21.1</sup> implies that _P_ ( _C ∪ D_ ) = 1. We want to prove


Observe that _Xn_ =<sup>�</sup><sup>_n_</sup> _m_ =1<sup>1</sup><sup>_A_</sup> _m_<sup>_−_�</sup> _m_<sup>_n_</sup> =1<sup>_P_(</sup><sup>_Am | Fm−_1).Onevent</sup><sup>_D_,bothsumsare</sup><sup>_∞_.Onevent</sup> _C_ , either both sums are finite or both sums equal _∞_ .

### **21.3 “Product” MGs**

#### **21.3.1 Convergence for “Multiplicative” MGs**

**Theorem 21.3** (Kakutani’s Theorem) **.** _Take_ ( _Xi, i ≥_ 1) _to be independent, Xi >_ 0 _, EXi_ = 1 _. We know that Mn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_XiisaMGandsoMn_</sup> _−−→a.s. M∞, with EM∞ ≤_ 1 _. Then properties (i) to (v) below are equivalent: (i) EM∞_ = 1 _. (ii) Mn → M∞ in L_<sup>1</sup> _. (iii)_ ( _Mn, n ≥ i_ ) _is UI. (iv) Set ai_ = _EXi_<sup>1</sup><sup>_/_2</sup> _and note that_ 0 _≤ ai ≤_ 1 _._<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_ai>_0</sup><sup>_._</sup> _(v)_<sup>�</sup> _i_<sup>(1</sup><sup>_−ai_)</sup><sup>_< ∞._</sup>

_Proof._ Conditions (i), (ii), (iii) are equivalent by the _L_<sup>1</sup> MG convergence theorem.

Conditions (iv), (v) are equivalent by calculus. Use 1 _− x_ + _x_<sup>2</sup> _≥ e_<sup>_−x_</sup> _≥_ 1 _− x_ for small _x >_ 0. Suppose (iv) holds. Consider


which is a MG.


_LECTURE 21. NOVEMBER 3_

80

Apply the Doob _L_<sup>2</sup> maximal inequality.


Note that _Mn ≤ Nn_<sup>2since</sup><sup>_Mn_=</sup><sup>_N_</sup> _n_<sup>2</sup> � _ni_ =1<sup>_a_</sup> _i_<sup>2.Therefore,</sup><sup>_E_[sup</sup> _n_<sup>_Mn_]</sup><sup>_≤_(4</sup><sup>_K_)2</sup><sup>_<∞_.Thisimpliesthat</sup> ( _Mn, n ≥_ 1) is UI. If _Z ≥_ 0, _EZ < ∞_ , the family _{X_ : 0 _≤ X ≤ Z}_ is UI. This gives (iii).

Suppose that (iv) is false, so<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_ai_= 0.FortheMG(</sup><sup>_Nn_),wehave</sup><sup>_Nn→N∞_a.s.Wemusthave</sup>


Since the denominator is 0, then<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_X_</sup> _i_<sup>1</sup><sup>_/_2</sup> = _M∞_<sup>1</sup><sup>_/_2</sup> = 0 a.s., so (i) fails.

#### **21.3.2 Likelihood Ratios (Absolute Continuity of Infinite Product Measures)**

Given densities _fi,_ 1 _≤ i < ∞_ and _gi,_ 1 _≤ i < ∞_ , assume _fi >_ 0 and _gi >_ 0. Take Ω= R<sup>_∞_</sup> with _X_ ( **_ω_** ) = _ωi_ . Work with _P_ , the product measure where the ( _Xi_ ) are independent with densities _fi_ . Consider _Q_ , where the ( _Xi_ ) have densities _gi_ . The “likelihood ratio”


is the Radon-Nikodym density


( _Qn_ is the probability measure with corresponding density _f_ 1 _⊗ f_ 2 _⊗· · · ⊗ fn_ .)

_Know_ . ( _Ln, n ≥_ 1) is a MG w.r.t. _P_ .

Suppose that ( _Ln, n ≥_ 1) is UI. Then _Ln → L∞_ in _L_<sup>1</sup> and _Ln_ = _E_ [ _L∞ | Fn_ ]. What this means, from the definition of the R-N density, is


so _L∞_ is the R-N density


on R<sup>_∞_</sup> . Therefore, _Q ≪ P_ .

Similarly, if _Q ≪ P_ , then we can prove ( _Ln, n ≥_ 1) is UI. So _Q ≪ P ⇔_ ( _Ln, n ≥_ 1) is UI _⇔_<sup>�</sup> _i_<sup>(1</sup><sup>_−ai_)</sup><sup>_< ∞_.</sup>


(by algebra). Our condition is

_∞_


_LECTURE 21. NOVEMBER 3_

81

“ _fi_ and _gi_ become close for large _i_ .”

We know that for _f̸ ≡ g_ , then _Q_ and _P_ are singular.

## **Lecture 22**

---

[← November 1](22-november-1.md) · [Up: contents](index.md) · [November 8 →](24-november-8.md)
