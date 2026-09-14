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

We have an unbiased estimator in 1 _{X_ 1 _> Y_ 1 _}_ , so all we need to do is RaoBlackwellize it conditional on _S_ ( _X_ ) and _S_ ( _Y_ ). Conditional on these statistics, _X_ 1 and _Y_ 1 are independently uniform draws from _S_ ( _X_ ) and _S_ ( _Y_ ), so the UMVU estimator is


**Common errors:** Note that _n_<sup><u>1</u></sup> � _i_<sup>1</sup><sup>_{Xi>Yi}_wouldnotbecorrect;itis</sup> unbiased but cannot be calculated from the complete sufficient statistic. And _n_ <u>1</u> � _i_<sup>1</sup><sup>_{X_(</sup><sup>_i_)</sup><sup>_> Y_(</sup><sup>_i_)</sup><sup>_}_is not even unbiased. However, the estimator</sup> _n_<sup><u>12</u></sup> � _ni,j_ =1<sup>1</sup><sup>_{X_(</sup><sup>_i_)</sup><sup>_>_</sup> _Y_ ( _j_ ) _}_ is correct; students who gave this answer or another equivalent answer got full credit as long as each of the _n_<sup>2</sup> pairs of _X_ and _Y_ values are represented once.

- (b) Define _µ_ = E _P X_ , _ν_ = E _QY_ , _σ_<sup>2</sup> = Var _P_ ( _X_ ), and _τ_<sup>2</sup> = Var _Q_ ( _Y_ ). Show that _T_ ( _X, Y_ ) = ( _X/Y_ )<sup>2</sup> is a consistent estimator for _θ_ = ( _µ/ν_ )<sup>2</sup> as _n →∞_ , assuming _ν >_ 0 and _σ_<sup>2</sup> _, τ_<sup>2</sup> _∈_ (0 _, ∞_ ).

9

---

[← 3. Nonparametric two-sample problem (20 points, 5 points / part).](15-3-nonparametric-two-sample-problem-20-points-5-points-part.md) · [Up: contents](index.md) · [Solution →](17-solution.md)
