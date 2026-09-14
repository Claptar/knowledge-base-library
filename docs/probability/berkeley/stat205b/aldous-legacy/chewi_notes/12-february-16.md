---
title: February 16
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# February 16

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **10.1 Markov Chains: Some Classical Methods**

We have a countable _S_ = _{i, j, k, . . . }_ and a transition matrix **P** = ( _pi,j_ ) _i,j∈S_ satisfying _pi,j ≥_ 0 and � _j_<sup>_pi,j_= 1.TheMarkovchain(</sup><sup>_X_0</sup><sup>_, X_1</sup><sup>_, X_2</sup><sup>_, . . ._)has</sup>


We write


Write _µn_ = dist( _Xn_ ). _µn_ can be viewed as a vector **_µ_** _n_ = ( _µn_ ( _i_ ) _, i ∈ S_ ), where _µn_ ( _i_ ) = P( _Xn_ = _i_ ). Then,


In matrix form, we have the **forwards equation** **_µ_** _n_ +1 = **_µ_** _n_ **P** , a vector-matrix product. Then,


so **_µ_** _n_ = **_µ_** 0 **P**<sup>_n_</sup> , where **P**<sup>_n_</sup> = **PP** _· · ·_ **P** is matrix multiplication. We obtained these equations by conditioning on _Xn_ .

Fix a function _f_ : _S →_ R. Consider _νn_ ( _i_ ) = E _if_ ( _Xn_ ). Condition on _X_ 1.


by the Markov property. Write _νn_ ( _i_ ) = E _if_ ( _Xn_ ). The **backwards equation** is **_ν_** _n_ +1 = **P** **_ν_** _n_ , so


We see that ( **P**<sup>_n_</sup> ) _i,j_ = P( _Xn_ = _j | X_ 0 = _i_ ).

38

39

_LECTURE 10. FEBRUARY 16_

The analog of ( _pi,j_ ) on general _S_ is the kerenel _Q_ = _Q_ ( _x, A_ ), which defines two maps.

For _µ ∈ P_ ( _S_ ), we have a map _µ �→ µ_ ˆ, where _µ_ ˆ( _·_ ) = � _µ_ (d _x_ ) _Q_ ( _x, ·_ ). Here, _µ �→ µQ_ . For a function _f_ : _S →_ R, we have a map _f �→ f_<sup>ˆ</sup> , where _f_<sup>ˆ</sup> ( _x_ ) = � _Q_ ( _x,_ d _y_ ) _f_ ( _y_ ). Here, _f �→ Qf_ .

Many questions about finite-state MCs can be answered in terms of the matrix **P** .

#### **10.1.1 Hitting Times**

For _A ⊆ S_ , write


In either case, the hitting time could equal _∞_ if _Xn ∈/ A ∀n_ . Consider _hA_ ( _i_ ) = P _i_ ( _TA < ∞_ ).

First way to study _hA_ : Define the matrix **Q** , the “ **P** -chain killed after entering _A_ ”.


_Easy_ : P _i_ ( _τA_ = _n, XτA_ = _j_ ) = ( **Q**<sup>_n_</sup> ) _i,j_ for _j ∈ A_ .


This is the matrix form of the identity


From this, we obtain


Second way to consider **h** _A_ :

**Proposition 10.1.** _(a)_ **h** = **h** _A satisfies (i) h_ ( _i_ ) =<sup>�</sup> _j_<sup>_pi,jh_(</sup><sup>_j_)</sup><sup>_fori ∈A,_</sup> _(ii) h_ ( _i_ ) = 1 _for i ∈ A, (iii)_ **h** _≥_ 0 _. (b) If_ **h** _satisifes (i) to (iii), then_ **h** _A ≤_ **h** _, so_ **h** _A is the minimal solution of (i) to (iii)._

_Proof._ (a) Condition on the first step for (i). (b) Define **P**<sup>_A_</sup> and ( _Xn_<sup>_A, n ≥_0),the“</sup><sup>**P**-chainstoppedon</sup><sup>_A_”,by</sup>


Given **h** which satisfies (i) to (iii), (i) and (ii) imply **h** = **P**<sup>_A_</sup> **h** and **h** _≥_ **1** _A_ . Therefore, **h** = **P**<sup>_A_</sup> **h** _≥_ **P**<sup>_A_</sup> **1** _A._

_LECTURE 10. FEBRUARY 16_

40


since


Let _n →∞_ . _h_ ( _i_ ) _≥_ P _i_ ( _τA < ∞_ ) _≡ hA_ ( _i_ ).

#### **10.1.2 Generating Functions**

Let _Ty_ = min _{n ≥_ 0 : _Xn_ = _y}_ , _p_<sup>_n_</sup> _x,y_<sup>= P</sup><sup>_x_(</sup><sup>_Xn_=</sup><sup>_y_) = (</sup><sup>**P**</sup><sup>_n_)</sup><sup>_i,j_.The“StrongMarkovProperty”says</sup>


Now, we have a formula for the GF of ( _Ty_ ).


Consider the matrix **Φ** ( _z_ ) with entries _φx,y_ ( _z_ ).


This, in principle, is a formula for the distribution of _Ty_ in terms of **P** .

### **10.2 More Examples of MCs**

**Example 10.2** (Random Walk on an Undirected Finite Graph _G_ = ( _V, E_ )) **.** The state space is _V_ . _v ∈ V_ has some degree _d_ ( _v_ ), the number of edges at _v_ . Suppose _d_ ( _v_ ) _≥_ 1. Then,


**Example 10.3** (Card-Shuffling “Random Transposition” Model) **.** Consider a _n_ card deck. _S_ is the set of _n_ ! orderings. Pick two random cards and interchange them; this is one step of the chain. For configurations **x** and **y** ,


_LECTURE 10. FEBRUARY 16_

41

_p_ **x** _,_ **x** =<sup>1</sup> _n_<sup>_._</sup>

## **Lecture 11**

---

[← February 14](11-february-14.md) · [Up: contents](index.md) · [February 21 →](13-february-21.md)
