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
      fun: 5011626.773814039
        x: [ 3.935e-02 -5.698e-01]
      nit: 14
      jac: [ 0.000e+00  0.000e+00]
 hess_inv: [[ 6.139e-06 -3.174e-07]
            [-3.174e-07  7.938e-08]]
     nfev: 72
     njev: 24
Estimated mu: 0.03934764631035018
Estimated theta: -0.569755702273577
```

The estimated $\theta$ is quite close to that given by ARIMA. The estimate of $\mu$ seems slightly off from that given by ARIMA. Standard errors are computed below.

```python
import numdifftools as nd #this library has functions to calculate first and second derivatives

H = nd.Hessian(lambda alpha: S_func(alpha, dt), step = 1e-6)(alphaest)

sighat = np.sqrt(S_func(alphaest, dt) / (n - 2))
covmat = (sighat ** 2) * np.linalg.inv(0.5 * H)
stderrs = np.sqrt(np.diag(covmat))

---

[← Initial guess: [muinit, thetainit]](27-initial-guess-muinit-thetainit.md) · [Up: contents](index.md) · [---- Output ---- →](29------output.md)
