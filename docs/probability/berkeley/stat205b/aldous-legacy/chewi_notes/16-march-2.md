---
title: March 2
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# March 2

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **14.1 Stationary Measures**

Consider **P** on countable _S_ .

**Proposition** : Consider the equations


Then, _µ_ ( _b, ·_ ) = E _b_ [number of visits to _·_ before _Tb_ ] is the minimal solution to (14.1) and P _b_ ( _Tb < ∞_ ) = � _x_<sup>_µ_(</sup><sup>_b, x_)</sup><sup>_p_(</sup><sup>_x, b_).</sup>

_µ_ ( _b, ·_ ) is the “ _b_ **-block occupation measure** ”.

**Theorem** : Suppose the Markov chain is irreducible and recurrent. Then, there exists an invariant _µ_ , unique up to scaling. Either

(i) _µ_ ( _S_ ) = _∞_ and E _xTx_ = _∞∀x_ (null-recurrent) or

(ii) _µ_ ( _S_ ) _< ∞_ and E _xTx < ∞∀x_ (positive-recurrent).

In case (ii),


is a stationary distribution.

**Theorem 14.1.** _Suppose the Markov chain is irreducible. Then, it is positive-recurrent if and only if a stationary distribution π exists. If so, then_


_Mystery_ . Starting by defining


and showing _π_ is stationary is not so easy.

55

_LECTURE 14. MARCH 2_

56

_Proof._ Suppose that a stationary distribution _π_ exists. Fix _b_ . Define


_µ_ is invariant, _µ_ ( _b_ ) = 1. “Minimality” in 13.4 implies that _µ_ ( _b, y_ ) _≤ µ_ ( _y_ ) _∀y_ . Therefore,


so the chain is positive-recurrent.

Suppose that the chain is positive-recurrent. 13.6 implies that _π_ exists. Fix _b_ . We know that _µ_ ( _b, ·_ ) is invariant, so


is the unique stationary distribution. This is true for _x_ = _b_ , so


_Warning_ . Suppose _S_ is infinite, the chain is irreducible, and an invariant _µ_ exists with _µ_ ( _S_ ) = _∞_ . This does _not_ imply that the chain is recurrent. Also, this does _not_ imply that the invariant measure is unique up to scaling.

**Example 14.2** (SRW on Z) **.**


For _p̸_ = 1 _/_ 2, there are two invariant measures:


Also, the chain is transient.

For _p_ = 1 _/_ 2, the chain is recurrent and there is a unique (up to scaling) invariant _µ_ ( _i_ ) _≡_ 1.

**Example 14.3** (Reflecting RW on Z<sup>+</sup> ) **.**


If _p >_ 1 _/_ 2, the chain is transient.

If _p_ = 1 _/_ 2, the chain is null-recurrent. If _p <_ 1 _/_ 2, the chain is positive-recurrent.

_LECTURE 14. MARCH 2_

57

### **14.2 Convergence to the Stationary Distribution**

_Know_ . If _∃µ_ 0 such that P _µ_ 0( _Xn_ = _j_ ) _−−−−→n→∞ π_ ( _j_ ) _∀j_ for some probability distribution _π_ , then _π_ is stationary.

**Theorem 14.4** (The MC Convergence Theorem) **.** _Suppose the chain is irreducible and positive-recurrent, so the stationary π exists. If the chain is also aperiodic, then_ P _µ_ 0( _Xn_ = _j_ ) _−−−−→n→∞ π_ ( _j_ ) _∀j ∀µ_ 0 _._

_Proof._ Fix _µ_ 0. We shall construct a Markov chain on _S × S_ , call it (( _Xn, Yn_ ) _, n_ = 0 _,_ 1 _, . . ._ ), such that (i) ( _Xn, n ≥_ 0) is the ( _µ_ 0 _,_ **P** )-chain,

(ii) ( _Yn, n ≥_ 0) is the stationary ( _π,_ **P** )-chain,

(iii) _Xn_ = _Yn ∀n ≥ T_ , where _T < ∞_ a.s.

This will prove the theorem because

_|_ P _µ_ 0( _Xn_ = _j_ ) _− π_ ( _j_ ) _|_ = _|_ P _µ_ 0( _Xn_ = _j_ ) _−_ P( _Yn_ = _j_ ) _| ≤_ P( _Xn̸_ = _Yn_ ) _≤_ P( _T > n_ ) _→_ 0 as _n →∞._ This is the **MC coupling method** .

The transition matrix on _S × S_ is


The initial distribution is _µ_ 0 _⊗ π_ . Two particles initially move as independent MCs, but after meeting, they stick together and move as a single MC.

_Fussy argument: why is_ ( _Xn, n ≥_ 0) _Markov?_

P( _Xn_ +1 = _xn_ +1 _| Xn_ = _xn, Yn_ = _yn,_ past of both proceses) = P( _Xn_ +1 = _xn_ +1 _| Xn_ = _xn, Yn_ = _yn_ ) = P( _Xn_ +1 = _xn_ +1 _| Xn_ = _xn_ ) _._ ���� form of TM

Condition on the past of _Xn_ .


which is the Markov property for ( _Xn_ ).

Define _T_ meet = min _{n_ : _Xn_ = _Yn}_ . Then, _Xn_ = _Yn ∀n ≥ T_ meet. It is enough to prove _T_ meet _< ∞_ a.s. Consider (( _X_<sup>ˆ</sup> _n, Y_<sup>ˆ</sup> _n_ ) _, n ≥_ 0) with ( _X_<sup>ˆ</sup> _n_ ) the ( _µ_ 0 _,_ **P** )-chain, ( _Y_<sup>ˆ</sup> _n_ ) the ( _π,_ **P** )-chain, independent. This is a **product chain** . The distribution of _T_ meet is the same.

Let **Q**<sup>ˆ</sup> be the transition matrix for the product chain. **P** is aperiodic, so


for large _n_ by aperiodicity of **P** . Hence, **Q**<sup>ˆ</sup> is irreducible.

It is easy to see that _π ⊗ π_ is invariant and stationary for **Q**<sup>ˆ</sup> . 14.1 implies that the product chain **Q**<sup>ˆ</sup> is positive-recurrent. Take state ( _b, b_ ). _T_ ( _b,b_ ) _< ∞_ a.s. in the product chain, so _T_ meet _≤ T_ ( _b,b_ ) _< ∞_ a.s. in the product chain, so also in the coupled chain.

_LECTURE 14. MARCH 2_

58

_Note for later_ : In order to show


it is enough to show that the product chain is irreducible and recurrent.

**Proposition 14.5.** _Suppose that the chain is irreducible and not positive-recurrent. Then,_


_Proof._ Reduce to the aperiodic case. First, suppose that the chain is transient.


by transience. Therefore, P _µ_ ( _Xn_ = _j_ ) _→_ 0.

So, suppose that the chain is null-recurrent. Consider the product chain. Suppose that the product chain is transient. As above, P _µ⊗µ_ ( _Xn_ = _j, Yn_ = _j_ ) _→_ 0, so (P _µ_ ( _Xn_ = _j_ ))<sup>2</sup> _→_ 0. Suppose that **Q**<sup>ˆ</sup> is recurrent. If the result is false, then _∃µ_ 0 _∃b ∃_ subsequence ( _jn_ ) such that


By compactness, there exists a subsequence _kn_ such that


By the coupling argument, (14.2) holds for all _µ_ . [See notes.] This implies that ( _αy_ ) is a stationary distribution, so the chain is positive-recurrent.

## **Lecture 15**

---

[← February 28](15-february-28.md) · [Up: contents](index.md) · [March 7 →](17-march-7.md)
