---
title: AutoReg's estimate of phi1 is slightly more than 1
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# AutoReg's estimate of phi1 is slightly more than 1

**Source:** [`CodeLabEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

md_arima_y = ARIMA(y, order = (1, 0, 0)).fit()
print(md_arima_y.params[1])
#ARIMA's estimate is less than 1 (even though quite close to 1)
#Also ARIMA gives an error/warning that initial parameters that is is using are out of the stationary region.
```

```
1.0115582545835275
0.9999135070206702
/Users/dohyeongki/miniconda3/envs/stat153/lib/python3.12/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
  warn('Non-stationary starting autoregressive parameters'
```

ARIMA can be used directly on ylog (as opposed to ylogdiff). In this case, we have to give $d = 1$ (as opposed to $d = 0$).

```python
md_ylog = ARIMA(ylog*100, order = (1, 1, 0)).fit() # note that now d = 1
print(md_ylog.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  314
Model:                 ARIMA(1, 1, 0)   Log Likelihood                -561.194
Date:                Sat, 15 Nov 2025   AIC                           1126.388
Time:                        16:52:44   BIC                           1133.880
Sample:                             0   HQIC                          1129.382
                                - 314
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          0.6898      0.030     23.035      0.000       0.631       0.748
sigma2         2.1085      0.078     27.061      0.000       1.956       2.261
===================================================================================
Ljung-Box (L1) (Q):                  61.43   Jarque-Bera (JB):             21878.01
Prob(Q):                              0.00   Prob(JB):                         0.00
Heteroskedasticity (H):               2.00   Skew:                             2.64
Prob(H) (two-sided):                  0.00   Kurtosis:                        43.62
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

The difference now is that the $\mu$ parameter is no longer present. In other words, the model that is fit here is:
\begin{align*}
   100 \left( \log y_t - \log y_{t-1} \right) = \phi_1 100 \left( \log y_{t-1} - \log y_{t-2} \right) + \epsilon_t.
\end{align*}
Whenever the differencing order is 1 or more, ARIMA does not use the intercept parameter. This makes a noticeable difference in predictions however.

```python
k = 100
n = len(ylog)
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)

fcast = md_ylog.get_prediction(start = n, end = n+k-1)
fcast_mean = fcast.predicted_mean # this gives the point predictions
plt.plot(tme, ylog*100, label = 'Data')
plt.plot(tme_future, fcast_mean, label = 'Forecast (ARIMA on ylog with d = 1)', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

On the other hand, if we use the model on ylogdiff, then the predictions for ylog are computed in the following way. We basically obtain predictions for the differenced series, and then use the predictions for $y_{n+1} - y_n, y_{n+2} - y_{n+1}, \dots, y_{n+k}-y_{n+k-1}$ to get predictions for $y_{n+1}, \dots, y_{n+k}$. This is done by taking telescoping sums of $y_{n+1} - y_n, y_{n+2} - y_{n+1}, \dots, y_{n+k}-y_{n+k-1}$, and then adding $y_n$.

```python
n = len(y)
k = 100
fcast_diff_1 = md_arima.get_prediction(start = n-1, end = n+k-2).predicted_mean #these are the forecasts for the differenced data
last_observed_ylog = 100*ylog[-1]
fcast_1 = np.zeros(k)
fcast_1[0] = last_observed_ylog + fcast_diff_1[0]
for i in range(1, k):
    fcast_1[i] = fcast_1[i-1] + fcast_diff_1[i]
```

```python
plt.plot(tme, ylog*100, label = 'Data')
plt.plot(tme_future, fcast_mean, label = 'Forecast (ARIMA on ylog with d = 1)', color = 'green')
plt.plot(tme_future, fcast_1, label = 'Forecast (ARIMA on ylogdiff with d = 0)', color = 'red')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

So here the presence of the intercept is leading to more intuitive predictions.

## TTLCONS

In Lecture 21, we fit ARIMA models to the following dataset.

```python
ttlcons = pd.read_csv('TTLCONS_13Nov2025.csv')
print(ttlcons.head())
y = ttlcons['TTLCONS'].to_numpy()
print(len(y))
plt.plot(y)
plt.title('Total Construction Spending')
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
391
```

*(1 figure omitted — see the original notebook.)*

Let us revisit that analysis here again. We fit models to the logarithm of the data.

```python
ylog = np.log(y)
plt.plot(ylog, color = 'black')
plt.title('Log of Total Construction Spending')
plt.xlabel('Time (months)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We can obtain candidate models by differencing the data, and looking at acf and pacf.

```python
ylogdiff = 100 * np.diff(ylog)
plt.plot(ylogdiff, color = 'black')
plt.title('Percent change in Total Construction Spending')
plt.xlabel('Time (months)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))
plot_acf(ylogdiff, lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF")
plot_pacf(ylogdiff, lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF")
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

These plots suggest:
1. AR(3) for the differenced log data
2. MA(6) for the differenced log data
3. ARIMA(3, 1, 0) for the log data (this is technically the same as Model 1 but the ARIMA function does not include intercepts while fitting this model so it can lead to different predictions)
4. ARIMA(0, 1, 6) for the log data

We can also take another difference of the data, and then look at acf and pacf.

```python
ylogdiff2 = np.diff(np.diff(ylog))
plt.plot(ylogdiff2)
plt.title("Double Differenced Data")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1)
plot_acf(ylogdiff2, lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF")
plot_pacf(ylogdiff2, lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF")
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

This suggests the ARIMA(0, 2, 1) model for ylog.

Here is how to calculate the predictions for each of the five models.

```python
k = 100
n = len(ylog)
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
```

First is Model One: AR(3) for the differenced log data.

```python

---

[← Below we fit these models to the original data without any differencing or logging.](05-below-we-fit-these-models-to-the-original-data-without-any-d.md) · [Up: contents](index.md) · [Model One: AR(3) for the differenced log data →](07-model-one-ar-3-for-the-differenced-log-data.md)
