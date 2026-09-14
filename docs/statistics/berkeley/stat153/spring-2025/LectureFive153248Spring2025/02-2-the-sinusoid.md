---
title: 2 The Sinusoid
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFive153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFive153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 The Sinusoid

**Source:** [`LectureFive153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFive153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

When we say sinusoid, we refer to the following function of time (t):


_R_ is called the _amplitude_ , _f_ is called the _frequency_ and Φ is called the _phase_ . The quantity 1 _/f_ is called the _period_ and 2 _πf_ is termed the _angular frequency_ . Sometimes, we shall use the notation _ω_ = 2 _πf_ for the angular frequency.

Using the formula cos( _α_ + _β_ ) = (cos _α_ )(cos _β_ ) _−_ (sin _α_ )(sin _β_ ), we can represent the sinusoid (1) in the following equivalent alternative form:


The parameters _A, B_ in (2) are related to _R, φ_ in (1) via _A_ = _R_ cos _φ_ and _B_ = _R_ sin _φ_ . While working with models involving sinuosoids, we use the representation (2) because the parameters _A_ and _B_ appear linearly in (2).

### **2.1 Discrete sampling and restricting** _f_ **to** [0 _,_ 1 _/_ 2]

Often in time series analysis, we work with equally spaced time points and assume that the time variable _t_ takes the values 1 _, . . . , n_ (where _n_ is the sample size). It turns out that if we consider the sinusoid (1) and restrict the time _t_ to 1 _, . . . , n_ , then we can always constrain the frequency parameter _f_ to [0 _,_ 1 _/_ 2]. This is a consequence of the following result.

**Fact 2.1.** _For every f ∈_ ( _−∞, ∞_ ) _and φ ∈_ ( _−∞, ∞_ ) _, there exists f_ 0 _∈_ [0 _,_ 1 _/_ 2] _and φ_ 0 _∈_ ( _−∞, ∞_ ) _such that_


1

_Proof._ Consider the following three cases.

1. If _f <_ 0, then we can write cos(2 _πft_ + _φ_ ) = cos(2 _π_ ( _−f_ ) _t − φ_ ). Clearly, _−f ≥_ 0.

2. If _f ≥_ 1, then we write (below [ _f_ ] is the largest integer less than or equal to _f_ ): cos(2 _πft_ + _φ_ ) = cos(2 _π_ [ _f_ ] _t_ + 2 _π_ ( _f −_ [ _f_ ]) _t_ + _φ_ ) = cos(2 _π_ ( _f −_ [ _f_ ]) _t_ + _φ_ ) _,_

because cos( _·_ ) is periodic with period 2 _π_ . Clearly 0 _≤ f −_ [ _f_ ] _<_ 1.

3. If _f ∈_ [1 _/_ 2 _,_ 1), then

cos(2 _πft_ + _φ_ ) = cos(2 _πt −_ 2 _π_ (1 _− f_ ) _t_ + _φ_ ) = cos(2 _π_ (1 _− f_ ) _t − φ_ )

because cos(2 _πt − x_ ) = cos _x_ for all integers _t_ . Clearly 0 _<_ 1 _− f ≤_ 1 _/_ 2.

Thus the sinusoid _R_ cos(2 _πft_ + _φ_ ) equals _R_ cos(2 _πf_ 0 _t_ + _φ_ 0) at all integers _t_ for some 0 _≤ f_ 0 _≤_ 1 _/_ 2 and a phase _φ_ 0 that is possibly different from _φ_ .

From now on, when we discuss sinusoids _s_ ( _t_ ) = _R_ cos(2 _πft_ + _φ_ ) in the context of _t_ = 1 _, . . . , n_ , we shall assume that the frequency parameter _f_ is restricted to [0 _,_ 1 _/_ 2]. Note also the behavior of the sinusoid for the two frequency extremes _f_ = 0 and _f_ = 1 _/_ 2. When _f_ = 0, the sinusoid _s_ ( _t_ ) is simply a constant function equal to _R_ cos( _φ_ ). When _f_ = 1 _/_ 2, we have

_s_ ( _t_ ) = _R_ cos( _πt_ + _φ_ ) = _R_ (cos _φ_ ) cos( _πt_ ) = _R_ ( _−_ 1)<sup>_t_</sup> cos _φ._

This sinusoid exhibits the maximum possible oscillation going back and forth between _R_ cos _φ_ and _−R_ cos _φ_ .

---

[← 1 Nonlinear Regression](01-1-nonlinear-regression.md) · [Up: contents](index.md) · [3 The sinusoidal model →](03-3-the-sinusoidal-model.md)
