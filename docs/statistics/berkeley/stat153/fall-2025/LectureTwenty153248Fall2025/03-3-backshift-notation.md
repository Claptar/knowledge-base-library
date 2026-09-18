---
title: 3 Backshift Notation
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Backshift Notation

A convenient piece of notation used while working with AR and MA models is the Backshift notation. Let $B$ denote the backshift operator defined by
$$B y_t = y_{t-1}, B^2 y_t = y_{t-2}, B^3 y_t = y_{t-3}, \dots$$
and similarly
$$B \epsilon_t = \epsilon_{t-1}, B^2 \epsilon_t = \epsilon_{t-2}, B^3 \epsilon_t = \epsilon_{t-3}, \dots.$$
Also let $I$ denote the identity operator: $I y_t = y_t$. More generally, we can define polynomial functions of the Backshift operator by, for example,
$$(I + B + 3B^2)y_t = I y_t + B y_t + 3B^2 y_t = y_t + y_{t-1} + 3y_{t-2}.$$

In general, for every polynomial $f(z)$, we can define $f(B)$. One can even extend this notation to negative powers of $B$ which correspond to forward shifts. For example, $B^{-1}y_t = y_{t+1}$, $B^{-5}y_t = y_{t+5}$ and $(B^3 + 9B^{-2})y_t = y_{t-3} + 9y_{t+2}$ etc.

In this notation, the defining equation $y_t = \phi_0 + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \dots + \phi_p y_{t-p} + \epsilon_t$ for the $\text{AR}(p)$ model can be written as $\phi(B)y_t = \phi_0 + \epsilon_t$ for the polynomial $\phi(z) = 1 - \phi_1 z - \phi_2 z^2 - \dots - \phi_p z^p$.

The defining equation $y_t = \epsilon_t + \theta_1 \epsilon_{t-1}$ for the $\text{MA}(1)$ model can be written as $y_t = \theta(B)\epsilon_t$ for the polynomial $\theta(z) = 1 + \theta_1 z$.

The defining equation $y_t = \epsilon_t + \theta_1 \epsilon_{t-1} + \dots + \theta_q \epsilon_{t-q}$ for the $\text{MA}(q)$ model becomes $y_t = \theta(B)\epsilon_t$ for the polynomial $\theta(z) = 1 + \theta_1 z + \dots \theta_q z^q$.

---

[← 2 Stationarity of AR(1)](02-2-stationarity-of-ar-1.md) · [Up: contents](index.md) · [4 Causal Stationary AR(1) formula using Backshift →](04-4-causal-stationary-ar-1-formula-using-backshift.md)
