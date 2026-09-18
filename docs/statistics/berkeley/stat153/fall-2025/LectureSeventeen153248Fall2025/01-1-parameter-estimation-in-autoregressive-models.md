---
title: 1 Parameter Estimation in AutoRegressive Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeventeen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureSeventeen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Parameter Estimation in AutoRegressive Models

## Lecture Seventeen
### Fall 2025, UC Berkeley

### Aditya Guntuboyina

### October 28, 2025

We shall discuss parameter estimation in AR($p$) models. Recall that the AR($p$) is given by:
$$
y_t = \phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t \tag{1}
$$
for $t = p + 1, \dots, n$. In matrix notation,
$$
Y = X\beta + \epsilon
$$
where
$$
Y = \begin{pmatrix} y_{p+1} \\ y_{p+2} \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix} \quad
X = \begin{pmatrix}
1 & y_p & y_{p-1} & \cdot & \cdot & \cdot & y_1 \\
1 & y_{p+1} & y_p & \cdot & \cdot & \cdot & y_2 \\
1 & y_{p+2} & y_{p+1} & \cdot & \cdot & \cdot & y_3 \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
1 & y_{n-1} & y_{n-2} & \cdot & \cdot & \cdot & y_{n-p}
\end{pmatrix} \quad
\beta = \begin{pmatrix} \phi_0 \\ \phi_1 \\ \phi_2 \\ \cdot \\ \cdot \\ \cdot \\ \phi_p \end{pmatrix} \quad
\epsilon = \begin{pmatrix} \epsilon_{p+1} \\ \epsilon_{p+2} \\ \cdot \\ \cdot \\ \cdot \\ \epsilon_n \end{pmatrix}
$$
The AR($p$) can be seen as a spcial of the usual linear regression model where the covariate matrix $X$ as well as the response vector $y$ are both formed from a single data set $y_1, \dots, y_n$.

We shall discuss estimation of the parameters $\phi_0, \dots, \phi_p$ and $\sigma$ in AR($p$). For simplicity, let us first assume $p = 1$ (we shall revert to the more general case later). The AR(1) model is given by:
$$
y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t \quad \text{for } t = 2, \dots, n. \tag{2}
$$
Because of the close relation between AR($p$) models and linear regression, let us first revisit parameter estimation in usual linear regression.

---

[Up: contents](index.md) · [2 Detour: usual linear regression →](02-2-detour-usual-linear-regression.md)
