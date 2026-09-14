---
title: November 17
source: https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# November 17

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **25.1 “Play Red”**

Consider a finite set _S_ and let _X_ 1 _, X_ 2 _, . . . , XN_ be a uniform random ordering. This is clearly a (finite) exchangeable sequence.

**Proposition 25.1.** _If_ ( _X_ 1 _, . . . , XN_ ) _is an exchangeable sequence, if_ 0 _≤ T ≤ N −_ 1 _is a stopping time, then XT_ +1 =d _X_ 1 _._

_Proof._ Recall from last lecture:

**Lemma** : If ( _Z_ 1 _, W_ ) = (d _Z_ 2 _, W_ ), then _E_ [ _φ_ ( _Z_ 1) _| W_ ] = _E_ [ _φ_ ( _Z_ 2) _| W_ ] a.s.

( _Xn_ +1 _, X_ 1 _, . . . , Xn_ ) =d ( _XN , X_ 1 _, . . . , Xn_ ). By the Lemma, _P_ ( _Xn_ +1 _∈ A | Fn_ ) = _P_ ( _XN ∈ A | Fn_ ) a.s., which implies that _P_ ( _Xn_ +1 _∈ A | FT_ ) = _P_ ( _XN ∈ A | FT_ ) a.s. on _{T_ = _n}_ , for all _n_ , so they equal each other everywhere. Now, take expectations:


### **25.2 de Finetti’s Theorem**

Given random _A_ and _B >_ 0, form the following construction: given _A_ = _a_ and _B_ = _b_ , let ( _Xi,_ 1 _≤ i < ∞_ ) be IID Normal( _a, b_ ). This is a **parametric Bayes** formulation.

Let _P_ ( _R_ ) be the space of all PMs on R. _M_ is a random variable with values in _P_ ( _R_ ). Construction: given _M_ = _µ_ , let ( _Xi, i ≥_ 1) be IID( _µ_ ). This gives an infinite exchangeable sequence.

**Theorem 25.2** (de Finetti’s Theorem) **.** _Let_ ( _Xi,_ 1 _≤ i < ∞_ ) _be exchangeable and_ R _-valued. Let τ be the tail σ-field. Then, conditionally on τ , the_ ( _Xi_ ) _are IID. That is,_

_(a) X_ 1 _, X_ 2 _, . . . are CI given τ ._

- _(b) There exists a kernel Q_ ( _ω, ·_ ) _(a random PM) such that Q_ ( _ω, ·_ ) _is the regular conditional distribution of Xi given τ , for each i._


92

_LECTURE 25. NOVEMBER 17_

93

_Proof (Sophisticated)._ Let _φ_ : R _→_ R be bounded and measurable. Exchangeable implies that


_σ_ ( _Xk, Xk_ +1 _, . . ._ ) _↓ τ_ as _k →∞_ . Apply reversed MG convergence, so the RHS converges to _E_ [ _φ_ ( _X_ 1) _| τ_ ] a.s. We conclude that _E_ [ _φ_ ( _X_ 1) _| X_ 2 _, X_ 3 _, . . ._ ] =d _E_ [ _φ_ ( _X_ 1) _| τ_ ].

_Fact_ : If _E_ [ _Z |G_ ] =d _Z_ , then _E_ [ _Z |G_ ] = _Z_ a.s. If _G ⊆H_ , if _E_ [ _Z |G_ ] =d _E_ [ _Z |H_ ], then _E_ [ _Z |G_ ] = _E_ [ _Z |H_ ] a.s.

By the exercise, _E_ [ _φ_ ( _X_ 1) _| X_ 2 _, X_ 3 _, . . ._ ] = _E_ [ _φ_ ( _X_ 1) _| τ_ ] a.s. By the same argument: _∀k ≥_ 1,


_U_ and _V_ are CI given _τ_ if and only if _E_ [ _φ_ ( _U_ ) _|V, τ_ ] = _E_ [ _φ_ ( _U_ ) _|τ_ ] a.s. Therefore, _Xk_ and ( _Xk_ +1 _, Xk_ +2 _, . . ._ ) are CI given _τ_ . This is enough to show that ( _X_ 1 _, X_ 2 _, X_ 3 _, . . ._ ) are CI given _τ_ .

Exchangeable implies that ( _X_ 1 _, Xi_ +1 _, Xi_ +2 _, . . ._ ) = (d _Xi, Xi_ +1 _, Xi_ +2 _, . . ._ ). By the Lemma,


Condition on _τ_ : _E_ [ _φ_ ( _X_ 1) _| τ_ ] = _E_ [ _φ_ ( _Xi_ ) _| τ_ ] a.s. Therefore, _X_ 1 and _Xi_ have the same conditional distribution given _τ_ .

Recall Glivenko-Cantelli: Define _F_ ( _x_ 1 _, x_ 2 _, . . . , xn, t_ ) to be the empirical distribution of ( _x_ 1 _, . . . , xn_ ):


If ( _Xi, i ≥_ 1) are IID with distribution function _F_ , then _F_ ( _X_ 1 _, . . . , Xn, t_ ) _−−→_<sup>a.s.</sup> _F_ ( _t_ ), for each _t_ , as _n →∞_ .

Given exchangeable ( _Xi,_ 1 _≤ i < ∞_ ), de Finetti’s Theorem 25.2 implies that


which is the distribution function of _Q_ ( _ω, ·_ ).

We can identify _Q_ with the limit 25.1.

### **25.3 MGs in Galton-Watson Branching Processes**

_ξ_ takes values in _{_ 0 _,_ 1 _,_ 2 _, . . . }_ . Each individual in generation _g_ has _ξ_ offspring in generation _g_ + 1. The _ξ_ are independent. _Zn_ is the number of individuals in generation _n_ , with _Z_ 0 = 1 as a default. Write _µ_ = _Eξ < ∞_ .

“Extinction” is the event _{Zn_ = 0 for some _n}_ and “survival” is the event _{Zn ≥_ 1 _∀n}_ .

Let _Fn_ = _σ_ ( _Z_ 0 _, Z_ 1 _, . . . , Zn_ ).


This implies that _EZn_ +1 = _µ · EZn_ , so inductively, _EZn_ = _µ_<sup>_n_</sup> .

_LECTURE 25. NOVEMBER 17_

94

If _µ <_ 1, then _P_ ( _Zn ≥_ 1) _≤ EZn ≤ µ_<sup>_n_</sup> _→_ 0, so _P_ (extinction) = 1.

_Undergraduate_ : “ _P_ (extinction) _<_ 1” if and only if _µ >_ 1 or _P_ ( _ξ_ = 1) = 1.

Study the case _µ >_ 1. 25.2 implies that ( _Zn/µ_<sup>_n_</sup> _, n ≥_ 0) is a MG, since _E_ [ _Zn/µ_<sup>_n_</sup> ] = 1. By the MG convergence theorem, _Zn/µ_<sup>_n_</sup> _−−→_<sup>a.s.</sup> _W ≥_ 0, _EW ≤_ 1. Suppose _Eξ_<sup>2</sup> _< ∞_ . We will show ( _Zn/µ_<sup>_n_</sup> _, n ≥_ 1) is UI. Then, _Zn/µ_<sup>_n_</sup> _→ W_ in _L_<sup>1</sup> and _EW_ = 1. Clearly, _{_ extinction _} ⊆{W_ = 0 _}_ . We can prove _{_ extinction _}_ = _{W_ = 0 _}_ a.s. So, either we have extinction, or _Zn_ grows exponentially fast.

_Calculation_ :


By induction,


so ( _Zn/µ_<sup>_n_</sup> _, n ≥_ 1) is UI.

### **25.4** _L_<sup>2</sup> **Theory**

_Topic_ : _L_<sup>2</sup> theory. (See Durrett for more.)

Consider ( _Mn, n ≥_ 0), _M_ 0 = 0, with ∆ _n_ = _Mn − Mn−_ 1. Suppose _EMn_<sup>2</sup><sup>_< ∞_,forall</sup><sup>_n_.</sup>

_Orthogonality of Increments_ . _E_ [∆ _i_ ∆ _j_ ] = 0, for _i < j_ , because _E_ [∆ _i_ ∆ _j | Fj−_ 1] = ∆ _iE_ [∆ _j | Fj−_ 1] = 0. So _EMn_<sup>2=�</sup><sup>_n_</sup> _i_ =1<sup>_E_[∆</sup> _i_<sup>2].Saythatthemartingaleis“</sup><sup>_L_2</sup><sup>**bounded**”ifsup</sup> _n_<sup>_EM_</sup> _n_<sup>2</sup><sup>_<∞_,whichisequivalentto</sup> � _∞i_ =1<sup>_E_[∆</sup> _i_<sup>2]</sup><sup>_<∞_.If(</sup><sup>_Mn_)is</sup><sup>_L_2bounded,then(</sup><sup>_L_1convergence)</sup><sup>_Mn_</sup> _−−→_<sup>a.s.</sup> _M∞_ and in _L_<sup>1</sup> . In fact, we also have _Mn → M∞_ in _L_<sup>2</sup> .


“Cauchy criterion = _⇒_ convergence” is the definition of a “complete metric space”. _Fact_ . _L_<sup>2</sup> is a complete metric space.

This implies that _Mn → M∞_ in _L_<sup>2</sup> .

## **Lecture 26**

---

[← November 15](26-november-15.md) · [Up: contents](index.md) · [November 22 →](28-november-22.md)
