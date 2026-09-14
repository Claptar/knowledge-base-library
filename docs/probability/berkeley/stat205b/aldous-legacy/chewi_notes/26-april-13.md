---
title: April 13
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# April 13

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **24.1 Donsker’s Invariance Principle**

_Setting_ . ( _Xi,_ 1 _≤ i < ∞_ ) are IID, E _X_ 1 = 0, E _X_ 1<sup>2= 1,</sup><sup>_Sn_= �</sup><sup>_n_</sup> _i_ =1<sup>_Xi_.</sup><sup>_S_(</sup><sup>_t_)isthelinearinterpolation.</sup>


“As _n →∞_ , the process _Sn_<sup>_∗_convergesindistributiontoBM.”</sup>

(Last Class) Given dist( _X_ 1) and standard BM ( _B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ), there exists a stopping time _T_ 1 with _B_ ( _T_ 1) =d _X_ 1 and E _T_ 1 = 1.

Use the Strong Markov Property. If _B_<sup>˜</sup> ( _u_ ) def= _B_ ( _T_ 1 + _u_ ) _− B_ ( _T_ 1), then the process ( _B_<sup>˜</sup> ( _u_ ) _,_ 0 _≤ u < ∞_ ) is distributed as BM independent of _F_ ( _T_ 1). There exists a stopping time _T_ 2 for _B_<sup>˜</sup> such that _B_<sup>˜</sup> ( _T_ 2) =d _X_ 2 and is independent of _B_ ( _T_ 1). Now, ( _B_ ( _T_ 1) _, B_ ( _T_ 1 + _T_ 2)) = (d _X_ 1 _, X_ 1 + _X_ 2).

_Conclusion_ : There exist IID ( _T_<sup>˜</sup> _i,_ 1 _≤ i < ∞_ ) such that


where _Tk_ =<sup>�</sup><sup>_k_</sup> _i_ =1<sup>_T_˜</sup><sup>_i_.</sup>

_Trick_ : Work with this construction of _S_ ( _t_ ) and _Sn_<sup>_∗_(</sup><sup>_t_).</sup>

_Idea_ : _Sk ≈ B_ ( _k_ ) to first-order.

**Proposition 24.1.**


Why?


by the SLLN for the ( _Ti_ ).

93

_LECTURE 24. APRIL 13_

94

_Proof._ Set


_Wn_ ( _t_ ) is distributed as BM. Study every _An_ def= _{∃_ 0 _≤ t ≤_ 1 _|Sn_<sup>_∗_(</sup><sup>_t_)</sup><sup>_−Wn_(</sup><sup>_t_)</sup><sup>_|>ε}_.Set</sup><sup>_k_=</sup><sup>_k_(</sup><sup>_t_)such</sup> that


Note that


If an average is _> ε_ , then one of the items _> ε_ . Rewrite (24.1):

Then,

Repeat the “continuity of BM” argument.

_Claim_ : Take _δ >_ 0. If _A_<sup>_∗_</sup> _n_<sup>,then</sup>

or


Need to show: P( _Dn_ ( _δ_ )) _→_ 0 as _n →∞_ , for fixed _δ >_ 0. By the SLLN,


By 24.2,


In _Dn_ ( _δ_ ), we have


_LECTURE 24. APRIL 13_

95


**Lemma 24.2** (Deterministic Lemma) **.** _If then_


Consider the metric space ( _C_ [0 _,_ 1] _, d_ ) on the space of continuous functions _f_ : [0 _,_ 1] _→_ R, with


We have seen a little about “weak convergence on metric spaces”.

Easy general fact, applied to our setting: If _Sn_<sup>_∗_,</sup><sup>_W ∗_</sup> _n_<sup>,and</sup><sup>_W_(</sup><sup>_W_istheBMprocess)satisfy</sup> (i) _d_ ( _Sn_<sup>_∗, W_</sup> _n_<sup>_∗_)</sup><sup>_→_0inprobabilityas</sup><sup>_n →∞_,</sup> (ii) _Wn_<sup>_∗_</sup> =d _W ∀n_ , then _Sn_<sup>_∗_</sup> _−→_ d _W_ .

Here, we have


and P( _d_ ( _Wn_<sup>_∗, S_</sup> _n_<sup>_∗_)</sup><sup>_> ε_)</sup><sup>_→_0</sup><sup>_∀ε_:24.1says</sup><sup>_d_(</sup><sup>_W ∗_</sup> _n_<sup>_, S_</sup> _n_<sup>_∗_)</sup><sup>_→_0inprobability.ThisisDonsker’sInvariancePrinci-</sup> ple. _Sn_<sup>_∗→W_indistributionon</sup><sup>_C_[0</sup><sup>_,_1].</sup>

As a general “weak convergence” fact, applied to Donsker’s Theorem:

_LECTURE 24. APRIL 13_

96

**Corollary 24.3.** _If ψ_ : _C_ [0 _,_ 1] _→_ R _is continuous, or more generally, if_ P( _W ∈Dψ_ ) = 0 _for Dψ_ def= _{f_ : _ψ is not continuous at f },_

_then ψ_ ( _Sn_<sup>_∗_)</sup> _−→_ d _ψ_ ( _W_ ) _on_ R _._

**Example 24.4.** _ψ_ ( _f_ ) def= sup0 _≤t≤_ 1 _f_ ( _t_ ). This _is_ everywhere continuous because


**Example 24.5.** _ψ_ ( _f_ ) = Leb _{t ∈_ [0 _,_ 1] : _f_ ( _t_ ) _>_ 0 _}_ . If we take


but _fn → f_ , so _ψ_ is not continuous. If _f_ satisfies


then _ψ is_ continuous at _f_ . If _fn → f_ , then 1( _fn>_ 0) _→_ 1( _f>_ 0) outside _{f_ = 0 _}_ . If _fn → f_ and _f_ satisfies (24.3), then 1( _fn_ ( _t_ ) _>_ 0) _→_ 1( _f_ ( _t_ ) _>_ 0) a.e. = _⇒_ �01<sup>1(</sup><sup>_fn_(</sup><sup>_t_)</sup><sup>_>_0) d</sup><sup>_t →_</sup> �01<sup>1(</sup><sup>_f_(</sup><sup>_t_)</sup><sup>_>_0) d</sup><sup>_t_,so</sup><sup>_ψ_(</sup><sup>_fn_)</sup><sup>_→ψ_(</sup><sup>_f_).</sup> _Dψ_ = _{f_ : Leb _{t_ : _f_ ( _t_ ) = 0 _} >_ 0 _}._

To use 24.3, we need to show P(Leb _{t_ : _W_ ( _t_ ) = 0 _} >_ 0) = 0. It is enough to show


but we have �01<sup>P(</sup><sup>_Wt_= 0) d</sup><sup>_t_= 0becauseP(</sup><sup>_Wt_= 0) = 0for</sup><sup>_t >_0.</sup>

**Example 24.6.**

_Exercise_ : If _f_ has the property


then _ψ_ is continuous at _f_ . To apply 24.3, we need to show P( _B_ has property (24.4)) = 1.

## **Lecture 25**

---

[← April 11](25-april-11.md) · [Up: contents](index.md) · [April 25 →](27-april-25.md)
