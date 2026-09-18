---
title: 4 Complex Sinuoids and Orthogonality
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEight153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureEight153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Complex Sinuoids and Orthogonality

## 4.1 Complex Sinusoids

As we saw in the last lecture, sinusoids are linear combinations of $\cos(2\pi f t)$ and $\sin(2\pi f t)$. While doing algebra with sinusoids, it is very useful to represent them in terms of complex exponentials as:
$$\cos(2\pi f t) = \frac{1}{2}\exp(2\pi i f t) + \frac{1}{2}\exp(-2\pi i f t) \quad \text{and} \quad \sin(2\pi f t) = \frac{1}{2i}\exp(2\pi i f t) - \frac{1}{2i}\exp(-2\pi i f t)$$
In the last lecture, we saw that while dealing with sinusoids at integer valued time points $t$, we can restrict the frequency $f$ to $[0, 1/2]$. However, if we use the formulae above, note that we have to deal with $-f$ as well (because of the second term $e^{-2\pi i f t} = e^{2\pi i (-f)t}$) and $-f$ lies between $-1/2$ and $0$. Thus when discussing sinusoids in terms of complex exponentials $e^{2\pi i f t}, t = 0, 1, \dots, n - 1$, one takes $f \in [-0.5, 0.5)$ (note that $f = -0.5$ leads to the same $e^{2\pi i f t}$ as $f = 0.5$ so we drop $f = 0.5$ from consideration). For example, the function `np.fft.fftfreq(n)` gives all Fourier frequencies in $[-0.5, 0.5)$.

If one does not want to deal with negative frequencies, then we can use
$$e^{-2\pi i f t} = \cos(2\pi f t) - i\sin(2\pi f t) = \cos(2\pi (1 - f)t) + i\sin(2\pi(1 - f)t) = e^{2\pi i(1-f)t}$$
because $\cos(2\pi (1 - f)t) = \cos(2\pi t - 2\pi f t) = \cos(2\pi f t)$ (note $t$ is an integer) and $\sin(2\pi(1 - f)t) = \sin(2\pi t - 2\pi f t) = -\sin(2\pi f t)$.

Therefore, if we want to use complex exponentials $e^{2\pi i f t}$ but we do not want to deal with negative frequencies, then we can restrict $f$ to $[0, 1)$. From here on, whenever we consider the complex sinusoid $x_t = e^{2\pi i f t}$ for $t = 0, 1, \dots, n - 1$, we restrict $f \in [0, 1)$.

## 4.2 Complex Sinusoidal Vectors

For every $0 \le j \le (n - 1)$, let us define the $n \times 1$ vector
$$u^j = (1, \exp(2\pi i j/n), \exp(2\pi i 2j/n), \dots, \exp(2\pi i (n - 1)j/n))^T.$$
This vector can be interpreted as the complex sinusoid $e^{2\pi i f t}$ with Fourier frequency $f = j/n$ evaluated at the time points $t = 0, 1, \dots, (n - 1)$. It is easy to see that

1. When $j = 0$, we have $u^0 = (1, 1, \dots, 1)$.

2. When $1 \le j \le n - 1$, we have $u^j = \bar{u}^{n-j}$. Here $\bar{u}$ denotes complex conjugate of $u$ (the complex conjugate $\bar{u}$ of a vector $u$ is defined as the vector obtained by taking the complex conjugates of each entry of $u$).

The most important property of these complex valued vectors $u^0, u^1, \dots, u^{n-1}$ is orthogonality. Specifically, for $0 \le j \ne k \le n - 1$, we have
$$\langle u^j, u^k \rangle = 0. \tag{6}$$
Recall that the inner product between two complex valued vectors $a = (a_1, \dots, a_n)^T$ and $b = (b_1, \dots, b_n)^T$ is given by
$$\langle a, b \rangle = \sum_{j=1}^n a_j \bar{b}_j.$$
Note specially the complex conjugate of $b_j$ above.

Here is the proof of (6). Fix $0 \le j \ne k \le n - 1$ and write
$$\begin{aligned}
\langle u^j, u^k \rangle &= \sum_{t=0}^{n-1} \exp\left(2\pi i \frac{j}{n} t\right) \overline{\exp\left(2\pi i \frac{k}{n} t\right)} \\
&= \sum_{t=0}^{n-1} \exp\left(2\pi i \frac{j}{n} t\right) \exp\left(-2\pi i \frac{k}{n} t\right) \\
&= \sum_{t=0}^{n-1} \exp\left(2\pi i \frac{j - k}{n} t\right) \\
&= \sum_{t=0}^{n-1} \left[\exp\left(2\pi i \frac{j - k}{n}\right)\right]^t \\
&= \frac{1 - \left(\exp\left(2\pi i \frac{j - k}{n}\right)\right)^n}{1 - \exp\left(2\pi i \frac{j - k}{n}\right)} \\
&= \frac{1 - \exp(2\pi i(j - k))}{1 - \exp\left(2\pi i \frac{j - k}{n}\right)} \\
&= \frac{1 - \cos(2\pi(j - k)) - i\sin(2\pi(j - k))}{1 - \exp\left(2\pi i \frac{j - k}{n}\right)} = \frac{1 - 1 - 0}{1 - \exp\left(2\pi i \frac{j - k}{n}\right)} = 0
\end{aligned}$$
This proves (6). It is also easy to see that (just take $j = k$ in the above calculation and the answer can be found in the third line)
$$\langle u^j, u^j \rangle = \|u^j\|^2 = n.$$
Therefore the $n$ complex-valued vectors $u^0, u^1, \dots, u^{n-1}$ are orthogonal and they all have the same squared length equal to $n$. This immediately implies that they form a basis for the space $\mathbb{C}^n$ consisting of all complex-valued vectors of length $n$. In other words, every complex-valued vector of length $n$ can be written as a linear combination of $u^0, u^1, \dots, u^{n-1}$.

## 4.3 The Inverse DFT formula

The inverse DFT formula recovers the data $y_0, \dots, y_{n-1}$ from their DFT $b_0, \dots, b_{n-1}$. We derive this formula below.

The main observation is the following: Because $u^0, \dots, u^{n-1}$ form a basis, we can write any $n \times 1$ vector of complex entries:
$$y = (y_0, \dots, y_{n-1})^T$$
as a linear combination of $u^0, \dots, u^{n-1}$. More specifically, we can write
$$y = a_0 u^0 + a_1 u^1 + \dots + a_{n-1} u^{n-1} \tag{7}$$
Take the inner product of both sides of the above equation with $u^j$ for a fixed $j$ and use orthogonality so that $\langle u^j, u^k \rangle = 0$ for $k \ne j$ and the fact that $\langle u^j, u^j \rangle = n$ to obtain
$$a_j = \frac{1}{n} \langle y, u^j \rangle = \frac{1}{n} \sum_{t=0}^{n-1} y_t \exp\left(-\frac{2\pi i j t}{n}\right). \tag{8}$$
By the formula (4) for the DFT $b_j$, it is easy to see that $a_j = b_j/n$. As a consequence (7) becomes:
$$y = \frac{1}{n} (b_0 u^0 + b_1 u^1 + \dots + b_{n-1} u^{n-1}).$$
Writing the $t$-th entry on both sides, we get
$$y_t = \frac{1}{n} \sum_{j=0}^{n-1} b_j \exp\left(\frac{2\pi i j t}{n}\right) \quad \text{for each } t = 0, 1, \dots, n - 1. \tag{9}$$
This is the inverse DFT formula. Note that the inverse DFT formula (9) as well as the DFT definition (4) look similar; the differences being in the sign of the exponent in the complex exponential and the presence of the factor $1/n$ in (9).

---

[← 3 Basic Properties of the DFT](03-3-basic-properties-of-the-dft.md) · [Up: contents](index.md)
