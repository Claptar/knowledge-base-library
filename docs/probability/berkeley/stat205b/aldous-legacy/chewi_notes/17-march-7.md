---
title: March 7
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# March 7

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **15.1 Coupling & Mixing Times**

For PMs _µ_ , _ν_ on countable _S_ ,


Consider an irreducible, positive-recurrent **P** with stationary distribution _π_ . Suppose that we construct (( _Xn, Yn_ ) _, n ≥_ 0) such that:

- ( _Xn_ ) is the ( _µ_ 0 _,_ **P** )-chain. Write _µn_ = dist( _Xn_ ).

- ( _Yn_ ) is the ( _π,_ **P** )-chain.

- _Xn_ = _Yn_ for all _n ≥ T_ (for some _T_ ).

Then, _∥µn − π∥≤_ P( _Xn̸_ = _Yn_ ) _≤_ P( _T > n_ ). This is the **MC coupling inequality** .

_Note_ : We did not assume that ( _Xn, Yn_ ) is Markov or _T_ is a stopping time, but in almost every example, these hold.

#### **15.1.1 Card Shuffling by Random Transposition**

**Example 15.1** (“Card Shuffling by Random Transposition”) **.** Consider a deck of _C_ cards. Rule: pick two cards uniformly, independently (they may be the same). Interchange them.

This is a MC on the state space of all _C_ ! decks. The **P** is symmetric, so _π_ is uniform. **P** is aperiodic because _p_ **x** _,_ **x** _≥_ 0. **P** is irreducible by group theory. So (for arbitrary _µ_ 0), the convergence theorem implies _∥µn − π∥→_ 0 as _n →∞_ ( _C_ is fixed). How large must _n_ be (in terms of _C_ ) for _∥µn − π∥_ to be small? This is the **mixing time** .

We will show a coupling with E _T ≤ C_<sup>2</sup> . Then,


59

_LECTURE 15. MARCH 7_

60

so order _C_<sup>2</sup> shuffles are enough. The correct mixing time is order _C_ log _C_ .


The following rule on **P** is the same as the previous rule:

- Pick the card label uniformly at random.

- Pick a position uniformly at random.

- Switch the card with the position.

The rule for coupling is: make the same choices in both decks.

Suppose we pick card _a_ and position 3.


Instead, if we pick card _b_ and position 4:


We will study _Zn_ , the number of unmatched cards. In our first choice, we went from _Zn_ = 4 to _Zn_ +1 = 4. In our second choice, we went to _Zn_ +1 = 3.

_Easy_ :


Study _T_ = min _{n_ : _Zn_ = 0 _}_ . Write _Sm_ = min _{n_ : _Zn ≤ m}_ . Then, _T_ = _S_ 0 = _S_ 1. (15.1) implies that

so


_LECTURE 15. MARCH 7_

61


_Comment_ : Use the structure of **P** to try to construct a coupling so that some notion like _Zn_ (“distance” between states) tends to decrease.

### **15.2 Ergodic Theorem for Markov Chains**

**Theorem 15.2** (Ergodic Theorem for Markov Chains) **.** _Consider an irreducible, positive-recurrent MC. Let π be the stationary distribution. Take f_ : _S →_ R _such that_<sup>�</sup> _x_<sup>_π_(</sup><sup>_x_)</sup><sup>_|f_(</sup><sup>_x_)</sup><sup>_| < ∞.Then,_</sup>


_Proof._ We can reduce to the IID SLLN. We can assume that _f ≥_ 0 (write _f_ = _f_<sup>+</sup> _− f_<sup>_−_</sup> ). Fix state _b_ . Let _T_<sup>_j_</sup> be the time of the _j_ th visit to _b_ .

If we consider a typical sequence for the chain:


Define Λ _j_ = ( _X_ ( _T_<sup>_j_</sup> ) _, X_ ( _T_<sup>_j_</sup> + 1) _, . . . , X_ ( _T_<sup>_j_+1</sup> _−_ 1)). The Strong Markov Property implies that the (Λ _j, j ≥_ 1) are IID. Λ _j_ takes values in<sup>�</sup><sup>_∞_</sup> _d_ =1<sup>_Sd_=</sup><sup>_S_(</sup><sup>_∞_).Define</sup><sup>_Rj_=�</sup> _i_<sup>_T_</sup> =<sup>_j_</sup> _T_<sup>_−j_1</sup><sup>_−_1</sup><sup>_f_(</sup><sup>_Xi_),thesumofthe</sup> _f_ -values over Λ _j−_ 1. The SMP implies ( _R_ 1 _, R_ 2 _, R_ 3 _, . . ._ ) are IID and ( _T_<sup>2</sup> _− T_<sup>1</sup> _, T_<sup>3</sup> _− T_<sup>2</sup> _, . . ._ ) are IID. Apply the IID SLLN.


where _Tb_<sup>+</sup> is the return time to _b_ . We can calculate E _R_ 2 =<sup>�</sup> _x_<sup>_µ_(</sup><sup>_b, x_)</sup><sup>_f_(</sup><sup>_x_).Weknowthat</sup><sup>_µ_(</sup><sup>_b, ·_)isa</sup> multiple of _π_ ( _·_ ), so


Now, apply 15.3 with _r_ ( _t_ ) =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>_f_(</sup><sup>_Xi_),</sup><sup>_tn_=</sup><sup>_T n_,</sup><sup>_rn_=</sup><sup>_Rn_(each</sup><sup>_ω_).Concludethat</sup>


**Lemma 15.3** (Deterministic Lemma, 205A) **.** _Let_ 0 _< tn ↑∞, tn/n → t_<sup>¯</sup> _>_ 0 _. Let ri ≥_ 0 _, such that_

_LECTURE 15. MARCH 7_

62


_Special Case_ : Fix _y_ . Set _f_ ( _x_ ) = 1( _x_ = _y_ ). Then,


where _Nt_ ( _y_ ) is the number of visits to _y_ before _t_ .

## **Lecture 16**

---

[← March 2](16-march-2.md) · [Up: contents](index.md) · [March 9 →](18-march-9.md)
