---
title: 1 Model from last class
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureEleven153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Model from last class

**Source:** [`LectureEleven153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last lecture, we studied the following model for a given time series _y_ 1 _, . . . , yn_ :

_yt_ = _β_ 0 + _β_ 1( _t −_ 1) + _β_ 2ReLU( _t −_ 2) + _· · ·_ + _βn−_ 1ReLU( _t −_ ( _n −_ 1)) + _ϵt_ (1)

i.i.d where, as always, _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). Here ReLU( _t − c_ ) = ( _t − c_ )+ equals 0 if _t ≤ c_ and equals ( _t − c_ ) if _t > c_ .

The unknown parameters in this model are _β_ 0 _, β_ 1 _, . . . , βn−_ 1 as well as _σ_ .

---

[Up: contents](index.md) · [2 Two alternative representations of (1) →](02-2-two-alternative-representations-of-1.md)
