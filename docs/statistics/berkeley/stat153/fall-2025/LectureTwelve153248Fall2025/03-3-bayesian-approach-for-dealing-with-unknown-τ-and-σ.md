---
title: 3 Bayesian approach for dealing with unknown τ and σ
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwelve153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Bayesian approach for dealing with unknown τ and σ

**Source:** [`LectureTwelve153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One gets smooth fits to the data by working with the prior (8) for small _τ_ . This is not very surprising because the prior injects a strong amount of bias in favor of smooth fits. The real power of the Bayesian approach lies in the ability to automatically infer _τ_ from the data. This is done by simply placing a prior on _τ_ (along with the priors on _β_ and _σ_ ). We shall use the following prior:


and


where _Q_ is the same as in (9). Note that this prior implies that we are allowing essentially (because _C_ is large) all possible values of _τ_ and _σ_ . In particular, we are **not** _a priori_ ruling out large _τ_ just because we don’t like wiggly fits.

The prior joint density for _β, τ, σ_ is


We will also ignore the indicator because _C_ will be very large. It is important to note that _Q_ is not a constant matrix as it depends on _τ_ . The likelihood is (as usual in linear regression)


The posterior for _β, τ, σ_ is therefore


The term inside the exponent is a quadratic in _β_ and it is natural to complete the square which is done as follows:


4

where


We thus have


Plugging this in the posterior formula, we deduce


This expression may look complicated but the dependence on _β_ is simple through the quadratic which implies that


This proves (7) and (10). It is also straightforward to integrate _β_ from the joint posterior to obtain the posterior of _τ, σ_ :


In practice, inference can be carried out by first taking a grid of _σ_ and _τ_ values and computing the above posterior (on the logarithmic scale) at the grid points. We can obtain point estimates of _σ_ and _τ_ by taking the posterior maximizers. Alternatively, we can obtain posterior samples of _σ_ and _τ_ by sampling from the grid points with posterior weights. For each ( _σ, τ_ ) sample, one can sample _β_ using the multivariate normal distribution (10).

This grid approach can be avoided by using MCMC methods such as the Gibbs sampler. We shall not be discussing these.

---

[← 2 Bayesian Regularization](02-2-bayesian-regularization.md) · [Up: contents](index.md) · [4 Comments on Bayesian Regularization →](04-4-comments-on-bayesian-regularization.md)
