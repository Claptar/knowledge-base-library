---
title: 2. A problem of limited means (20 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/final2020.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/final2020.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. A problem of limited means (20 points, 5 points / part).

**Source:** [`units/old-exams/final2020.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/final2020.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts for this problem:

- The uniform density Unif[ _a, b_ ] with parameters _a < b_ has density


Its mean and variance are ( _a_ + _b_ ) _/_ 2

and ( _b − a_ )<sup>2</sup> _/_ 12, respectively.

- The exponential distribution Exp( _λ_ ) with scale parameter _λ_ has density


The Gaussian density is printed in the preamble of Problem 2. Assume that we are in the Gaussian sequence model with


with the additional assumption that _|µi| ≤ θ_ for some _θ >_ 0. Assume unless specified otherwise that _θ_ is known.

- (a) Give the MLE of _µ_ 1 _, . . . , µd_ in this model.

- (b) Give an unbiased estimator for the mean squared error of the MLE, as a function of _X_ 1 _, . . . , Xd_ and _θ_ .

- (c) Now, suppose we introduce Bayesian assumptions: we assume addii.i.d.

- tionally that _µi ∼_ Unif[ _−θ,_ + _θ_ ], still with _θ_ known. Give an explicit expression for the Bayes estimator of _µ_ 1 _, . . . , µd_ using squared error loss.

- (d) Now, we relax the assumption that _θ_ is known and introduce a hierarchical Bayesian model with an exponential hyperprior for _θ_ :


Suggest a Gibbs sampler algorithm to sample from the posterior distribution of ( _θ, µ_ 1 _, . . . , µd_ ). Give the update rules explicitly.

4

---

[← 1. One Poisson, two Poissons (30 points, 5 points / part).](03-1-one-poisson-two-poissons-30-points-5-points-part.md) · [Up: contents](index.md) · [3. Gamma palooza (25 points, 5 points / part). →](05-3-gamma-palooza-25-points-5-points-part.md)
