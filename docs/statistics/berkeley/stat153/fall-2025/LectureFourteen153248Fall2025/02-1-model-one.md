---
title: 1 Model One
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFourteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFourteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Model One

**Source:** [`LectureFourteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFourteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This is the model


where ind stands for “independently distributed as”. Note that the right hand side depends on _t_ so the distribution of _yt_ changes with _t_ and we cannot therefore use “i.i.d”.

The parameters in this model are _µ_ 1 _, . . . , µn_ and _σ_<sup>2</sup> . Clearly this is a high-dimensional because the number of parameters is large.

If we attempt to estimate the parameters by maximizing the likelihood without any regularization, we get _µt_ = _yt_ and _σ_<sup>2</sup> = 0, leading to full interpolation (overfitting) to the data. Regularization is therefore necessary to obtain something useful. If we want to obtain “smooth” trend estimates, we can employ regularization terms which force neighboring values or neighboring slopes of _µt_ to be close. If we focus on slopes (which leads to more smoothness compared to just imposing closeness of values), we obtain the estimators _µ_ ˆ<sup>ridge</sup> _t_ ( _λ_ ) and _µ_ ˆ<sup>lasso</sup> _t_ ( _λ_ ) which minimize:

and


respectively. We have already studied these estimators last week where we observed, among other things, that they can be alternatively represented as _µ_ ˆ<sup>ridge</sup> _t_ ( _λ_ ) = _Xβ_<sup>ˆridge</sup> ( _λ_ ) and

1

_µ_ ˆ<sup>lasso</sup> _t_ ( _λ_ ) = _Xβ_<sup>ˆlasso</sup> ( _λ_ ) where


and _β_<sup>ˆridge</sup> ( _λ_ ) and _β_<sup>ˆlasso</sup> ( _λ_ ) minimize

and


respectively.

This model is an example of a “Mean Model” where the focus is on estimating the mean parameters _µt_ . In contrast, the next two models will be examples of “Variance Models”.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Model Two →](03-2-model-two.md)
