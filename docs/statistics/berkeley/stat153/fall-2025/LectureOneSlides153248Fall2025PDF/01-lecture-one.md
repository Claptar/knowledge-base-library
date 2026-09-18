---
title: Lecture One
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureOneSlides153248Fall2025PDF.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureOneSlides153248Fall2025PDF.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureOneSlides153248Fall2025PDF.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureOneSlides153248Fall2025PDF.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture One

STAT 153/STAT 248, Fall 2025

Aditya Guntuboyina (28 August 2025)

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

US Population Data

*(Graph titled "US Population Data" with y-axis "Population (in thousands)" ranging from 180000 to 340000 and x-axis "Time (in months)" ranging from 0 to 800.)*

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

What's the next number?

1.) 5, 8, 11, 14, 17, _
2.) 42, 32, 23, 15, 8, _
3.) 3, 6, 12, 24, 48, _
4.) -3, 7, -6, 11, -9, 15, _, _
5.) 4, 16, 36, 64, 100, _

---

## Basic Time Series Prediction Problem

Find the next number: 1, 4, 9, 16, 25, #

The answer is 36 but how did we arrive at it?

We noticed that $y_t$ is a function of the time $t$

In other words, we performed a (quadratic) regression of $y_t$ over time $t$

---

---

[Up: contents](index.md) · [Regression over time →](02-regression-over-time.md)
