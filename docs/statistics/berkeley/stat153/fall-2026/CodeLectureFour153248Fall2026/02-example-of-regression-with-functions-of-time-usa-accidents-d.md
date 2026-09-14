---
title: 'Example of Regression with functions of time: USA Accidents Dataset'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFour153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureFour153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Example of Regression with functions of time: USA Accidents Dataset

**Source:** [`CodeLectureFour153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFour153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

This dataset was inbuilt in R. I have saved it as "USAccDeaths.csv".

```python
USAccDeaths = pd.read_csv("USAccDeaths.csv")
dt = USAccDeaths['x']
plt.plot(dt)
plt.xlabel("Time (months) from 1973 to 1978")
plt.ylabel("Number of accidental deaths")
plt.title("Number of accidental deaths in  USA")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

To this data, below we fit the model:
\begin{align*}
   y_t &= \beta_0 + \beta_{11} \cos(2 \pi f_1 t/12) + \beta_{12} \sin(2 \pi f_1 t/12) \\ &+ \beta_{21} \cos(2 \pi f_2 t/12) + \beta_{22} \sin(2 \pi f_2 t/12) \\ &+ \beta_{31} \cos(2 \pi f_3 t/12) + \beta_{32} \sin(2 \pi f_3 t/12) + \epsilon_t.
\end{align*}
with fixed frequencies $f_1 = 1$, $f_2 = 2$ and $f_3 = 3$.

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

X = np.column_stack([v1, v2, v3, v4, v5, v6])
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
Dep. Variable:                      x   R-squared:                       0.706
Model:                            OLS   Adj. R-squared:                  0.679
Method:                 Least Squares   F-statistic:                     25.98
Date:                Tue, 08 Sep 2026   Prob (F-statistic):           1.60e-15
Time:                        18:54:09   Log-Likelihood:                -551.88
No. Observations:                  72   AIC:                             1118.
Df Residuals:                      65   BIC:                             1134.
Df Model:                           6
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       8788.7917     63.995    137.336      0.000    8660.985    8916.598
x1          -734.1918     90.502     -8.112      0.000    -914.937    -553.446
x2          -711.3231     90.502     -7.860      0.000    -892.069    -530.578
x3           408.0417     90.502      4.509      0.000     227.296     588.787
x4            97.1151     90.502      1.073      0.287     -83.630     277.861
x5           145.9722     90.502      1.613      0.112     -34.773     326.718
x6          -185.6111     90.502     -2.051      0.044    -366.357      -4.866
==============================================================================
Omnibus:                        5.033   Durbin-Watson:                   0.900
Prob(Omnibus):                  0.081   Jarque-Bera (JB):                4.860
Skew:                           0.635   Prob(JB):                       0.0880
Kurtosis:                       2.912   Cond. No.                         1.41
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

*(1 figure omitted — see the original notebook.)*

```python
h = 60
n = len(dt)
t = np.arange(1, n + h + 1)

cols = []
for k in (1, 2, 3):
    cols += [np.cos(2*np.pi*k*t/12), np.sin(2*np.pi*k*t/12)]
X = sm.add_constant(np.column_stack(cols))

mod = sm.OLS(dt, X[:n]).fit()
print(mod.summary())
pred = mod.predict(X[n:])

plt.figure(figsize=(11, 6))
plt.plot(t[:n], dt, 'o-', color='blue', label='Observed')
#plt.plot(t[:n], mod.fittedvalues, color='red', label='Fitted')
plt.plot(t[n:], pred, color='green', ls='--', label='Forecast (5 yrs)')
plt.xlabel("Time (months from Jan 1973)")
plt.ylabel("Deaths")
plt.title("US accidental deaths: 5-year forecast")
plt.legend()
plt.show()
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      x   R-squared:                       0.706
Model:                            OLS   Adj. R-squared:                  0.679
Method:                 Least Squares   F-statistic:                     25.98
Date:                Tue, 08 Sep 2026   Prob (F-statistic):           1.60e-15
Time:                        18:54:39   Log-Likelihood:                -551.88
No. Observations:                  72   AIC:                             1118.
Df Residuals:                      65   BIC:                             1134.
Df Model:                           6
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       8788.7917     63.995    137.336      0.000    8660.985    8916.598
x1          -734.1918     90.502     -8.112      0.000    -914.937    -553.446
x2          -711.3231     90.502     -7.860      0.000    -892.069    -530.578
x3           408.0417     90.502      4.509      0.000     227.296     588.787
x4            97.1151     90.502      1.073      0.287     -83.630     277.861
x5           145.9722     90.502      1.613      0.112     -34.773     326.718
x6          -185.6111     90.502     -2.051      0.044    -366.357      -4.866
==============================================================================
Omnibus:                        5.033   Durbin-Watson:                   0.900
Prob(Omnibus):                  0.081   Jarque-Bera (JB):                4.860
Skew:                           0.635   Prob(JB):                       0.0880
Kurtosis:                       2.912   Cond. No.                         1.41
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

*(1 figure omitted — see the original notebook.)*

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Example of Lagged or Auto Regression →](03-example-of-lagged-or-auto-regression.md)
