---
title: 1 Nonlinear AutoRegression
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFive153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyFive153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Nonlinear AutoRegression

**Source:** [`LectureTwentyFive153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFive153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last lecture, we started discussing nonlinear forms of autoregression for an observed time series _y_ 1 _, . . . , yn_ . For each _t_ , we take _xt_ = ( _yt−_ 1 _, . . . , yt−p_ )<sup>_T_</sup> for some integer _p ≥_ 1. _xt_ can be called the covariate at time _t_ corresponding to the response value _yt_ . In the context of recurrent neural network models, _xt_ is referred to as the input at time _t_ .

The usual (linear) autoregression AR( _p_ ) model corresponds to:


The loss function is<sup>�</sup> _t_<sup>(</sup><sup>_yt −µt_)2,andtheparameters</sup><sup>_β_0</sup><sup>_, β_areestimatedbyminimizingthe</sup> loss.

In nonlinear autoregression, we change the formula (1) into a nonlinear function of _xt_ . When _p_ = 1, one simple nonlinear AR(1) model is:


We simplify this slightly by dropping _xt_ (because _xt_ = ( _xt − c_ 0)+ + _c_ 0 for all _t_ provided _c_ 0 is smaller than all the observed values of _xt_ ; we will not lose anything by dropping _xt_ ). This leads to


We rewrite this equation using the following notation:


_st_ is a linear function of _xt_ which maps the scalar _xt_ to the _k ×_ 1 vector _st_ . _σ_ ( _·_ ) denotes the ReLU function applied pointwise to the input. So _rt_ is obtained by apply the ReLU function to each coordinate of _st_ . Finally _µt_ is a linear function of _rt_ (we shall sometimes refer to _µt_ as the output corresponding to the input _xt_ ).

1

When _p ≥_ 1, there are multiple ways of generalizing (2). One simple way is to consider the following “additive” model (below _x_<sup>(</sup> _t_<sup>_i_)</sup> = _yt−i_ denotes the _i_<sup>_th_</sup> coordinate of _xt_ )


This is called an additive model because _µt_ can be written as an additive sum of separate functions of _x_<sup>(</sup> _t_<sup>_i_)</sup> for _i_ = 1 _, . . . , p_ . A different (i.e., non-additive) generalization of (2) is the single-hidden layer neural network defined as follows.


Here _st_ is again _k ×_ 1, _W_ is _k × p_ and _b_ is _p ×_ 1. We shall refer to (4) as the NonLinear AR model of order _p_ . The total number of parameters here is _kp_ + _k_ + _k_ + 1 = _kp_ + 2 _k_ + 1. When _p_ increases by 1, the number of parameters in (4) increases by _k_ . On the other hand, in the usual (linear), AR( _p_ ) model, the number of parameters increases only by 1 when _p_ increases by 1. So these models have a tendency to become high-dimensional faster than the linear AR( _p_ ) models.

---

[Up: contents](index.md) · [2 Recurrent Neural Network (RNN) →](02-2-recurrent-neural-network-rnn.md)
