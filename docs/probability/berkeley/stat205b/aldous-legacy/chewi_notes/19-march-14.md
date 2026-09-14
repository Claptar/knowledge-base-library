---
title: March 14
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# March 14

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **17.1 Martingale Methods for Markov Chains**

#### **17.1.1 Harmonic Functions**

_Setting_ . ( _Xn_ ) is an irreducible MC on countable _S_ . **P** = ( _p_ ( _x, y_ )). We have _h_ : _S →_ [0 _, ∞_ ) and let _Fn_ = _σ_ ( _X_ 0 _, X_ 1 _, . . . , Xn_ ). Suppose E _h_ ( _X_ 0) _< ∞_ . Then, ( _h_ ( _Xn_ ) _,_ 0 _≤ n < ∞_ ) is a MG if and only if _h_ ( _x_ ) =<sup>�</sup> _y_<sup>_p_(</sup><sup>_x, y_)</sup><sup>_h_(</sup><sup>_y_)</sup><sup>_∀x ∈S_.</sup>


which is the MG property.

_h_ is **harmonic** w.r.t. **P** .

( _h_ ( _Xn_ ) _,_ 0 _≤ n < ∞_ ) is a super-MG if and only if _h_ ( _x_ ) _≥_<sup>�</sup> _y_<sup>_p_(</sup><sup>_x, y_)</sup><sup>_h_(</sup><sup>_y_).</sup><sup>_h_is</sup><sup>**superharmonic**w.r.t.</sup><sup>**P**.</sup>

**Lemma 17.1.** _If_ ( _Xn_ ) _is recurrent and h ≥_ 0 _is superharmonic, then h is constant._

_Proof. h_ ( _Xn_ ) _≥_ 0 is a super-MG, so (MG convergence) _h_ ( _Xn_ ) _→_ some _H∞ ≥_ 0 a.s.

For states _y_ 1, _y_ 2, _Xn_ visits _y_ infinitely often, so _H∞_ = _h_ ( _y_ 1) = _h_ ( _y_ 2) a.s., so _h_ is constant.

_Fact_ . A transient chain may or may not have the property

there exists a non-constant harmonic _h_ with 0 _≤ h ≤_ 1 _._ (17.1)

**Example 17.2.** Consider the following chain.


67

_LECTURE 17. MARCH 14_

68

P( _Xn →∞_ or _Xn →−∞_ ) = 1. _h_ ( _x_ ) def= P _x_ ( _Xn →_ + _∞_ ). Note that _h_ ( _Xn_ +1) = P _x_ ( _Xn →∞| Xm, Xm−_ 1 _, Xm−_ 2 _, . . ._ ) _≡_ P( _A | Fm_ ) is always a MG _._ Hence, _h_ is harmonic. It is easy to see that _h_ ( _x_ ) _→_ 1 as _x →∞_ and _h_ ( _x_ ) _→_ 0 as _x →−∞_ .

**Example 17.3.** ( _ξi, i ≥_ 1) are IID Z<sup>_d_</sup> -valued. _Xn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_ξi_isaMConZ</sup><sup>_d_.</sup> Suppose _h_ is harmonic, 0 _≤ h ≤_ 1. _h_ ( _Xn_ ) is a MG, so _h_ ( _Xn_ ) _−−→_<sup>a.s.</sup> _H∞_ , say. _H∞_ is in the exchangeable _σ_ -field of ( _ξi,_ 1 _≤ i < ∞_ ), which is trivial by the Hewitt-Savage 0-1 law. So, _H∞_ is constant. Since _h_ ( _Xn_ ) is a MG, then _h_ ( _Xn_ ) = E[ _H∞ | Fn_ ] is constant.

_Remark_ . “Martin boundary theory” discusses extreme harmonic functions and the number of ways that a countable-state chain can go to infinity.

#### **17.1.2 Mean Hitting Times**

**Lemma 17.4.** _Fix A ⊆ S. TA_ = min _{n ≥_ 0 : _Xn ∈ A}. (a) Suppose h_ ( _x_ ) def= E _xTA < ∞∀x ∈ S. Define Yn_ = _h_ ( _Xn_ ) + _n. Then,_ ( _Yn∧TA ,_ 0 _≤ n < ∞_ ) _is a MG. (b) If_ 0 _≤ h < ∞ satisfies h_ ( _x_ ) _≥_<sup>�</sup> _y_<sup>_p_(</sup><sup>_x, y_)</sup><sup>_h_(</sup><sup>_y_) + 1</sup><sup>_∀x∈/A,then_E</sup><sup>_xTA≤h_(</sup><sup>_x_)</sup><sup>_∀x._</sup>

_Proof._ (a) For _x ∈/ A_ , then condition on the first step _h_ ( _x_ ) = 1 + E _xh_ ( _X_ 1) = 1 +<sup>�</sup> _y_<sup>_p_(</sup><sup>_x, y_)</sup><sup>_h_(</sup><sup>_y_).</sup> Then, _Y_ 0 = E[ _Y_ 1 _| X_ 0] on _{TA >_ 0 _}_ . By the same argument, _Yn_ = E[ _Yn_ +1 _| Fn_ ] on _{TA > n}_ , which implies that ( _Yn∧TA , n ≥_ 0) is a MG.

- (b) Given such an _h_ , write _Yn_ = _h_ ( _Xn_ ) + _n_ . The above argument implies that ( _Yn∧TA , n ≥_ 0) is a super-MG. By MG convergence, _Yn∧TA →_ some _Z_ a.s. as _n →∞_ and E _Z ≤_ E _Y_ 0. However, _Yn →∞_ as _n →∞_ , so _TA < ∞_ a.s. So, _Z_ = _YTA ≥ TA_ .

E _xTA ≤_ E _xZ ≤_ E _xY_ 0 = _h_ ( _x_ ) _._

#### **17.1.3 Criteria for Recurrence on Infinite** _S_

We can use these ideas to prove recurrence/transience.

_Idea_ . _h_ ( _x_ ) is the distance from _x_ to a reference state. If _h_ tends to decrease, then we have recurrence. If _h_ tends to increase, then we have transience.

**Proposition 17.5.** _If there exists h_ : _S →_ [0 _, ∞_ ) _and a finite B ⊆ S such that_

- _(i) h_ ( _x_ ) _≥_<sup>�</sup> _y_<sup>_p_(</sup><sup>_x, y_)</sup><sup>_h_(</sup><sup>_y_)</sup><sup>_∀x∈/B,_</sup>

- _(ii) |{x_ : _h_ ( _x_ ) _≤ M }| < ∞∀M < ∞,_

_then the chain is recurrent._

_Proof._ (i) implies that _h_ ( _Xn∧TB_ ) is a super-MG, so _h_ ( _Xn∧TB_ ) _−−→_<sup>a.s.</sup> some _Z_ as _n →∞_ . By contradiction: _Xn_ visits each state only finitely often. So, (ii) implies _h_ ( _Xn_ ) _→∞_ a.s. Therefore, _TB < ∞_ a.s. Since this is true for every initial state, P( _Xn_ visits _B_ infinitely often) = 1. However, _B_ is finite, so _Xn_ visits

_LECTURE 17. MARCH 14_

69

_B_ only finitely often, which is a contradiction.

**Proposition 17.6.** _As above, but strengthen (i) to ∃δ >_ 0 _such that (iii) h_ ( _x_ ) _≥_<sup>�</sup> _y_<sup>_p_(</sup><sup>_x, y_)</sup><sup>_h_(</sup><sup>_y_) +</sup><sup>_δ∀x∈/B_</sup> _and also assume (iv) |{y_ : _p_ ( _x, y_ ) _>_ 0 _}| < ∞ for x ∈ B. Then, the chain is positive-recurrent._


Consider _Zm_ = “the chain watched only on _B_ ” = _XSm_ , where _Sm_ is the time of the _m_ th visit to _B_ . ( _Zm_ ) is an irreducible, finite-state chain, so it has a stationary distribution _π_ ˆ.


From the homework, _π_ is an invariant measure for **P** and


so the chain is positive-recurrent.

_Later Homework_ . Show the corresponding sufficient condition for transience.

## **Lecture 18**

---

[← March 9](18-march-9.md) · [Up: contents](index.md) · [March 16 →](20-march-16.md)
