---
title: 'Topic Seven: Neural Networks'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureOneSlides153248Fall2026PDF.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Topic Seven: Neural Networks

**Source:** [`LectureOneSlides153248Fall2026PDF.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- A drawback of these models is that we have to select the value of  appropriately _p_

- •<sup>Even if  is chosen well, the dependence of</sup> _p yt_ on its past values abruptly cuts off at _p_

- • RNNs are a way of fitting functions which use all the past values: _yt_ = _ft_ ( _xt_ , _xt_ −1, …, _x_ 1)

- • We shall study vanilla RNNs and more fancy variants such as LSTMs and GRUs (and possibly also transformers)


Here is a simulated data generated as: for _p_ = 344 _yt_ = _yt_ − _p_ + _ϵt_


Here are the forecasts by the AR model with the correct : _p_

Here are the forecasts by an LSTM (which does not use knowledge of the true ): _p_


• Topic 1: Multiple Linear Regression • Topic 2: Nonlinear Regression • Topic 3: High-dimensional Regression • Topic 4: Variance Models and Spectral Analysis

• Topic 5: ARIMA modeling

• Topic 6: Vector Time Series (VAR models) • Topic 7: Neural Networks

- We will work with a variety of models and will apply them to a variety of real time series datasets

- We fit models to data mostly using likelihood maximization (sometimes with additional regularization terms)

- We will also look at some Bayesian techniques

---

[← Topic Seven: Neural Networks](11-topic-seven-neural-networks.md) · [Up: contents](index.md)
