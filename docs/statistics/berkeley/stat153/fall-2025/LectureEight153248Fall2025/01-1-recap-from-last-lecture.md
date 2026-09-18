---
title: 1 Recap from last lecture
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEight153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureEight153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Recap from last lecture

## Lecture Eight
Fall 2025, UC Berkeley

Aditya Guntuboyina

September 23, 2025

In the last lecture, we considered fitting the sinusoidal model
$$y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t \quad \text{with } \epsilon_t \stackrel{\text{i.i.d}}{\sim} N(0, \sigma^2) \tag{1}$$
to observed time series $y_1, \dots, y_n$. A key role for inferring the frequency parameter $f$ in this model is played by:
$$RSS(f) := \min_{\beta_0, \beta_1, \beta_2} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 \cos(2\pi f t) - \beta_2 \sin(2\pi f t))^2 = \|y - X_f \hat{\beta}_f\|^2$$
where
$$y = \begin{pmatrix} y_1 \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix} \quad \text{and} \quad X_f = \begin{pmatrix} 1 & \cos(2\pi f(1)) & \sin(2\pi f(1)) \\ \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot \\ 1 & \cos(2\pi f(n)) & \sin(2\pi f(n)) \end{pmatrix} \quad \text{and} \quad \hat{\beta}_f = (X_f^T X_f)^{-1} X_f^T y.$$
$RSS(f)$ is simply the residual sum of squares in the linear regression model obtained by fixing the frequency parameter $f$. It describes how well the sinusoid with frequency $f$ fits the observed data $y_1, \dots, y_n$.

Calculating $RSS(f)$ separately for each value of $f$ in a grid of values of $f$ can be computationally quite inefficient (particularly when $n$ is large). We have started discussing efficient computation of $RSS(f)$ in the last lecture. The key here is to recognize the following alternative formula for $RSS(f)$ (proved in last lecture) that holds when $f \in (0, 0.5)$ is a Fourier frequency i.e., $nf$ is an integer:
$$RSS(f) = \sum_t (y_t - \bar{y})^2 - 2I(f) \quad \text{when } f \in (0, 0.5) \text{ is a Fourier Frequency} \tag{2}$$
where $I(f)$ is defined by
$$I(f) := \frac{1}{n} \left( \sum_{t=1}^n y_t \cos(2\pi f t) \right)^2 + \frac{1}{n} \left( \sum_{t=1}^n y_t \sin(2\pi f t) \right)^2 \quad \text{for } f \in (0, 0.5) \tag{3}$$
$I(f)$ is known as the Periodogram of the data $y_1, \dots, y_n$.

In this lecture, we study the Discrete Fourier Transform (DFT) of the observed time series data, and see how the DFT is related to the periodogram.

---

[Up: contents](index.md) · [2 Discrete Fourier Transform (DFT) and Periodogram →](02-2-discrete-fourier-transform-dft-and-periodogram.md)
