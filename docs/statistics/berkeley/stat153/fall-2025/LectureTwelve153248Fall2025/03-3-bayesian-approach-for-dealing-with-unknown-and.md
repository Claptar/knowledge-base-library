---
title: 3 Bayesian approach for dealing with unknown $\tau$ and $\sigma$
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwelve153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwelve153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Bayesian approach for dealing with unknown $\tau$ and $\sigma$

One gets smooth fits to the data by working with the prior (8) for small $\tau$. This is not very surprising because the prior injects a strong amount of bias in favor of smooth fits. The real power of the Bayesian approach lies in the ability to automatically infer $\tau$ from the data. This is done by simply placing a prior on $\tau$ (along with the priors on $\beta$ and $\sigma$). We shall use the following prior:
$$\log \tau, \log \sigma \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C)$$
and
$$\beta \mid \tau, \sigma \sim N(0, Q)$$
where $Q$ is the same as in (9). Note that this prior implies that we are allowing essentially (because $C$ is large) all possible values of $\tau$ and $\sigma$. In particular, we are not a priori ruling out large $\tau$ just because we don't like wiggly fits.

The prior joint density for $\beta, \tau, \sigma$ is
$$f_{\beta,\tau,\sigma}(\beta, \tau, \sigma) = f_\tau(\tau) f_\sigma(\sigma) f_{\beta \mid \tau}(\beta)$$
$$= \frac{I\{e^{-C} < \tau < e^C\}}{2C\tau} \frac{I\{e^{-C} < \sigma < e^C\}}{2C\sigma} \left(\frac{1}{\sqrt{2\pi}}\right)^n \frac{1}{\sqrt{\det Q}} \exp\left(-\frac{1}{2} \beta^T Q^{-1} \beta\right)$$
$$\propto \frac{I\{e^{-C} < \tau, \sigma < e^C\}}{\tau\sigma} \frac{1}{\sqrt{\det Q}} \exp\left(-\frac{1}{2} \beta^T Q^{-1} \beta\right).$$

We will also ignore the indicator because $C$ will be very large. It is important to note that $Q$ is not a constant matrix as it depends on $\tau$. The likelihood is (as usual in linear regression)
$$\left(\frac{1}{\sqrt{2\pi}}\right)^n \sigma^{-n} \exp\left(-\frac{1}{2\sigma^2} \|y - X\beta\|^2\right).$$

The posterior for $\beta, \tau, \sigma$ is therefore
$$f_{\beta,\tau,\sigma \mid \text{data}}(\beta, \tau, \sigma) \propto \frac{\sigma^{-n-1}\tau^{-1}}{\sqrt{\det Q}} \exp\left(-\frac{1}{2}\left(\frac{1}{\sigma^2} \|y - X\beta\|^2 + \beta^T Q^{-1} \beta\right)\right).$$

The term inside the exponent is a quadratic in $\beta$ and it is natural to complete the square which is done as follows:
$$\frac{1}{\sigma^2} \|y - X\beta\|^2 + \beta^T Q^{-1} \beta = \frac{y^T y}{\sigma^2} - \frac{2\beta^T X^T y}{\sigma^2} + \beta^T \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right) \beta$$
$$= (\beta - \mu)^T \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right) (\beta - \mu) + \frac{y^T y}{\sigma^2} - \mu^T \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right) \mu$$

where
$$\mu := \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2}$$
We thus have
$$\frac{1}{\sigma^2} \|y - X\beta\|^2 + \beta^T Q^{-1} \beta$$
$$= (\beta - \mu)^T \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right) (\beta - \mu) + \frac{y^T y}{\sigma^2} - \frac{y^T X}{\sigma^2} \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2}.$$

Plugging this in the posterior formula, we deduce
$$f_{\beta,\tau,\sigma \mid \text{data}}(\beta, \tau, \sigma)$$
$$\propto \frac{\sigma^{-n-1}\tau^{-1}}{\sqrt{\det Q}} \exp\left(-\frac{1}{2}\left((\beta - \mu)^T \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right) (\beta - \mu) + \frac{y^T y}{\sigma^2} - \frac{y^T X}{\sigma^2} \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2}\right)\right)$$
$$= \frac{\sigma^{-n-1}\tau^{-1}}{\sqrt{\det Q}} \exp\left(-\frac{1}{2}(\beta - \mu)^T \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right) (\beta - \mu)\right) \exp\left(-\frac{y^T y}{2\sigma^2}\right)$$
$$\times \exp\left(\frac{y^T X}{2\sigma^2} \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2}\right).$$

This expression may look complicated but the dependence on $\beta$ is simple through the quadratic which implies that
$$\beta \mid \text{data}, \sigma, \tau \sim N\left(\mu, \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1}\right) = N\left(\left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2}, \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1}\right)$$

This proves (7) and (10). It is also straightforward to integrate $\beta$ from the joint posterior to obtain the posterior of $\tau, \sigma$:
$$f_{\tau,\sigma \mid \text{data}}(\tau, \sigma)$$
$$\propto \frac{\sigma^{-n-1}\tau^{-1}}{\sqrt{\det Q}} \sqrt{\det \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1}} \exp\left(-\frac{y^T y}{2\sigma^2}\right) \exp\left(\frac{y^T X}{2\sigma^2} \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2}\right).$$

In practice, inference can be carried out by first taking a grid of $\sigma$ and $\tau$ values and computing the above posterior (on the logarithmic scale) at the grid points. We can obtain point estimates of $\sigma$ and $\tau$ by taking the posterior maximizers. Alternatively, we can obtain posterior samples of $\sigma$ and $\tau$ by sampling from the grid points with posterior weights. For each $(\sigma, \tau)$ sample, one can sample $\beta$ using the multivariate normal distribution (10).

This grid approach can be avoided by using MCMC methods such as the Gibbs sampler. We shall not be discussing these.

---

[← 2 Bayesian Regularization](02-2-bayesian-regularization.md) · [Up: contents](index.md) · [4 Comments on Bayesian Regularization →](04-4-comments-on-bayesian-regularization.md)
