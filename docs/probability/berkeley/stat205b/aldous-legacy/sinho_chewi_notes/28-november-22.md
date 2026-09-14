---
title: November 22
source: https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# November 22

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **26.1 Brownian Motion**

A R<sup>1</sup> -valued process ( _B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) is **(standard) Brownian motion (Wiener process)** if _B_ (0) = 0 and

- (a) _B_ ( _t_ 0) _, B_ ( _t_ 1) _−B_ ( _t_ 0) _, . . . , B_ ( _tn_ ) _−B_ ( _tn−_ 1) are independent, for any 0 _≤ t_ 0 _< t_ 1 _< · · · < tn_ (“independent increments”).

- (b) _B_ ( _t_ ) _− B_ ( _s_ ) has the Normal(0 _, t − s_ ) distribution, where _t − s_ is the variance.

- (c) The sample paths _t �→ B_ ( _t_ ) are continuous. We have a measurable function _B_ ( _ω, t_ ). In other words, for all _ω_ , _t �→ B_ ( _ω, t_ ) is continuous [0 _, ∞_ ) _→_ R.

Write Q2 for the **dyadic rationals** , the set of _{i/_ 2<sup>_j_</sup> _, i, j ≥_ 0 _}_ . We will work on the time interval [0 _,_ 1]. Enumerate Q2 as _q_ 1 _, q_ 2 _, q_ 3 _, . . ._ . For each _n_ , properties (a) and (b) specify a joint distribution of


by relabeling the _qi_ . These are _consistent_ , as _n_ increases. Suppose that we add a time _s_ between _t_ 1 and _t_ 2. We check that Normal(0 _, s − t_ 1) + Normal(0 _, t_ 2 _− s_ ) = Normal(0 _, t_ 2 _− t_ 1) for independent normals. Use the Kolmogorov Extension Theorem to show that there exists a process ( _B_ ( _q_ ) _, q ∈_ Q2 _∩_ [0 _,_ 1]).

For _f_ : Q2 _∩_ [0 _,_ 1] _→_ R and _δ >_ 0, define


If _|t − s| ≤ δ_ , then _|f_<sup>˜</sup> ( _t_ ) _− f_<sup>˜</sup> ( _s_ ) _| ≤ w_ ( _t, δ_ ). Then, (26.1) implies that _f_<sup>˜</sup> is continuous.

95

_LECTURE 26. NOVEMBER 22_

96

Now, it is enough to show _P_ ( _w_ ( _B_ ( _·_ ) _, δ_ ) _≥ ε_ ) _→_ 0 as _δ ↓_ 0, with _ε >_ 0 fixed. This will imply _w_ ( _B_ ( _·_ ) _, δ_ ) _→_ 0 a.s. as _δ →_ 0. Then, we can apply 26.1 to show that there exists _B_<sup>˜</sup> such that ( _t �→ B_<sup>˜</sup> ( _ω, t_ ) is continuous) a.s. It is easy to check that properties (a) and (b) remain true for all real _t_ . Redefine _B_ ( _t, ω_ ) _≡_ 0 _∀t_ on a null set.

Define


Consider 0 _≤ q_ 1 _< q_ 2 _≤_ 1 with _q_ 2 _− q_ 1 _≤_ 1 _/_ 2<sup>_m_</sup> , which means they are either in the same or adjacent intervals. Then _|f_ ( _q_ 2) _− f_ ( _q_ 1) _| ≤_ 3 ¯ _w_ ( _f,_ 2<sup>_−m_</sup> ). It is enough to prove _P_ ( ¯ _w_ ( _B_ ( _·_ ) _,_ 2<sup>_−m_</sup> ) _≥ ε_ ) _→_ 0 as _m →∞_ . ( _Yn ↓_ 0 in probability implies _Yn ↓_ 0 a.s.)

Define _Sm_ = sup0 _≤q≤_ 1 _/_ 2 _m |B_ ( _q_ ) _|_ . _w_ ¯( _B_ ( _·_ ) _,_ 2<sup>_−m_</sup> ) is the maximum of 2<sup>_m_</sup> identically distributed RVs. Then _P_ ( ¯ _w_ ( _B_ ( _·_ ) _,_ 2<sup>_−m_</sup> ) _≥ ε_ ) _≤_ 2<sup>_m_</sup> _P_ ( _Sm ≥ ε_ ).

Fix _m_ and take _n > m_ . Consider _B_ ( _i/_ 2<sup>_n_</sup> _,_ 0 _≤ i ≤_ 2<sup>_n_</sup> _/_ 2<sup>_m_</sup> ). This is a MG. Therefore, _B_<sup>4</sup> ( _i/_ 2<sup>_n_</sup> _, i ≥_ 0) is a sub-MG. Use the _L_<sup>1</sup> maximal inequality.


(If _Z_ is Normal(0 _,_ 1), then _B_ ( _t_ ) =d _t_ 1 _/_ 2 _Z_ .) Let _n →∞_ . Then _P_ ( _Sm > ε_ ) _≤ ε−_ 42 _−_ 2 _mEZ_ 4.


**Theorem 26.2.** _For almost all ω, the sample path t �→ B_ ( _ω, t_ ) _is_ **_nowhere_** _differentiable._

If Brownian motion were differentiable at the origin, we would expect _B_ ( _t_ ) _∼ O_ ( _t_ ) as _t →_ 0, which contradicts the fact that _B_ ( _t_ ) has SD _t_<sup>1</sup><sup>_/_2</sup> .

_Analysis_ . Consider _f_ : [0 _,_ 1] _→_ R. Fix _C < ∞_ . Suppose _∃s_ such that _f_<sup>_′_</sup> ( _s_ ) exists and _|f_<sup>_′_</sup> ( _s_ ) _| ≤ C/_ 2. Then, there exists _n_ 0 such that for _n ≥ n_ 0,


Rewrite the above statement: define _An_ = _{f_ : (26.2) holds for some _s}_ . As _n →∞_ ,


For 0 _≤ k ≤ n −_ 1, define


Given _f ∈ An_ , (26.2) holds for some _s_ , say _k/n ≤ s ≤_ ( _k_ + 1) _/n_ . Near _s_ , the slope is _C_ , so the maximum difference is at most _C ·_ 5 _/n_ , so _Y_ ( _f, k, n_ ) _≤_ 5 _C/n_ . Then


_Probability_ .


_LECTURE 26. NOVEMBER 22_

97

since the increment is Normal(0 _,_ 1 _/n_ ) = _n_<sup>_−_1</sup><sup>_/_2</sup> _Z_ . Regard _B_ ( _·_ ) as a random _f_ .


Then


Let _n →∞_ . _P_ ( _B_ ( _·_ ) _∈ A_ ) = 0.

## **Lecture 27**

---

[← November 17](27-november-17.md) · [Up: contents](index.md) · [November 29 →](29-november-29.md)
