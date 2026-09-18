---
title: 3 Other Nonlinear Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNine153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureNine153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureNine153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNine153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Other Nonlinear Models

Our methodology for inference in these sinusoid models also extends to other similar nonlinear regression models. For example, consider the following model which is applicable when we want to introduce two break points for the regression line:
$$y_t = \beta_0 + \beta_1 t + \beta_2 \text{ReLU}(t - c_1) + \beta_3 \text{ReLU}(t - c_2) + \epsilon_t$$
with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. This model can also be written as
$$y = X_c \beta + \epsilon$$
where $c = (c_1, c_2)$ and
$$X_c := \begin{pmatrix}
1 & 1 & \text{ReLU}(1 - c_1) & \text{ReLU}(1 - c_2) \\
1 & 2 & \text{ReLU}(2 - c_1) & \text{ReLU}(2 - c_2) \\
1 & 3 & \text{ReLU}(3 - c_1) & \text{ReLU}(3 - c_2) \\
\cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot \\
1 & n & \text{ReLU}(n - c_1) & \text{ReLU}(n - c_2)
\end{pmatrix}$$
We estimate $c = (c_1, c_2)$ by minimizing $RSS(c)$ over all $c = (c_1, c_2)$ with $c_1, c_2 \in [1, n]$, and
$$RSS(c) = \min_\beta \|y - X_c \beta\|^2.$$
One can numerically minimize $RSS(c)$ over all $c_1, c_2 \in [1, n]$. A natural grid one can use here is $\{1, \dots, n\}$.

The posterior of $c$ becomes:
$$\pi(c \mid \text{data}) \propto \left(\frac{1}{RSS(c)}\right)^{(n-4)/2} |X_c^T X_c|^{-1/2}.$$
For more break points, one can consider:
$$y_t = \beta_0 + \beta_1 t + \sum_{j=1}^k \beta_{j+1} \text{ReLU}(t - c_j) + \epsilon_t.$$
Conceptually estimation and inference here proceed just as before with $X_c$ changed appropriately. But the method can become computationally expensive if $k \ge 4$.

---

[← 2 Sinusoidal Models with more frequencies](02-2-sinusoidal-models-with-more-frequencies.md) · [Up: contents](index.md)
