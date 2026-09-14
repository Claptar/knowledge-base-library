---
title: ARIMA Example Two
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureOneSlides153248Fall2025PDF.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureOneSlides153248Fall2025PDF.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# ARIMA Example Two

**Source:** [`LectureOneSlides153248Fall2025PDF.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureOneSlides153248Fall2025PDF.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

FRED data on monthly retail sales (in millions of dollars) for beer, wine and liquor stores (typo on axis label: should be month not year)


###### Below we plot the data along with predictions by two different ARIMA models


##### **Topic Six: Recurrent Neural Networks**

- <sup>AR models are simply linear regression of  on</sup> _yt_

- lagged covariates _xt_ := (1, _yt_ −1, …, _yt_ − _p_ )

- •<sup>It is natural to use nonlinear regression of  on</sup> _yt_

- for improved predictive power

- _xt_

- We perform this nonlinear regression using single hidden-layer neural networks

• These is Nonlinear AutoRegression which fits functions _yt_ = _f_ ( _xt_ ) = _f_ ( _yt_ −1, …, _yt_ − _p_ )

##### **Topic Six: Recurrent Neural Networks**

- A drawback of these models is that we have to select the value of  appropriately _p_

- <sup>Even if  is chosen well, the dependence of</sup> _p yt_ on its past values abruptly cuts off at _p_

- • RNNs are a way of fitting functions which use all the past values: _yt_ = _ft_ ( _xt_ , _xt_ −1, …, _x_ 1)

- • We shall study vanilla RNNs and more fancy variants such as LSTMs and GRUs


Here is a simulated data generated as: for _p_ = 344 _yt_ = _yt_ − _p_ + _ϵt_


Here are the forecasts by the AR model with the correct : _p_

Here are the forecasts by an LSTM (which does not use knowledge of the true ): _p_


• Topic 1: Multiple Linear Regression • Topic 2: Nonlinear Regression • Topic 3: High-dimensional Regression • Topic 4: Variance Models and Spectral Analysis

- Topic 5: ARIMA modeling

• Topic 6: Recurrent Neural Networks

• We will work with a variety of models and will apply them to a variety of real time series datasets

• We fit models to data mostly using likelihood maximization (sometimes with additional regularization terms)

• When uncertainty quantification is desired, we employ Bayesian methods

---

[← ARIMA Example One](08-arima-example-one.md) · [Up: contents](index.md)
