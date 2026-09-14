---
title: Check that both predictions are identical
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Check that both predictions are identical

**Source:** [`Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print(np.column_stack([predvalues, fcast_mean]))
```

```
[[22015.82610003 22015.82610003]
 [22297.35726353 22297.35726353]
 [22577.46189255 22577.46189255]
 [22733.34849543 22733.34849543]
 [22927.7624808  22927.7624808 ]
 [23143.75177595 23143.75177595]
 [23346.56851705 23346.56851705]
 [23550.37282678 23550.37282678]
 [23759.57018454 23759.57018454]
 [23969.4607915  23969.4607915 ]
 [24180.3448357  24180.3448357 ]
 [24393.30052786 24393.30052786]
 [24607.96390436 24607.96390436]
 [24824.19709577 24824.19709577]
 [25042.14861695 25042.14861695]
 [25261.82954785 25261.82954785]]
```

Below we plot the predictions along with the datapoints from the test set (actual last 16 observations) that we previously set aside.

```python
plt.figure(figsize = (12, 7))
plt.plot(tme_train, y_train, label = 'Training Data')
plt.plot(tme_test, fcast_mean, label = 'Forecast', color = 'black')
plt.plot(tme_test, y_test, color = 'red', label = 'Actual future values')
plt.axvline(x=n_train, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions by the AR(3) model are decent but there are not very accurate.

## Model Two: AR(p) model on the log(data)

Instead of fitting AR(p) models directly on the observed GNP training data, it makes sense to fit them to the logarithmed data. This method will also give predictions on the log-scale, which will need to be exponentiated to obtain predictions on the original scale.

```python
ylog_train = np.log(y_train)
ylog_test = np.log(y_test)
```

Here is the code for the automatic procedure that iteratively fits AR(p) models, starting from $p = 1$ and incrementing $p$ by 1 each time, until the 95% confidence interval for $\phi_p$ (the lag-p coefficient) includes 0 (the procedure then stops and reports the last model).

```python
max_p = 20
p = 1
while p <= max_p:
    armd = AutoReg(ylog_train, lags = p).fit()
    conf_ints = armd.conf_int(alpha = 0.05)
    lower, upper = conf_ints.iloc[-1]
    # sometimes this is throwing an error saying that conf_ints is not a pandas array
    # (in such cases, use conf_ints[-1,:])
    if (lower < 0 < upper):
        print(f"Stopping at p = {p} because 0 is in the phi_{p} interval")
        break
    p += 1
if p >= max_p:
    print(f"Reached p = {max_p} without finding a phi_p interval containing 0")
p = p - 1 # note that if the algorithm outputs p = 4, we should take p = 3

print(p)
```

```
Stopping at p = 4 because 0 is in the phi_4 interval
3
```

Now let us fit the AR(p) model (with $p$ selected as above) to the logarithm of the GNP data.

```python
armod_sm = AutoReg(ylog_train, lags = p).fit()
print(armod_sm.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                    GNP   No. Observations:                  296
Model:                     AutoReg(3)   Log Likelihood                 870.225
Method:               Conditional MLE   S.D. of innovations              0.012
Date:                Thu, 03 Apr 2025   AIC                          -1730.451
Time:                        21:06:22   BIC                          -1712.050
Sample:                             3   HQIC                         -1723.081
                                  296
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0201      0.005      4.213      0.000       0.011       0.030
GNP.L1         1.1730      0.058     20.342      0.000       1.060       1.286
GNP.L2         0.0029      0.093      0.032      0.975      -0.179       0.184
GNP.L3        -0.1772      0.061     -2.906      0.004      -0.297      -0.058
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.0020           +0.0000j            1.0020            0.0000
AR.2            1.9309           +0.0000j            1.9309            0.0000
AR.3           -2.9162           +0.0000j            2.9162            0.5000
-----------------------------------------------------------------------------
```

Below we predict the next 16 values.

```python
k = 16
fcast = armod_sm.get_prediction(start = n_train, end = n_train + k - 1)
fcast_mean = fcast.predicted_mean # this gives the point predictions
```

```python
plt.figure(figsize = (12, 7))
plt.plot(tme_train, y_train, label = 'Training Data')
plt.plot(tme_test, np.exp(fcast_mean), label = 'Forecast', color = 'black') # Note the exponentiation
plt.plot(tme_test, y_test, color = 'red',  label = 'Actual future values')
plt.axvline(x=n_train, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Compare these predictions with those obtained from Method One. The predictions from Model Two seem closer (compared to Model One) to the actual values but the accuracy is still not very good.

## Model Three: Working with Differenced Data

Instead of working with log GNP data, it is common to work their differences:
\begin{equation*}
   y_t = \log \text{GNP}_t - \log \text{GNP}_{t-1} = \log \frac{\text{GNP}_{t}}{\text{GNP}_{t-1}}
\end{equation*}
Because $\log x \approx x-1$, as we remarked previously, $100 y_t$ represents the percentage change in GNP from year $t-1$ to year $t$.

The differenced log-data look very different from the original data and the log-data.

```python
ylogdiff_train = np.diff(ylog_train)

plt.figure(figsize = (12, 6))
plt.plot(ylogdiff_train)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Notice that the differenced log-data has  no "trend". The trend has been removed by differencing.

```python
max_p = 20
p = 1
while p <= max_p:
    armd = AutoReg(ylogdiff_train, lags = p).fit()
    conf_ints = armd.conf_int(alpha = 0.05)
    lower, upper = conf_ints[-1, :]
    if (lower < 0 < upper):
        print(f"Stopping at p = {p} because 0 is in the phi_{p} interval")
        break
    p += 1
if p >= max_p:
    print(f"Reached p = {max_p} without finding a phi_p interval containing 0")
p = p-1 #note that if the algorithm outputs p = 4, we should take p = 3

print(p)
```

```
Stopping at p = 3 because 0 is in the phi_3 interval
2
```

We now fit the AR model with the chosen $p$.

```python
armod_sm = AutoReg(ylogdiff_train, lags = p, trend = 'c').fit()
print(armod_sm.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  295
Model:                     AutoReg(2)   Log Likelihood                 867.445
Method:               Conditional MLE   S.D. of innovations              0.013
Date:                Thu, 03 Apr 2025   AIC                          -1726.889
Time:                        21:06:22   BIC                          -1712.169
Sample:                             2   HQIC                         -1720.993
                                  295
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0092      0.001      7.030      0.000       0.007       0.012
y.L1           0.1948      0.057      3.389      0.001       0.082       0.307
y.L2           0.2051      0.060      3.395      0.001       0.087       0.324
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.7837           +0.0000j            1.7837            0.0000
AR.2           -2.7332           +0.0000j            2.7332            0.5000
-----------------------------------------------------------------------------
```

Now we obtain predictions. We can use the same method as before to generate predictions for the future 16 values.

```python
k = 16
fcast = armod_sm.get_prediction(start = n_train - 1, end = n_train + k - 2)
fcast_mean = fcast.predicted_mean # this gives the point predictions
```

However that these predictions are for the differenced log-data (they are not for the original data). To be clear, suppose $y_t$ denotes $\log(\text{GNP}_t)$. Then we obtained predictions for the future 16 values of $y_t - y_{t-1}$ i.e., $y_{n+1} - y_n, y_{n+2} - y_{n+1}, ..., y_{n+k} - y_{n+k-1}$. But we need predictions for $y_t$ not for these differences. To compute the predictions for $y_t$, we can simply do the following:
\begin{equation*}
   \hat{y}_{n+1} = y_n + \widehat{y_{n+1} - y_n}
\end{equation*}
and
\begin{equation*}
   \hat{y}_{n+2} = \hat{y}_{n+1} + \widehat{y_{n+2} - y_{n+1}}
\end{equation*}
and so on recursively computing $\hat{y}_{n+3}$, $\hat{y}_{n+4}$ etc. This process is implemented in the code below. Note that we have to exponentiate the predictions for $y_t$ in the end because for $\text{GNP}_t = \exp(y_t)$.

```python
last_observed_log = ylog_train.iloc[-1]
log_forecast = np.zeros(k)
log_forecast[0] = last_observed_log + fcast_mean[0]
for i in range(1, k):
    log_forecast[i] = log_forecast[i - 1] + fcast_mean[i]
original_scale_forecast = np.exp(log_forecast)
```

Below we plot these predictions along with the actual test values.

```python
plt.figure(figsize = (12, 7))
plt.plot(tme_train, y_train, label = 'Training Data')
plt.plot(tme_test, original_scale_forecast, label = 'Forecast', color = 'black')
plt.plot(tme_test, y_test, color = 'red',  label = 'Actual future values')
plt.axvline(x=n_train, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is very interesting that these predictions are much more accurate compared to the predictions obtained by the previous two models. This suggests that AR(p) models are better for the difference log-data than for the log-data without differencing (and also for the original data).

The following is another way of obtaining the predictions for the original data from the model fitted to the differenced data. The AR(2) model that we just fitted to $y_t = \log \text{GNP}_t - \log \text{GNP}_{t-1}$ is:
\begin{equation*}
   y_t = \hat{\phi}_0 + \hat{\phi}_1 y_{t-1} + \hat{\phi}_2 y_{t-2} + \epsilon_t
\end{equation*}
If we replace $y_t$ by $\log \text{GNP}_t - \log \text{GNP}_{t-1}$ and rewrite the equation above, we obtain:
\begin{equation*}
   \log \text{GNP}_t = \hat{\phi}_0 + (\hat{\phi}_1 + 1) \log \text{GNP}_{t-1} + \left(\hat{\phi}_2 - \hat{\phi}_1 \right) \log \text{GNP}_{t-2} - \hat{\phi}_2 \log \text{GNP}_{t-3} + \epsilon_t
\end{equation*}
Thus in terms of $\log \text{GNP}_t$, the fitted model can be interpreted as an AR(3) model. However, it is a special kind of AR(3) model (for example, the sum of the fitted coefficients for $\log \text{GNP}_{t-1}$, $\log \text{GNP}_{t-2}$, $\log \text{GNP}_{t-3}$ equals 0). We can compare this special AR(3) model to the model obtained by fitting AR(3) to the $\log \text{GNP}_t$ data:

```python
phi_vals = np.array([armod_sm.params[0], armod_sm.params[1] + 1,
                     armod_sm.params[2] - armod_sm.params[1], -armod_sm.params[2]])

---

[← Predictions](06-predictions.md) · [Up: contents](index.md) · [Lab10 Part 08 — →](08-lab10-part-08.md)
