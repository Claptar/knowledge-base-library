---
title: 4 Rewriting the Model in terms of $yt$
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFifteen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFifteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Rewriting the Model in terms of $yt$

The model (3) is written in terms of the DFT $b_j$. Because the original data can be written in terms of the DFT, we can convert (3) into a specification for the original data $y_t$. This will lead us to another model representation which is directly in terms of the original data $y_t$.

The key to this is the following formula which writes the data in terms of the DFT.
$$y_t = \frac{1}{n} \sum_{j=0}^{n-1} b_j \exp\left(\frac{2\pi i j t}{n}\right) \quad \text{for } t = 0, 1, \dots, n - 1. \tag{4}$$
We saw this formula previously in Lecture 8. It is known as the **Inverse DFT formula**.

The right hand side of (4) involves complex numbers ($b_j$ and $\exp(2\pi i j t/n)$). On the other hand, the left hand is the data $y_t$ which is always real. Below we change the right hand side in (4) to make it consist of only real terms.

We can rewrite the inverse DFT formula in the following way.
$$\begin{aligned}
y_t &= \frac{1}{n} \sum_{j=0}^{n-1} b_j \exp\left(\frac{2\pi i j t}{n}\right) \\
&= \frac{1}{n} \sum_{j=0}^{n-1} (\text{Re}(b_j) + i \text{Im}(b_j)) \left(\cos\left(\frac{2\pi j t}{n}\right) + i \sin\left(\frac{2\pi j t}{n}\right)\right) \\
&= \frac{1}{n} \sum_{j=0}^{n-1} \left(\text{Re}(b_j) \cos\left(\frac{2\pi j t}{n}\right) - \text{Im}(b_j) \sin\left(\frac{2\pi j t}{n}\right)\right) + i \frac{1}{n} \sum_{j=0}^{n-1} \left(\text{Re}(b_j) \sin\left(\frac{2\pi j t}{n}\right) + \text{Im}(b_j) \cos\left(\frac{2\pi j t}{n}\right)\right)
\end{aligned}$$
We can ignore the imaginary part above as the dataset consists of real numbers, and this leads to
$$\begin{aligned}
y_t &= \frac{1}{n} \sum_{j=0}^{n-1} \left(\text{Re}(b_j) \cos\left(\frac{2\pi j t}{n}\right) - \text{Im}(b_j) \sin\left(\frac{2\pi j t}{n}\right)\right) \\
&= \frac{b_0}{n} + \frac{1}{n} \sum_{j=1}^{n-1} \left(\text{Re}(b_j) \cos\left(\frac{2\pi j t}{n}\right) - \text{Im}(b_j) \sin\left(\frac{2\pi j t}{n}\right)\right)
\end{aligned}$$
We are assuming that $n$ is odd and that $m = (n - 1)/2$. We split the sum above into $j = 1, \dots, m$ and then $j = m + 1, \dots, n - 1$, and then use $b_{n-j} = \bar{b}_j$ or, equivalently, $\text{Re}(b_{n-j}) = \text{Re}(b_j)$ and $\text{Im}(b_{n-j}) = -\text{Im}(b_j)$. This gives
$$y_t = \frac{b_0}{n} + \sum_{j=1}^m \left(\frac{2\text{Re}(b_j)}{n} \cos\left(\frac{2\pi j t}{n}\right) + \frac{-2\text{Im}(b_j)}{n} \sin\left(\frac{2\pi j t}{n}\right)\right).$$
where we also used $\cos(2\pi(n - j)t/n) = \cos(2\pi j t/n)$ and $\sin(2\pi(n - j)t/n) = -\sin(2\pi j t/n)$.

In other words, when $n$ is odd and $m = (n - 1)/2$, we have
$$y_t = \beta_0 + \sum_{j=1}^m \left(\beta_{1j} \cos\frac{2\pi j t}{n} + \beta_{2j} \sin\frac{2\pi j t}{n}\right) \tag{5}$$
where, for $j = 1, \dots, m$,
$$\beta_0 = \frac{b_0}{n} \quad \beta_{1j} = \frac{2\text{Re}(b_j)}{n} \quad \beta_{2j} = -\frac{2\text{Im}(b_j)}{n} \tag{6}$$
The formula (5) holds for every dataset $y_0, \dots, y_{n-1}$. As a result, the model (3) is equivalent to (5) with
$$\beta_{1j} = \frac{2\text{Re}(b_j)}{n} \sim N\left(0, \frac{4}{n^2}\gamma_j^2\right) \quad \text{and} \quad \beta_{2j} = \frac{-2\text{Re}(b_j)}{n} \sim N\left(0, \frac{4}{n^2}\gamma_j^2\right).$$
The spectrum model therefore has the following three equivalent definitions:

- **Definition 1:** $\text{Re}(b_1), \text{Im}(b_1), \dots, \text{Re}(b_m), \text{Im}(b_m)$ are all independent with $\text{Re}(b_j), \text{Im}(b_j) \overset{\text{i.i.d}}{\sim} N(0, \gamma_j^2)$ for $j = 1, \dots, m$.

- **Definition 2:**
$$y_t = \beta_0 + \sum_{j=1}^m \left(\beta_{1j} \cos\frac{2\pi j t}{n} + \beta_{2j} \sin\frac{2\pi j t}{n}\right) \tag{7}$$
with $\beta_{11}, \beta_{21}, \beta_{12}, \beta_{22}, \dots, \beta_{1m}, \beta_{2m}$ all independent with
$$\beta_{1j}, \beta_{2j} \overset{\text{i.i.d}}{\sim} N(0, \tau_j^2).$$

- **Definition 3:** $I(j/n) = f(j/n)\eta_j$ with $\eta_j \overset{\text{i.i.d}}{\sim} \text{Exp}(1)$.

These two definitions are equivalent because of (5) and (6). The three sets of parameters $(\gamma_1^2, \dots, \gamma_m^2)$ and $(\tau_1^2, \dots, \tau_m^2)$ and $(f(1/n), \dots, f(m/n))$ are related via:
$$\frac{4\gamma_j^2}{n^2} = \tau_j^2 \iff \frac{2\gamma_j}{n} = \tau_j$$
which is because
$$\text{Re}(b_j) \sim N(0, \gamma_j^2) \implies \frac{2\text{Re}(b_j)}{n} \sim N\left(0, \frac{4\gamma_j^2}{n^2}\right),$$
and
$$f(j/n) = \frac{2\gamma_j^2}{n} = \frac{n\tau_j^2}{2} \quad \text{for } j = 1, \dots, m.$$

---

[← 3 Spectrum Model from DFT](02-3-spectrum-model-from-dft.md) · [Up: contents](index.md) · [5 Regularized Estimation →](04-5-regularized-estimation.md)
