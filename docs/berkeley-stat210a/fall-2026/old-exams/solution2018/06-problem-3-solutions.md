---
title: Problem 3 solutions
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2018.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/solution2018.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 3 solutions

**Source:** [`old-exams/solution2018.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2018.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- (a) Let _T_ =<sup>�</sup> _i_<sup>_X_</sup> _i_<sup>2,whichisthecompletesufficientstatisticfortheGaus-</sup> sian scale family.

Multiplying the prior by the likelihood and dropping factors that do not depend on _θ_ , we have


where _α_ ˜ = _α_ + _n/_ 2 and _β_<sup>˜</sup> = _β_ + _T/_ 2.

The Bayes estimator for squared error loss is just the posterior mean:


- (b) We will use the fact that _T_ =<sup>�</sup> _i_<sup>_X_</sup> _i_<sup>2</sup><sup>_∼θχ_</sup> _n_<sup>2,whichhasmean</sup><sup>_nθ_and</sup> variance 2 _nθ_<sup>2</sup> . The bias is


The variance is


- (c) We want to solve


over _d ∈_ (0 _, ∞_ ). Expanding the square, we get


leading to the solution


Now using the fact that _θ_<sup>_−_1</sup> _∼_ Gamma( _α, β_ ), we have


- (d) We can essentially repeat the same computation from part (b), replacing _α −_ 1 with _α_ + 1, to obtain


Furthermore,


Now integrating over _θ_ to obtain the Bayes risk, we get


Now we can use the fact that


to obtain


Plugging into the previous expression, we get


(e) The relative squared error risk for a linear estimator is


using the fact that<sup>_<u>a</u>_</sup> _θ_ <u>�</u> _i_<sup>_X_</sup> _i_<sup>2has mean</sup><sup>_an_and variance 2</sup><sup>_a_2</sup><sup>_n_.Minimizing</sup> the risk gives _a_<sup>_∗_</sup> = _n_ +21<sup>,sothebestlinearestimator(forrelativerisk)</sup> is _n_ +21 � _i_<sup>_X_</sup> _i_<sup>2,whichhasrisk1</sup><sup>_−_</sup> _n_ +2 _<u>n</u>_<sup>=</sup> _n_ +22<sup>.Moreover,thisriskis</sup> constant in _θ_ .

Because the Bayes risk of any Bayes estimator gives a lower bound on the minimax risk, we know that the minimax risk is at least sup _α>_ 0 _n_ +2(2 _α_ +1)<sup>=</sup> _n_ +22<sup>.But our optimal linear estimator achieves constant risk of</sup> _n_ +22<sup>, giv-</sup> ing a matching upper bound; hence our estimator _n_ +21 � _i_<sup>_X_</sup> _i_<sup>2isindeed</sup> achieving the minimax risk.

**Note:** there was a lot of confusion about “constant risk” on this problem. The Bayes risk (average-case risk) is always a constant; we get it by averaging over _θ_ so there’s no way it could possibly depend on _θ_ . Similarly, any _a_ we choose will give us a constant relative risk function (try it); but some of those constant risk functions are strictly better than others, so they can’t all be minimax! What we know is: if a _Bayes estimator_ has a constant _risk function_ in _θ_ , that’s when we know we have a minimax estimator. That doesn’t actually apply in this problem because the risk functions of the Bayes estimators are not constant, and our linear estimators (which do have constant risk functions) aren’t among the Bayes estimators in the problem.

13

**4. Inference in the Laplace family (15 points, 5 points / part).** Some useful facts for this problem:

   - The Laplace location family with location parameter _θ_ is given by the density _pθ_ ( _x_ ) = _f_ ( _x − θ_ ), where _f_ ( _x_ ) = 2<sup><u>1</u></sup><sup>_e−|x|_.</sup>

   - The sign function is defined as


i.i.d. Assume we observe _X_ 1 _, . . . , Xn ∼_ Laplace( _θ_ ).

- (a) Find the score test of _H_ 0 : _θ_ = 0 vs. _H_ 1 : _θ >_ 0. Give the test statistic and threshold value in terms of a quantile of a binomial distribution (for simplicity you may assume _α_ is chosen so the binomial distribution has an exact _α_ quantile, so the test need not be randomized. Also note P _θ_ ( _X_ = 0) = 0 for all _θ_ , so you don’t need to worry about what happens there).

- (b) Suppose we are not so sure about the Laplace assumption, but we do believe the data come from a symmetric location family, meaning _pθ_ ( _x_ ) = _f_ ( _x − θ_ ) for some unknown _f_ : R _→_ [0 _, ∞_ ) that integrates to 1 and is symmetric about the origin (we can think of the nonparametric family as being parameterized by ( _θ, f_ )). Show that the test from part (a) is still a valid, finite-sample test of _H_ 0 : _θ_ = 0 vs. _H_ 1 : _θ >_ 0 in this larger family.

- (c) Now consider testing _H_ 0 : _θ ≤_ 0 vs. _H_ 1 : _θ >_ 0 (note the null hypothesis now includes negative values of _θ_ ). Show that the test from part (a) is a valid and unbiased level- _α_ test for the nonparametric family from part (b).

14

---

[← Problem 2 solutions](05-problem-2-solutions.md) · [Up: contents](index.md) · [Problem 4 solutions →](07-problem-4-solutions.md)
