---
title: 3 Rewriting the Model in terms of $yt$
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFifteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFifteen153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFifteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFifteen153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Rewriting the Model in terms of $yt$

The model (1) is written in terms of the DFT $b_j$. Because the original data can be written in terms of the DFT, we can convert (1) into a specification for the original data $y_t$. This will lead us to the model representation that we already saw in Lecture 13.

The key to this is the following formula which writes the data in terms of the DFT.
$$
y_t = \frac{1}{n}\sum_{j=0}^{n-1} b_j \exp\left(\frac{2\pi i j t}{n}\right) \quad \text{for } t = 0, 1, \dots, n-1. \tag{3}
$$
We saw this formula previously in Lecture 8. It is known as the **Inverse DFT formula**.

The right hand side of (3) involves complex numbers ($b_j$ and $\exp(2\pi i j t/n)$). On the other hand, the left hand is the data $y_t$ which is always real. Below we change the right hand side in (3) to make it consist of only real terms.

We can rewrite the inverse DFT formula in the following way.
$$
y_t = \frac{1}{n}\sum_{j=0}^{n-1} b_j \exp\left(\frac{2\pi i j t}{n}\right)
$$
$$
= \frac{1}{n}\sum_{j=0}^{n-1} (\text{Re}(b_j) + i\text{Im}(b_j))\left(\cos\left(\frac{2\pi j t}{n}\right) + i\sin\left(\frac{2\pi j t}{n}\right)\right)
$$
$$
= \frac{1}{n}\sum_{j=0}^{n-1} \left(\text{Re}(b_j)\cos\left(\frac{2\pi j t}{n}\right) - \text{Im}(b_j)\sin\left(\frac{2\pi j t}{n}\right)\right) + i\frac{1}{n}\sum_{j=0}^{n-1} \left(\text{Re}(b_j)\sin\left(\frac{2\pi j t}{n}\right) + \text{Im}(b_j)\cos\left(\frac{2\pi j t}{n}\right)\right)
$$
We can ignore the imaginary part above as the dataset consists of real numbers, and this leads to
$$
y_t = \frac{1}{n}\sum_{j=0}^{n-1} \left(\text{Re}(b_j)\cos\left(\frac{2\pi j t}{n}\right) - \text{Im}(b_j)\sin\left(\frac{2\pi j t}{n}\right)\right)
$$
$$
= \frac{b_0}{n} + \frac{1}{n}\sum_{j=1}^{n-1} \left(\text{Re}(b_j)\cos\left(\frac{2\pi j t}{n}\right) - \text{Im}(b_j)\sin\left(\frac{2\pi j t}{n}\right)\right)
$$
We are assuming that $n$ is odd and that $m = (n-1)/2$. We split the sum above into $j = 1, \dots, m$ and then $j = m+1, \dots, n-1$, and then use $b_{n-j} = \bar{b}_j$ or, equivalently, $\text{Re}(b_{n-j}) = \text{Re}(b_j)$ and $\text{Im}(b_{n-j}) = -\text{Im}(b_j)$. This gives
$$
y_t = \frac{b_0}{n} + \sum_{j=1}^m \left(\frac{2\text{Re}(b_j)}{n}\cos\left(\frac{2\pi j t}{n}\right) + \frac{-2\text{Im}(b_j)}{n}\sin\left(\frac{2\pi j t}{n}\right)\right).
$$
where we also used $\cos(2\pi(n-j)t/n) = \cos(2\pi j t/n)$ and $\sin(2\pi(n-j)t/n) = -\sin(2\pi j t/n)$.

In other words, when $n$ is odd and $m = (n-1)/2$, we have
$$
y_t = \beta_0 + \sum_{j=1}^m \left(\beta_{1j}\cos\frac{2\pi j t}{n} + \beta_{2j}\sin\frac{2\pi j t}{n}\right) \tag{4}
$$
where, for $j = 1, \dots, m$,
$$
\beta_0 = \frac{b_0}{n} \quad \beta_{1j} = \frac{2\text{Re}(b_j)}{n} \quad \beta_{2j} = -\frac{2\text{Im}(b_j)}{n} \tag{5}
$$
The formula (4) holds for every dataset $y_0, \dots, y_{n-1}$. As a result, the model (1) is equivalent to (4) with
$$
\beta_{1j} = \frac{2\text{Re}(b_j)}{n} \sim N\left(0, \frac{4}{n^2}\gamma_j^2\right) \quad \text{and} \quad \beta_{2j} = \frac{-2\text{Re}(b_j)}{n} \sim N\left(0, \frac{4}{n^2}\gamma_j^2\right).
$$
The spectrum model therefore has the following two equivalent definitions:

- **Definition 1:** $\text{Re}(b_1), \text{Im}(b_1), \dots, \text{Re}(b_m), \text{Im}(b_m)$ are all independent with $\text{Re}(b_j), \text{Im}(b_j) \overset{\text{i.i.d}}{\sim} N(0, \gamma_j^2)$ for $j = 1, \dots, m$.
- **Definition 2:**
$$
y_t = \beta_0 + \sum_{j=1}^m \left(\beta_{1j}\cos\frac{2\pi j t}{n} + \beta_{2j}\sin\frac{2\pi j t}{n}\right) \tag{6}
$$
with $\beta_{11}, \beta_{21}, \beta_{12}, \beta_{22}, \dots, \beta_{1m}, \beta_{2m}$ all independent with
$$
\beta_{1j}, \beta_{2j} \overset{\text{i.i.d}}{\sim} N(0, \tau_j^2).
$$

These two definitions are equivalent because of (4) and (5). The two sets of parameters $\gamma_1^2, \dots, \gamma_m^2$ and $\tau_1^2, \dots, \tau_m^2$ are related via:
$$
\frac{4\gamma_j^2}{n^2} = \tau_j^2 \iff \frac{2\gamma_j}{n} = \tau_j.
$$
This is because
$$
\text{Re}(b_j) \sim N(0, \gamma_j^2) \implies \frac{2\text{Re}(b_j)}{n} \sim N\left(0, \frac{4\gamma_j^2}{n^2}\right).
$$
The power spectrum is given by:
$$
f(j/n) = \frac{2\gamma_j^2}{n} = \frac{n\tau_j^2}{2} \quad \text{for } 0 < \frac{j}{n} < \frac{1}{2}.
$$

## 4 Two key properties of the Spectrum Model

Consider Definition 2 of the spectrum model. We focus on two key properties of $\{y_t\}$. First, as noted in Lecture 13, the variance of $y_t$ can be written as
$$
\text{var}(y_t) = \sum_{j=1}^m \tau_j^2 = \frac{2}{n}\sum_{j=1}^m f(j/n) \approx 2\int_0^{1/2} f(\omega)d\omega.
$$
In other words, the variance of $y_t$ is closely approximated by twice the integral of the spectral density $f(\omega)$ over the interval $[0, 0.5]$.

Next consider the covariance between $y_t$ and $y_{t+h}$:
$$
\text{cov}(y_t, y_{t+h}) = \sum_{j=1}^m \tau_j^2 \cos\left(\frac{2\pi j h}{n}\right) = \frac{2}{n}\sum_{j=1}^m f(j/n)\cos\left(\frac{2\pi j h}{n}\right) \approx 2\int_0^{1/2} f(\omega)\cos(2\pi\omega h)d\omega.
$$
This shows that $\text{cov}(y_t, y_{t+h})$ can be nonzero, implying that $y_t$ and $y_{t+h}$ may be correlated. Consequently, the spectrum model naturally allows for dependence in $y_t$ across different time points, illustrating its ability to capture and represent temporal correlations.

## 5 The case of even $n$

We assumed that $n$ is odd (and $m = (n-1)/2$). If $n$ is even, then $1/2$ becomes a Fourier frequency and $b_{n/2}$ becomes real (because $\sin(\pi t) = 0$ for all $t$). In this case, we can simply avoid working with $1/2$ by taking $m = (n-2)/2$ and using the model:
$$
\text{Re}(b_j), \text{Im}(b_j) \overset{\text{i.i.d}}{\sim} N(0, \gamma_j^2) \quad \text{for } j = 1, \dots, m.
$$
This will be equivalent to (6). Basically everything will stay the same as before (only difference is that $m = (n-2)/2$). Here we are essentially forcing $\gamma_{n/2} = 0$. One can try to also try to estimate $\gamma_{n/2}$ using $b_{n/2} \sim N(0, \gamma_{n/2}^2)$ (as was done in Lab 7) but this approach is more complicated.

---

[← 1 Spectrum Model](01-1-spectrum-model.md) · [Up: contents](index.md)
