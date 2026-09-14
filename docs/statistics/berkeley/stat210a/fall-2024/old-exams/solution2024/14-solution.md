---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2024.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2024.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`old-exams/solution2024.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2024.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

There is no admissible unbiased estimator. If _α_ is known then _Tb_ is ancillary and we can make a further reduction to _Tw ∼_ Binom( _Nw, α_ + _β_ ), where _α_ is known and _β ≥_ 0. The UMVU estimator _Tw/Nw − α_ can be negative, so it is dominated by ( _Tw/Nw − α_ )+ which has smaller loss almost surely. If the UMVUE is inadmissible then so is any other unbiased estimator.

- (d) (*) Now assume that the _β_ parameter possibly varies by group. That is, _πi,j_ = _α_ +<sup>�</sup><sup>_K_</sup> _k_ =1<sup>_βk_1</sup><sup>_{g_(</sup><sup>_i_) =</sup><sup>_g_(</sup><sup>_j_) =</sup><sup>_k}_, where</sup><sup>_α ∈_[0</sup><sup>_,_1] and</sup><sup>_β_1</sup><sup>_, . . . , βK∈_[0</sup><sup>_,_1</sup><sup>_−α_]</sup> are all unknown.

Assume we want to test the hypothesis _H_ 0 : _β_ 1 = _. . ._ = _βK_ = 0 against the alternative _H_ 1 : max _k βk >_ 0. Assume we have an estimator _β_<sup>ˆ</sup><sup>_∗_</sup> ( _X_ ) for the parameter _β_<sup>_∗_</sup> = max _k βk_ , and we want to will use a test that rejects for large values of _β_<sup>ˆ</sup><sup>_∗_</sup> ( _X_ ). How could we carry out an exact (finite-sample) test using _β_<sup>ˆ</sup><sup>_∗_</sup> as the test statistic? You do not need to give an explicit formula for the threshold, but explain how you would calculate it either in words or pseudocode. **Solution:** Under _H_ 0, all edges have the same chance of occurring, so _T_ + = _Tw_ + _Tb_ is complete sufficient and the conditional distribution given _T_ + = _t_ is uniform over all configurations with exactly _t_ total edges. Sampling from this conditional distribution is equivalent to permuting the � _m_ 2 � total _Xi,j_ values.

To be more precise, we can generate _B_ graphs by placing _t_ edges uniformly at random and calculate _θ_<sup>ˆ</sup><sup>_∗b_</sup> based on the _b_ th such graph. The exact permutation _p_ -value is 1+1 _B_ � _b_<sup>1</sup><sup>_{θ_ˆ</sup><sup>_∗b≥θ_ˆ</sup><sup>_∗_(</sup><sup>_X_)</sup><sup>_}_.</sup>

10

---

[← Solution](13-solution.md) · [Up: contents](index.md) · [4. Estimation in the Geometric model (25 points, 5 points / part). →](15-4-estimation-in-the-geometric-model-25-points-5-points-part.md)
