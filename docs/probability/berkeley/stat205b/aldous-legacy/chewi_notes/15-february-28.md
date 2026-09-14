---
title: February 28
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# February 28

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **13.1 Periodicity**

Consider the directed graph associated with **P** on countable _S_ .

For state _x_ , _d_ ( _x_ ) def= greatest common divisor of _{n_ : _p_<sup>_n_</sup> _x,x_<sup>_>_0</sup><sup>_}_.</sup>

**Theorem 13.1** (Text, Exercise) **.** _Suppose that the Markov chain is irreducible._

_(a) d_ ( _x_ ) = _d ≥_ 1 _for each x ∈ S. The case d_ = 1 _is_ **_aperiodic_** _, and the case d ≥_ 2 _is_ **_periodic_** _with period d._

_(b) ∃n_ ( _x_ ) _< ∞ such that p_<sup>_n_</sup> _x,x_<sup>_>_0</sup><sup>_foralln ≥n_(</sup><sup>_x_)</sup><sup>_withd | n._</sup>

_(c) S can be partitioned into d “cyclic classes” C_ 0 _, C_ 1 _, . . . , Cd−_ 1 _such that if x ∈ Cu,_ P _x_ ( _Xn ∈ Cv_ ) _is_ 1 _if n_ = _v − u modulo d,_ 0 _if not._

- _(d) If the Markov chain is aperiodic, ∀_ ( _x, y_ ) _∃n_ ( _x, y_ ) _such that p_<sup>_n_</sup> _x,y_<sup>_>_0</sup><sup>_∀n ≥n_(</sup><sup>_x, y_)</sup><sup>_._</sup>

- _(e) If the period is d ≥_ 2 _, then_ **P**<sup>_d_</sup> _defines a MC on each Cu, which is irreducible on Cu. (f) If ∃x with px,x >_ 0 _, then by (a), d_ = 1 _and the chain is aperiodic._

### **13.2 Existence of Invariant Measures**

If _µ_ and _ν_ are PMs on measurable _S_ , the variation distance is _∥µ − ν∥_ def= sup _A |µ_ ( _A_ ) _− ν_ ( _A_ ) _|_ . If _S_ is countable, then


and _∥µn − µ∞∥→_ 0 _⇐⇒ µn_ ( _i_ ) _→ µ∞_ ( _i_ ) _∀i ∈ S_ .

**_µ_ P** is dist( _X_ 1) when _µ_ = dist( _X_ 0).

**Lemma 13.2.** _For a MC with transition matrix_ **P** _,_


51

_LECTURE 13. FEBRUARY 28_

52

_Proof._


since<sup>�</sup> _i_<sup>_pj,i≡_1.</sup>

**Lemma 13.3.** _Let_ ( _Xn,_ 0 _≤ n < ∞_ ) _be the_ ( _µ_ 0 _, P_ ) _chain. Write_ **_µ_** _n_ = dist( _Xn_ ) = **_µ_** 0 **P**<sup>_n_</sup> _. If ∥µn − µ∞∥→_ 0 _for some PM µ∞, then µ∞ is a stationary distribution for_ **P** _,_ **_µ_** _∞_ = **_µ_** _∞_ **P** _._

_Proof._


By the Triangle Inequality,


So, the possible _n →∞_ limit distributions are exactly the stationary distributions.

Let _Tx_ = _Tx_<sup>+= min</sup><sup>_{n ≥_1 :</sup><sup>_Xn_=</sup><sup>_x}_.Fixstate</sup><sup>_b_.Define</sup>


which implies that _µ_ ( _b, b_ ) = 1. _µ_ ( _b, ·_ ) is a measure on _S_ and E _bTb_ = _µ_ ( _b, S_ ) _≤∞_ .

**Proposition 13.4** (No Assumptions) **.** _Consider these equations for an unknown measure µ:_


_Then, µ_ ( _b, ·_ ) _is the minimal solution of_ (13.1) _and_ P _b_ ( _Tb < ∞_ ) =<sup>�</sup> _x_<sup>_µ_(</sup><sup>_b, x_)</sup><sup>_p_(</sup><sup>_x, b_)</sup><sup>_∀x._</sup>

_Proof._ Let the matrix **K** be the “chain killed at _Tb_ ”. _Kx,y_ = _Px,y_ for _y̸_ = _b_ and _Kx,y_ = 0 for _y_ = _b_ . Write _αn_ ( _y_ ) = P _b_ ( _Xn_ = _y, Tb > n_ ). Check that **_α_** _n_ +1 = **_α_** _n_ **K** . _α_ 0( _y_ ) = _δb_ ( _y_ ) = 1( _y_ = _b_ ). Therefore, **_α_** _n_ = **_δ_** _b_ **K**<sup>_n_</sup> . By definition, _µ_ ( _b, y_ ) =<sup>�</sup><sup>_∞_</sup> _n_ =0<sup>_αn_(</sup><sup>_y_),so</sup><sup>**_µ_**(</sup><sup>_b, ·_) = �</sup><sup>_∞_</sup> _n_ =0<sup>**_δ_**</sup><sup>_b_</sup><sup>**K**</sup><sup>_n_.Rewrite(13.1)as</sup><sup>**_µ_**=</sup><sup>**_δ_**</sup><sup>_b_+</sup><sup>**_µ_K**.Hence,</sup> **_µ_** ( _b, ·_ ) satisfies (13.1).

Let **_µ_** be some solution of (13.1). Then, **_µ_** = **_δ_** _b_ + ( **_δ_** _b_ + **_µ_ K** ) **K** = **_δ_** _b_ + **_δ_** _b_ **K** + **_µ_ K**<sup>2</sup> . Inductively, **_µ_** = **_µ_ K**<sup>_m_+1</sup> +<sup>�</sup><sup>_m_</sup> _n_ =0<sup>**_δ_**</sup><sup>_b_</sup><sup>**K**</sup><sup>_n≥_�</sup><sup>_m_</sup> _n_ =0<sup>**_δ_**</sup><sup>_b_</sup><sup>**K**</sup><sup>_n↑_�</sup><sup>_∞_</sup> _n_ =0<sup>**_δ_**</sup><sup>_b_</sup><sup>**K**</sup><sup>_n_=</sup><sup>**_µ_**(</sup><sup>_b, ·_),whichimplies</sup><sup>**_µ_**</sup><sup>_≥_</sup><sup>**_µ_**(</sup><sup>_b, ·_).</sup>

_LECTURE 13. FEBRUARY 28_

53


However, P _b_ ( _Xn_ = _y, Tb_ = _n_ + 1) = P _b_ ( _Tb > n, Xn_ = _y, Tb_ = _n_ + 1) = _αn_ ( _y_ ) _p_ ( _y, b_ ) by conditioning on _Fn_ , so:


**Lemma 13.5.** _Suppose the Markov chain is irreducible. Suppose_ **_µ_** = **_µ_ P** _, where_ 0 _≤ µ_ ( _x_ ) _≤∞._

_(a) If µ_ ( _b_ ) = 0 _for some b, then µ ≡_ 0 _._

_(b) If µ_ ( _b_ ) = _∞ for some b, then µ ≡∞._

_Proof._ Fix _x_ . There exist _n, m_ such that _p_<sup>_n_</sup> _x,b_<sup>_>_0and</sup><sup>_pm_</sup> _b,x_<sup>_>_0.</sup><sup>**_µ_**=</sup><sup>**_µ_P**</sup><sup>_n_impliesthat</sup><sup>_µ_(</sup><sup>_b_)</sup><sup>_≥µ_(</sup><sup>_x_)</sup><sup>_pn_</sup> _x,b_<sup>,</sup> so if _µ_ ( _b_ ) = 0, then _µ_ ( _x_ ) = 0. **_µ_** = **_µ_ P**<sup>_m_</sup> implies that _µ_ ( _x_ ) _≥ µ_ ( _b_ ) _p_<sup>_m_</sup> _b,x_<sup>,whichimpliesthatif</sup><sup>_µ_(</sup><sup>_b_)=</sup><sup>_∞_,</sup> then _µ_ ( _x_ ) = _∞_ .

**Theorem 13.6.** _Suppose the Markov chain is irreducible and recurrent. Then, there exists an invariant µ which satisfies_ 0 _< µ_ ( _x_ ) _< ∞∀x ∈ S. This µ is unique up to scaling. Either_

_(i) µ_ ( _S_ ) = _∞ and_ E _xTx_ = _∞∀x (_ **_null-recurrent_** _), or_

_(ii) µ_ ( _S_ ) _< ∞ and_ E _xTx < ∞∀x (_ **_positive-recurrent_** _)._

_Proof._ Fix _b_ . Define _µ_ ( _·_ ) = _µ_ ( _b, ·_ ), which satisfies (13.1). Then, _µ_ ( _x_ ) = ( _µP_ )( _x_ ) for _x̸_ = _b_ and ( _µP_ )( _b_ ) = P _b_ ( _Tb < ∞_ ) = 1 = _µ_ ( _b_ ), since the chain is recurrent. Therefore, **_µ_** = **_µ_ P** is invariant. Since _µ_ ( _b_ ) = 1, 13.5 and the assumption that the chain is irreducible implies 0 _< µ_ ( _x_ ) _< ∞∀x_ .

_Why is µ unique?_ Suppose _µ_ ˆ is invariant: rescale to make _µ_ ˆ( _b_ ) = 1. By minimality in 13.4, **_µ_** ˆ _≥_ **_µ_** ( _b, ·_ ). Since they are both invariant, **_µ_** ˆ _−_ **_µ_** ( _b, ·_ ) _≥_ **0** is invariant and equals 0 at _b_ . Then, 13.5 implies that **_µ_** ˆ _−_ **_µ_** ( _b, ·_ ) _≡_ **0** , so **_µ_** ˆ = **_µ_** ( _b, ·_ ).

Consider some invariant _µ_ . _µ_ ( _x, ·_ ) is a scaled version of _µ_ , so _µ_ ( _x, ·_ ) = _cxµ_ ( _·_ ), 0 _< cx < ∞_ , by uniqueness.


which implies that either (i) or (ii) occur.

**Corollary 13.7.** _A finite-state irreducible chain is positive-recurrent._

_Proof._ Last class, we showed that the chain is recurrent, so an invariant _µ_ exists, so


_LECTURE 13. FEBRUARY 28_

54

Therefore, we are in case (ii).

## **Lecture 14**

---

[← February 23](14-february-23.md) · [Up: contents](index.md) · [March 2 →](16-march-2.md)
