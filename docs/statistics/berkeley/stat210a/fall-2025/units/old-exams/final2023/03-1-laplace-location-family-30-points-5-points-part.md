---
title: 1. Laplace Location Family (30 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/final2023.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/final2023.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. Laplace Location Family (30 points, 5 points / part).

**Source:** [`units/old-exams/final2023.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/final2023.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts for this problem:

- The exponential distribution with scale parameter _θ >_ 0 is called Exp( _θ_ ) and has density


The mean is _θ_ and the variance is _θ_<sup>2</sup> .

- The Gamma distribution with scale parameter _θ >_ 0 and shape parameter _k >_ 0 is called Gamma( _k, θ_ ) and has density


where Γ( _k_ ) = �0 _∞_<sup>_tk−_1</sup><sup>_e−t dt_.The mean and variance are</sup><sup>_kθ_and</sup><sup>_kθ_2.</sup>

- A sum of _k_ independent Exp( _θ_ ) random variables is Gamma( _k, θ_ ).

- If _Z ∼_ Gamma( _k, θ_ ) then _aZ ∼_ Gamma( _k, aθ_ ), for any _a >_ 0.

Suppose that we observe an i.i.d. sample from the _Laplace scale family_ with parameter _θ >_ 0:


Note the density is supported on the entire real line. This is not the same as the Laplace location family that we have used as a running example in class.

- (a) Show that _|Xi| ∼_ Exp( _θ_ ) for _i_ = 1 _, . . . , n_ .

- (b) Find a minimal sufficient statistic for this model. Is it complete?

- (c) Find the maximum likelihood estimator for _θ_ and give its asymptotic distribution.

- (d) Show the estimator from the previous part is unbiased. Does it achieve the Cram´er-Rao Lower Bound?

- (e) Now, suppose that we are concerned the variance might be gradually shrinking. Specifically, we are concerned that the _i_ th random variable has parameter

2

_θi_ = _θ_ 0(1 _− δ_ )<sup>_i_</sup> . That is, we consider an alternative model with an additional parameter _δ ∈_ [0 _,_ 1), where


Assume (for this part **only** ) that the value of _θ_ 0 is known.

Suppose that we want to test our original model (which has _δ_ = 0) against the alternative that _δ >_ 0. Suggest a score test, giving an explicit expression for the score statistic and a cutoff based on its asymptotic distribution. You do **not** need to justify why the score statistic (calculated in the usual way and appropriately normalized) is asymptotically Gaussian in this non-i.i.d. model; you can just assume that it is.

- (f) (*) Now, drop the assumption that _θ_ 0 is known, so that now both _θ_ 0 and _δ_ are unknown. Assume we want to test the same hypothesis, _H_ 0 : _δ_ = 0 against _H_ 1 : _δ >_ 0, with _θ_ 0 as a nuisance parameter. How can we modify the test from the previous part so that it has finite-sample control of the Type I error rate? You do not need to give an explicit cutoff, but you should give a sufficient explanation of how you would find it without knowing the value of _θ_ 0.

3

---

[← Final Examination: QUESTION BOOKLET](02-final-examination-question-booklet.md) · [Up: contents](index.md) · [Problem 1 answers continued (1) →](04-problem-1-answers-continued-1.md)
