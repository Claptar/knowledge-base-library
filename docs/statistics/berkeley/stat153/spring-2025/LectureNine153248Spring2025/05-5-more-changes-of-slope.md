---
title: 5 More Changes of Slope
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureNine153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 More Changes of Slope

**Source:** [`LectureNine153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Suppose we want to introduce two break points for the regression line. This can be done via:

_yt_ = _β_ 0 + _β_ 1 _t_ + _β_ 2ReLU( _t − c_ 1) + _β_ 3ReLU( _t − c_ 2) + _ϵt_

i.i.d with _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). This model can also be written as


where _c_ = ( _c_ 1 _, c_ 2) and


The MLE of _c_ = ( _c_ 1 _, c_ 2) is given by the minimizer of _RSS_ ( _c_ ) over all _c_ = ( _c_ 1 _, c_ 2) with _c_ 1 _, c_ 2 _∈{_ 1 _, . . . , n}_ , and

_RSS_ ( _c_ ) = min _∥y − Xcβ∥_<sup>2</sup> _. β_

4

One can numerically minimize _RSS_ ( _c_ ) over all _c_ 1 _, c_ 2 _∈{_ 1 _, . . . , n}_ . The posterior of _c_ becomes:


For more break points, one can consider:


Conceptually estimation and inference here proceed just as before with _Xc_ changed appropriately. But the method can become computationally expensive if _k ≥_ 4.

5

---

[← 4 Posterior Sampling for Uncertainty Quantification](04-4-posterior-sampling-for-uncertainty-quantification.md) · [Up: contents](index.md)
