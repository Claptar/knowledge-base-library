---
title: 1 Smoothing the Periodogram
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFifteen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFifteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Smoothing the Periodogram

### Lecture Fifteen
Fall 2025, UC Berkeley

Aditya Guntuboyina

October 16, 2025

Consider a time series dataset $y_0, \dots, y_{n-1}$. One of most common tools in time data analysis is the periodogram. It is given by:
$$I(j/n) := \frac{|b_j|^2}{n} \quad \text{for } 0 < \frac{j}{n} < 1/2$$
where $b_j$ is the Discrete Fourier Transform (DFT) defined by
$$b_j := \sum_{t=0}^{n-1} y_t \exp\left(-\frac{2\pi i j t}{n}\right).$$
Let us assume that $n$ is odd and $m = (n - 1)/2$. Then the periodogram ordinate is defined for $j = 1, \dots, m$.

The periodogram shows which frequency components contribute most strongly to the behaviour of the observed time series. It is useful for identifying the dominant cyclical patterns or periodicities within a dataset.

For most real datasets, the periodogram appears rough and noisy, especially when looking at its plot on the log-scale (i.e., when looking at the plot of log-periodogram). In such cases, researchers attempt to smooth the periodogram to get a clean summary of the trend in the periodogram without getting distracted by noise. What is a good way of smoothing the periodogram?

A nice way of smoothing is via the use of an appropriate model. Previously, we saw for estimating a smooth trend function, say $\mu_t$, from observed time series data $y_t$, a natural model is:
$$y_t = \mu_t + \epsilon_t \quad \text{with } \epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2).$$
We can try to use a similar model for the periodogram. Modeling $I(j/n)$ as a smooth trend function plus Gaussian noise does not make much sense for multiple reasons: (a) the periodogram is a positive quantity so using the normal distribution may not be a good idea, (b) the noise in the periodogram is more pronounced on the log-scale so we should probably use an additive noise model for the log-periodogram as opposed to the periodogram directly. In other words, we should use a multiplicative noise model for the periodogram.

The model that we shall use here is:
$$I(j/n) = f(j/n)\eta_j \quad \text{for } j = 1, \dots, m.$$
where $f(j/n)$ is a smooth function that represents the trend in the periodogram, and
$$\eta_j \overset{\text{i.i.d}}{\sim} \frac{1}{2}\chi_2^2.$$
$\chi_2^2$ is the chi-squared distribution with 2 degrees of freedom; its density is given by:
$$f_{\chi_2^2}(x) := \frac{1}{2}\exp(-x/2)I\{x > 0\}.$$
The density of $\chi_2^2/2$ is then given by:
$$f_{\chi_2^2/2}(x) = 2f_{\chi_2^2}(2x) = \exp(-x)I\{x > 0\}.$$
The above is the density of the Standard Exponential Distribution (the exponential distribution $\text{Exp}(\lambda)$ has density $\lambda e^{-\lambda x}I\{x > 0\}$; the above corresponds to $\lambda = 1$). Thus
$$\frac{\chi_2^2}{2} = \text{Exp}(1).$$
Our model can therefore also be written as:
$$I(j/n) = f(j/n)\eta_j \quad \text{with } \eta_j \overset{\text{i.i.d}}{\sim} \text{Exp}(1). \tag{1}$$
This is a multiplicative noise model. We can rewrite it in additive form by taking logarithms:
$$\log I(j/n) = \log f(j/n) + \log \eta_j \quad \text{with } \eta_j \overset{\text{i.i.d}}{\sim} \text{Exp}(1). \tag{2}$$
The noise in this additive representation is captured by the terms $\log \eta_j$, $1 \le j \le n$. These variables do not have mean zero (from the internet $\mathbb{E} \log \eta_j \approx -0.5772$). Therefore $\log f(j/n)$ does the represent the mean of $\log I(j/n)$ (in fact, it is strictly larger than the mean of $\log I(j/n)$). Rather, $f(j/n)$ represents the mean of $I(j/n)$.

We shall refer to (1) or (2) as the Spectrum Model.

## 2 Power Spectral Density

Since the mean of the $\text{Exp}(1)$ distribution equals 1, the mean of $I(j/n)$ in the Spectrum Model (1) is given by $f(j/n)$. This quantity is known as the **power of frequency $j/n$**:
$$f(j/n) := \text{power of frequency } j/n = \text{mean of } I(j/n) \text{ in model } (1).$$
If we plot the points $(j/n, f(j/n))$ for $j = 1, \dots, m$ and join the neighboring points by lines, we get a continuous function plot. This function is known as the **power spectral density** and is defined on $[0, 0.5]$.

This definition of the power spectral density is not rigorous. For a rigorous treatment, see any book on time series (e.g., Chapter 4 of Shumway and Stoffer; or the book "Spectral Analysis for Univariate Time Series" by Percival and Walden).

Note that the power spectral density is not a probability density function in the sense that it does not integrate to one.

---

[Up: contents](index.md) · [3 Spectrum Model from DFT →](02-3-spectrum-model-from-dft.md)
