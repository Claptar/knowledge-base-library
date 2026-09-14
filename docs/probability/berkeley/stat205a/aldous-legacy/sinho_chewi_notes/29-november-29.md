---
title: November 29
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# November 29

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **27.1 Aspects of Brownian Motion**

- model for many processes fluctuating continuously: stock market, etc.

- ( _Theory_ ) limit of RWs with small step size

- Gaussian process

- “diffusions”: continuous-path Markov processes

- martingale properties

We will concentrate on the last aspect.

##### **Definition 27.1. Brownian motion** ( _B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) has the properties

- for _s < t_ , _B_ ( _t_ ) _− B_ ( _s_ ) = Normal(0d _, t − s_ )

- for 0 _≤ t_ 1 _< t_ 2 _< · · · < tn_ , the increments ( _B_ ( _ti_ +1) _− B_ ( _ti_ ) _,_ 1 _≤ i ≤ n −_ 1) are independent

- the sample paths _t �→ B_ ( _t_ ) are continuous

- _B_ (0) = 0

### **27.2 Continuous-Time Martingales**

( _Mt, Ft_ ) with the filtration ( _Ft,_ 0 _≤ t < ∞_ ) is a **MG** if

- _E|Mt| < ∞∀t_

- _Mt_ is adapted to _Ft_

- for _s < t_ , _E_ [ _Mt | Ft_ ] = _Ms_ a.s.

All of our MGs will have continuous paths. The general theory requires only right-continuity.

_T_ : Ω _→_ [0 _, ∞_ ) is a **stopping time** if _{T ≤ t} ∈Ft_ , for all 0 _≤ t < ∞_ . In discrete time, the stopping time property with _{T ≤ n}_ was equivalent to the definition with _{T_ = _n}_ , but this is not true in continuous time.

**Theorem 27.2** (Optional Sampling Theorem) **.** _If_ ( _Mt_ ) _is a MG, if T is a stopping time, and if (for t_ 0 _an integer, WLOG) P_ ( _T ≤ t_ 0) = 1 _, then EMT_ = _EM_ 0 _._

98

_LECTURE 27. NOVEMBER 29_

99

_Proof._ Fix _m_ and look at times that are multiples of 2<sup>_−m_</sup> . Define _Tm_ = inf _{i/_ 2<sup>_m_</sup> : _i/_ 2<sup>_m_</sup> _> T }_ . Note that _{T < t}_ =<sup>�</sup> _n_<sup>_{T≤t −_1</sup><sup>_/n}∈Ft_.This</sup><sup>_Tm_isastoppingtimefor(</sup><sup>_Mi/_2</sup><sup>_m, Fi/_2</sup><sup>_m, i≥_0),and</sup> _Tm ≤ t_ 0 + 1. Apply the discrete-time OST to obtain _EMTm_ = _EM_ 0 and _MTm_ = _E_ [ _Mt_ 0+1 _| FTm_ ] (which implies that ( _MTm , m ≥_ 1) is UI). As _m →∞_ , _Tm ↓ T_ , and right-continuity implies that _MTm → MT_ a.s., so _EMTm → EMT_ .

With BM we associate the natural filtration _Ft_ = _σ_ ( _Bs,_ 0 _≤ s ≤ t_ ).

**Proposition 27.3.** _The following are MGs. • Bt • Bt_<sup>2</sup><sup>_−t_</sup> _•_ exp( _θBt − θ_<sup>2</sup> _t/_ 2) _, for θ ∈_ R _• Bt_<sup>3</sup><sup>_−_3</sup><sup>_tBt_</sup> _• Bt_<sup>4</sup><sup>_−_6</sup><sup>_tB_</sup> _t_<sup>2+ 3</sup><sup>_t_2</sup>

_Proof._ Fix _s < t_ .

_Bt_ = _Bs_ + ( _Bt − Bs_ ) _E_ [ _Bt | Fs_ ] = _Bs_ + _E_ [ _Bt − Bs | Fs_ ] = _Bs_ + _E_ [ _Bt − Bs_ ] = _Bs_ + 0 = _Bs_

_Bt − Bs_ is independent of ( _Bs_ 1 _, Bs_ 2 _, . . . , Bsn_ ) for all 0 _≤ s_ 1 _< s_ 2 _< · · · < sn ≤ s_ . We conclude that _Bt − Bs_ is independent of _Fs_ def= _σ_ ( _Bi,_ 0 _≤ u ≤ s_ ) using the MT fact about independence: it suffices to prove independence for any finite subcollection.


_Aside_ . If _W_ = Normal(0d _, σ_ 2), then _E_ exp( _θW_ ) = exp( _θ_ 2 _σ_ 2 _/_ 2). Write _Zt_<sup>_θ_= exp(</sup><sup>_θBt−θ_2</sup><sup>_t/_2).</sup>


Informally, ( _Zt_<sup>_θ,_0</sup><sup>_≤t < ∞_)isaMG,so</sup>

should be a MG. If we differentiate _k_ times, and set _θ_ = 0, we get a sequence of polynomials in _Bt_ .

_LECTURE 27. NOVEMBER 29_

100

A typical stopping time is _Tb_ = inf _{t_ : _B_ ( _t_ ) = _b}_ = inf _{t_ : _B_ ( _t_ ) _≥ b}_ (for _b >_ 0). Also, for _b >_ 0, _t >_ 0, _{Tb ≤ t}_ = _{_ sup _s≤t B_ ( _s_ ) _≥ b}_ . Note that


is _Ft_ -measurable.

**Lemma 27.4.** _Fix −a <_ 0 _< b. Consider T_ = min _{T−a, Tb}. Then_


_Proof. P_ ( _T > t_ ) _≤ P_ ( _B_ ( _t_ ) _∈_ [ _−a, b_ ]) _→_ 0 as _t →∞_ , so _T < ∞_ a.s. Apply OST, 27.2, to 0 and _T ∧ t_ .


As _t →∞_ , _BT ∧t → BT_ a.s. and


This implies that 0 = _EBT_ , but _BT_ takes values in _{−a, b}_ only, so we must have the distribution (27.1) and (27.2).

Apply the OST 27.2 to _Bt_<sup>2</sup><sup>_−t_.Then</sup><sup>_EB_</sup> _T_<sup>2</sup> _∧t_<sup>=</sup><sup>_E_[</sup><sup>_T∧t_].Let</sup><sup>_t →∞_.</sup>


Note _P_ ( _Tb < ∞_ ) _≥ P_ ( _Tb < T−a_ ) _→_ 1 as _a →∞_ , so _Tb < ∞_ a.s.

Fix _c >_ 0 and _−∞ < d < ∞_ . Consider _T_ = inf _{t_ : _Bt_ = _c_ + _dt} ≤∞_ .

**Lemma 27.5.**


_for_ 0 _≤ λ < ∞. This is the Laplace transform of T ._

_Proof._ Consider _θ >_ max(0 _,_ 2 _d_ ). Apply the OST 27.2 to exp( _θBt − θ_<sup>2</sup> _t/_ 2) and _T ∧ t_ .


_Case d ≤_ 0 _, θ >_ 0: Here, _BT ∧t −_ ( _θ_<sup>2</sup> _/_ 2)( _T ∧ t_ ) _≤ θc_ , _T ≤ Tc < ∞_ .

_LECTURE 27. NOVEMBER 29_

101

_Case d >_ 0 _, θ >_ 2 _d_ :


and _θBT ∧t −_ ( _θ_<sup>2</sup> _/_ 2)( _T ∧ t_ ) _→∞_ as _t →∞_ on _{T_ = _∞}_ . Let _t →∞_ . 1 = _E_ [exp( _θBT −_ ( _θ_<sup>2</sup> _/_ 2) _T_ )]1( _T <∞_ ). Put _BT_ = _c_ + _dT_ on _{T < ∞}_ .


Given _λ >_ 0, define _θ_ = _θ_ ( _λ_ ) as the solution of _θd − θ_<sup>2</sup> _/_ 2 = _−λ_ , so _θ_ ( _λ_ ) = _d_ + _√d_<sup>2</sup> + 2 _λ >_ max(0 _,_ 2 _d_ ). 1 = _E_ exp( _cθ_ ( _λ_ ) _− λT_ ) _E_ exp( _−λT_ ) = exp( _−cθ_ ( _λ_ ))

## **Lecture 28**

---

[← November 22](28-november-22.md) · [Up: contents](index.md) · [December 1 →](30-december-1.md)
