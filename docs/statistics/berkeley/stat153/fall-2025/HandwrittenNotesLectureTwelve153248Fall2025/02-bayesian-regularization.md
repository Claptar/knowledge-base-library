---
title: Bayesian Regularization
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwelve153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureTwelve153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureTwelve153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwelve153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Bayesian Regularization

$$y = X\beta + \varepsilon, \qquad \varepsilon_t \overset{\text{iid}}{\sim} N(0, \sigma^2)$$

$$\text{likelihood}: \quad \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^n \exp\left\{ -\frac{\|y - X\beta\|^2}{2\sigma^2} \right\}$$

$$\beta = (\beta_0, \beta_1, \dots, \beta_{n-1}) \quad & \quad \sigma$$

## (1) $\beta_0, \beta_1, \dots, \beta_{n-1} \overset{\text{iid}}{\sim} \text{Unif}(-C, C)$
$$C \to \infty$$

$$\text{posterior} \quad \beta \mid \text{data}, \sigma \underset{\Downarrow \text{ when } C \to \infty}{\sim} N\left( (X^T X)^{-1} X^T y, \, \sigma^2 (X^T X)^{-1} \right)$$
$$\downarrow$$
$$n\text{-variate normal}$$
$$\text{Homework}$$

## (2) $\beta_0, \beta_1, \dots, \beta_{n-1} \overset{\text{iid}}{\sim} N(0, \overset{\downarrow}{C}) \quad (C \text{ large})$

$$\beta \mid \text{data}, \sigma \quad \Downarrow \text{posterior}$$

$$\frac{1}{\sqrt{2\pi} C} \exp\left\{ -\frac{\beta_j^2}{2C} \right\}$$
$$\text{behaves like a constant}$$

---

$$\sim N\left( \left(\frac{X^T X}{\sigma^2} + \frac{I}{C}\right)^{-1} \frac{X^T y}{\sigma^2}, \, \left(\frac{X^T X}{\sigma^2} + \frac{I}{C}\right)^{-1} \right)$$
$$\begin{array}{l} \text{Valid for} \\ \text{every } C \\ \text{(not just for} \\ \text{large } C) \end{array}$$

$$\text{for most } \beta_j \text{ very similar to } \text{Unif}(-C, C)$$
$$\frac{I\{-C < \beta_j < C\}}{2C}$$

$$\text{If } C \to \infty: \quad N\left( \left(\frac{X^T X}{\sigma^2}\right)^{-1} \frac{X^T y}{\sigma^2}, \, \left(\frac{X^T X}{\sigma^2}\right)^{-1} \right)$$
$$= N\left( (X^T X)^{-1} X^T y, \, \sigma^2 (X^T X)^{-1} \right)$$

$$\text{coincides with posterior for } \text{Unif}(-\infty, \infty) \text{ prior.}$$

$$\frac{1}{\sqrt{2\pi} C} \exp\left( -\frac{\beta_j^2}{2C} \right)$$
$$C = 10^{10} \qquad \beta_j \in (-10, 10)$$

---

[← Model](01-model.md) · [Up: contents](index.md) · [Summarize →](03-summarize.md)
