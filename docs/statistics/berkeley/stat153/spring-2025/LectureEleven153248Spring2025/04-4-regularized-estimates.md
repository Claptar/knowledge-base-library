---
title: 4 Regularized Estimates
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureEleven153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Regularized Estimates

**Source:** [`LectureEleven153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We discussed two estimates of _β_ 0 _, . . . , βn−_ 1 based on the idea of regularization. The first is the ridge estimate _β_<sup>ˆridge</sup> ( _λ_ ) defined as the minimizer of:


The second is the LASSO estimate _β_<sup>ˆlasso</sup> ( _λ_ ) given by the minimizer of:


_λ_ denotes a parameter which can be tuned to change the behavior of _β_<sup>ˆridge</sup> ( _λ_ ) and _β_<sup>ˆlasso</sup> ( _λ_ ). When _λ_ = 0, both _β_<sup>ˆridge</sup> ( _λ_ ) and _β_<sup>ˆlasso</sup> ( _λ_ ) coincide with the unregularized least squares estimator. When _λ_ is very large, both _β_<sup>ˆridge</sup> ( _λ_ ) and _β_<sup>ˆlasso</sup> ( _λ_ ) coincide with the linear regression estimator (i.e., the first two components of _β_<sup>ˆridge</sup> ( _λ_ ) and _β_<sup>ˆlasso</sup> ( _λ_ ) coincide with linear regression while the last _n −_ 2 components are simply set to zero).

Based on the alternative representations of Section 2, we can rewrite the optimization objectives (9) and (10) as


and


2

We denote the minimizer of (5) by _µ_ ˆ<sup>ridge</sup> _t_ ( _λ_ ) and the minimizer of (6) by _µ_ ˆ<sup>lasso</sup> _t_ ( _λ_ ). The relation between _µ_ ˆ<sup>ridge</sup> _t_ ( _λ_ ) and _β_<sup>ˆridge</sup> ( _λ_ ) is given by


Similarly the relation between _µ_ ˆ<sup>ridge</sup> _t_ ( _λ_ ) and _β_<sup>ˆridge</sup> ( _λ_ ) is given by


The estimator _µ_ ˆ<sup>ridge</sup> _t_ ( _λ_ ) is actually known by the name Hodrick-Prescott filter in the econometrics literature (see e.g., `https://en.wikipedia.org/wiki/Hodrick\OT1\textendashPrescott_ filter` ), and it is closely related to the cubic spline smoother (see e.g., `https://en. wikipedia.org/wiki/Smoothing_spline` ).

The estimator _µ_ ˆ<sup>lasso</sup> _t_ ( _λ_ ) is known by the name _ℓ_ 1 trend filter (see `https://stanford.edu/ ~`<sup>`boyd/papers/l1_trend_filter.html`).</sup>

Both the objective functions (5) and (6) ensure good fit to the data (because of the term � _nt_ =1<sup>(</sup><sup>_yt−µt_)2)whilealsoensuringthatneighboringslopes</sup><sup>_µt_+1</sup><sup>_−µt_and</sup><sup>_µt−µt−_1are</sup> close to each other (this is because of the terms _λ_<sup>�</sup><sup>_n_</sup> _t_ =2<sup>_−_1((</sup><sup>_µt_+1</sup><sup>_−µt_)</sup><sup>_−_(</sup><sup>_µt −µt−_1))2and</sup> _λ_<sup>�</sup><sup>_n_</sup> _t_ =2<sup>_−_1</sup><sup>_|_(</sup><sup>_µt_+1</sup><sup>_−µt_)</sup><sup>_−_(</sup><sup>_µt −µt−_1)</sup><sup>_|_).Closenessofneighboringslopes</sup><sup>_µt_+1</sup><sup>_−µt_and</sup><sup>_µt −µt−_1</sup> gives a smooth appearance to _{µt}_ . These can therefore be seen as methods for trying to fit a smooth trend function _µt_ to the observed time series _yt_ .

---

[← 3 (Unregularized) MLE](03-3-unregularized-mle.md) · [Up: contents](index.md) · [5 Ridge vs LASSO →](05-5-ridge-vs-lasso.md)
