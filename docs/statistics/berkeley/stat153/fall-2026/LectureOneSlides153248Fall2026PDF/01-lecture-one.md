---
title: Lecture One
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureOneSlides153248Fall2026PDF.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureOneSlides153248Fall2026PDF.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture One

STAT 153/STAT 248, Fall 2026

Aditya Guntuboyina (Fall 2026)

---

## What is Time Series?

Time series is a set of observations each one being recorded at a specific time

The websites https://fred.stlouisfed.org/ and https://trends.google.com have many examples of time series that we will use in this class

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

## Questions

- Prediction: what is an estimate of the population at a future point (e.g., Jan 2040)?
- What is the rate of growth of the American population?
- Has the growth rate been roughly constant over time?
- What is the period where the population grew the fastest? Slowest?

---

Time Series Analysis answers such questions by fitting statistical models to observed time series data

---

## Time Series Prediction/Forecasting

One of the most important questions in time series analysis is that of prediction (estimating future values based on the given data)

---

### What's the next number?

1.) 5, 8, 11, 14, 17, _
2.) 42, 32, 23, 15, 8, _
3.) 3, 6, 12, 24, 48, _
4.) -3, 7, -6, 11, -9, 15, _, _
5.) 4, 16, 36, 64, 100, _

---

## Basic Time Series Prediction Problem

Find the next number: 5, 8, 13, 20, 29, 40, #

The answer is 53 but how did we arrive at it?

We noticed that $y_t$ is a function of the time $t$:
$$y_t = t^2 + 4$$

In other words, we performed a (quadratic) regression of $y_t$ over time $t$

---

## Regression over time

The first time series technique we will study is regression over the time variable $t$

Simple linear regression of the time series $y_t$ on the time variable $t$ will fit a line to the observed time series data

Multiple linear regression of $y_t$ on $t$ and other functions of $t$ (such as powers, sinusoids etc) will fit more general functions to the data

---

## Linear regression of $y_t$ on $1, t$

---

## Linear regression of $y_t$ on $1, \cos(\pi t/6), \sin(\pi t/6)$:

---

$$y_t \sim 1, \cos(\pi t/6), \sin(\pi t/6), \cos(\pi t/3), \sin(\pi t/3)$$

---

$$\cos(\pi t/6), \sin(\pi t/6), \cos(\pi t/3), \sin(\pi t/3), \cos(\pi t/2), \sin(\pi t/2)$$

---

$$y_t \sim \text{sinusoids} + \text{quadratic}$$

---

## Topic One: Multiple Linear Regression

- These models clearly give (sometimes reasonable) solutions to the prediction problem
- The first topic in this course is multiple linear regression
- We will go over the usual frequentist inference but also discuss in detail Bayesian inference for linear regression

---

## Topic Two: Nonlinear Regression

For many time series, nonlinear regression over $t$ leads to much more useful and realistic models

---

## Linear regression of $y_t$ on $1, t$

---

- For the US population dataset, simple linear regression over $t$ fits one line to the entire data which is clearly unrealistic
- Quadratic (and higher order polynomial) regression does not seem ideal either. These models are also not very interpretable in terms of growth rates
- A more realistic model here is:
  $$y_t = \beta_0 + \beta_1 t + \alpha_1 (t - c_1)_+ + \alpha_2 (t - c_2)_+ + \text{error}$$
- This model allows for three different slopes (growth rates)
- This is a nonlinear regression model with parameters $\beta_0, \beta_1, \alpha_1, c_1, \alpha_2, c_2$

---

---

[Up: contents](index.md) · [Annual Sunspots Data →](02-annual-sunspots-data.md)
