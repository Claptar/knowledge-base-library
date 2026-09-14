---
title: April 27
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# April 27

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **26.1 Local Time for Brownian Motion**

[Morters-Peres book, Chapter 6.]

#### **26.1.1 Existence**

The classic example of a fractal set is _C_ 0 _, C_ 1 _, C_ 2 _, . . ._ . The _Cn_ are closed and _Cn ↓ C∞_ , so _C∞_ is closed and non-empty. area( _C∞_ ) = 0.


Instead, consider PMs where _µn_ is a _uniform_ (relative to area) PM on _Cn_ . Then, _µn → µ∞_ weakly, with supp( _µ∞_ ) = _C∞_ . Intuitively, _µ∞_ is a “uniform” PM on _C∞_ .

For ( _B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ), the zero-set _Z_ ( _ω_ ) = _{t_ : _B_ ( _t, ω_ ) = 0 _}_ is a random closed subset of [0 _, ∞_ ). We know Leb( _Z_ ( _ω_ )) = 0 a.s. since P( _B_ ( _t_ ) = 0) = 0, _t >_ 0. [MP] proves that the Hausdorff dimension of _Z_ ( _ω_ ) is 1 _/_ 2 a.s. If we have any measure on _Z_ ( _ω_ ), we can describe it via


which must have the property


We will give a construction of a process called “local time at 0” which has the property (26.1).

Study _D_ ( _a, b, t_ ), the number of downcrossings completed by time _t_ .

**Theorem 26.1.** _There exists a process_ ( _L_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) _such that for all an ↑_ 0 _, bn ↓_ 0 _,_ lim _a.s. n→∞_<sup>_Z_(</sup><sup>_bn −an_)</sup><sup>_D_(</sup><sup>_an, bn, t_) =</sup><sup>_L_(</sup><sup>_t_)</sup>

Clearly, such _L_ ( _t_ ) has property (26.1).

100

_LECTURE 26. APRIL 27_

101

_Key Idea_ : Take _a < m < b_ . Look at one downcrossing over [ _a, b_ ] followed by an upcrossing. _X_<sup>_∗_</sup> is the number of downcrossings of [ _a, m_ ] and _Y_<sup>_∗_</sup> is the number of downcrossings of [ _m, b_ ]. We know


Then,


where _Y_<sup>_∗∗_</sup> =d _Y ∗_ . So,


independent.

**Lemma 26.2.** _Take a < m < b and a stopping time T with B_ ( _T_ ) _≥ b. Write D_ = _D_ ( _a, b, T_ ) _and D_ ( _a, m, T_ ) _and D_ ( _m, b, T_ ) _. These are related by_


_where the X’s, Y ’s, and D are independent, Xj_ =d _X ∗, j ≥_ 1 _, Yj_ =d _Y ∗, j ≥_ 1 _, X_ 0 _≥_ 0 _, and Y_ 0 _≥_ 0 _._

**Lemma 26.3.** _Take an ↑_ 0 _, bn ↓_ 0 _, and b > b_ 1 _> b_ 2 _> · · ·. The discrete-“time” process_


_is a submartingale and converges a.s. to L_ ( _Tb_ ) _, say, as n →∞._

_Proof._ We can assume _an_ +1 = _an_ , _bn_ +1 _< bn_ .


Note that


This is the sub-MG property.

If _G_ = Geometric(d _p_ ), then E _G_ 2 _≤_ 2 _/p_ 2. [MP] says


_LECTURE 26. APRIL 27_

102

Actually, the LHS is smaller. So, E(2( _bn − an_ ) _D_ ( _an, bn, Tn_ ))<sup>2</sup> _≤_ 8( _b − an_ )<sup>2</sup> _→_ 8 _b_<sup>2</sup> _._

Apply the Sub-MG Convergence Theorem.

After the stopping time _T_<sup>ˆ</sup> _t_ , then _B_<sup>ˆ</sup> ( _u_ ) def= _B_ ( _T_<sup>ˆ</sup> _t_ + _u_ ), _u ≥_ 0 is BM. Apply the construction to _B_<sup>ˆ</sup> ( _n_ ) to get _L_<sup>ˆ</sup> ( _Tb_ ).

_Trick_ : Define


We can show that the paths _t �→ L_ ( _t, ω_ ) are continuous.

#### **26.1.2 Connection with the Maximum Process**

Why is _L_ ( _t_ ) interesting?

Recall _|B_ ( _t_ ) _|_ is “reflecting BM”. Given _B_ ( _t_ ), consider _M_ ( _t_ ) = sup0 _≤s≤t B_ ( _s_ ).

_Fact_ : Given BM _B_ 1( _t_ ) and _M_ 1( _t_ ), the process _B_ 2( _t_ ) def= _M_ 1( _t_ ) _− B_ 1( _t_ ) is distributed as reflecting BM. We have the “same” _L_ ( _t_ ) for _B_ ( _t_ ) and _|B_ ( _t_ ) _|_ .

Given this fact, consider _L_ ( _t_ ), local time at zero for _B_ 2( _t_ ). _t �→ L_ ( _t_ ) has the property (26.1): it is increasing only at _t_ such that _B_ 2( _t_ ) = 0, that is, when _B_ 1( _t_ ) = _M_ 1( _t_ ). But, _t �→ M_ 1( _t_ ) has the same property (26.1). This suggests:

_Fact_ : The process ( _L_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) = (d _M_ ( _t_ ) _,_ 0 _≤ t < ∞_ ).

#### **26.1.3 Occupation Density**

Consider _f_ : [0 _, t_ ] _→_ R. There is always an “occupation measure” on R


This may or may not have a density


If _f_ is smooth,


It is not obvious if “occupation density” exists for BM paths.

**Theorem 26.4** (Local Time = Occupation Density) **.** _There exists_ ( _L_ ( _t, y, ω_ ) _,_ 0 _≤ t < ∞, y ∈_ R) _such that y �→ L_ ( _t, y, ω_ ) _is the occupation density of the function_ ( _s �→ B_ ( _s, ω_ ) _,_ 0 _≤ s ≤ t_ ) _and also_ ( _t, y_ ) _�→ L_ ( _t, y, ω_ ) _is jointly continuous._

_Idea_ : _L_ ( _t,_ 0 _, ω_ ) is the _L_ ( _t_ ) process we constructed.

For each _y_ , we repeat the construction with _an ↑ y_ , _bn ↓ y_ to get _L_ ( _t, y, ω_ ).

_LECTURE 26. APRIL 27_

103

_Fact_ : For BM, E[time spent within [ _a, b_ ] during downcrossings over [ _a, b_ ]] = ( _b − a_ )<sup>2</sup> . In the limit,


By the SLLN, the total amount of time spent in [ _an, bn_ ] _∼_ 2( _bn − an_ ) _D_ ( _an, bn, t_ ).

---

[← April 25](27-april-25.md) · [Up: contents](index.md)
