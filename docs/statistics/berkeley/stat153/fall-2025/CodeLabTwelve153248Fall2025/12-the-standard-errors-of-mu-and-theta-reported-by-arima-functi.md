---
title: The standard errors of mu and theta reported by ARIMA function are
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTwelve153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# The standard errors of mu and theta reported by ARIMA function are

**Source:** [`CodeLabTwelve153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwelve153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print("MA standard errors:", md.bse[0:2])
```

```
Estimated mu: -0.0011366484142282629
Estimated theta: -0.7728310145141554
Estimated sigma: 0.48594221424137307
Covariance matrix:
 [[1.94152441e-05 8.29322690e-07]
 [8.29322690e-07 1.17034011e-03]]
Standard errors: [0.00440627 0.03421023]
MA standard errors: [0.01689423 0.03682785]
```

The standard error corresponding to $\mu$ that we computed is a little off from the one reported by the ARIMA function, but the standard errors corresponding to $\theta$ are almost the same.

Note that we did not calculate standard errors for $\sigma$. This can be done by calculating the posterior of $\sigma$ (this can be written in terms of the chi-squared distribution).

The ARIMA function works with the full likelihood unlike the analysis above which works with the conditional likelihood (conditioning on $\epsilon_0 = 0$). So the answers will be slightly different. The full likelihood is more complicated to write down.

---

[← ---- Output ----](11------output.md) · [Up: contents](index.md)
