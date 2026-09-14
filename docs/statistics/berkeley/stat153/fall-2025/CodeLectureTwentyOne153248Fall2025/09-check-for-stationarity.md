---
title: Check for stationarity
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Check for stationarity

**Source:** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

if np.all(moduli > 1):
    print("The model is causal and stationary.")
else:
    print("The model is NOT stationary (some roots have modulus ≤ 1).")
```

```
AR(4) coefficients (on original data):
a1 = 1.2221, a2 = -0.1577, a3 = 0.1433, a4 = -0.2077

Roots of the characteristic polynomial:
Root 1: 1.0000+0.0000j,  Modulus: 1.0000
Root 2: 0.7166+0.0000j,  Modulus: 0.7166
Root 3: -0.2472+0.4783j,  Modulus: 0.5384
Root 4: -0.2472-0.4783j,  Modulus: 0.5384
The model is NOT stationary (some roots have modulus ≤ 1).
```

Predictions can be made based on the AR(4) model fitted above.

```python
#The following are the coefficients of the above AR(4) model:
phi_vals = np.array([armod.params[0], armod.params[1] + 1, armod.params[2] - armod.params[1], armod.params[3]-armod.params[2], -armod.params[3]])
print(phi_vals)
k = 100
n = len(y)
yhat = np.concatenate([y.astype(float), np.full(k, -9999)]) #extend data by k placeholder values
p = len(phi_vals)-1
for i in range(1, k+1):
    ans = phi_vals[0]
    for j in range(1, p+1):
        ans += phi_vals[j] * yhat[n+i-j-1]
    yhat[n+i-1] = ans
predvalues = yhat[n:]
print(predvalues)
```

```
[ 0.00194823  1.22210763 -0.15767478  0.14326653 -0.20769939]
[14.5770252  14.57834935 14.58052477 14.58327511 14.5862494  14.58948729
 14.59291757 14.59645407 14.60008131 14.60377551 14.6075125  14.61128214
 14.61507571 14.61888557 14.62270738 14.62653787 14.63037443 14.63421539
 14.63805951 14.64190589 14.64575388 14.64960303 14.65345301 14.65730359
 14.66115459 14.6650059  14.66885742 14.67270911 14.67656091 14.68041278
 14.68426472 14.68811669 14.6919687  14.69582073 14.69967277 14.70352482
 14.70737688 14.71122895 14.71508102 14.71893309 14.72278517 14.72663724
 14.73048932 14.7343414  14.73819348 14.74204556 14.74589764 14.74974972
 14.7536018  14.75745388 14.76130596 14.76515804 14.76901012 14.7728622
 14.77671428 14.78056636 14.78441844 14.78827052 14.7921226  14.79597468
 14.79982677 14.80367885 14.80753093 14.81138301 14.81523509 14.81908717
 14.82293925 14.82679133 14.83064341 14.83449549 14.83834757 14.84219965
 14.84605173 14.84990381 14.85375589 14.85760797 14.86146005 14.86531213
 14.86916422 14.8730163  14.87686838 14.88072046 14.88457254 14.88842462
 14.8922767  14.89612878 14.89998086 14.90383294 14.90768502 14.9115371
 14.91538918 14.91924126 14.92309334 14.92694542 14.9307975  14.93464959
 14.93850167 14.94235375 14.94620583 14.95005791]
```

Let us plot these predictions along with the original data (on the log-scale and then on the orginal scale).

```python
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
plt.plot(tme, y, label = 'Data')
plt.plot(tme_future, predvalues, label = 'Forecast', color = 'black')
plt.axvline(x=n, color='gray', linestyle='--')
plt.title('Log Scale')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
plt.plot(tme, np.exp(y), label = 'Data')
plt.plot(tme_future, np.exp(predvalues), label = 'Forecast', color = 'black')
plt.axvline(x=n, color='gray', linestyle='--')
plt.title('Original Scale')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### AR(3) without intercept

To illustrate a technical point, suppose that we don't want an intercept term while fitting the AR(3) model after differencing. We can do this by setting **trend = 'n'** in AutoReg as follows.

```python
p = 3
armod_nointercept = AutoReg(ydiff, lags = p, trend = 'n').fit()
print(armod_nointercept.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  390
Model:                     AutoReg(3)   Log Likelihood                1193.843
Method:               Conditional MLE   S.D. of innovations              0.011
Date:                Thu, 13 Nov 2025   AIC                          -2379.686
Time:                        16:54:50   BIC                          -2363.852
Sample:                             3   HQIC                         -2373.408
                                  390
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
y.L1           0.2542      0.049      5.185      0.000       0.158       0.350
y.L2           0.0923      0.050      1.837      0.066      -0.006       0.191
y.L3           0.2400      0.049      4.909      0.000       0.144       0.336
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.2919           -0.0000j            1.2919           -0.0000
AR.2           -0.8383           -1.5882j            1.7959           -0.3273
AR.3           -0.8383           +1.5882j            1.7959            0.3273
-----------------------------------------------------------------------------
```

The above AR(3) model is also in the causal stationary regime. It can be converted to the following AR(4) model for the original (undifferenced) $y_t$:
\begin{equation*}
   y_t = (1 + \hat{\phi}_1) y_{t-1} + (\hat{\phi}_2 - \hat{\phi}_1) y_{t-2} + (\hat{\phi}_3 - \hat{\phi}_2) y_{t-3} - \hat{\phi}_3 y_{t-4} + \epsilon_t.
\end{equation*}

```python
print(armod_nointercept.params)
phi_vals_nointercept = np.array([0, armod_nointercept.params[0] + 1, armod_nointercept.params[1] - armod_nointercept.params[0], armod_nointercept.params[2]-armod_nointercept.params[1], -armod_nointercept.params[2]])
print(phi_vals_nointercept)
```

```
[0.25418633 0.09234799 0.2400083 ]
[ 0.          1.25418633 -0.16183835  0.14766032 -0.2400083 ]
```

Predictions using this AR model (which does not have an intercept) are computed as follows.

```python
yhat = np.concatenate([y.astype(float), np.full(k, -9999)]) #extend data by k placeholder values
p = len(phi_vals_nointercept)-1
for i in range(1, k+1):
    ans = phi_vals_nointercept[0]
    for j in range(1, p+1):
        ans += phi_vals_nointercept[j] * yhat[n+i-j-1]
    yhat[n+i-1] = ans
predvalues_nointercept = yhat[n:]
print(predvalues_nointercept)
```

```
[14.57487898 14.57359749 14.57301636 14.57250515 14.57201397 14.57170244
 14.5714552  14.57124569 14.57109484 14.57097781 14.57088384 14.57081295
 14.57075816 14.57071513 14.57068212 14.57065661 14.57063675 14.57062142
 14.57060957 14.57060037 14.57059326 14.57058776 14.5705835  14.5705802
 14.57057765 14.57057567 14.57057414 14.57057296 14.57057204 14.57057133
 14.57057078 14.57057036 14.57057003 14.57056977 14.57056958 14.57056942
 14.5705693  14.57056921 14.57056914 14.57056909 14.57056905 14.57056901
 14.57056899 14.57056897 14.57056895 14.57056894 14.57056893 14.57056892
 14.57056892 14.57056891 14.57056891 14.57056891 14.57056891 14.57056891
 14.5705689  14.5705689  14.5705689  14.5705689  14.5705689  14.5705689
 14.5705689  14.5705689  14.5705689  14.5705689  14.5705689  14.5705689
 14.5705689  14.5705689  14.5705689  14.5705689  14.5705689  14.5705689
 14.5705689  14.5705689  14.5705689  14.5705689  14.5705689  14.5705689
 14.5705689  14.5705689  14.5705689  14.5705689  14.5705689  14.5705689
 14.5705689  14.5705689  14.5705689  14.5705689  14.5705689  14.5705689
 14.5705689  14.5705689  14.5705689  14.5705689  14.5705689  14.5705689
 14.5705689  14.5705689  14.5705689  14.5705689 ]
```

Let us plot the different predictions together.

```python
plt.plot(tme, np.exp(y), label = 'Data')
plt.plot(tme_future, np.exp(predvalues), label = 'Forecast (with intercept)', color = 'black')
plt.plot(tme_future, np.exp(predvalues_nointercept), label = 'Forecast (no intercept)', color = 'red')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The two predictions are quite different. The absence of the intercept term seems to make a big difference in the predictions in this example.

### Model Fitting and Prediction using the function ARIMA

Below, we fit the AR(3) model to the differenced data $y_t - y_{t-1}$ using the ARIMA function with order $(3, 1, 0)$. Note that the ARIMA function is applied directly to the original data $y_t$ (and not to the differenced series).

```python
ar_arima = ARIMA(y, order = (3, 1, 0)).fit()
print(ar_arima.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                TTLCONS   No. Observations:                  391
Model:                 ARIMA(3, 1, 0)   Log Likelihood                1200.965
Date:                Thu, 13 Nov 2025   AIC                          -2393.930
Time:                        16:56:04   BIC                          -2378.066
Sample:                             0   HQIC                         -2387.642
                                - 391
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          0.2542      0.046      5.516      0.000       0.164       0.345
ar.L2          0.0923      0.042      2.217      0.027       0.011       0.174
ar.L3          0.2400      0.045      5.293      0.000       0.151       0.329
sigma2         0.0001   7.34e-06     16.845      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.99   Jarque-Bera (JB):                47.28
Prob(Q):                              0.32   Prob(JB):                         0.00
Heteroskedasticity (H):               0.48   Skew:                            -0.23
Prob(H) (two-sided):                  0.00   Kurtosis:                         4.64
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

One thing to note is that the ARIMA function does not fit a intercept term by default when the differencing order $d \geq 1$. Below we obtain forecasts for the data using the fitted ARIMA model. The predictions outputted by the get_prediction() function directly applies to $y_t$ (there is no need to do any conversion of the predictions of the differenced series to predictions of the original series; these conversions are automatically done by the get_prediction() function).

```python
fcast = ar_arima.get_prediction(start = n, end = n+k-1)
fcast_mean = fcast.predicted_mean #this gives the point predictions
plt.plot(tme, np.exp(y), label = 'Data')
plt.plot(tme_future, np.exp(predvalues), label = 'Forecast (AutoReg)', color = 'black')
plt.plot(tme_future, np.exp(predvalues_nointercept), label = 'Forecast (AutoReg with no intercept)', color = 'red')
plt.plot(tme_future, np.exp(fcast_mean), label = 'Forecast (ARIMA)', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions obtained by the ARIMA model coincide with those obtained by the AutoReg model with no intercept.

### Double Differenced Data (ARIMA models with d = 2)

The differenced series (ydiff) plotted above might be said to have some trends. One can get rid of these by differencing the series again.

```python
ydiff2 = np.diff(np.diff(y))
plt.figure(figsize = (12, 7))
plt.plot(ydiff2)
plt.title("Double Differenced Data")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us look at the sample acf and pacf of the double differenced data.

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1)
plot_acf(ydiff2, lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF")
plot_pacf(ydiff2, lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF")
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

From the ACF above, MA(1) is a simple model that can be used for this double-difference data. We shall fit this model. Instead of fitting the model to the double-differenced data, we can directly use ARIMA with order (0, 2, 1) to the original data. This model can then be used to obtain forecasts for the original data directly.

```python
ma_arima = ARIMA(y, order = (0, 2, 1)).fit()
print(ma_arima.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                TTLCONS   No. Observations:                  391
Model:                 ARIMA(0, 2, 1)   Log Likelihood                1199.732
Date:                Thu, 13 Nov 2025   AIC                          -2395.464
Time:                        16:57:39   BIC                          -2387.537
Sample:                             0   HQIC                         -2392.321
                                - 391
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ma.L1         -0.8730      0.026    -33.690      0.000      -0.924      -0.822
sigma2         0.0001   6.74e-06     18.126      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   1.68   Jarque-Bera (JB):                47.87
Prob(Q):                              0.20   Prob(JB):                         0.00
Heteroskedasticity (H):               0.55   Skew:                            -0.20
Prob(H) (two-sided):                  0.00   Kurtosis:                         4.67
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

The model that is fit here is: $y_t - 2 y_{t-1} + y_{t-2} = \epsilon_t + \theta \epsilon_{t-1}$. Note that there is no mean term $\mu$ on the right hand side.

```python
fcast_ma = ma_arima.get_prediction(start = n, end = n+k-1)
fcast_mean_ma = fcast_ma.predicted_mean #this gives the point predictions
plt.plot(tme, np.exp(y), label = 'Data')
plt.plot(tme_future, np.exp(predvalues), label = 'Forecast (AR(3) with intercept on differenced data)', color = 'black')
plt.plot(tme_future, np.exp(fcast_mean), label = 'Forecast (AR(3) without intercept on differenced data)', color = 'green')
plt.plot(tme_future, np.exp(fcast_mean_ma), label = 'Forecast (MA(1) on twice differenced data)', color = 'red')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

This example illustrates that these different models can give predictions for future data that can behave quite differently.

---

[← Display results](08-display-results.md) · [Up: contents](index.md)
