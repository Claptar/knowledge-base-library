---
title: these are the coefficients of the characteristic polynomial
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# these are the coefficients of the characteristic polynomial

**Source:** [`CodeLabTen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

---

[← these pacf values start with the value 1 at lag 0.](05-these-pacf-values-start-with-the-value-1-at-lag-0.md) · [Up: contents](index.md) · [Extract coefficients for the characteristic polynomial →](07-extract-coefficients-for-the-characteristic-polynomial.md)
