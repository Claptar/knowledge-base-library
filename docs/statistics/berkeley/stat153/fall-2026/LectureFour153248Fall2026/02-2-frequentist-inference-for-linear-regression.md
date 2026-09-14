---
title: 2 Frequentist Inference for Linear Regression
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFour153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureFour153248Fall2026.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Frequentist Inference for Linear Regression

**Source:** [`LectureFour153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFour153248Fall2026.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The basic ideas behing frequentist inference are as follows:

1. Construct a method for estimating the unknown parameters. In the simple linear regression context, one can use least squares to estimate _β_ 0 _, β_ 1 _, . . . , βm_ . Probably the most popular estimation strategy is Maximum Likelihood Estimation (this requires writing down a likelihood function).

2. Calculate (exactly or using some approximations) the distribution of the estimators. Use quantiles of the distribution for obtaining interval estimates for the unknown parameters. The quantiles might themselves depend on other unknown parameters (which would then have to be replaced by estimates).

### **2.1 Estimates**

#### **2.1.1 Least Squares Estimates**

For linear regression, the estimates are obtained by the method of least squares, where the sum of squares


is minimized over all values of _β_ 0 _, β_ 1 _, . . . , βm_ . The minimizing values _β_<sup>ˆ</sup> 0 _, . . . , β_<sup>ˆ</sup> _m_ are known as least squares estimates.

Using the notation:


the sum of squares function _S_ ( _β_ 0 _, . . . , βm_ ) can be written as

_S_ ( _β_ ) = _∥y − Xβ∥_<sup>2</sup> _._

2

The least squares estimator _β_<sup>ˆ</sup> is given by the formula:


The proof of (3) is as follows. The gradient of _S_ ( _β_ ) is given by


Because _β_<sup>ˆ</sup> minimizes _S_ ( _β_ ), the gradient should equal zero when _β_ = _β_<sup>ˆ</sup> , and this leads to


#### **2.1.2 Maximum Likelihood Estimates (MLEs)**

i.i.d Under the assumption _ϵi ∼ N_ (0 _, σ_<sup>2</sup> ), we can write the likelihood explicitly and maximize it to obtain MLEs. As seen below, the MLE of _β_ 0 _, . . . , βm_ will coincide with least squares, but the ML method additionally will give an estimate of _σ_ .

i.i.d With the normality assumption _ϵi ∼ N_ (0 _, σ_<sup>2</sup> ), the linear regression model can be rewritten as:


The likelihood then becomes:


Recall _S_ ( _β_ 0 _, . . . , βm_ ) above is the sum of squares defined in (2). To write this likelihood, we are assuming that _x_ 1 _, . . . , xn_ are fixed. This assumption is fine if _xi_ = _i_ (regression with time as covariate) but not strictly true when _xi_ = _yi−_ 1 (auto-regression). We shall see how it is still approximately true in the case of AutoRegression later.

Another way to write the likelihood is to note that (5) is equivalent to:


In other words, the _n_ -dimensional vector _y_ is multivariate normal with mean _Xβ_ and covariance _σ_<sup>2</sup> _In_ . Recall that the density of the multivariate normal _y ∼ Nn_ ( _µ,_ Σ) is given by:


Thus the density corresponding to (7) is:


3

which is the same as (6) because _S_ ( _β_ ) = _∥y − Xβ∥_<sup>2</sup> .

The Maximum Likelihood Estimates of the parameters _β, σ_ are obtained by maximizing the likelihood. As maximizing a function is equivalent to maximizing its logarithm, we attempt to maximize the log-likelihood which leads to an easier maximization. The log-likelihood is:


To maximize the log-likelihood, we simply take derivatives with respect to the unknown parameters _β, σ_ and equate those to zero:


The first equation coincide with the corresponding equations (4) for minimizing least squares. This shows that the MLE for _β_ coincides with the least squares estimators (3). The MLE for _σ_ is given by the third equation above (with _β_ replaced by _β_<sup>ˆ</sup> respectively):


i.i.d To summarize, under the assumption of normality on the errors _ϵi ∼ N_ (0 _, σ_<sup>2</sup> ), the MLE of _β_ coincides with the least squares estimator (3), and the MLE of _σ_ is given by (8).

### **2.2 Distribution of Estimates**

Here we need to calculate the distribution of the estimates. For _β_<sup>ˆ</sup> (given by (3)), using the fact (7) we can write

_β_ ˆ = ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_T_</sup> _y ∼ N_ (( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_T_</sup> _Xβ, σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_T_</sup> _X_ ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> ) = _N_ ( _β, σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> ) _._ Here we used the following fact:


Because _β_<sup>ˆ</sup> _∼ N_ ( _β, σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> ), it is clear that _β_<sup>ˆ</sup> is unbiased for _β_ .

The distribution of _σ_ ˆMLE is given by:


where _χ_<sup>2</sup> _n−m−_ 1<sup>isthechi-squareddistributionwith</sup><sup>_n −m −_1degreesoffreedom.Wewill</sup> not go into the proof of this fact.

The mean of the chi-squared distribution equals its degrees of freedom which implies that


4

Therefore the MLE for _σ_<sup>2</sup> is not unbiased (in contrast, the MLEs _β_<sup>ˆ</sup> 0 and _β_<sup>ˆ</sup> 1 are unbiased). It is easy to correct the bias leading to the following unbiased estimator of _σ_<sup>2</sup> :


Usage of ˆ _σ_ unbiased is much more common than that of ˆ _σ_ MLE (note that ˆ _σ_ unbiased is not unbiased for _σ_ ; rather the square of _σ_ ˆunbiased is unbiased for _σ_<sup>2</sup> ).

Another fact is that _β_<sup>ˆ</sup> and _σ_ ˆunbiased<sup>2areindependent.</sup>

These facts are used to derive the following confidence interval for a component _βj_ of _β_ :


where _tn−m−_ 1 _,α/_ 2 is the positive point such that P _{tn−m−_ 1 _≥ tn−m−_ 1 _,α/_ 2 _}_ = _α/_ 2 (i.e., the _t_ -distribution with _n − m −_ 1 degrees of freedom assigns probability mass _α/_ 2 to the right of _tn−m−_ 1 _,α/_ 2). Also ( _X_<sup>_T_</sup> _X_ )<sup>_j_+1</sup><sup>_,j_+1</sup> is the ( _j_ + 1 _, j_ + 1)-th diagonal entry of ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> . Note that _β_<sup>ˆ</sup> _∼ N_ ( _β, σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> ) so that _β_<sup>ˆ</sup> _j ∼ N_ ( _βj, σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_j_+1</sup><sup>_,j_+1</sup> ) (the index is _j_ + 1 instead of _j_ on the right hand side because the first component of _β_<sup>ˆ</sup> is _β_<sup>ˆ</sup> 0 and not _β_<sup>ˆ</sup> 1).

(9) is a valid confidence interval because:


where _tn−m−_ 1 is the _t_ -distribution with _n − m −_ 1 degrees of freedom.

This section on deriving the distributions of the frequentist estimates has been discussed for completeness. We will not be using these facts or ideas in this course.

---

[← 1 Multiple Linear Regression](01-1-multiple-linear-regression.md) · [Up: contents](index.md) · [3 Bayesian Inference for Linear Regression →](03-3-bayesian-inference-for-linear-regression.md)
