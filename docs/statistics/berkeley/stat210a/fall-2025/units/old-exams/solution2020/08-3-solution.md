---
title: 3. Solution
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2020.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/solution2020.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Solution

**Source:** [`units/old-exams/solution2020.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2020.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

(a) The likelihood is


- (b) If _k_ 1 _, . . . , kn_ are known then ( _S_ 1 _, S_ 2) is complete sufficient. We can make a sufficiency reduction, after which we have


Let _ρ_ = _σ_ 2 _/σ_ 1 and _R_ = _S_ 2 _/S_ 1, then


As a result, if _c_ 1 and _c_ 2 are respectively the lower and upper _α/_ 2 quantiles of _F_ 2 _k_ + _,_ 2 _k_ +, then


So the CI is � _cR_ 2<sup>_,_</sup> _c_<sup>_<u>R</u>_</sup> 1 � (note the ordering).

- (c) If _σ_ 1 and _σ_ 2 are known, and _k_ 1 = _· · ·_ = _kn_ = _k_ , then the likelihood reduces to the one-parameter exponential family,


13

so we should reject for large values of _P_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Mi_=�</sup> _i,j_<sup>_Xij_,or</sup> equivalently for large values of _P_ 1 = _σ_ 1<sup>_<u>n</u>_</sup> <u>1</u><sup>_σ_</sup> 2<sup>_<u>n</u>_</sup> � _i,j_<sup>_Xij_,whosedistribution</sup> doesn’t depend on _σ_ 1 _, σ_ 2. To find the rejection threshold for _P_ 1, which is a product of 2 _n_ independent Gamma( _k_ 0 _,_ 1) random variables under the null, we can repeatedly sample from this distribution and take the upper _α_ quantile of the empirical distribution. This is exact up to Monte Carlo error, which we can make as small as we want.

- (d) We can rewrite the likelihood again as


so that the first term in the exponent represents the parameter of interest and the other three represent the nuisance parameters ( _k_ 1 + _k_ 2 _, σ_ 1 _, σ_ 2). The UMPU test, then, rejects for large values of _M_ 1 _/M_ 2, conditional on ( _M_ 1 _M_ 2 _, S_ 1 _, S_ 2).

- (e) If _ρ_ = _σ_ 2 _/σ_ 1, then


We could use this to construct a permutation test of _H_ 0 : _ρ_ = _ρ_ 0. A sufficient statistic for the null model consists of the unordered sets _{Xi_ 1 _, Xi_ 2 _/ρ_ 0 _}_ for _i_ = 1 _, . . . , n_ . Write that statistic as _U_ ( _X_ ); then we can sample from the distribution of _X_ given _U_ ( _X_ ) by randomly permuting within each pair ( _Xi_ 1 _, Xi_ 2 _/ρ_ 0) independently for each _i_ . Under alternative values of _ρ > ρ_ 0, we will tend to have _Xi_ 2 _/ρ_ 0 _> Xi_ 1, so we can pick any test statistic that will tend to be large when that is the case. (Getting everything right up to here would be enough for 4 points out of the possible 5).

If we pick a test statistic that we can easily evaluate for all the different candidate values of _ρ_ 0, then we can get a confidence interval too. There

14

are a lot of possible choices but a robust and convenient one would be


because the exchangeability of ( _Xi_ 1 _, Xi_ 2 _/ρ_ 0) under the null means each indicator has an equal 50% chance to be 1 or 0. Let _Ri_ = _Xi_ 2 _/Xi_ 1, then this is saying if _ρ_ = _ρ_ 0 then the sample median value of _Ri_ should be about _ρ_ 0, and we reject if too many _Ri_ values are above _ρ_ 0. If we want to make the test two-sided, then we should reject if too many _or_ too few _Ri_ values are above _ρ_ 0. This test statistic is convenient in part because we don’t have to do Monte Carlo sampling; we just know the null distribution of _B_ and it doesn’t even depend on _U_ .

Ignoring randomizing at the boundary, assume _b_ 1 _≥_ 1 and _b_ 2 = _n − b_ 1 are respectively the lower and upper _α/_ 2 quantiles of Binom( _n,_ 1 _/_ 2) (if _b_ 1 = 0 then _n_ is too small for the binomial test to ever reject, so we have to randomize at the boundary or use a different approach). Then the two-sided permutation test _fails_ to reject at level _α_ if


where _R_ (1) _> R_ (2) _> · · · > R_ ( _n_ ) are the order statistics of _R_ 1 _, . . . , Rn_ . As a result, [ _R_ ( _n_ +1 _−b_ 1) _, R_ ( _b_ 1)] is a valid confidence interval for _ρ_ (note P _ρ_ ( _R_ ( _b_ 1) = _ρ_ ) = 0 so we can use the closed interval without affecting the coverage).

15

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

16

- (b) Now go back to assuming that _Xi_ are random, sampled i.i.d. from an unknown distribution. Show that the test from part (a) still works; i.e. its distribution under the null is independent of _X_ 1 _, . . . , Xn_ .

- (c) Assume (for this part **only** ) that _σ_<sup>2</sup> is known. Show that the MLE _τ_ ˆ _n_ is consistent for _τ_ as _n →∞_ . (For full credit, please check appropriate conditions).

- (d) Continue to assume (for this part **only** ) that _σ_<sup>2</sup> is known. Assuming the MLE is consistent, and _τ ∈_ ( _−_ 1 _,_ 1) (i.e. not at the boundary of the parameter space), find its asymptotic distribution as _n →∞_ . (You do not need to check conditions for this).

- (e) (*) Suppose we add an intercept to the model, so


Can we still estimate _τ_ consistently as _n →∞_ using maximum likelihood? Prove or give a counterexample.

17

---

[← 3. Gamma palooza (25 points, 5 points / part).](07-3-gamma-palooza-25-points-5-points-part.md) · [Up: contents](index.md) · [4. Solution →](09-4-solution.md)
