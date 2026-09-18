---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureNine153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureNine153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureNine153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureNine153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Introduction

## Lecture NINE

Data: $y_0, y_1, \dots, y_{n-1}$ (Python indexing)

$$y_t = \beta_0 + \beta_1 \cos 2\pi ft + \beta_2 \sin 2\pi ft + \varepsilon_t$$
$$\varepsilon_t \sim N(0, \sigma^2)$$

Parameters:
$$\underbrace{\beta_0, \beta_1, \beta_2, \sigma}_{\text{nuisance parameters}}, f$$

$$RSS(f) = \min_{\beta_0, \beta_1, \beta_2} \sum_{t=0}^{n-1} \left( y_t - \beta_0 - \beta_1 \cos 2\pi ft - \beta_2 \sin 2\pi ft \right)^2$$

$$\hat{f} \to \text{minimizer of } RSS(f)$$

$$\text{posterior}(f) \propto \left(\frac{1}{RSS(f)}\right)^{\frac{n-3}{2}} |X_f^T X_f|^{-1/2} I(0 < f < \frac{1}{2})$$

We need some candidate values for $f$ to compute $RSS(f)$ (& then subsequent minimization or posterior computation). There are two options:

(1) Take a dense grid of points in $[0, 0.5]$

(2) Take the grid of **Fourier frequencies**:
$\{\frac{1}{n}, \frac{2}{n}, \dots\} \text{ in } (0, \frac{1}{2})$.
Then $RSS(f)$, $f \in \text{Fourier grid } \{\frac{1}{n}, \frac{2}{n}, \dots\} \cap (0, \frac{1}{2})$ can be efficiently computed using the FFT algorithm.

---

$$\begin{pmatrix} y_0, y_1, \dots, y_{n-1} \\ \downarrow \text{DFT} \\ b_0, b_1, \dots, b_{n-1} \end{pmatrix} \quad \left\} \text{This step uses the FFT algorithm & is very fast.} \right.$$

$$b_j = \sum_{t=0}^{n-1} y_t \exp\left(-2\pi i \frac{j}{n} t\right)$$

$$\text{Periodogram: } I(\frac{j}{n}) = \frac{|b_j|^2}{n}$$

$$\boxed{RSS\left(\frac{j}{n}\right) = \sum_{t=0}^{n-1} (y_t - \bar{y})^2 - 2 I\left(\frac{j}{n}\right)}$$

Minimize $RSS\left(\frac{j}{n}\right)$ to get $\hat{f} = \frac{\hat{j}}{n}$

$$\text{posterior}\left(\frac{j}{n}\right) \propto \left(\frac{1}{RSS\left(\frac{j}{n}\right)}\right)^{\frac{n-3}{2}} |X_{\frac{j}{n}}^T X_{\frac{j}{n}}|^{-1/2} I\left(0 < \frac{j}{n} < \frac{1}{2}\right)$$

Lecture 7, we saw that if $f \in (0, \frac{1}{2}]$ is a Fourier frequency,

$$X_f^T X_f = \begin{bmatrix} n & 0 & 0 \\ 0 & \frac{n}{2} & 0 \\ 0 & 0 & \frac{n}{2} \end{bmatrix} \leftarrow \text{does not depend on } f$$

$$X_f = \begin{bmatrix} 1 & \cos(2\pi ft), & \sin(2\pi ft) \\ \vdots & t=0, 1, \dots, n-1 & t=0, 1, \dots, n-1 \end{bmatrix}$$

$$\text{posterior}\left(\frac{j}{n}\right) \propto \left(\frac{1}{RSS\left(\frac{j}{n}\right)}\right)^{\frac{n-3}{2}} I\left(0 < \frac{j}{n} < \frac{1}{2}\right)$$

---

This reduction to Fourier frequencies is only used for COMPUTATIONAL PURPOSES.

---

[Up: contents](index.md) · [More Nonlinear Regression Models →](02-more-nonlinear-regression-models.md)
