---
title: Regression over time
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureOneSlides153248Fall2025PDF.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureOneSlides153248Fall2025PDF.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureOneSlides153248Fall2025PDF.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureOneSlides153248Fall2025PDF.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Regression over time

The first time series technique we will study is regression over the time variable $t$

Simple linear regression of the time series $y_t$ on the time variable $t$ will fit a line to the observed time series data

Multiple linear regression of $y_t$ on $t$ and other functions of $t$ (such as powers, sinusoids etc) will fit more general functions to the data

---

Linear regression of $y_t$ on $1, t$

*(Graph titled "US Population" comparing "US population" (blue line) and "Linear Fit" (red line) with y-axis "US Population (in thousands)" ranging from 175000 to 350000 and x-axis "Time (months)" ranging from 0 to 800.)*

---

*(Graph titled "Monthly Totals of Accidental Deaths in the US 1973-1978" with y-axis "Deaths" ranging from 7000 to 11000 and x-axis "Time" ranging from 1973 to 1979.)*

---

Linear regression of $y_t$ on $1, \cos(\pi t/6), \sin(\pi t/6)$:

*(Graph titled "Monthly Totals of Accidental Deaths in the US 1973-1978" showing original data line with circles and fitted curve in red over time points 0 to 70.)*

---

$$y_t \sim 1, \cos(\pi t/6), \sin(\pi t/6), \cos(\pi t/3), \sin(\pi t/3)$$

*(Graph titled "Monthly Totals of Accidental Deaths in the US 1973-1978" showing original data line with circles and fitted curve in red over time points 0 to 70.)*

---

$$\cos(\pi t/6), \sin(\pi t/6), \cos(\pi t/3), \sin(\pi t/3), \cos(\pi t/2), \sin(\pi t/2)$$

*(Graph titled "Monthly Totals of Accidental Deaths in the US 1973-1978" showing original data line with circles and fitted curve in red over time points 0 to 70.)*

---

$$y_t \sim \text{sinusoids} + \text{quadratic}$$

*(Graph titled "Monthly Totals of Accidental Deaths in the US 1973-1978" showing original data line with circles and fitted curve in red over time points 0 to 70.)*

---

## Topic One: Multiple Linear Regression

- These models clearly give (sometimes reasonable) solutions to the prediction problem
- The first topic in this course is multiple linear regression
- We will go over the usual frequentist inference but also discuss in detail Bayesian inference for linear regression

---

## Topic Two: Nonlinear Regression

For many time series, nonlinear regression over $t$ leads to much more useful and realistic models

---

*(Graph titled "US Population Data" with y-axis "Population (in thousands)" ranging from 180000 to 340000 and x-axis "Time (in months)" ranging from 0 to 800.)*

---

*(Graph titled "US Population" showing "US population" and "Linear Fit" with y-axis "US Population (in thousands)" from 175000 to 350000 and x-axis "Time (months)" from 0 to 800.)*

---

- For the US population dataset, simple linear regression over $t$ fits one line to the entire data which is clearly unrealistic
- Quadratic (and higher order polynomial) regression does not seem ideal either. These models are also not very interpretable in terms of growth rates
- A more realistic model here is:
$$y_t = \beta_0 + \beta_1 t + \alpha_1(t - c_1)_+ + \alpha_2(t - c_2)_+ + \text{error}$$
- This model allows for three different slopes (growth rates)
- This is a nonlinear regression model with parameters $\beta_0, \beta_1, \alpha_1, c_1, \alpha_2, c_2$

---

---

[← Lecture One](01-lecture-one.md) · [Up: contents](index.md) · [Annual Sunspots Data →](03-annual-sunspots-data.md)
