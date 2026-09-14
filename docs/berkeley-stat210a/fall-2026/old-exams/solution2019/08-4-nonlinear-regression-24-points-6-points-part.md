---
title: 4. Nonlinear regression (24 points, 6 points / part).
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2019.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/solution2019.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4. Nonlinear regression (24 points, 6 points / part).

**Source:** [`old-exams/solution2019.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2019.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note the Gaussian density is printed in the preamble of Problem 2. We are given a sample of _n_ pairs ( _xi, Yi_ ) where _x_ 1 _, . . . , xn ∈_ R are fixed real numbers and


Assume (except where otherwise specified) that:

- _g_ : R _→_ R is a known function which is strictly increasing and infinitely differentiable.

- _h_ : R _→_ (0 _, ∞_ ) is a known continuous function.

- _α, β ∈_ R and _σ_<sup>2</sup> _>_ 0 are unknown

Finally, let _ri_ = _Yi − g_ (ˆ _α_ + _βx_<sup>ˆ</sup> _i_ ) denote the _i_ th residual. Throughout the problem, assume we are estimating the parameter vector ( _α, β, σ_<sup>2</sup> ) jointly by maximum likelihood; let (ˆ _α, β,_<sup>ˆ</sup> ˆ _σ_<sup>2</sup> ) denote the joint MLE.

- (a) Show that the MLE for _α_ and _β_ is found by setting weighted averages of the residuals to 0:


and give explicit expressions for the weights _wi_ in terms of the data, the functions _g_ and _h_ , and the maximum likelihood estimators _α,_ ˆ _β,_<sup>ˆ</sup> ˆ _σ_<sup>2</sup> .

- (b) Give an explicit expression for the MLE for _σ_<sup>2</sup> , i.e. _σ_ ˆ<sup>2</sup> , in terms of the data, the functions _g_ and _h_ , and the maximum likelihood estimators _α,_ ˆ _β_<sup>ˆ</sup> .

- (c) (*) Now assume (for this part **ONLY** ) that instead of fixed numbers we observe i.i.d. random variables _X_ 1 _, . . . , Xn_ , which are continuous and bounded random variables ( _|Xi| ≤ B_ almost surely, for some _B >_ 0.) Give the asymptotic distribution of the maximum likelihood estimators (ˆ _α, β_<sup>ˆ</sup> ) in terms of the functions _g_ and _h_ , and expectations of suitable random variables. The limit is taken as _n →∞_ with the other parameters fixed.

You may assume without proof that (ˆ _α, β,_<sup>ˆ</sup> ˆ _σ_<sup>2</sup> ) are consistent for the true population values, and that all of the regularity conditions from class

13

for our theorem on the asymptotic distribution of the MLE hold (the log-likelihood and its derivatives are well-behaved in the required sense). You do not need to write down what the conditions are, either.

( **Hint:** it might be easier to do the problem assuming _σ_<sup>2</sup> is known, and then explain why the answer doesn’t change when _σ_<sup>2</sup> is unknown.)

- (d) (*) We now go back to assuming the _xi_ values are fixed. Now assume _h_ ( _z_ ) _≡_ 1 but _g_ is completely unknown (apart from the restrictions described in the preamble: strictly increasing and infinitely differentiable). Give a finite-sample test of _H_ 0 : _β ≤_ 0 vs _H_ 1 : _β >_ 0. You should provide a test statistic and describe how to calculate the critical value. For full credit you must show your test controls the rejection probability throughout the composite null hypothesis (that is, for all valid choices of _g_ , _α_ , and _σ_<sup>2</sup> .)

Since we are already using the letter _α_ for the intercept, I suggest using _a_ to denote the significance level in your answer.

14

---

[← 3. Solution.](07-3-solution.md) · [Up: contents](index.md) · [4. Solution →](09-4-solution.md)
