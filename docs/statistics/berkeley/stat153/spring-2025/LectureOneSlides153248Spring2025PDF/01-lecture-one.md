---
title: Lecture One
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureOneSlides153248Spring2025PDF.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureOneSlides153248Spring2025PDF.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureOneSlides153248Spring2025PDF.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureOneSlides153248Spring2025PDF.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture One

### STAT 153/STAT 248, Spring 2025

Aditya Guntuboyina (21 January 2025)

---

## What is Time Series?

Time series is a set of observations each one being recorded at a specific time

---

## US Population

Population of the United States

| observation_date | POPTHM |
| :--- | :--- |
| 1959-01-01 | 175818 |
| 1959-02-01 | 176044 |
| 1959-03-01 | 176274 |
| 1959-04-01 | 176503 |
| 1959-05-01 | 176723 |
| 1959-06-01 | 176954 |
| 1959-07-01 | 177208 |
| 1959-08-01 | 177479 |
| 1959-09-01 | 177755 |
| 1959-10-01 | 178026 |
| 1959-11-01 | 178273 |
| 1959-12-01 | 178504 |
| 1960-01-01 | 178925 |
| 1960-02-01 | 179326 |
| 1960-03-01 | 179707 |
| 1960-04-01 | 180067 |
| 1960-05-01 | 180408 |
| 1960-06-01 | 180728 |

- Units are thousands so that 300,000 actually refers to 300 million
- This dataset is downloaded from FRED

---

## US Population Data

*(Plot of Population (in thousands) vs. Time (in months))*

---

## Questions

- Prediction: what is an estimate of the population at a future point (e.g., Jan 2040)?
- What is the rate of growth of the American population?
- Has the growth rate been roughly constant over time?
- What is the period where the population grew the fastest? Slowest?

---

Time Series Analysis answers such questions by fitting statistical **models** to observed time series data

---

## Time Series Prediction/Forecasting

One of the most important questions in time series analysis is that of prediction (estimating future values based on the given data)

---

## Basic Time Series Prediction Problem

Find the next number: 1, 4, 9, 16, 25, #

The answer is 36 but how did we arrive at it?

We noticed that $Y_t$ is a function of the time $t$

In other words, we performed a (quadratic) regression of $Y_t$ over time $t$

---

## Regression over time

The first time series technique we will study is regression over the time variable $t$

Simple linear regression of the time series $Y_t$ on the time variable $t$ will fit a line to the observed time series data

Multiple linear regression of $Y_t$ on $t$ and other functions of $t$ (such as powers, sinusoids etc) will fit more general functions to the data

---

## Monthly Totals of Accidental Deaths in the US 1973-1978

*(Plot of Deaths vs. Time from 1973 to 1979)*

---

## Linear regression of $Y_t$ on $1, \cos(\pi t / 6), \sin(\pi t / 6)$:

### Monthly Totals of Accidental Deaths in the US 1973-1978

*(Plot of Deaths vs. Time with fitted line)*

---

## $Y_t \sim 1, \cos(\pi t / 6), \sin(\pi t / 6), \cos(\pi t / 3), \sin(\pi t / 3)$

### Monthly Totals of Accidental Deaths in the US 1973-1978

*(Plot of Deaths vs. Time with fitted curve)*

---

## $\cos(\pi t / 6), \sin(\pi t / 6), \cos(\pi t / 3), \sin(\pi t / 3), \cos(\pi t / 2), \sin(\pi t / 2)$

### Monthly Totals of Accidental Deaths in the US 1973-1978

*(Plot of Deaths vs. Time with fitted curve)*

---

## $Y_t \sim \text{sinusoids} + \text{quadratic}$

### Monthly Totals of Accidental Deaths in the US 1973-1978

*(Plot of Deaths vs. Time with fitted curve)*

---

## Topic One: Multiple Linear Regression

- These models clearly give (sometimes reasonable) solutions to the prediction problem
- The first topic in this course is multiple linear regression
- We will go over the usual frequentist inference but also discuss in detail Bayesian inference for linear regression

---

## Topic Two: Nonlinear Regression

For many time series, nonlinear regression over $t$ leads to much more useful and realistic models

---

## US Population Data

*(Plot of Population (in thousands) vs. Time (in months))*

---

- For the US population dataset, simple linear regression over $t$ fits one line to the entire data which is clearly unrealistic
- Quadratic (and higher order polynomial) regression does not seem ideal either. These models are also not very interpretable in terms of growth rates
- A more realistic model here is:
  $$Y_t = \beta_0 + \beta_1 t + \alpha_1 (t - c_1)_+ + \alpha_2 (t - c_2)_+ + \text{error}$$
- This model allows for three different slopes (growth rates)
- This is a nonlinear regression model with parameters $\beta_0, \beta_1, \alpha_1, c_1, \alpha_2, c_2$

---

## Annual Sunspots Data

### Sunspot Data

*(Plot of Yearly Sunspot Numbers vs. Year (1700 to 2021))*

---

---

[Up: contents](index.md) · [Sunspot →](02-sunspot.md)
