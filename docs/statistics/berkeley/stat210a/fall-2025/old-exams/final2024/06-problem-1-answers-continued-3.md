---
title: Problem 1 answers continued (3)
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2024.pdf
source_file: sources/berkeley-stat210a/fall-2025/old-exams/final2024.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 1 answers continued (3)

**Source:** [`old-exams/final2024.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2024.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

5

**2. Inverse gamma prior (20 points, 5 points / part).** Some useful facts for this problem:

- A _χ_<sup>2</sup> _d_<sup>random variable has mean</sup><sup>_d_and variance 2</sup><sup>_d_.</sup>

- If _Y_ is a Gamma( _α, β_ ) random variable (in its “rate parameterization”) then it has density


on (0 _, ∞_ ). _Y_ has mean _α/β_ and variance _α/β_<sup>2</sup> . This distribution is defined for _α, β >_ 0.

- The inverse-gamma distribution (denoted _IG_ ( _α, β_ )) is the distribution of _W_ = 1 _/Y_ where _Y ∼_ Gamma( _α, β_ ). Then _W ∈_ (0 _, ∞_ ) has the density


Note that _β_ is a scale parameter for _W_ . _W_ has mean _α−β_ 1<sup>provided</sup><sup>_α>_</sup> _<u>β−</u>_ 1 1, and variance ( _α−_ 1)<sup>2</sup> ( _α−_ 2)<sup>provided</sup><sup>_α>_2.Thisdistributionislikewise</sup> defined for _α, β >_ 0.

- Define the _squared relative error_ loss function


and define the corresponding risk function _R_ rel( _δ_ ( _·_ ) _, θ_ ) = E _θ_ [ _L_ rel( _δ_ ( _X_ ) _, θ_ )]. Consider the Bayesian model with


Note that the variance is _θ_ , not _θ_<sup>2</sup> , and assume _n ≥_ 2.

- (a) Find the posterior distribution of _θ_ given _X_ = ( _X_ 1 _, . . . , Xn_ ) and the Bayes estimator for _θ_ under the standard (not relative) squared error loss.

- (b) Find the Bayes estimator for _θ_ under the squared relative error loss _L_ rel.

- (c) (*) For the estimator in part (b), find the risk function _R_ rel( _δ_ ( _·_ ) _, θ_ ) as a function of _θ_ and show that the Bayes risk is <u>2</u> _n_ +2( _α_ +1)<sup>.</sup>

- (d) For the relative squared error risk, find a linear estimator of the form _δ_ ( _X_ ) = _a_<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_X_</sup> _i_<sup>2that is minimax, and prove it is minimax.</sup>

6

---

[← Problem 1 answers continued (2)](05-problem-1-answers-continued-2.md) · [Up: contents](index.md) · [Problem 2 answers continued (1) →](07-problem-2-answers-continued-1.md)
