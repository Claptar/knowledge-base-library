---
title: Standard Errors corresponding to the parameter estimates
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTwelve153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLabTwelve153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Standard Errors corresponding to the parameter estimates

After obtaining the MLEs $\hat{\mu}$ and $\hat{\theta}$, the next step is to obtain standard errors. For this, we can use the Bayesian approach with the standard prior:
\begin{align*}
   \mu, \theta, \log \sigma \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C).
\end{align*}

The posterior is then
\begin{align*}
  f_{\mu, \theta, \sigma \mid \text{data}}(\mu, \theta, \sigma) &\propto   \left(\frac{1}{\sqrt{2 \pi}\sigma}\right)^n  \exp
  \left(-\frac{S(\mu, \theta)}{2 \sigma^2} \right) \times
                                                                  \frac{1}{\sigma}
                                                                  I\{
                                                                  -C <
                                                                  \mu, \theta,
                                                                  \log
                                                                  \sigma
                                                                  <
                                                                  C\}
  \\
  &\propto \sigma^{-n-1} \exp
  \left(-\frac{S(\mu, \theta)}{2 \sigma^2} \right) I\{
                                                                  -C <
                                                                  \mu, \theta,
                                                                  \log
                                                                  \sigma
                                                                  <
                                                                  C\}
\end{align*}
This is the joint posterior of $\mu, \theta, \sigma$. To obtain the posterior of $\mu, \theta$ (without $\sigma$), we integrate the above over $\sigma$ (from 0 to $\infty$). This integration is exactly the same as Lecture 4, and we get
\begin{align*}
   f_{\mu, \theta \mid \text{data}}(\mu, \theta) \propto \left(\frac{1}{S(\mu, \theta)} \right)^{n/2} I\{
                                                                  -C <
                                                                  \mu, \theta
                                                                  <
                                                                  C\} \propto \left(\frac{S(\hat{\mu}, \hat{\theta})}{S(\mu, \theta)} \right)^{n/2} I\{
                                                                  -C <
                                                                  \mu, \theta
                                                                  <
                                                                  C\}
\end{align*}
If $S(\mu, \theta)$ is a quadratic function of $\mu, \theta$, then this will be a $t$-density. However our $S(\mu, \theta)$ will involve higher powers of $\theta$ and is not quadratic. The posterior usually is fairly concentrated around the MLE $(\hat{\mu}, \hat{\theta})$ though, so we it makes sense to approximate $S(\mu, \theta)$ by a quadratic around $(\hat{\mu}, \hat{\theta})$. This is done by Taylor expansion as follows. Let $\alpha = (\mu, \theta)$ and $\hat{\alpha} =
(\hat{\mu}, \hat{\theta})$. Taylor expansion for $\alpha$ near
$\hat{\alpha}$ gives
\begin{align*}
  S(\alpha) &= S(\hat{\alpha}) + \left<\nabla S(\hat{\alpha}), \alpha
              - \hat{\alpha} \right> + \left(\alpha - \hat{\alpha}
              \right)^T \left(\frac{1}{2} HS(\hat{\alpha}) \right) \left(\alpha - \hat{\alpha}
              \right) \\
  &= S(\hat{\alpha}) + \left(\alpha - \hat{\alpha}
              \right)^T \left(\frac{1}{2} HS(\hat{\alpha}) \right) \left(\alpha - \hat{\alpha}
              \right)
\end{align*}
where we used $\nabla S(\hat{\alpha}) = 0$ because $\hat{\alpha}$
minimizes $S(\alpha)$. Here $HS(\hat{\alpha})$ denotes the Hessian of
$S$ at $\hat{\alpha}$.

Therefore
\begin{align*}
 & f_{\mu, \theta \mid \text{data}}(\mu, \theta) \\ &\propto
                                                  \left(\frac{1}{S(\mu,
                                                  \theta)}
                                                  \right)^{n/2}  I\{
                                                  -C < \mu, \theta < C\} \\
  &\propto \left(\frac{S(\hat{\alpha})}{S(\alpha)}
                                                  \right)^{n/2}  I\{
    -C < \mu, \theta < C\} \\
  &= \left(\frac{S(\hat{\alpha})}{S(\hat \alpha) + \left(\alpha - \hat{\alpha}
              \right)^T \left(\frac{1}{2} HS(\hat{\alpha}) \right) \left(\alpha - \hat{\alpha}
              \right)}
                                                  \right)^{n/2}  I\{-C < \mu, \theta < C\} \\
  &= \left(\frac{1}{1 + \left(\alpha - \hat{\alpha}
              \right)^T \left(\frac{1}{2 S(\hat{\alpha})} HS(\hat{\alpha}) \right) \left(\alpha - \hat{\alpha}
              \right)}
                                                  \right)^{n/2}  I\{-C < \mu, \theta < C\} \\
  &= \left(\frac{1}{1 + \frac{1}{n-2}\left(\alpha - \hat{\alpha}
              \right)^T \left(\frac{n-2}{2 S(\hat{\alpha})} HS(\hat{\alpha}) \right) \left(\alpha - \hat{\alpha}
              \right)}
                                                  \right)^{\frac{n-2+2}{2}}  I\{-C < \mu, \theta < C\}.
\end{align*}
Comparing the above with the formula:
\begin{align*}
  \left(\frac{1}{1 + \frac{1}{k} (x - m)^T \Sigma^{-1} (x - m)} \right)^{\frac{k + p}{2}}
\end{align*}
for the $p$-variate $t$-density $t_{k, p}(\mu, \Sigma)$, we see that
(ignoring the indicator function $ I\{-C < \mu, \theta < C\}$)
\begin{align*}
  \alpha \mid \text{data} \sim t_{n-2, 2} \left(\hat{\alpha},
  \frac{S(\hat{\alpha})}{n - 2} \left(\frac{1}{2} HS(\hat{\alpha})
  \right)^{-1} \right).
\end{align*}
So the standard errors corresponding to $\mu$ and $\theta$ can be obtained by taking the square roots of the diagonal entries of
\begin{align*}
\frac{S(\hat{\alpha})}{n - 2} \left(\frac{1}{2} HS(\hat{\alpha})
  \right)^{-1}
\end{align*}
In order to compute these, we need to calculate the Hessian of $S(\alpha)$ with respect to $\alpha$. We will use numerical differentiation (specifically a function from the library numdifftools) for this.

```python
import numdifftools as nd
# this library has functions to calculate first and second derivatives

alphaest = result.x
n = len(dt)
H = nd.Hessian(lambda alpha: S_func(alpha, dt), step = 1e-6)(alphaest)

sighat = np.sqrt(S_func(alphaest, dt) / (n - 2))
covmat = (sighat ** 2) * np.linalg.inv(0.5 * H)
stderrs = np.sqrt(np.diag(covmat))

# ---- Output ----
print("Estimated mu:", alphaest[0])
print("Estimated theta:", alphaest[1])
print("Estimated sigma:", sighat)
print("Covariance matrix:\n", covmat)
print("Standard errors:", stderrs)

#The standard errors of mu and theta reported by ARIMA function are:
print("ARIMA standard errors:", md.bse[0:2])
```

```
Estimated mu: 5.009073896055675
Estimated theta: -0.6582279929829957
Estimated sigma: 0.9824318225976606
Covariance matrix:
 [[ 2.84046626e-04 -2.35806811e-06]
 [-2.35806811e-06  1.33611939e-03]]
Standard errors: [0.01685368 0.03655297]
ARIMA standard errors: [0.01689423 0.03682785]
```

It is easy to see that the standard errors obtained by our formula are very close to the standard errors reported by the ARIMA function.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Varve Dataset from Lecture 21 →](03-varve-dataset-from-lecture-21.md)
