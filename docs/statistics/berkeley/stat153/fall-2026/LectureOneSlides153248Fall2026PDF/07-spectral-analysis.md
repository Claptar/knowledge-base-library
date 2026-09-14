---
title: Spectral Analysis
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureOneSlides153248Fall2026PDF.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Spectral Analysis

**Source:** [`LectureOneSlides153248Fall2026PDF.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Spectral Analysis is a special case of variance modeling where the variance model is applied to the Discrete Fourier Transform of the data (as opposed to the data directly)

This is one of the most important tools used by Engineers for Signal Processing

#### **EEG Example: Eyes open vs Closed**


How to quantify the differences between these two time series?

Spectra estimates (multiply x axis by 160 for Hz):


There is a clear difference in the spectra at around the 10 Hz frequency which is a known fact from cognitive neuroscience.

###### **Topic Five: Lagged Regression (ARIMA)**

- Find next number: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, #

- This is the Fibonacci sequence ( _yt_ = _yt_ −1 + _yt_ −2) and the next number is 144

- • Here regression over time will not work •<sup>Instead, we have to regress  over its own</sup> _yt_

- lagged values and _yt_ −1 _yt_ −2

- This is called Lagged Regression or AutoRegression

###### • AutoRegression is the main idea behind the ARIMA class of models which are widely used for time series prediction

- ARIMA stands for AutoRegressive Integrated Moving Average Models

• The basic idea is simply to do a linear regression of  on for _yt xt_ = (1, _yt_ −1, …, _yt_ − _p_ ) some fixed lag _p_ ≥1 • ARIMA models give decent predictions on real datasets and are used extensively

---

[← Topic Four: Variance Modeling](06-topic-four-variance-modeling.md) · [Up: contents](index.md) · [ARIMA Example One →](08-arima-example-one.md)
