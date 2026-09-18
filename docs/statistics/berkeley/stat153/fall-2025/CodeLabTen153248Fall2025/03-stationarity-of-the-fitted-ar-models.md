---
title: Stationarity of the Fitted AR models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLabTen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTen153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Stationarity of the Fitted AR models

Let us check whether the fitted AR models are causal stationary.

```python
print(armd_2.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  325
Model:                     AutoReg(2)   Log Likelihood               -1505.524
Method:               Conditional MLE   S.D. of innovations             25.588
Date:                Mon, 10 Nov 2025   AIC                           3019.048
Time:                        12:45:28   BIC                           3034.159
Sample:                             2   HQIC                          3025.080
                                  325
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         24.4561      2.372     10.308      0.000      19.806      29.106
y.L1           1.3880      0.040     34.685      0.000       1.310       1.466
y.L2          -0.6965      0.040    -17.423      0.000      -0.775      -0.618
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            0.9965           -0.6655j            1.1983           -0.0937
AR.2            0.9965           +0.6655j            1.1983            0.0937
-----------------------------------------------------------------------------
```

The roots and their modulus are actually given as part of the above summary output (the moduli are strictly larger than 1 so this model is causal stationary). We can also compute the AR polynomial roots and their moduli as follows.

```python
#characteristic polynomial
coeffs = [(-1)*armd_2.params[2], (-1)*armd_2.params[1], 1]
# these are the coefficients of the characteristic polynomial
roots = np.roots(coeffs) # these are the roots of the characteristic polynomial
print(coeffs)
print(roots)
magnitudes = np.abs(roots)
print(magnitudes)
```

```
[0.6964603222695153, -1.388032716491234, 1]
[0.99649088+0.66546067j 0.99649088-0.66546067j]
[1.19826206 1.19826206]
```

Now let us check whether the fitted AR(9) model is causal and stationary.

```python
print(armd_9.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  325
Model:                     AutoReg(9)   Log Likelihood               -1443.314
Method:               Conditional MLE   S.D. of innovations             23.301
Date:                Mon, 10 Nov 2025   AIC                           2908.628
Time:                        12:45:28   BIC                           2949.941
Sample:                             9   HQIC                          2925.132
                                  325
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         12.7820      4.002      3.194      0.001       4.938      20.626
y.L1           1.1720      0.055     21.338      0.000       1.064       1.280
y.L2          -0.4207      0.086     -4.905      0.000      -0.589      -0.253
y.L3          -0.1350      0.089     -1.525      0.127      -0.309       0.039
y.L4           0.1013      0.088      1.149      0.251      -0.072       0.274
y.L5          -0.0666      0.088     -0.757      0.449      -0.239       0.106
y.L6           0.0018      0.088      0.021      0.983      -0.171       0.174
y.L7           0.0151      0.088      0.173      0.863      -0.157       0.187
y.L8          -0.0430      0.085     -0.508      0.612      -0.209       0.123
y.L9           0.2177      0.054      3.999      0.000       0.111       0.324
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.0701           -0.0000j            1.0701           -0.0000
AR.2            0.8499           -0.5728j            1.0249           -0.0944
AR.3            0.8499           +0.5728j            1.0249            0.0944
AR.4            0.4186           -1.0985j            1.1756           -0.1921
AR.5            0.4186           +1.0985j            1.1756            0.1921
AR.6           -0.4824           -1.2224j            1.3142           -0.3098
AR.7           -0.4824           +1.2224j            1.3142            0.3098
AR.8           -1.2225           -0.4668j            1.3086           -0.4419
AR.9           -1.2225           +0.4668j            1.3086            0.4419
-----------------------------------------------------------------------------
```

All roots have magnitudes strictly larger than 1 so this is also a causal and stationary  model. These roots and their magnitudes can also be computed as follows.

```python
# Extract coefficients for the characteristic polynomial
coeffs = [(-1) * armd_9.params[i] for i in range(9, 0, -1)] # Reverse order: lags 9→1
coeffs.append(1)
roots = np.roots(coeffs)
magnitudes = np.abs(roots)
print(magnitudes)
```

```
[1.30855577 1.30855577 1.31416814 1.31416814 1.17555576 1.17555576
 1.07010924 1.02490237 1.02490237]
```

These magnitudes coincide with the values in the table although the order in which they are listed in the table may be different (there is no default ordering for displaying the roots).

---

[← AR order selection through PACF](02-ar-order-selection-through-pacf.md) · [Up: contents](index.md)
