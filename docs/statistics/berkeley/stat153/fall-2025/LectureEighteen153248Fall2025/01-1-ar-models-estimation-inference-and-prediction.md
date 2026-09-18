---
title: '1 AR models: estimation, inference and prediction'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEighteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEighteen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureEighteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEighteen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 AR models: estimation, inference and prediction

### Lecture Eighteen
Fall 2025, UC Berkeley
Aditya Guntuboyina
October 30, 2025

The AR($p$) model is given by:
$$y_t = \phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t \tag{1}$$
The unknown parameters are $\phi_0, \phi_1, \dots, \phi_p$ as well as $\sigma$ ($\sigma$ is the standard deviation of $\epsilon_t$). These need to be estimated from the observed data $y_1, \dots, y_n$.

The likelihood is (below $\theta$ denotes the vector consisting of all the parameters $\phi_0, \dots, \phi_p$ and $\sigma$):
$$f_{y_1, \dots, y_n \mid \theta}(y_1, \dots, y_n) = f_{y_{p+1}, \dots, y_n \mid y_1, \dots, y_p, \theta}(y_{p+1}, \dots, y_n) f_{y_1, \dots, y_p \mid \theta}(y_1, \dots, y_p).$$
The first term on the right hand side above $f_{y_{p+1}, \dots, y_n \mid y_1, \dots, y_p, \theta}(y_{p+1}, \dots, y_n)$ is the conditional likelihood of $y_{p+1}, \dots, y_n$ given $y_1, \dots, y_p$. This conditional likelihood is calculated as
$$\begin{aligned}
f_{y_{p+1}, \dots, y_n \mid y_1, \dots, y_p, \theta}(y_{p+1}, \dots, y_n) &= \prod_{t=p+1}^n f_{y_t \mid y_{t-1}, \dots, y_1, \theta}(y_t) \\
&= \prod_{t=p+1}^n f_{\phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t \mid y_{t-1}, \dots, y_1, \theta}(y_t) \\
&= \prod_{t=p+1}^n f_{\epsilon_t \mid y_{t-1}, \dots, y_1, \theta}(y_t - \phi_0 - \phi_1 y_{t-1} - \dots - \phi_p y_{t-p}).
\end{aligned}$$
In order to proceed further, we shall make the following assumption:
$$\epsilon_t \mid y_{t-1}, \dots, y_1 \sim N(0, \sigma^2) \quad \text{for each } t = p + 1, \dots, n, \tag{2}$$
which can be ensured by assuming that $\epsilon_t \sim N(0, \sigma^2)$ and that $\epsilon_t$ is independent of $y_1, \dots, y_{t-1}$. With (2), we get
$$\begin{aligned}
f_{y_{p+1}, \dots, y_n \mid y_1, \dots, y_p, \theta}(y_{p+1}, \dots, y_n) &= \prod_{t=p+1}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left(-\frac{(y_t - \phi_0 - \phi_1 y_{t-1} - \dots - \phi_p y_{t-p})^2}{2\sigma^2}\right) \\
&= \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^{n-p} \exp\left(-\frac{1}{2\sigma^2} \sum_{t=p+1}^n (y_t - \phi_0 - \phi_1 y_{t-1} - \dots - \phi_p y_{t-p})^2\right).
\end{aligned}$$

Observe that, in order to write the above formula, we only used the model equation (1) for $t = p + 1, \dots, n$.

The conditional joint density $f_{y_{p+1}, \dots, y_n \mid y_1, \dots, y_p, \theta}(y_{p+1}, \dots, y_n)$ is called the **conditional likelihood** of the AR($p$) model. The full likelihood is
$$\begin{aligned}
f_{y_1, \dots, y_n \mid \theta}(y_1, \dots, y_n) &= f_{y_{p+1}, \dots, y_n \mid y_1, \dots, y_p, \theta}(y_{p+1}, \dots, y_n) f_{y_1, \dots, y_p \mid \theta}(y_1, \dots, y_p) \\
&= \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^{n-p} \exp\left(-\frac{1}{2\sigma^2} \sum_{t=p+1}^n (y_t - \phi_0 - \phi_1 y_{t-1} - \dots - \phi_p y_{t-p})^2\right) f_{y_1, \dots, y_p \mid \theta}(y_1, \dots, y_p).
\end{aligned}$$
If we assume that $f_{y_1, \dots, y_p \mid \theta}(y_1, \dots, y_p)$ does not depend on $\theta$, then maximizing the full likelihood is equivalent to maximizing the conditional likelihood.

If we want to derive $f_{y_1, \dots, y_p \mid \theta}(y_1, \dots, y_p)$ in a more principled way, then we have to use the model equation (1) for smaller values of $t$ (i.e., $t = p, p - 1, p - 2, \dots, 0, -1, \dots$). This makes the analysis complicated and is not really worth it. It also only works under some "stationarity" assumptions on $\phi_0, \dots, \phi_p$. It is much simpler working with the conditional likelihood.

Using the matrix notation:
$$Y_{(n-p) \times 1} = \begin{pmatrix} y_{p+1} \\ y_{p+2} \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix} \quad X_{(n-p) \times (p+1)} = \begin{pmatrix} 1 & y_p & y_{p-1} & \dots & y_1 \\ 1 & y_{p+1} & y_{p+2} & \dots & y_2 \\ \cdot & \cdot & \cdot & \dots & \cdot \\ \cdot & \cdot & \cdot & \dots & \cdot \\ \cdot & \cdot & \cdot & \dots & \cdot \\ 1 & y_{n-1} & y_{n-2} & \dots & y_{n-p} \end{pmatrix} \quad \beta_{(p+1) \times 1} = \begin{pmatrix} \phi_0 \\ \phi_1 \\ \cdot \\ \cdot \\ \cdot \\ \phi_p \end{pmatrix},$$
the conditional likelihood (which is also proportional to the full likelihood under the assumption that $f_{y_1, \dots, y_p \mid \theta}(y_1, \dots, y_p)$ does not depend on $\theta$) becomes:
$$\text{likelihood} \propto \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^{n-p} \exp\left(-\frac{\|Y - X\beta\|^2}{2\sigma^2}\right). \tag{3}$$
This likelihood is the same as the likelihood in linear regression with $n - p$ observations. We can therefore infer the parameters $\phi_0, \dots, \phi_p$ and $\sigma$ as in usual linear regression with the prior:
$$\phi_0, \phi_1, \dots, \phi_p, \log \sigma \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C).$$
This will allow us to write down the joint posterior of $(\beta, \sigma)$. Integrating over $\sigma$ leads to the posterior of $\beta$ alone. As in Lecture 4, this leads to
$$\beta \mid \text{data} \sim t_{n-2p-1, p+1}\left(\hat{\beta}, \hat{\sigma}^2 (X^T X)^{-1}\right)$$
where
$$\hat{\beta} := (X'X)^{-1}X'Y \quad \text{and} \quad \hat{\sigma} = \sqrt{\frac{\|Y - X\hat{\beta}\|^2}{n - 2p - 1}}.$$
Note that the degrees of freedom of the $t$-distribution above is $n - 2p - 1$ as the number of observations equals $n - p$ and the number of components of $\beta$ is $p + 1$. If inference for $\sigma$ is desired, one can use:
$$\frac{\|Y - X\hat{\beta}\|^2}{\sigma^2} \;\middle|\; \text{data} \sim \chi^2_{n-2p-1}.$$

Note that Bayesian inference for AR models is identical to Bayesian inference for linear regression models because the likelihood (3) is the same as in the usual linear model (with $n - p$ observations). Bayesian inference only cares about the likelihood.

Frequentist inference for the AR($p$) model is based on the MLE which is given by $\hat{\beta}$ and
$$\hat{\sigma}_{\text{MLE}} = \sqrt{\frac{\|Y - X\hat{\beta}\|^2}{n - p}}.$$
To obtain frequentist confidence intervals for the parameters $\phi_i$, one needs to find the distribution of $\hat{\beta}$. Here the analysis is quite different from that used in linear regression (see, for example, Section 3.5 of the book by Shumway and Stoffer titled *Time Series Analysis and its applications* (Fourth Edition)). The results turn out to be quite close to those obtained by the Bayesian method.

Unlike Bayesian inference, frequentist inference for the AR model is not identical to frequentist inference for the usual linear regression model. For example, one does not use $t$-distributions for inferring the $\phi$ parameters in AR($p$) models. Instead, one uses normal distributions (e.g., $z$-scores as opposed to $t$-scores) which are justified by asymptotic arguments that are different from and more complicated than those used for linear regression.

On the computer, estimation and inference for AR models can be done in two ways:
1. Just create $y$ and $X$ as above, and use OLS in statsmodels.
2. Use the `AutoReg` function in statsmodels.

Both methods give the same estimates of $\phi_0, \dots, \phi_p$. The estimate of $\sigma$ is slightly different: OLS gives $\hat{\sigma}_{\text{OLS}} := \sqrt{\text{RSS}/(n - 2p - 1)}$ and AutoReg gives $\hat{\sigma}_{\text{MLE}} := \sqrt{\text{RSS}/(n - p)}$. The two methods also give slightly different standard errors corresponding to the coefficient estimates. OLS gives square roots of the diagonal entries of $\hat{\sigma}^2_{\text{OLS}}(X^T X)^{-1}$ while AutoReg considers $\hat{\sigma}^2_{\text{MLE}}(X^T X)^{-1}$. Finally OLS does coefficient inference using the $t$-distribution (with $n - 2p - 1$ degrees of freedom) while AutoReg recommends inference using the normal distribution.

## 2 Predictions from AR($p$) models

If the parameters $\phi_0, \dots, \phi_p$ and $\sigma$ (collectively denoted by $\theta$) of the AR($p$) model are fixed, then the prediction for a future value $y_{n+i}$ is given by
$$\hat{y}_{n+i}(\theta) := \mathbb{E}(y_{n+i} \mid y_1, \dots, y_n, \theta)$$
These values are calculated recursively for $i = 1, 2, \dots$ using the following recursion:
$$\hat{y}_{n+i}(\theta) = \phi_0 + \phi_1 \hat{y}_{n+i-1}(\theta) + \phi_2 \hat{y}_{n+i-2}(\theta) + \dots + \phi_p \hat{y}_{n+i-p}(\theta) \quad \text{for } i = 1, 2, \dots \tag{4}$$
which is initialized by
$$\hat{y}_j(\theta) = y_j \quad \text{for } j = n, n - 1, \dots, n + 1 - p, \tag{5}$$
Since $\theta$ is unknown, we can replace it by the conditional MLE $\hat{\theta}$.

---

[Up: contents](index.md) · [3 Prediction Standard Errors →](02-3-prediction-standard-errors.md)
