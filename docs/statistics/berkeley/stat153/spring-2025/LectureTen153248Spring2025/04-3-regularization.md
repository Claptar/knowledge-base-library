---
title: 3 Regularization
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Regularization

**Source:** [`LectureTen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

To produce useful estimates in cases where the MLE overfits, one employs the idea of regularization. We will discuss two ways of doing this: Ridge regularization and LASSO regularization.

The Ridge estimate of _β_ will be denoted by _β_<sup>ˆ</sup> ridge( _λ_ ) and is given by the minimizer of:


In other words, _β_<sup>ˆ</sup> ridge( _λ_ ) minimizes a new criterion function that is obtained by adding the penalty term _λ_ (<sup>�</sup><sup>_n_</sup> _j_ =2<sup>_−_1</sup><sup>_β_</sup> _j_<sup>2)totheleastsquarescriterion.</sup>

Here _λ_ denotes a tuning parameter. Different choices of _λ_ give rise to different ridge estimators _β_<sup>ˆ</sup> ridge( _λ_ ). When _λ_ = 0, the penalty term is not used in (5) so that _β_<sup>ˆ</sup> ridge( _λ_ ) coincides with the unregularized least squares estimator. If _λ_ is set to be very large, then the penalty term dominates the objective function (5) and then the first two components of _β_ ˆridge( _λ_ ) coincide with linear regression while the last _n −_ 2 components are simply set to zero.

The LASSO estimate of _β_ will be denoted by _β_<sup>ˆ</sup> lasso( _λ_ ) and is given by the minimizer of:


3

In other words, _β_<sup>ˆ</sup> lasso( _λ_ ) minimizes a new criterion function that is obtained by adding the penalty term _λ_ (<sup>�</sup><sup>_n_</sup> _j_ =2<sup>_−_1</sup><sup>_|βj|_)totheleastsquarescriterion.Asinthecaseoftheridge</sup> estimator, when _λ_ = 0, the penalty term is not used in (6) so that _β_<sup>ˆ</sup> ridge( _λ_ ) coincides with the unregularized least squares estimator. If _λ_ is set to be very large, then the penalty term dominates the objective function (6) and then the first two components of _β_<sup>ˆ</sup> ridge( _λ_ ) coincide with linear regression while the last _n −_ 2 components are simply set to zero.

The only difference between the ridge and lasso is in the penalty term:<sup>�</sup> _j_<sup>_β_</sup> _j_<sup>2vs�</sup> _j_<sup>_|βj|_.</sup> We will discuss computation and the differences between these estimators in the next lecture.

Note that, in usual implementations of ridge and lasso, the penalty is usually placed on all the coefficients (with the possible exception of the intercept). Here we are only placing it on _β_ 2 _, . . . , βn−_ 1. As we saw in the interpretation section, _β_ 1 is quite different (both in having different units and also being somewhat bigger in size) compared to _β_ 2 _, . . . , βn−_ 1. It would not make sense in this example to include _β_ 1 in the penalty term.

4

---

[← 2 (Unregularized) MLE](03-2-unregularized-mle.md) · [Up: contents](index.md)
