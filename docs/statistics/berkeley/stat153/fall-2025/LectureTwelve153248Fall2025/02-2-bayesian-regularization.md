---
title: 2 Bayesian Regularization
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwelve153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Bayesian Regularization

**Source:** [`LectureTwelve153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We now treat regularization in high-dimensional regression from the Bayesian point of view. Before discussing regularization, let us first recap the basics of Bayesian regression in the model:


The basic prior that we used previously is


2

for a large positive constant _C_ . For this prior, we showed (see e.g., problem 5 in Homework 1) that


when _C →∞_ . This fact is not quite true if _C_ is not very large.

A slightly different prior which allows exact formulae even for finite _C_ is the Gaussian prior:


Under this prior, it turns out that


where _I_ is the identity matrix. It is instructive to compare (5) and (7). Unlike (5) which is only true for large _C_ , the fact (7) is true for every _C >_ 0. It is also clear that when _C →∞_ , then (7) is the same as (5). Observe that when _C_ is large, there is not much difference qualitatively between unif( _−C, C_ ) and _N_ (0 _, C_ ) (they are both uninformative priors).

We shall prove a more general form of (7) later in this lecture.

Now let us specialize to the case of the high dimensional regression (2). If we use the prior (6) with _C →∞_ , then the posterior mean becomes the unregularized least squares (or unregularized MLE) estimator ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_T_</sup> _y_ . The fitted values will then perfectly interpolate the data leading to overfitting. From the Bayesian perspective, this is happening because the prior (6) with very large _C_ is not useful for this dataset. The prior needs to be changed for a more meaningful analysis. In the frequentist analysis, the main motivation for the ridge regularization (3) is the need to obtain smaller estimates for _β_ 2 _, . . . , βn−_ 1 which will lead to a smoother fit to the data. This same effect can be obtained by the following modification of the prior (6):


for a small parameter _τ_ (in the above, we also assume that _β_ 0 _, . . . , βn−_ 1 are all independent). The prior (8) can be written as


where _Q_ is the diagonal matrix with diagonal entries _C, C, τ_<sup>2</sup> _, . . . , τ_<sup>2</sup> . Under the prior (9), the posterior of _β_ is given by


We will prove this result later in this lecture. The posterior mean therefore is given by


This expression is closely related to the ridge estimator (4). Note that _Q_<sup>_−_1</sup> is diagonal with diagonal entries 1 _/C,_ 1 _/C,_ 1 _/τ_<sup>2</sup> _, . . . ,_ 1 _/τ_<sup>2</sup> . When _C_ is very large, the first two diagonal entries of _Q_<sup>_−_1</sup> are very close to zero so that


3

Thus the posterior mean (11) is therefore


which matches (4) if


Ridge regularization therefore can be understood as Bayesian regression with the prior (8). The precise equivalence is obtained if _λ_ is related to _τ_<sup>2</sup> via _λ_ = _σ_<sup>2</sup> _/τ_<sup>2</sup> .

---

[← 1 Recap: Ridge Regression](01-1-recap-ridge-regression.md) · [Up: contents](index.md) · [3 Bayesian approach for dealing with unknown τ and σ →](03-3-bayesian-approach-for-dealing-with-unknown-τ-and-σ.md)
