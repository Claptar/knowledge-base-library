---
title: February 14
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# February 14

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **9.1 Markov Chains: Big Picture**

|**state space** S|**discrete time**|**continuous time**|
|---|---|---|
|finite|very similar|very similar|
|countable|our focus|similar|
|general: measure theory|(_∗_)|doesn’t exist|
|general: topology|(_∗_)|SDE (starting from BM)<br>semigroup setting|


We will do a little of the sections marked ( _∗_ ).

### **9.2 Measure Theory Background**

“ _X_ and _Y_ are independent” means “ _σ_ ( _X_ ) and _σ_ ( _Y_ ) are independent”.

**Definition 9.1.** _X_ and _Y_ are **conditionally independent (CI) given** _G_ means


_Idea_ : Given _G_ , knowing also _X_ gives no extra information about _Y_ .

_Easy Fact_ . If _X_ and _Y_ are CI given _G_ , if _V_ is _G_ -measurable, then _X_ and ( _Y, V_ ) are CI given _G_ .

_Recall_ . _µ_ is a PM on _S_ 1 _× S_ 2. _µ_ 1 is the marginal PM on _S_ 1. _Q_ is a kernel _Q_ ( _s_ 1 _, B_ ) from _S_ 1 _→ S_ 2. There is a one-to-one correspondence _µ ↔_ ( _µ_ 1 _, Q_ ).

**Lemma 9.2** (The Splice Lemma) **.** _Given spaces S_ 1 _, S_ 2 _, S_ 3 _(Borel spaces), given a PM µ_ 1 _,_ 2 _on S_ 1 _× S_ 2 _and a PM µ_ 2 _,_ 3 _on S_ 2 _× S_ 3 _such that their marginals on S_ 2 _are identical, then there exists a unique PM µ on S_ 1 _× S_ 2 _× S_ 3 _such that, for µ_ = dist( _X_ 1 _, X_ 2 _, X_ 3) _,_

- dist( _X_ 1 _, X_ 2) = _µ_ 1 _,_ 2 _and_ dist( _X_ 2 _, X_ 3) = _µ_ 2 _,_ 3 _, and_

- _X_ 1 _and X_ 2 _are CI given X_ 2 _._

35

_LECTURE 9. FEBRUARY 14_

36

_Proof._ Consider ( _S_ 1 _× S_ 2) _× S_ 3. Specify _µ_ by

- the marginal on _S_ 1 _× S_ 2 is _µ_ 1 _,_ 2,

- the kernel _Q_ from _S_ 1 _× S_ 2 to _S_ 3 is _Q_ (( _s_ 1 _, s_ 2) _, B_ ) = _Q_ 2 _,_ 3( _s_ 2 _, B_ ), where _Q_ 2 _,_ 3 is the kernel _S_ 2 _→ S_ 3 associated with _µ_ 2 _,_ 3.

This specifies _µ_ . Then,


We have checked (9.1), which implies CI. The calculation also says that dist( _X_ 2 _, X_ 3) = _µ_ 2 _,_ 3. _Exercise_ : Prove uniqueness.

### **9.3 Existence of General Markov Chains (Borel Spaces)**

**Theorem 9.3** (Existence of General Markov Chains (Borel Spaces)) **.** _Given Borel S_ 0 _, S_ 1 _, S_ 2 _, . . . , given a PM µ_ 0 _on S_ 0 _, given kernels Qn from Sn to Sn_ +1 _(each n ≥_ 0 _), there exists_ ( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ) _, unique in distribution, such that_

_(a)_ dist( _X_ 0) = _µ_ 0 _, (b) Qn is the conditional probability kernel for Xn_ +1 _given Xn, (c) Xn_ +1 _and_ ( _X_ 0 _, X_ 1 _, . . . , Xn−_ 1) _are CI given Xn (all n ≥_ 1 _), (d)_ ( _Xn, Xn_ +1 _, . . ._ ) _and Fn are CI given Xn._

_Proof._ Suppose (induction) we have constructed ( _X_ 0 _, X_ 1 _, . . . , Xn_ ). Apply the Splice Lemma 9.2 to ( _X_ 0 _, X_ 1 _, . . . , Xn−_ 1) and _Xn_ and _Xn_ +1. We have a joint distribution for ( _X_ 0 _, X_ 1 _, . . . , Xn−_ 1) and _Xn_ . The joint distribution of _Xn_ and _Xn_ +1 is specified by dist( _Xn_ ) and the kernel _Qn_ . The Splice Lemma implies the existence of dist( _X_ 0 _, X_ 1 _, . . . , Xn, Xn_ +1) with the CI property. Apply the Kolmogorov Extension Theorem to get dist( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ).

(c) gives the “one-step ahead”property, but we want the analog for the entire future.

Write _Fn_ = _σ_ ( _X_ 0 _, X_ 1 _, . . . , Xn_ ). (c) and the “Easy Fact” imply (c’) _Fn_ and ( _Xn, Xn_ +1) are CI given _Xn_ . **Claim (d)** : By MT, it is enough to prove, for each _m_ ,

(d’) ( _Xn, Xn_ +1 _, . . . , Xn_ + _m_ ) and _Fn_ are CI given _Xn_ , for all _n_ .

Use induction on _m_ . The statement is true for _m_ = 1 by (c’). We will prove the statement for _m_ = 2. The same argument (exercise) gives the inductive step _m → m_ + 1.

Apply (c’) to _n_ + 1.


_LECTURE 9. FEBRUARY 14_

37

Condition on _Fn_ .


using the _m_ = 1 case of CI. Condition on _Xn_ .

_E_ [ _g_ ( _Xn_ +1 _, Xn_ +2) _| Xn_ ] = _E_ [ _h_ ( _Xn_ +1) _| Xn_ ] _,_ so ( _Xn_ +1 _, Xn_ +2) and _Fn_ are CI given _Xn_ . This is (d’) for _m_ = 2.

In practice, we usually consider time-homogeneous chains: _Sn_ = _S_ , _Qn_ = _Q_ .

_(Idea)_ . Given _Xn_ 0 = _x_ 0, the future process ( _Xn_ 0+ _n, n ≥_ 0) has the same distribution as the process ( _x_ 0 = _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ).

_Formula_ . For bounded, measurable _h_ : _S_<sup>_∞_</sup> _→_ R,


where _g_ ( _x_ ) def= _Eh_ ( _X_<sup>ˆ</sup> 0 _, X_<sup>ˆ</sup> 1 _, . . ._ ), where ( _X_<sup>ˆ</sup> _n, n ≥_ 0) is the chain with _X_ 0 = _x_ .

### **9.4 Elementary Examples**

Recall the following elementary examples for _S_ countable.

The kernel is specified by transition probabilities _pi,j ≡ p_ ( _i, j_ ) = P( _X_ 1 = _j | X_ 0 = _i_ ) which form a transition matrix **P** = ( _pi,j_ : _i, j ∈ S_ ).

**Example 9.4** (Random Walk on Z<sup>_d_</sup> ) **.** Given IID _ξi_ , _i ≥_ 1, Z<sup>_d_</sup> -valued, _Xn_ =<sup>�</sup><sup>_n_</sup> _t_ =1<sup>_ξt_.Then,(</sup><sup>_Xn_)is</sup> Markov, _p_ ( _i, j_ ) = P( _ξ_ = _j − i_ ). Here, _S_ = Z<sup>_d_</sup> .

**Example 9.5** (Renewal Chain) **.** _S_ = Z<sup>+</sup> = _{_ 0 _,_ 1 _,_ 2 _, . . . }_ . Take ( _ξi, i ≥_ 1) to be IID, P( _ξ ≥_ 1) = 1, _Sn_ =<sup>�</sup><sup>_n_</sup> _t_ =1<sup>_ξt_.Define</sup><sup>_Xn_= min</sup><sup>_{n −Sm_:</sup><sup>_Sm≤n}_.ThisisMarkovonZ+.Then,</sup>


**Example 9.6** (Galton-Watson Branching Process) **.** Given a PM _µ_ on _{_ 0 _,_ 1 _,_ 2 _, . . . }_ , _X_ 0 = 1 (1 individual in generation 0). In each generation, each individual has a random (dist = _µ_ ) number of offspring in the next generation. _Xn_ is the population in generation _n_ . This is Markov. _p_ ( _i, j_ ) = P( _ξ_ 1 + _ξ_ 2 + _· · ·_ + _ξi_ = _j_ ) for IID( _µ_ ) RVs ( _ξi_ ).

_S_ is infinite in 9.4 to 9.6.

**Example 9.7** (Ehrenfest Urn Model) **.** There are _B_ balls and 2 boxes. Pick a random ball and move it to the other box. _Xn_ is the number of balls in the left box.


## **Lecture 10**

---

[← February 9](10-february-9.md) · [Up: contents](index.md) · [February 16 →](12-february-16.md)
