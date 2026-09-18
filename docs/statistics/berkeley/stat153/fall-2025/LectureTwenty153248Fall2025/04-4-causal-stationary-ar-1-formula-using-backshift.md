---
title: 4 Causal Stationary AR(1) formula using Backshift
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Causal Stationary AR(1) formula using Backshift

We derived the formula (3) by recursing the $\text{AR}(1)$ equation $y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t$ successively into the past (as in (2)) and taking the limit $M \to \infty$. This method is difficult to carry out for $\text{AR}(p)$ when $p \ge 2$. Instead there is an alternative method (using Backshift) of directly arriving at (3) from $y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t$. This alternative method is very easy to generalize to higher $p$.

Here is the description of the backshift method for $\text{AR}(1)$. We will tackle higher $p$ in the next section. First note that $\text{AR}(1)$ difference equation in backshift notation is
$$\phi(B)y_t = \phi_0 + \epsilon_t \quad \text{where } \phi(z) = 1 - \phi_1 z.$$

Thus we can formally write
$$y_t = \frac{1}{\phi(B)} (\phi_0 + \epsilon_t).$$

Using
$$\frac{1}{\phi(z)} = \frac{1}{1 - \phi_1 z} = 1 + \phi_1 z + \phi_1^2 z^2 + \phi_1^3 z^3 + \dots, \tag{9}$$
we obtain
$$y_t = (I + \phi_1 B + \phi_1^2 B^2 + \dots) (\phi_0 + \epsilon_t)$$
$$= (I + \phi_1 B + \phi_1^2 B^2 + \dots) \phi_0 + (I + \phi_1 B + \phi_1^2 B^2 + \dots) \epsilon_t$$
$$= (1 + \phi_1 + \phi_1^2 + \dots) \phi_0 + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j} = \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j}$$
which gives (3). This formal method is sometimes called Backshift Calculus and it works for higher order AR models as well.

---

[← 3 Backshift Notation](03-3-backshift-notation.md) · [Up: contents](index.md) · [5 AR(p) for $p \ge 1$ →](05-5-ar-p-for.md)
