---
title: STAT 153 & 248 - Time Series
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeven153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureSeven153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureSeven153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeven153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# STAT 153 & 248 - Time Series

### Lecture Seven
#### Spring 2025, UC Berkeley
#### Aditya Guntuboyina
#### February 11, 2025

## 1 Recap from last lecture

In the last couple of lectures, we considered fitting the sinusoidal model
$$
y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t \quad \text{with } \epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2) \tag{1}
$$
to observed time series $y_1, \dots, y_n$. A key role for inferring the frequency parameter $f$ in this model is played by:
\$\$
RSS(f) := \min_{\beta_0, \beta_1, \beta_2} \sum_{t=1}^n (y_t - \beta

---

[Up: contents](index.md)
