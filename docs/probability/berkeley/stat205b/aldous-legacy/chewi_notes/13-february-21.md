---
title: February 21
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# February 21

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **11.1 Strong Markov Property**

Let ( _Xn, n_ = 0 _,_ 1 _,_ 2 _, . . ._ ) be a MC on a countable _S_ = _{x, y, z, . . . }_ . Let _Fn_ = _σ_ ( _X_ 0 _, X_ 1 _, . . . , Xn_ ).

**Markov property** : for bounded, measurable _f_ : _S_<sup>_∞_</sup> _→_ R, write _g_ ( _x_ ) = E _xf_ ( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ). Then, E _µ_ [ _f_ ( _Xn, Xn_ +1 _, Xn_ +2 _, . . ._ ) _| Fn_ ] = _g_ ( _Xn_ ).

_Recall_ : A stopping time _T_ : Ω _→{_ 0 _,_ 1 _,_ 2 _, . . . } ∪{∞}_ is such that _{T ≤ n} ∈Fn_ , for all 0 _≤ n < ∞_ . This is equivalent to _{T_ = _n} ∈Fn_ , for all 0 _≤ n < ∞_ .

**Theorem 11.1** (Strong Markov Property) **.** _Write g_ ( _x_ ) = E _xf_ ( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ) _, where f_ : _S_<sup>_∞_</sup> _→_ R _is bounded and measurable. Then,_ E _µ_ [ _f_ ( _XT , XT_ +1 _, . . ._ ) _| FT_ ] = _g_ ( _XT_ ) _a.s. on {T < ∞}._

_Proof. XT_ 1( _T <∞_ ) is _FT_ -measurable. We need to check: for _B ∈FT_ ,


Break over _n_ = 0 _,_ 1 _,_ 2 _, . . ._ . 1 _B_ 1( _T <∞_ ) =<sup>�</sup><sup>_∞_</sup> _n_ =0<sup>1</sup><sup>_B∩{T_=</sup><sup>_n}_=�</sup> _n_<sup>_∞_</sup> =0<sup>1</sup><sup>_A_</sup> _n_<sup>,where</sup><sup>_An_=</sup><sup>_B ∩{T_=</sup><sup>_n}∈Fn_</sup> by the definition of _FT_ . So, it is enough to show


which is


This is the Markov property.

_Special Case_ . Suppose _T_ is such that _XT_ = _y_ (non-random _y_ ) on _{T < ∞}_ . Then,

E _µ_ [ _f_ ( _XT , XT_ +1 _, . . ._ ) _| FT_ ] = _g_ ( _y_ ) on _{T < ∞}, ∀f._

This implies _f_ ( _XT , XT_ +1 _, . . ._ ) and _FT_ are independent on _{T < ∞}_ and


### **11.2 Recurrence Times**

Consider _Ty_<sup>+</sup> def= min _{n ≥_ 1 : _Xn_ = _y}_ and _ρx,y_ = P _x_ ( _Ty_<sup>+</sup><sup>_< ∞_).</sup>

42

_LECTURE 11. FEBRUARY 21_

43

**Lemma 11.2.** _For distinct x, y, z, ρx,z ≥ ρx,yρy,z._

_Proof._


We want to say the second factor is _ρy,z_ by the SMP. Take _f_ ( _x_ 0 _, x_ 1 _, x_ 2 _, . . ._ ) = 1( _xi_ = _z_ for some _i_ ).


Take the expectation over 1( _T <∞_ ).


Define _Ty_<sup>_k_tobethetimeofthe</sup><sup>_k_thvisitto</sup><sup>_y_,</sup><sup>_T_0</sup> _y_<sup>=0,and</sup><sup>_T k_</sup> _y_<sup>+1</sup> = min _{n_ : _n > Ty_<sup>_k, Xn_=</sup><sup>_y}_.Then,</sup> _ρx,y_ = P _x_ ( _Ty_<sup>1</sup><sup>_< ∞_).</sup>

**Theorem 11.3** (Theorem 6.4.1) **.**


_Proof._ It is true for _k_ = 1. By induction, suppose it is true for _k_ .


However,


By induction, this is _ρ_<sup>_k_</sup> _y,y_<sup>.Hence,</sup>

P _x_ ( _Ty_<sup>_k_+1</sup> _< ∞_ ) = _ρ_<sup>_k_</sup> _y,y_<sup>_ρx,y,_</sup>

so the statement is true for _k_ + 1.

**Definition 11.4.** A state _y_ is **recurrent** if _ρy,y_ = 1 and **transient** if _ρy,y <_ 1.

Consider the number of visits to _y_ ,<sup>�</sup><sup>_∞_</sup> _n_ =1<sup>1(</sup><sup>_X_</sup> _n_<sup>=</sup><sup>_y_)=</sup><sup>_N_(</sup><sup>_y_).</sup>

**Lemma 11.5.** _If y is recurrent, then_ P _y_ ( _N_ ( _y_ ) = _∞_ ) = 1 _, so_ E _yN_ ( _y_ ) = _∞. If y is transient, then_ P _y_ ( _N_ ( _y_ ) _≥ k_ ) = P _y_ ( _Ty_<sup>_k< ∞_) =</sup><sup>_ρk_</sup> _y,y_<sup>_,fork_= 0</sup><sup>_,_1</sup><sup>_,_2</sup><sup>_, . . . ,andso_</sup>


_LECTURE 11. FEBRUARY 21_

44


##### **Corollary 11.6.**


**Theorem 11.7** (Theorem 6.4.3) **.** _Suppose x is recurrent and ρx,y >_ 0 _. Then, y is recurrent and ρy,x_ = 1 _. [So, ρx,y_ = 1 _by switching x and y.]_


### **11.3 Elementary Graph Theory**

Consider a directed graph on countable _S_ , the set of vertices. Given **P** = ( _pi,j_ ), put the edge _i → j_ if _pi,j >_ 0. We can define an equivalence relation _R_ by

_i R j ⇐⇒ i_ = _j_ or _∃_ directed path from _i_ to _j_ and from _j_ to _i._

_LECTURE 11. FEBRUARY 21_

45

This partitions _S_ into “strongly connected components” (SCC).

A SCC “ _C_ ” is **open** if _∃i ∈ C, j ∈/ C_ with _i → j_ ( _pi,j >_ 0), **closed** if not.

**Corollary 11.8.** _In a SCC C, either all x ∈ C are recurrent or all x ∈ C are transient._

_Proof._ Suppose some _x ∈ C_ is recurrent. Take any _y ∈ C_ . Then, _ρx,y >_ 0, so by 11.7, _y_ is recurrent.

**Example 11.9.** Suppose _S_ = _{_ 0 _,_ 1 _,_ 2 _, . . . }_ and suppose _p_ 0 _,_ 0 = 1, _pi,i_ +1 _>_ 0, _pi,i−_ 1 _>_ 0. There are two SCCs, one open (and therefore transient) and one closed. So,

P( _Xn_ = 0 ultimately) + P( _Xn →∞_ as _n →∞_ ) = 1 _,_ since _N_ ( _y_ ) _< ∞_ for each _y ≥_ 1.

## **Lecture 12**

---

[← February 16](12-february-16.md) · [Up: contents](index.md) · [February 23 →](14-february-23.md)
