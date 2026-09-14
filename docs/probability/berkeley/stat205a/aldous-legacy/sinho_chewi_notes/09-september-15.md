---
title: September 15
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# September 15

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **7.1 Polynomial Approximation Theorem**

“ _X_ is Bernoulli( _p_ )” means


IID means independent and identically distributed.

**Theorem 7.1** (Bernstein’s Theorem) **.** _Given a continuous function f_ : [0 _,_ 1] _→_ R _, define_


_fn_ ( _x_ ) _is a polynomial of degree n. Then_ sup _x|fn_ ( _x_ ) _− f_ ( _x_ ) _| →_ 0 _as n →∞._


We want to bound


Explanation: We used _|EY | ≤ E|Y |_ and _Sn/n → x_ in probability by the WWLN. From analysis: set

25

_LECTURE 7. SEPTEMBER 15_

26

_M_ def= sup _|f | < ∞_ . “Uniform continuity” of _f_ says that given _ε >_ 0, _∃δ >_ 0 such that _|y_ 1 _− y_ 2 _| ≤ δ ⇒|f_ ( _y_ 1) _− f_ ( _y_ 2) _| ≤ ε_

Choose _ε >_ 0 and take _δ_ as in the definition of uniform continuity. Also, var( _Sn_ ) = _n_ var( _X_ ) = _nx_ (1 _−x_ ) and _x_ (1 _− x_ ) _≤_ 1 _/_ 4. Then, we know:


### **7.2 Background to Proving a.s. Limits**

#### **7.2.1 Axioms**

If we have events _Bn ↑ B_ , then _P_ ( _Bn_ ) _↑ P_ ( _B_ ). If _Bn ↓ B_ , then _P_ ( _Bn_ ) _↓ P_ ( _B_ ).

For arbitrary events _An_ , the event that “ _An_ happens infinitely often” means<sup>�</sup><sup>_∞_</sup> _m_ =1 � _∞n_ = _m_<sup>_An_.“</sup><sup>_An_ult.”</sup> means<sup>�</sup><sup>_∞_</sup> _m_ =1 � _∞n_ = _m_<sup>_An_.Theseeventsareopposites:(</sup><sup>_An_inf.often)</sup><sup>_c_= (</sup><sup>_A_</sup> _n_<sup>_c_ult.).</sup> If _P_ ( _Bm_ ) = 1, 1 _≤ m < ∞_ , then _P_ (<sup>�</sup><sup>_∞_</sup> _m_ =1<sup>_Bm_) = 1.</sup>

**Lemma 7.2** (Weak) **.** _(i) P_ ( _An inf. often_ ) _≥_ lim sup _n P_ ( _An_ ) _(ii) P_ ( _An ult._ ) _≤_ lim inf _n P_ ( _An_ )

_Proof._

Take _Q →∞_ .

Take _m →∞_ .


#### **7.2.2 Borel-Cantelli Lemmas**

**Lemma 7.3** (First Borel-Cantelli-Lemma) **.** _For arbitrary events_ ( _An,_ 1 _≤ n < ∞_ ) _, if_<sup>�</sup> _n_<sup>_P_(</sup><sup>_An_)</sup><sup>_< ∞,_</sup> _then P_ ( _An inf. often_ ) = 0 _._

_Proof._ Let _Xn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>1</sup><sup>_A_</sup> _i_<sup>bethenumberofeventsthatoccur.Let</sup><sup>_X∞_=�</sup><sup>_∞_</sup> _i_ =1<sup>1</sup><sup>_A_</sup> _i_<sup>_≤∞_.Then</sup> _EX∞_ =<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_P_(</sup><sup>_Ai_)</sup><sup>_< ∞_(byhypothesis),whichimpliesthat</sup><sup>_P_(</sup><sup>_X∞_=</sup><sup>_∞_) = 0.</sup>

**Lemma 7.4** (Second Borel-Cantelli Lemma) **.** _For independent events_ ( _Ai,_ 1 _≤ i < ∞_ ) _,_<sup>�</sup> _i_<sup>_P_(</sup><sup>_Ai_) =</sup><sup>_∞,_</sup> _then P_ ( _An inf. often_ ) = 1 _._

_LECTURE 7. SEPTEMBER 15_

27

_(There are many variants under alternate assumptions.)_

_Proof._ Fix _m_ . We will prove _P_ (<sup>�</sup><sup>_∞_</sup> _n_ = _m_<sup>_An_) = 1,orprove</sup><sup>_P_(�</sup><sup>_∞_</sup> _n_ = _m_<sup>_A_</sup> _n_<sup>_c_) = 0.</sup> Fact: If 0 _≤ x ≤_ 1, then 1 _− x ≤ e_<sup>_−x_</sup> .

Independence implies that

Let _Q ↑∞_ .


_for each ε >_ 0 _, then_ lim sup _n Yn ≤ y a.s._

**Corollary 7.6.** _If_<sup>�</sup> _n_<sup>_P_(</sup><sup>_|Yn| ≥ε_)</sup><sup>_< ∞foreachε >_0</sup><sup>_,thenYn→_0</sup><sup>_a.s._</sup>

_Deterministic Fact_ . For reals ( _yn_ ) and _y_ , “lim sup _n yn ≤ y_ ” is equivalent to “ _yn ≤ y_ + _ε_ ultimately, for each _ε >_ 0”, which is equivalent to “ _yn ≤ y_ + 1 _/j_ ultimately, for each _j ≥_ 1”.

_Proof._ The hypothesis and 7.3 imply that _P_ ( _Yn ≤ y_ + 1 _/j_ ult.) = 1 for each _j_ . Since

_P_ ( _Bj_ ) = 1 _∀j_ = _⇒ P_ ( _Bj_ for all _j_ ) = 1

then _P_ ( _Yn ≤ y_ + 1 _/j_ ult., for each _j ≥_ 1) = 1. By the deterministic fact, _P_ (lim sup _n Yn ≤ y_ ) = 1.

### **7.3** 4 **th Moment SLLN**

SLLN means the **strong law of large numbers** .

**Theorem 7.7** (4th Moment SLLN) **.** _Let_ ( _Xi,_ 1 _≤ i < ∞_ ) _be IID, EX_ = 0 _, and EX_<sup>4</sup> _< ∞. Write Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi.Then_</sup>

_(i) ESn_<sup>4</sup><sup>_≤_3</sup><sup>_n_2</sup><sup>_EX_4</sup>

_(ii) Sn/n →_ 0 _as n →∞._

_LECTURE 7. SEPTEMBER 15_

28

_If EX_ = _µ, applying the theorem to X − µ shows that Sn/n → µ a.s._


Note that _E_ [ _XiXjXkXl_ ] = 0 if some index “ _j_ ” appears only once. For example,


Therefore,


since ( _EY_ )<sup>2</sup> _≤ E_ ( _Y_<sup>2</sup> ).

(ii) Fix _ε >_ 0.

This implies that


By 7.6, _Sn/n →_ 0 a.s. We used the fact that _s_<sup>4</sup> = _|s|_<sup>4</sup> and _s_<sup>2</sup> = _|s|_<sup>2</sup> , but this does not work for the third moment: _s_<sup>3</sup><sup>_̸_</sup> = _|s|_<sup>3</sup> .

**Corollary 7.8.** _If_ ( _Ai,_ 1 _≤ i < ∞_ ) _are independent_ Bernoulli( _p_ ) _, Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>1</sup><sup>_A_</sup> _i_<sup>_,thenSn/n→pa.s._</sup> _as n →∞._

We say “data” for _n_ real numbers _x_ 1 _, . . . , xn_ . The empirical distribution is the uniform distribution on ( _x_ 1 _, . . . , xn_ ). The empirical distribution function is


**Theorem 7.9** (Glivenko-Cantelli Theorem) **.** _If Xi,_ 1 _≤ i < ∞ are IID with an arbitrary distribution function F , let Gn_ ( _ω, x_ ) _be the empirical distribution of_ ( _X_ 1( _ω_ ) _, X_ 2( _ω_ ) _, . . . , Xn_ ( _ω_ )) _, or_


_For fixed x, the events {Xi ≤ x} are IID_ Bernoulli( _G_ ( _x_ )) _. Using the SLLN for events, Gn_ ( _ω, x_ ) _→ G_ ( _x_ ) _as n →∞._

## **Lecture 8**

---

[← September 13](08-september-13.md) · [Up: contents](index.md) · [September 20 →](10-september-20.md)
