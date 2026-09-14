---
title: September 27
source: https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# September 27

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **10.1 Truncation**

**Corollary 10.1** (SLLN) **.** _Take IID_ ( _Xi_ ) _, where EX_<sup>+</sup> = _∞, EX_<sup>_−_</sup> _< ∞ (X_ = _X_<sup>+</sup> _− X_<sup>_−_</sup> _). Let Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi.ThenSn/n →∞a.s._</sup>

_Proof._ Fix a large _B < ∞_ . Define _Yi_ = _Xi_ 1( _Xi≤B_ ). Then the ( _Yi_ ) are IID, with _E|Yi| < ∞_ , so we can apply the SLLN to ( _Yi_ ).

Then


for each _B_ . As _B ↑∞_ , then _E_ [ _X_ 1( _X≤B_ )] _↑−EX_<sup>_−_</sup> + _EX_<sup>+</sup> = + _∞_ . Therefore, letting _B ↑∞_ ,


### **10.2 Renewal SLLN**

If we travel halfway at 60 mph and halfway at 20 mph, the average speed is 30 mph. To see this, traveling 120 miles takes 1 hour + 3 hours = 4 hours.

**Lemma 10.2** (Deterministic Lemma) **.** _Consider real numbers s_ 0 = 0 _, sn/n → a ∈_ (0 _, ∞_ ) _as n →∞. Let h_ ( _t_ ) = min _{n_ : _sn ≥ t} and m_ ( _t_ ) = max _{n_ : _sn ≤ t}. Note that m_ ( _t_ ) _≥ h_ ( _t_ ) _−_ 1 _. Then h_ ( _t_ ) _/t →_ 1 _/a and m_ ( _t_ ) _/t →_ 1 _/a as t →∞._

_Proof._ Fix _ε >_ 0. Then _sn ≤_ ( _a_ + _ε_ ) _n_ ultimately, which implies that _h_ ( _t_ ) _≥ t/_ ( _a_ + _ε_ ) ultimately. Then


37

_LECTURE 10. SEPTEMBER 27_

38

Similarly, _m_ ( _t_ ) _≤ t/_ ( _a_ + _ε_ ) ultimately, which implies that lim sup _t m_ ( _t_ ) _/t ≤_ 1 _/a_ . We have


**Corollary 10.3** (Renewal SLLN) **.** _Let_ ( _Xi_ ) _be IID, with EX_ = _µ ∈_ (0 _, ∞_ ) _. Let Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi.Define_</sup> _Nt_ = max _{n_ : _Sn ≤ t} and Ht_ = min _{n_ : _Sn ≥ t}. Then Nt/t →_ 1 _/µ and Ht/t →_ 1 _/µ a.s. as t →∞._

_Proof._ Use the SLLN and 10.2

_Story_ . Light bulbs have IID lifetimes _X_ 1 _, X_ 2 _, . . . >_ 0. We have a new bulb at time 0, and let _Nt_ be the number of bulbs replaced by time _t_ .

### **10.3 Stopping Times**

A random variable is a measurable function _Xi_ : (Ω _, F, P_ ) _→_ R. Given _X_ 0 _, X_ 1 _, . . . , Xn_ , we define the _σ_ -field _Fn_ = _σ_ ( _X_ 0 _, . . . , Xn_ ), the collection of events of the form _{ω_ : ( _X_ 0( _ω_ ) _, . . . , Xn_ ( _ω_ )) _∈ B}_ for some measurable _B ⊆_ R<sup>_n_+1</sup> (so _Fn ⊆F_ ). _Fn_ is the “information at time _n_ ”.

A **stopping time** is a RV _T_ : (Ω _, F, P_ ) _→{_ 0 _,_ 1 _,_ 2 _, . . . } ∪{∞}_ such that


This is equivalent to the definition


Given (10.1), _{T ≤ n}_ = _{T_ = 0 _} ∪{T_ = 1 _} ∪· · · ∪{T_ = _n} ∈Fn_ , since each event is in _Fn_ . Given (10.1), _{T_ = _n}_ = _{T ≤ n} \ {T ≤ n −_ 1 _} ∈Fn_ , since both events are in _Fn_ .

**Example 10.4.** _T_ = min _{n_ : _Xn ∈ B}_ for some measurable _B ⊆_ R<sup>1</sup> is a stopping time because


_Note_ . Given arbitrary _X_ 1 _, X_ 2 _, . . . , Xn_ , define _S_ 0 = 0, _Sm_ =<sup>�</sup><sup>_m_</sup> _i_ =1<sup>_Xi_.Then</sup>


and so _T_ = min _{n_ : _Sn ≥ b}_ is a stopping time.

_T_ = _∞_ if the event never happens.

Given _X_ 1 _, . . . , XN_ (for a given _N_ ), _T_ = max _{n_ : _n ≤ N, Xn ≥ a}_ is _not_ a stopping time.

**Theorem 10.5** (Wald’s Equation/Identity/Formula) **.** _Let_ ( _Xi_ ) _be IID with EX_ = _µ and Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi._</sup> _Let T be a stopping time with ET < ∞. Then EST_ = _µ · ET ._

_Note_ . This is an undergraduate result under the assumption that _T_ is independent of ( _Xi_ ).

_Fact_ . _E_<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_Yi_= �</sup><sup>_∞_</sup> _i_ =1<sup>_EYi_,provided�</sup> _i_<sup>_E|Yi| < ∞_.</sup> _Proof_ :<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Yi→_�</sup><sup>_∞_</sup> _i_ =1<sup>_Yi_a.s.,andthesummationisdominatedby�</sup><sup>_n_</sup> _i_ =1<sup>_|Yi|_.Usedominatedconvergence.</sup>

_LECTURE 10. SEPTEMBER 27_

39


We need to show that _EST_ = _µ · ET_ . By the Fact, it is enough to show that<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_E|Xi|_1(</sup><sup>_i≤T_)</sup><sup>_<∞_.</sup> We can apply (10.3) to _|Xi|_ . Then


### **10.4 Fatou’s Lemma**

**Lemma 10.6** (Fatou’s Lemma) **.** _Take arbitrary Xn ≥_ 0 _. Then E_ [lim inf _n Xn_ ] _≤_ lim inf _n EXn ≤∞._

_Proof._ Define _YN_ = inf _n≥N Xn_ . Then 0 _≤ YN ↑_ lim inf _Xn_ , so 0 _≤ EYN ↑ E_ [lim inf _Xn_ ]. Since _YN ≤ XN_ , _E_ [lim inf _Xn_ ] = lim inf _EYN N ≤_ lim inf _EXN N_

**Corollary 10.7.** _Take arbitrary Xn ≥_ 0 _. If Xn → X∞ a.s., then EX∞ ≤_ lim inf _n EXn ≤∞._

Recall the aggressive “gambling on a favorable game” example. There, _Xn ≥_ 0, _Xn →_ 0 a.s., but _EXn →∞_ .

### **10.5 Back to Renewal Theory**

Under the assumptions of 10.3, with the additional assumption that _X ≥_ 0 a.s., then _E_ [ _N_ ( _t_ ) _/t_ ] _→_ 1 _/µ_ as _t →∞_ .

_Proof._ By 10.6,

It is enough to show the upper bound


Since _X ≥_ 0, _N_ ( _t_ ) + 1 = min _{n_ : _Sn > t}_ is a stopping time. min( _N_ ( _t_ ) + 1 _, m_ ) is also a stopping time. Apply 10.5 to obtain

_ES_ min( _N_ ( _t_ )+1 _,m_ ) = _µE_ min( _N_ ( _t_ ) + 1 _, m_ )

_LECTURE 10. SEPTEMBER 27_

40


## **Lecture 11**

---

[← September 22](11-september-22.md) · [Up: contents](index.md) · [September 29 →](13-september-29.md)
