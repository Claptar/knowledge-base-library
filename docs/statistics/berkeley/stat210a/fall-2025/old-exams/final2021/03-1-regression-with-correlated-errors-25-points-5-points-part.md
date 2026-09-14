---
title: 1. Regression with correlated errors (25 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2021.pdf
source_file: sources/berkeley-stat210a/fall-2025/old-exams/final2021.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. Regression with correlated errors (25 points, 5 points / part).

**Source:** [`old-exams/final2021.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2021.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts for this problem:


where _| · |_ is the determinant (note the exponent of 1 _/_ 2 is correct; it should not be _n/_ 2). The mean is _µ_ and the variance is Σ.

- If _Z ∼ Nn_ ( _µ,_ Σ), and _A ∈_ R<sup>_k×n_</sup> and _b ∈_ R<sup>_k_</sup> are fixed, then


Suppose that for _i_ = 1 _, . . . , n_ we observe fixed covariates _xi ∈_ R<sup>_d_</sup> and random response _Yi_ = _x_<sup>_′_</sup> _i_<sup>_β_+</sup><sup>_εi_, for coefficient vector</sup><sup>_β∈_R</sup><sup>_d_and</sup><sup>_εi∈_R.The errors are</sup> multivariate Gaussian with mean zero and positive definite covariance matrix Σ _∈_ R<sup>_n×n_</sup> . In terms of the full response vector _Y ∈_ R<sup>_n_</sup> and design matrix _X ∈_ R<sup>_n×d_</sup> with _i_ th row _x_<sup>_′_</sup> _i_<sup>, we have</sup>


Assume _n ≥ d ≥_ 1 and _X_ has full column rank. For parts (a) and (b), we will assume Σ is known and we want to estimate _β_ . For (c)-(e) we will assume Σ is unknown.

- (a) Show that _Y_ follows a full-rank exponential family model and identify its complete sufficient statistic.

- (b) Find the maximum likelihood estimator of _β_ and give its distribution.

- (c) Now, for the remainder of the problem, suppose that Σ is unknown so we have to estimate it. To facilitate this, we observe i.i.d. replicates _Y_<sup>(</sup><sup>_k_)</sup> for _k_ = 1 _, . . . , m_ , with distribution


Note that _X_ and _β_ are the same for _k_ = 1 _, . . . , m_ (they do not depend on _k_ ); only the errors change (and the responses change as a result). Define


Show that _Y_ and Σ<sup>�</sup> are independent of each other.

2

(d) Show that Σ<sup>�</sup> is an unbiased estimator of Σ.

- (e) Now assume _n_ = _d_ . Is Σ<sup>�</sup> UMVU? Why or why not?

3

---

[← Final Examination: QUESTION BOOKLET](02-final-examination-question-booklet.md) · [Up: contents](index.md) · [Problem 1 answers continued (1) →](04-problem-1-answers-continued-1.md)
