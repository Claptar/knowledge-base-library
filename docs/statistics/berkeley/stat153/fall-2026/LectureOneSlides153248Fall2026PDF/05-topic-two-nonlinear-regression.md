---
title: 'Topic Two: Nonlinear Regression'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureOneSlides153248Fall2026PDF.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Topic Two: Nonlinear Regression

**Source:** [`LectureOneSlides153248Fall2026PDF.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For many time series, nonlinear regression over _t_ leads to much more useful and realistic models


Linear regression of  on 1, _t yt_

- For the US population dataset, simple linear _t_

- regression over  fits one line to the entire data which is clearly unrealistic

- Quadratic (and higher order polynomial) regression does not seem ideal either. These models are also not very interpretable in terms of growth rates

- • A more realistic model here is: _yt_ = _β_ 0 + _β_ 1 _t_ + _α_ 1( _t_ − _c_ 1)+ + _α_ 2( _t_ − _c_ 2)+ + error

- This model allows for three different slopes (growth rates)

- This is a nonlinear regression model with parameters _β_ 0, _β_ 1, _α_ 1, _c_ 1, _α_ 2, _c_ 2


**Annual Sunspots Data**

- Wikipedia says that the number of sunspots varies according to the 11 year solar cycle

- Why should the periodicity be exactly 11? Why not 10.5 or 11.5? What is the uncertainty around 11?

- Can the periodicity be figured out from the dataset?

- One way to do this is to fit the model: _yt_ = _β_ 0 + _β_ 1 cos( _ωt_ ) + _β_ 2 sin( _ωt_ ) + error

- This is a nonlinear regression model with parameters _β_ 0, _β_ 1, _β_ 2, _ω_


**Lynx Trappings Dataset**


**Unemployment Rate from FRED**

• The model:

is _yt_ = _β_ 0 + _β_ 1 cos( _ωt_ ) + _β_ 2 sin( _ωt_ ) + error closely related to Fourier Analysis

- We will study concepts such as Fourier Frequencies, Discrete Fourier Transform and the Periodogram

- These are extensively used in engineering time series analysis

• We shall look at some practical applications of these concepts


**Topic Three: High-dimensional Regression**

**Topic Three: High-dimensional Regression** • To get a good idea of the underlying trend in this data, fitting a single line is clearly not ideal _k_ Fitting is • _yt_ = _β_ 0 + _β_ 1 _t_ + ∑ _αj_ ( _t_ − _cj_ )+ + _ϵ j_ =1 _k k_ also not likely to be good if  is small. But if is large, there is risk of overfitting _k_ • In such cases, we take  to be large, and fit the model using regularization.

###### **Topic Three: High-dimensional Regression**

- We work here with the ‘full’ model: _yt_ = _β_ 0 + _β_ 1 _t_ + _β_ 2( _t_ −2)+ + _β_ 3( _t_ −3)+ + … + _βn_ −1( _t_ − _n_ + 1)+ + _ϵ_

- We study the Ridge and LASSO regularizations for fitting this model

- • This model gives a good representation of the trend present in the data removing the artifacts of noise

Here is this model (with Ridge regularization) applied to the temperature anomalies dataset:


**Comparing Trends in Two Datasets**


The differences can be seen much more clearly if we use this high-dimensional model (with ridge regularization) to estimate the underlying trends

---

[← Regression over time](04-regression-over-time.md) · [Up: contents](index.md) · [Topic Four: Variance Modeling →](06-topic-four-variance-modeling.md)
