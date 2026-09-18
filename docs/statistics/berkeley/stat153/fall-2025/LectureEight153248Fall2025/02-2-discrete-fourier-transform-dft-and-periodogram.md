---
title: 2 Discrete Fourier Transform (DFT) and Periodogram
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEight153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureEight153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Discrete Fourier Transform (DFT) and Periodogram

The periodogram $I(f)$ clearly can be rewritten as:
$$I(f) = \frac{1}{n} \left| \sum_{t=1}^n y_t \exp(-2\pi i f t) \right|^2.$$
The term inside the modulus sign above is almost the same as the Discrete Fourier Transform (DFT) of the data. There is only one difference which comes from changing the data indexing slightly. While discussing the DFT, it is a standard convention to write the data as $y_0, y_1, \dots, y_{n-1}$ (instead of $y_1, \dots, y_n$). In other words, we start the indexing with 0 (as in Python) as opposed to 1. With this indexing, the DFT is defined as follows.

The DFT of data $y_0, \dots, y_{n-1}$ is defined by:
$$b_j := \sum_{t=0}^{n-1} y_t \exp\left(-\frac{2\pi i j t}{n}\right) \quad \text{for } j = 0, 1, \dots, n - 1. \tag{4}$$
In words, $b_j$ is the dot product between the data and the complex sinusoid with frequency $f = j/n$. Note that the complex sinusoid with frequency $f$ is given by:
$$\exp(2\pi i f t) \quad \text{for } t = 0, 1, 2, \dots, n - 1.$$
The $n$ (possibly) complex numbers $b_0, b_1, \dots, b_{n-1}$ are collectively called the DFT of $y_0, \dots, y_{n-1}$. Typically, $y_0, \dots, y_{n-1}$ will represent observed time series data. It is important to note that even though $y_0, \dots, y_{n-1}$ are real-valued, their DFT $b_0, \dots, b_{n-1}$ can be complex-valued.

**More on indexing:** As mentioned previously, while defining the DFT, we index the data starting from zero. In the definition (4), the first data point (which is $y_0$) is being multiplied by $\exp(-2\pi i j(0)/n) = 1$, the second data point is being multiplied by $\exp(-2i\pi j/n)$ and, in general, the $t$-th data point is being multiplied by $\exp(-2i\pi j(t - 1)/n)$. If we instead define the DFT by:
$$\tilde{b}_j := \sum_{t=1}^n y_t \exp\left(-\frac{2\pi i j t}{n}\right),$$
then the $t$-th data point will be multiplied by $\exp(-2i\pi j t/n)$. $b_j$ and $\tilde{b}_j$ will be different and they will be related by:
$$b_j = \tilde{b}_j \exp\left(\frac{2\pi i j}{n}\right).$$
The multiplier $\exp(2\pi i j/n)$ above has modulus one which means that
$$|b_j| = |\tilde{b}_j|.$$
So if we are only looking at the moduli of the DFT terms (note the periodogram only involves the moduli of DFT), then it does not matter whether we index data starting with 0 or 1. The standard convention while studying the DFT is to index starting from 0.

The connection between the periodogram and the DFT is given by:
$$I(j/n) = \frac{|b_j|^2}{n} \quad \text{for } 0 < \frac{j}{n} < 1/2$$
and the connection between $RSS(j/n)$ and DFT is given by:
$$RSS(j/n) = \sum_t (y_t - \bar{y})^2 - 2I(j/n) \quad \text{for } 0 < j/n < 0.5.$$

It is important to note that the DFT can be calculated very efficiently. The DFT of $y = (y_0, \dots, y_{n-1})^T$ can be obtained in numpy using the command `np.fft.fft(y)`. Here fft stands for Fast Fourier Transform which is a special efficient algorithm for computing the DFT. Naively, it would seem that to compute the DFT would need $O(n^2)$ computation (for each of $n$ values of $j$, we have to compute $b_j$ which requires a sum over the dataset of size $n$), but the FFT algorithm exploits symmetry and redundancy in the complex exponentials to compute the DFT in only $O(n \log n)$ time. We will not be going over the details of the FFT algorithm in class.

---

[← 1 Recap from last lecture](01-1-recap-from-last-lecture.md) · [Up: contents](index.md) · [3 Basic Properties of the DFT →](03-3-basic-properties-of-the-dft.md)
