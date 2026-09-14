---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2021.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/solution2021.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`units/old-exams/solution2021.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2021.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The log-likelihood for a single observation is


which is a uniformly bounded and continuous function of _θ ∈_ [0 _, b_ ]. As a result, by our uniform LLN, _n_<sup><u>1</u></sup><sup>_ℓn_(</sup><sup>_θ_;</sup><sup>_X_) converges uniformly in probability to</sup> its expectation, which is _−D_ KL( _θ ∥ θ_ 0). Further, since the model is identifiable, the last function has a unique maximum at _θ_ = _θ_ 0, so by our proposition from class, the maximizer of _ℓn_ ( _θ_ ; _X_ ) converges to _θ_ 0 in probability.

- (b) Give the asymptotic distribution of the maximum likelihood estimator as _n → ∞_ , for _θ_ 0 _∈_ (0 _, b_ ). Give an explicit expression for the asymptotic variance in terms of a definite integral (you don’t need to check any regularity conditions for this part).

---

[← 2. Contamination model (25 points, 5 points / part).](08-2-contamination-model-25-points-5-points-part.md) · [Up: contents](index.md) · [Solution →](10-solution.md)
