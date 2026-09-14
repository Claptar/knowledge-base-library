---
title: AR(p) Models and Stationarity
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwenty153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwenty153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# AR(p) Models and Stationarity

**Source:** [`CodeLectureTwenty153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwenty153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Consider fitting AR($p$) models starting with $p = 1$ to the following GNP dataset (from https://fred.stlouisfed.org/series/GNP). This is quarterly data.

```python
gnp = pd.read_csv("GNP_30Oct2025.csv")
print(gnp.head())
y = gnp['GNP'].to_numpy()
plt.plot(y, color = 'black')
plt.show()
```

```
observation_date      GNP
0       1947-01-01  244.142
1       1947-04-01  247.063
2       1947-07-01  250.716
3       1947-10-01  260.981
4       1948-01-01  267.133
```

*(1 figure omitted — see the original notebook.)*

As usual, we fit AR($p$) models using the AutoReg function.

```python
armd = AutoReg(y, lags = 1).fit()
print(armd.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  314
Model:                     AutoReg(1)   Log Likelihood               -2054.516
Method:               Conditional MLE   S.D. of innovations            171.573
Date:                Fri, 07 Nov 2025   AIC                           4115.031
Time:                        14:45:08   BIC                           4126.270
Sample:                             1   HQIC                          4119.523
                                  314
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          8.8687     13.423      0.661      0.509     -17.439      35.176
y.L1           1.0116      0.001    827.008      0.000       1.009       1.014
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            0.9886           +0.0000j            0.9886            0.0000
-----------------------------------------------------------------------------
```

Is the above fitted AR(1) model causal-stationary? For an AR(1) causal-stationarity happens when $|\phi_1| < 1$. Here the fitted value for $\phi_1$ equals $1.0116$ which exceeds 1. So this model is not causal stationary. In fact, from the plot of the GNP dataset, it should be clear that a stationary model will not be appropriate for it. Predictions based on this fitted AR(1) model will become exponentially large (as the prediction horizon increases) which makese sense (given the nature of the data).

---

[Up: contents](index.md) · [Preprocessing using logarithms and differences →](02-preprocessing-using-logarithms-and-differences.md)
