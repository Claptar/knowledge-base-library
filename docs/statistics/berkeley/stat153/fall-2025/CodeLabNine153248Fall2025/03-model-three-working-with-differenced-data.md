---
title: 'Model Three: Working with Differenced Data'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabNine153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabNine153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLabNine153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabNine153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Model Three: Working with Differenced Data

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
    lower, upper = conf_ints[-1,:]
    if (lower < 0 < upper):
        print(f"Stopping at p = {p} because 0 is in the phi_{p} interval")
        break
    p += 1
if p >= max_p:
    print(f"Reached p = {max_p} without finding a phi_p interval containing 0")
p = p-1 # note that if the algorithm outputs p = 4, we should take p = 3
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
Date:                Fri, 31 Oct 2025   AIC                          -1726.889
Time:                        19:31:09   BIC                          -1712.169
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
fcast = armod_sm.get_prediction(start = n_train-1, end = n_train+k-2)
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
    log_forecast[i] = log_forecast[i-1] + fcast_mean[i]
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
phi_vals = np.array([armod_sm.params[0], armod_sm.params[1] + 1, armod_sm.params[2] - armod_sm.params[1], -armod_sm.params[2]]) #these are the fitted coefficients in the AR(3) model derived from AR(2) applied to the differences
armod_nodiff = AutoReg(ylog_train, lags = 3).fit()
print(np.column_stack([phi_vals, armod_nodiff.params]))
```

```
[[ 0.00924128  0.02014238]
 [ 1.194775    1.17303216]
 [ 0.01035034  0.0029458 ]
 [-0.20512534 -0.17724759]]
```

It is interesting that the parameter estimates are somewhat similar but not exactly the same.

With this AR(3) model for $\log \text{GNP}_t$ that is derived from the AR(2) model for $y_t = \log \text{GNP}_t - \log \text{GNP}_{t-1}$, we can obtain predictions in the usual way as follows.

```python
yhat = np.concatenate([ylog_train.astype(float), np.full(k, -9999)])
# extend data by k placeholder values
p = len(phi_vals)-1
for i in range(1, k+1):
    ans = phi_vals[0]
    for j in range(1, p+1):
        ans += phi_vals[j] * yhat[n_train+i-j-1]
    yhat[n_train+i-1] = ans
predvalues = yhat[n_train:]
print(predvalues)
```

```
[10.0401751  10.05858192 10.07752672 10.09423368 10.11061512 10.12647412
 10.14216459 10.15771507 10.17320371 10.18865159 10.20407884 10.21949372
 10.23490196 10.25030637 10.26570866 10.28110976]
```

These predictions coincide with the predictions obtained previously.

```python
plt.figure(figsize = (12, 7))
plt.plot(tme_train, y_train, label = 'Training Data')
plt.plot(tme_test, original_scale_forecast, label = 'Forecast', color = 'black')
plt.plot(tme_test, np.exp(predvalues), label = 'Forecast', color = 'green')
plt.plot(tme_test, y_test, color = 'red',  label = 'Actual future values')
plt.axvline(x=n_train, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The green and black predictions coincide above.

To conclude, predictions from the AR(3) model applied directly to the $\log \text{GNP}$ data are different from the predictions obtained by AR(2) fitted to the differences of $\log \text{GNP}$. It is quite common, while using AR models, to work with differenced data.

---

[← Model Two: AR(p) model on the log(data)](02-model-two-ar-p-model-on-the-log-data.md) · [Up: contents](index.md)
