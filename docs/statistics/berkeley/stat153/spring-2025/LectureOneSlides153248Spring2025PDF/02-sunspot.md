---
title: Sunspot
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureOneSlides153248Spring2025PDF.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureOneSlides153248Spring2025PDF.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureOneSlides153248Spring2025PDF.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureOneSlides153248Spring2025PDF.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Sunspot

From Wikipedia, the free encyclopedia

Sunspots are temporary spots on the Sun's surface that are darker than the surrounding area. They are one of the most recognizable Solar phenomena and despite the fact that they are mostly visible in the solar photosphere they usually affect the entire solar atmosphere. They are regions of reduced surface temperature caused by concentrations of magnetic flux that inhibit convection. Sunspots appear within active regions, usually in pairs of opposite magnetic polarity. Their number varies according to the approximately 11-year solar cycle.

Individual sunspots or groups of sunspots may last anywhere from a few days to a few months, but eventually decay. Sunspots expand and contract as they move across the surface of the Sun, with diameters ranging from 16 km (10 mi) to 160,000 km (100,000 mi). Larger sunspots can be visible from Earth without the aid of a telescope. They may travel at relative speeds, or proper motions, of a few hundred meters per second when they first emerge.

Indicating intense magnetic activity, sunspots accompany other active region phenomena such as coronal loops, prominences, and reconnection events. Most solar flares and coronal mass ejections originate in these magnetically active regions around visible sunspot groupings. Similar phenomena indirectly observed on stars other than the Sun are commonly called starspots, and both light and dark spots have been measured.

- Top: active region 2192 in 2014 containing the largest sunspot of solar cycle 24 and active region 1302 in September 2011.
- Middle: sunspot close-up in the visible spectrum (left) and another sunspot in UV, taken by the TRACE observatory.
- Bottom: a large group of sunspots

---

- Wikipedia says that the number of sunspots varies according to the 11 year solar cycle
- Why should the periodicity be exactly 11? Why not 10.5 or 11.5? What is the uncertainty around 11?
- Can the periodicity be figured out from the dataset?
- One way to do this is to fit the model:
  $$Y_t = \beta_0 + \beta_1 \cos(\omega t) + \beta_2 \sin(\omega t) + \text{error}$$
- This is a nonlinear regression model with parameters $\beta_0, \beta_1, \beta_2, \omega$

---

## Lynx Trappings Dataset

### Annual Number of Lynx Trappings in Canada (1821 -- 1934)

*(Plot of Number of Lynx Trappings vs. Time (year))*

---

## Unemployment Rate from FRED

### Unemployment Rate

*(Plot of Unemployment Rate as a Percent vs. Time (months))*

---

## Topic Three: High-dimensional Regression

- It is sometimes tempting to throw in a large number of variables while regressing over time
- For example, consider the model:
  $$Y_t = \beta_0 + \beta_1 t + \beta_2(t - 2)_+ + \beta_3(t - 3)_+ + \dots + \beta_n(t - n)_+ + \epsilon$$
- This model allows a different growth rate between every two time points
- To fit such models sensibly, one would need to employ regularization
- We shall study the Ridge and LASSO regularizations

---

Here is this model (with Ridge regularization) applied to the Google trends data for "yahoo"

*(Plot of y vs. x with fitted red curve)*

---

## Topic Four: Variance Modeling

Daily closing prices of Apple Stock from Yahoo Finance

### AAPL$AAPL.Adjusted
2007-01-03 / 2025-01-17

*(Plot of Apple adjusted closing price over time)*

---

## Stock Returns

### AAPL.rtn
2007-01-03 / 2025-01-17

*(Plot of stock returns over time)*

---

- Financial analysts also study the volatility of stock price returns
- For estimating volatility, it is common to use the model: $Y_t \sim N(0, \sigma_t^2)$ and then to model $\sigma_t$ (which is a proxy for volatility) as a function of $t$
- These are examples of variance models as opposed to the mean (regression) models we saw so far
- **Spectral Analysis** converts the observed time series to the Fourier basis and then uses a variance model on the coefficients

---

## Topic Five: Lagged Regression (ARIMA)

- Find next number: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, #
- This is the Fibonacci sequence ($Y_t = Y_{t-1} + Y_{t-2}$) and the next number is 144
- Here regression over time will not work
- Instead, we have to regress $Y_t$ over its own lagged values $Y_{t-1}$ and $Y_{t-2}$
- This is called Lagged Regression or AutoRegression

---

- AutoRegression is the main idea behind the ARIMA class of models which are widely used for time series prediction
- ARIMA stands for AutoRegressive Integrated Moving Average Models
- We shall study these models in Topic Five

---

## Topic Six: Recurrent Neural Networks

- Recurrent Neural Networks (RNNs) are usually formulated in the framework of regression: $(x_t, y_t), t = 1, \dots, n$
- This means that at each time point $t$, we observe a response value $y_t$ as well as a covariate vector $x_t$
- Usually in regression, one uses models $y_t = f(x_t)$. But RNNs use $y_t = f_t(x_t, x_{t-1}, \dots, x_1)$
- We shall go over these models (including LSTMs) and some of their applications

---

- Topic 1: Multiple Linear Regression
- Topic 2: Nonlinear Regression
- Topic 3: High-dimensional Regression
- Topic 4: Variance Models and Spectral Analysis
- Topic 5: ARIMA modeling
- Topic 6: Recurrent Neural Networks

---

## Different kinds of time series data

- Univariate Time Series
- Vector Time Series
- Time Series Regression data
- Sequential Data

---

## Univariate Time Series

- $y_1, \dots, y_T$ where each $y_t$ is a real number
- This is the simplest time series dataset
- We shall be mostly working with these in this course

---

## Vector Time Series

- $y_1, \dots, y_T$ where each $y_t$ is vector-valued
- For example, consider $y_t = (y_{t1}, y_{t2})^T$ where $y_{t1}$ is the unemployment rate and $y_{t2}$ is the GDP growth rate for the $t^{\text{th}}$ quarter. This is a bivariate time series
- When the dimension of the vectors is large, these are referred to as high-dimensional time series
- We will not spend that much time on vector time series

---

## Time Series Regression

- $(x_1, y_1), \dots, (x_T, y_T)$ where each $x_t$ is vector-valued and $y_t$ is real-valued
- For each time point $t$, we observe a covariate vector $x_t$ as well as a response value $y_t$
- The goal is to predict $y_{T+1}$ given $x_{T+1}$ and the current data set (and then $y_{T+2}$ given $x_{T+2}$ etc.)
- This is a more general setting compared to both regression over time ($x_t = t$) and lagged regression ($x_t = (y_{t-1}, y_{t-2}, \dots, y_{t-p})$)
- We shall study RNNs in this setting

---

## Sequential Data

- In Machine Learning, sequential data mostly refers to $(x_i, y_i), i = 1, \dots, n$ where each $x_i$ is a time series and/or each $y_i$ is a time series. There is often no dependence across $i$
- E.g., consider the problem of determining whether a review is positive or not based on the text of the review. $x_i$ denotes the $i^{\text{th}}$ review and $y_i$ is binary
- Each review $x_i\$ is a sequence of words which can be viewed as a time series.
- RNNs have heavily been used here

---

[← Lecture One](01-lecture-one.md) · [Up: contents](index.md)
