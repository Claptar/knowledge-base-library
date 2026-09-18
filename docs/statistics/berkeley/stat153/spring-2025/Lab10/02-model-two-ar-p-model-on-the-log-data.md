---
title: 'Model Two: AR(p) model on the log(data)'
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab10.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Model Two: AR(p) model on the log(data)

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

---

[← Model One: AR(p) directly on the training data](01-model-one-ar-p-directly-on-the-training-data.md) · [Up: contents](index.md) · [Model Three: Working with Differenced Data →](03-model-three-working-with-differenced-data.md)
