---
title: '1 AR models: estimation, inference and prediction'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEighteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEighteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 AR models: estimation, inference and prediction

**Source:** [`LectureEighteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEighteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The AR(p) model is given by:


The unknown parameters are _ϕ_ 0 _, ϕ_ 1 _, . . . , ϕp_ as well as _σ_ ( _σ_ is the standard deviation of _ϵt_ ). These need to be estimated from the observed data _y_ 1 _, . . . , yn_ .

The likelihood is (below _θ_ denotes the vector consisting of all the parameters _ϕ_ 0 _, . . . , ϕp_ and _σ_ ):


The first term on the right hand side above _fyp_ +1 _,...,yn|y_ 1 _,...,yp,θ_ ( _yp_ +1 _, . . . , yn_ ) is the conditional likelihood of _yp_ +1 _, . . . , yn_ given _y_ 1 _, . . . , yp_ . This conditional likelihood is calculated as


In order to proceed further, we shall make the following assumption:


which can be ensured by assuming that _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ) **and that** _ϵt_ **is independent of** _y_ 1 _, . . . , yt−_ 1. With (2), we get


1

Observe that, in order to write the above formula, we only used the model equation (1) for _t_ = _p_ + 1 _, . . . , n_ .

The conditional joint density _fyp_ +1 _,...,yn|y_ 1 _,...,yp,θ_ ( _yp_ +1 _, . . . , yn_ ) is called the **conditional likelihood** of the AR( _p_ ) model. The full likelihood is


If we assume that _fy_ 1 _,...,yp|θ_ ( _y_ 1 _, . . . , yp_ ) does not depend on _θ_ , then maximizing the full likelihood is equivalent to maximizing the conditional likelihood.

If we want to derive _fy_ 1 _,...,yp|θ_ ( _y_ 1 _, . . . , yp_ ) in a more principled way, then we have to use the model equation (1) for smaller values of _t_ (i.e., _t_ = _p, p −_ 1 _, p −_ 2 _, . . . ,_ 0 _, −_ 1 _, . . ._ ). This makes the analysis complicated and is not really worth it. It also only works under some “stationarity” assumptions on _ϕ_ 0 _, . . . , ϕp_ . It is much simpler working with the conditional likelihood.

Using the matrix notation:


the conditional likelihood (which is also proportional to the full likelihood under the assumption that _fy_ 1 _,...,yp|θ_ ( _y_ 1 _, . . . , yp_ ) does not depend on _θ_ ) becomes:


This likelihood is the same as the likelihood in linear regression with _n − p_ observations. We can therefore infer the parameters _ϕ_ 0 _, . . . , ϕp_ and _σ_ as in usual linear regression with the prior:


This will allow us to write down the joint posterior of ( _β, σ_ ). Integrating over _σ_ leads to the posterior of _β_ alone. As in Lecture 4, this leads to


where


Note that the degrees of freedom of the _t_ -distribution above is _n −_ 2 _p −_ 1 as the number of observations equals _n − p_ and the number of components of _β_ is _p_ + 1. If inference for _σ_ is desired, one can use:


2

Note that Bayesian inference for AR models is identical to Bayesian inference for linear regression models because the likelihood (3) is the same as in the usual linear model (with _n − p_ observations). Bayesian inference only cares about the likelihood.

Frequentist inference for the AR( _p_ ) model is based on the MLE which is given by _β_<sup>ˆ</sup> and


To obtain frequentist confidence intervals for the parameters _ϕi_ , one needs to find the distribution of _β_<sup>ˆ</sup> . Here the analysis is quite different from that used in linear regression (see, for example, Section 3.5 of the book by Shumway and Stoffer titled _Time Series Analysis and its applications_ (Fourth Edition)). The results turn out to be quite close to those obtained by the Bayesian method.

Unlike Bayesian inference, frequentist inference for the AR model is not identical to frequentist inference for the usual linear regression model. For example, one does not use _t_ -distributions for inferring the _ϕ_ parameters in AR( _p_ ) models. Instead, one uses normal distributions (e.g., _z_ -scores as opposed to _t_ -scores) which are justified by asymptotic arguments that are different from and more complicated than those used for linear regression.

On the computer, estimation and inference for AR models can be done in two ways:

1. Just create _y_ and _X_ as above, and use OLS in statsmodels.

2. Use the AutoReg function in statsmodels.

Both methods give the same estimates of _ϕ_ 0 _, . . . , ϕp_ . The estimate of _σ_ is slightly different: OLS gives _σ_ ˆ _OLS_ := ~~�~~ _RSS/_ ( _n −_ 2 _p −_ 1) and AutoReg gives _σ_ ˆ _MLE_ := ~~�~~ _RSS/_ ( _n − p_ ). The two methods also give slightly different standard errors corresponding to the coefficient estimates. OLS gives square roots of the diagonal entries of _σ_ ˆ _OLS_<sup>2(</sup><sup>_XT X_)</sup><sup>_−_1whileAutoReg</sup> considers _σ_ ˆ _MLE_<sup>2(</sup><sup>_XT X_)</sup><sup>_−_1.FinallyOLSdoescoefficientinferenceusingthe</sup><sup>_t_-distribution</sup> (with _n −_ 2 _p −_ 1 degrees of freedom) while AutoReg recommends inference using the normal distribution.

---

[Up: contents](index.md) · [2 Predictions from AR ( p ) models →](02-2-predictions-from-ar-p-models.md)
