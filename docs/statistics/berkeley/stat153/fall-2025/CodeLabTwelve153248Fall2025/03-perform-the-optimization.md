---
title: Perform the optimization
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTwelve153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Perform the optimization

**Source:** [`CodeLabTwelve153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

result = minimize(S_func, init_params, args=(dt,))
print(result)
mu_hat, theta_hat = result.x

print("Estimated mu:", mu_hat)
print("Estimated theta:", theta_hat)
```

```
message: Optimization terminated successfully.
  success: True
   status: 0
      fun: 384.13856984891936
        x: [ 5.009e+00 -6.582e-01]
      nit: 10
      jac: [ 0.000e+00  0.000e+00]
 hess_inv: [[ 1.476e-04 -1.728e-06]
            [-1.728e-06  6.930e-04]]
     nfev: 51
     njev: 17
Estimated mu: 5.009073896055675
Estimated theta: -0.6582279929829957
```

```python
print(result.x)
print(md.params)
```

```
[ 5.0090739  -0.65822799]
[ 5.00917415 -0.65657733  0.96028995]
```

The estimates of $\mu$ and $\theta$ obtained by minimizing $S(\mu, \theta)$ are clearly very close to those reported by the ARIMA function. The estimate of $\sigma$ is given by $\sqrt{S(\hat{\mu}, \hat{\theta})/n}$.

```python
sigma_hat = np.sqrt(S_func(result.x, dt) / len(dt))
print("Estimated sigma:", sigma_hat)
print("ARIMA reported sigma:", np.sqrt(md.params[2]))
```

```
Estimated sigma: 0.9799726652424028
ARIMA reported sigma: 0.9799438524963823
```

## Standard Errors corresponding to the parameter estimates

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

---

[← Initial guess: [muinit, thetainit]](02-initial-guess-muinit-thetainit.md) · [Up: contents](index.md) · [this library has functions to calculate first and second derivatives →](04-this-library-has-functions-to-calculate-first-and-second-der.md)
