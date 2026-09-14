---
title: 1 Time Series Models, and Stationarity
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwenty153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwenty153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Time Series Models, and Stationarity

**Source:** [`LectureTwenty153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwenty153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A time series model describes the distribution of random variables _yt_ for all _t_ past and present i.e., _t_ = _. . . , −_ 3 _, −_ 2 _, −_ 1 _,_ 0 _,_ 1 _,_ 2 _,_ 3 _, . . ._ , in terms of certain unknown parameters. We refer to this collection of random variables as doubly infinite because _t_ extends to infinity in both directions.

All the time series models that we shall study in this course will be jointly Gaussian (i.e., the joint distribution of ( _yt_ 1 _, . . . , ytk_ ) will be multivariate Gaussian for every _k_ and _t_ 1 _, . . . , tk_ ). Gaussianity ensures that the behavior of the time series model is characterized by means (expectations) and covariances.

Some time series satisfy the property of stationarity which is defined as follows:

**Definition 1.1** (Stationarity) **.** _A doubly infinite sequence of random variables yt is said to be stationary if both the following conditions hold:_

_1. The mean of yt (denoted by_ E _yt) is the same for all times t_

_2. The variance of yt (denoted by var_ ( _yt_ ) _) is the same for all times t_

_3. The covariance between yt_ 1 _and yt_ 2 _only depends on the distance |t_ 1 _− t_ 2 _| between t_ 1 _and t_ 2 _._

Stationarity implies, for example, that the mean of _y−_ 2000 should be the same as _y_ 9999. Also the covariance between _y−_ 2000 and _y−_ 2100 should be the same as the covariance between _y_ 9899 and _y_ 9999 etc.

For a stationary time series model _{yt}_ , the covariance between _yt_ and _yt_ + _h_ will only depend on _|h|_ . We denote:

_γ_ ( _h_ ) = cov( _yt, yt_ + _h_ ) for _h_ = _. . . , −_ 2 _, −_ 1 _,_ 0 _,_ 1 _,_ 2 _, . . . ._

_γ_ ( _h_ ) is called the AutoCovariance Function (ACVF) of the stationary time series model _{yt}_ . Observe that

_γ_ (0) = cov( _yt, yt_ ) = var( _yt_ ) & _γ_ ( _−h_ ) = cov( _yt, yt−h_ ) = cov( _yt−h, yt_ ) = cov( _yt−h, yt−h_ + _h_ ) = _γ_ ( _h_ )

So _γ_ ( _h_ ) is a symmetric function of _h_ , and we only need to evaluate it at nonnegative _h_ .

1

The AutoCorrelation Function (ACF) of a stationary time series model _{yt}_ is defined as:


Note that _ρ_ (0) = 1 and _ρ_ ( _h_ ) = _ρ_ ( _−h_ ).

It is important to remember the following two points:

1. Stationarity refers to a time series model (not to actual data)

2. Not all time series models are stationary. In fact, there are many time series models that are not stationary.

3. ACVF and ACF are only defined for stationary time series models.

Let us now look at some examples of time series models, starting with the simplest.

_i.i.d_ **Example 1.2** (White Noise) **.** _The simplest time series model is yt_ = _ϵt where ϵt ∼ N_ (0 _, σ_<sup>2</sup> ) _. This is known as the Gaussian white noise model. It is easy to check that_ E _yt_ = 0 _and cov_ ( _yt, yt_ + _h_ ) = _σ_<sup>2</sup> _I{h_ = 0 _}. So the conditions of stationarity are satisfied, and the Gaussian white noise is a stationary model. Its ACF is ρ_ ( _h_ ) = _I{h_ = 0 _}._

**Example 1.3** (Constant mean plus White Noise) **.** _The next simplest time series model is i.i.d yt_ = _µ_ + _ϵt where, again, ϵt ∼ N_ (0 _, σ_<sup>2</sup> ) _. This is also a stationary time model because_ E _yt_ = _µ and cov_ ( _yt, yt_ + _h_ ) = _σ_<sup>2</sup> _I{h_ = 0 _}. Its ACF is ρ_ ( _h_ ) = _I{h_ = 0 _}._

The next two examples are for non-stationary time series models.

**Example 1.4.** _yt_ = _β_ 0 + _β_ 1 _t_ + _ϵt. Here the mean of yt is:_


_and covariances are:_


_So the mean changes with t, variance is constant and there is no correlation between different time points. Because the mean changes with t, this is a non-stationary model._

**Example 1.5.** _yt_ = _β_ 0 + _β_ 1 cos(2 _πft_ ) + _β_ 2 sin(2 _πft_ ) + _ϵt The means are given by:_


_and covariances are:_


_Again the mean changes with t, variance is constant and there is no correlation between different time points. Because the mean changes with t, this is non-stationary._

2

---

[Up: contents](index.md) · [2 Moving Average (MA) Models →](02-2-moving-average-ma-models.md)
