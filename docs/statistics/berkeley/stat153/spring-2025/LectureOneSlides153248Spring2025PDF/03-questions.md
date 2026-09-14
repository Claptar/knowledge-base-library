---
title: Questions
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureOneSlides153248Spring2025PDF.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureOneSlides153248Spring2025PDF.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Questions

**Source:** [`LectureOneSlides153248Spring2025PDF.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureOneSlides153248Spring2025PDF.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### • Prediction: what is an estimate of the population at a future point (e.g., Jan 2040)? • What is the rate of growth of the American population?

- Has the growth rate been roughly constant over time?

- What is the period where the population grew the fastest? Slowest?

Time Series Analysis answers such questions by fitting statistical models to observed time series data

## **Time Series Prediction/Forecasting**

One of the most important questions in time series analysis is that of prediction (estimating future values based on the given data)

#### **Basic Time Series Prediction Problem**

Find the next number: 1, 4, 9, 16, 25, #

The answer is 36 but how did we arrive at it?

We noticed that is a function of the time _t Yt_

In other words, we performed a (quadratic) regression of _Yt_ over time _t_

---

[← US Population](02-us-population.md) · [Up: contents](index.md) · [Regression over time →](04-regression-over-time.md)
