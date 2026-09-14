---
title: Problem 2 solutions
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2018.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/solution2018.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 2 solutions

**Source:** [`old-exams/solution2018.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2018.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Let _Uj_ =<sup>�</sup> _i_<sup>_N_</sup> _j_<sup>(</sup><sup>_i_).Thefullmodeldensityis</sup>


where _ηj_ = log _λj_ and _Uj_ =<sup>�</sup> _i_<sup>_N_</sup> _j_<sup>(</sup><sup>_i_).Thisisafull-rankexponen-</sup> tial family with _ηj_ ranging over all of R<sup>_s_</sup> . The _s_ sufficient statistics _U_ 1 _, . . . , Us_ are therefore complete sufficient. As _Uj/m_ is unbiased for _λj_ , it is UMVU.

2. Let _T_ =<sup>�</sup> _i_ �1 _≤j<k≤s_<sup>_e−d_(</sup><sup>_j,k_)</sup><sup>_N_</sup> _j_<sup>(</sup><sup>_i_)</sup><sup>_N_</sup> _k_<sup>(</sup><sup>_i_).Thefullmodeldensityisnow</sup> proportional to


which has _s_ + 1 sufficient statistics _U_ 1 _, . . . , Us, T_ with corresponding natural parameters _η_ 1 _, . . . , ηs, β_ .

3. As usual, the UMPU test will reject for large values of _T_ conditional on _U_ . In practice, we can find the critical value by Monte Carlo, by resampling the entire data set under the null model, conditional on _Uj_ , and recomputing the test statistic _T_ each time we do. Due to the fact about conditional multinomials, and the fact that species are independent of one another under the null, this means that for each species (each column of the table) we should resample ( _N_ 1<sup>(</sup><sup>_j_)</sup><sup>_, . . . , N_</sup> _m_<sup>(</sup><sup>_j_))ind.</sup> _∼_ Multinomial( _Uj,_ (1 _, . . . ,_ 1) _/m_ ), for _j_ = 1 _, . . . , m_ .

One way to look at this is that we take every individual that was counted in the data set, and we independently send each of them to a uniformly random site (while preserving which species they are). Note this reassignment does not change the total number of individuals of each species in the data set.

4. In this case the null model is essentially that ( _Nj_<sup>(1)</sup> _, . . . , Nj_<sup>(</sup><sup>_s_)</sup> )<sup>i.i.d.</sup> _∼ Fj_ , independently for each _j_ with _Fj_ completely unknown. The complete sufficient statistic for the (null) model is therefore the empirical distribution of counts ( _Nj_<sup>(1)</sup> _, . . . , Nj_<sup>(</sup><sup>_s_)</sup> ) for each of the _s_ species (i.e., _s_

7

empirical distributions each recording _m_ observations). Resampling the data table conditional on those empirical distributions amounts to randomly shuffling the entries of each column of the table and then recompouting the test statistic. This is a permutation test where we permute each column of the table separately.

8

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

9

- (b) Give the mean squared error of the Bayes estimator from part (a), as a function of _θ_ (you don’t need to try too hard to simplify it).

- (c) Find the Bayes estimator for _θ_ under the squared relative error loss _L_ rel.

- (d) (*) For the estimator in part (c), find the risk function _R_ rel( _δ_ ( _·_ ) _, θ_ ) as a function of _θ_ and show that the Bayes risk is <u>2</u> _n_ +2( _α_ +1)<sup>.</sup>

- (e) For the relative squared error risk, find a linear estimator of the form _δ_ ( _X_ ) = _a_<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_X_</sup> _i_<sup>2thatisminimax,andproveitisminimax.</sup>

10

---

[← Species](04-species.md) · [Up: contents](index.md) · [Problem 3 solutions →](06-problem-3-solutions.md)
