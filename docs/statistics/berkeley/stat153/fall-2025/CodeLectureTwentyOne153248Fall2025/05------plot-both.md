---
title: '---- Plot both ----'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ---- Plot both ----

**Source:** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize=(8,5))

lags = np.arange(len(acov_ar2))

plt.stem(lags, acov_ar2, markerfmt='bo', label="AR(2)")
plt.stem(lags, acov_ma2, markerfmt='ro', label="MA(2)")

plt.title("Autocovariance Comparison: AR(2) vs MA(2)")
plt.xlabel("Lag")
plt.ylabel("Gamma(h)")
plt.legend()
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The autocovariances of the two models are somewhat close to each other. This suggests that the AR(2) and MA(2) models are not very different from each other.

## ARIMA Modeling

We apply the Box-Jenkins philosophy to a real dataset from FRED. The Box-Jenkins philosophy deals with nonstationarity by differencing, and then attempts to fit a **causal, stationary** AR models  to the  differenced data.

### TTLCONS data

The following data gives the monthly total construction spending in the United States (after taking logs)

```python
ttlcons = pd.read_csv('TTLCONS_13Nov2025.csv')
print(ttlcons.head())
y = np.log(ttlcons['TTLCONS'])
print(len(y))
plt.plot(y)
plt.title('Logarithm of Total Construction Spending')
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

It will clearly be not appropriate to fit a causal stationary model to this dataset. So we first difference and visualize the differenced data.

```python
ydiff = np.diff(y)
plt.plot(ydiff)
plt.title('Differenced Logarithm of Total Construction Spending')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now we look for an appropriate AR($p$) or MA($q$) model to the data. For this, let us first plot the sample ACF and PACF values.

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))
plot_acf(ydiff, lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF")
plot_pacf(ydiff, lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF")
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The sample PACF appears to be negligible after lag 3. This suggests fitting an AR(3) model to the data.

```python
p = 3
armod = AutoReg(ydiff, lags = p).fit()
print(armod.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  390
Model:                     AutoReg(3)   Log Likelihood                1198.770
Method:               Conditional MLE   S.D. of innovations              0.011
Date:                Thu, 13 Nov 2025   AIC                          -2387.541
Time:                        16:53:22   BIC                          -2367.748
Sample:                             3   HQIC                         -2379.692
                                  390
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0019      0.001      3.159      0.002       0.001       0.003
y.L1           0.2221      0.049      4.491      0.000       0.125       0.319
y.L2           0.0644      0.050      1.278      0.201      -0.034       0.163
y.L3           0.2077      0.049      4.209      0.000       0.111       0.304
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.3956           -0.0000j            1.3956           -0.0000
AR.2           -0.8529           -1.6500j            1.8574           -0.3259
AR.3           -0.8529           +1.6500j            1.8574            0.3259
-----------------------------------------------------------------------------
```

From the Modulus values reported near the end of the summary table, it is clear that the fitted AR(3) model is causal and stationary. Let us use the fitted model to predict the future values of the time series. Because the model is fitted to the differenced data, we would need to convert it to the original data before makign predictions. The fitted model is:
\begin{equation*}
    y_t - y_{t-1} = \hat{\phi}_0 + \hat{\phi}_1 \left(y_{t-1} - y_{t-2} \right) + \hat{\phi}_2 \left(y_{t-2} - y_{t-3} \right) + \hat{\phi}_3 \left(y_{t-3} - y_{t-4} \right) + \epsilon_t
\end{equation*}
which is equivalent to
\begin{equation*}
    y_t = \hat{\phi}_0 + \left(1 + \hat{\phi}_1 \right) y_{t-1} + \left(\hat{\phi}_2 - \hat{\phi}_1 \right) y_{t-2} + \left(\hat{\phi}_3 - \hat{\phi}_2 \right) y_{t-3}  - \hat{\phi}_3 y_{t-4} + \epsilon_t
\end{equation*}
This is an AR(4) model and we can predict using it in the usual way as follows.

This AR(4) model is for the original data, and will not be stationary as can be checked below.

```python
phi0_hat, phi1_hat, phi2_hat, phi3_hat = armod.params

---

[← ---- MA(2) model ----](04------ma-2-model.md) · [Up: contents](index.md) · [Convert differenced AR(3) model to AR(4) model for the original data →](06-convert-differenced-ar-3-model-to-ar-4-model-for-the-origina.md)
