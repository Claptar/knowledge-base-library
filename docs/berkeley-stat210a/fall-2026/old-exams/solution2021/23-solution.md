---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2021.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/solution2021.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`old-exams/solution2021.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2021.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The minimal sufficient statistic is


To see why, note that by standard arguments _Tk_ ( _X_ ) = �� _i≤k_<sup>_Xi,_�</sup> _i>k_<sup>_Xi_</sup> � is complete sufficient (and therefore minimal sufficient) for the submodels with _k_ fixed. That is, we must observe at least ( _T_ 4 _, T_ 5 _, T_ 6) to be able to evaluate all likelihood ratios between distributions in each submodel, and _T_ ( _X_ ) is equivalent to ( _T_ 4 _, T_ 5 _, T_ 6), so if _T_ ( _X_ ) is sufficient then it is also minimal.

Furthermore, we can also show by standard arguments that _T_ ( _X_ ) is complete sufficient for the exponential family where _θ_ 1 = _· · ·_ = _θ_ 4 and _θ_ 7 = _· · ·_ = _θ_ 10, but _θ_ 5 and _θ_ 6 are unrestricted. Since our model is a submodel of that model, _T_ ( _X_ ) is also sufficient for our model.

- (e) Continuing with the three-parameter model above, consider a Bayesian api.i.d. _∼_

- proach where we assign priors _k ∼_ Unif( _{_ 4 _,_ 5 _,_ 6 _}_ ) independently of _γ_ 0 _, γ_ 1 Beta( _α, β_ ). Give a Gibbs sampler algorithm to sample from the posterior distribution of ( _k, γ_ 0 _, γ_ 1).

---

[← Solution](22-solution.md) · [Up: contents](index.md) · [Solution →](24-solution.md)
