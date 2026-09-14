---
title: 2 Two alternative representations of (1)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEleven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEleven153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Two alternative representations of (1)

**Source:** [`LectureEleven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEleven153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

There are two alternative ways of writing the model (1). The first one is


and

_µt_ = _β_ 0 + _β_ 1( _t −_ 1) + _β_ 2ReLU( _t −_ 2) + _· · ·_ + _βn−_ 1ReLU( _t −_ ( _n −_ 1)) _._ (3) The _β_ ’s can be written in terms of _µt_ as follows: _β_ 0 = _µ_ 1, _β_ 1 = _µ_ 2 _− µ_ 1, and


In (2), _µt_ can be interpreted as the underlying trend present in the data.

The second way of writing (1) is in regression form:

_y_ = _Xβ_ + _ϵ_

where


1

---

[← 1 High-dimensional Linear Model from last class](01-1-high-dimensional-linear-model-from-last-class.md) · [Up: contents](index.md) · [3 (Unregularized) Least Squares →](03-3-unregularized-least-squares.md)
