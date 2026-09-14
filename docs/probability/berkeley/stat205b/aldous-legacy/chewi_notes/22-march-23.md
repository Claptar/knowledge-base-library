---
title: March 23
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# March 23

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **20.1 Ergodic Theory & Markov Chains**

**Proposition 20.1.** _Any stationary irreducible Markov countable state (S) Markov chain is ergodic._

_Proof._ Let _π_ be the stationary distribution. We know that the chain is positive-recurrent, which implies that it visits every state infinitely often. Consider an invariant set _A ⊆ S_<sup>_∞_</sup> . Define the function _h_ ( _x_ ) = E _x_ 1(( _X_ 0 _,X_ 1 _,..._ ) _∈A_ ).


The LHS is a MG, so it converges a.s. to 1(( _X_ 0 _,X_ 1 _,..._ ) _∈A_ ). Since _h_ ( _Xn_ ) is also converging a.s., _h_ ( _x_ ) is constant for all _x_ , so _h_ ( _x_ ) = 0 for all _x_ or _h_ ( _x_ ) = 1 for all _x_ . Therefore, E _π_ 1(( _X_ 0 _,X_ 1 _,..._ ) _∈A_ ) is 0 or 1, so the chain is ergodic.

_Fact_ . Here, the _tail σ_ -field is trivial _⇐⇒_ the chain is aperiodic.

### **20.2 Ergodic Theorem**

**Theorem 20.2** (The Ergodic Theorem) **.** _For stationary_ ( _Xi,_ 0 _≤ i < ∞_ ) _with_ E _|X_ 0 _| < ∞ and_


_we have n_<sup>_−_1</sup> _Sn →_ E[ _X_ 0 _| I_ ] _a.s. and in L_<sup>1</sup> _as n →∞._

Ergodic implies that the limit is E _X_ 0.

**Lemma 20.3** (Maximal Lemma) **.** _Write Mk_ = max(0 _, S_ 1 _, S_ 2 _, . . . , Sk_ ) _. Then,_ E[ _X_ 01( _Mk>_ 0)] _≥_ 0 _. Proof._ See the text.

_Easy_ . E[ _Xk | I_ ]<sup>a.s</sup> = E[ _X_ 0 _| I_ ] and ( _Xk −_ E[ _Xk | I_ ] _, k ≥_ 0) is stationary.

78

_LECTURE 20. MARCH 23_

79

_Classic Proof of 20.2._ Reduce to the case E[ _X_ 0 _| I_ ] = 0. Write


It is enough to prove _X_<sup>¯</sup> _≤_ 0 a.s. (then apply this to _−X_<sup>¯</sup> ).

Fix _ε >_ 0. Consider _Xi_<sup>_∗_=(</sup><sup>_Xi −ε_)1</sup> ( _X>ε_<sup>¯</sup> )<sup>.Checkthat(</sup><sup>_X_</sup> _i_<sup>_∗, i≥_0)isstationary,anddefine</sup><sup>_S_</sup> _k_<sup>_∗_,</sup><sup>_M ∗_</sup> _k_<sup>as</sup> in 20.3. Define _Fn_ = _{Mn_<sup>_∗>_0</sup><sup>_}_.Let</sup>


Apply the Maximal Lemma 20.3 to ( _Xi_<sup>_∗_).</sup>


Note that _Fn ↑ F_ and E _|X_ 0<sup>_∗| ≤_E</sup><sup>_|X_0</sup><sup>_|_+</sup><sup>_ε < ∞_.Therefore,</sup>


However, _F ∈I_ and E[ _X_ 0 _| I_ ] = 0, which implies that E[ _X_ 01 _F_ ] = 0. _X_ 0<sup>_∗_=(</sup><sup>_X_0</sup><sup>_−ε_)1</sup><sup>_F_impliesthat</sup> E _X_ 0<sup>_∗_= E[</sup><sup>_X_01</sup><sup>_F_]</sup><sup>_−ε_P(</sup><sup>_F_),soP(</sup><sup>_F_) = 0.Hence,P( ¯</sup><sup>_X> ε_) = 0,so</sup><sup>_X_¯</sup><sup>_≤_0a.s.</sup>

### **20.3 Applications to Range/Recurrence of “Stationary Increment” Random Walks**

_Setting_ . Let ( _X_ 1 _, X_ 2 _, X_ 3 _, . . ._ ) be stationary, Z<sup>_d_</sup> -valued. _S_ 0 = 0 and _Sk_ =<sup>�</sup><sup>_k_</sup> _i_ =1<sup>_Xi_.Theevent</sup><sup>_A_istheevent</sup> that we “never return to 0”: _{Sk̸_ = 0 _, ∀k ≥_ 1 _}_ = _{_ ( _X_ 1 _, X_ 2 _, . . ._ ) _∈ A_<sup>ˆ</sup> _}_ , where


So, _A_<sup>ˆ</sup> _⊆_ (Z<sup>_d_</sup> )<sup>_∞_</sup> .

**Theorem 20.4.** _In the setting above, Rn is the number of distinct sites in_ Z<sup>_d_</sup> _that_ ( _S_ 1 _, . . . , Sn_ ) _visits. Then, n_<sup>_−_1</sup> _Rn −−→_<sup>_a.s._</sup> E[1 _A | I_ ] _. L_<sup>1</sup>

_Idea_ . _Rn_ counts the number of events. We will sandwich _Rn_ between two stationary processes of events.

_Proof. Rn_ is at least the number of _m_ ’s (1 _≤ m ≤ n_ ) such that ( _Sm_ +1 _, Sm_ +2 _, . . ._ ) are all different from _Sm_ . The latter is<sup>�</sup><sup>_n_</sup> _m_ =1<sup>1</sup> (( _Xm_ +1 _,Xm_ +2 _,..._ ) _∈A_<sup>ˆ</sup> )<sup>andthe</sup><sup>_m_=0caseis1</sup><sup>_A_.TheErgodicTheorem20.2</sup> implies


(This is one side of the theorem.)

_LECTURE 20. MARCH 23_

80

Fix _k_ . Observe


Apply the Ergodic Theorem 20.2 to the stationary process of indicators.


Let _k ↑∞_ , _Ak ↓ A_ .


**Theorem 20.5.** _In the setting above, assume the random variables are_ Z<sup>1</sup> _-valued and_ E _|X_ 1 _| < ∞._

_(i) If_ E[ _X_ 1 _| I_ ] = 0 _, then_ P( _A_ ) = 0 _(“recurrence”)._

_(ii) If_ P( _A_ ) = 0 _, then_ P( _Sn_ = 0 _infinitely often_ ) = 1 _._

_Proof._ (i) By 20.4, it is enough to prove _Rn/n →_ 0 a.s. (then E[1 _A |I_ ] = 0 = _⇒_ P( _A_ ) = 0). However, _Rn ≤_ 1 + max _m≤n Sm −_ min _m≤n Sm_ . So, it is enough to show


The Ergodic Theorem 20.2 says


and it is a deterministic fact that (20.3) = _⇒_ (20.2).

- (ii) We will show P( _Xn_ = 0 for at least 2 values of _n_ ) = 1. A similar argument will work for any _B_ . Write _Tn_ for the time of the _n_ th return to 0. _{T_ 1 = _j, T_ 2 = _j_ + _k}_ = _{T_ 1 = _j} ∩ Gj,k_ , where


Stationarity implies P( _Gj,k_ ) = P( _G_ 0 _,k_ ) = P( _T_ 1 = _k_ ). The hypothesis implies that


so<sup>�</sup><sup>_∞_</sup> _k_ =1<sup>(</sup><sup>_Gj,k∩{T_1=</sup><sup>_j}_)=</sup><sup>_{T_1=</sup><sup>_j}_a.s.So,</sup><sup>_{T_1=</sup><sup>_j, T_2</sup><sup>_<∞}_=</sup><sup>_{T_1=</sup><sup>_j}_a.s.Taketheunion</sup> over _j_ , and we have _{T_ 1 _< ∞, T_ 2 _< ∞}_ = _{T_ 1 _< ∞}_ a.s. The latter has probability 1, so the former has probability 1.

## **Lecture 21**

---

[← March 21](21-march-21.md) · [Up: contents](index.md) · [April 4 →](23-april-4.md)
