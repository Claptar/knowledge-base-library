---
title: 3. Gamma palooza (25 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/final2020.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/final2020.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Gamma palooza (25 points, 5 points / part).

**Source:** [`units/old-exams/final2020.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/final2020.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

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

5

- (e) (*) Drop all assumptions from previous parts, so _n_ is arbitrary and no parameters of the model are known.

Suppose that we begin doubting the validity of our Gamma model, and we want to generalize it to replace the Gamma family with a generic scale family:


for a generic, unknown, continuous distribution function _Gi_ that puts all its mass on positive values of _x_ (i.e., _Gi_ (0) = 0). We want to guarantee Type I error control no matter what _G_ 1 _, . . . , Gn_ are.

Explain how to calculate an exact 95% confidence interval for _σ_ 2 _/σ_ 1. Your interval must be nontrivial; we will not award any points for answers like “flip a coin and cover the entire parameter space with probability 95%.”

( **Hint:** This problem is closely related to testing _H_ 0 : _σ_ 1 = _σ_ 2 against _H_ 1 : _σ_ 1 _> σ_ 2. The testing problem might be easier to think about at first, and partial credit will be awarded for making progress on it.)

6

**4. Apocalypse** _τ_ **(25 points, 5 points / part).**

Some useful facts for this problem:

_•_ For _σ_<sup>2</sup> _>_ 0 and _µ ∈_ R, the Gaussian density for _X ∼ N_ ( _µ, σ_<sup>2</sup> ) is


Its mean and variance are _µ_ and _σ_<sup>2</sup> .

Assume we observe i.i.d. pairs ( _Xi, Yi_ ) for _i_ = 1 _, . . . , n_ , where _X_ 1 _, . . . , Xn ∈_ R<sup>_k_</sup> are sampled from a known density _q_ ( _x_ ) and _Yi_ are real numbers with


Assume the errors _ε_ 1 _, . . . , εn_ are independent of _X_ 1 _, . . . , Xn_ .

The parameters _τ ∈_ [ _−_ 1 _,_ 1] and _σ_<sup>2</sup> _>_ 0 are fixed and unknown, but the real-valued function _fτ_ ( _x_ ) is known up to its parameter _τ_ .

Assume that

- _fτ_ ( _x_ ) is infinitely differentiable _with respect to τ_ , with first and second derivatives


   - _gτ_ ( _x_ ) _>_ 0 for all _τ_ and _x_ .

   - _|gτ_ ( _x_ ) _|, |hτ_ ( _x_ ) _| ≤_ 1 for all _τ_ and _x_ .

- (a) Assume (for this part **only** ) that _Xi_ are fixed instead of random, while i.i.d.

- the errors still have the same distribution, _εi ∼ N_ (0 _, σ_<sup>2</sup> ). Consider testing _H_ 0 : _τ_ = 0 against the alternative _H_ 1 : _τ̸_ = 0 using the test statistic


where


What number should we plug in for _d_ ? Give the distribution of _T_ under the null, and justify your answer.

7

- (b) Now go back to assuming that _Xi_ are random, sampled i.i.d. from an unknown distribution. Show that the test from part (a) still works; i.e. its distribution under the null is independent of _X_ 1 _, . . . , Xn_ .

- (c) Assume (for this part **only** ) that _σ_<sup>2</sup> is known. Show that the MLE _τ_ ˆ _n_ is consistent for _τ_ as _n →∞_ . (For full credit, please check appropriate conditions).

- (d) Continue to assume (for this part **only** ) that _σ_<sup>2</sup> is known. Assuming the MLE is consistent, and _τ ∈_ ( _−_ 1 _,_ 1) (i.e. not at the boundary of the parameter space), find its asymptotic distribution as _n →∞_ . (You do not need to check conditions for this).

- (e) (*) Suppose we add an intercept to the model, so


Can we still estimate _τ_ consistently as _n →∞_ using maximum likelihood? Prove or give a counterexample.

8

---

[← 2. A problem of limited means (20 points, 5 points / part).](04-2-a-problem-of-limited-means-20-points-5-points-part.md) · [Up: contents](index.md)
