---
title: Annual Sunspots Data
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureOneSlides153248Fall2025PDF.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureOneSlides153248Fall2025PDF.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureOneSlides153248Fall2025PDF.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureOneSlides153248Fall2025PDF.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Annual Sunspots Data

*(Graph titled "Sunspot Data" with y-axis "Yearly Sunspot Numbers" ranging from 0 to 250 and x-axis "Year (1700 to 2021)".)*

---

### Sunspot

From Wikipedia, the free encyclopedia

*For other uses, see Sunspot (disambiguation).*

**Sunspots** are temporary spots on the Sun's surface that are darker than the surrounding area. They are one of the most recognizable Solar phenomena and despite the fact that they are mostly visible in the solar photosphere they usually affect the entire solar atmosphere. They are regions of reduced surface temperature caused by concentrations of magnetic flux that inhibit convection. Sunspots appear within active regions, usually in pairs of opposite magnetic polarity.[2] Their number varies according to the approximately 11-year solar cycle.

Individual sunspots or groups of sunspots may last anywhere from a few days to a few months, but eventually decay. Sunspots expand and contract as they move across the surface of the Sun, with diameters ranging from 16 km (10 mi)[3] to 160,000 km (100,000 mi).[4] Larger sunspots can be visible from Earth without the aid of a telescope.[5] They may travel at relative speeds, or proper motions, of a few hundred meters per second when they first emerge.

Indicating intense magnetic activity, sunspots accompany other active region phenomena such as coronal loops, prominences, and reconnection events. Most solar flares and coronal mass ejections originate in these magnetically active regions around visible sunspot groupings. Similar phenomena indirectly observed on stars other than the Sun are commonly called starspots, and both light and dark spots have been measured.[6]

- Top: active region 2192 in 2014 containing the largest sunspot of solar cycle 24[1] and active region 1302 in September 2011.
- Middle: sunspot close-up in the visible spectrum (left) and another sunspot in UV, taken by the TRACE observatory.
- Bottom: a large group of sunspots

---

- Wikipedia says that the number of sunspots varies according to the 11 year solar cycle
- Why should the periodicity be exactly 11? Why not 10.5 or 11.5? What is the uncertainty around 11?
- Can the periodicity be figured out from the dataset?
- One way to do this is to fit the model:
$$y_t = \beta_0 + \beta_1 \cos(\omega t) + \beta_2 \sin(\omega t) + \text{error}$$
- This is a nonlinear regression model with parameters $\beta_0, \beta_1, \beta_2, \omega$

---

## Lynx Trappings Dataset

*(Graph titled "Annual Number of Lynx Trappings in Canada (1821 -- 1934)" with y-axis "Number of Lynx Trappings" ranging from 0 to 7000 and x-axis "Time (year)" ranging from 0 to 100+.)*

---

## Unemployment Rate from FRED

*(Graph titled "Unemployment Rate" with y-axis "Unemployment Rate as a Percent" ranging from 2 to 14 and x-axis "Time (months)" ranging from 0 to 900+.)*

---

- The model:
$$y_t = \beta_0 + \beta_1 \cos(\omega t) + \beta_2 \sin(\omega t) + \text{error}$$
is closely related to Fourier Analysis
- We will study concepts such as Fourier Frequencies, Discrete Fourier Transform and the Periodogram
- These are extensively used in engineering time series analysis
- We shall look at some practical applications of these concepts

---

## Topic Three: High-dimensional Regression

- It is sometimes tempting to throw in a large number of variables while regressing over time
- For example, consider the model:
$$y_t = \beta_0 + \beta_1 t + \beta_2(t - 2)_+ + \beta_3(t - 3)_+ + \dots + \beta_n(t - n)_+ + \epsilon$$
- This model allows a different growth rate between every two time points
- To fit such models sensibly, one would need to employ regularization
- We shall study the Ridge and LASSO regularizations

---

Here is this model (with Ridge regularization) applied to a dataset on temperature anomalies

*(Graph displaying raw temperature anomalies (blue line) with a smoothed Ridge regularization fit (orange line) plotted over indices 0 to 175.)*

---

## Topic Four: Variance Modeling

Daily closing prices $P_t$ of S&P 500 (2000-01-01 to 2024-01-01)

*(Graph titled "S&P 500 daily closing price" with y-axis "Price (dollar)" ranging from 1000 to 5000 and x-axis "Date" ranging from 0 to 6000.)*

---

## Stock Returns $r_t$

$$r_t = 100 \times (\log P_t - \log P_{t-1}) \qquad \text{Note } r_t \approx 100 \times \frac{P_t - P_{t-1}}{P_{t-1}}$$

*(Graph titled "SNP Daily Percentage Returns" with y-axis ranging from -10 to 10 and x-axis ranging from 0 to 6000.)*

---

- Financial analysts also study the volatility of stock price returns
- For estimating volatility, it is common to use the model: $r_t \sim N(0, \sigma_t^2)$ and then to model $\sigma_t$ (which is a proxy for volatility) as a function of $t$
- These are examples of variance models as opposed to the mean (regression) models we saw so far

---

For the S&P returns data, below is an estimate of $\log \sigma_t$

*(Graph showing estimated $\log \sigma_t$ over time points 0 to 6000 using "ridge" (blue line) and "lasso" (black line).)*

---

*(Stacked graphs: Top graph showing "SNP Daily Percentage Returns" over time 0 to 6000; bottom graph showing estimates of $\log \sigma_t$ using "ridge" and "lasso" over the same time horizon.)*

---

## Spectral Analysis

Spectral Analysis is a special case of variance modeling where the variance model is applied to the Discrete Fourier Transform of the data (as opposed to the data directly)

This is one of the most important tools used by Engineers for Signal Processing

---

## EEG Example: Eyes open vs Closed

*(Two EEG signal plots: upper plot titled "y_o" (eyes open), lower plot titled "y_c" (eyes closed), both with values between -0.0002 and 0.0002 over 10000 time points.)*

How to quantify the differences between these two time series?

---

Spectra estimates (multiply x axis by 160 for Hz):

*(Plot comparing spectra estimates of "Open" (black line) and "Closed" (red line) with x-axis from 0.0 to 0.5 and y-axis from -24 to -16.)*

There is a clear difference in the spectra at around the 10 Hz frequency which is a known fact from cognitive neuroscience.

---

## Topic Five: Lagged Regression (ARIMA)

- Find next number: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, #
- This is the Fibonacci sequence ($y_t = y_{t-1} + y_{t-2}$) and the next number is 144
- Here regression over time will not work
- Instead, we have to regress $y_t$ over its own lagged values $y_{t-1}$ and $y_{t-2}$
- This is called Lagged Regression or AutoRegression

---

- AutoRegression is the main idea behind the ARIMA class of models which are widely used for time series prediction
- ARIMA stands for AutoRegressive Integrated Moving Average Models
- The basic idea is simply to do a linear regression of $y_t$ on $x_t = (1, y_{t-1}, \dots, y_{t-p})$ for some fixed lag $p \ge 1$
- ARIMA models give decent predictions on real datasets and are used extensively

---

## ARIMA Example One

FRED data on GNP (seasonally adjusted, billions of dollars). This is a quarterly dataset (four quarters in a year).

*(Graph showing quarterly GNP from 0 to 30000 over time periods 0 to 300+.)*

Here are the predictions given by an AR model for the last four

---

[← Regression over time](02-regression-over-time.md) · [Up: contents](index.md)
