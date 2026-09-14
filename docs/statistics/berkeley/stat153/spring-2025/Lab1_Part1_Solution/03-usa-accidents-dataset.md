---
title: USA Accidents Dataset
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab1_Part1_Solution.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab1_Part1_Solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# USA Accidents Dataset

**Source:** [`Lab1_Part1_Solution.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab1_Part1_Solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

This dataset was inbuilt in R. I have saved it as "USAccDeaths.csv".

```python
USAccDeaths = pd.read_csv("USAccDeaths.csv")
print(USAccDeaths.head(10))
print(USAccDeaths.tail(10))
print(USAccDeaths.shape)
```

```
Unnamed: 0      x
0           1   9007
1           2   8106
2           3   8928
3           4   9137
4           5  10017
5           6  10826
6           7  11317
7           8  10744
8           9   9713
9          10   9938
    Unnamed: 0      x
62          63   7791
63          64   8192
64          65   9115
65          66   9434
66          67  10484
67          68   9827
68          69   9110
69          70   9070
70          71   8633
71          72   9240
(72, 2)
```

```python
dt = USAccDeaths['x']
plt.plot(dt)
plt.xlabel("Time (months) from 1973 to 1978")
plt.ylabel("Number of accidental deaths")
plt.title("Number of accidental deaths in  USA")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Problem 2
Fit a sinusoids + quadratic multiple regression model to the data.

```python
t = np.arange(1, len(dt) + 1)

f1, f2, f3 = 1, 2, 3
d = 12

v1 = np.cos(2 * np.pi * f1 * t/d)
v2 = np.sin(2 * np.pi * f1 * t/d)
v3 = np.cos(2 * np.pi * f2 * t/d)
v4 = np.sin(2 * np.pi * f2 * t/d)
v5 = np.cos(2 * np.pi * f3 * t/d)
v6 = np.sin(2 * np.pi * f3 * t/d)

v7 = t
v8 = t ** 2

X = np.column_stack([v1, v2, v3, v4, v5, v6, v7, v8])
X = sm.add_constant(X)

lin_mod = sm.OLS(dt, X).fit()
print(lin_mod.summary())

plt.figure(figsize = (10, 6))
plt.plot(t, dt, label = "USA Accidental Deaths", marker = 'o', linestyle = '-', color = 'blue')
plt.plot(t, lin_mod.fittedvalues, label = 'Fitted', color = 'red', linestyle = '-')
plt.xlabel("Time")
plt.ylabel("Deaths")
plt.title("Monthly totals of accidental deaths in the US (1973-1978)")
plt.legend()
plt.show()
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      x   R-squared:                       0.881
Model:                            OLS   Adj. R-squared:                  0.866
Method:                 Least Squares   F-statistic:                     58.54
Date:                Thu, 23 Jan 2025   Prob (F-statistic):           2.93e-26
Time:                        23:54:49   Log-Likelihood:                -519.15
No. Observations:                  72   AIC:                             1056.
Df Residuals:                      63   BIC:                             1077.
Df Model:                           8
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       9957.8596    127.837     77.895      0.000    9702.397    1.02e+04
x1          -734.1366     58.404    -12.570      0.000    -850.847    -617.426
x2          -757.6844     58.832    -12.879      0.000    -875.250    -640.119
x3           417.1503     58.386      7.145      0.000     300.476     533.825
x4            75.5988     58.454      1.293      0.201     -41.213     192.410
x5           156.7378     58.385      2.685      0.009      40.065     273.411
x6          -198.0336     58.385     -3.392      0.001    -314.706     -81.361
x7           -72.0713      8.056     -8.946      0.000     -88.171     -55.972
x8             0.8285      0.107      7.752      0.000       0.615       1.042
==============================================================================
Omnibus:                        1.222   Durbin-Watson:                   2.216
Prob(Omnibus):                  0.543   Jarque-Bera (JB):                1.034
Skew:                          -0.043   Prob(JB):                        0.596
Kurtosis:                       2.419   Cond. No.                     7.33e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 7.33e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

*(1 figure omitted — see the original notebook.)*

---

[← Plot the original dataset along with the fitted values](02-plot-the-original-dataset-along-with-the-fitted-values.md) · [Up: contents](index.md)
