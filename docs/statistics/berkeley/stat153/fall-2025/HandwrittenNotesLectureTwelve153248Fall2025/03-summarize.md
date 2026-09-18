---
title: Summarize
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwelve153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureTwelve153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureTwelve153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwelve153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Summarize

(1) If you are using $C$ large $\left(\text{either in } \begin{matrix} \text{Unif}(-C, C) \\ \text{or } N(0, C) \end{matrix}\right)$ the posterior mean = least squares will lead to overfitting.

### (3) $\beta_0, \beta_1 \overset{\text{iid}}{\sim} N(0, C), \quad C \text{ large} \qquad \beta_2, \dots, \beta_{n-1} \overset{\text{iid}}{\sim} N(0, \tau^2) \quad \text{for some small } \tau > 0$

---

This will lead to smooth fits without overfitting (depending on the chosen value of $\tau$)

The formula for the posterior:

$$\beta \sim N_n\left( \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix}, \, \begin{pmatrix} C & & & 0 \\ & C & & \\ & & \tau^2 & & \\ & & & \ddots & \\ 0 & & & & \tau^2 \end{pmatrix} \right)$$

$$\beta \sim N(0, Q) \qquad \underbrace{\qquad\qquad\qquad\qquad\quad}_{Q}$$

Check: posterior now becomes

$$N\left( \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2}, \, \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \right)$$

$$\beta \mid \text{data}, \sigma \quad \text{posterior mean}:$$
$$\left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2}$$

$$Q^{-1} = \begin{pmatrix} 1/C & & & 0 \\ & 1/C & & \\ & & 1/\tau^2 & & \\ & & & \ddots & \\ 0 & & & & 1/\tau^2 \end{pmatrix}$$

$$\approx \begin{pmatrix} 0 & 0 & & 0 \\ 0 & 0 & & \\ & & 1/\tau^2 & & \\ & & & \ddots & \\ 0 & & & & 1/\tau^2 \end{pmatrix} = \frac{1}{\tau^2} J$$

---

$$\text{posterior mean}: \quad \left(\frac{X^T X}{\sigma^2} + \frac{1}{\tau^2} J\right)^{-1} \frac{X^T y}{\sigma^2} = \left(X^T X + \frac{\sigma^2}{\tau^2} J\right)^{-1} X^T y$$

$$\text{Ridge}: \quad (X^T X + \lambda J)^{-1} X^T y$$

$$\text{Coincide if } \quad \lambda = \frac{\sigma^2}{\tau^2}$$

---

$$\beta_j \overset{\text{iid}}{\sim} N(0, C) \ (\text{or } \text{Unif}(-C, C)) \quad C \text{ large}$$
$$\text{Bayesian} = \text{Frequentist}$$
$$(X^T X)^{-1} X^T y$$

$$\beta_0, \beta_1 \overset{\text{iid}}{\sim} N(0, C), \ C \text{ large} \qquad \beta_j \overset{\text{iid}}{\sim} N(0, \tau^2), \ j = 2, \dots, n-1$$

$$\begin{array}{c} \text{Frequentist} \\ \text{with Ridge} \\ \text{Regularization} \end{array} = \text{Bayesian}$$

$$\begin{array}{l} \overset{\text{Prior 1}}{\longrightarrow} \beta_j \overset{\text{iid}}{\sim} N(0, C) \longrightarrow \text{least squares} \\ \overset{\text{Prior 2}}{\longrightarrow} \beta_0, \beta_1 \overset{\text{iid}}{\sim} N(0, C), \quad \beta_j \overset{\text{iid}}{\sim} N(0, \tau^2) \longrightarrow \text{Ridge Regularization} \\ \qquad\qquad\qquad\qquad\qquad\quad \text{if } \tau \text{ is small} \end{array}$$

Prior 2 is restrictive.

---

$$\text{Prior 3}: \quad \beta_0, \beta_1 \overset{\text{iid}}{\sim} N(0, C), \quad \beta_j \overset{\text{iid}}{\sim} N(0, \tau^2)$$
$$\log \tau \sim \text{Unif}(-C, C), \quad \log \sigma \sim \text{Unif}(-C, C)$$

$$\text{More General}$$

$$\text{prior}:$$
$$f_{\beta, \sigma, \tau}(\beta, \sigma, \tau) \propto \frac{1}{\sqrt{\det Q}} \exp\left( -\frac{\beta^T Q^{-1} \beta}{2} \right) \frac{I\{-C < \log \tau < C\}}{\tau} \frac{I\{-C < \log \sigma < C\}}{\sigma}$$

$$\beta \sim N\left( \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix}, \, \begin{pmatrix} C & & & 0 \\ & C & & \\ & & \tau^2 & & \\ & & & \ddots & \\ 0 & & & & \tau^2 \end{pmatrix} \right) = \frac{\tau^{-1} \sigma^{-1}}{\sqrt{\det Q}} \exp\left( -\frac{\beta^T Q^{-1} \beta}{2} \right)$$
$$N(0, Q)$$

$$\text{Likelihood}: \quad \sigma^{-n} \exp\left( -\frac{\|y - X\beta\|^2}{2\sigma^2} \right)$$

$$\begin{array}{l} \text{posterior} \\ (\beta, \tau, \sigma) \\ f_{\beta, \tau, \sigma \mid \text{data}}(\beta, \tau, \sigma) \end{array} : \quad \frac{\sigma^{-n-1} \tau^{-1}}{\sqrt{\det Q}} \exp\left\{ -\frac{1}{2} \left( \frac{\|y - X\beta\|^2}{\sigma^2} + \beta^T Q^{-1} \beta \right) \right\}$$

$$\text{For fixed } \sigma, \tau, \text{ integration w.r.t } \beta \text{ is tractable.}$$

---

$$\frac{\|y - X\beta\|^2}{\sigma^2} + \beta^T Q^{-1} \beta \qquad \begin{pmatrix} x^2 - 4x + 6 \\ = (x-2)^2 + 2 \end{pmatrix}$$
$$= (\beta - b)^T \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right) (\beta - b) + \frac{y^T y}{\sigma^2} - b^T \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right) b$$

$$b = \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2}$$

$$\underset{\sigma, \tau \mid \text{data}}{f(\sigma, \tau)} \propto \text{integral of } \underset{\beta, \sigma, \tau \mid \text{data}}{f(\beta, \sigma, \tau)} \text{ w.r.t } \beta$$

$$\propto \frac{\sigma^{-n-1} \tau^{-1}}{\sqrt{\det Q}} \left[\det\left(\left[\frac{X^T X}{\sigma^2} + Q^{-1}\right]^{-1}\right)\right]^{1/2} \exp\left(-\frac{y^T y}{2\sigma^2}\right) \exp\left\{ \frac{y^T X}{2\sigma^2} \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2} \right\}$$

(1) Take a grid of values of $\sigma$ & $\tau$
(2) Compute $f_{\sigma, \tau \mid \text{data}}$ over the grid
(3) posterior mean/mode of $\sigma$ & $\tau$
Sample values of $\sigma$ & $\tau$
(4) Sample $\beta$ from $\beta \mid \text{data}, \sigma, \tau$ : normal posterior

---

## Why no overfitting?

$$f_{\text{data} \mid \beta, \sigma} : \begin{array}{l} \text{Likelihood} \\ \text{maximization leads to} \\ \hat{\beta} = \text{unregularized} \\ \qquad \text{least squares} \end{array} \quad \hat{\sigma} = 0$$

$$f_{\text{data} \mid \tau, \sigma} = \int f_{\text{data} \mid \beta, \sigma}(\text{data}) \, f_{\beta \mid \tau}(\beta) \, d\beta$$
$$\underbrace{\qquad\qquad\qquad\quad}_{f_{\tau, \sigma \mid \text{data}}}$$

$$f_{\tau, \sigma \mid \text{data}} \propto f_{\text{data} \mid \tau, \sigma} \, f_{\tau, \sigma}$$
$$\downarrow$$
$$f_{\text{data} \mid \beta, \sigma}$$
$$\uparrow$$

---

[← Bayesian Regularization](02-bayesian-regularization.md) · [Up: contents](index.md)
