---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2024.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/solution2024.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`old-exams/solution2024.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2024.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Now in addition to the RSS from the model space Θ we have the residual sum of squares from the null model, which is RSS0 =<sup>�6</sup> _i_ =1<sup>(</sup><sup>_Xi−_</sup> _X_ )<sup>2</sup> , where _X_ = 6<sup><u>1</u></sup> � _i_<sup>_Xi_.Thenullmodelhas</sup><sup>_d_0=1degreeoffreedomandthefull</sup> model has _d_ = 3 degrees of freedom. Hence _d − d_ 0 = 2 and _n − d_ = 3, and the _F_ statistic is


4

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

**Solution:**

5

The prior times the likelihood, ignoring factors that do not depend on _θ_ , is


The posterior expectation, then, is


- (b) Find the Bayes estimator for _θ_ under the squared relative error loss _L_ rel.

---

[← Solution](06-solution.md) · [Up: contents](index.md) · [Solution →](08-solution.md)
