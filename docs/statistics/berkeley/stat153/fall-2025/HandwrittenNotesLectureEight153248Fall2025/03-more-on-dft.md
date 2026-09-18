---
title: More on DFT
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEight153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureEight153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureEight153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEight153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# More on DFT

$$y_0, y_1, \dots, y_{n-1}$$
$$b_j = \sum_{t=0}^{n-1} y_t \exp\left(-2\pi i \frac{j}{n} t\right), \quad j = 0, 1, \dots, n-1$$

1. $b_0 = \sum_{t=0}^{n-1} y_t \quad \}$ uninteresting, always real

2. $b_j = \underbrace{\sum_{t=0}^{n-1} y_t \cos 2\pi \frac{j}{n} t}_{\text{Re}(b_j)} - i \underbrace{\sum_{t=0}^{n-1} y_t \sin 2\pi \frac{j}{n} t}_{\text{Im}(b_j)}$

Generally $b_j$ will be complex.
(Sometimes $b_j$ can be real e.g. $n$ even, $j = \frac{n}{2}$)

3.
$$\begin{aligned}
b_{n-j} &= \sum_{t=0}^{n-1} y_t \exp\left(-2\pi i \frac{n-j}{n} t\right) \\
&= \sum_{t=0}^{n-1} y_t \exp(-2\pi i t) \exp\left(2\pi i \frac{j}{n} t\right) \\
&= \sum_{t=0}^{n-1} y_t \exp\left(2\pi i \frac{j}{n} t\right) \\
&= \sum_{t=0}^{n-1} y_t \overline{\exp\left(-2\pi i \frac{j}{n} t\right)}
\end{aligned}$$

$$\begin{aligned}
e^{i\theta} &= \cos\theta + i\sin\theta \\
\overline{e^{i\theta}} &= \cos\theta - i\sin\theta \\
e^{i\theta} &= \overline{e^{-i\theta}}
\end{aligned}$$

---

$$= \sum_{t=0}^{n-1} \overline{y_t \exp\left(-2\pi i \frac{j}{n} t\right)} \quad \text{because } y_t \text{ is real}$$
$$= \overline{b_j}$$

Thus
$$b_{n-j} = \overline{b_j} \qquad \left\} \begin{array}{l} n=10 \\ j=5 \\ b_5 = \overline{b_5} \end{array} \right.$$

$n = 11$:
$$y_0, y_1, \dots, y_{10}$$
$$\underset{\substack{\uparrow \\ \text{real}}}{b_0}, \, \underbrace{b_1, \, b_2, \, b_3, \, b_4, \, b_5}_{\text{complex}}, \, \overline{b_5}, \, \overline{b_4}, \, \overline{b_3}, \, \overline{b_2}, \, \overline{b_1}$$

$$I\left(\frac{j}{n}\right) = \frac{|b_j|^2}{n}, \qquad I\left(\frac{6}{11}\right) = I\left(\frac{5}{11}\right)$$

$n = 10$:
$$b_0, \, b_1, \, b_2, \, b_3, \, b_4, \, \underset{\substack{\uparrow \\ \text{real}}}{b_5}, \, \overline{b_4}, \, \overline{b_3}, \, \overline{b_2}, \, \overline{b_1}$$

3. You can recover the data from the DFT.
$$b_0, \, b_1, \, b_2, \dots, b_{n-1}$$
$$y_t = \frac{1}{n} \sum_{j=0}^{n-1} b_j \exp\left(2\pi i \frac{j}{n} t\right) \to \text{\textbf{Inverse DFT}}$$
$$b_j = \sum_{t=0}^{n-1} y_t \exp\left(-2\pi i \frac{j}{n} t\right) \to \text{Defn of DFT}$$

---

---

[← Indexing starting at 0 vs 1](02-indexing-starting-at-0-vs-1.md) · [Up: contents](index.md) · [Proof of IDFT →](04-proof-of-idft.md)
