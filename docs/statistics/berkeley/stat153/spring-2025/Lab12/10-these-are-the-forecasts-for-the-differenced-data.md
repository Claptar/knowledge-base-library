---
title: these are the forecasts for the differenced data
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# these are the forecasts for the differenced data

**Source:** [`Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

last_observed_y = y.iloc[-1]
fcast_1_arima = np.zeros(k)
fcast_1_arima[0] = last_observed_y + fcast_diff_1_arima[0]
for i in range(1, k):
    fcast_1_arima[i] = fcast_1_arima[i-1] + fcast_diff_1_arima[i]
```

```python
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)


plt.figure(figsize = (12, 7))
plt.plot(tme, np.exp(y), label = 'Data')
plt.plot(tme_future, np.exp(fcast_1), label = 'Forecast (Model One (AutoReg))', color = 'black')
plt.plot(tme_future, np.exp(fcast_1_arima), label = 'Forecast (Model One (ARIMA))', color = 'red')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

One can ask if Model One can be fit directly to the original data via ARIMA(3, 1, 0). This function, by default, will not include an intercept term (i.e., it will fit Model Two). To use the intercept term for the differenced data, one needs to supply the argument 't' for trend as follows.

```python
mod1_arima = ARIMA(y, order=(3, 1, 0), trend='t').fit()
print(mod1_arima.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                TTLCONS   No. Observations:                  386
Model:                 ARIMA(3, 1, 0)   Log Likelihood                1187.247
Date:                Fri, 18 Apr 2025   AIC                          -2364.495
Time:                        09:33:42   BIC                          -2344.729
Sample:                             0   HQIC                         -2356.656
                                - 386
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
x1             0.0041      0.001      3.693      0.000       0.002       0.006
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
```

The output above is basically the same as the output for mod1 (ARIMA(3, 0, 0) applied to diff(y)). With this models, predictions are obtained directly for the original data and there is no need for post-processing to convert them into predictions for the original series.

```python
fcast_y_arima = mod1_arima.get_prediction(start=n, end=n+k-1).predicted_mean

plt.figure(figsize = (12, 7))
plt.plot(tme, np.exp(y), label = 'Data')
plt.plot(tme_future, np.exp(fcast_1), label = 'Forecast (Model One (AutoReg))', color = 'black')
plt.plot(tme_future, np.exp(fcast_1_arima), label = 'Forecast (Model One (ARIMA(3, 0, 0) for diff(y)))', color = 'red')
plt.plot(tme_future, np.exp(fcast_y_arima), label = 'Forecast (Model One (ARIMA(3, 1, 0) for y))', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions are basically the same for the three versions of fitting Model One.

### Model Two

Next we move to Model Two which we fit by applying ARIMA(3, 1, 0) directly to $y_t$ (there is no need to provide any special argument as in trend = '').

```python
mod2 = ARIMA(y, order=(3, 1, 0)).fit()
print(mod2.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                TTLCONS   No. Observations:                  386
Model:                 ARIMA(3, 1, 0)   Log Likelihood                1181.467
Date:                Fri, 18 Apr 2025   AIC                          -2354.934
Time:                        09:33:42   BIC                          -2339.121
Sample:                             0   HQIC                         -2348.662
                                - 386
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          0.2497      0.047      5.316      0.000       0.158       0.342
ar.L2          0.0941      0.042      2.216      0.027       0.011       0.177
ar.L3          0.2363      0.046      5.127      0.000       0.146       0.327
sigma2         0.0001   7.58e-06     16.661      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   1.02   Jarque-Bera (JB):                47.32
Prob(Q):                              0.31   Prob(JB):                         0.00
Heteroskedasticity (H):               0.51   Skew:                            -0.27
Prob(H) (two-sided):                  0.00   Kurtosis:                         4.63
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

This model does not fit a constant term, as can be seen from the regression output above. This lack of constant term affects predictions quite strongly, as seen below.

```python
fcast_2 = mod2.get_prediction(start=n, end=n+k-1).predicted_mean

plt.figure(figsize = (12, 7))
plt.plot(tme, np.exp(y), label = 'Data')
plt.plot(tme_future, np.exp(fcast_y_arima), label = 'Forecast (Model One)', color = 'black')
plt.plot(tme_future, np.exp(fcast_2), label = 'Forecast (Model Two)', color = 'red')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The lack of the intercept term provides bad predictions.

### Model Three

Next we fit Model Three ARIMA(0, 2, 1) to $y$.

```python
mod3 = ARIMA(y, order=(0, 2, 1)).fit()
fcast_3 = mod3.get_prediction(start=n, end=n+k-1).predicted_mean

plt.figure(figsize = (12, 7))
plt.plot(tme, np.exp(y), label = 'Data')
plt.plot(tme_future, np.exp(fcast_y_arima), label = 'Forecast (Model One)', color = 'black')
plt.plot(tme_future, np.exp(fcast_2), label = 'Forecast (Model Two)', color = 'red')
plt.plot(tme_future, np.exp(fcast_3), label = 'Forecast (Model Three)', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Models one and three give somewhat similar predictions.

### Model Four

We fit Model Four by using ARIMA(3, 2, 2) on $y$.

```python
mod4 = ARIMA(y, order=(3, 2, 2)).fit()
fcast_4 = mod4.get_prediction(start=n, end=n+k-1).predicted_mean

plt.figure(figsize = (12, 7))
plt.plot(tme, np.exp(y), label = 'Data')
plt.plot(tme_future, np.exp(fcast_y_arima), label = 'Forecast (Model One)', color = 'black')
plt.plot(tme_future, np.exp(fcast_2), label = 'Forecast (Model Two)', color = 'red')
plt.plot(tme_future, np.exp(fcast_3), label = 'Forecast (Model Three)', color = 'green')
plt.plot(tme_future, np.exp(fcast_4), label = 'Forecast (Model Four)', color = 'blue')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Comparison between Model One and Model Four:

Models 1 and 4 give essentially the same forecast. They appear quite different: Model 1 is AR(3) with intercept applied to diff(y) while Model 4 is ARMA(3, 2) applied to diff(diff(y)) (twice differenced data) without intercept. Why are they giving the same forecast?

```python
print(mod4.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                TTLCONS   No. Observations:                  386
Model:                 ARIMA(3, 2, 2)   Log Likelihood                1184.165
Date:                Fri, 18 Apr 2025   AIC                          -2356.331
Time:                        09:33:43   BIC                          -2332.627
Sample:                             0   HQIC                         -2346.929
                                - 386
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          0.0428      0.592      0.072      0.942      -1.117       1.203
ar.L2         -0.0126      0.071     -0.177      0.860      -0.152       0.127
ar.L3          0.1041      0.062      1.691      0.091      -0.017       0.225
ma.L1         -0.8459      0.602     -1.405      0.160      -2.026       0.334
ma.L2         -0.0603      0.532     -0.113      0.910      -1.102       0.982
sigma2         0.0001   7.51e-06     16.259      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.01   Jarque-Bera (JB):                40.35
Prob(Q):                              0.93   Prob(JB):                         0.00
Heteroskedasticity (H):               0.54   Skew:                            -0.21
Prob(H) (two-sided):                  0.00   Kurtosis:                         4.53
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

## AIC and BIC

In lectures this week, we used AIC and BIC to do model selection. The formulae for AIC and BIC are:
\begin{equation*}
   AIC \text{ for model} = (-2) \times \text{maximized log-likelihood for model} + 2 \times \text{number of parameters in the model}
\end{equation*}
and
\begin{equation*}
     BIC \text{ for model} = (-2) \times \text{maximized log-likelihood for model} + (\log \text{~sample size}) \times \text{number of parameters in the model}
\end{equation*}

Let us compute these for each of the models and check if the answer matches the one given by the model function.

```python
n = len(y)
mod1_aic_formula = -2 * mod1_arima.llf + 2 * len(mod1_arima.params)
mod1_bic_formula = -2 * mod1_arima.llf + (np.log(n - 1)) * len(mod1_arima.params)
print(mod1_aic_formula, mod1_arima.aic)
print(mod1_bic_formula, mod1_arima.bic)

---

[← these are the forecasts for the differenced data](09-these-are-the-forecasts-for-the-differenced-data.md) · [Up: contents](index.md) · [Note that we have used (n - 1) for sample size in the calculation for BIC →](11-note-that-we-have-used-n---1-for-sample-size-in-the-calculat.md)
