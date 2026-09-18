---
title: 2 On the formulae for stationary AR(1)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyOne153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyOne153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentyOne153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyOne153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 On the formulae for stationary AR(1)

Above, we first wrote down the formulae (3) and (4) for stationary $\text{AR}(1)$ and then verified that they indeed satisfy the $\text{AR}(1)$ equation. It turns that these formulae can be derived by "solving" the $\text{AR}(1)$ equation (1) for $y_t$ in terms of $\{\epsilon_t\}$. We shall present this solution method here. We will not present a rigorous justification for this method (which can be found, for example, in the book "Time Series: theory and methods" by Brockwell and Davis).

Before describing this solution method, we need to introduce the backshift notation.

## 2.1 Backshift Notation

A convenient piece of notation used while working with AR and MA models is the Backshift notation. Let $B$ denote the backshift operator defined by
$$
B y_t = y_{t-1}, B^2 y_t = y_{t-2}, B^3 y_t = y_{t-3}, \dots
$$
and similarly
$$
B \epsilon_t = \epsilon_{t-1}, B^2 \epsilon_t = \epsilon_{t-2}, B^3 \epsilon_t = \epsilon_{t-3}, \dots.
$$
Also let $I$ denote the identity operator: $I y_t = y_t$. More generally, we can define polynomial functions of the Backshift operator by, for example,
$$
(I + B + 3B^2) y_t = I y_t + B y_t + 3B^2 y_t = y_t + y_{t-1} + 3y_{t-2}.
$$
In general, for every polynomial $f(z)$, we can define $f(B)$. One can even extend this notation to negative powers of $B$ which correspond to forward shifts. For example, $B^{-1}y_t = y_{t+1}$, $B^{-5}y_t = y_{t+5}$ and $(B^3 + 9B^{-2})y_t = y_{t-3} + 9y_{t+2}$ etc.

In this notation, the defining equation $y_t = \phi_0 + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \dots + \phi_p y_{t-p} + \epsilon_t$ for the $\text{AR}(p)$ model can be written as $\phi(B)y_t = \phi_0 + \epsilon_t$ for the polynomial $\phi(z) = 1 - \phi_1 z - \phi_2 z^2 - \dots - \phi_p z^p$.

The defining equation $y_t = \epsilon_t + \theta \epsilon_{t-1}$ for the $\text{MA}(1)$ model can be written as $y_t = \theta(B)\epsilon_t$ for the polynomial $\theta(z) = 1 + \theta_1 z$.

The defining equation $y_t = \epsilon_t + \theta_1 \epsilon_{t-1} + \dots + \theta_q \epsilon_{t-q}$ for the $\text{MA}(q)$ model becomes $y_t = \theta(B)\epsilon_t$ for the polynomial $\theta(z) = 1 + \theta_1 z + \dots \theta_q z^q$.

## 2.2 AR(1) solutions using Backshift Calculus

The two stationary solutions (3) and (4) to the $\text{AR}(1)$ difference equation (1) for the two cases $|\phi_1| < 1$ and $|\phi_1| > 1$ can also be derived using formal operations that are sometimes known as Backshift Calculus. This is described in this section. First note that (1) can be written as
$$
\phi(B)y_t = \phi_0 + \epsilon_t \quad \text{where } \phi(z) = 1 - \phi_1 z.
$$
Thus we can formally write
$$
y_t = \frac{1}{\phi(B)} (\phi_0 + \epsilon_t).
$$
Using
$$
\frac{1}{\phi(z)} = \frac{1}{1 - \phi_1 z} = 1 + \phi_1 z + \phi_1^2 z^2 + \phi_1^3 z^3 + \dots,
$$
we obtain
$$
\begin{aligned}
y_t &= (I + \phi_1 B + \phi_1^2 B^2 + \dots)(\phi_0 + \epsilon_t) \\
&= (I + \phi_1 B + \phi_1^2 B^2 + \dots)\phi_0 + (I + \phi_1 B + \phi_1^2 B^2 + \dots)\epsilon_t \\
&= (1 + \phi_1 + \phi_1^2 + \dots)\phi_0 + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j} = \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j}
\end{aligned}
$$
which gives (3).

When $|\phi_1| > 1$, the process (3) does not make sense. So we expand $1/\phi(z)$ in the following alternative way:
$$
\begin{aligned}
\frac{1}{\phi(z)} &= \frac{1}{1 - \phi_1 z} \\
&= \frac{-1}{\phi_1 z} \left( 1 - \frac{1}{\phi_1 z} \right)^{-1} \\
&= \frac{-1}{\phi_1 z} \left( 1 + \frac{1}{\phi_1 z} + \frac{1}{\phi_1^2 z^2} + \dots \right) = -\frac{z^{-1}}{\phi_1} - \frac{z^{-2}}{\phi_1^2} - \frac{z^{-3}}{\phi_1^3} - \dots.
\end{aligned}
$$
We thus get
$$
\begin{aligned}
y_t &= \frac{1}{\phi(B)} (\phi_0 + \epsilon_t) \\
&= \left( -\frac{B^{-1}}{\phi_1} - \frac{B^{-2}}{\phi_1^2} - \frac{B^{-3}}{\phi_1^3} - \dots \right)(\phi_0 + \epsilon_t) = \frac{\phi_0}{1 - \phi_1} - \sum_{j=1}^\infty \frac{\epsilon_{t+j}}{\phi_1^j}
\end{aligned}
$$
which gives (4). This formal method is called Backshift Calculus and it works for higher order AR models as well.

---

[← 1 Stationarity of AR(1)](01-1-stationarity-of-ar-1.md) · [Up: contents](index.md) · [3 Stationary and Causality for AR(p), $p \geq 2$ →](03-3-stationary-and-causality-for-ar-p.md)
