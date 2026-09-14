---
title: (since we are dealing with a pure AR process, there is no theta coefficient)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# (since we are dealing with a pure AR process, there is no theta coefficient)

**Source:** [`Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

AR2_process = ArmaProcess(ar, ma)
nlags = 20

ma_infinity = AR2_process.arma2ma(lags=nlags) # this gives \psi_j, j = 0, \dots, lags-1

psi_j = np.array([
    (2 / np.sqrt(3)) * (0.5) ** j * np.sin((j + 1) * np.pi / 3)
    for j in range(nlags)
])

print(np.column_stack([psi_j, ma_infinity]))
```

```
[[ 1.00000000e+00  1.00000000e+00]
 [ 5.00000000e-01  5.00000000e-01]
 [ 3.53525080e-17  0.00000000e+00]
 [-1.25000000e-01 -1.25000000e-01]
 [-6.25000000e-02 -6.25000000e-02]
 [-8.83812699e-18  0.00000000e+00]
 [ 1.56250000e-02  1.56250000e-02]
 [ 7.81250000e-03  7.81250000e-03]
 [ 1.65714881e-18  0.00000000e+00]
 [-1.95312500e-03 -1.95312500e-03]
 [-9.76562500e-04 -9.76562500e-04]
 [-2.76191468e-19  0.00000000e+00]
 [ 2.44140625e-04  2.44140625e-04]
 [ 1.22070313e-04  1.22070312e-04]
 [ 1.68347800e-19  0.00000000e+00]
 [-3.05175781e-05 -3.05175781e-05]
 [-1.52587891e-05 -1.52587891e-05]
 [-6.47323754e-21  0.00000000e+00]
 [ 3.81469727e-06  3.81469727e-06]
 [ 1.90734863e-06  1.90734863e-06]]
```

## TTLCONS (Total Construction Spending Data)

In Lecture 22, we fit ARIMA models to the following dataset.

```python
ttlcons = pd.read_csv('TTLCONS_14April2025.csv')
print(ttlcons.head())

y = np.log(ttlcons['TTLCONS']) # note that we are taking logarithms
print(len(y))

plt.figure(figsize = (12, 6))
plt.plot(y)
plt.xlabel('Time (months)')
plt.show()
```

```
observation_date  TTLCONS
0       1993-01-01   458080
1       1993-02-01   462967
2       1993-03-01   458399
3       1993-04-01   469425
4       1993-05-01   468998
386
```

*(1 figure omitted — see the original notebook.)*

We fitted the following models to $\{y_t\}$ (here $y_t$ is log of the data from FRED)
1. AR(3) for $y_t - y_{t-1}$: $$y_t - y_{t-1} = \phi_0 + \phi_1 (y_{t-1} - y_{t-2}) + \phi_2 (y_{t-2} - y_{t-3}) + \phi_3 (y_{t-3} - y_{t-4}) + \epsilon_t$$
2. ARIMA(3, 1, 0) for $y_t$: $$y_t - y_{t-1} = \phi_1 (y_{t-1} - y_{t-2}) + \phi_2 (y_{t-2} - y_{t-3}) + \phi_3 (y_{t-3} - y_{t-4}) + \epsilon_t$$ (the only difference betwen this model and the previous one is the absence of the $\phi_0$ term)
3. ARIMA(0, 2, 1) for $y_t$: $$y_t - 2 y_{t-1} + y_{t-2} = \epsilon_t + \theta \epsilon_{t-1}$$
4. ARIMA(3, 2, 2) for $y_t$: $$y_{t} - 2 y_{t-1} + y_{t-2} - \phi_1 \left(y_{t-1} - 2 y_{t-2} + y_{t-3} \right) - \phi_2 \left(y_{t-2} - 2 y_{t-3} + y_{t-4} \right) - \phi_3 \left(y_{t-3} - 2 y_{t-4} + y_{t-5} \right) = \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2}$$

Note that there is no intercept term in models 2, 3, and 4.

Here is the code for fitting each of these models.

### Model One

We will difference the data and then fit the AR(3) model. This can be done in two ways. Either we can use AutoReg or ARIMA(3, 0, 0).

```python
mod1_AutoReg = AutoReg(np.diff(y), lags=3).fit()
print(mod1_AutoReg.summary())

---

[← these are the theta-coefficients of the ARMA process](02-these-are-the-theta-coefficients-of-the-arma-process.md) · [Up: contents](index.md) · [AutoReg uses OLS (also known as conditional MLE) for parameter estimation. →](04-autoreg-uses-ols-also-known-as-conditional-mle-for-parameter.md)
