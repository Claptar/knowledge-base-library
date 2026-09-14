---
title: 1 AutoRegressive Models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeventeen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureSeventeen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 AutoRegressive Models

**Source:** [`LectureSeventeen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeventeen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last lecture, we started discussing AutoRegressive models as a first step towards learning the more general ARIMA models. Methodologically, AutoRegression is simply regression of the observed time series on lagged versions of itself. Suppose the observed dataset is _y_ 1 _, . . . , yn_ . From this data, we create a ( _n − p_ ) _×_ 1 vector _Y_ and a ( _n − p_ ) _×_ ( _p_ + 1) design matrix _X_ as follows:


_p_ here is an integer which represents the order of the AutoRegressive (AR) model. We then regress _Y_ on _X_ (in the standard way using least squares or OLS) to obtain fitted regression coefficients _φ_ 0 _, φ_ 1 _, . . . , φp_ . Since the response variable is _yt_ and the regressors are 1 _, yt−_ 1 _, . . . , yt−p_ for _t_ = _p_ + 1 _, . . . , n_ , the fitted regression model can be written as

_yt_ = _φ_<sup>ˆ</sup> 0 + _φ_<sup>ˆ</sup> 1 _yt−_ 1 + _· · ·_ + _φ_<sup>ˆ</sup> _pyt−p._ (1)

This is how data is typically analyzed in AutoRegression. In the next section, we shall write down the structure of the AR **model** and we shall see how the above estimation procedure is related to Maximum Likelihood.

One of the main uses of AR (and more generally ARIMA) models is for prediction (also known as forecasting).

For predicting _yn_ +1, we plug _t_ = _n_ + 1 in (1) to get


Note that _yn, yn−_ 1 _, . . . , yn_ +1 _−p_ are all observed and they are the last _p_ observations. For predicting _yn_ +2, we plug _t_ = _n_ + 2 in (1) to get


1

In the above, _yn_ +1 is not observed. But we can replace it by the predicted value _y_ ˆ _n_ +1. This gives


More generally, we predict _yn_ + _i_ by the recursion


where the recursion is initialized with


When this method is applied on some time series datasets, the predictions obtained can vary quite significantly with _p_ . We will try to obtain some intuition for the structure of the predictions later in this lecture.

---

[Up: contents](index.md) · [2 The AR Model →](02-2-the-ar-model.md)
