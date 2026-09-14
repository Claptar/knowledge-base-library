---
title: AR(2) Model
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureSixteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureSixteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# AR(2) Model

**Source:** [`CodeLectureSixteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureSixteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

The Yule model is a special case of the AR(2) model. Specifically, the AR(2) model is: $y_t = \phi_0 + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \epsilon_t$ and the Yule model is a special case obtained by taking $\phi_2 = 1$. Below we fit the AR(2) model to the sunspots data (i.e., we estimate all the parameters $\phi_0, \phi_1, \phi_2$).

```python
p = 2 #this is the order of the AR model
n = len(y)
print(n)
```

```
325
```

```python
yreg = y[p:] #these are the response values in the autoregression
Xmat = np.ones((n-p, 1)) #this will be the design matrix (X) in the autoregression
for j in range(1, p+1):
    col = y[p-j : n-j].reshape(-1, 1)
    Xmat = np.column_stack([Xmat, col])
```

```python
armod = sm.OLS(yreg, Xmat).fit()
print(armod.params)
print(armod.summary())
sighat = np.sqrt(np.mean(armod.resid ** 2))
print(sighat)
```

```
[24.45610705  1.38803272 -0.69646032]
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.829
Model:                            OLS   Adj. R-squared:                  0.828
Method:                 Least Squares   F-statistic:                     774.7
Date:                Thu, 23 Oct 2025   Prob (F-statistic):          2.25e-123
Time:                        16:56:04   Log-Likelihood:                -1505.5
No. Observations:                 323   AIC:                             3017.
Df Residuals:                     320   BIC:                             3028.
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         24.4561      2.384     10.260      0.000      19.767      29.146
x1             1.3880      0.040     34.524      0.000       1.309       1.467
x2            -0.6965      0.040    -17.342      0.000      -0.775      -0.617
==============================================================================
Omnibus:                       33.173   Durbin-Watson:                   2.200
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               50.565
Skew:                           0.663   Prob(JB):                     1.05e-11
Kurtosis:                       4.414   Cond. No.                         231.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
25.588082517109108
```

```python
#Simulations from the fitted AR(2) model:
fig, axes = plt.subplots(3, 3, figsize = (12, 6))
axes = axes.flatten()

for j in range(3):
    ysim = y.copy()
    for i in range(2, n):
        err = rng.normal(loc = 0, scale = sighat, size = 1)
        ysim[i] = armod.params[0] + armod.params[1] * ysim[i-1] + armod.params[2] * ysim[i-2] + err[0]
    axes[j].plot(ysim)

axes[3].plot(y)

for j in range(4, 9):
    ysim = y.copy()
    for i in range(2, n):
        err = rng.normal(loc = 0, scale = sighat, size = 1)
        ysim[i] = armod.params[0] + armod.params[1] * ysim[i-1] + armod.params[2] * ysim[i-2] + err[0]
    axes[j].plot(ysim)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

These datasets are still smooth (much smoother than observations simulated from $y_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin(2 \pi f t) + \epsilon_t$).

Below, we obtain predictions using the AR(2) model.

```python
#Generate k-step ahead forecasts:
k = 100
yhat = np.concatenate([y, np.full(k, -9999)]) #extend data by k placeholder values
for i in range(1, k+1):
    ans = armod.params[0]
    for j in range(1, p+1):
        ans += armod.params[j] * yhat[n+i-j-1]
    yhat[n+i-1] = ans
predvalues = yhat[n:]
```

```python
#Plotting the series with forecasts:
plt.figure(figsize=(12, 6))
time_all = np.arange(1, n + k + 1)
plt.plot(time_all, yhat, color='C0')
plt.plot(range(1, n + 1), y, label='Original Data', color='C1')
plt.plot(range(n + 1, n + k + 1), predvalues, label='Forecasts', color='blue')
plt.axvline(x=n, color='black', linestyle='--', label='Forecast Start')
#plt.axhline(y=np.mean(y), color='gray', linestyle=':', label='Mean of Original Data')
plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Time Series + AR(p) Forecasts')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions above are quite different from those obtained from the Yule model. The predictions actually are given by a damped sinusoid (as we shall see in the coming lectures). The predictions become flat after a few time points. When the cycles become irregular with varying periods, constant predictors might do well compared to sinusoidal predictors which may go out of phase at some places.

---

[← Sunspots Data](03-sunspots-data.md) · [Up: contents](index.md)
