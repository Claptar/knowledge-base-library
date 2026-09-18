---
title: 3 Model Three
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFourteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFourteen153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFourteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFourteen153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Model Three

Model three is essentially Model two but applied to the DFT. In order to describe this, let us first revisit the DFT. Given a time series $y_0, \dots, y_{n-1}$, its DFT is $b_0, b_1, \dots, b_{n-1}$ where
$$b_j = \sum_{t=0}^{n-1} y_t \exp\left( -\frac{2\pi i j t}{n} \right).$$
$b_j$ is a complex number with real and imaginary parts given by
$$\text{Re}(b_j) = \sum_{t=0}^{n-1} y_t \cos\left( \frac{2\pi j t}{n} \right) \quad \text{and} \quad \text{Im}(b_j) = -\sum_{t=0}^{n-1} y_t \sin\left( \frac{2\pi j t}{n} \right)$$
When $j = 0$, the imaginary part is zero and we get $b_0 = \sum_{t=0}^{n-1} y_t$. $b_0$ is therefore just the sum of the datapoints and it does not provide any information on cycles etc.

Another fact that we previously verified is $b_{n-j} = \bar{b}_j$ (here $\bar{b}_j$ denotes the complex conjugate of $b_j$). Because of this property, the later half of the DFT terms is redundant (as they can be recovered from the first half).

If $n$ is odd and $m = (n - 1)/2$, then the most important DFT terms are $b_1, \dots, b_m$. The other terms are $b_0$ which is simply the sum of the data points and $b_{m+1}, \dots, b_{n-1}$ which are simply the complex conjugates of $b_m, b_{m-1}, \dots, b_1$.

If $n$ is even and $m = (n - 2)/2$, then the most important DFT terms are $b_1, \dots, b_m$ and $b_{m+1}$. The other DFT terms are $b_0$ which is simply the sum of the data points and $b_{m+2}, \dots, b_{n-1}$ which are the complex conjugates of $b_m, \dots, b_1$. Note in this case that $m+1 = b_{n/2}$ will have zero imaginary part (hence $b_{m+1}$ is real).

Below we focus on the case where $n$ is odd for simplicity, and take $m = (n - 1)/2$. Model three is obtained by using Model two for the DFT terms $b_1, \dots, b_m$. Because $b_j$ can be complex, we use the modeling assumption for both the real and imaginary parts:
$$\text{Re}(b_j), \text{Im}(b_j) \overset{\text{i.i.d}}{\sim} N(0, \gamma_j^2) \quad \text{for } j = 1, \dots, m. \tag{4}$$
We also assume that $b_j$ are independent across $j$. The unknown parameters in this model are $\gamma_1, \dots, \gamma_m$. $\gamma_j$ represents the strength of the sinusoids at frequency $j/n$.

The likelihood corresponding to (4) is proportional to:
$$\prod_{j=1}^m \frac{1}{\gamma_j} \exp\left( -\frac{(\text{Re}(b_j))^2}{2\gamma_j^2} \right) \frac{1}{\gamma_j} \exp\left( -\frac{(\text{Im}(b_j))^2}{2\gamma_j^2} \right)$$
$$= \prod_{j=1}^m \frac{1}{\gamma_j^2} \exp\left( -\frac{(\text{Re}(b_j))^2 + (\text{Im}(b_j))^2}{2\gamma_j^2} \right) = \prod_{j=1}^m \frac{1}{\gamma_j^2} \exp\left( -\frac{|b_j|^2}{2\gamma_j^2} \right).$$
Therefore the likelihood depends on the squared magnitudes $|b_j|^2$ of the DFT coefficients. Recall that the periodogram $I(j/n)$ is defined as
$$I(j/n) := \frac{|b_j|^2}{n}.$$
We can therefore rewrite the likelihood in terms of the periodogram as follows:
$$\prod_{j=1}^m \frac{1}{\gamma_j^2} \exp\left( -\frac{nI(j/n)}{2\gamma_j^2} \right). \tag{5}$$

This likelihood depends on the data only through the periodogram ordinates $I(j/n)$ for $j = 1, \dots, m$. Therefore the periodogram forms the sufficient statistic in this model. Under (4), we have
$$I(j/n) = \frac{1}{n} |b_j|^2 = \frac{1}{n} ((\text{Re}(b_j))^2 + (\text{Im}(b_j))^2) \sim \frac{\gamma_j^2}{n} \chi_2^2.$$
The model can therefore be written directly in terms of the periodogram as
$$I(j/n) \overset{\text{ind}}{\sim} \frac{\gamma_j^2}{n} \chi_2^2 \quad \text{for } j = 1, \dots, m.$$
We can write the likelihood for the above model in terms of the periodogram and this would be proportional to (5). Note also that $\chi_2^2$ distribution with two degrees of freedom actually coincides with the Exponential distribution with $\lambda$ parameter equal to $1/2$.

Intuitively, Model (4) does not care so much about the individual DFT coefficients $b_j$ but only their magnitude.

The negative log-likelihood corresponding to (5) is
$$\sum_{j=1}^m \left( 2 \log \gamma_j + \frac{nI(j/n)}{2\gamma_j^2} \right).$$
As in the case of Model two, for optimization purposes we work with the logarithms of $\gamma_j$. Let $\alpha_j = \log \gamma_j$. The negative log-likelihood in terms of $\alpha_j$ is
$$\sum_{j=1}^m \left( 2\alpha_j + \frac{nI(j/n)}{2} e^{-2\alpha_j} \right).$$
If we directly minimize the above with respect to $\alpha_j$ (without any additional regularization), we get
$$\alpha_j = \log \sqrt{\frac{nI(j/n)}{2}} \quad \text{and} \quad \gamma_j^2 = e^{2\alpha_j} = \frac{nI(j/n)}{2}.$$
This basically means that the $\gamma_j^2$ parameters fully interpolate the periodogram leading to full overfitting. For more meaningful estimation, we need to add regularization. If we assume smoothness of $\alpha_j$, we can add the penalty $\sum_{j=2}^{m-1} ((\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}))^2$ or $\sum_{j=2}^{m-1} |(\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1})|$ to the negative log-likelihood. This leads to the estimators $\hat{\alpha}_t^{\text{ridge}}(\lambda)$ and $\hat{\alpha}_t^{\text{lasso}}(\lambda)$ which are defined as the minimizers of
$$\sum_{j=1}^m \left( 2\alpha_j + \frac{nI(j/n)}{2} e^{-2\alpha_j} \right) + \lambda \sum_{j=2}^{m-1} ((\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}))^2$$
and
$$\sum_{t=1}^n \left( 2\alpha_j + \frac{nI(j/n)}{2} e^{-2\alpha_j} \right) + \lambda \sum_{j=2}^{m-1} |(\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1})|$$
respectively. The penalties encourage smoothness in $\{\alpha_j\}$, leading to more stable and interpretable estimates for $\{\gamma_j\}$.

In the next lecture, we shall explain the equivalence of this model with the spectrum model from last lecture. We shall also explore some applications for this model.

---

[← 2 Model Two](02-2-model-two.md) · [Up: contents](index.md)
