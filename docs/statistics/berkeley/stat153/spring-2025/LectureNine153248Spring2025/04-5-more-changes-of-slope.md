---
title: 5 More Changes of Slope
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureNine153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureNine153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 5 More Changes of Slope

Suppose we want to introduce two break points for the regression line. This can be done via:
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
The MLE of $c = (c_1, c_2)$ is given by the minimizer of $RSS(c)$ over all $c = (c_1, c_2)$ with $c_1, c_2 \in \{1, \dots, n\}$, and
$$RSS(c) = \min_\beta \|y - X_c \beta\|^2.$$

One can numerically minimize $RSS(c)$ over all $c_1, c_2 \in \{1, \dots, n\}$. The posterior of $c$ becomes:
$$\pi(c \mid \text{data}) \propto \left(\frac{1}{RSS(c)}\right)^{(n-4)/2} |X_c^T X_c|^{-1/2}.$$
For more break points, one can consider:
$$y_t = \beta_0 + \beta_1 t + \sum_{j=1}^k \beta_{j+1} \text{ReLU}(t - c_j) + \epsilon_t.$$
Conceptually estimation and inference here proceed just as before with $X_c$ changed appropriately. But the method can become computationally expensive if $k \ge 4$.

---

[← 4 Posterior Sampling for Uncertainty Quantification](03-4-posterior-sampling-for-uncertainty-quantification.md) · [Up: contents](index.md)
