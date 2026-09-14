---
title: List of frequently used notation
source: https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/bmbook.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# List of frequently used notation

**Source:** [`bmbook.pdf`](https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **Numbers:**

- _⌈x⌉_ the smallest integer bigger or equal to _x_

- _⌊x⌋_ the largest integer smaller or equal to _x_

### **Topology of Euclidean space** R<sup>_d_</sup> **:**

R<sup>_d_</sup> Euclidean space consisting of all column vectors _x_ = ( _x_ 1 _, . . . , xd_ )<sup>T</sup> � � _d | · |_ Euclidean norm _| x|_ = �� _x_<sup>2</sup> _i i_ =1 � _B_ ( _x, r_ ) the open ball of radius _r >_ 0 centred in _x ∈_ R<sup>_d_</sup> , i.e. _B_ ( _x, r_ ) = _{y ∈_ R<sup>_d_</sup> : _| x − y| < r} U_ closure of the set _U ⊂_ R<sup>_d_</sup> _∂U_ boundary of the set _U ⊂_ R<sup>_d_</sup> B( _A_ ) the collection of all Borel subsets of _A ⊂_ R<sup>_d_</sup> .

### **Binary relations:**

_a ∧ b_ the minimum of _a_ and _b a ∨ b_ the maximum of _a_ and _b X_ =d _Y_ the random variables _X_ and _Y_ have the same distribution _a_ ( _n_ ) _≍ b_ ( _n_ ) the ratio of the two sides is bounded from above and below by positive constants that do not depend on _n a_ ( _n_ ) _∼ b_ ( _n_ ) the ratio of the two sides converges to one.

9

### **Vectors, functions, and measures:**

_Id d × d_ identity matrix 1 _A_ indicator function with 1 _A_ ( _x_ ) = 1 if _x ∈ A_ and 0 otherwise _δx_ Dirac measure with mass concentrated on _x_ , i.e. _δx_ ( _A_ ) = 1 if _x ∈ A_ and 0 otherwise _f_<sup>+</sup> the positive part of the function _f_ , i.e. _f_<sup>+</sup> ( _x_ ) = _f_ ( _x_ ) _∨_ 0 _f_<sup>_−_</sup> the negative part of the function _f_ , i.e. _f_<sup>_−_</sup> ( _x_ ) = _−_ ( _f_ ( _x_ ) _∧_ 0) _Ld_ or _L_ Lebesgue measure on R<sup>_d_</sup> _σx,r_ ( _d −_ 1)-dimensional surface measure on _∂B_ ( _x, r_ ) _⊂_ R<sup>_d_</sup> if _x_ = 0, _r_ = 1 we also write _σ_ = _σ_ 0 _,_ 1 _σx,r ϖx,r_ uniform distribution on _∂B_ ( _x, r_ ), _ϖx,r_ = _σx,r_ ( _∂B_ ( _x,r_ ))<sup>,</sup> if _x_ = 0, _r_ = 1 we also write _ϖ_ = _ϖ_ 0 _,_ 1.

### **Function spaces:**

- _C_ ( _K_ ) topological space of all continuous functions on the compact _K ⊂_ R<sup>_d_</sup> , equipped with the supremum norm _∥f ∥_ = sup _x∈K |f_ ( _x_ ) _|_

### **Probability measures and** _σ_ **-algebras:**

P _x_ a probability measure on a measure space (Ω _, A_ ) such that the process _{B_ ( _t_ ): _t ≥_ 0 _}_ is a Brownian motion started in _x_ E _x_ the expectation associated with P _x_ p( _t, x, y_ ) the transition density of Brownian motion P _x{B_ ( _t_ ) _∈ A}_ = � _A_<sup>p(</sup><sup>_t, x, y_)</sup><sup>_dy_</sup> _F_<sup>0</sup> ( _t_ ) the smallest _σ_ -algebra that makes _{B_ ( _s_ ): 0 _≤ s ≤ t}_ measurable _F_<sup>+</sup> ( _t_ ) the right-continuous augmentation _F_<sup>+</sup> ( _t_ ) =<sup>�</sup> _s>t_<sup>_F_0(</sup><sup>_s_).</sup>

10

### **Stopping times:**

For any Borel sets _A_ 1 _, A_ 2 _, . . . ⊂_ R<sup>_d_</sup> and a Brownian motion _B_ : [0 _, ∞_ ) _→_ R<sup>_d_</sup> ,

_τ_ ( _A_ 1) := inf _{t ≥_ 0: _B_ ( _t_ ) _∈ A_ 1 _},_ the entry time into _A_ 1 _,_


the time to enter _A_ 1 and then _A_ 2 and so on until _An_ .

**Systems of subsets in** R<sup>_d_</sup> **:**

For any fixed _d_ -dimensional unit cube Cube = _x_ + [0 _,_ 1]<sup>_d_</sup> we denote:

- D _k_ family of all half-open dyadic subcubes _D_ = _x_ +<sup>�</sup><sup>_d_</sup> _i_ =1 � _ki_ 2<sup>_−k_</sup> _,_ ( _ki_ + 1)2<sup>_−k_�</sup> _⊂_ R<sup>_d_</sup> , _ki ∈{_ 0 _, . . . ,_ 2<sup>_k_</sup> _−_ 1 _},_ of sidelength 2<sup>_−k_</sup>

- D all half-open dyadic cubes D =<sup>�</sup><sup>_∞_</sup> _k_ =0<sup>D</sup><sup>_k_inCube</sup>

- C _k_ family of all compact dyadic subcubes _D_ = _x_ +<sup>�</sup><sup>_d_</sup> _i_ =1 � _ki_ 2<sup>_−k_</sup> _,_ ( _ki_ + 1)2<sup>_−k_�</sup> _⊂_ R<sup>_d_</sup> , _ki ∈{_ 0 _, . . . ,_ 2<sup>_k_</sup> _−_ 1 _},_ of sidelength 2<sup>_−k_</sup>

- C all compact dyadic cubes C =<sup>�</sup><sup>_∞_</sup> _k_ =0<sup>C</sup><sup>_k_inCube.</sup>

### **Potential theory:**

For a metric space ( _E, ρ_ ) and mass distribution _µ_ on _E_ :

_φα_ ( _x_ ) the _α_ -potential of a point _x ∈ E_ defined as _φα_ ( _x_ ) = � _ρd_ ( _x,yµ_ <u>(</u> _<u>y</u>_ ))<sup>_α,_</sup> _Iα_ ( _µ_ ) the _α_ -energy of the measure _µ_ defined as _Iα_ ( _µ_ ) = �� _dµρ_ <u>((</u> _xx,y_ <u>)</u> _dµ_ )<sup>_α_</sup> <u>(</u> _<u>y</u>_ <u>)</u><sup>,</sup>

Cap _α_ ( _E_ ) the (Riesz) _α_ -capacity of _E_ defined as Cap _α_ ( _E_ ) = sup _{Iα_ ( _µ_ )<sup>_−_1</sup> : _µ_ ( _E_ ) = 1 _}_ .

For a general kernel _K_ : _E × E →_ [0 _, ∞_ ]:

_Uµ_ ( _x_ ) the potential of _µ_ at _x_ defined as _Uµ_ ( _x_ ) = � _K_ ( _x, y_ ) _dµ_ ( _y_ ), _IK_ ( _µ_ ) _K_ -energy of _µ_ defined as _IK_ ( _µ_ ) = �� _K_ ( _x, y_ ) _dµ_ ( _x_ ) _dµ_ ( _y_ ) _,_ Cap _K_ ( _E_ ) _K_ -capacity of _E_ defined as Cap _K_ ( _E_ ) = sup _{IK_ ( _µ_ )<sup>_−_1</sup> : _µ_ ( _E_ ) = 1 _}._

11

If _K_ ( _x, y_ ) = _f_ ( _ρ_ ( _x, y_ )) we also write:

_If_ ( _µ_ ) instead of _IK_ ( _µ_ ), Cap _f_ ( _E_ ) instead of Cap _K_ ( _E_ ).

### **Sets and processes associated with Brownian motion:**

For a linear Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ :

_{M_ ( _t_ ): _t ≥_ 0 _}_ the maximum process defined by _M_ ( _t_ ) = sup _s≤t B_ ( _s_ ), Rec the set of record points _{t ≥_ 0: _B_ ( _t_ ) = _M_ ( _t_ ) _}_ , Zero the set of zeros _{t ≥_ 0: _B_ ( _t_ ) = 0 _}_ .

For a Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ in R<sup>_d_</sup> for _d ≥_ 1:

Graph the graph _{_ ( _t, B_ ( _t_ )): _t ≥_ 0 _} ⊂_ R<sup>_d_+1</sup> , Range the range _{B_ ( _t_ ): _t ≥_ 0 _} ⊂_ R<sup>_d_</sup> .

12

### CHAPTER 0

---

[← Foreword](02-foreword.md) · [Up: contents](index.md) · [Motivation →](04-motivation.md)
