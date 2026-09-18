---
title: STAT 153 & 248 - Time Series
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureThirteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureThirteen153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureThirteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureThirteen153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# STAT 153 & 248 - Time Series

## Lecture Thirteen
### Spring 2025, UC Berkeley
### Aditya Guntuboyina
### March 5, 2025

In this lecture, we shall revisit sines and cosines and discuss a high-dimensional model involving sinusoids (there will be connections to the high-dimensional regression models that we studied last week; even though the main model for this week will be somewhat different from those).

## 1 Recap: Sunspots Data

In order to motivate the model that we shall study today, consider the annual sunspots dataset $y_t$ that we previously looked at multiple times in this class.

Previously (e.g., Lecture 8), we used the following models for the sunspots data:
$$y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t \tag{1}$$
$$y_t = \beta_0 + \beta_1 \cos(2\pi f_1 t) + \beta_2 \sin(2\pi f_1 t) + \beta_3 \cos(2\pi f_2 t) + \beta_4 \sin(2\pi f_2 t) + \epsilon_t \tag{2}$$
$$y_t = \beta_0 + \beta_1 \cos(2\pi f_1 t) + \beta_2 \sin(2\pi f_1 t) + \beta_3 \cos(2\pi f_2 t) + \beta_4 \sin(2\pi f_2 t) + \beta_5 \cos(2\pi f_3 t) + \beta_6 \sin(2\pi f_3 t) + \epsilon_t \tag{3}$$
In all these models, $\epsilon_t \sim N(0, \sigma^2)$. $f, f_1, f_2, f_3$ represent unknown frequency parameters. These models are helpful for understanding certain aspects of the sunspots data. For example, model (1), when fitted to

---

[Up: contents](index.md)
