---
title: 'Dataset Two: simulated dataset'
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureSeventeen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureSeventeen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Dataset Two: simulated dataset

**Source:** [`CodeLectureSeventeen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureSeventeen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

AR(1) predictions behave quite differently in the three regimes $\phi_1 < 1$, $\phi_1 = 1$ and $\phi_1 > 1$. To see this, consider the simulated dataset below.

```python
seed = 43
rng = np.random.default_rng(seed)
n = 400
sig = 0.5
ysim = np.zeros(n)
for i in range(2, n):
    err = rng.normal(loc = 0, scale = sig, size = 1)
    phi_0 = 0.1
    phi_1 = 1
    ysim[i] = phi_0 + phi_1 * ysim[i-1] + err[0]
plt.figure(figsize = (12, 6))
plt.plot(ysim)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
p = 1
armod_sm = AutoReg(ysim, lags = p, trend = 'c').fit()
print(armod_sm.summary())
k = 1000
predvalues_sm = armod_sm.predict(start = n, end = n+k-1)
yhat = np.concatenate([ysim, predvalues_sm])
plt.figure(figsize=(12, 6))
time_all = np.arange(1, n + k + 1)
plt.plot(time_all, yhat, color='C0', label="Extended Series with Forecasts")
plt.plot(range(1, n + 1), ysim, label='Original Data', color='C1')
plt.plot(range(n + 1, n + k + 1), predvalues_sm, label='Forecasts (Statsmodels AutoReg)', color='blue')
plt.axvline(x=n, color='black', linestyle='--', label='Forecast Start')
plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Time Series + AR(p) Forecasts')
plt.legend()
plt.show()
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  400
Model:                     AutoReg(1)   Log Likelihood                -283.472
Method:               Conditional MLE   S.D. of innovations              0.492
Date:                Sat, 22 Mar 2025   AIC                            572.945
Time:                        15:05:19   BIC                            584.911
Sample:                             1   HQIC                           577.684
                                  400
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0705      0.037      1.891      0.059      -0.003       0.144
y.L1           1.0021      0.002    555.249      0.000       0.999       1.006
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            0.9979           +0.0000j            0.9979            0.0000
-----------------------------------------------------------------------------
```

*(1 figure omitted — see the original notebook.)*

The estimated $\phi_1$ is more than 1 and the predictions are exponential. If we forcibly set the $\phi_1$ parameter to be 1, the predictions will be linear. This is done below.

```python
k = 1000
yhat = np.concatenate([ysim, np.full(k, -9999)]) #extend data by k placeholder values
phi_vals = np.array([armod_sm.params[0], 1]) #\phi_1 parameter is set to 1
for i in range(1, k+1):
    ans = phi_vals[0]
    for j in range(1, p+1):
        ans += phi_vals[j] * yhat[n+i-j-1]
    yhat[n+i-1] = ans
predvalues = yhat[n:]

#Plotting the series with forecasts:
plt.figure(figsize=(12, 6))
time_all = np.arange(1, n + k + 1)
plt.plot(time_all, yhat, color='C0')
plt.plot(range(1, n + 1), ysim, label='Original Data', color='C1')
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

Now for the following simulated dataset, the estimated $\phi_1$ is slightly smaller than 1. This leads to predictions that decay to a constant.

```python
seed = 123
rng = np.random.default_rng(seed)
n = 400
sig = 0.5
ysim = np.zeros(n)
for i in range(2, n):
    err = rng.normal(loc = 0, scale = sig, size = 1)
    phi_0 = 0.1
    phi_1 = 1
    ysim[i] = phi_0 + phi_1 * ysim[i-1] + err[0]
plt.figure(figsize = (12, 6))
plt.plot(ysim)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
p = 1
armod_sm = AutoReg(ysim, lags = p, trend = 'c').fit()
print(armod_sm.summary())
k = 1000
predvalues_sm = armod_sm.predict(start = n, end = n+k-1)
yhat = np.concatenate([ysim, predvalues_sm])
plt.figure(figsize=(12, 6))
time_all = np.arange(1, n + k + 1)
plt.plot(time_all, yhat, color='C0', label="Extended Series with Forecasts")
plt.plot(range(1, n + 1), ysim, label='Original Data', color='C1')
plt.plot(range(n + 1, n + k + 1), predvalues_sm, label='Forecasts (Statsmodels AutoReg)', color='blue')
plt.axvline(x=n, color='black', linestyle='--', label='Forecast Start')
plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Time Series + AR(p) Forecasts')
plt.legend()
plt.show()
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  400
Model:                     AutoReg(1)   Log Likelihood                -289.700
Method:               Conditional MLE   S.D. of innovations              0.500
Date:                Sat, 22 Mar 2025   AIC                            585.400
Time:                        15:06:45   BIC                            597.367
Sample:                             1   HQIC                           590.140
                                  400
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.1857      0.055      3.391      0.001       0.078       0.293
y.L1           0.9974      0.002    538.039      0.000       0.994       1.001
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.0026           +0.0000j            1.0026            0.0000
-----------------------------------------------------------------------------
```

*(1 figure omitted — see the original notebook.)*

Again, if we force $\phi_1$ to equal 1, the predictions will be linear.

```python
k = 1000
yhat = np.concatenate([ysim, np.full(k, -9999)]) #extend data by k placeholder values
phi_vals = np.array([armod_sm.params[0], 1]) #\phi_1 parameter is set to 1
for i in range(1, k+1):
    ans = phi_vals[0]
    for j in range(1, p+1):
        ans += phi_vals[j] * yhat[n+i-j-1]
    yhat[n+i-1] = ans
predvalues = yhat[n:]

#Plotting the series with forecasts:
plt.figure(figsize=(12, 6))
time_all = np.arange(1, n + k + 1)
plt.plot(time_all, yhat, color='C0')
plt.plot(range(1, n + 1), ysim, label='Original Data', color='C1')
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

---

[← Dataset One: California Population](02-dataset-one-california-population.md) · [Up: contents](index.md) · [Dataset Three: Sunspots →](04-dataset-three-sunspots.md)
