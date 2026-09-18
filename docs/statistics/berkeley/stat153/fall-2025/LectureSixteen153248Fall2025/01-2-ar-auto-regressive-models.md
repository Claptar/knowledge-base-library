---
title: 2 AR (Auto-Regressive) Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSixteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSixteen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureSixteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSixteen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 AR (Auto-Regressive) Models

### Lecture Sixteen
Fall 2025, UC Berkeley

Aditya Guntuboyina

October 23, 2025

## 1 Auto or Lagged Regression

Our next topic of study is AutoRegression. The main models here are called ARIMA. ARIMA is an acronym standing for Auto-Regressive Integrated Moving Average. We will first study Auto-Regressive (AR) models, then we shall include the MA part to get ARMA models, finally we see what "Integrated" means.

We observe time series $y_1, \dots, y_n$. AR models are simply linear regression models where the covariates are chosen to be past (or lagged) values of $y_t$.

The AR model of order $p$ (referred to by $AR(p)$) is given by
$$y_t = \phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t \tag{1}$$
for $t = p + 1, \dots, n$. In matrix notation,
$$Y = X\beta + \epsilon$$
where
$$Y = \begin{pmatrix} y_{p+1} \\ y_{p+2} \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix} \quad X = \begin{pmatrix} 1 & y_p & y_{p-1} & \cdot & \cdot & \cdot & y_1 \\ 1 & y_{p+1} & y_p & \cdot & \cdot & \cdot & y_2 \\ 1 & y_{p+2} & y_{p+1} & \cdot & \cdot & \cdot & y_3 \\ \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\ 1 & y_{n-1} & y_{n-2} & \cdot & \cdot & \cdot & y_{n-p} \end{pmatrix} \quad \beta = \begin{pmatrix} \phi_0 \\ \phi_1 \\ \phi_2 \\ \cdot \\ \cdot \\ \cdot \\ \phi_p \end{pmatrix} \quad \epsilon = \begin{pmatrix} \epsilon_{p+1} \\ \epsilon_{p+2} \\ \cdot \\ \cdot \\ \cdot \\ \epsilon_n \end{pmatrix}$$

This regression model is called AutoRegression because the responses as well as the covariates are both formed from the same time series: the time series $y_t$ is regressed on its own lagged values $y_{t-1}, \dots, y_{t-p}$.

The parameters $\phi_0, \dots, \phi_p$ are estimated in the usual way by minimizing $\|Y - X\beta\|^2$. Let the estimates by $\hat{\phi}_0, \dots, \hat{\phi}_p$.

AR models are useful for predicting future values of the time series. For predicting $y_{n+1}$, we plug $t = n + 1$ in (1) to get
$$y_{n+1} = \hat{\phi}_0 + \hat{\phi}_1 y_n + \hat{\phi}_2 y_{n-1} + \dots + \hat{\phi}_p y_{n+1-p}.$$
Note that $y_n, y_{n-1}, \dots, y_{n+1-p}$ are all observed and they are the last $p$ observations. For predicting $y_{n+2}$, we plug $t = n + 2$ in (1) to get
$$y_{n+2} = \hat{\phi}_0 + \hat{\phi}_1 y_{n+1} + \hat{\phi}_2 y_n + \dots + \hat{\phi}_p y_{n+2-p}.$$
In the above, $y_{n+1}$ is not observed. But we can replace it by the predicted value $\hat{y}_{n+1}$. This gives
$$y_{n+2} = \hat{\phi}_0 + \hat{\phi}_1 \hat{y}_{n+1} + \hat{\phi}_2 y_n + \dots + \hat{\phi}_p y_{n+2-p}.$$
More generally, we predict $y_{n+i}$ by the recursion
$$\hat{y}_{n+i} = \hat{\phi}_0 + \hat{\phi}_1 \hat{y}_{n+i-1} + \dots + \hat{\phi}_p \hat{y}_{n+i-p} \quad \text{for } i = 1, 2, \dots$$
where the recursion is initialized with
$$\hat{y}_j = y_j \quad \text{for } j = n, n - 1, \dots, n + 1 - p.$$

We will look at AR models in more details in the coming lectures. Today, we shall provide a motivation for their use through the sunspots dataset. This was how the AR models were originally invented by Yule [1].

---

[Up: contents](index.md) · [3 AR Models for the Sunspots Data →](02-3-ar-models-for-the-sunspots-data.md)
