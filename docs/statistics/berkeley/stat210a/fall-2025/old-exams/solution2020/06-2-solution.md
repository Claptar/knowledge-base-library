---
title: 2. Solution
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/solution2020.pdf
source_file: sources/berkeley-stat210a/fall-2025/old-exams/solution2020.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. Solution

**Source:** [`old-exams/solution2020.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/solution2020.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

(a) The likelihood is


so the likelihood is maximized by taking _µ_ ˆ _i_ as close to _Xi_ as possible, subject to the constraint that _|µ_ ˆ _i| ≤ θ_ . As a result,


- (b) This is a SURE problem. Defining


we have


Then Stein’s unbiased risk estimator is


- (c) Under this model, the pairs ( _µi, Xi_ ) are i.i.d. so the posterior distribution only depends on _Xi_ . The prior for _µi_ is 21 _θ_<sup>1</sup><sup>_{|µi|≤θ}_andthe</sup> likelihood is _φ_ ( _Xi − µi_ ) where _φ_ ( _z_ ) = (2 _π_ )<sup>_−_1</sup><sup>_/_2</sup> _e_<sup>_−z_2</sup><sup>_/_2</sup> , so the posterior density is


where the 1 _/_ 2 _θ_ term cancels on the top and the bottom. This is the distribution of a _N_ ( _Xi,_ 1) random variable truncated to the interval [ _−θ, θ_ ], which we can write as _N_ ( _Xi,_ 1)1 _{|µi| ≤ θ}_ .

9

The Bayes estimator is the posterior expectation,


- (d) We have just shown that, conditional on ( _θ, X_ ), the coordinates of _µ_ are truncated normal random variables:


They are conditionally independent because the pairs ( _µi, Xi_ ) are i.i.d. given _θ_ (note they are not marginally independent if _θ_ is random). The conditional density of _θ_ given ( _µ, X_ ) is proportional to


so normalizing it gives


We could sort of call this a truncated Gamma( _−d_ + 1 _, λ_ ) distribution, but the “shape parameter” is negative (note the density wouldn’t be normalizable if the lower bound of the support were at 0). Anyway the density is given explicitly above, so we can sample from it by plugging a uniform random variable into its inverse CDF.

So the Gibbs sampler iterates between:


I kind of wish I’d told you to use the improper “flat” prior on _θ_ , with _p_ ( _θ_ ) _≡_ 1. Then the Gibbs update for _θ_ would have been exactly a Pareto distribution, which would have been kind of cool. Oh, well!

10

---

[← 2. A problem of limited means (20 points, 5 points / part).](05-2-a-problem-of-limited-means-20-points-5-points-part.md) · [Up: contents](index.md) · [3. Gamma palooza (25 points, 5 points / part). →](07-3-gamma-palooza-25-points-5-points-part.md)
