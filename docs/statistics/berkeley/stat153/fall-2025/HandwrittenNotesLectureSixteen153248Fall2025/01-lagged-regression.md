---
title: Lagged Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureSixteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureSixteen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureSixteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureSixteen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lagged Regression

1. Lagged Regression
2. Neural Networks (RNN, LSTM)

or (Auto Regression)

$$
\begin{array}{ccccc}
\text{A} & \text{R} & \text{I} & \text{M} & \text{A} \\
\uparrow & & \uparrow & & \uparrow \\
\text{Auto} & \text{Regressive} & \text{Integrated} & \text{Moving} & \text{Average}
\end{array}
$$

$$(\text{AR}) + (\text{MA}) + (\text{I}) = \text{ARIMA}$$

## Auto Regression (AR)

Time series: $\boxed{y_1, \dots, y_n}$

Forecasting: $y_{n+1}, y_{n+2}, \dots, y_{n+k}$ for some $k$ we want to predict

$$y = X\beta + \varepsilon$$

(1) $y_t = \beta_0 + \beta_1 t + \beta_2 (t - c)_+ + \varepsilon_t$

$$
y = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix} \quad X = \begin{bmatrix} 1 & & \\ \vdots & t & (t-c)_+ \\ 1 & & \end{bmatrix}
$$

$\left. \begin{array}{l} \\ \\ \\ \\ \end{array} \right\} \text{Models that we studied so far. } X \text{ is made of } t.$

**Auto Regression**: $X$ is made of past values of $y$.

---

## AR(1) Model
$\downarrow$ **Order**

$$\boxed{y_t} = \phi_0 + \phi_1 \boxed{y_{t-1}} + \varepsilon_t,$$
$$\varepsilon_t \overset{iid}{\sim} N(0, \sigma^2) \qquad t = 2, 3, \dots, n$$

$$y = X\beta + \varepsilon$$

$$
y = \begin{pmatrix} y_2 \\ \vdots \\ y_n \end{pmatrix} \quad X = \begin{bmatrix} 1 & y_1 \\ \vdots & \vdots \\ 1 & y_{n-1} \end{bmatrix} \quad \beta = \begin{pmatrix} \phi_0 \\ \phi_1 \end{pmatrix}
$$

## AR(2)

$$y_t = \phi_0 + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \varepsilon_t,$$
$$t = 3, 4, \dots, n$$

$$
y = \begin{pmatrix} y_3 \\ \vdots \\ y_n \end{pmatrix} \quad X = \begin{bmatrix} 1 & y_2 & y_1 \\ \vdots & \vdots & \vdots \\ 1 & y_{n-1} & y_{n-2} \end{bmatrix}
$$

---

[Up: contents](index.md) · [AR($p$) →](02-ar.md)
