---
title: 3 Basic Properties of the DFT
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEight153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureEight153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Basic Properties of the DFT

Here are some basic things to note about the DFT (defined in (4)).

1. $b_0$ is always equal to $y_0 + \dots + y_{n-1}$. To see this, just plug in $j = 0$ in (4).

2. In general $b_j$ is a complex number with real and imaginary parts given by:
$$\text{real part of } b_j = \sum_{t=0}^{n-1} y_t \cos\left(\frac{2\pi j t}{n}\right) \quad \text{and imaginary part of } b_j = -\sum_{t=0}^{n-1} y_t \sin\left(\frac{2\pi j t}{n}\right)$$
Sometimes the imaginary part will be zero (for example, when $n$ is even and $j = n/2$) but, in general, $b_j$ will be complex-valued.

3. For each $j = 1, \dots, n - 1$, the DFT term $b_{n-j}$ equals the complex conjugate of $b_j$:
$$b_{n-j} = \bar{b}_j. \tag{5}$$
The reason for the above is
$$b_{n-j} = \sum_t y_t \exp\left(-\frac{2\pi i (n - j)t}{n}\right) = \sum_t y_t \exp\left(\frac{2\pi i j t}{n}\right) \exp(-2\pi i t) = \bar{b}_j,$$
where, in the above, we used that $\exp(-2\pi i t) = 1$ (because $t$ is an integer) and that $\exp\left(\frac{2\pi i j t}{n}\right)$ is the complex conjugate of $\exp\left(-\frac{2\pi i j t}{n}\right)$. Note that, for the above argument, it is crucial that $y_0, \dots, y_{n-1}$ are real. If some of $y_0, \dots, y_{n-1}$ are complex, the relation (5) is no longer true.

Because of (5), the DFT terms for later indices $j$ can be determined as complex conjugates for the DFT terms for earlier indices. For example, when $n = 11$, the DFT can be written as:
$$b_0, b_1, b_2, b_3, b_4, b_5, \bar{b}_5, \bar{b}_4, \bar{b}_3, \bar{b}_2, \bar{b}_1,$$
and, for $n = 12$, it is
$$b_0, b_1, b_2, b_3, b_4, b_5, b_6 = \bar{b}_6, \bar{b}_5, \bar{b}_4, \bar{b}_3, \bar{b}_2, \bar{b}_1.$$
Note that when $n = 12$, the term $b_6$ is necessarily real because $b_6 = \bar{b}_6$.

Thus when $n = 11$, the data consists of 11 real numbers while the DFT consists of one real number ($b_0$) and 5 complex numbers. On the other hand, when $n = 12$, the data consists of 12 real numbers while the DFT consists of two real numbers ($b_0$ and $b_6$) and 5 complex numbers.

It turns out that the data $y_0, y_1, \dots, y_{n-1}$ can be recovered from the DFT $b_0, \dots, b_{n-1}$ using a simple formula (this formula is sometimes known as the inverse DFT formula). Before seeing this, it is necessary to understand orthogonality properties of complex sinusoids with Fourier frequencies.

---

[← 2 Discrete Fourier Transform (DFT) and Periodogram](02-2-discrete-fourier-transform-dft-and-periodogram.md) · [Up: contents](index.md) · [4 Complex Sinuoids and Orthogonality →](04-4-complex-sinuoids-and-orthogonality.md)
