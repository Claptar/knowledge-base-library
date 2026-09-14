---
title: 1. Solution
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/solution2020.pdf
source_file: sources/berkeley-stat210a/fall-2025/old-exams/solution2020.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. Solution

**Source:** [`old-exams/solution2020.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/solution2020.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- (a) The likelihood is


a one-parameter exponential family with natural parameter _η_ = log _θ_ , complete sufficient statistic _T_ = _X_ + 2 _Y_ , normalizing constant _B_ ( _θ_ ) = _θ_ + _θ_<sup>2</sup> , and carrier density _x_ !1 _y_ !<sup>(wrtthecountingmeasureonpairsof</sup> non-negative integers). _T_ is complete sufficient because log _θ_ varies over the entire real line, which is an open set.

- (b) Because E _θX_ = _θ_ , we can get a UMVUE by Rao-Blackwellizing it, to obtain the estimator


where _P_ ( _t_ ) includes all possible values of _X_ given _X_ + 2 _Y_ = _t_ , and the factors in the likelihood that involve _θ_ cancel in the numerator and denominator.

If _X_ = _Y_ = 2 then _T_ = 6, so


- (c) An i.i.d. sample from an exponential family with sufficient statistic _Xi_ + 2 _Yi_ is just another exponential family with sufficient statistic _T_ = � _i_<sup>_Xi_+�</sup> _i_<sup>2</sup><sup>_Yi_.The MLE sets the complete sufficient statistic equal to</sup> its expectation (in this case _n_ ( _θ_ + 2 _θ_<sup>2</sup> )) and solves for _θ_ :


Because _θ_<sup>ˆ</sup> _n >_ 0, we choose the positive root and the MLE is


4

(d) As a function of _θ_ , the log-likelihood and its derivatives are


We can calculate the Fisher information as either the variance of the score, in which case


or as minus the expectation of the second derivative, in which case


Either way, we can apply our usual result about the asymptotic distribution of the MLE to obtain


(e) This is a delta method problem for the differentiable function _g_ ( _x, y_ ) = ( _x_ +<sup>_√_</sup> _<u>y</u>_ <u>)</u> _/_ 2, _∇g_ ( _x, y_ ) = � 21<sup>_,_</sup> 4<sup>_~~√~~_</sup> <u>1</u> _<u>y</u>_ �. The argument to _g_ is ( _X n, Y n_ ), whose distribution is given by


from the CLT. The correct limiting variance is


and _g_ ( _θ, θ_<sup>2</sup> ) = _θ_ , so


The asymptotic relative efficiency is atrocious:


which is _maximized_ at 40% when _θ_ = 1, but tends to 0 as _θ_ becomes large _or_ small (you did not need to analyze the ARE on your exam, the formula would be enough).

Essentially, this is because as _θ →∞_ , _θ_<sup>2</sup> _≫ θ_ so the estimator should be driven by the much more informative _Y n_ , but as _θ →_ 0, _θ_<sup>2</sup> _≪ θ_ so the estimator should be driven by the much more informative _X n_ . Using the sufficient statistic _X n_ + 2 _Y n_ as our vehicle for estimation (as the UMVU and MLE both do) gets this right, because the one with larger mean will dominate the sum. By contrast _θ_<sup>˜</sup> _n_ does a very poor job because it gives both sources of information, _X n_ and _Y n_ , an equal voice in determining the “ensemble” estimator.

This automatic, adaptive reweighting of evidence from _X n_ vs. _Y n_ is just the kind of “everyday miracle” that happens when we use the MLE (or even just when we make a sufficiency reduction). We’d have to think very hard to always get this kind of thing right if we had to design an estimator from scratch.

- (f) The easiest choice here is the generalized likelihood ratio test. We have already calculated the MLE under the null in part (c), and the loglikelihood at the null MLE is


max

Under the full model, the MLE for ( _θ, λ_ ) is just ( _X n, Y n_ ), so the loglikelihood is


The GLRT statistic is twice the difference, which we can simplify a bit to


with _θ_<sup>ˆ</sup> _n_ as defined in part (c). The null has one parameter and the alternative has two, so we should reject if _G_ ( _X_ ) is above the upper _α_ quantile of a _χ_<sup>2</sup> 1<sup>distribution.</sup>

7

---

[← 1. One Poisson, two Poissons (30 points, 5 points / part).](03-1-one-poisson-two-poissons-30-points-5-points-part.md) · [Up: contents](index.md) · [2. A problem of limited means (20 points, 5 points / part). →](05-2-a-problem-of-limited-means-20-points-5-points-part.md)
