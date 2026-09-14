---
title: Problem 2 answers continued (3)
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2018.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/final2018.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 2 answers continued (3)

**Source:** [`old-exams/final2018.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2018.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

10

**3. Inverse gamma prior (20 points, 4 points / part).** Some useful facts for this problem:

   - Recall that the Gaussian density function for _Z ∼ N_ ( _µ, σ_<sup>2</sup> ) is


- A _χ_<sup>2</sup> _d_<sup>randomvariablehasmean</sup><sup>_d_andvariance2</sup><sup>_d_.</sup>

- If _Y_ is a Gamma( _α, β_ ) random variable (in its “rate parameterization”) then it has density


on (0 _, ∞_ ). _Y_ has mean _α/β_ and variance _α/β_<sup>2</sup> . This distribution is defined for _α, β >_ 0.

- The inverse-gamma distribution (denoted _IG_ ( _α, β_ )) is the distribution of _W_ = 1 _/Y_ where _Y ∼_ Gamma( _α, β_ ). Then _W ∈_ (0 _, ∞_ ) has the density


Note that _β_ is a scale parameter for _W_ . _W_ has mean _α−β_ 1<sup>provided</sup> _α >_ 1, and variance ( _α−_ 1) _<u>β−</u>_<sup>2</sup> (1 _α−_ 2)<sup>provided</sup><sup>_α>_2.Thisdistributionis</sup> likewise defined for _α, β >_ 0.

- Define the _squared relative error_ loss function


and define the corresponding risk function _R_ rel( _δ_ ( _·_ ) _, θ_ ) = E _θ_ [ _L_ rel( _δ_ ( _X_ ) _, θ_ )]. Consider the Bayesian model with


Note that the variance is _θ_ , not _θ_<sup>2</sup> , and assume _n ≥_ 2.

- (a) Find the posterior distribution of _θ_ given _X_ = ( _X_ 1 _, . . . , Xn_ ) and the Bayes estimator for _θ_ under the usual squared error loss.

11

- (b) Give the mean squared error of the Bayes estimator from part (a), as a function of _θ_ (you don’t need to try too hard to simplify it).

- (c) Find the Bayes estimator for _θ_ under the squared relative error loss _L_ rel.

- (d) (*) For the estimator in part (c), find the risk function _R_ rel( _δ_ ( _·_ ) _, θ_ ) as a function of _θ_ and show that the Bayes risk is <u>2</u> _n_ +2( _α_ +1)<sup>.</sup>

- (e) For the relative squared error risk, find a linear estimator of the form _δ_ ( _X_ ) = _a_<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_X_</sup> _i_<sup>2thatisminimax,andproveitisminimax.</sup>

12

---

[← Problem 2 answers continued (2)](07-problem-2-answers-continued-2.md) · [Up: contents](index.md) · [Problem 3 answers continued (1) →](09-problem-3-answers-continued-1.md)
