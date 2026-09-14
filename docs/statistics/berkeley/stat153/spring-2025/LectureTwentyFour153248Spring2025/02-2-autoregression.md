---
title: 2 AutoRegression
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyFour153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 AutoRegression

**Source:** [`LectureTwentyFour153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We also studied autoregression models where the covariates are simply lagged values of _yt_ . The simplest of these models is AR(1) where _xt_ = _yt−_ 1. This is simply (1) with _t_ replaced by _xt_ = _yt−_ 1:


One can create a nonlinear version of AR(1) by simply using (3) with _xt_ = _yt−_ 1. We shall refer to this as Nonlinear AutoRegression of order 1: NAR(1) (there are many nonlinear autoregression models and this one is only one of them):


Now let us consider the case of AR( _p_ ) for _p ≥_ 1. The usual AR( _p_ ) model is simply:


Observe that (5) can be written in compressed form as simply _yt_ = _β_ 0 + _β_ 1 _yt−_ 1 + _· · ·_ + _βpyt−p_ + _ϵt_ which is the usual form of AR( _p_ ).

What is a natural nonlinear version of (5)? Put another way, what is a good extension of (4) for _p ≥_ 1? There are multiple ways of obtaining these versions. Looking at the structure of (4), clearly _xt_ = _yt−_ 1 will be replaced by _xt_ = ( _yt−_ 1 _, . . . , yt−p_ )<sup>_T_</sup> . The next line gives the formula for _st_ . This would need to be changed because _xt_ is no longer a scalar. One way to do this would be to write one version of the formula for _st_ in (4) for each component of _xt_ . This would result in:


2

Here _xt_ 1 = _yt−_ 1 _, . . . , xtp_ = _yt−p_ denote the components of _xt_ . With this choice of _st_ , note that _µt_ becomes


In other words, we are fitting an **additive** model for _yt_ in terms of the covariates _xt_ 1 = _yt−_ 1 _, . . . , xtp_ = _yt−p_ . Additive models are popular in regression but they do not incorporate any interactions between the covariates. For example, if the true model generating the data is _yt_ = 0 _._ 5 _yt−_ 1 _yt−_ 2 + _ϵt_ , the additive model is unlikely to work well (because ( _x_ 1 _, x_ 2) _�→_ 0 _._ 5 _x_ 1 _x_ 2 is not an additive function of _x_ 1 and _x_ 2).

Instead of using the additive model in (6), we shall use the following model as NAR( _p_ ) (Nonlinear AutoRegression of order _p_ ). This is obtained by changing the second line of (6) to be an arbitrary linear function of _xt_ :


Here _W_ is a _k × p_ matrix and _b_ is a _k ×_ 1 vector. The parameters in this model are the entries of the matrix _W_ , the vector _b_ , the coefficients _β_ 0 and the components of _β_ and finally the noise standard deviation _σ_ .

In neural network terminology, the model (7) is called a **single-hidden layer neural network** because it first applies a linear transformation to the input _xt_ (via _st_ = _Wxt_ + _b_ ), then passes the result through the nonlinear activation function _σ_ to get _rt_ , which forms the hidden layer. The output _µt_ is then computed as a linear function of _rt_ (via _µt_ = _β_ 0 + _β_<sup>_T_</sup> _rt_ ) and noise _ϵt_ is added to explain the discrepancy between _yt_ and _µt_ . The presence of one nonlinear transformation between the input _xt_ and the output _µt_ , combined with otherwise linear operations, is exactly the structure of a single-hidden layer neural network.

To sum up, we take the single-hidden layer neural network model (7) to be our nonlinear generalization of AR( _p_ ).

Note that (7) can also be treated as a linear regression model but the linearity is in terms of the feature vector _rt_ (not in terms of the original covariate _xt_ ). We shall refer to _rt_ as the feature vector at time _t_ , it is also common to refer to it as the hidden layer output at time _t_ .

---

[← 1 Regression with t as covariate](01-1-regression-with-t-as-covariate.md) · [Up: contents](index.md) · [3 Recurrent Neural Networks (RNNs) →](03-3-recurrent-neural-networks-rnns.md)
