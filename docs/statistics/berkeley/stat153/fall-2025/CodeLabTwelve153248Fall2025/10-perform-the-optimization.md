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
      fun: 149.0042362521212
        x: [-1.137e-03 -7.728e-01]
      nit: 12
      jac: [ 0.000e+00  0.000e+00]
 hess_inv: [[ 4.132e-05  4.927e-06]
            [ 4.927e-06  2.550e-03]]
     nfev: 63
     njev: 21
Estimated mu: -0.0011366484142282629
Estimated theta: -0.7728310145141554
```

```python
print(result.x)
print(mamod.params)
```

```
[-0.00113665 -0.77283101]
[-0.00125667 -0.77099236  0.23528045]
```

```python
sigma_hat = np.sqrt(S_func(result.x, dt) / len(dt))
print("Estimated sigma:", sigma_hat)
print("MA reported sigma:", np.sqrt(mamod.params[2]))
```

```
Estimated sigma: 0.485173925675123
MA reported sigma: 0.4850571581949342
```

The estimates are very close to each other. Below are the standard errors.

```python
alphaest = result.x
n = len(dt)
H = nd.Hessian(lambda alpha: S_func(alpha, dt), step = 1e-6)(alphaest)

sighat = np.sqrt(S_func(alphaest, dt) / (n - 2))
covmat = (sighat ** 2) * np.linalg.inv(0.5 * H)
stderrs = np.sqrt(np.diag(covmat))

---

[← Initial guess: [muinit, thetainit]](09-initial-guess-muinit-thetainit.md) · [Up: contents](index.md) · [---- Output ---- →](11------output.md)
