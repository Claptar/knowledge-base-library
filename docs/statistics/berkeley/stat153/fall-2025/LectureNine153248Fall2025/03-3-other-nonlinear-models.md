---
title: 3 Other Nonlinear Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNine153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureNine153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Other Nonlinear Models

**Source:** [`LectureNine153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNine153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Our methodology for inference in these sinusoid models also extends to other similar nonlinear regression models. For example, consider the following model which is applicable when we want to introduce two break points for the regression line:


i.i.d with _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). This model can also be written as


where _c_ = ( _c_ 1 _, c_ 2) and


6

We estimate _c_ = ( _c_ 1 _, c_ 2) by minimizing _RSS_ ( _c_ ) over all _c_ = ( _c_ 1 _, c_ 2) with _c_ 1 _, c_ 2 _∈_ [1 _, n_ ], and


One can numerically minimize _RSS_ ( _c_ ) over all _c_ 1 _, c_ 2 _∈_ [1 _, n_ ]. A natural grid one can use here is _{_ 1 _, . . . , n}_ .

The posterior of _c_ becomes:


For more break points, one can consider:


Conceptually estimation and inference here proceed just as before with _Xc_ changed appropriately. But the method can become computationally expensive if _k ≥_ 4.

7

---

[← 2 Sinusoidal Models with more frequencies](02-2-sinusoidal-models-with-more-frequencies.md) · [Up: contents](index.md)
