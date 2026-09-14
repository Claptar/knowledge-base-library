---
title: 7 Parameter Estimation in MA(1)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyThree153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7 Parameter Estimation in MA(1)

**Source:** [`LectureTwentyThree153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Estimating the parameters of ARMA (as well as ARIMA, SARIMA models) is much harder than parameter estimation in AR models which was handled by standard regression (ordinary least squares). We will not study this topic (and simply rely on the `ARIMA` function for fitting these models to data). But here, I will just illustrate the difficulties involved in the simplest case of an non-AR model: MA(1). Recall that the MA(1) model is given by


i.i.d where _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). The joint density of _y_ 1 _, . . . , yn_ is multivariate normal with mean vector _m_ := ( _µ, . . . , µ_ )<sup>_T_</sup> and covariance matrix Σ where Σ equals the _n × n_ matrix whose ( _i, j_ )<sup>_th_</sup> entry is given by


The likelihood is therefore

where _y_ is the _n ×_ 1 vector with components _y_ 1 _, . . . , yn_ . This is a function of the unknown parameters _µ, θ, σ_ which can be estimated by maximizing the logarithm of the likelihood. The presence of Σ<sup>_−_1</sup> makes this computationally expensive. Some (exact or approximate) formula should be used for Σ<sup>_−_1</sup> so that one does not need to invert an _n × n_ matrix every time the log-likelihood is to be computed.

An alternative approach is to try to write the likelihood (approximately) without using an explicit Σ<sup>_−_1</sup> . One way of doing this is to use the connection to AR models. The MA(1) model (2) _yt_ = _µ_ + _θ_ ( _B_ ) _ϵt_ (with _θ_ ( _B_ ) = 1+ _θB_ ) can be converted to an AR model as follows:


so that

This requires the assumption that _|θ| <_ 1. For this AR model, we can write the likelihood:


This formula involves _y_ 0 _, y−_ 1 _, y−_ 2 _, . . ._ for which we have no data. We can deal with them by simply setting them to be zero (you can think of writing the conditional likelihood of the data _y_ 1 _, . . . , yn_ given _y_ 0 _, y−_ 1 _, y−_ 2 _, . . ._ as zero). The likelihood then becomes:


5

where


The MLEs of _µ_ and _θ_ are obtained by minimizing _S_ ( _µ, θ_ ):


This is a nonlinear minimization that can be done via some optimization routines in Python (say in `scipy` ). The MLE for _σ_ is easily seen to be


For uncertainty quantification, we can take a Bayesian approach and combine the likelihood with a prior on _θ, µ, σ_ . Here is how this is done. **I did not cover the following in lecture, and this material is optional. It is included here just for completeness** .

We assume that _θ, µ, σ_ are independent with:


for a large _C →∞_ . Note that we have restricted the range of _θ_ to ( _−_ 1 _,_ 1) because we assumed that _|θ| <_ 1. The posterior is then


To obtain the posterior of _µ_ and _θ_ alone, we integrate the above with respect to _σ_ . Integrating from 0 to _∞_ (assuming _C_ is large so _e_<sup>_−C_</sup> _≈_ 0 and _e_<sup>_C_</sup> _≈∞_ ), we obtain (as in Lecture Three):


This posterior can be evaluated numerically over a grid of values of _µ_ and _θ_ and approximated by the appropriate discrete distribution over the grid. Alternatively, we can approximate this posterior by a suitable _t_ -distribution by doing a Taylor expansion of _S_ ( _µ, θ_ ) near the minimizer _µ,_ ˆ _θ_<sup>ˆ</sup> . To illustrate this, let _α_ = ( _µ, θ_ ) and _α_ ˆ = (ˆ _µ, θ_<sup>ˆ</sup> ). Taylor expansion for _α_ near _α_ ˆ gives


where we used _∇S_ (ˆ _α_ ) = 0 because _α_ ˆ minimizes _S_ ( _α_ ). Here _HS_ (ˆ _α_ ) denotes the Hessian of

6

_S_ at _α_ ˆ. Therefore


Comparing the above with the formula:


for the _p_ -variate _t_ -density _tk,p_ ( _µ,_ Σ), we see that (ignoring the indicator function _I{−_ 1 _< θ <_ 1 _, −C < µ < C}_ )


This _t_ -density can be used for uncertainty quantification of _µ_ and _θ_ .

---

[← 6 SARIMA Models](06-6-sarima-models.md) · [Up: contents](index.md) · [8 Additional Optional Reading →](08-8-additional-optional-reading.md)
