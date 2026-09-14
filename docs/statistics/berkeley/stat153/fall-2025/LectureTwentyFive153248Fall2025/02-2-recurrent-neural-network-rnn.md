---
title: 2 Recurrent Neural Network (RNN)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyFive153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyFive153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Recurrent Neural Network (RNN)

**Source:** [`LectureTwentyFive153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyFive153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

RNN will involve one modification of the first equation in (4). Specifically, in an RNN, we will take _st_ to be a linear function not only of _xt_ but also of the feature vector _rt−_ 1 at the previous time. This leads to the following set of equations defining the RNN:


This formula can also be written as


In Model (4), the hidden layer output _rt_ is computed purely from the current input _xt_ through a linear transformation ( _st_ ) and the nonlinearity _σ_ ( _·_ ), so _rt_ depends only on _xt_ . In

2

the RNN (5) however, the computation of _rt_ involves not just the current _xt_ but also the previous hidden layer output _rt−_ 1 through an additional linear term _Wrrt−_ 1. This means that in the second model, the feature vector _rt_ is influenced both by the current input and by the feature vector from the previous step, whereas in the first model, it is influenced only by the current input.

Model (4) is a standard single-hidden layer feedforward neural network where the hidden layer _rt_ depends only on the current input. In contrast, the second model RNN (5) introduces a **recurrent** connection by adding a term _Wrrt−_ 1 to the hidden layer input, meaning that _rt_ now depends not only on the current input _xt_ but also on the previous hidden state _rt−_ 1. This recurrence creates a form of memory across time steps, making the second model a recurrent neural network (RNN), while the first model has no memory and treats each input independently.

The matrix _Wr_ is _k × k_ so it is a square matrix. The parameters in the RNN are _Wr, W, b, β_ 0 _, β_ . Typically _k_ will be larger than _p_ . Model (5) also requires an initialization of _rt_ usually done by _r_ 0 = 0.

In the model (4), the feature vector _rt_ depends only on _xt_ . On the other hand, in (5), _rt_ depends on all the inputs: _xt, xt−_ 1 _, . . . , x_ 1 (or _xt, xt−_ 1 _, . . . , xp_ +1 in case _xt_ = ( _yt−_ 1 _, . . . , yt−p_ )<sup>_T_</sup> is not defined for _t ≤ p_ ; below we assume that the inputs _xt_ are defined for all _t_ = 1 _,_ 2 _, . . ._ without loss of generality; in a time series setting, this can be arranged by rearranging the time index). To see how _rt_ depends on _xt, xt−_ 1 _, . . ._ , note that


From the above, _rt_ clearly depends on all of _x_ 1 _, . . . , xt_ . But the strength of the dependence of _rt_ on _xs_ varies with _s_ .

From the above (e.g., see the formula (7) for _r_ 4), it is clear that the formula for _rt_ will involve products of a large number of terms where the matrix _Wr_ appears multiple times. This can lead to stability problems when _Wr_ is large. For example, imagine that _Wr_ is a scalar which is strictly larger than 1 in magnitude, then multiple appearances of _Wr_ in products will blow them up, causing _rt_ to explode for moderate and large _t_ . When _Wr_ is a matrix, this will happen when the spectral radius of _Wr_ (defined as the largest modulus of any eigenvalue of _Wr_ ) is strictly larger than one. This is a regime which needs to be avoided to prevent instability.

The nonlinear activation function _σ_ ( _·_ ) also appears multiple times in the formula for _rt_ , (see again the formula (7) for _r_ 4). For better stability, it is customary in RNNs to take _σ_ to be the hyperbolic tangent function (instead of ReLU). The hyperbolic tangent function is given by


Unlike the ReLU function (which can take arbitrarily large positive values), the hyperbolic tangent activation function always takes values between _−_ 1 and 1. This helps the RNN be more stable.

3

So the RNN is given by:


or


Here the activation function _σ_ tanh is the tanh activation function given by


The only difference between (8) and (5) (and also (9) and (6)) is the tanh activation function.

Use of the tanh activation, as well as requiring that _Wr_ does not have spectral radius strictly larger than 1 makes the RNN stable. However, if _Wr_ has spectral radius strictly smaller than 1 (note that we can ignore the case where the spectral radius is exactly equal to one, because _Wr_ and other parameters of the RNN are learned by a training algorithm and it is unlikely that this algorithm will output an estimate of _Wr_ with spectral radius exactly equal to 1), then the RNN has the problem of “lack of long memory”. This means that _rt_ effectively depends only on those inputs _xu_ which are somewhat close to _t_ . To see this, let us calculate the derivative of _rt_ with respect to _xu_ for _u ≤ t_ . The formula is given by:


Here _∂x∂rut_<sup>denotesthe</sup><sup>_k× p_JacobianMatrixofderivativesof</sup><sup>_rt_withrespectto</sup><sup>_xu_.On</sup> the right hand side in (10), _σ_<sup>_′_</sup> ( _st_ ) should be interpreted as _k × k_ diagonal matrices whose diagonal entries are obtained by applying the _σ_<sup>_′_</sup> ( _u_ ) = _dud_<sup>_σ_(</sup><sup>_u_)functiontoeachelementof</sup><sup>_st_</sup> ( _σ_<sup>_′_</sup> ( _st−_ 1) _, . . ._ are similarly defined as _k × k_ diagonal matrices). This diagonal interpretation of _σ_<sup>_′_</sup> ( _u_ ) aligns with the Jacobian of the pointwise interpretation of _σ_ ( _u_ ) when _u_ is a vector.

As a concrete example,


Note that these gradient formulae are with respect to inputs _xu_ , and not with respect to the parameters (which is crucial to parameter estimation). In the formula (10), it is clear that when _u_ is much smaller than _t_ , many more terms appear in the right hand side of (10) compared to the case when _u_ is closer to _t_ . Note here that _σ_ is the tanh activation function:


Thus each _σ_<sup>_′_</sup> ( _·_ ) term will add a fractional multiplier to _∂rt/∂xu_ . The number of these fractional multipliers will increase as _u_ decreases in (10).

4

Further the matrix _Wr_ also plays a key role in (10). For the model equation in (8) to be stable, _Wr_ needs to have spectral radius (defined as the largest modulus of any eigenvalue) to be strictly smaller than one. In that case, each additional _Wr_ multiplier will bring the whole term down, leading to _∂rt/∂xu_ being small when _u_ is much smaller than _t_ .

This points to the following shortcoming of RNNs that more sophisticated models such as GRUs and LSTMs attempt to fix. We want _rt_ to represent the ideal summary of _x_ 1 _, . . . , xt_ that is relevant for the output _yt_ . However, in an RNN, _rt_ effectively only depends on those inputs _xu_ which are somewhat close to _t_ . In this sense, the RNN can be thought of as not having a very long memory.

This “lack of long memory” problem with RNNs can be fixed by use of GRUs and LSTMs.

---

[← 1 Nonlinear AutoRegression](01-1-nonlinear-autoregression.md) · [Up: contents](index.md) · [3 GRU (Gated Recurrent Unit) →](03-3-gru-gated-recurrent-unit.md)
