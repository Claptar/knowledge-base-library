---
title: 3 Recurrent Neural Networks (RNNs)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyFour153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Recurrent Neural Networks (RNNs)

**Source:** [`LectureTwentyFour153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We are now ready to define an RNN. RNN will involve one modification of the second equation in (7). Specifically, we will take _st_ to be a linear function not only of _xt_ but also of the feature vector _rt−_ 1 at the previous time. This leads to (the difference relative to (7)

3

is highlighted in blue below)


In Model (7), the hidden layer output _rt_ is computed purely from the current input _xt_ through a linear transformation ( _st_ ) and the nonlinearity _σ_ ( _·_ ), so _rt_ depends only on _xt_ . In the RNN (8) however, the computation of _rt_ involves not just the current _xt_ but also the previous hidden layer output _rt−_ 1 through an additional linear term _Wrrt−_ 1. This means that in the second model, the feature vector _rt_ is influenced both by the current input and by the feature vector from the previous step, whereas in the first model, it is influenced only by the current input.

Model (7) is a standard single-hidden layer feedforward neural network where the hidden layer _rt_ depends only on the current input. In contrast, the second model RNN (8) introduces a **recurrent** connection by adding a term _Wrrt−_ 1 to the hidden layer input, meaning that _rt_ now depends not only on the current input _xt_ but also on the previous hidden state _rt−_ 1. This recurrence creates a form of memory across time steps, making the second model a recurrent neural network (RNN), while the first model has no memory and treats each input independently.

The matrix _Wr_ is _k ×k_ so it is a square matrix. The parameters now include _Wr, W, b, β_ 0 _, β_ (along with the noise standard deviation _σ_ ). Typically _k_ will be larger than _p_ . Model (8) also requires an initialization of _rt_ usually done by _r_ 0 = 0.

In the model (7), the feature vector _rt_ depends only on _xt_ . On the other hand, in (8), _rt_ depends on all the inputs: _xt, xt−_ 1 _, . . . , x_ 1 (or _xt, xt−_ 1 _, . . . , xp_ +1 in case _xt_ = ( _yt−_ 1 _, . . . , yt−p_ )<sup>_T_</sup> is not defined for _t ≤ p_ ; below we assume that the inputs _xt_ are defined for all _t_ = 1 _,_ 2 _, . . ._ without loss of generality; in a time series setting, this can be arranged by rearranging the time index). To see how _rt_ depends on _xt, xt−_ 1 _, . . ._ , note that


From the above, _rt_ clearly depends on all of _x_ 1 _, . . . , xt_ . But the strength of the dependence of _rt_ on _xs_ varies with _s_ .

RNNs can have stability issues because the formula for _rt_ involves the product of a possibly large number of terms where the matrix _Wr_ appears multiple times (e.g., see the formula (9) for _r_ 4 above). Imagining _Wr_ to be a scalar (just for the sake of making this argument), then two things can happen: it can be strictly larger than 1 in magnitude or strictly smaller than 1 in magnitude (it cannot be exactly equal to 1 in magnitude because these parameters are learning by a training algorithm and it is unlikely that this algorithm will output an estimate of _Wr_ that is exactly equal to 1 in magnitude). If _Wr_ is strictly larger than 1 in magnitude, then multiple appearances of _Wr_ in products will blow them up, causing _rt_ to explode for moderate and large _t_ . On the other hand, if _Wr_ is strictly smaller than 1 in magnitude, then

4

the products will be very small, and this leads to _rt_ depending mainly on _xs_ for which _s_ is close to _t_ (the implication is that RNNs cannot capture long-range dependence). When _Wr_ is a matrix (instead of a scalar), this argument will still hold but, instead of magnitude, we need to use the spectral radius of _Wr_ (spectral radius of a square matrix is defined as the largest magnitude of any eigenvalue).

The nonlinear activation function _σ_ ( _·_ ) also appears multiple times in the formula for _rt_ , (see again the formula (9) for _r_ 4). To solve stability problems, it is customary in RNNs to take _σ_ to be the hyperbolic tangent function (instead of ReLU). The hyperbolic tangent function is given by


Unlike the ReLU function (which can take arbitrarily large positive values), the hyperbolic tangent activation function always takes values between _−_ 1 and 1. This helps the RNN be more stable.

We will discuss the RNNs more next week (along with related models such as GRU and LSTM).

---

[← 2 AutoRegression](02-2-autoregression.md) · [Up: contents](index.md) · [4 Parameter Estimation via PyTorch →](04-4-parameter-estimation-via-pytorch.md)
