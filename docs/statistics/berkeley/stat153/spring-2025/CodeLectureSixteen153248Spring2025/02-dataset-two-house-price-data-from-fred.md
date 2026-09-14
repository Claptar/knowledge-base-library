---
title: 'Dataset Two: House Price Data from FRED'
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureSixteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureSixteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Dataset Two: House Price Data from FRED

**Source:** [`CodeLectureSixteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureSixteen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
#The following is FRED data on Average Sales Price of Houses Sold for the US (https://fred.stlouisfed.org/series/ASPUS)
hprice = pd.read_csv('ASPUS_March2025.csv')
print(hprice.head())
y = hprice['ASPUS'].to_numpy()
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.xlabel('Year')
plt.ylabel('Dollars')
plt.title('Average Sales Price of Houses Sold in the US')
plt.show()
```

```
observation_date  ASPUS
0       1963-01-01  19300
1       1963-04-01  19400
2       1963-07-01  19200
3       1963-10-01  19600
4       1964-01-01  19600
```

*(1 figure omitted — see the original notebook.)*

```python
p = 30 #this is the order of the AR model
n = len(y)
print(n)
```

```
248
```

```python
yreg = y[p:] #these are the response values in the autoregression
Xmat = np.ones((n-p, 1)) #this will be the design matrix (X) in the autoregression
for j in range(1, p+1):
    col = y[p-j : n-j].reshape(-1, 1)
    Xmat = np.column_stack([Xmat, col])
print(Xmat.shape)
print(y)
```

```
(218, 31)
[ 19300  19400  19200  19600  19600  20200  20500  20900  21500  21000
  21600  21700  22700  23200  23000  22800  24000  24200  23900  24400
  25400  26700  26600  27000  27600  28100  28100  27100  27000  27300
  26000  26300  27300  28600  28300  28200  29000  29400  30300  31600
  32800  35100  35900  36600  38000  38600  39000  39300  40900  42600
  42200  44400  46000  47800  48100  50300  51600  54300  54000  57500
  59300  61600  63500  66400  68300  72400  74200  72700  73600  74400
  77500  80000  80900  84300  83800  83700  81200  85700  83900  84600
  86700  89100  92500  90800  94700  99200  98500  97800  98500 100500
 100500 103800 106300 112000 114400 115600 120800 126100 129900 133500
 137900 134800 141500 140400 144300 146800 150200 151200 149500 151200
 145500 150100 151100 148200 145400 144400 144500 145300 141700 147200
 144700 148900 148000 148300 153600 154200 152800 156100 153500 158900
 157700 160900 161100 166000 164000 171000 172200 177200 174700 175400
 180000 178800 184300 181500 189100 191800 193000 204800 202900 202400
 204100 212100 211000 211200 207800 214200 227600 227600 219100 232500
 233100 241000 248100 256000 262900 265300 274000 286300 288500 287800
 294600 294200 305300 302600 308100 299600 322100 310100 301200 305800
 290400 304200 285100 276600 257000 273400 274100 272900 275300 268800
 266000 278000 268100 267600 263000 259700 278000 282700 294500 297700
 307400 320400 324400 334400 331400 340600 340400 369400 348000 339700
 347400 366700 357000 357900 358800 364900 374800 376900 373200 399700
 374600 378400 392900 384000 375500 376700 382700 384600 383000 371100
 400600 396900 417400 428600 468000 496700 499300 525100 520300 521000
 505300 503000 521900 498300 519700 502200 498700 510300]
```

```python
armod = sm.OLS(yreg, Xmat).fit()
print(armod.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.998
Model:                            OLS   Adj. R-squared:                  0.997
Method:                 Least Squares   F-statistic:                     2805.
Date:                Thu, 13 Mar 2025   Prob (F-statistic):          8.59e-232
Time:                        16:17:10   Log-Likelihood:                -2216.9
No. Observations:                 218   AIC:                             4496.
Df Residuals:                     187   BIC:                             4601.
Df Model:                          30
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       1362.7186    893.733      1.525      0.129    -400.376    3125.813
x1             0.7860      0.073     10.749      0.000       0.642       0.930
x2             0.5475      0.094      5.848      0.000       0.363       0.732
x3            -0.2009      0.102     -1.968      0.051      -0.402       0.000
x4            -0.0526      0.102     -0.518      0.605      -0.253       0.148
x5             0.0467      0.101      0.463      0.644      -0.152       0.245
x6            -0.3590      0.098     -3.664      0.000      -0.552      -0.166
x7             0.0043      0.101      0.042      0.966      -0.196       0.205
x8             0.1898      0.102      1.859      0.065      -0.012       0.391
x9             0.1898      0.104      1.821      0.070      -0.016       0.395
x10           -0.2491      0.103     -2.417      0.017      -0.452      -0.046
x11            0.0068      0.107      0.064      0.949      -0.204       0.218
x12            0.3036      0.105      2.886      0.004       0.096       0.511
x13           -0.4766      0.110     -4.325      0.000      -0.694      -0.259
x14           -0.1386      0.115     -1.201      0.231      -0.366       0.089
x15            0.6107      0.117      5.208      0.000       0.379       0.842
x16           -0.0564      0.123     -0.458      0.647      -0.299       0.186
x17           -0.2568      0.125     -2.055      0.041      -0.503      -0.010
x18            0.1249      0.120      1.040      0.300      -0.112       0.362
x19            0.1171      0.118      0.992      0.323      -0.116       0.350
x20           -0.1026      0.118     -0.870      0.386      -0.335       0.130
x21           -0.2723      0.119     -2.286      0.023      -0.507      -0.037
x22            0.1050      0.119      0.885      0.377      -0.129       0.339
x23            0.0348      0.119      0.292      0.771      -0.200       0.270
x24           -0.2470      0.118     -2.086      0.038      -0.481      -0.013
x25            0.5378      0.116      4.629      0.000       0.309       0.767
x26            0.0990      0.124      0.796      0.427      -0.146       0.344
x27           -0.5720      0.123     -4.640      0.000      -0.815      -0.329
x28            0.2559      0.130      1.971      0.050      -0.000       0.512
x29            0.1036      0.126      0.821      0.413      -0.145       0.352
x30           -0.0665      0.107     -0.623      0.534      -0.277       0.144
==============================================================================
Omnibus:                       31.034   Durbin-Watson:                   1.997
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               93.321
Skew:                           0.553   Prob(JB):                     5.44e-21
Kurtosis:                       6.008   Cond. No.                     2.27e+06
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.27e+06. This might indicate that there are
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

Repeat the above code for different values of $p$ to see how the predictions change.

---

[← Dataset One: Liquor Sales Data from FRED](01-dataset-one-liquor-sales-data-from-fred.md) · [Up: contents](index.md) · [Sunspots Data →](03-sunspots-data.md)
