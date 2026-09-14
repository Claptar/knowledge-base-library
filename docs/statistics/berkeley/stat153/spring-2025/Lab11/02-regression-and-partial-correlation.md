---
title: Regression and Partial Correlation
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Regression and Partial Correlation

**Source:** [`Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

As already mentioned, the sample pacf at lag $h$ is defined as the estimate $\hat{\phi}_h$ of $\phi_h$ when the AR($h$) model is fit to the data. From this definition, it makes sense that these values can be used for AR model selection. However why does this definition have the name "partial correlation". In statistics, the partial correlation between two variables $y, x$ given a bunch of other variables $z_1, \dots, z_k$ is defined as the correlation between the residuals $e^{y \mid z_1, \dots, z_k}$ and $e^{x \mid z_1, \dots, z_k}$. Below we calculate the partial correlation in terms of residuals, and then see how it is related to our definition of the sample pacf.

Let us first fix a value of $p$ and then compute the sample PACF at lag $p$ directly (without using inbuilt library functions).

```python
p = 9 # fix a value of p
yreg = y[p: ] # these are the response values in the autoregression
Xmat = np.ones((n - p, 1)) # this will be the design matrix (X) in the autoregression
for j in range(1, p + 1):
    col = y[p - j:n - j].reshape(-1, 1)
    Xmat = np.column_stack([Xmat, col])
armod = sm.OLS(yreg, Xmat).fit()
print(armod.params)

pacf_lag_p = armod.params[-1]
print(pacf_lag_p)
```

```
[ 1.27820089e+01  1.17199169e+00 -4.20714239e-01 -1.35002174e-01
  1.01279088e-01 -6.66442555e-02  1.83774039e-03  1.51264798e-02
 -4.29674964e-02  2.17687794e-01]
0.2176877941518983
```

Here the response variable yreg denotes $y_t, t = p+1, \dots, n$. The first column of Xmat is the column of ones, the second column is $y_{t-1}, t = p+1, \dots, n$, third column is $y_{t-2}, t = p+1, \dots, n$ and so on with the last column being $y_{t-p}, t = p+1, \dots, n$.

```python
print(np.column_stack([yreg, Xmat]))
print(y)
```

```
[[ 13.3   1.   16.7 ...  26.7  18.3   8.3]
 [  5.    1.   13.3 ...  38.3  26.7  18.3]
 [  0.    1.    5.  ...  60.   38.3  26.7]
 ...
 [ 83.2   1.   29.6 ...  69.8 113.3  94. ]
 [125.5   1.   83.2 ...  39.8  69.8 113.3]
 [154.7   1.  125.5 ...  21.7  39.8  69.8]]
[  8.3  18.3  26.7  38.3  60.   96.7  48.3  33.3  16.7  13.3   5.    0.
   0.    3.3  18.3  45.   78.3 105.  100.   65.   46.7  43.3  36.7  18.3
  35.   66.7 130.  203.3 171.7 121.7  78.3  58.3  18.3   8.3  26.7  56.7
 116.7 135.  185.  168.3 121.7  66.7  33.3  26.7   8.3  18.3  36.7  66.7
 100.  134.8 139.   79.5  79.7  51.2  20.3  16.   17.   54.   79.3  90.
 104.8 143.2 102.   75.2  60.7  34.8  19.   63.  116.3 176.8 168.  136.
 110.8  58.   51.   11.7  33.  154.2 257.3 209.8 141.3 113.5  64.2  38.
  17.   40.2 138.2 220.  218.2 196.8 149.8 111.  100.   78.2  68.3  35.5
  26.7  10.7   6.8  11.3  24.2  56.7  75.   71.8  79.2  70.3  46.8  16.8
  13.5   4.2   0.    2.3   8.3  20.3  23.2  59.   76.3  68.3  52.9  38.5
  24.2   9.2   6.3   2.2  11.4  28.2  59.9  83.  108.5 115.2 117.4  80.8
  44.3  13.4  19.5  85.8 192.7 227.3 168.7 143.  105.5  63.3  40.3  18.1
  25.1  65.8 102.7 166.3 208.3 182.5 126.3 122.  102.7  74.1  39.   12.7
   8.2  43.4 104.4 178.3 182.2 146.6 112.1  83.5  89.2  57.8  30.7  13.9
  62.8 123.6 232.  185.3 169.2 110.1  74.5  28.3  18.9  20.7   5.7  10.
  53.7  90.5  99.  106.1 105.8  86.3  42.4  21.8  11.2  10.4  11.8  59.5
 121.7 142.  130.  106.6  69.4  43.8  44.4  20.2  15.7   4.6   8.5  40.8
  70.1 105.5  90.1 102.8  80.9  73.2  30.9   9.5   6.    2.4  16.1  79.
  95.  173.6 134.6 105.7  62.7  43.5  23.7   9.7  27.9  74.  106.5 114.7
 129.7 108.2  59.4  35.1  18.6   9.2  14.6  60.2 132.8 190.6 182.6 148.
 113.   79.2  50.8  27.1  16.1  55.3 154.3 214.7 193.  190.7 118.9  98.3
  45.   20.1   6.6  54.2 200.7 269.3 261.7 225.1 159.   76.4  53.4  39.9
  15.   22.   66.8 132.9 150.  149.4 148.   94.4  97.6  54.1  49.2  22.5
  18.4  39.3 131.  220.1 218.9 198.9 162.4  91.   60.5  20.6  14.8  33.9
 123.  211.1 191.8 203.3 133.   76.1  44.9  25.1  11.6  28.9  88.3 136.3
 173.9 170.4 163.6  99.3  65.3  45.8  24.7  12.6   4.2   4.8  24.9  80.8
  84.5  94.  113.3  69.8  39.8  21.7   7.    3.6   8.8  29.6  83.2 125.5
 154.7]
```

Now let us calculate the same sample PACF value using partial correlation. Specifically, we will calculate the partial correlation between the variables $y_t$ and $y_{t-p}$ given all the intervening variables $y_{t-1}, y_{t-2}, \dots, y_{t-p+1}$. For this, we first need to calculate the residual of $y_t$ given $y_{t-1}, \dots, y_{t-p+1}$ as well as the residual of $y_{t-p}$ given $y_{t-1}, \dots, y_{t-p+1}$.

The residual of $y_t$ given $y_{t-1}, \dots, y_{t-p+1}$ is calculated as follows.

```python
armod1 = sm.OLS(yreg, Xmat[:, :-1]).fit()
res_y = armod1.resid
```

The residual of $y_{t-p}$ given $y_{t-1}, \dots, y_{t-p+1}$ is calculated as follows.

```python
armod2 = sm.OLS(Xmat[:, -1], Xmat[:, :-1]).fit()
res_x = armod2.resid
```

The sample correlation between these two residuals is the sample PACF at lag $p$:

```python
pcorr = np.corrcoef(res_y, res_x)[0, 1]
print(pcorr, pacf_lag_p)
```

```
0.21950061866415008 0.2176877941518983
```

Note that this is basically the same as the Sample PACF at lag $p$. The minor discrepancy occurs because the two residuals do not have exactly the same variance. More precisely, the regression coefficient $\hat{\beta}_j$ in a multiple linear regression of $y$ on a set of covariates $x_1, \dots, x_k$ satisfies the following formula:
\begin{equation*}
  \hat{\beta}_j = \text{corr}(e^{y \mid x_k, k \neq j}, e^{x_j \mid x_k, k \neq j}) \sqrt{\frac{\text{var}(e^{y \mid x_k, k \neq j})}{\text{var}(e^{x_j \mid x_k, k \neq j})}}
\end{equation*}

```python
var_res_y = np.var(res_y)
var_res_x = np.var(res_x)
print(var_res_y, var_res_x)
```

```
570.4359419392475 579.9762661182705
```

These residual variances are similar but not exactly the same. This explains why the correlation between the residuals does not exactly equal the fitted regression coefficient $\hat{\phi}_p$. But if we multiply the partial correlation by the ratio of the standard deviations, we recover the sample pacf at lag p (i.e., $\hat{\phi}_p$) exactly.

```python
reg_coeff = pcorr * np.sqrt(var_res_y/var_res_x)
print(reg_coeff, pacf_lag_p)
```

```
0.2176877941518987 0.2176877941518983
```

## Fitting AR(9) and AR(2) to the Sunspots Data

Based on the PACF plot, the two models which make sense for the sunspots data are AR(2) and AR(9). Let us fit both of these models to the data.

```python
armd_2 = AutoReg(y, lags=2).fit()
armd_9 = AutoReg(y, lags=9).fit()
```

```python
k = 200
fcast_9 = armd_9.get_prediction(start=n, end=n+k-1)
fcast_mean_9 = fcast_9.predicted_mean

fcast_2 = armd_2.get_prediction(start=n, end=n+k-1)
fcast_mean_2 = fcast_2.predicted_mean
```

```python
yhat_9 = np.concatenate([y, fcast_mean_9])
yhat_2 = np.concatenate([y, fcast_mean_2])

plt.figure(figsize=(12, 6))
time_all = np.arange(1, n + k + 1)
plt.plot(time_all, yhat_9, color='C0')
plt.plot(range(1, n + 1), y, label='Original Data', color='C1')
plt.plot(range(n + 1, n + k + 1), fcast_mean_9, label='Forecasts (AR-9)', color='blue')
plt.plot(range(n + 1, n + k + 1), fcast_mean_2, label='Forecasts (AR-2)', color='green')
plt.axvline(x=n, color='black', linestyle='--', label='Forecast Start')
plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Time Series + AR(p) Forecasts')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Visually the AR(9) predictions appear better at least for the initial few predictions.

## AR models and Stationarity

For an AR(p) model $y_t = \phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t$, its characteristic polynomial is given by $\phi(z) = 1 - \phi_1 z - \phi_2 z^2 - \dots - \phi_p z^p$. This is a polynomial of degree $p$ so it has $p$ roots $z_1, \dots, z_p$. Some of the roots may be complex (even though $\phi_1, \dots, \phi_p$ are all real). If the modulus $|z_j|$ of $z_j$ is strictly larger than 1 for every $j$, then the corresponding AR(p) model is called **causal and stationary**.

Let us check stationary of the fitted AR(2) and AR(9) models that we just fitted to the sunspots dataset.

```python
print(armd_2.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  325
Model:                     AutoReg(2)   Log Likelihood               -1505.524
Method:               Conditional MLE   S.D. of innovations             25.588
Date:                Thu, 10 Apr 2025   AIC                           3019.048
Time:                        15:55:25   BIC                           3034.159
Sample:                             2   HQIC                          3025.080
                                  325
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         24.4561      2.372     10.308      0.000      19.806      29.106
y.L1           1.3880      0.040     34.685      0.000       1.310       1.466
y.L2          -0.6965      0.040    -17.423      0.000      -0.775      -0.618
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            0.9965           -0.6655j            1.1983           -0.0937
AR.2            0.9965           +0.6655j            1.1983            0.0937
-----------------------------------------------------------------------------
```

The roots and their modulus are actually given as part of the summary output. We can also compute them as follows.

```python

---

[← ACF and PACF](01-acf-and-pacf.md) · [Up: contents](index.md) · [characteristic polynomial →](03-characteristic-polynomial.md)
