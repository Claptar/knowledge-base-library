---
title: ARIMA models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwentyTwo153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureTwentyTwo153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureTwentyTwo153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwentyTwo153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# ARIMA models

$$
p, d, q
$$

$y_t$ is $\text{ARIMA}(p, d, q)$ if $(I - B)^d y_t$ is $\text{ARMA}(p, q)$

$$
\phi(B)\{(I - B)^d y_t - \mu\} = \theta(B)\varepsilon_t
$$

Difference $y_t$:
$$
y_t - y_{t-1}
$$
$$
\nabla y_t = y_t - y_{t-1} = (I - B)y_t
$$

$$
(I - B) y_t = y_t - y_{t-1}
$$
$$
\begin{aligned}
(I - B)^2 y_t &= (I - 2B + B^2)y_t \\
&= \mathbf{y_t - 2y_{t-1} + y_{t-2}}
\end{aligned}
$$

---

$$
\begin{aligned}
(I - B)((I - B)y_t) &= (I - B)(y_t - y_{t-1}) \\
&= (I - B)y_t - (I - B)y_{t-1} \\
&= (y_t - y_{t-1}) - (y_{t-1} - y_{t-2})
\end{aligned}
$$

$$
\begin{matrix}
y : \text{GNP} \\
\log y \\
(I - B)(\log y) \\
\text{AR}(2)
\end{matrix}
\qquad \longrightarrow \qquad
\begin{matrix}
y : \text{GNP} \\
\log y \\
\text{ARIMA}(2, 1, 0)
\end{matrix}
$$

$$
\{\text{arima}(\log y_t, \text{order} = (2, 1, 0), \text{trend} = \text{'t'})
$$

($d = 1$) $\text{ARIMA}(p, 1, q)$

$$
\phi(B)(\nabla y_t - \mu) = \theta(B)\varepsilon_t
$$

$$
\nabla y_t = \mu + \eta_t
$$
$\eta_t \sim \text{ARMA}(p, q)$ with mean $0$

$$
\begin{aligned}
y_1 - y_0 &= \mu + \eta_1 \\
y_2 - y_1 &= \mu + \eta_2
\end{aligned}
$$

---

$$
y_n - y_{n-1} = \mu + \eta_n
$$

$$
y_t = y_0 + t\mu + (\eta_1 + \dots + \eta_t)
$$

$$
\to y_t = \mathbf{y_0} + \mathbf{t\mu} + \gamma_t \quad \text{where } \nabla \gamma_t = \text{ARMA}(p, q) \text{ with zero mean}
$$
$\uparrow$
$\text{trend} = \text{'t'}$ model ($d = 1$)

$$
y_t = y_0 + \gamma_t \quad \text{where } \nabla \gamma_t = \text{ARMA}(p, q) \text{ with zero mean}
$$
$\text{trend} = \text{'c'}$ Default : $\mu = 0$ when $d = 1$ or more

SARIMA
$\downarrow$
Seasonal

---

[← ARMA $(p, q)$](01-arma.md) · [Up: contents](index.md)
