---
title: 5 Alternative Representations
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEleven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEleven153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Alternative Representations

**Source:** [`LectureEleven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEleven153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Based on the alternative representations of Section 2, we can rewrite the optimization objectives (4) and (5) as


and


We denote the minimizer of (6) by _µ_ ˆ<sup>ridge</sup> _t_ ( _λ_ ) and the minimizer of (7) by _µ_ ˆ<sup>lasso</sup> _t_ ( _λ_ ). The relation between _µ_ ˆ<sup>ridge</sup> _t_ ( _λ_ ) and _β_<sup>ˆ</sup> ridge( _λ_ ) is given by


Similarly the relation between _µ_ ˆ<sup>ridge</sup> _t_ ( _λ_ ) and _β_<sup>ˆ</sup> ridge( _λ_ ) is given by


The estimator _µ_ ˆ<sup>ridge</sup> _t_ ( _λ_ ) is actually known by the name Hodrick-Prescott filter in the econometrics literature (see e.g., `https://en.wikipedia.org/wiki/Hodrick\OT1\textendashPrescott_ filter` ), and it is closely related to the cubic spline smoother (see e.g., `https://en. wikipedia.org/wiki/Smoothing_spline` ).

The estimator _µ_ ˆ<sup>lasso</sup> _t_ ( _λ_ ) is known by the name _ℓ_ 1 trend filter (see `https://stanford.edu/ ~`<sup>`boyd/papers/l1_trend_filter.html`).</sup>

Both the objective functions (6) and (7) ensure good fit to the data (because of the term � _nt_ =1<sup>(</sup><sup>_yt−µt_)2)whilealsoensuringthatneighboringslopes</sup><sup>_µt_+1</sup><sup>_−µt_and</sup><sup>_µt−µt−_1are</sup> close to each other (this is because of the terms _λ_<sup>�</sup><sup>_n_</sup> _t_ =2<sup>_−_1((</sup><sup>_µt_+1</sup><sup>_−µt_)</sup><sup>_−_(</sup><sup>_µt −µt−_1))2and</sup> _λ_<sup>�</sup><sup>_n_</sup> _t_ =2<sup>_−_1</sup><sup>_|_(</sup><sup>_µt_+1</sup><sup>_−µt_)</sup><sup>_−_(</sup><sup>_µt −µt−_1)</sup><sup>_|_).Closenessofneighboringslopes</sup><sup>_µt_+1</sup><sup>_−µt_and</sup><sup>_µt −µt−_1</sup> gives a smooth appearance to _{µt}_ . These can therefore be seen as methods for trying to fit a smooth trend function _µt_ to the observed time series _yt_ .

---

[← 4 Regularized Estimates](04-4-regularized-estimates.md) · [Up: contents](index.md) · [6 Ridge vs LASSO →](06-6-ridge-vs-lasso.md)
