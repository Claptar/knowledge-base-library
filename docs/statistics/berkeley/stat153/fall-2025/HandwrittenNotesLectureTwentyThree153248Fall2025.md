---
title: Lecture Twenty-Three
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwentyThree153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureTwentyThree153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureTwentyThree153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwentyThree153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture Twenty-Three

**$\text{ARMA}(p, q)$**: $\phi(B)(y_t - \mu) = \theta(B)\varepsilon_t$

Causal-stationary regime: $\phi$ having roots all with modulus $> 1$

$\text{ARIMA}(\text{data}, \text{order} = (p, 0, q))$

**Preprocessing**: $y \to \underbrace{(I - B)y}_{y_t - y_{t-1}} \to (I - B)^2 y = y_t - 2y_{t-1} + y_{t-2}$

**$\text{ARIMA}(p, d, q)$**:
$$\phi(B)\left((I - B)^d y - \mu\right) = \theta(B)\varepsilon_t$$

$\to \begin{pmatrix} d \le 2 \\ p \le 5 \\ q \le 5 \end{pmatrix} \qquad d \quad \begin{matrix} (I - B)y \\ (I - B)^2 y \end{matrix}$

**Seasonal ARIMA**

Quite often, we deal with monthly data.

$(p, q)$
Sample ACF

---

(1) Seasonal ARMA models
(2) Multiplicative Seasonal ARMA models
(3) Seasonal ARIMA models (SARIMA models)

**Seasonal ARMA**

$\text{MA}(1)$: $y_t = \mu + \varepsilon_t + \theta \varepsilon_{t-1}$

$$\text{ACF}(h) = \begin{cases} 1 & \text{if } h = 0 \\ \frac{\theta}{1 + \theta^2} & \text{if } h = 1 \\ 0 & \text{if } |h| \ge 2 \end{cases}$$

Suppose we want:
$$\text{ACF}(h) = \begin{cases} 1 & \text{if } h = 0 \\ \frac{\theta}{1 + \theta^2} & \text{if } h = 12 \\ 0 & \text{for all other } h \end{cases}$$

$$y_t = \mu + \varepsilon_t + \theta \varepsilon_{t-12}$$

$$\text{Cov}(y_t, y_{t+h})$$
$$= \text{Cov}(\varepsilon_t + \theta \varepsilon_{t-12}, \, \varepsilon_{t+h} + \theta \varepsilon_{t+h-12})$$
$$\ne 0 \text{ only when } h = 0, 12, -12$$

---

$$\text{ACF}(h) = \begin{cases} 1 & h = 0 \\ \ne 0 & |h| = 12 \\ 0 & \text{for all other } h \end{cases}$$

$$\text{Seasonal MA}(1)_{12}$$

$\text{MA}(1)$:
$$y_t - \mu = \theta(B)\varepsilon_t$$
$$\theta(z) = 1 + \theta z$$

$\text{Seasonal MA}(1)$:
$$y_t - \mu = \theta(B^{12})\varepsilon_t$$
$$B^{12} y_t = y_{t-12}$$

$\text{ARMA}(p, q)$:
$$\phi(B)(y_t - \mu) = \theta(B)\varepsilon_t$$

**$\text{Seasonal ARMA}(p, q)$ with period $s$**
$$\phi(B^s)(y_t - \mu) = \theta(B^s)\varepsilon_t$$

$\text{ARMA}(p, q)$
ACF
PACF

---

**$\text{Seasonal ARMA}(p, q)$ with period $s$**
will have the same structure of ACF, PACF as regular $\text{ARMA}(p, q)$ but at lags that are multiples of $s$.

$\text{MA}(2)$:
ACF
PACF

$\text{Seasonal MA}(2)$ with period $s$

**CO2 data**: $\text{MA}(1)$
ACF

---

Seasonal $\text{MA}(1)$ with period $s=12$

**Multiplicative Seasonal ARMA models**

$$\left. \begin{array}{ll} y_t - \mu = \theta(B)\varepsilon_t & \to \text{regular } \text{MA}(1) \\ & \quad \theta(z) = 1 + \theta z \\ y_t - \mu = \Theta(B^s)\varepsilon_t & \to \text{seasonal } \text{MA}(1) \text{ with period } 12 \end{array} \right\}$$

$$y_t - \mu = \theta(B)\Theta(B^s)\varepsilon_t \quad \to$$

$$\text{MA}(1) \times \text{MA}(1)_{12}$$

$$y_t - \mu = (1 + \theta B)(1 + \Theta B^s)\varepsilon_t$$
$$y_t - \mu = \varepsilon_t + \theta \varepsilon_{t-1} + \Theta \varepsilon_{t-s} + \theta\Theta \varepsilon_{t-s-1}$$
$\to$ special case of $\text{MA}(13)$.

---

$\text{ACF}$ of $\text{MA}(1) \times \text{MA}(1)_{12}$

Check:
$$\text{ACF}(h) = \begin{cases} 1 & \text{if } h = 0 \\ \frac{\theta}{1 + \theta^2} & \text{if } h = 1 \\ \frac{\Theta}{1 + \Theta^2} & h = 12 \\ \frac{\theta\Theta}{(1 + \theta^2)(1 + \Theta^2)} & h = 11, 13 \end{cases}$$

$$\text{Cov}(\underbrace{\varepsilon_t + \theta \varepsilon_{t-1} + \Theta \varepsilon_{t-12} + \theta\Theta \varepsilon_{t-13}}_{y_t}, \, \underbrace{\varepsilon_{t+11} + \theta \varepsilon_{t+10} + \Theta \varepsilon_{t-1} + \theta\Theta \varepsilon_{t-2}}_{y_{t+11}})$$

$$\varepsilon_{t+13} + \theta \varepsilon_{t+12} + \Theta \varepsilon_{t+1} + \theta\Theta \varepsilon_t$$

---

## Multiplicative Seasonal ARMA

$$\left. \begin{array}{l} \text{ARMA}(p, q) \to \phi(B)(y_t - \mu) = \theta(B)\varepsilon_t \\ \begin{array}{l} \text{Seasonal} \\ \text{ARMA}(P, Q) \\ \text{with period } s \end{array} \to \Phi(B^s)(y_t - \mu) = \Theta(B^s)\varepsilon_t \end{array} \right\}$$

$$\phi(B)\Phi(B^s)(y_t - \mu) = \theta(B)\Theta(B^s)\varepsilon_t$$

**Heuristic for understanding ACF & PACF**

ACF
$\text{MA}(2) \times \text{MA}(2)_{12}$

PACF

## SARIMA Models

---

$\text{ARIMA}(\text{data}, \text{order} = (p, d, q), \text{seasonal order} = (P, D, Q, s))$

$$(I - B^s)^D (I - B)^d y_t = x_t \to \text{preprocessing}$$

$$\Phi(B^s)\phi(B)(x_t - \mu) = \Theta(B^s)\theta(B)\varepsilon_t$$

$$\Phi(B^s)\phi(B)\left((I - B^s)^D (I - B)^d y_t - \mu\right) = \Theta(B^s)\theta(B)\varepsilon_t$$

SARIMA

---

[Up: contents](index.md)
