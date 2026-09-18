---
title: 1 Spectrum Model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFifteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFifteen153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFifteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFifteen153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Spectrum Model

### Lecture Fifteen
Spring 2025, UC Berkeley

Aditya Guntuboyina

March 11, 2025

In the last lecture, we looked at the spectral model for a given time series dataset $y_0, \dots, y_{n-1}$. In terms of the DFT $b_0, \dots, b_{n-1}$, the model is given by:
$$
\text{Re}(b_j), \text{Im}(b_j) \overset{\text{i.i.d}}{\sim} N(0, \gamma_j^2) \tag{1}
$$
for $j = 1, \dots, m$ where $m = (n-1)/2$ (we are assuming that $n$ is odd). The unknown parameters in this model are $\gamma_1^2, \dots, \gamma_m^2$ and $\gamma_j$ represents the strength of sinusoids at frequency $j/n$.

The likelihood corresponding to (1) is proportional to:
$$
\prod_{j=1}^m \frac{1}{\gamma_j} \exp\left(-\frac{(\text{Re}(b_j))^2}{2\gamma_j^2}\right) \frac{1}{\gamma_j} \exp\left(-\frac{(\text{Im}(b_j))^2}{2\gamma_j^2}\right)
$$
$$
= \prod_{j=1}^m \frac{1}{\gamma_j^2} \exp\left(-\frac{(\text{Re}(b_j))^2 + (\text{Im}(b_j))^2}{2\gamma_j^2}\right) = \prod_{j=1}^m \frac{1}{\gamma_j^2} \exp\left(-\frac{|b_j|^2}{2\gamma_j^2}\right).
$$
Therefore the likelihood depends on the squared magnitudes $|b_j|^2$ of the DFT coefficients. Recall that the periodogram $I(j/n)$ is defined as
$$
I(j/n) := \frac{|b_j|^2}{n}.
$$
We can therefore rewrite the likelihood in terms of the periodogram as follows:
$$
\prod_{j=1}^m \frac{1}{\gamma_j^2} \exp\left(-\frac{nI(j/n)}{2\gamma_j^2}\right). \tag{2}
$$
This likelihood depends on the data only through the periodogram ordinates $I(j/n)$ for $j = 1, \dots, m$. Therefore the periodogram forms the sufficient statistic in this model. Under (7), we have
$$
I(j/n) = \frac{1}{n}|b_j|^2 = \frac{1}{n}\left((\text{Re}(b_j))^2 + (\text{Im}(b_j))^2\right) \sim \frac{\gamma_j^2}{n}\chi_2^2.
$$
The model can therefore be written directly in terms of the periodogram as
$$
I(j/n) \overset{\text{ind}}{\sim} \frac{\gamma_j^2}{n}\chi_2^2 \quad \text{for } j = 1, \dots, m.
$$

We can write the likelihood for the above model in terms of the periodogram and this would be proportional to (8). Note also that $\chi_2^2$ distribution with two degrees of freedom actually coincides with the Exponential distribution with $\lambda$ parameter equal to $1/2$.

Model (1) does not care so much about the individual DFT coefficients $b_j$ but only their magnitude.

The negative log-likelihood corresponding to (8) is
$$
\sum_{j=1}^m \left(2\log \gamma_j + \frac{nI(j/n)}{2\gamma_j^2}\right).
$$
For optimization purposes we work with the logarithms of $\gamma_j$. Let $\alpha_j = \log \gamma_j$. The negative log-likelihood in terms of $\alpha_j$ is
$$
\sum_{j=1}^m \left(2\alpha_j + \frac{nI(j/n)}{2}e^{-2\alpha_j}\right).
$$
If we directly minimize the above with respect to $\alpha_j$ (without any additional regularization), we get
$$
\alpha_j = \log \sqrt{\frac{nI(j/n)}{2}} \quad \text{and} \quad \gamma_j^2 = e^{2\alpha_j} = \frac{nI(j/n)}{2}.
$$
This basically means that the $\gamma_j^2$ parameters fully interpolate the periodogram leading to full overfitting. For more meaningful estimation, we need to add regularization. If we assume smoothness of $\alpha_j$, we can add the penalty $\sum_{j=2}^{m-1} ((\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}))^2$ or $\sum_{j=2}^{m-1} |(\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1})|$ to the negative log-likelihood. This leads to the estimators $\hat{\alpha}_t^{\text{ridge}}(\lambda)$ and $\hat{\alpha}_t^{\text{lasso}}(\lambda)$ which are defined as the minimizers of
$$
\sum_{j=1}^m \left(2\alpha_j + \frac{nI(j/n)}{2}e^{-2\alpha_j}\right) + \lambda \sum_{j=2}^{m-1} ((\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}))^2
$$
and
$$
\sum_{t=1}^n \left(2\alpha_j + \frac{nI(j/n)}{2}e^{-2\alpha_j}\right) + \lambda \sum_{j=2}^{m-1} |(\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1})|
$$
respectively. The penalties encourage smoothness in $\{\alpha_j\}$, leading to more stable and interpretable estimates for $\{\gamma_j^2\}$.

## 2 Power Spectral Density

The sufficient statistic for Model 2 is the periodogram $I(j/n)$. The mean of the periodogram (according to the model) is given by $2\gamma_j^2/n$. This quantity is known as the **power of frequency $j/n$**:
$$
f(j/n) = \text{power of frequency } j/n = \frac{2\gamma_j^2}{n}.
$$
If we plot the points $(j/n, f(j/n))$ for $j = 1, \dots, m$ and join the neighboring points by lines, we get a continuous function plot. This function is known as the **power spectral density** and is defined on $[0, 0.5]$.

This definition of the power spectral density is not rigorous. For a rigorous treatment, see any book on time series (e.g., Chapter 4 of Shumway and Stoffer; or the book "Spectral Analysis for Univariate Time Series" by Percival and Walden).

After estimating the parameters $\gamma_1^2, \dots, \gamma_m^2$, it is customary to look at a plot of the estimated power spectral density $f(j/n) = 2\gamma_j^2/n$ (also known as the **power spectrum**).

---

[Up: contents](index.md) · [3 Rewriting the Model in terms of $yt$ →](02-3-rewriting-the-model-in-terms-of.md)
