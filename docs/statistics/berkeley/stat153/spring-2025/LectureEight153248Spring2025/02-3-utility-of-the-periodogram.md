---
title: 3 Utility of the Periodogram
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEight153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureEight153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureEight153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEight153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Utility of the Periodogram

The periodogram is a very commonly used tool for time series data analysis. It has the following two main uses:

1. If we want to fit the single sinusoidal model
   $$y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t \tag{7}$$
   to the data, then the periodogram allows efficient computation of $RSS(f)$ for Fourier frequencies $f \in (0, 0.5)$ via the following formula:
   $$RSS(f) = \sum_{t=0}^{n-1} (y_t - \bar{y})^2 - 2I(f).$$
   For data sets with large $n$, directly computing $RSS(f)$ over a fine grid might be computationally infeasible. In such cases, one can restrict to Fourier frequencies and compute $RSS(f)$ using the above formula (note that, due to the FFT algorithm, $I(f)$ for Fourier frequencies $f$ can be computed very efficiently).

   Remember also that $RSS(f)$ is key to doing inference for $f$ in the model (7). The MLE of $f$ is obtained by minimizing $RSS(f)$. The Bayesian posterior is given by:
   $$\propto \left(\frac{1}{RSS(f)}\right)^{(n-3)/2} |X_f^T X_f|^{-1/2} I\{0 < f < 1/2\}.$$
   When $f$ is a Fourier frequency lying in $(0, 1/2)$, we saw in Lecture 6 that
   $$X_f^T X_f = \begin{pmatrix} n & 0 & 0 \\ 0 & n/2 & 0 \\ 0 & 0 & n/2 \end{pmatrix} \quad \text{and} \quad (X_f^T X_f)^{-1} = \begin{pmatrix} 1/n & 0 & 0 \\ 0 & 2/n & 0 \\ 0 & 0 & 2/n \end{pmatrix}$$
   so that $|X_f^T X_f| = n^3/8$. Importantly, this term does not depend on $f$. Thus if we restrict to Fourier frequencies, then the Bayesian posterior simplifies to
   $$\propto \left(\frac{1}{RSS(f)}\right)^{(n-3)/2} I\{0 < f < 1/2\}.$$

2. The periodogram can suggest alternative models for the data. For example, if the periodogram has two prominent peaks, then this suggests the model:
   $$y_t = \beta_0 + \beta_1 \cos(2\pi f_1 t) + \beta_2 \sin(2\pi f_1 t) + \beta_3 \cos(2\pi f_2 t) + \beta_4 \sin(2\pi f_2 t) + \epsilon_t. \tag{8}$$
   Formal inference for this model proceeds very similarly to (7). The main difference is that the definition of $RSS$ should now be changed to:
   $$RSS(f_1, f_2) = \min_{\beta_j, 0 \le j \le 4} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 \cos(2\pi f_1 t) - \beta_2 \sin(2\pi f_1 t) - \beta_3 \cos(2\pi f_2 t) - \beta_4 \sin(2\pi f_2 t))^2$$
   The analysis now proceeds as before with this modified definition of $RSS$. The MLE of $f_1$ and $f_2$ is obtained by minimizing $RSS(f_1, f_2)$ over $f_1, f_2$, and the Bayesian posterior is given by
   $$\propto \left(\frac{1}{RSS(f_1, f_2)}\right)^{(n-5)/2} |X_f^T X_f|^{-1/2}$$

where $X_f$ is now given by

$$X_{f_1, f_2} = \begin{pmatrix} 1 & \cos(2\pi f_1(1)) & \sin(2\pi f_1(1)) & \cos(2\pi f_2(1)) & \sin(2\pi f_2(1)) \\ 1 & \cos(2\pi f_1(2)) & \sin(2\pi f_1(2)) & \cos(2\pi f_2(2)) & \sin(2\pi f_2(2)) \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ 1 & \cos(2\pi f_1(n)) & \sin(2\pi f_1(n)) & \cos(2\pi f_2(n)) & \sin(2\pi f_2(n)) \end{pmatrix}$$

In practice, evaluation and minimization of $RSS(f_1, f_2)$ can be done either on a joint grid for $f_1$ and $f_2$, or some sequential algorithm. It may be helpful to note here that if $f_1$ and $f_2$ are both Fourier frequencies and both lie strictly between $0$ and $0.5$, then

$$RSS(f_1, f_2) = \sum_t (y_t - \bar{y})^2 - 2I(f_1) - 2I(f_2).$$

Thus if one restricts to Fourier frequencies, then inference under the model (8) can be easily via the periodogram. If we work with arbitrary frequencies, grid-based minimization of $RSS$ and evaluation of the Bayesian posterior would be computationally expensive.

## 4 Other Nonlinear Regression Models

While our focus so far has been on sinusoidal models, the methodology can be applied in the same way to some other nonlinear regression models. Here are some examples:

1. Consider the model:
   $$y_t = \beta_0 + \beta_1 t + \beta_2 \cos(2\pi f t) + \beta_3 \sin(2\pi f t) + \epsilon_t \tag{9}$$
   The difference between (7) and (9) is the presence of $\beta_1 t$. The RSS for this model is:
   $$RSS(f) = \min_{\beta_0, \beta_1, \beta_2, \beta_3} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 t - \beta_2 \cos(2\pi f t) - \beta_3 \sin(2\pi f t))^2.$$

2. Consider the model:
   $$y_t = \beta_0 + \beta_1 t + \beta_2(t - s)_+ + \epsilon_t \tag{10}$$
   This is sometimes called the broken-stick regression model because the function $t \mapsto \beta_0 + \beta_1 t + \beta_2(t - s)_+$ resembles a broken stick. RSS for this model is:
   $$RSS(s) = \min_{\beta_0, \beta_1, \beta_2} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 t - \beta_2(t - s)_+)^2.$$

Homework Two will contain some other examples of these models.

---

[← 1 DFT](01-1-dft.md) · [Up: contents](index.md)
