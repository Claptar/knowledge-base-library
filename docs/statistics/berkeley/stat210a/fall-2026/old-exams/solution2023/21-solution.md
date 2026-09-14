---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2023.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/solution2023.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`old-exams/solution2023.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2023.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The prior is _λ_ ( _θ_ ) _∝θ θ_<sup>_α_</sup> <u>1</u><sup>+11</sup><sup>_{θ≥θ_0</sup><sup>_}_, and the likelihood is</sup><sup>_pθ_(</sup><sup>_x_)=</sup><sup><u>1</u></sup> _θ_<sup>1</sup><sup>_{x≤_</sup> _θ}_ , so the posterior distribution is


As a result the posterior mean (which is the Bayes estimator for squared error loss) is _θ_<sup>ˆ</sup> =<sup><u>1+</u></sup> _α_<sup>_<u>α</u>_max(</sup><sup>_θ_0</sup><sup>_, X_) = (1 + 1</sup><sup>_/α_) max(</sup><sup>_θ_0</sup><sup>_, X_).</sup>

**Common mistake:** The posterior is not Pareto( _θ_ 0 _, α_ +1) (if it were, it wouldn’t depend on the data). A good number of students forgot to mind the indicators.

12

I think people made that mistake because we have often been lackadaisical in class and on homework about keeping explicit track of the support of distributions. It is usually fine not to worry about the support, since there is usually a base measure for the family that determines the support for all densities in the problem, and so it goes without saying that all densities we work with for that problem have the same support. But for both the uniform and Pareto families in this problem, the support depends on the parameter so we have to keep track of it if we want to get the calculations right.

- (b) Next consider the prior _λ_ ( _θ_ ) = 2 _θ ·_ 1 _{_ 0 _≤ θ ≤_ 1 _}_ . Find the Bayes estimator and Bayes risk.

---

[← 4. Bayes estimation for Uniform Scale family (20 points, 5 points / part).](20-4-bayes-estimation-for-uniform-scale-family-20-points-5-poin.md) · [Up: contents](index.md) · [Solution →](22-solution.md)
