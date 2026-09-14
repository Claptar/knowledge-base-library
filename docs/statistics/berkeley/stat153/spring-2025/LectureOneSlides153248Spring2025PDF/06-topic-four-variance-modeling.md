---
title: 'Topic Four: Variance Modeling'
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureOneSlides153248Spring2025PDF.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureOneSlides153248Spring2025PDF.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Topic Four: Variance Modeling

**Source:** [`LectureOneSlides153248Spring2025PDF.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureOneSlides153248Spring2025PDF.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Daily closing prices of Apple Stock from Yahoo Finance


**Stock Returns**

###### • Financial analysts also study the volatility of stock price returns

- For estimating volatility, it is common to use the model: and then to model _Yt_ ∼ _N_ (0, _σt_<sup>2)</sup> _σt_

- (which is a proxy for volatility) as a function of _t_

- • These are examples of variance models as opposed to the mean (regression) models we saw so far

- Spectral Analysis converts the observed time series to the Fourier basis and then uses a variance model on the coefficients

##### **Topic Five: Lagged Regression (ARIMA)**

- Find next number: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, #

- This is the Fibonacci sequence ( _Yt_ = _Yt_ −1 + _Yt_ −2) and the next number is 144

- • Here regression over time will not work •<sup>Instead, we have to regress</sup> _Yt_ over its own lagged values _Yt_ −1 and _Yt_ −2

- • This is called Lagged Regression or AutoRegression

• AutoRegression is the main idea behind the ARIMA class of models which are widely used for time series prediction

• ARIMA stands for AutoRegressive Integrated Moving Average Models • We shall study these models in Topic Five

### **Topic Six: Recurrent Neural Networks**

- Recurrent Neural Networks (RNNs) are usually formulated in the framework of regression: ( _xt_ , _yt_ ), _t_ = 1,…, _n_

- This means that at each time point , we _t_ observe a response value  as well as a _yt_

- covariate vector _xt_

- • Usually in regression, one uses models . But RNNs use

- _yt_ = _f_ ( _xt_ ) _yt_ = _ft_ ( _xt_ , _xt_ −1, …, _x_ 1)

- We shall go over these models (including LSTMs) and some of their applications

• Topic 1: Multiple Linear Regression • Topic 2: Nonlinear Regression • Topic 3: High-dimensional Regression • Topic 4: Variance Models and Spectral Analysis

- Topic 5: ARIMA modeling

• Topic 6: Recurrent Neural Networks

---

[← Topic Two: Nonlinear Regression](05-topic-two-nonlinear-regression.md) · [Up: contents](index.md) · [Different kinds of time series data →](07-different-kinds-of-time-series-data.md)
