---
title: 4. Solution
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/solution2019.pdf
source_file: sources/berkeley-stat210a/fall-2025/old-exams/solution2019.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4. Solution

**Source:** [`old-exams/solution2019.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/solution2019.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

(a) The log likelihood is


The first derivative with respect to _α_ is

for _wi_ = _g_ ˙( _α_ + _βxi_ ) _/h_ ( _xi_ ). Similarly, the gradient with respect to _β_ is


Any local minimizer of the log-likelihood sets the gradient equal to zero. ( **Remark:** we gave full credit for just setting the derivative to zero, but the question statement should have been clearer about the difference between local optimality and global optimality: it is a necessary but not sufficient condition that the gradient should be zero, but it is possible for there to be more than one local minimum. It is also possible, I realized later, to come up with counterexamples where there is no MLE because the likelihood is maximized at infinity.)

Note that our estimate of _σ_<sup>2</sup> plays no role in determining _α_ ˆ and _β_<sup>ˆ</sup> ; we would get the same estimators for _α_ and _β_ whether we estimate _σ_<sup>2</sup> or whether it is known. This will be useful in part (c).

(b) Differentiating with respect to _σ_<sup>2</sup> gives


and setting the derivative equal to 0 while the other parameters are at their MLEs gives


15

- (c) First assume _σ_<sup>2</sup> _>_ 0 is known. Then the only two unknown parameters are _α_ and _β_ , and the score is


The variance of the score conditional on _X_ is


The expectation of the score given _X_ is zero, so the marginal variance is simply the expectation of the conditional variance:


Note that the exam should have guaranteed _h_ ( _Xi_ ) didn’t have positive density at zero; that could make the expectation infinite. Assuming it is not infinite though, and the conditions hold for our theorem on the asymptotic distribution, then we have


If instead _σ_<sup>2</sup> is unknown, nothing actually changes because, as noted in part (a), the MLE (ˆ _α, β_<sup>ˆ</sup> ) is the same regardless of _σ_<sup>2</sup> , which merely scales the log-likelihood up or down. Since it is the same random variable regardless of whether _σ_<sup>2</sup> is known or estimated, it also has the same limiting distribution regardless.

- (d) Let _µi_ = _g_ ( _α_ + _βxi_ ) and assume without loss of generality that _µi_ is non-decreasing in _i_ . If _β_ = 0 then _µ_ 1 = _· · ·_ = _µn_ and the _Yi_ values are i.i.d., but if _β >_ 0 then the means are increasing too (and if _β <_ 0 the means are decreasing). We can use a permutation test whose test statistic is meant to pick up correlation between _x_ and _µ_ , for example _T_ ( _Y_ ) = _x_<sup>_′_</sup> _Y_ . We use a Monte Carlo version of the permutation test

16

as usual: take _B_ random permutations and reject if _T_ ( _Y_ ) is among the _⌊a_ ( _B_ + 1) _⌋_ largest of _T_ ( _Y_ ) _, T_ ( _π_ 1 _Y_ ) _, . . . , T_ ( _πBY_ ).

If _Yi_ = _µi_ + _ϵi_ and assume _β ≤_ 0. Then for a generic permutation _π_ ,


Note that ( _x_<sup>_′_</sup> _ϵ, x_<sup>_′_</sup> ( _π_ 1 _ϵ_ ) _, x_<sup>_′_</sup> ( _πBϵ_ )) are exchangeable no matter what, but _x_<sup>_′_</sup> _µ ≤ x_<sup>_′_</sup> ( _πµ_ ) for all _π_ ; therefore _T_ ( _Y_ ) has a less than _a_ chance of being among the _⌊a_ ( _B_ + 1) _⌋_ largest values.

17

---

[← 4. Nonlinear regression (24 points, 6 points / part).](08-4-nonlinear-regression-24-points-6-points-part.md) · [Up: contents](index.md)
