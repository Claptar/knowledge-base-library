---
title: September 20
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# September 20

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **8.1 Glivenko-Cantelli Theorem**

**Lemma 8.1.** _Let Fn and F be distribution functions. If_

_(i) Fn_ ( _x_ ) _→ F_ ( _x_ ) _for each rational x_

_(ii) Fn_ ( _x_ ) _→ F_ ( _x_ ) _and Fn_ ( _x−_ ) _→ F_ ( _x−_ ) _for each_ **_atom_** _of F (F_ ( _x_ ) _− F_ ( _x−_ ) = _P_ ( _X_ = _x_ ) _>_ 0 _) then_ sup _x|Fn_ ( _x_ ) _− F_ ( _x_ ) _| →_ 0 _._

**Theorem 8.2** (Glivenko-Cantelli Theorem) **.** _Let_ ( _Xi,_ 1 _≤ i < ∞_ ) _be IID with distribution function F . Let Gn_ ( _ω, x_ ) _be the empirical distribution function of_ ( _X_ 1 _, . . . , Xn_ ) _._


_Then_ sup _x|Gn_ ( _ω, x_ ) _− F_ ( _x_ ) _| →_ 0 _a.s. as n →∞._

_Proof._ Fix _x_ . The events _{X_ 1 _≤ x}_ , _{X_ 2 _≤ x}_ , etc. are IID events, with probability _F_ ( _x_ ). The SLLN implies that _Gn_ ( _ω, x_ ) _→ F_ ( _x_ ) a.s. as _n →∞_ .

If _S_ = _{_ rationals _} ∪{_ atoms of _F }_ (which is countable), then _P_ ( _{Gn_ ( _ω, x_ ) _→ F_ ( _x_ ) _∀x ∈ S}_ ) = 1. Then 8.1 implies that


### **8.2 Gambling on a Favorable Game**

**Example 8.3** (Betting on a Favorable Game) **.** Take a stake _s_ , where you gain _s_ with probability 1 _/_ 2+ _α_ and lose _s_ with probability 1 _/_ 2 _− α_ . (Imagine _α_ = 1%.)

_Strategy_ : Bet some proportion _q_ of your total, each time.

Let _Xn_ be your fortune after _n_ bets. Then


29

_LECTURE 8. SEPTEMBER 20_

30


where _An_ +1 is the event that you win the ( _n_ + 1)th bet. Then


where _Yi_ = log(1 _− q_ + 2 _q_ 1 _Ai_ ). As _n →∞_ ,


If (1 _/n_ ) log _Xn → c_ , then _Xn → e_<sup>_cn_</sup> , where _c_ is the asymptotic growth rate. The optimal choice of _q_ is to maximize _EY_ .


for _α_ , _q_ small. Choose _q_ = 2 _α_ .

_EXn_ = _X_ 0(1 + 2 _qα_ )<sup>_n_</sup> _→∞_ , but _Xn →_ 0 a.s. if _q ≥ q_ crit _≈_ 4 _α_ .

### **8.3 a.s. Limits for Maxima**

**Lemma 8.4** (Deterministic Lemma) **.** _If xn ≥_ 0 _and_ 0 _< bn ↑∞, then_


_Proof._ “ _≥_ ” is obvious. Fix _j_ .


Let _j →∞_ . Then


**Example 8.5.** Let ( _Xi, i ≥_ 1) be IID Exponential(1), so _P_ ( _X > x_ ) = _e_<sup>_−x_</sup> . Write _Mn_ = max1 _≤i≤n Xi_ . Then _Xn_ lim sup a.s. (8.1) _n_ log _n_<sup>= 1</sup>

_LECTURE 8. SEPTEMBER 20_

31

and _Mn_ log _n_<sup>_→_1</sup> a.s.

_Proof._ Fix _ε >_ 0. Then


and<sup>�</sup> _n_<sup>_n−_(1+</sup><sup>_ε_)</sup><sup>_< ∞_.TheFirstBorel-CantelliLemmaimpliesthat</sup>


Here, _Xn/_ log _n →_ 0 in probability, but not a.s.


### **8.4** 2 **nd Moment SLLN**

**Lemma 8.6** (Deterministic Lemma) **.** _Let Sn be real. To prove Sn/n →_ 0 _, it is enough to prove ∃n_ ( _j_ ) _↑∞ such that (i) Sn_ ( _j_ ) _/n_ ( _j_ ) _→_ 0 _as j →∞, (ii) dj/n_ ( _j_ ) _→_ 0 _as j →∞, for dj_ = max _n_ ( _j_ ) _≤n<n_ ( _j_ +1)�� _Sn − Sn_ ( _j_ )�� _._

_LECTURE 8. SEPTEMBER 20_

32


as _j →∞_ .

**Theorem 8.7** (2nd Moment SLLN) **.** _Given_ ( _Xi,_ 1 _≤ i < ∞_ ) _, with EXi ≡_ 0 _, let_ sup _i EXi_<sup>2=</sup><sup>_B<∞_</sup> _and the Xi be_ **_orthogonal_** _, E_ ( _XiXj_ ) = 0 _, j̸_ = _i. (We are not assuming independence!) Write_


_Then Sn/n →_ 0 _a.s._

_Proof._ Since var( _Sn_ ) _≤ nB_ , Chebyshev’s inequality implies

Take _n_ ( _j_ ) = _j_<sup>2</sup> . Use Borel-Cantelli.


By 8.6, it is enough to prove _Dj/j_<sup>2</sup> _→_ 0 a.s., for

Then

Since

Letting _n_ = _j_<sup>2</sup> + _i_ , we have


_LECTURE 8. SEPTEMBER 20_

33


The First Borel-Cantelli Lemma implies that _Dj/j_<sup>2</sup> _→_ 0 as _j →∞_ .

**Theorem 8.8** (Dominated Convergence Theorem) **.** _If Xn → X a.s., if ∃Y ≥_ 0 _such that |Xn| ≤ Y a.s. for all n, and if EY < ∞, then EXn → EX, E_ ( _Xn − X_ ) _→_ 0 _, and E_ ( _X_ ) _< ∞._

_Proof._ Fix _ε >_ 0. Define _AN_ = _{|Xn − X| ≤ ε,_ all _n ≥ N }_ . Then _AN ↑ A∞_ , say, and _P_ ( _A∞_ ) = 1. Also, _A_<sup>_c_</sup> _N_<sup>_↓A_</sup> _∞_<sup>_c_,and</sup><sup>_P_(</sup><sup>_Ac_</sup> _∞_<sup>) = 0.</sup>


lim sup _E|XN − X| ≤ ε_ + 0 _,_ by monotone convergence _N_

This is true for all _ε_ , so _E|XN − X| →_ 0.

## **Lecture 9**

---

[← September 15](09-september-15.md) · [Up: contents](index.md) · [September 22 →](11-september-22.md)
