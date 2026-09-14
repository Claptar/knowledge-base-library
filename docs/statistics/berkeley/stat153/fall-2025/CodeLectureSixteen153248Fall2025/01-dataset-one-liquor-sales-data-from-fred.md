---
title: 'Dataset One: Liquor Sales Data from FRED'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureSixteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureSixteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Dataset One: Liquor Sales Data from FRED

**Source:** [`CodeLectureSixteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureSixteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
#The following is FRED data on retail sales (in millions of dollars) for beer, wine and liquor stores (https://fred.stlouisfed.org/series/MRTSSM4453USN)
beersales = pd.read_csv('MRTSSM4453USN_October2025.csv')
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
0       1992-01-01           1414
1       1992-02-01           1444
2       1992-03-01           1496
3       1992-04-01           1569
4       1992-05-01           1707
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
403
[1414 1444 1496 1569 1707 1663 1792 1744 1658 1763 1715 2354 1512 1433
 1573 1606 1683 1679 1828 1665 1600 1647 1670 2287 1450 1410 1607 1648
 1715 1741 1858 1742 1710 1693 1731 2416 1459 1407 1619 1594 1696 1747
 1769 1745 1731 1678 1762 2437 1575 1549 1723 1687 1836 1837 1908 1936
 1672 1748 1871 2395 1605 1526 1745 1712 1940 1886 1976 1960 1783 1932
 1962 2657 1740 1665 1783 1848 2015 1938 2079 1993 1910 2033 2026 2857
 1755 1700 1867 1974 2078 2017 2200 2013 2000 2088 2140 3076 1810 1863
 2066 2011 2225 2278 2326 2288 2228 2223 2409 3192 1995 1941 2201 2110
 2337 2389 2349 2382 2191 2279 2495 3349 1999 1994 2236 2174 2429 2349
 2427 2451 2170 2267 2456 3294 2003 1931 2145 2202 2431 2297 2466 2511
 2323 2495 2514 3456 2169 2101 2270 2418 2543 2505 2716 2485 2481 2586
 2619 3604 2104 2194 2398 2501 2568 2637 2771 2645 2639 2656 2782 3925
 2303 2394 2616 2653 2870 2906 2966 2878 2852 2773 2987 4067 2445 2478
 2862 2730 3107 3203 3163 3136 2911 2942 3142 4195 2551 2677 2852 2861
 3264 3132 3359 3316 3010 3201 3235 4260 2782 2657 2888 2990 3312 3160
 3397 3249 3119 3274 3209 4422 2754 2790 3076 3168 3319 3292 3503 3307
 3222 3349 3374 4484 2765 2858 3111 3221 3325 3402 3584 3428 3373 3372
 3499 4696 2877 3077 3413 3278 3640 3668 3589 3606 3365 3482 3714 4917
 3021 3088 3465 3334 3771 3636 3848 3908 3459 3605 3863 4961 3213 3143
 3466 3511 3947 3822 4014 3988 3601 3857 3865 5245 3359 3273 3625 3631
 4070 3957 4252 3995 3818 4004 3995 5444 3376 3528 3786 3844 4114 4179
 4436 4182 4136 4138 4359 5645 3474 3503 3957 3960 4328 4353 4466 4324
 4221 4218 4506 5801 3684 3686 4314 4028 4574 4611 4632 4569 4296 4432
 4797 5969 3837 3818 4331 4252 4741 4647 4876 4902 4349 4569 4933 6163
 4066 4184 5081 4757 5737 5572 5905 5634 5410 5590 5631 7142 4960 4831
 5566 5560 5940 5877 6044 5601 5468 5647 5893 7474 4812 4920 5441 5544
 5727 5833 6003 5755 5621 5744 6017 7651 4983 4972 5535 5527 6067 6040
 6096 5834 5783 5736 6166 7863 4907 5248 5765 5539 6264 6155 6256 6203
 5658 5987 6453 7854 5055 5037 5613 5626 6310 5950 6225]
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
(391, 13)
[[1.000e+00 2.354e+03 1.715e+03 ... 1.496e+03 1.444e+03 1.414e+03]
 [1.000e+00 1.512e+03 2.354e+03 ... 1.569e+03 1.496e+03 1.444e+03]
 [1.000e+00 1.433e+03 1.512e+03 ... 1.707e+03 1.569e+03 1.496e+03]
 ...
 [1.000e+00 5.626e+03 5.613e+03 ... 6.256e+03 6.155e+03 6.264e+03]
 [1.000e+00 6.310e+03 5.626e+03 ... 6.203e+03 6.256e+03 6.155e+03]
 [1.000e+00 5.950e+03 6.310e+03 ... 5.658e+03 6.203e+03 6.256e+03]]
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
Method:                 Least Squares   F-statistic:                     2597.
Date:                Thu, 23 Oct 2025   Prob (F-statistic):               0.00
Time:                        16:14:31   Log-Likelihood:                -2529.9
No. Observations:                 391   AIC:                             5086.
Df Residuals:                     378   BIC:                             5137.
Df Model:                          12
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          6.7819     21.711      0.312      0.755     -35.907      49.471
x1             0.0439      0.018      2.448      0.015       0.009       0.079
x2             0.0428      0.018      2.379      0.018       0.007       0.078
x3             0.0521      0.018      2.913      0.004       0.017       0.087
x4             0.0336      0.018      1.870      0.062      -0.002       0.069
x5             0.0523      0.018      2.898      0.004       0.017       0.088
x6             0.0002      0.018      0.009      0.993      -0.036       0.036
x7            -0.0128      0.018     -0.697      0.486      -0.049       0.023
x8            -0.0304      0.019     -1.633      0.103      -0.067       0.006
x9            -0.0440      0.019     -2.368      0.018      -0.081      -0.007
x10           -0.0621      0.019     -3.352      0.001      -0.099      -0.026
x11           -0.0163      0.019     -0.875      0.382      -0.053       0.020
x12            0.9739      0.019     52.184      0.000       0.937       1.011
==============================================================================
Omnibus:                      172.369   Durbin-Watson:                   0.812
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1196.724
Skew:                           1.726   Prob(JB):                    1.36e-260
Kurtosis:                      10.845   Cond. No.                     3.36e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.36e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
```

```python
arfitted = armod.fittedvalues
#Plotting the fitted values against response values
plt.xlabel('Fitted Values')
plt.ylabel('Response Values')
plt.title('AR(1) Model Fitted Values vs Response Values')
plt.plot(arfitted, yreg, 'o')
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
plt.plot(time_all, yhat,  color='C0')
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
