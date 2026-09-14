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
Estimated mu: -0.00397079554935901
Estimated theta: -0.747415904826925
Estimated sigma: 0.9424430612455296
Covariance matrix:
 [[ 1.41671210e-04 -2.63105421e-06]
 [-2.63105421e-06  1.07831062e-03]]
Standard errors: [0.01190257 0.03283764]
```

The obtained standard errors are also close to those obtained from ARIMA.

### One more example

Here is one more example where we can check that our estimates and their standard errors for parameters in MA(1) are close to those obtained from the ARIMA function.

```python
beersales = pd.read_csv('MRTSSM4453USN_March2025.csv')
y = beersales['MRTSSM4453USN']
ydiff12 = y.diff(periods = 12)
y2d = ydiff12.diff()
dt = y2d.dropna().to_numpy()
```

Below we fit MA(1) via the ARIMA function.

```python
ma_mod = ARIMA(dt, order = (0, 0, 1)).fit()
print(ma_mod.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  383
Model:                 ARIMA(0, 0, 1)   Log Likelihood               -2358.779
Date:                Sat, 19 Apr 2025   AIC                           4723.558
Time:                        01:20:09   BIC                           4735.402
Sample:                             0   HQIC                          4728.256
                                - 383
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.1714      2.575      0.067      0.947      -4.876       5.219
ma.L1         -0.5697      0.028    -20.263      0.000      -0.625      -0.515
sigma2      1.308e+04    652.547     20.037      0.000    1.18e+04    1.44e+04
===================================================================================
Ljung-Box (L1) (Q):                   6.31   Jarque-Bera (JB):               125.42
Prob(Q):                              0.01   Prob(JB):                         0.00
Heteroskedasticity (H):               5.26   Skew:                            -0.21
Prob(H) (two-sided):                  0.00   Kurtosis:                         5.77
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Next we fit MA(1) using our method.

```python

---

[← Perform the optimization](25-perform-the-optimization.md) · [Up: contents](index.md) · [Initial guess: [muinit, thetainit] →](27-initial-guess-muinit-thetainit.md)
