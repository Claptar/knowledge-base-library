---
title: 3. Gamma palooza (25 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2020.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/solution2020.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Gamma palooza (25 points, 5 points / part).

**Source:** [`units/old-exams/solution2020.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2020.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some useful facts for this problem:

- For shape parameter _k >_ 0 (not necessarily an integer) and scale parameter _σ >_ 0, the Gamma( _k, σ_ ) distribution has density


Its mean and variance are _kσ_ and _kσ_<sup>2</sup> , respectively.

- The _χ_<sup>2</sup> _d_<sup>distributionisGamma(</sup><sup>_d/_2</sup><sup>_,_2).Itisusuallydefinedwhen</sup><sup>_d_is</sup> an integer, but the density is still a proper density for any _d >_ 0. The same is true for distributions derived from the _χ_<sup>2</sup> like _t_ or _F_ whose “degrees of freedom” argument(s) can take on any positive real value.

- Assume that we observe independent random variables _Xij_ with


Unless otherwise specified, assume all _ki_ and _σj_ are unknown and strictly positive (different parts of the problem will consider simpler submodels). Let _Sj_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xij_and</sup><sup>_Mi_=</sup><sup>_Xi_1</sup><sup>_Xi_2.</sup>

- (a) Show that _T_ ( _X_ ) = ( _S_ 1 _, S_ 2 _, M_ 1 _, . . . , Mn_ ) is a complete sufficient statistic for this model.

- (b) Assume (for this part **only** ) that _k_ 1 _, . . . , kn_ are known. Give an explicit formula for an exact equal-tailed confidence interval for _σ_ 2 _/σ_ 1, in terms of the sufficient statistics described above and quantiles for one or more known distributions from class.

- (c) Assume instead (for this part **only** ) that _σ_ 1 and _σ_ 2 are known, and also it is known that _k_ 1 = _k_ 2 = _· · ·_ = _kn_ = _k_ , but the common value _k_ is unknown. Suggest a UMP test of the hypothesis _H_ 0 : _k_ = _k_ 0 against the alternative _H_ 1 : _k > k_ 0, where _k_ 0 is generic. Give the test statistic and explain how to calculate the rejection cutoff (give an explicit recipe that anyone can follow).

- (d) Suppose (for this part **only** ) that _n_ = 2 with all of _k_ 1 _, k_ 2 _, σ_ 1 _, σ_ 2 unknown. Suggest an exact UMPU test of _H_ 0 : _k_ 1 = _k_ 2 against _H_ 1 : _k_ 1 _> k_ 2. Say what test statistic you would use and give a precise mathematical description of the rejection cutoff, but you do **not** need to give an explicit expression or recipe for how to calculate it.

11

- (e) (*) Drop all assumptions from previous parts, so _n_ is arbitrary and no parameters of the model are known.

Suppose that we begin doubting the validity of our Gamma model, and we want to generalize it to replace the Gamma family with a generic scale family:


for a generic, unknown, continuous distribution function _Gi_ that puts all its mass on positive values of _x_ (i.e., _Gi_ (0) = 0). We want to guarantee Type I error control no matter what _G_ 1 _, . . . , Gn_ are.

Explain how to calculate an exact 95% confidence interval for _σ_ 2 _/σ_ 1. Your interval must be nontrivial; we will not award any points for answers like “flip a coin and cover the entire parameter space with probability 95%.”

( **Hint:** This problem is closely related to testing _H_ 0 : _σ_ 1 = _σ_ 2 against _H_ 1 : _σ_ 1 _> σ_ 2. The testing problem might be easier to think about at first, and partial credit will be awarded for making progress on it.)

12

---

[← 2. Solution](06-2-solution.md) · [Up: contents](index.md) · [3. Solution →](08-3-solution.md)
