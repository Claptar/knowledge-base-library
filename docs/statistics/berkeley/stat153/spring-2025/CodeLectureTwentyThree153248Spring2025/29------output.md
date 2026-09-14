---
title: '---- Output ----'
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyThree153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ---- Output ----

**Source:** [`CodeLectureTwentyThree153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyThree153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print("Estimated mu:", alphaest[0])
print("Estimated theta:", alphaest[1])
print("Estimated sigma:", sighat)
print("Covariance matrix:\n", covmat)
print("Standard errors:", stderrs)
```

```
Estimated mu: 0.03934764631035018
Estimated theta: -0.569755702273577
Estimated sigma: 112.78237853564474
Covariance matrix:
 [[ 6.07038956e+00 -5.25557790e-04]
 [-5.25557790e-04  1.18250503e-03]]
Standard errors: [2.46381606 0.03438757]
```

These standard errors seem close to those given by ARIMA.

---

[← Perform the optimization](28-perform-the-optimization.md) · [Up: contents](index.md)
