---
title: 1. Poisson minimax estimation (24 points, 4 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2019.pdf
source_file: sources/berkeley-stat210a/fall-2025/old-exams/final2019.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. Poisson minimax estimation (24 points, 4 points / part).

**Source:** [`old-exams/final2019.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2019.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts for this problem:

- For _θ >_ 0, the Poisson density for _X ∼_ Pois( _θ_ ) is<sup>_<u>θx</u>_</sup> _x_<sup>_<u>e</u>_</sup> !<sup>_−θ_</sup> on _x_ = 0 _,_ 1 _, . . ._ . The mean and variance are both _θ_ .

- The Gamma density for _X ∼_ Gamma( _k, β_ ), where _β >_ 0 is the _rate_ parameter, is


where Γ( _k_ ) = �0 _∞_<sup>_zk−_1</sup><sup>_e−z dz_.Themeanandvarianceare</sup><sup>_k/β_and</sup> _k/β_<sup>2</sup> , respectively.

- If _X ∼_ Gamma( _k, β_ ) (in the rate parameterization) with _k >_ 1, then E[ _X_<sup>_−_1</sup> ] = _β/_ ( _k −_ 1).

Consider estimating _θ_ given a single Poisson observation _X ∼_ Pois( _θ_ ) using the loss function


Throughout this problem, unless otherwise specified, the risk of a given estimator is always calculated using this loss.

- (a) Find the MLE and calculate its risk function.

- (b) Show that _θ ∼_ Gamma( _k, β_ ) is a conjugate prior for this problem and give the posterior distribution.

- (c) Find the Bayes estimator for the prior from part (b) and the loss _L_ defined above.

- (d) (*) Show that the Bayes risk of the Bayes estimator from part (c) is 1 _/_ (1 + _β_ )

- (e) Show that the MLE is minimax relative to the loss _L_ .

- (f) Show that the minimax risk for the usual squared error loss — i.e., _L_ SE( _d, θ_ ) = ( _d − θ_ )<sup>2</sup> — is infinite (this motivates changing the loss function to our _L_ , which “adjusts” for the hardness of the problem).

2

---

[← Final Examination: QUESTION BOOKLET](02-final-examination-question-booklet.md) · [Up: contents](index.md) · [Problem 1 answers continued (1) →](04-problem-1-answers-continued-1.md)
