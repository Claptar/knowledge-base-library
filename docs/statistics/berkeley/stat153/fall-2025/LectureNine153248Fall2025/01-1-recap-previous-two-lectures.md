---
title: '1 Recap: previous two lectures'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNine153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureNine153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureNine153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNine153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Recap: previous two lectures

## Lecture Nine
### Fall 2025, UC Berkeley
### Aditya Guntuboyina
### September 26, 2025

We observe time series data $y_0, \dots, y_{n-1}$ (note we are now using Python indexing starting from 0). We want to fit the sinusoidal model:
$$y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t \quad \text{with } \epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2). \tag{1}$$
The main parameter is the frequency $f$ (which we restrict to the interval $[0, 0.5]$). The other parameters $(\beta_0, \beta_1, \beta_2, \sigma)$ are nuisance parameters.

The key role in the inference of $f$ is played by the RSS:
$$RSS(f) := \min_{\beta_0,\beta_1,\beta_2} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 \cos(2\pi f t) - \beta_2 \sin(2\pi f t))^2 = \|y - X_f \hat{\beta}_f\|^2$$
where
$$y = \begin{pmatrix} y_1 \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix} \quad \text{and} \quad X_f = \begin{pmatrix} 1 & \cos(2\pi f(1)) & \sin(2\pi f(1)) \\ \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot \\ 1 & \cos(2\pi f(n)) & \sin(2\pi f(n)) \end{pmatrix} \quad \text{and} \quad \hat{\beta}_f = (X_f^T X_f)^{-1} X_f^T y.$$
$RSS(f)$ is simply the residual sum of squares in the linear regression model obtained by fixing the frequency parameter $f$. It describes how well the sinusoid with frequency $f$ fits the observed data $\{y_t\}$.

To estimate $f$, we minimize $RSS(f)$. For uncertainty quantification for $f$, we can use the posterior formula:
$$\text{posterior}(f) \propto \left(\frac{1}{RSS(f)}\right)^{(n-3)/2} |X_f^T X_f|^{-1/2} I\{0 < f < 1/2\}.$$
For both these tasks (minimization of $RSS(f)$ and calculation of the posterior of $f$), we need to discretize and restrict $f$ to a finite set of values in the range $(0, 1/2)$. Here there are two options:

1. Take a dense grid of values in $(0, 1/2)$
2. Work with the Fourier frequencies $j/n$ which are in the range $(0, 1/2)$.

The advantage of taking the second option (Fourier Frequencies) is that it admits very fast computation of $RSS(f)$ via the following:

1. Calculate the DFT of the data:
$$b_j = \sum_{t=0}^{n-1} y_t \exp\left(-\frac{2\pi i j t}{n}\right) \quad \text{for } j = 0, 1, \dots, n - 1.$$
This can be done via a very fast algorithm called the FFT (in python, use `np.fft.fft()`).

2. Calculate the periodogram:
$$I(j/n) := \frac{|b_j|^2}{n} \quad \text{for } 0 < \frac{j}{n} < 0.5$$

3. Use the formula:
$$RSS(j/n) = \sum_{t=0}^{n-1} (y_t - \bar{y})^2 - 2I(j/n).$$
This formula was proved in Lecture 7. The key observation is that when $f$ is a Fourier frequency lying in $(0, 0.5)$, we have
$$X_f^T X_f = \begin{pmatrix} n & 0 & 0 \\ 0 & n/2 & 0 \\ 0 & 0 & n/2 \end{pmatrix} \tag{2}$$

4. Minimize $RSS(j/n)$ over $j$ to obtain $\hat{f}$.

5. Calculate the posterior of $f$ via:
$$\text{posterior}(j/n) \propto \left(\frac{1}{RSS(j/n)}\right)^{(n-3)/2} I\{0 < j/n < 0.5\}.$$

Note that we did not write the $|X_f^T X_f|^{-1/2}$ term above. This is because, when $f$ is a Fourier frequency in $(0, 0.5)$, we have (2) so that $|X_f^T X_f| = n^3/8$ which does not depend on $f$ (so $|X_f^T X_f|^{-1/2}$ can be absorbed in the constant of proportionality).

It is important to note that restriction to Fourier frequencies is only done for computational reasons. There are no other advantages to doing this, and, in fact, there could be significant loss of information in doing so. This can be easily seen in real datasets such as the sunspots dataset.

---

[Up: contents](index.md) · [2 Sinusoidal Models with more frequencies →](02-2-sinusoidal-models-with-more-frequencies.md)
