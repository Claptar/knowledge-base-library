---
title: 1 Time Series Models and Stationarity
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNineteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureNineteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Time Series Models and Stationarity

**Source:** [`LectureNineteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNineteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We have already seen many models for observed time series data _y_ 1 _, . . . , yn_ . These models describe the distribution of _y_ 1 _, . . . , yn_ in terms of various parameters. Even though, the observed data only corresponds to times _t_ = 1 _, . . . , n_ , it makes sense for the model to describe the distribution of _yt_ for all _t_ past and present i.e., _t_ = _. . . , −_ 3 _, −_ 2 _, −_ 1 _,_ 0 _,_ 1 _,_ 2 _,_ 3 _, . . ._ . This is because one may be interested in predicting the values of _yt_ for unobserved times.

All the models we will study have error terms _ϵt_ that we assume are i.i.d Gaussian _N_ (0 _, σ_<sup>2</sup> ). For all models that we have so far studied, the i.i.d Gaussian errors assumption ensures that the whole time series _{yt}_ is jointly Gaussian (this will not be true for the neural network models that we will consider later). Gaussianity ensures that the behavior of the time series model is characterized by means (expectations) and covariances.

Some time series models satisfy the property of **stationarity** which is defined as follows:

**Definition 1.1** (Stationarity) **.** _A time series model for yt, t_ = _. . . , −_ 3 _, −_ 2 _, −_ 1 _,_ 0 _,_ 1 _,_ 2 _,_ 3 _, . . . is said to be stationary if both the following conditions hold:_

_1. The mean of yt (denoted by_ E _yt) is the same for all times t_

_2. The variance of yt (denoted by var_ ( _yt_ ) _) is the same for all times t_

_3. The covariance between yt_ 1 _and yt_ 2 _only depends on the distance |t_ 1 _− t_ 2 _| between t_ 1 _and t_ 2 _._

1

Stationarity implies, for example, that the mean of _y−_ 2000 should be the same as _y_ 9999. Also the covariance between _y−_ 2000 and _y−_ 2100 should be the same as the covariance between _y_ 9899 and _y_ 9999 etc.

For a stationary time series model _{yt}_ , the covariance between _yt_ and _yt_ + _h_ will only depend on _|h|_ . We denote:


_γ_ ( _h_ ) is called the AutoCovariance Function (ACVF) of the stationary time series model _{yt}_ . Observe that

_γ_ (0) = cov( _yt, yt_ ) = var( _yt_ ) & _γ_ ( _−h_ ) = cov( _yt, yt−h_ ) = cov( _yt−h, yt_ ) = cov( _yt−h, yt−h_ + _h_ ) = _γ_ ( _h_ )

So _γ_ ( _h_ ) is a symmetric function of _h_ , and we only need to evaluate it at nonnegative _h_ .

The AutoCorrelation Function (ACF) of a stationary time series model _{yt}_ is defined as:


Note that _ρ_ (0) = 1 and _ρ_ ( _h_ ) = _ρ_ ( _−h_ ).

It is important to remember the following points:

1. Stationarity refers to a time series model (not to actual data)

2. Not all time series models are stationary. In fact, there are many time series models that are not stationary.

3. ACVF and ACF are only defined for stationary time series models.

Let us now look at some examples of time series models, starting with the simplest.

**Example 1.2** (Gaussian White Noise) **.** _The simplest time series model is yt_ = _ϵt where i.i.d ϵt ∼ N_ (0 _, σ_<sup>2</sup> ) _. This is known as the Gaussian white noise model. It is easy to check that_ E _yt_ = 0 _and cov_ ( _yt, yt_ + _h_ ) = _σ_<sup>2</sup> _I{h_ = 0 _}. So the conditions of stationarity are satisfied, and the Gaussian white noise is a stationary model. Its ACF is ρ_ ( _h_ ) = _I{h_ = 0 _}._

**Example 1.3** (Constant mean plus White Noise) **.** _The next simplest time series model is i.i.d yt_ = _µ_ + _ϵt where, again, ϵt ∼ N_ (0 _, σ_<sup>2</sup> ) _. This is also a stationary time model because_ E _yt_ = _µ and cov_ ( _yt, yt_ + _h_ ) = _σ_<sup>2</sup> _I{h_ = 0 _}. Its ACF is ρ_ ( _h_ ) = _I{h_ = 0 _}._

The next two examples are for non-stationary time series models.

**Example 1.4.** _yt_ = _β_ 0 + _β_ 1 _t_ + _ϵt. Here the mean of yt is:_


_and covariances are:_


_So the mean changes with t, variance is constant and there is no correlation between different time points. Because the mean changes with t, this is a non-stationary model._

2

**Example 1.5.** _yt_ = _β_ 0 + _β_ 1 cos(2 _πft_ ) + _β_ 2 sin(2 _πft_ ) + _ϵt The means are given by:_


_and covariances are:_


_Again the mean changes with t, variance is constant and there is no correlation between different time points. Because the mean changes with t, this is non-stationary._

The next example is the spectrum model.

**Example 1.6.** _Consider the Spectrum model:_


_with β_ 11 _, β_ 21 _, β_ 12 _, β_ 22 _, . . . , β_ 1 _m, β_ 2 _m all independent with_


_Here m is the largest positive integer that is strictly smaller than n/_ 2 _._

_For this model,_ E _yt_ = _β_ 0 _so that the mean is constant over time (unlike the previous two models). The covariance is given by_

_cov_ ( _yt_ 1 _, yt_ 2)


_This model incorporates dependence between yt at different time points t (unlike the previous two models). Further, the covariance between yt_ 1 _and yt_ 2 _only depends on the distance |t_ 1 _−t_ 2 _| between the two time points._

_A slightly inelegant thing about this model is that the specification_ (1) _depends on the sample size n. One can make the frequencies to take values in the continuum_ (0 _,_ 1 _/_ 2) _and replace the sum_<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_byanintegral.ThiscanbedoneforexampleasinShumwayand_</sup> _Stoffer [1, Theorem C.2]._

Our next example is AR models. Are AR models stationary? The answer is a bit complicated. Let us start with AR(1) and then consider AR( _p_ ) for _p ≥_ 2 in the next lecture.

3

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Stationarity of AR(1) →](03-2-stationarity-of-ar-1.md)
