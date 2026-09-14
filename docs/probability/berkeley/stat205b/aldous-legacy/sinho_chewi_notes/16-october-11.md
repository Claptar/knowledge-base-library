---
title: October 11
source: https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# October 11

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **14.1 Recap**

Given a PM _µ_ on _S_ 1 _× S_ 2, there exists a marginal PM _µ_ 1 on _S_ 1, and (if _S_ 2 is Borel) there exists a kernel _Q_ from _S_ 1 to _S_ 2 such that (BR1) to (BR3) hold.

_Interpretation_ : If _µ_ is the distribution of ( _X, Y_ ), then _µ_ 1 is the distribution of _X_ , and


### **14.2 Product Measure**

Given PMs _µ_ 1 on ( _S_ 1 _, S_ 2), _µ_ 2 on ( _S_ 2 _, S_ 2), there exists a “ **product measure** ” _µ_ = _µ_ 1 _⊗ µ_ 2 on _S_ 1 _× S_ 2.

1. _µ_ ( _A × B_ ) = _µ_ 1( _A_ ) _× µ_ 2( _B_ ) for _A ∈S_ 1 and _B ∈S_ 2.


3. For measurable _h_ : _S_ 1 _× S_ 2 _→_ R,


provided _h ≥_ 0 or _|h|_ is _µ_ -integrable. This is **Fubini’s Theorem** .

Define _Q_ ( _s_ 1 _, B_ ) = _µ_ 2( _B_ ) _∀s_ 1 _∀B_ . Use (BR1) through (BR3).

Saying dist( _X, Y_ ) = _µ_ 1 _⊗ µ_ 2 is equivalent to _X_ and _Y_ are independent, with dist( _X_ ) = _µ_ 1 and dist( _Y_ ) = _µ_ 2. _Comment_ . 3 works for _σ_ -finite measures, such as _λ_ , the Lebesgue measure on R<sup>1</sup> .

3, in terms of expectations, says that _Eh_ ( _X_ 1 _, X_ 2) = _Eh_ 1( _X_ 1), where _h_ 1( _x_ 1) = _Eh_ ( _x_ 1 _, X_ 2). The general identity is (usually) best viewed as calculating the same quantity in two different ways.

**Example 14.1.** If _X ≥_ 0, then _EX_ = �0 _∞ P_ ( _X ≥ t_ ) d _t_ .

To prove this, let _D_ = _{_ ( _x, t_ ) : _x ≥ t}_ and _µ_ be the distribution of _X_ . _λ_ ( _Dx_ ) = _x_ and _Dt_ = ( _t, ∞_ ), so


53

_LECTURE 14. OCTOBER 11_

54


**Example 14.2.** Let _X_ 1 _, X_ 2 be independent. For _j_ = 1 _,_ 2, _µj_ = dist( _Xj_ ) and _φj_ ( _t_ ) = exp( _itXj_ ) for _t ∈_ R. (Here, _i_ =<sup>_√_</sup> _−_ 1.) We can prove **Parseval’s identity** :

We know that


where


Do this for the other way too, and we get _E_ exp( _iX_ 1 _X_ 2) = _Eφ_ 1( _X_ 2).

**Example 14.3** (Convolution Formula (Undergraduate)) **.** Suppose _X_ and _Y_ have independent densities _fX_ and _fY_ , with distribution functions _FX_ and _FY_ . Then _S_ = _X_ + _Y_ has density


Now, suppose that we have no regularity assumptions. Let _D_ = _{_ ( _x, y_ ) : _x_ + _y ≤ s}_ , _µX_ be the distribution of _X_ , and _µY_ be the distribution of _Y_ .


This implies


Informally, differentiate with respect to _s_ , provided that _µY_ has a density _fY_ .


How do we justify (14.1)? Justify identities involving differentiation by checking the integrated form. We need to show


With a “change of variables”,


_LECTURE 14. OCTOBER 11_

55

so if _µX_ has a density _fX_ , then the change of variables gives


**Example 14.4.** Suppose ( _X, Y_ ) has joint density _f_ ( _x, y_ ) and a marginal density _f_ 1( _x_ ). We can define _f_ ( _y | x_ ) = _f_ ( _x, y_ ) _/f_ 1( _x_ ). Define the kernel _Q_ by _Q_ ( _x, ·_ ) is the PM with density _y �→ f_ ( _y | x_ ). Then this _Q_ is the kernel in the general theorem about _µ_ = dist( _X, Y_ ).

We need to verify (BR1).


### **14.3 RVs & PMs**

_Know_ . _X_ = (Ω _, F, P_ ) _→_ ( _S, S_ ) has a distribution _µ_ = dist( _X_ ), a PM on ( _S, S_ ).

“Given _µ_ , is there an _X_ with dist( _X_ ) = _µ_ ?” has a trivial “yes” answer. We can take ( _S, S, µ_ ).

_Know_ . There exists a RV _U_ with a uniform distribution on [0 _,_ 1].

_Know_ . For any PM _µ_ on R, the RV _X_ = _Fµ_<sup>_−_1(</sup><sup>_U_)hasdist(</sup><sup>_X_) =</sup><sup>_µ_.</sup>

_Know_ . The binary expansion _U_ = 0 _.b_ 1( _U_ ) _b_ 2( _U_ ) _b_ 3( _U_ ) _. . ._ gives an infinite sequence of RVs ( _bi_ ( _U_ )) which are independent,


**Definition 14.5.** ( _S, S_ ) is a **Borel space** if there exists a Borel-measurable _A ⊆ R_ and a bijection _φ_ : _A → S_ such that both _φ_ and _φ_<sup>_−_1</sup> are measurable.

_φ_ , the identity map from ( _S_ 0 _, S_ 1) to ( _S_ 0 _, S_ 2) is measurable iff _S_ 2 _⊆S_ 1. _φ_<sup>_−_1</sup> is measurable iff _S_ 1 _⊆S_ 2. _φ_ and _φ_<sup>_−_1</sup> are measurable is equivalent to _S_ 1 = _S_ 2.

Outsource to analysis:

**Theorem 14.6.** _Every complete separable metric space is a Borel space._

Consider a PM _ν_ on a Borel space ( _S, S_ ). Let _µ_ be the PM on _A_ , the push-forward of _ν_ under _φ_<sup>_−_1</sup> . _X_ = _Fµ_<sup>_−_1(</sup><sup>_U_)isaRVwithdistribution</sup><sup>_µ_.</sup><sup>_ν_isthepush-forwardof</sup><sup>_µ_under</sup><sup>_φ_.Then</sup><sup>_φ_(</sup><sup>_F −_</sup> _µ_<sup>1(</sup><sup>_U_))hasdistri-</sup> bution _ν_ .

We have proved:

_LECTURE 14. OCTOBER 11_

56

**Lemma 14.7.** _Given a PM ν on a Borel space_ ( _S, S_ ) _, there exists a measurable h_ : [0 _,_ 1] _→ S such that h_ ( _U_ ) _has distribution ν._

_Observation_ . Let _πk_ be the _k_ th prime number, and _I_<sup>(</sup><sup>_k_)</sup> = _{πk, πk_<sup>2</sup><sup>_, π_</sup> _k_<sup>3</sup><sup>_, . . . }_isaninfiniteset.</sup> Then _I_<sup>(2)</sup> _, I_<sup>(3)</sup> _, I_<sup>(4)</sup> _, . . ._ are disjoint. Given a sequence _µk_ of PMs on R, define _Uk_ =<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>2</sup><sup>_−ibπ_</sup> _k_<sup>_i_(</sup><sup>_U_).</sup> Then _Uk_ is Uniform[0 _,_ 1], independent as _k_ varies. Define _Xk_ = _Fµ_<sup>_−_</sup> _k_<sup>1(</sup><sup>_Uk_).Wegetaninfinitesequenceofinde-</sup> pendent RVs with the given distribution _µk_ , which are all functions of _some U_ . If **X** = ( _X_ 1 _, X_ 2 _, . . ._ ), then dist( **X** ) is a PM on R<sup>_∞_</sup> with distribution _µ_ 1 _⊗ µ_ 2 _⊗ µ_ 3 _⊗· · ·_ .

## **Lecture 15**

---

[← October 6](15-october-6.md) · [Up: contents](index.md) · [October 13 →](17-october-13.md)
