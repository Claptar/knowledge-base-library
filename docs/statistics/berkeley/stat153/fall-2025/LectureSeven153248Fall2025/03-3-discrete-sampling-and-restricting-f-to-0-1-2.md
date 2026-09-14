---
title: 3 Discrete sampling and restricting f to [0 , 1 / 2]
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeven153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Discrete sampling and restricting f to [0 , 1 / 2]

**Source:** [`LectureSeven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Often in time series analysis, we work with equally spaced time points and assume that the time variable _t_ takes the values 1 _, . . . , n_ (where _n_ is the sample size). It turns out that if we consider the sinusoid (2) and restrict the time _t_ to 1 _, . . . , n_ , then we can always constrain the frequency parameter _f_ to [0 _,_ 1 _/_ 2]. This is a consequence of the following result.

**Fact 3.1.** _For every f ∈_ ( _−∞, ∞_ ) _and ϕ ∈_ ( _−∞, ∞_ ) _, there exists f_ 0 _∈_ [0 _,_ 1 _/_ 2] _and ϕ_ 0 _∈_ ( _−∞, ∞_ ) _such that_

_s_ ( _t_ ) = _β_ 0 + _R_ cos(2 _πft_ + _ϕ_ ) = _β_ 0 + _R_ cos(2 _πf_ 0 _t_ + _ϕ_ 0) _for all t_ = 1 _, . . . , n._

_Proof._ Consider the following three cases.

1. If _f <_ 0, then we can write cos(2 _πft_ + _ϕ_ ) = cos(2 _π_ ( _−f_ ) _t − ϕ_ ). Clearly, _−f ≥_ 0.

2. If _f ≥_ 1, then we write (below [ _f_ ] is the largest integer less than or equal to _f_ ): cos(2 _πft_ + _ϕ_ ) = cos(2 _π_ [ _f_ ] _t_ + 2 _π_ ( _f −_ [ _f_ ]) _t_ + _ϕ_ ) = cos(2 _π_ ( _f −_ [ _f_ ]) _t_ + _ϕ_ ) _,_

because cos( _·_ ) is periodic with period 2 _π_ . Clearly 0 _≤ f −_ [ _f_ ] _<_ 1.

3. If _f ∈_ [1 _/_ 2 _,_ 1), then

cos(2 _πft_ + _ϕ_ ) = cos(2 _πt −_ 2 _π_ (1 _− f_ ) _t_ + _ϕ_ ) = cos(2 _π_ (1 _− f_ ) _t − ϕ_ )

because cos(2 _πt − x_ ) = cos _x_ for all integers _t_ . Clearly 0 _<_ 1 _− f ≤_ 1 _/_ 2.

Thus the sinusoid _R_ cos(2 _πft_ + _ϕ_ ) equals _R_ cos(2 _πf_ 0 _t_ + _ϕ_ 0) at all integers _t_ for some 0 _≤ f_ 0 _≤_ 1 _/_ 2 and a phase _ϕ_ 0 that is possibly different from _ϕ_ .

From now on, when we discuss sinusoids _s_ ( _t_ ) = _β_ 0 + _R_ cos(2 _πft_ + _ϕ_ ) in the context of _t_ = 1 _, . . . , n_ , we shall assume that the frequency parameter _f_ is restricted to [0 _,_ 1 _/_ 2]. Note also the behavior of the sinusoid for the two frequency extremes _f_ = 0 and _f_ = 1 _/_ 2. When

2

_f_ = 0, the sinusoid _s_ ( _t_ ) is simply a constant function equal to _β_ 0 + _R_ cos( _ϕ_ ). When _f_ = 1 _/_ 2, we have

_s_ ( _t_ ) = _β_ 0 + _R_ cos( _πt_ + _ϕ_ ) = _β_ 0 + _R_ (cos _ϕ_ ) cos( _πt_ ) = _β_ 0 + _R_ ( _−_ 1)<sup>_t_</sup> cos _ϕ._

This sinusoid exhibits the maximum possible oscillation going back and forth between _β_ 0 + _R_ cos _ϕ_ and _β_ 0 _− R_ cos _ϕ_ .

---

[← 2 The Sinusoid](02-2-the-sinusoid.md) · [Up: contents](index.md) · [4 Least Squares Estimation of β, f, σ →](04-4-least-squares-estimation-of-β-f-σ.md)
