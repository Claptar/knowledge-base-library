---
title: 1 Parameter Interpretation in (1)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Parameter Interpretation in (1)

**Source:** [`LectureTen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let _µt_ denote the deterministic part of model (1), i.e.,

_µt_ = _β_ 0 + _β_ 1( _t −_ 1) + _β_ 2ReLU( _t −_ 2) + _β_ 3ReLU( _t −_ 3) + _· · ·_ + _βn−_ 1ReLU( _t −_ ( _n −_ 1)) _._ (3) The model (1) can then be written as


Here _µt_ represents the trend function that we aim to estimate from the data. For illustration, consider _yt_ to be the logarithm of California’s population in year _t_ . The trend function _µt_ captures the underlying systematic pattern in the population growth, while _ϵt_ accounts for random fluctuations around this trend.

1

Sometimes, we can also interpret _µt_ as the ’actual’ data and _ϵt_ as the measurement error causing _µt_ to be observed as _yt_ . For example, in the population example, _µt_ would represent the actual population (on log scale) while _yt_ would represent our noisy measurement of it.

The parameters _β_ 0 _, β_ 1 _, β_ 2 _, . . . , βn−_ 1 can be interpreted in terms of _µt_ as follows. We will focus on the population example here for simplicity. Plugging _t_ = 1 in (3), we get


So _β_ 0 can be interpreted as the actual population on log scale (or the value of the trend function) at time _t_ = 1. Plugging _t_ = 2 in (3), we get _µ_ 2 = _β_ 0 + _β_ 1 = _µ_ 1 + _β_ 1 so that


If _Pt_ = exp( _µt_ ) denotes the population on the original scale, then


Here we used the fact that log _x ≈ x −_ 1 if _x_ is close to 1. In other words, 100 _β_ 1 can be interpreted as the percentage growth of the population from year 1 to year 2.

For _β_ 2, let us plug _t_ = 3 in (3) to get _µ_ 3 = _β_ 0 + 2 _β_ 1 + _β_ 2. Replacing _β_ 0 = _µ_ 1 and _β_ 1 = _µ_ 2 _− µ_ 1, we obtain


This means that

100 _β_ 2 _≈_ (percentage change from year 2 to 3) _−_ (percentage change from year 1 to 2)

Continuing this way for _t_ = 4 _,_ 5 _, ..., n_ , we get


so that

100 _βt ≈_ (percentage change from year _t_ to ( _t_ + 1)) _−_ (percentage change from year ( _t −_ 1) to _t_ ) _._ For example, suppose


The interpretation then is that _µt_ started with the value _µ_ 1 = exp(7 _._ 3) _≈_ 1480 (if the population units are in thousands of persons, this means that the population at time 1 was 1.48 million). From year 1 to year 2, the population grew by 4%. From year 2 to year 3, the population grew by 4 _−_ 0 _._ 1 = 3 _._ 9%. From year 3 to year 4, the population grew by 3 _._ 9 _−_ 0 _._ 05 = 3 _._ 85%, and so on.

It is important to understand that the parameters _β_ 2 _, . . . , βn−_ 1 are on a different scale (units) compared to _β_ 0 and _β_ 1. _β_ 0 is in the scale of the data, 100 _β_ 1 represents percent change, while 100 _βj_ for _j ≥_ 2 represents the change in percent change.

We next study strategies for estimating the unknown parameters _β_ 0 _, β_ 1 _, . . . , βn−_ 1 (as well as _σ_ ) from the observed time series _y_ 1 _. . . . .yn_ .

2

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 (Unregularized) MLE →](03-2-unregularized-mle.md)
