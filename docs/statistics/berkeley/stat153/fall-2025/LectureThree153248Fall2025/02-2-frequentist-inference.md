---
title: 2 Frequentist Inference
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureThree153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureThree153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Frequentist Inference

**Source:** [`LectureThree153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureThree153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The basic ideas behing frequentist inference are as follows:

1. Construct a method for estimating the unknown parameters. In the simple linear regression context, one can use least squares to estimate _β_ 0 and _β_ 1. Probably the most popular estimation strategy is Maximum Likelihood Estimation (this requires writing down a likelihood function).

2. Calculate (exactly or using some approximations) the distribution of the estimators. Use quantiles of the distribution for obtaining interval estimates for the unknown parameters. The quantiles might themselves depend on other unknown parameters (which would then have to be replaced by estimates).

1

For linear regression, the point estimates are obtained by the method of least squares, where the sum of squares


is minimized over all values of _β_ 0 and _β_ 1. To minimize _S_ ( _β_ 0 _, β_ 1), we take derivatives with respect to _β_ 0 _, β_ 1 and equate to zero:


It is an exercise to verify that the solution to the above equations is given by:


where


We shall refer to (4) as the least squares estimators.

Maximum Likelihood Estimation (MLE) can also be used. To write down the likelihood, one most commonly uses the normality assumption:


With this normality assumption, the linear regression model can be rewritten as:


The likelihood then becomes:


Recall _S_ ( _β_ 0 _, β_ 1) above is the sum of squares defined in (2). To write this likelihood, we are assuming that _x_ 1 _, . . . , xn_ are fixed. This assumption is fine if _xi_ = _i_ (regression with time as covariate) but not strictly true when _xi_ = _yi−_ 1 (auto-regression). We shall see how it is still approximately true in the case of AutoRegression later.

The Maximum Likelihood Estimates of the parameters _β_ 0 _, β_ 1 _, σ_ are obtained by maximizing the likelihood. As maximizing a function is equivalent to maximizing its logarithm, we attempt to maximize the log-likelihood which leads to an easier maximization. The log-likelihood is:


2

To maximize the log-likelihood, we simply take derivatives with respect to the unknown parameters _β_ 0 _, β_ 1 _, σ_ and equate those to zero:


The first two equations coincide with the corresponding equations (3) for minimizing least squares. This shows that the MLEs for _β_ 0 and _β_ 1 coincide with the least squares estimators (4). The MLE for _σ_ is given by the third equation above (with _β_ 0 and _β_ 1 replaced by _β_<sup>ˆ</sup> 0 and _β_<sup>ˆ</sup> 1 respectively):


The next step is to determine the distribution of the estimators. Let us illustrate this with _β_ ˆ1:


where the second equality uses<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_y_¯(</sup><sup>_xi −x_¯)=</sup><sup>_y_¯ �</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_xi −x_¯)=0.Underthenormality</sup> assumption (6), it is easy to check that


For _β_<sup>ˆ</sup> 0, one can derive a similar normal distribution (proof omitted):


For _σ_ ˆMLE, the distribution becomes (proof omitted):


where _χ_<sup>2</sup> _n−_ 2<sup>isthechi-squareddistributionwith</sup><sup>_n −_2degreesoffreedom.Themeanofthe</sup> chi-squared distribution equals its degrees of freedom which implies that


Therefore the MLE for _σ_<sup>2</sup> is not unbiased (in contrast, the MLEs _β_<sup>ˆ</sup> 0 and _β_<sup>ˆ</sup> 1 are unbiased). It is easy to correct the bias leading to the following unbiased estimator of _σ_<sup>2</sup> :


Usage of ˆ _σ_ unbiased is much more common than that of ˆ _σ_ MLE (note that ˆ _σ_ unbiased is not unbiased for _σ_ ; rather the square of _σ_ ˆunbiased is unbiased for _σ_<sup>2</sup> ).

Another important fact is that ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1) and _σ_ ˆunbiased<sup>2areindependent.</sup>

3

These facts are used to derive the following confidence interval for _β_ 1:


where _tn−_ 2 _,α/_ 2 is the positive point such that P _{tn−_ 2 _≥ tn−_ 2 _,α/_ 2 _}_ = _α/_ 2 (i.e., the _t_ -distribution with _n −_ 2 degrees of freedom assigns probability mass _α/_ 2 to the right of _tn−_ 2 _,α/_ 2). (11) is a valid confidence interval because:


where _tn−_ 2 is the _t_ -distribution with _n −_ 2 degrees of freedom.

---

[← 1 Simple Linear Regression](01-1-simple-linear-regression.md) · [Up: contents](index.md) · [3 Bayesian Inference →](03-3-bayesian-inference.md)
