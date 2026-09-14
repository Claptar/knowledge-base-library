---
title: 'Topic Two: Nonlinear Regression'
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureOneSlides153248Spring2025PDF.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureOneSlides153248Spring2025PDF.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Topic Two: Nonlinear Regression

**Source:** [`LectureOneSlides153248Spring2025PDF.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureOneSlides153248Spring2025PDF.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For many time series, nonlinear regression over _t_ leads to much more useful and realistic models


- For the US population dataset, simple linear _t_

- regression over  fits one line to the entire data which is clearly unrealistic

- Quadratic (and higher order polynomial) regression does not seem ideal either. These models are also not very interpretable in terms of growth rates

- • A more realistic model here is: _Yt_ = _β_ 0 + _β_ 1 _t_ + _α_ 1( _t_ − _c_ 1)+ + _α_ 2( _t_ − _c_ 2)+ + error

- This model allows for three different slopes (growth rates)

- This is a nonlinear regression model with parameters _β_ 0, _β_ 1, _α_ 1, _c_ 1, _α_ 2, _c_ 2


**Annual Sunspots Data**

- Wikipedia says that the number of sunspots varies according to the 11 year solar cycle

- Why should the periodicity be exactly 11? Why not 10.5 or 11.5? What is the uncertainty around 11?

- Can the periodicity be figured out from the dataset?

- One way to do this is to fit the model: _Yt_ = _β_ 0 + _β_ 1 cos( _ωt_ ) + _β_ 2 sin( _ωt_ ) + error

- This is a nonlinear regression model with parameters _β_ 0, _β_ 1, _β_ 2, _ω_


**Lynx Trappings Dataset**


**Unemployment Rate from FRED**

###### **Topic Three: High-dimensional Regression**

- It is sometimes tempting to throw in a large number of variables while regressing over time

- • For example, consider the model: _Yt_ = _β_ 0 + _β_ 1 _t_ + _β_ 2( _t_ −2)+ + _β_ 3( _t_ −3)+ + … + _βn_ ( _t_ − _n_ )+ + _ϵ_

- This model allows a different growth rate between every two time points

- To fit such models sensibly, one would need to employ regularization

- We shall study the Ridge and LASSO regularizations

Here is this model (with Ridge regularization) applied to the Google trends data for “yahoo”

---

[← Regression over time](04-regression-over-time.md) · [Up: contents](index.md) · [Topic Four: Variance Modeling →](06-topic-four-variance-modeling.md)
