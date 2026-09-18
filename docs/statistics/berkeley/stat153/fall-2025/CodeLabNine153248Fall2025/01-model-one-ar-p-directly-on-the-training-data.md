---
title: 'Model One: AR(p) directly on the training data'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabNine153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabNine153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLabNine153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabNine153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Model One: AR(p) directly on the training data

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.ar_model import AutoReg
```

## GNP Dataset

The following dataset is from FRED: https://fred.stlouisfed.org/series/GNP. This is a quarterly dataset (there are four quarters in each year).

```python
gnp = pd.read_csv("GNP_02April2025.csv")
print(gnp.head())

y = gnp['GNP']
plt.figure(figsize = (12, 6))
plt.plot(y, color = 'black')
plt.show()
```

```
observation_date      GNP
0       1947-01-01  244.142
1       1947-04-01  247.063
2       1947-07-01  250.716
3       1947-10-01  260.981
4       1948-01-01  267.133
```

*(1 figure omitted — see the original notebook.)*

Let us reserve the last 16 observations (corresponding to the most recent 4 years) for testing purposes. We shall fit models to the rest of the data, and then evaluate prediction accuracy on the last 16 observations.

```python
n = len(y)
tme = range(1, n+1)

n_test = 16

n_train = n - n_test
y_train = y[:n_train]
tme_train = tme[:n_train]
y_test = y[n_train:]
tme_test = tme[n_train:]
```

As seen in class, AR(p) can be fit in two ways. Either by using the AutoReg function (from the library statsmodels), or by manually creating $y$ and $X$ and then running OLS. Both methods give identical parameter estimates. But the standard errors will be slightly different (also AutoReg will use $z$-scores while OLS uses $t$-scores). Below we fit the AR(2) model for the GNP data using both these methods, and compare the results obtained.

```python
p = 2
armod_sm = AutoReg(y_train, lags = p, trend = 'c').fit()
# trend = 'c' will fit the model
# y_t = phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t
# trend = 'n' will fit the model
# y_t = \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t
# (note there is no intercept term phi_0)
# the default choice is trend = 'c' so we can just drop it if we want
armod_sm = AutoReg(y_train, lags = p).fit()
print(armod_sm.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                    GNP   No. Observations:                  296
Model:                     AutoReg(2)   Log Likelihood               -1912.402
Method:               Conditional MLE   S.D. of innovations            161.714
Date:                Fri, 31 Oct 2025   AIC                           3832.803
Time:                        19:31:09   BIC                           3847.538
Sample:                             2   HQIC                          3838.704
                                  296
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         27.5376     13.295      2.071      0.038       1.480      53.595
GNP.L1         0.7827      0.057     13.751      0.000       0.671       0.894
GNP.L2         0.2273      0.057      3.961      0.000       0.115       0.340
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            0.9919           +0.0000j            0.9919            0.0000
AR.2           -4.4357           +0.0000j            4.4357            0.5000
-----------------------------------------------------------------------------
```

Next let us fit the same model by running OLS (after creating the response vector and the design matrix).

```python
n_train = len(y_train)
yreg = y_train[p:] # these are the response values in the autoregression
Xmat = np.ones((n_train-p, 1)) # this will be the design matrix (X) in the autoregression
for j in range(1, p+1):
    col = y_train[p-j : n_train-j]
    Xmat = np.column_stack([Xmat, col])

armod = sm.OLS(yreg, Xmat).fit()
print(armod.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                    GNP   R-squared:                       0.999
Model:                            OLS   Adj. R-squared:                  0.999
Method:                 Least Squares   F-statistic:                 2.409e+05
Date:                Fri, 31 Oct 2025   Prob (F-statistic):               0.00
Time:                        19:31:09   Log-Likelihood:                -1912.4
No. Observations:                 294   AIC:                             3831.
Df Residuals:                     291   BIC:                             3842.
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         27.5376     13.363      2.061      0.040       1.237      53.838
x1             0.7827      0.057     13.681      0.000       0.670       0.895
x2             0.2273      0.058      3.940      0.000       0.114       0.341
==============================================================================
Omnibus:                      447.590   Durbin-Watson:                   2.036
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           172061.765
Skew:                          -7.246   Prob(JB):                         0.00
Kurtosis:                     120.626   Cond. No.                     1.82e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.82e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
```

Check that the parameter estimates are the same. The standard errors are quite close to each other. One of them gives z-scores while the other gives t-scores:

```python
print(np.column_stack([armod.params, armod_sm.params]))
print(np.column_stack([armod.bse, armod_sm.bse])) # these are the standard errors
```

```
[[27.53762002 27.53762002]
 [ 0.78267356  0.78267356]
 [ 0.2272753   0.2272753 ]]
[[13.36316472 13.29481049]
 [ 0.0572102   0.05691756]
 [ 0.05767742  0.05738239]]
```

You are free to use either of these two methods while working with data.

### Determination of the order $p$

One practical aspect of fitting AR(p) models is the determination of the order $p$. When $p$ increases, the models become more complicated and can overfit the data. The following heuristic can be used to determine $p$:
1. Initialize at $p = 1$
2. Fit the AR(p) model to the data. Look at the 95% interval for the parameter $\phi_p$. If the interval contains 0, then use $p-1$ as the order. If the interval does not contain 0, then set $p = p+1$ and repeat Step 2.

Let us apply this method to the GNP training data. The first step is to fit the AR(1) model.

```python
p = 1
armod_sm = AutoReg(y_train, lags = p).fit()
print(armod_sm.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                    GNP   No. Observations:                  296
Model:                     AutoReg(1)   Log Likelihood               -1926.082
Method:               Conditional MLE   S.D. of innovations            165.696
Date:                Fri, 31 Oct 2025   AIC                           3858.164
Time:                        19:31:09   BIC                           3869.225
Sample:                             1   HQIC                          3862.593
                                  296
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         22.9779     13.531      1.698      0.089      -3.541      49.497
GNP.L1         1.0080      0.001    681.901      0.000       1.005       1.011
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            0.9920           +0.0000j            0.9920            0.0000
-----------------------------------------------------------------------------
```

The 95% interval for $\phi_1$ is $[1.005, 1.011]$ which clearly does not contain zero. So we proceed to fit AR(2).

```python
p = 2
armod_sm = AutoReg(y_train, lags = p).fit()
print(armod_sm.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                    GNP   No. Observations:                  296
Model:                     AutoReg(2)   Log Likelihood               -1912.402
Method:               Conditional MLE   S.D. of innovations            161.714
Date:                Fri, 31 Oct 2025   AIC                           3832.803
Time:                        19:31:09   BIC                           3847.538
Sample:                             2   HQIC                          3838.704
                                  296
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         27.5376     13.295      2.071      0.038       1.480      53.595
GNP.L1         0.7827      0.057     13.751      0.000       0.671       0.894
GNP.L2         0.2273      0.057      3.961      0.000       0.115       0.340
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            0.9919           +0.0000j            0.9919            0.0000
AR.2           -4.4357           +0.0000j            4.4357            0.5000
-----------------------------------------------------------------------------
```

The 95% interval for $\phi_2$ is $[0.115, 0.340]$ which also does not contain 0. So we increase $p$ and proceed to fit AR(3).

```python
p = 3
armod_sm = AutoReg(y_train, lags = p).fit()
print(armod_sm.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                    GNP   No. Observations:                  296
Model:                     AutoReg(3)   Log Likelihood               -1900.679
Method:               Conditional MLE   S.D. of innovations            158.859
Date:                Fri, 31 Oct 2025   AIC                           3811.357
Time:                        19:31:09   BIC                           3829.758
Sample:                             3   HQIC                          3818.727
                                  296
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         35.7792     13.315      2.687      0.007       9.683      61.876
GNP.L1         0.7197      0.059     12.225      0.000       0.604       0.835
GNP.L2         0.0467      0.077      0.604      0.546      -0.105       0.198
GNP.L3         0.2455      0.072      3.411      0.001       0.104       0.387
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            0.9922           -0.0000j            0.9922           -0.0000
AR.2           -0.5913           -1.9378j            2.0260           -0.2971
AR.3           -0.5913           +1.9378j            2.0260            0.2971
-----------------------------------------------------------------------------
```

The 95% interval for $\phi_3$ is $[0.104, 0.387]$ which also does not contain 0. So we increase $p$ again and proceed to fit AR(4).

```python
p = 4
armod_sm = AutoReg(y_train, lags = p).fit()
print(armod_sm.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                    GNP   No. Observations:                  296
Model:                     AutoReg(4)   Log Likelihood               -1894.593
Method:               Conditional MLE   S.D. of innovations            159.078
Date:                Fri, 31 Oct 2025   AIC                           3801.186
Time:                        19:31:09   BIC                           3823.247
Sample:                             4   HQIC                          3810.023
                                  296
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         35.1435     13.528      2.598      0.009       8.629      61.658
GNP.L1         0.7188      0.059     12.185      0.000       0.603       0.834
GNP.L2         0.0310      0.086      0.359      0.720      -0.138       0.200
GNP.L3         0.3317      0.222      1.491      0.136      -0.104       0.768
GNP.L4        -0.0701      0.171     -0.409      0.683      -0.406       0.266
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            0.9923           -0.0000j            0.9923           -0.0000
AR.2           -0.6826           -1.5330j            1.6781           -0.3167
AR.3           -0.6826           +1.5330j            1.6781            0.3167
AR.4            5.1069           -0.0000j            5.1069           -0.0000
-----------------------------------------------------------------------------
```

The 95% interval for $\phi_4$ is $[-0.406, 0.266]$. This interval contains 0 which suggests that $\phi_4$ term is redundant. So we use $p = 3$ for this dataset.

### Predictions

The fitted AR(3) can be used to generate point predictions for the future 16 observations.

```python
p = 3
armod_sm = AutoReg(y_train, lags = p).fit()
print(armod_sm.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                    GNP   No. Observations:                  296
Model:                     AutoReg(3)   Log Likelihood               -1900.679
Method:               Conditional MLE   S.D. of innovations            158.859
Date:                Fri, 31 Oct 2025   AIC                           3811.357
Time:                        19:31:09   BIC                           3829.758
Sample:                             3   HQIC                          3818.727
                                  296
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         35.7792     13.315      2.687      0.007       9.683      61.876
GNP.L1         0.7197      0.059     12.225      0.000       0.604       0.835
GNP.L2         0.0467      0.077      0.604      0.546      -0.105       0.198
GNP.L3         0.2455      0.072      3.411      0.001       0.104       0.387
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            0.9922           -0.0000j            0.9922           -0.0000
AR.2           -0.5913           -1.9378j            2.0260           -0.2971
AR.3           -0.5913           +1.9378j            2.0260            0.2971
-----------------------------------------------------------------------------
```

```python
k = 16
fcast = armod_sm.get_prediction(start = n_train, end = n_train+k-1)
fcast_mean = fcast.predicted_mean # this gives the point predictions
```

The predictions can also be calculated manually (without using the get_prediction function) as follows (this was discussed in class).

```python
#Predictions
yhat = np.concatenate([y_train.astype(float), np.full(k, -9999)])
# extend data by k placeholder values
phi_vals = armod_sm.params
for i in range(1, k+1):
    ans = phi_vals.iloc[0]
    for j in range(1, p+1):
        ans += phi_vals.iloc[j] * yhat[n_train+i-j-1]
    yhat[n_train+i-1] = ans
predvalues = yhat[n_train:]

# Check that both predictions are identical:
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
 [23969.46079149 23969.46079149]
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
plt.plot(tme_test, y_test, color = 'red',  label = 'Actual future values')
plt.axvline(x=n_train, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions by the AR(3) model are decent but there are not very accurate.

---

[Up: contents](index.md) · [Model Two: AR(p) model on the log(data) →](02-model-two-ar-p-model-on-the-log-data.md)
