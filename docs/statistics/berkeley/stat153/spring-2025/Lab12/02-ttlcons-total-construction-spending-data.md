---
title: TTLCONS (Total Construction Spending Data)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# TTLCONS (Total Construction Spending Data)

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

## Model One

We will difference the data and then fit the AR(3) model. This can be done in two ways. Either we can use AutoReg or ARIMA(3, 0, 0).

```python
mod1_AutoReg = AutoReg(np.diff(y), lags=3).fit()
print(mod1_AutoReg.summary())
# AutoReg uses OLS (also known as conditional MLE) for parameter estimation.

# Alternatively, we can use ARIMA(3, 0, 0). This method uses the full MLE:
mod1 = ARIMA(np.diff(y), order=(3, 0, 0), trend='c').fit()
print(mod1.summary())

# Both these methods give similar but slightly different answers:
print(np.column_stack([mod1_AutoReg.params, mod1.params[:-1]]))
# From this output, we can see that the estimate of the intercept is slightly different (almost double)
# but the remaining estimates are almost the same.
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  385
Model:                     AutoReg(3)   Log Likelihood                1179.667
Method:               Conditional MLE   S.D. of innovations              0.011
Date:                Fri, 18 Apr 2025   AIC                          -2349.335
Time:                        09:33:42   BIC                          -2329.608
Sample:                             3   HQIC                         -2341.509
                                  385
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0021      0.001      3.302      0.001       0.001       0.003
y.L1           0.2148      0.050      4.309      0.000       0.117       0.313
y.L2           0.0636      0.051      1.252      0.211      -0.036       0.163
y.L3           0.2014      0.050      4.047      0.000       0.104       0.299
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.4139           -0.0000j            1.4139           -0.0000
AR.2           -0.8648           -1.6626j            1.8741           -0.3263
AR.3           -0.8648           +1.6626j            1.8741            0.3263
-----------------------------------------------------------------------------
                               SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  385
Model:                 ARIMA(3, 0, 0)   Log Likelihood                1187.247
Date:                Fri, 18 Apr 2025   AIC                          -2364.495
Time:                        09:33:42   BIC                          -2344.729
Sample:                             0   HQIC                         -2356.656
                                - 385
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0041      0.001      3.693      0.000       0.002       0.006
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
[[0.00207946 0.00407175]
 [0.21484133 0.21483792]
 [0.0635657  0.06356862]
 [0.20137871 0.20137351]]
```

The main difference between the parameter estimates from the two different versions of fitting AR(3) to $y_t - y_{t-1}$ is in the intercept estimate (0.0021 vs 0.0041). But the two parameter estimates lead to almost the same predictions. In the code below, predictions are first obtained for the differenced data, and then for the original data.

```python
n = len(y)
k = 100
fcast_diff_1 = mod1_AutoReg.get_prediction(start=n-1, end=n+k-2).predicted_mean
# these are the forecasts for the differenced data
last_observed_y = y.iloc[-1]
fcast_1 = np.zeros(k)
fcast_1[0] = last_observed_y + fcast_diff_1[0]
for i in range(1, k):
    fcast_1[i] = fcast_1[i-1] + fcast_diff_1[i]
```

Next we obtain the forecasts using mod1 (which was fitted using ARIMA(3, 0, 0)).

```python
n = len(y)
k = 100
fcast_diff_1_arima = mod1.get_prediction(start=n-1, end=n+k-2).predicted_mean
# these are the forecasts for the differenced data
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

## Model Two

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

## Model Three

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

## Model Four

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

## Comparison between Model One and Model Four:

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

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [AIC and BIC →](03-aic-and-bic.md)
