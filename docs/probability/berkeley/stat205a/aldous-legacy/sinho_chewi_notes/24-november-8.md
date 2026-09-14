---
title: November 8
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# November 8

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **22.1 Setup for OST**

Let ( _Xn, n ≥_ 0) be a sub-MG and _T < ∞_ a.s. be a stopping time. We want to conclude that _EX_ 0 _≤ EXT_ . What _extra_ assumptions do we need?

_Know_ . It is sufficient that _T ≤ t_ 0 _< ∞_ a.s., so it is sufficient that _E|XT − XT ∧n| →_ 0 as _n →∞_ .

**Theorem 22.1.** _(See Durrett.) It is sufficient that (a) E|Xn|_ 1( _T >n_ ) _→_ 0 _as n →∞, and (b) E|XT | < ∞._

**Theorem 22.2** (Useful Version of OST) **.** _Suppose:_ ( _Xn_ ) _is a sub-MG, T is a stopping time, and ET < ∞. Write_ ∆ _n_ = _Xn − Xn−_ 1 _. If there exists a constant b such that_


_then EX_ 0 _≤ EXT ._

_Proof._


Consider _Y_ = _|X_ 0 _|_ +<sup>�</sup><sup>_T_</sup> _n_ =1<sup>_|_∆</sup><sup>_n|_.Notethat</sup><sup>_|XT | ≤Y_and</sup><sup>_|XT ∧n| ≤Y_.Then</sup>


We have


Take expectations of both sides.


82

_LECTURE 22. NOVEMBER 8_

83

Therefore,


so _E|XT | ≤ EY < ∞_ , which checks (b). For condition (a),


as _n →∞_ , since _EY < ∞_ . (We are using the fact that _E|W | < ∞_ and _P_ ( _An_ ) _→_ 0 imply _E_ [ _W_ 1 _An_ ] _→_ 0.)

### **22.2 Martingale Proofs**

_Principle_ . Given a MG proof of an exact formula, one can often get inequality conclusions out of inequality assumptions.

**Corollary 22.3** (Inequality Version of Wald’s Identity) **.** _Suppose_ ( _ξi_ ) _are independent, µi ≤ Eξi ≤ µ_ 2 _, and_ sup _i E|ξi| < ∞. Let Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_ξi.Then,foranystoppingtimeTwithET< ∞,_</sup>


Wald: If the ( _ξi_ ) are IID, then _EST_ = ( _Eξ_ ) _·_ ( _ET_ ).

_Proof._ Apply 22.2 to _Xn_ = _Sn − nµ_ 1, so that ∆ _n_ = _ξn − µ_ 1. _E_ [∆ _n | Fn−_ 1] = _Eξn − µ_ 1 _≥_ 0, so ( _Xn_ ) is a sub-MG. We have

_E_ [ _|_ ∆ _n| | Fn−_ 1] = _E|_ ∆ _n| ≤ E|ξn|_ + _|µ_ 1 _| ≤ b_

by hypothesis. Therefore, _EX_ 0 _≤ EXT_ , so 0 _≤ EST − µ_ 1 _ET_ , so _EST ≥ µ_ 1 _ET_ .

**Lemma 22.4.** _Take_ ( _ξi_ ) _IID, Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_ξi._</sup> _Fix a >_ 0 _and b > Eξ. Suppose ∃θ >_ 0 _such that E_ exp( _θξ_ ) = _e_<sup>_θb_</sup> _. Then P_ ( _Sn ≥ a_ + _bn for some n ≥_ 0) _≤ e_<sup>_−θa_</sup> _._

_Proof._ Set _ξ_<sup>ˆ</sup> _i_ = _ξi − b_ . Then _S_<sup>ˆ</sup> _n_ = _Sn − nb_ and _E_ exp( _θξ_<sup>ˆ</sup> ) = 1 by definition. Then (exp( _θS_<sup>ˆ</sup> _n_ ) _, n ≥_ 0) is a MG. Apply the _L_<sup>1</sup> maximal inequality, so

Set _λ_ = _e_<sup>_θa_</sup> . Then


which implies the result.

**Lemma 22.5.** _Suppose_ ( _ξi_ ) _are IID and let Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_ξi.Suppose∃θ>_0</sup><sup>_suchthat_</sup> _φ_ ( _θ_ ) = _E_ exp( _θξ_ ) = 1

_LECTURE 22. NOVEMBER 8_

84

_Suppose T is a stopping time with ET < ∞ and Sn ≤ B on {n < T } for all n. Then E_ exp( _θST_ ) = 1 _._

_Proof. Xn_ def= exp( _θSn_ ) is a MG. We need to check (22.1) from 22.2.


On _{n ≤ T }_ = _{n −_ 1 _< T }_ , we have _Sn−_ 1 _≤ B_ , so _Xn−_ 1 _≤ e_<sup>_θB_</sup> . Therefore, 2 _Xn−_ 1 _≤_ 2 _e_<sup>_θB_</sup> on _{n ≤ T }_ . This verifies (22.1).

### **22.3 Boundary Crossing Inequalities**

_Setting_ . Let ( _ξi_ ) be IID with _Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_ξi_.Supposethat</sup><sup>_|ξi| ≤L_andassume</sup><sup>_Eξ<_0,with</sup><sup>_P_(</sup><sup>_ξ>_0)</sup><sup>_>_0.</sup> Fix _a <_ 0 _< b_ , and consider _T_ = min _{n_ : _Sn ≥ b_ or _Sn ≤ a}_ .

_Exercise_ . _ET < ∞_ .

So, _P_ ( _ST ≥ b_ and _ST ≤ b_ + _L_ ) = _x_ , say, and _P_ ( _ST ≤ a_ and _ST ≥ a − L_ ) = 1 _− x_ .

Consider _φ_ ( _θ_ ) = _E_ exp( _θξ_ ) _< ∞_ . We know that _φ_ (0) = 1, _φ_<sup>_′_</sup> (0) = _Eξ <_ 0, and _φ_ ( _θ_ ) _→∞_ as _θ →∞_ . Therefore, _∃θ >_ 0 such that _φ_ ( _θ_ ) = 1.

Apply 22.5 to conclude that _E_ exp( _θST_ ) = 1.


With some algebra,


_Special Case_ . If _P_ ( _ξ_ = 1) = _p <_ 1 _/_ 2 and _P_ ( _ξ_ = _−_ 1) = _q_ = 1 _− p_ and _a <_ 0 _< b_ are integers, then (22.2) is an equality, so


Write _φ_ ( _θ_ ) = _pe_<sup>_θ_</sup> + _qe_<sup>_−θ_</sup> = 1 and solve, so _e_<sup>_θ_</sup> = _q/p_ . This yields the result that we see in an undergraduate course.

## **Lecture 23**

---

[← November 3](23-november-3.md) · [Up: contents](index.md) · [November 10 →](25-november-10.md)
