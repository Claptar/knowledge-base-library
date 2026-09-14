---
title: 2 High-dimensional Version of (2)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 High-dimensional Version of (2)

**Source:** [`LectureTen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We illustrate overfitting prevention via regularization in the high-dimensional model obtained by using all possible _cj_ ’s in (2). This model is described below. Note that because our time _t_ runs from 1 _, . . . , n_ , we can restrict each _cj_ to the open interval (1 _, n_ ). Indeed, when _cj ≤_ 1, the ReLU term ReLU( _t − cj_ ) coincides with the linear term _t − cj_ (which can be absorbed in _β_ 0 + _β_ 1 _t_ ) and when _cj ≥ n_ , the ReLU term ReLU( _t − cj_ ) equals zero.

In fact, it turns out that it is enough to restrict _cj_ to be an integer in (1 _, n_ ) i.e., _cj ∈ {_ 2 _, . . . , n −_ 1 _}_ . This is because ReLU( _t − cj_ ) _, t_ = 1 _, . . . , n_ for any other _cj_ can be rewritten as a linear combination of ReLU( _t − cj_ ) _, t_ = 1 _, . . . , n_ for integer _cj_ . As an example, note that

ReLU( _t −_ 5 _._ 7) = 0 _._ 3ReLU( _t −_ 5) + 0 _._ 7ReLU( _t −_ 6) for all _t ≤_ 5 and _t ≥_ 6 _._

Allowing all possible _cj_ ’s in _{_ 2 _, . . . , n −_ 1 _}_ leads to the model:


i.i.d where, as always, _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). Note that we are writing _β_ 1( _t −_ 1) instead of _β_ 1 _t_ for aesthetical reasons. This does not change the model in any way.

The unknown parameters in this model are _β_ 0 _, β_ 1 _, . . . , βn−_ 1 as well as _σ_ . Here are main differences between the two models (2) and (4):

1. The model (2) will be typically used with a small value of _k_ (such as 1 _,_ 2 _,_ 3 _,_ 4). This makes it a low-dimensional model. On the other hand, the number of unknown parameters in (4) equals _n_ +1 which is quite large. So (4) is an example of a high-dimensional model.

2. (2) is a nonlinear model because of the presence of the parameters _c_ 1 _, . . . , ck_ . On the other hand, there are no such nonlinear parameters in (4) which makes it a linear regression model.

To summarize, (2) is a low-dimensional nonlinear regression model, while (4) is a highdimensional linear regression model.

2

### **2.1 Least Squares in** (4) **interpolates data**

Since (4) is a linear regression model, we can estimate the coefficients in the usual way by the MLE, or equivalently, least squares by minimizing


over all _β_ 0 _, . . . , βn−_ 1. The smallest value achievable in the above minimization will be the RSS.

Because the number of coefficients equals the number of data points, the optimization (5) will give a perfect fit to the data leading to _RSS_ = 0. This is because, for any data _y_ 1 _, . . . , yn_ , it is possible to choose _β_ 0 _, . . . , βn−_ 1 such that


for every _t_ = 1 _, . . . , n_ . To write _β_ 0 _, . . . , βn−_ 1 in terms of the observed data _y_ 1 _, . . . , yn_ , first plug in _t_ = 1 in (6) to get


Then plug _t_ = 2 in (6) to get _y_ 2 = _β_ 0 + _β_ 1 = _y_ 1 + _β_ 1 so that


Then plug _t_ = 3 in (6) to get _y_ 3 = _β_ 0 + 2 _β_ 1 + _β_ 2. Replacing _β_ 0 = _y_ 1 and _β_ 1 = _y_ 2 _− y_ 1, we obtain


Continuing this way plugging _t_ = 4 _,_ 5 _, . . . , n_ , we get


Therefore the least squares parameter estimates for the model (4) are given by:


for _j_ = 2 _, . . . , n −_ 1. This will lead to fitted values which coincide exactly with the observed data. Also the MLE of _σ_ will be zero. The unbiased estimate of _σ_ <u>(that</u> we previously used in linear regression) will not exist because it will equal ~~�~~ _RSS/_ ( _n − p_ ) with _p_ = _n_ .

To summarize, least squares in the model (4) will overfit the data, and will not produce any useful insight from the data.

To produce useful estimates in cases where the MLE overfits, one employs the idea of regularization. In the next lecture, we will discuss two ways of doing this: Ridge regularization and LASSO regularization. We will also understand regularization from the Bayesian perspective.

3

---

[← 1 Background](01-1-background.md) · [Up: contents](index.md)
