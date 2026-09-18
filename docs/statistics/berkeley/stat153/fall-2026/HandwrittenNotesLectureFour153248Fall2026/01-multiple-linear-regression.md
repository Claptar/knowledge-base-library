---
title: Multiple Linear Regression
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureFour153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/HandwrittenNotesLectureFour153248Fall2026.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureFour153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureFour153248Fall2026.pdf) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Multiple Linear Regression

$y$ : Response
$x_1, \dots, x_m$ : Covariates

Data: $(y_i, \boxed{x_{i1}, x_{i2}, \dots, x_{im}})$, $i = 1, \dots, n$

Response vector: $y = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix} \to n \times 1$

Covariate matrix:
$$X = \begin{bmatrix} 1 & x_{11} & x_{12} & \dots & x_{1m} \\ 1 & x_{21} & x_{22} & \dots & x_{2m} \\ \vdots & \vdots & \vdots & & \vdots \\ 1 & x_{n1} & x_{n2} & \dots & x_{nm} \end{bmatrix}$$
$$\downarrow$$
$$n \times (m+1)$$

**Time Series:** $y_t, \quad t = 1, \dots, n$

$$y = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}$$

(1) Use functions of time to construct $X$.
$$y_t = \boxed{\beta_0 + \beta_1 t + \beta_2 t^2} + \text{error}$$

$$X = \begin{bmatrix} 1 & \overset{t}{1} & \overset{t^2}{1^2} \\ 1 & 2 & 2^2 \\ \vdots & \vdots & \vdots \\ 1 & n & n^2 \end{bmatrix}$$

$$X = \begin{bmatrix} 1 & \cos \frac{2\pi t}{12} & \sin & \cos() \\ \vdots & & & \\ 1 & & & \end{bmatrix}$$

(2) Use lagged values of $y$ as covariates.
$$y_{t-1}, \quad y_{t-2}, \quad \dots, \quad y_{t-m}$$

$$X = \begin{bmatrix} 1 & y_0 & y_{-1} & \dots \\ 1 & y_1 & y_0 & \\ \vdots & \vdots & y_1 & \\ 1 & y_{n-1} & y_{n-2} & \end{bmatrix}$$

$y_1, \dots, y_n \qquad (m = 2)$

$$y = \begin{pmatrix} y_3 \\ \vdots \\ y_n \end{pmatrix}, \qquad X = \begin{bmatrix} 1 & y_2 & y_1 \\ 1 & \vdots & \vdots \\ \vdots & & \\ 1 & y_{n-1} & y_{n-2} \end{bmatrix}$$
$$(n-2)$$

$$\boxed{y, \quad X} \qquad \text{sm.OLS}(y, X)$$

---

---

[Up: contents](index.md) · [Frequentist Inference →](02-frequentist-inference.md)
