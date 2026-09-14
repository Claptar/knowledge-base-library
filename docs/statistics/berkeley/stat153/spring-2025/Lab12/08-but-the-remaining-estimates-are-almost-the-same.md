---
title: but the remaining estimates are almost the same.
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# but the remaining estimates are almost the same.

**Source:** [`Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  385
Model:                     AutoReg(3)   Log Likelihood                1179.667
Method:               Conditional MLE   S.D. of innovations              0.011
Date:                Fri, 18 Apr 2025   AIC                          -2349.335
Time:                        09:33:42   BIC                          -2329.608
Sample:                             3   HQIC                         -2341.509
                                  385
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0021      0.001      3.302      0.001       0.001       0.003
y.L1           0.2148      0.050      4.309      0.000       0.117       0.313
y.L2           0.0636      0.051      1.252      0.211      -0.036       0.163
y.L3           0.2014      0.050      4.047      0.000       0.104       0.299
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.4139           -0.0000j            1.4139           -0.0000
AR.2           -0.8648           -1.6626j            1.8741           -0.3263
AR.3           -0.8648           +1.6626j            1.8741            0.3263
-----------------------------------------------------------------------------
                               SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  385
Model:                 ARIMA(3, 0, 0)   Log Likelihood                1187.247
Date:                Fri, 18 Apr 2025   AIC                          -2364.495
Time:                        09:33:42   BIC                          -2344.729
Sample:                             0   HQIC                         -2356.656
                                - 385
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0041      0.001      3.693      0.000       0.002       0.006
ar.L1          0.2148      0.046      4.717      0.000       0.126       0.304
ar.L2          0.0636      0.045      1.425      0.154      -0.024       0.151
ar.L3          0.2014      0.048      4.199      0.000       0.107       0.295
sigma2         0.0001    7.2e-06     17.040      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.14   Jarque-Bera (JB):                43.88
Prob(Q):                              0.70   Prob(JB):                         0.00
Heteroskedasticity (H):               0.50   Skew:                            -0.27
Prob(H) (two-sided):                  0.00   Kurtosis:                         4.56
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
[[0.00207946 0.00407175]
 [0.21484133 0.21483792]
 [0.0635657  0.06356862]
 [0.20137871 0.20137351]]
```

The main difference between the parameter estimates from the two different versions of fitting AR(3) to $y_t - y_{t-1}$ is in the intercept estimate (0.0021 vs 0.0041). But the two parameter estimates lead to almost the same predictions. In the code below, predictions are first obtained for the differenced data, and then for the original data.

```python
n = len(y)
k = 100
fcast_diff_1 = mod1_AutoReg.get_prediction(start=n-1, end=n+k-2).predicted_mean

---

[← Lab12 Part 07 —](07-lab12-part-07.md) · [Up: contents](index.md) · [these are the forecasts for the differenced data →](09-these-are-the-forecasts-for-the-differenced-data.md)
