---
title: 2 Estimation of β 0 and β 1
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwo153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwo153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Estimation of β 0 and β 1

**Source:** [`LectureTwo153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwo153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **2.1 Least Squares Estimates**

The estimates of _β_ 0 and _β_ 1 reported by standard libraries (such as `statsmodels` ) are obtained using the method of least squares. This involves minimizing the sum of squares criterion:


over all values of _β_ 0 and _β_ 1. It is left as an exercise to verify that:

where


### **2.2 MLE under Normality of Errors**

Suppose we assume that the error terms _ϵ_ 1 _, . . . , ϵn_ in (2) are i.i.d normal with mean zero and some variance _σ_<sup>2</sup> :


Then the least squares estimates of _β_ 0 and _β_ 1 coincide with the Maximum Likelihood Estimates (MLEs).

Another way of writing the model (2) and (4) is:


To obtain the MLEs of the parameters ( _β_ 0 _, β_ 1 as well as _σ_ ), we need to write the likelihood function and then maximize it. The likelihood function is the joint density of the data for

2

fixed values of the parameters _β_ 0 _, β_ 1 _, σ_ :


where _S_ ( _β_ 0 _, β_ 1) is the sum of squares (3).


To write this likelihood, we are assuming that _x_ 1 _, . . . , xn_ are fixed. This assumption is fine if _xi_ = _i_ (regression with time as covariate) but not strictly true when _xi_ = _yi−_ 1 (autoregression). We shall see how it is still approximately true in the case of AutoRegression later.

Maximization of the likelihood is a three variable optimization problem (the variables being _β_ 0 _, β_ 1 _, σ_ ). The optimal values of _β_ 0 and _β_ 1 in this problem coincide with the least squares estimate. We shall see why in the next lecture.

3

---

[← 1 Simple Linear Regression](01-1-simple-linear-regression.md) · [Up: contents](index.md)
