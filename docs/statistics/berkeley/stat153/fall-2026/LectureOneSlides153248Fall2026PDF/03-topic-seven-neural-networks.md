---
title: 'Topic Seven: Neural Networks'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureOneSlides153248Fall2026PDF.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureOneSlides153248Fall2026PDF.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Topic Seven: Neural Networks

- A drawback of these models is that we have to select the value of $p$ appropriately
- Even if $p$ is chosen well, the dependence of $y_t$ on its past values abruptly cuts off at $p$
- RNNs are a way of fitting functions which use all the past values: $y_t = f_t(x_t, x_{t-1}, \dots, x_1)$
- We shall study vanilla RNNs and more fancy variants such as LSTMs and GRUs (and possibly also transformers)

---

Here is a simulated data generated as: $y_t = y_{t-p} + \epsilon_t$ for $p = 344$

---

Here are the forecasts by the AR model with the correct $p$:

---

Here are the forecasts by an LSTM (which does not use knowledge of the true $p$):

---

- Topic 1: Multiple Linear Regression
- Topic 2: Nonlinear Regression
- Topic 3: High-dimensional Regression
- Topic 4: Variance Models and Spectral Analysis
- Topic 5: ARIMA modeling
- Topic 6: Vector Time Series (VAR models)
- Topic 7: Neural Networks

---

- We will work with a variety of models and will apply them to a variety of real time series datasets
- We fit models to data mostly using likelihood maximization (sometimes with additional regularization terms)
- We will also look at some Bayesian techniques

---

[← Annual Sunspots Data](02-annual-sunspots-data.md) · [Up: contents](index.md)
