---
title: 4 Regularized Estimates
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEleven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEleven153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Regularized Estimates

**Source:** [`LectureEleven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEleven153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

To produce useful estimates in cases where the MLE overfits, one employs the idea of regularization. We will discuss two ways of doing this: Ridge regularization and LASSO regularization.

The Ridge estimate of _β_ will be denoted by _β_<sup>ˆ</sup> ridge( _λ_ ) and is given by the minimizer of:


In other words, _β_<sup>ˆ</sup> ridge( _λ_ ) minimizes a new criterion function that is obtained by adding the penalty term _λ_ (<sup>�</sup><sup>_n_</sup> _j_ =2<sup>_−_1</sup><sup>_β_</sup> _j_<sup>2)totheleastsquarescriterion.</sup>

Here _λ_ denotes a tuning parameter. Different choices of _λ_ give rise to different ridge estimators _β_<sup>ˆ</sup> ridge( _λ_ ). When _λ_ = 0, the penalty term is not used in (4) so that _β_<sup>ˆ</sup> ridge( _λ_ ) coincides with the unregularized least squares estimator. If _λ_ is set to be very large, then the penalty term dominates the objective function (4) and then the first two components of _β_ ˆridge( _λ_ ) coincide with linear regression while the last _n −_ 2 components are simply set to zero.

The LASSO estimate of _β_ will be denoted by _β_<sup>ˆ</sup> lasso( _λ_ ) and is given by the minimizer of:


In other words, _β_<sup>ˆ</sup> lasso( _λ_ ) minimizes a new criterion function that is obtained by adding the penalty term _λ_ (<sup>�</sup><sup>_n_</sup> _j_ =2<sup>_−_1</sup><sup>_|βj|_)totheleastsquarescriterion.Asinthecaseoftheridge</sup> estimator, when _λ_ = 0, the penalty term is not used in (5) so that _β_<sup>ˆ</sup> ridge( _λ_ ) coincides with the unregularized least squares estimator. If _λ_ is set to be very large, then the penalty term dominates the objective function (5) and then the first two components of _β_<sup>ˆ</sup> ridge( _λ_ ) coincide with linear regression while the last _n −_ 2 components are simply set to zero.

2

The only difference between the ridge and lasso is in the penalty term:<sup>�</sup> _j_<sup>_β_</sup> _j_<sup>2vs�</sup> _j_<sup>_|βj|_.</sup> We will discuss computation and the differences between these estimators in the next lecture.

Note that, in usual implementations of ridge and lasso, the penalty is usually placed on all the coefficients (with the possible exception of the intercept). Here we are only placing it on _β_ 2 _, . . . , βn−_ 1. Because of this choice, these regularized estimates revert to linear regression when the tuning parameter is large.

---

[← 3 (Unregularized) Least Squares](03-3-unregularized-least-squares.md) · [Up: contents](index.md) · [5 Alternative Representations →](05-5-alternative-representations.md)
