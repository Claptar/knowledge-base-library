---
title: Indexing starting at 0 vs 1
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEight153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureEight153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureEight153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEight153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Indexing starting at 0 vs 1

$$b_j = \sum_{t=0}^{n-1} y_t \exp\left(-2\pi i \frac{j}{n} t\right)$$
$$\tilde{b}_j = \sum_{t=1}^n y_t \exp\left(-2\pi i \frac{j}{n} t\right)$$

$$b_j = \underset{\text{point}}{\text{first data}} \times e^{-2\pi i \frac{j}{n}(0)} + \underset{\text{point}}{\text{2nd data}} \, e^{-2\pi i \frac{j}{n}(1)} + \dots + \underset{\text{point}}{t^{\text{th}}\text{ data}} \, e^{-2\pi i \frac{j}{n}(t-1)} + \dots$$

$$\tilde{b}_j = \underset{\text{point}}{\text{first data}} \times e^{-2\pi i \frac{j}{n}(1)} + \underset{\text{point}}{\text{2nd data}} \, e^{-2\pi i \frac{j}{n}(2)} + \dots + \underset{\text{point}}{t^{\text{th}}\text{ data}} \, e^{-2\pi i \frac{j}{n} t} + \dots$$

---

$$b_j = \tilde{b}_j \exp\left(\frac{2\pi i j}{n}\right)$$
Check then $|b_j| = |\tilde{b}_j|$

$$b_j = \sum_{t=0}^{n-1} y_t \exp\left(-2\pi i \frac{j}{n} t\right), \quad j = 0, 1, \dots, n-1$$

$(b_0, \dots, b_{n-1})$ is called the DFT of $y_0, \dots, y_{n-1}$

**Note:** Data $y_0, \dots, y_{n-1}$ are always real but the DFT $b_j$ can be complex

$$I\left(\frac{j}{n}\right) = \frac{|b_j|^2}{n} \quad \text{for } 0 < \frac{j}{n} < \frac{1}{2}$$

$$RSS\left(\frac{j}{n}\right) = \sum (y_t - \bar{y})^2 - 2\, I\left(\frac{j}{n}\right)$$

**IMPORTANT:** DFT $b_j, \, j = 0, 1, \dots, n-1$ can be computed efficiently by the **FFT algorithm**. (COOLEY & TUKEY, $O(n\log n)$)
**FAST FOURIER TRANSFORM**

$$n=4 \qquad n=2$$

---

---

[← Recap from last lecture](01-recap-from-last-lecture.md) · [Up: contents](index.md) · [More on DFT →](03-more-on-dft.md)
