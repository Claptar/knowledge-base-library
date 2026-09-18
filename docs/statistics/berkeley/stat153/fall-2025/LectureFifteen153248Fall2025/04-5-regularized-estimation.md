---
title: 5 Regularized Estimation
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFifteen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFifteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 5 Regularized Estimation

Parameter estimation is done by maximizing likelihood with a regularization penalty which ensures smoothness of the estimates (without the regularization penalty, we would overfit in the sense that the estimate of $f(j/n)$ would coincide with the periodogram $I(j/n)$).

To obtain the likelihood, we can use any of the three definitions of the spectrum model. If we use Definition 1 (i.e., (3)), the likelihood will be given by:
$$\begin{aligned}
&\prod_{j=1}^m \frac{1}{\gamma_j} \exp\left(-\frac{(\text{Re}(b_j))^2}{2\gamma_j^2}\right) \frac{1}{\gamma_j} \exp\left(-\frac{(\text{Im}(b_j))^2}{2\gamma_j^2}\right) \\
&= \prod_{j=1}^m \frac{1}{\gamma_j^2} \exp\left(-\frac{(\text{Re}(b_j))^2 + (\text{Im}(b_j))^2}{2\gamma_j^2}\right) = \prod_{j=1}^m \frac{1}{\gamma_j^2} \exp\left(-\frac{|b_j|^2}{2\gamma_j^2}\right).
\end{aligned}$$
We can rewrite the above likelihood in terms of the periodogram (because $I(j/n) = |b_j|^2/n$) as follows:
$$\prod_{j=1}^m \frac{1}{\gamma_j^2} \exp\left(-\frac{n I(j/n)}{2\gamma_j^2}\right). \tag{8}$$
We can also use the definition (1) and write the likelihood directly using the exponential distribution. Note that the density of $\eta_j$ is $\exp(-x)I\{x > 0\}$ and the density of $f(j/n)\eta_j$ is $\frac{1}{f(j/n)}\exp(-\frac{x}{f(j/n)})I\{x > 0\}$. Thus the likelihood (joint density of $I(j/n)$, $1 \le j \le m$) is:
$$\prod_{j=1}^n \frac{1}{f(j/n)} \exp\left(-\frac{I(j/n)}{f(j/n)}\right). \tag{9}$$
The above is equivalent to (8) (up to proportionality) because $f(j/n) = 2\gamma_j^2/n$.

The negative log-likelihood corresponding to (8) is
$$\sum_{j=1}^m \left(2\log \gamma_j + \frac{n I(j/n)}{2\gamma_j^2}\right).$$
For optimization purposes we work with the logarithms of $\gamma_j$. Let $\alpha_j = \log \gamma_j$. The negative log-likelihood in terms of $\alpha_j$ is
$$\sum_{j=1}^m \left(2\alpha_j + \frac{n I(j/n)}{2} e^{-2\alpha_j}\right).$$

If we directly minimize the above with respect to $\alpha_j$ (without any additional regularization), we get
$$\alpha_j = \log \sqrt{\frac{n I(j/n)}{2}} \quad \text{and} \quad \gamma_j^2 = e^{2\alpha_j} = \frac{n I(j/n)}{2}.$$
This basically means that the $\gamma_j^2$ parameters fully interpolate the periodogram leading to full overfitting. For more meaningful estimation, we need to add regularization. If we assume smoothness of $\alpha_j$, we can add the penalty $\sum_{j=2}^{m-1} ((\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}))^2$ or $\sum_{j=2}^{m-1} |(\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1})|$ to the negative log-likelihood. This leads to the estimators $\hat{\alpha}_t^{\text{ridge}}(\lambda)$ and $\hat{\alpha}_t^{\text{lasso}}(\lambda)$ which are defined as the minimizers of
$$\sum_{j=1}^m \left(2\alpha_j + \frac{n I(j/n)}{2} e^{-2\alpha_j}\right) + \lambda \sum_{j=2}^{m-1} ((\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}))^2$$
and
$$\sum_{t=1}^n \left(2\alpha_j + \frac{n I(j/n)}{2} e^{-2\alpha_j}\right) + \lambda \sum_{j=2}^{m-1} |(\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1})|$$
respectively. The penalties encourage smoothness in $\{\alpha_j\}$, leading to more stable and interpretable estimates for $\{\gamma_j^2\}$.

Once we obtain estimates $\hat{\alpha}_j$ of $\alpha_j$, we can convert them to estimates of $\gamma_j$ via $\hat{\gamma}_j = \exp(\hat{\alpha}_j)$ and then to estimates of $f(j/n)$ via $\hat{f}(j/n) = 2\hat{\gamma}_j^2/n$.

## 6 The case of even $n$

We assumed that $n$ is odd (and $m = (n - 1)/2$). If $n$ is even, then $1/2$ becomes a Fourier frequency and $b_{n/2}$ becomes real (because $\sin(\pi t) = 0$ for all $t$). In this case, we can simply avoid working with $1/2$ by taking $m = (n - 2)/2$ and using the model:
$$\text{Re}(b_j), \text{Im}(b_j) \overset{\text{i.i.d}}{\sim} N(0, \gamma_j^2) \quad \text{for } j = 1, \dots, m.$$
This will be equivalent to (7). Basically everything will stay the same as before (only difference is that $m = (n - 2)/2$). Here we are essentially forcing $\gamma_{n/2} = 0$. One can try to also try to estimate $\gamma_{n/2}$ using $b_{n/2} \sim N(0, \gamma_{n/2}^2)$ but this approach is slightly more complicated.

---

[← 4 Rewriting the Model in terms of $yt$](03-4-rewriting-the-model-in-terms-of.md) · [Up: contents](index.md)
