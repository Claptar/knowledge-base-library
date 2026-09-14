---
title: Perform the optimization
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyThree153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Perform the optimization

**Source:** [`CodeLectureTwentyThree153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

result = minimize(S_func, init_params, args=(dt,))
print(result)
mu_hat, theta_hat = result.x
alphaest = result.x

print("Estimated mu:", mu_hat)
print("Estimated theta:", theta_hat)
```

```
message: Optimization terminated successfully.
  success: True
   status: 0
      fun: 349.95037593379897
        x: [-3.971e-03 -7.474e-01]
      nit: 12
      jac: [ 3.815e-06  0.000e+00]
 hess_inv: [[ 7.978e-05 -1.413e-06]
            [-1.413e-06  6.066e-04]]
     nfev: 60
     njev: 20
Estimated mu: -0.00397079554935901
Estimated theta: -0.747415904826925
```

The estimates are quite close to those obtained by ARIMA.

To obtain the standard errors for uncertainty quantification, we shall use the formula given at the end of the notes for Lecture 23. This formula involves calculating the Hessian matrix of $S(\mu, \theta)$ at the point estimates $\hat{\mu}$ and $\hat{\theta}$. We shall use the python library numdifftools for numerically evaluating the Hessian of $S(\mu, \theta)$.

```python
import numdifftools as nd #this library has functions to calculate first and second derivatives

H = nd.Hessian(lambda alpha: S_func(alpha, dt), step = 1e-6)(alphaest)

sighat = np.sqrt(S_func(alphaest, dt) / (n - 2))
covmat = (sighat ** 2) * np.linalg.inv(0.5 * H)
stderrs = np.sqrt(np.diag(covmat))

---

[← Initial guess: [muinit, thetainit]](24-initial-guess-muinit-thetainit.md) · [Up: contents](index.md) · [---- Output ---- →](26------output.md)
