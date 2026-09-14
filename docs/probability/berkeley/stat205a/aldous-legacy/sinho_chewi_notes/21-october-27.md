---
title: October 27
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# October 27

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **19.1 Optional Sampling Theorem**

Last class: let ( _Xn_ ) be a sub-MG w.r.t. ( _Fn_ ). ( _Hn_ ) is a predictable process which is bounded. Define _Y_ = _H · X_ by _Y_ 0 = 0, ∆<sup>_Y_</sup> _n_<sup>=</sup><sup>_Hn_∆</sup><sup>_X_</sup> _n_<sup>.Then(</sup><sup>_Yn_)isasub-MG,provided</sup><sup>_Hn≥_0.</sup><sup>_Hn_isthenumberofshares</sup> held on day _n_ .

The sub-MG property is


which implies that _EXn_ is increasing.

**Corollary 19.1.** _Let_ ( _Xn_ ) _be a sub-MG. Let_ 0 _≤ T_ 1 _≤ T_ 2 _≤ t_ 0 _be stopping times. Then E_ [ _XT_ 2 _| FT_ 1] _≥ XT_ 1

_Proof._ Fix an event _A ∈FT_ 1. The strategy is: “If _A_ happens, buy 1 share at _T_ 1 and sell at _T_ 2. If _A_ does not happen, do nothing.” _Hn_ = 1 _A_ 1( _T_ 1 _<n≤T_ 2). We want to check that _Hn_ is predictable. In other words, we want to check _A∩{T_ 1 _< n ≤ T_ 2 _} ∈Fn−_ 1. We can write _{T_ 1 _< n ≤ T_ 2 _}_ as _{T_ 1 _≤ n−_ 1 _}\{T_ 2 _≤ n−_ 1 _}_ , because _T_ 2 _≥ T_ 1, so we have ( _A ∩{T_ 1 _≤ n −_ 1 _}_ ) _\_ ( _A ∩{T_ 2 _≤ n −_ 1 _}_ ). By the definition of _A ∈FT_ 1, the two events are in _Fn−_ 1.

So, ( _Yn_ ) is a sub-MG. _Yn_ = ( _XT_ 2 _∧n − XT_ 1 _∧n_ )1 _A_ , where _a ∧ b_ = min( _a, b_ ). The sub-MG property implies that _EYt_ 0 _≥ EY_ 0 = 0. We have shown


_Fact_ . If _E_ [ _Z_ 1 _A_ ] _≥_ 0 _∀A ∈G_ , then _E_ [ _Z | G_ ] _≥_ 0 a.s. Therefore,


“OST” is the **Optional Sampling Theorem** .

**Theorem 19.2** (Basic Version of OST) **.** _If_ ( _Xn_ ) _is a (sub-)MG,_ 0 = _T_ 0 _≤ T_ 1 _≤ T_ 2 _≤· · · are stopping times, if Ti ≤ ti (a constant), then_ ( _XTi, i_ = 0 _,_ 1 _,_ 2 _, . . ._ ) _is a (sub-)MG w.r.t._ ( _FTi, i_ = 0 _,_ 1 _,_ 2 _, . . ._ ) _._

In particular, _EXTi ≥ EX_ 0 for a sub-MG and _EXTi_ = _EX_ 0 for a MG, and _EXT_ 2 _≥ EXT_ 1 if _T_ 2 _≥ T_ 1. There are many other versions without the restriction that _T ≤ t_ 0.

72

_LECTURE 19. OCTOBER 27_

73

Write _XN_<sup>_∗_=max(</sup><sup>_X_0</sup><sup>_, X_1</sup><sup>_, . . . , XN_).Weknowthat</sup><sup>_P_(</sup><sup>_X_</sup> _N_<sup>_∗≥x_)</sup><sup>_≤_�</sup><sup>_N_</sup> _n_ =0<sup>_P_(</sup><sup>_Xn≥x_)isalwaystrue.Ifthe</sup> ( _Xi_ ) are independent, then _P_ ( _XN_<sup>_∗≥x_) = 1</sup><sup>_−_�</sup><sup>_N_</sup> _n_ =0<sup>_P_(</sup><sup>_Xn< x_).WithMGs,wecangetbetterboundsthan</sup> the former.

### **19.2 Maximal Inequalities**

**Lemma 19.3.** _Let_ ( _Xn_ ) _be a super-MG, Xn ≥_ 0 _a.s. Write X_<sup>_∗_</sup> = sup _n Xn, so XN_<sup>_∗↑X∗asN→∞._</sup> _Then P_ ( _X_<sup>_∗_</sup> _≥ λ_ ) _≤ EX_ 0 _/λ, for all λ >_ 0 _._

_Proof._ Define _T_ = min _{n_ : _Xn ≥ λ}_ . Apply the OST 19.2 to 0 and _T ∧ N_ . Then


This implies


Let _N →∞_ . Then we only have Apply this to _λj ↑ λ_ to obtain (Check this.)


Note that

max _A_<sup>_E_[</sup><sup>_Y_1</sup><sup>_A_] =</sup><sup>_E_[</sup><sup>_Y_1(</sup><sup>_Y ≥_0)] =</sup><sup>_E_max(</sup><sup>_Y,_0) =</sup><sup>_EY_+</sup> which implies that _E_ [ _Y_ 1 _A_ ] _≤ EY_<sup>+</sup> .

_Proof._ Let _T_ = min _{n_ : _Xn ≥ λ}_ . Apply the OST 19.2 to _T ∧ N_ and _N_ : _EXT ∧N ≤ EXN_ . Therefore, _EXT_ 1( _T ≤N_ ) + _EXN_ 1( _T >N_ ) _≤ EXN_ 1( _T ≤N_ ) + _EXN_ 1( _T >N_ ) _XT ≥ λ_ , so


**Corollary 19.5.** _If_ ( _Xn_ ) _is a MG, then (because Yn_ = _|Xn| is also a sub-MG)_


_LECTURE 19. OCTOBER 27_

74


_These are two different bounds for the same quantity._

Use the notation


_Proof._


by the Cauchy-Schwarz Inequality. The inequality is saying _a ≤_ 2 _√ba_ , so _a ≤_ 4 _b_ . There is also a special case when _a_ = _∞_ .

If we use the H¨older Inequality instead of the Cauchy-Schwarz Inequality, then we obtain


for 1 _< p < ∞_ . This is _not_ true for _p_ = 1.

**Example 19.7.** Let _X_ 0 = 1 and consider a simple symmetric RW on Z, stopping at

_T_ = min _{n ≥_ 1 : _Xn_ = 0 _}_ ( _Xn_ ) is a MG. _EXn_ = 1 _∀n_ . Also, _XN_<sup>_∗↑X∗_=sup</sup> _n_<sup>_Xn_.Elementaryfact:</sup><sup>_P_(</sup><sup>_X∗≥m_)=1</sup><sup>_/m_.</sup> Therefore, _EX_<sup>_∗_</sup> = _∞_ , so _EXN_<sup>_∗↑∞_,but</sup><sup>_EXN_= 1</sup><sup>_∀N_.</sup>

## **Lecture 20**

---

[← October 25](20-october-25.md) · [Up: contents](index.md) · [November 1 →](22-november-1.md)
