---
title: 'Dataset One: Liquor Sales Data from FRED'
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureSixteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureSixteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Dataset One: Liquor Sales Data from FRED

**Source:** [`CodeLectureSixteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureSixteen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
#The following is FRED data on retail sales (in millions of dollars) for beer, wine and liquor stores (https://fred.stlouisfed.org/series/MRTSSM4453USN)
beersales = pd.read_csv('MRTSSM4453USN_March2025.csv')
print(beersales.head())
y = beersales['MRTSSM4453USN'].to_numpy()
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.xlabel('Year')
plt.ylabel('Millions of Dollars')
plt.title('Retail Sales: Beer, wine and liquor stores')
plt.show()
```

```
observation_date  MRTSSM4453USN
0       1992-01-01           1509
1       1992-02-01           1541
2       1992-03-01           1597
3       1992-04-01           1675
4       1992-05-01           1822
```

*(1 figure omitted — see the original notebook.)*

AutoRegressive (AR) models are a simple way for obtaining forecasts (predictions) for future values of the time series.

```python
p = 12 #this is the order of the AR model
n = len(y)
print(n)
print(y)
```

```
396
[1509 1541 1597 1675 1822 1775 1912 1862 1770 1882 1831 2511 1614 1529
 1678 1713 1796 1792 1950 1777 1707 1757 1782 2443 1548 1505 1714 1757
 1830 1857 1981 1858 1823 1806 1845 2577 1555 1501 1725 1699 1807 1863
 1886 1861 1845 1788 1879 2598 1679 1652 1837 1798 1957 1958 2034 2062
 1781 1860 1992 2547 1706 1621 1853 1817 2060 2002 2098 2079 1892 2050
 2082 2821 1846 1768 1894 1963 2140 2059 2209 2118 2031 2163 2154 3037
 1866 1808 1986 2099 2210 2145 2339 2140 2126 2219 2273 3265 1920 1976
 2190 2132 2357 2413 2463 2422 2358 2352 2549 3375 2109 2052 2327 2231
 2470 2526 2483 2518 2316 2409 2638 3542 2114 2109 2366 2300 2569 2486
 2568 2595 2297 2401 2601 3488 2121 2046 2273 2333 2576 2433 2611 2660
 2461 2641 2660 3654 2293 2219 2398 2553 2685 2643 2867 2622 2618 2727
 2763 3801 2219 2316 2530 2640 2709 2783 2924 2791 2784 2801 2933 4137
 2424 2519 2753 2791 3017 3055 3117 3024 2997 2913 3137 4269 2569 2603
 3005 2867 3262 3364 3322 3292 3057 3087 3297 4403 2675 2806 2989 2997
 3420 3279 3517 3472 3151 3351 3386 4461 2913 2781 3024 3130 3467 3307
 3555 3399 3263 3425 3356 4625 2878 2916 3214 3310 3467 3438 3657 3454
 3365 3497 3524 4681 2888 2984 3249 3363 3471 3551 3740 3576 3517 3515
 3646 4892 2995 3202 3550 3409 3786 3816 3733 3752 3503 3626 3869 5124
 3143 3211 3601 3463 3915 3773 3993 4054 3586 3738 4004 5143 3331 3258
 3594 3641 4092 3963 4162 4135 3733 3998 4007 5435 3480 3391 3755 3761
 4215 4097 4401 4134 3949 4141 4131 5628 3487 3643 3908 3967 4244 4310
 4575 4312 4264 4265 4492 5818 3580 3609 4076 4079 4457 4482 4598 4451
 4344 4341 4636 5969 3787 3788 4433 4138 4698 4736 4757 4691 4411 4550
 4925 6129 3939 3919 4446 4364 4865 4768 5001 5025 4457 4680 5051 6307
 4155 4274 5188 4855 5853 5683 6020 5742 5513 5696 5738 7279 5056 4924
 5674 5668 6056 5993 6163 5711 5576 5759 6009 7623 4906 5016 5547 5652
 5839 5947 6120 5867 5730 5855 6134 7796 5080 5068 5642 5634 6184 6157
 6213 5947 5894 5847 6288 8023 5007 5360 5876 5646 6385 6273 6375 6324
 5768 6104 6577 8017]
```

AR models work just like regression. The response vector and design matrix in the regression are set up as follows.

```python
yreg = y[p:] #these are the response values in the autoregression
Xmat = np.ones((n-p, 1)) #this will be the design matrix (X) in the autoregression
for j in range(1, p+1):
    col = y[p-j : n-j]
    Xmat = np.column_stack([Xmat, col])
print(Xmat.shape)
print(Xmat)
```

```
(384, 13)
[[1.000e+00 2.511e+03 1.831e+03 ... 1.597e+03 1.541e+03 1.509e+03]
 [1.000e+00 1.614e+03 2.511e+03 ... 1.675e+03 1.597e+03 1.541e+03]
 [1.000e+00 1.529e+03 1.614e+03 ... 1.822e+03 1.675e+03 1.597e+03]
 ...
 [1.000e+00 5.768e+03 6.324e+03 ... 8.023e+03 6.288e+03 5.847e+03]
 [1.000e+00 6.104e+03 5.768e+03 ... 5.007e+03 8.023e+03 6.288e+03]
 [1.000e+00 6.577e+03 6.104e+03 ... 5.360e+03 5.007e+03 8.023e+03]]
```

```python
armod = sm.OLS(yreg, Xmat).fit()
print(armod.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.988
Model:                            OLS   Adj. R-squared:                  0.988
Method:                 Least Squares   F-statistic:                     2552.
Date:                Thu, 13 Mar 2025   Prob (F-statistic):               0.00
Time:                        23:45:11   Log-Likelihood:                -2478.8
No. Observations:                 384   AIC:                             4984.
Df Residuals:                     371   BIC:                             5035.
Df Model:                          12
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        -15.7845     22.657     -0.697      0.486     -60.336      28.767
x1             0.0294      0.018      1.661      0.098      -0.005       0.064
x2             0.0407      0.018      2.296      0.022       0.006       0.076
x3             0.0511      0.018      2.901      0.004       0.016       0.086
x4             0.0287      0.018      1.621      0.106      -0.006       0.063
x5             0.0487      0.018      2.743      0.006       0.014       0.084
x6             0.0104      0.018      0.580      0.562      -0.025       0.046
x7            -0.0028      0.018     -0.157      0.876      -0.038       0.032
x8            -0.0210      0.018     -1.181      0.238      -0.056       0.014
x9            -0.0382      0.018     -2.149      0.032      -0.073      -0.003
x10           -0.0583      0.018     -3.288      0.001      -0.093      -0.023
x11           -0.0176      0.018     -0.988      0.324      -0.053       0.017
x12            0.9692      0.018     54.000      0.000       0.934       1.005
==============================================================================
Omnibus:                      172.409   Durbin-Watson:                   0.858
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1166.518
Skew:                           1.771   Prob(JB):                    4.94e-254
Kurtosis:                      10.769   Cond. No.                     3.59e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.59e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
```

```python
arfitted = armod.fittedvalues
#Plotting the original data and the fitted values:
plt.plot(figure = (12, 6))
plt.plot(yreg)
plt.plot(arfitted, color = 'red', label = 'Fitted')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Generate k-step ahead forecasts:
k = 100
yhat = np.concatenate([y, np.full(k, -9999)]) #extend data by k placeholder values
for i in range(1, k+1):
    ans = armod.params[0]
    for j in range(1, p+1):
        ans += armod.params[j] * yhat[n+i-j-1]
    yhat[n+i-1] = ans
predvalues = yhat[n:]
```

```python
#Plotting the series with forecasts:
plt.figure(figsize=(12, 6))
time_all = np.arange(1, n + k + 1)
plt.plot(time_all, yhat, label='Extended Series (yhat)', color='C0')
plt.plot(range(1, n + 1), y, label='Original Data', color='C1')
plt.plot(range(n + 1, n + k + 1), predvalues, label='Forecasts', color='blue')
plt.axvline(x=n, color='black', linestyle='--', label='Forecast Start')
#plt.axhline(y=np.mean(y), color='gray', linestyle=':', label='Mean of Original Data')
plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Time Series + AR(p) Forecasts')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions depend crucially on the order $p$ of the model. If $p \geq 12$, we get reasonable predictions. However for smaller values of $p$, the predictions look very unnatural. Go back and repeat the code above for other values of $p$.

---

[Up: contents](index.md) · [Dataset Two: House Price Data from FRED →](02-dataset-two-house-price-data-from-fred.md)
