---
title: 7 Parameter Estimation in MA(1)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyThree153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwentyThree153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 7 Parameter Estimation in MA(1)

Estimating the parameters of ARMA (as well as ARIMA, SARIMA models) is much harder than parameter estimation in AR models which was handled by standard regression (ordinary least squares). We will not study this topic (and simply rely on the ARIMA function for fitting these models to data). But here, I will just illustrate the difficulties involved in the simplest case of an non-AR model: MA(1). Recall that the MA(1) model is given by
$$y_t = \mu + \epsilon_t + \theta \epsilon_{t-1} \tag{2}$$
where $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. The joint density of $y_1, \dots, y_n$ is multivariate normal with mean vector $m := (\mu, \dots, \mu)^T$ and covariance matrix $\Sigma$ where $\Sigma$ equals the $n \times n$ matrix whose $(i, j)^{\text{th}}$ entry is given by
$$\Sigma(i, j) = \begin{cases}
\sigma^2(1 + \theta^2) & \text{when } i = j \\
\sigma^2\theta & \text{when } |i - j| = 1 \\
0 & \text{for all other } (i, j)
\end{cases}$$
The likelihood is therefore
$$\left(\frac{1}{\sqrt{2\pi}}\right)^n (\det \Sigma)^{-1/2} \exp\left(-\frac{1}{2}(y - m)' \Sigma^{-1}(y - m)\right)$$
where $y$ is the $n \times 1$ vector with components $y_1, \dots, y_n$. This is a function of the unknown parameters $\mu, \theta, \sigma$ which can be estimated by maximizing the logarithm of the likelihood. The presence of $\Sigma^{-1}$ makes this computationally expensive. Some (exact or approximate) formula should be used for $\Sigma^{-1}$ so that one does not need to invert an $n \times n$ matrix every time the log-likelihood is to be computed.

An alternative approach is to try to write the likelihood (approximately) without using an explicit $\Sigma^{-1}$. One way of doing this is to use the connection to AR models. The MA(1) model (2) $y_t = \mu + \theta(B)\epsilon_t$ (with $\theta(B) = 1 + \theta B$) can be converted to an AR model as follows:
$$\epsilon_t = \frac{1}{\theta(B)}(y_t - \mu) = \frac{1}{1 + \theta B}(y_t - \mu) = (1 - \theta B + \theta^2 B^2 - \theta^3 B^3 + \dots)(y_t - \mu)$$
so that
$$y_t - \theta y_{t-1} + \theta^2 y_{t-2} - \theta^3 y_{t-3} + \dots = \frac{\mu}{1 + \theta} + \epsilon_t$$
This requires the assumption that $|\theta| < 1$. For this AR model, we can write the likelihood:
$$\left(\frac{1}{\sqrt{2\pi}\sigma}\right)^n \exp\left(-\frac{1}{2\sigma^2}\sum_{t=1}^n \left(y_t - \frac{\mu}{1 + \theta} - \theta y_{t-1} + \theta^2 y_{t-2} - \theta^3 y_{t-3} + \dots\right)^2\right).$$
This formula involves $y_0, y_{-1}, y_{-2}, \dots$ for which we have no data. We can deal with them by simply setting them to be zero (you can think of writing the conditional likelihood of the data $y_1, \dots, y_n$ given $y_0, y_{-1}, y_{-2}, \dots$ as zero). The likelihood then becomes:
$$\left(\frac{1}{\sqrt{2\pi}\sigma}\right)^n \exp\left(-\frac{S(\mu, \theta)}{2\sigma^2}\right)$$

where
$$\begin{aligned}
S(\mu, \theta) &= \left(y_1 - \frac{\mu}{1 + \theta}\right)^2 + \left(y_2 - \frac{\mu}{1 + \theta} - \theta y_1\right)^2 + \left(y_3 - \frac{\mu}{1 + \theta} - \theta y_2 + \theta^2 y_1\right)^2 + \dots + \\
&\quad \left(y_n - \frac{\mu}{1 + \theta} - \theta y_{n-1} + \theta^2 y_{n-2} - \dots + (-1)^{n-1}\theta^{n-1} y_1\right)^2.
\end{aligned}$$
The MLEs of $\mu$ and $\theta$ are obtained by minimizing $S(\mu, \theta)$:
$$\hat{\mu}, \hat{\theta} \text{ minimize } S(\mu, \theta).$$
This is a nonlinear minimization that can be done via some optimization routines in Python (say in scipy). The MLE for $\sigma$ is easily seen to be
$$\hat{\sigma} = \frac{S(\hat{\mu}, \hat{\theta})}{n}.$$
For uncertainty quantification, we can take a Bayesian approach and combine the likelihood with a prior on $\theta, \mu, \sigma$. Here is how this is done. I did not cover the following in lecture, and this material is optional. It is included here just for completeness.

We assume that $\theta, \mu, \sigma$ are independent with:
$$\theta \sim \text{Unif}(-1, 1) \quad \mu \sim \text{Unif}(-C, C) \quad \log \sigma \sim \text{Unif}(-C, C)$$
for a large $C \to \infty$. Note that we have restricted the range of $\theta$ to $(-1, 1)$ because we assumed that $|\theta| < 1$. The posterior is then
$$\begin{aligned}
f_{\mu, \theta, \sigma|\text{data}}(\mu, \theta, \sigma) &\propto \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^n \exp\left(-\frac{S(\mu, \theta)}{2\sigma^2}\right) \times \frac{1}{\sigma} I\{-1 < \theta < 1, -C < \mu, \log \sigma < C\} \\
&\propto \sigma^{-n-1} \exp\left(-\frac{S(\mu, \theta)}{2\sigma^2}\right) I\{-1 < \theta < 1, -C < \mu, \log \sigma < C\}.
\end{aligned}$$
To obtain the posterior of $\mu$ and $\theta$ alone, we integrate the above with respect to $\sigma$. Integrating from 0 to $\infty$ (assuming $C$ is large so $e^{-C} \approx 0$ and $e^C \approx \infty$), we obtain (as in Lecture Three):
$$f_{\mu, \theta|\text{data}}(\mu, \theta) \propto \left(\frac{1}{S(\mu, \theta)}\right)^{n/2} I\{-1 < \theta < 1, -C < \mu < C\}.$$
This posterior can be evaluated numerically over a grid of values of $\mu$ and $\theta$ and approximated by the appropriate discrete distribution over the grid. Alternatively, we can approximate this posterior by a suitable $t$-distribution by doing a Taylor expansion of $S(\mu, \theta)$ near the minimizer $\hat{\mu}, \hat{\theta}$. To illustrate this, let $\alpha = (\mu, \theta)$ and $\hat{\alpha} = (\hat{\mu}, \hat{\theta})$. Taylor expansion for $\alpha$ near $\hat{\alpha}$ gives
$$\begin{aligned}
S(\alpha) &= S(\hat{\alpha}) + \langle\nabla S(\hat{\alpha}), \alpha - \hat{\alpha}\rangle + (\alpha - \hat{\alpha})^T \left(\frac{1}{2}HS(\hat{\alpha})\right) (\alpha - \hat{\alpha}) \\
&= S(\hat{\alpha}) + (\alpha - \hat{\alpha})^T \left(\frac{1}{2}HS(\hat{\alpha})\right) (\alpha - \hat{\alpha})
\end{aligned}$$
where we used $\nabla S(\hat{\alpha}) = 0$ because $\hat{\alpha}$ minimizes $S(\alpha)$. Here $HS(\hat{\alpha})$ denotes the Hessian of

$S$ at $\hat{\alpha}$. Therefore
$$\begin{aligned}
f_{\mu, \theta|\text{data}}(\mu, \theta) &\propto \left(\frac{1}{S(\mu, \theta)}\right)^{n/2} I\{-1 < \theta < 1, -C < \mu < C\} \\
&\propto \left(\frac{S(\hat{\alpha})}{S(\alpha)}\right)^{n/2} I\{-1 < \theta < 1, -C < \mu < C\} \\
&= \left(\frac{S(\hat{\alpha})}{S(\hat{\alpha}) + (\alpha - \hat{\alpha})^T \left(\frac{1}{2}HS(\hat{\alpha})\right)(\alpha - \hat{\alpha})}\right)^{n/2} I\{-1 < \theta < 1, -C < \mu < C\} \\
&= \left(\frac{1}{1 + (\alpha - \hat{\alpha})^T \left(\frac{1}{2S(\hat{\alpha})}HS(\hat{\alpha})\right)(\alpha - \hat{\alpha})}\right)^{n/2} I\{-1 < \theta < 1, -C < \mu < C\} \\
&= \left(\frac{1}{1 + \frac{1}{n-2}(\alpha - \hat{\alpha})^T \left(\frac{n-2}{2S(\hat{\alpha})}HS(\hat{\alpha})\right)(\alpha - \hat{\alpha})}\right)^{\frac{n-2+2}{2}} I\{-1 < \theta < 1, -C < \mu < C\}.
\end{aligned}$$
Comparing the above with the formula:
$$\left(\frac{1}{1 + \frac{1}{k}(x - m)^T \Sigma^{-1}(x - m)}\right)^{\frac{k+p}{2}}$$
for the $p$-variate $t$-density $t_{k, p}(\mu, \Sigma)$, we see that (ignoring the indicator function $I\{-1 < \theta < 1, -C < \mu < C\}$)
$$\alpha \mid \text{data} \sim t_{n-2, 2}\left(\hat{\alpha}, \frac{S(\hat{\alpha})}{n - 2}\left(\frac{1}{2}HS(\hat{\alpha})\right)^{-1}\right).$$
This $t$-density can be used for uncertainty quantification of $\mu$ and $\theta$.

## 8 Additional Optional Reading

1. Sections 3.5, 3.6 and 3.9 of Shumway-Stoffer 4th edition.

---

[← 5 Multiplicative Seasonal ARMA Models](04-5-multiplicative-seasonal-arma-models.md) · [Up: contents](index.md)
