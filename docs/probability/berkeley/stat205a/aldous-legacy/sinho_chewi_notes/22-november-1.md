---
title: November 1
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# November 1

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **20.1 Upcrossing Inequality**

Take any R-valued ( _Xn, n ≥_ 0) and any _a < b_ . Define _S_ 1 = min _{n_ : _Xn ≤ a}_ , _T_ 1 = min _{n_ : _Xn ≥ b}_ , _S_ 2 = min _{n > T_ 1 : _Xn ≤ a}_ , _T_ 2 = min _{n > S_ 2 : _Xn ≥ b}_ , etc.

Define _Un_ = _Un_ [ _a, b_ ] = max _{k_ : _Tk ≤ n}_ , the number of upcrossings over [ _a, b_ ] completed by time _n_ .

**Theorem 20.1** (The Upcrossing Inequality) **.** _Suppose_ ( _Xn_ ) _is a sub-MG. Then_


_Proof._ Note that ( _x − a_ )<sup>+</sup> _≤ x_<sup>+</sup> + _|a|_ , so _E_ ( _X − a_ )<sup>+</sup> _≤ EX_<sup>+</sup> + _|a|_ .

( _Trick_ ) In the case that _Xn ≥ a ∀n_ , we will prove ( _b − a_ ) _EUn ≤ EXn_<sup>+</sup><sup>_−EX_</sup> 0<sup>+.Forgeneral(</sup><sup>_Xn_),apply</sup> the result to max( _Xn, a_ ) _− a_ , which is a sub-MG. Use the “buy low, sell high” strategy: buy 1 share at _Si_ , and sell 1 share at _Ti_ . Consider _Y_ = _H · X_ , where _Hn_ = 1( _S_ 1 _<n≤T_ 1) + 1( _S_ 2 _<n≤T_ 2) + _· · ·_ . This is a predictable process, so ( _Yn_ ) is a sub-MG.


Take expectations.


Consider the opposite strategy _K_ : _Kn_ = 1 _− Hn_ . ( _Xn − Yn_ ) = ( _K · X_ ) _n_ + _X_ 0 is a sub-MG.


### **20.2 Martingale Convergence**

75

_LECTURE 20. NOVEMBER 1_

76

**Theorem 20.2** (Martingale Convergence Theorem) **.** _If_ ( _Xn_ ) _is a sub-MG, if_ sup _n EXn_<sup>+</sup><sup>_<∞,then_</sup> _Xn → X∞ a.s., for some X∞ with E|X∞| < ∞._

_Proof. Un_ [ _a, b_ ] _↑ U∞_ [ _a, b_ ], so


which implies that _U∞_ [ _a, b_ ] _< ∞_ a.s. This implies


For reals ( _xn_ ), if lim sup _n xn >_ lim inf _n xn_ , then _U∞_ [ _a, b_ ] = _∞_ , for some _a < b_ . Since _U∞_ [ _a, b_ ] _< ∞_ for all rational _a < b_ , then lim sup _xn_ = lim inf _xn ∈_ [ _−∞, ∞_ ]. Therefore, _Xn → X∞_ a.s., but _X∞ ∈_ [ _−∞, ∞_ ]. Recall Fatou’s Lemma: If _Yn ≥_ 0,


**Corollary 20.3.** _If_ ( _Xn_ ) _is a super-MG, if Xn ≥_ 0 _a.s., then Xn → X∞ a.s. and_ 0 _≤ EX∞ ≤ EX_ 0 _._

_Proof._ Apply 20.2 to ( _−Xn_ ), so _Xn → X∞_ a.s. Use Fatou’s Lemma: _EX∞ ≤_ lim inf _n EXn ≤ EX_ 0.

Recall the simple RW _X_ 0 = 1, stopped at _T_ = min _{n_ : _Xn_ = 0 _}_ . Let _Yn_ = _X_ min( _T,n_ ). Then _Yn →_ 0 = _Y∞_ a.s., but _EYn_ = 1 _∀n_ but _EY∞_ = 0.

### **20.3 Facts About Uniform (Equi-)Integrability**

Consider R-valued RVs.


If _E|Y | < ∞_ , then lim _b→∞ E_ [ _|Y |_ 1( _|Y |>b_ )] = 0.

We will quote some facts (see Durrett or Billingsley).

1. If sup _α E|Yα|_<sup>_q_</sup> _< ∞_ for some _q >_ 1, then ( _Yα_ ) is UI, which implies that sup _α E|Yα| < ∞_ .

2. if _Yn → Y∞_ a.s., if ( _Yn_ ) is UI, then _E|Y∞| < ∞_ and _E|Yn − Y∞| →_ 0, i.e. _Yn → Y∞_ in _L_<sup>1</sup> .

3. If _Yn → Y∞_ in _L_<sup>1</sup> , then ( _Yn_ ) is UI.

_LECTURE 20. NOVEMBER 1_

77

4. If _E|Y | < ∞_ , the family of _{E_ [ _Y | G_ ] _,_ all _G}_ is UI.

**Theorem 20.5.** _For a MG_ ( _Xn_ ) _, the following are equivalent. (i)_ ( _Xn_ ) _is UI._

_(ii) Xn converges in L_<sup>1</sup> _. (iii) There exists a RV X∞ with E|X∞| < ∞ such that Xk_ = _E_ [ _X∞ | Fk_ ] _∀k._

_If these conditions hold, then ∃X∞ such that Xn → X∞ both a.s. and in L_<sup>1</sup> _._

_Proof._ ( _iii_ ) _⇒_ ( _i_ ), by 4.

(i) implies, by 1, sup _n E|Xn| < ∞_ , which by 20.2 implies _Xn_ converges to some _X∞_ a.s., which implies by 2 that _Xn → X∞_ in _L_<sup>1</sup> , which implies (ii).

Given (ii), _Xn → X∞_ in _L_<sup>1</sup> , which implies that _E|Xn − X∞| →_ 0 with _E|X∞| < ∞_ . We need to prove that _EX∞_ 1 _A_ = _EXk_ 1 _A ∀A ∈Fk_ . Fix _A_ and _k_ . By the MG property, for _n > k_ , _E_ [ _Xn | Fk_ ] = _Xk_ , so _EXn_ 1 _A_ = _EXk_ 1 _A_ . Hence, _|EX∞_ 1 _A − EXn_ 1 _A| ≤ E|X∞ − Xn| →_ 0 as _n →∞_ , so _|EX∞_ 1 _A − EXk_ 1 _A|_ = 0.

**Theorem 20.6** (Levy’s 0-1 Law) **.** _Take any process_ ( _Yn, n ≥_ 0) _. Take any RV Z with E|Z| < ∞ and Z ∈ σ_ ( _Yn, n ≥_ 0) _. Then Xn_ = _E_ [ _Z | Y_ 1 _, . . . , Yn_ ] _is a UI martingale, so by 20.5, Xn → X∞ a.s. and in L_<sup>1</sup> _. In fact, X∞_ = _Z because_


**Remark** : In particular, take _Z_ = 1 _A_ . Then

_P_ ( _A | Y_ 1 _, . . . , Yn_ )( _ω_ ) _→_ 1 _A_ ( _ω_ ) a.s.

for all _A ∈ σ_ ( _Yn, n ≥_ 0).

For independent ( _Yn_ ), suppose _A_ is in the tail _σ_ -field.

_P_ ( _A | Y_ 1 _, . . . , Yn_ )( _ω_ ) = _P_ ( _A_ ) _→_ 1 _A_ a.s. as _n →∞_ which implies that 1 _A_ is a constant a.s., which implies that _P_ ( _A_ ) = 0 or 1.

## **Lecture 21**

---

[← October 27](21-october-27.md) · [Up: contents](index.md) · [November 3 →](23-november-3.md)
