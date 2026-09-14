---
title: 'Dataset Two: House Price Data from FRED'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureSixteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureSixteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Dataset Two: House Price Data from FRED

**Source:** [`CodeLectureSixteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureSixteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
#The following is FRED data on Average Sales Price of Houses Sold for the US (https://fred.stlouisfed.org/series/ASPUS)
hprice = pd.read_csv('ASPUS_October2025.csv')
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
250
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
(220, 31)
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
 505300 503000 521900 498300 519700 502200 498700 510900 514200 512800]
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
Method:                 Least Squares   F-statistic:                     2885.
Date:                Thu, 23 Oct 2025   Prob (F-statistic):          4.29e-235
Time:                        16:22:56   Log-Likelihood:                -2239.4
No. Observations:                 220   AIC:                             4541.
Df Residuals:                     189   BIC:                             4646.
Df Model:                          30
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       1252.3043    895.312      1.399      0.164    -513.784    3018.393
x1             0.7836      0.073     10.799      0.000       0.640       0.927
x2             0.5246      0.093      5.623      0.000       0.341       0.709
x3            -0.2076      0.100     -2.077      0.039      -0.405      -0.010
x4             0.0044      0.099      0.045      0.964      -0.191       0.200
x5             0.0292      0.099      0.296      0.768      -0.166       0.224
x6            -0.3315      0.098     -3.382      0.001      -0.525      -0.138
x7            -0.0284      0.101     -0.282      0.778      -0.227       0.170
x8             0.1678      0.102      1.646      0.101      -0.033       0.369
x9             0.1665      0.103      1.621      0.107      -0.036       0.369
x10           -0.2485      0.103     -2.413      0.017      -0.452      -0.045
x11            0.0576      0.106      0.546      0.586      -0.151       0.266
x12            0.3131      0.104      3.004      0.003       0.107       0.519
x13           -0.4220      0.108     -3.910      0.000      -0.635      -0.209
x14           -0.1454      0.110     -1.316      0.190      -0.363       0.073
x15            0.5566      0.116      4.807      0.000       0.328       0.785
x16           -0.0623      0.118     -0.527      0.599      -0.295       0.171
x17           -0.3085      0.123     -2.515      0.013      -0.550      -0.066
x18            0.1707      0.119      1.432      0.154      -0.064       0.406
x19            0.0860      0.118      0.728      0.468      -0.147       0.319
x20           -0.0764      0.118     -0.649      0.517      -0.309       0.156
x21           -0.2422      0.119     -2.043      0.042      -0.476      -0.008
x22            0.1030      0.119      0.867      0.387      -0.131       0.337
x23            0.0116      0.120      0.097      0.923      -0.225       0.248
x24           -0.2901      0.118     -2.468      0.014      -0.522      -0.058
x25            0.5416      0.117      4.641      0.000       0.311       0.772
x26            0.1503      0.123      1.219      0.224      -0.093       0.394
x27           -0.5970      0.123     -4.840      0.000      -0.840      -0.354
x28            0.2527      0.131      1.930      0.055      -0.006       0.511
x29            0.1942      0.121      1.610      0.109      -0.044       0.432
x30           -0.1401      0.103     -1.365      0.174      -0.343       0.062
==============================================================================
Omnibus:                       33.340   Durbin-Watson:                   1.992
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              114.033
Skew:                           0.550   Prob(JB):                     1.73e-25
Kurtosis:                       6.351   Cond. No.                     2.29e+06
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.29e+06. This might indicate that there are
strong multicollinearity or other numerical problems.
```

```python
arfitted = armod.fittedvalues
#Plotting the fitted values against response values
plt.xlabel('Fitted Values')
plt.ylabel('Response Values')
plt.title('AR(1) Model Fitted Values vs Response Values')
#plotting with reduced size points for better visibility
plt.plot(arfitted, yreg, 'o', markersize=4)

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
time_all = np.arange(1, n + k + 1)
plt.plot(time_all, yhat, color='C0')
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

We will now apply AR models to logarithms of $y$.

```python
ylog = np.log(y)
plt.plot(ylog)
plt.xlabel('Year')
plt.ylabel('Log Dollars')
plt.title('Log of Average Sales Price of Houses Sold in the US')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
p = 30 #this is the order of the AR model
n = len(ylog)
print(n)
```

```
250
```

```python
yreg = ylog[p:] #these are the response values in the autoregression
Xmat = np.ones((n-p, 1)) #this will be the design matrix (X) in the autoregression
for j in range(1, p+1):
    col = ylog[p-j : n-j].reshape(-1, 1)
    Xmat = np.column_stack([Xmat, col])
```

```python
armod_log = sm.OLS(yreg, Xmat).fit()
print(armod_log.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.999
Model:                            OLS   Adj. R-squared:                  0.999
Method:                 Least Squares   F-statistic:                     7003.
Date:                Thu, 23 Oct 2025   Prob (F-statistic):          1.96e-271
Time:                        16:22:59   Log-Likelihood:                 509.83
No. Observations:                 220   AIC:                            -957.7
Df Residuals:                     189   BIC:                            -852.5
Df Model:                          30
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.1013      0.033      3.049      0.003       0.036       0.167
x1             0.8024      0.073     11.057      0.000       0.659       0.946
x2             0.4279      0.092      4.628      0.000       0.246       0.610
x3            -0.1316      0.097     -1.356      0.177      -0.323       0.060
x4             0.0597      0.095      0.627      0.531      -0.128       0.247
x5            -0.0348      0.095     -0.366      0.715      -0.222       0.153
x6            -0.2380      0.094     -2.544      0.012      -0.423      -0.053
x7             0.0186      0.095      0.195      0.845      -0.169       0.207
x8             0.0834      0.095      0.874      0.383      -0.105       0.272
x9             0.0662      0.095      0.694      0.488      -0.122       0.254
x10           -0.1635      0.095     -1.727      0.086      -0.350       0.023
x11            0.0860      0.095      0.905      0.367      -0.101       0.273
x12            0.2016      0.094      2.135      0.034       0.015       0.388
x13           -0.2995      0.096     -3.128      0.002      -0.488      -0.111
x14           -0.0542      0.097     -0.558      0.577      -0.246       0.137
x15            0.3066      0.097      3.161      0.002       0.115       0.498
x16           -0.1182      0.097     -1.214      0.226      -0.310       0.074
x17           -0.1742      0.098     -1.781      0.077      -0.367       0.019
x18            0.0710      0.097      0.735      0.463      -0.119       0.261
x19            0.1175      0.096      1.227      0.221      -0.071       0.306
x20            0.1415      0.096      1.473      0.143      -0.048       0.331
x21           -0.2030      0.096     -2.105      0.037      -0.393      -0.013
x22            0.0006      0.097      0.007      0.995      -0.191       0.192
x23           -0.0754      0.097     -0.780      0.437      -0.266       0.115
x24           -0.1470      0.097     -1.517      0.131      -0.338       0.044
x25            0.3098      0.096      3.228      0.001       0.120       0.499
x26            0.1047      0.098      1.065      0.288      -0.089       0.299
x27           -0.3197      0.098     -3.256      0.001      -0.513      -0.126
x28            0.1514      0.101      1.503      0.135      -0.047       0.350
x29            0.0733      0.097      0.756      0.451      -0.118       0.264
x30           -0.0703      0.075     -0.938      0.349      -0.218       0.078
==============================================================================
Omnibus:                        0.073   Durbin-Watson:                   1.980
Prob(Omnibus):                  0.964   Jarque-Bera (JB):                0.002
Skew:                           0.001   Prob(JB):                        0.999
Kurtosis:                       3.013   Cond. No.                     6.47e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 6.47e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

```python
arfitted_log = armod_log.fittedvalues
#Plotting the fitted values against response values
plt.xlabel('Fitted Values')
plt.ylabel('Response Values')
plt.title('AR(1) Model Fitted Values vs Response Values')
#plotting with reduced size points for better visibility
plt.plot(arfitted_log, yreg, 'o', markersize=4)

plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Generate k-step ahead forecasts:
k = 100
yhat = np.concatenate([ylog, np.full(k, -9999)]) #extend data by k placeholder values
for i in range(1, k+1):
    ans = armod_log.params[0]
    for j in range(1, p+1):
        ans += armod_log.params[j] * yhat[n+i-j-1]
    yhat[n+i-1] = ans
predvalues_log = yhat[n:]
```

```python
#Plotting the series with forecasts:
time_all = np.arange(1, n + k + 1)
plt.plot(time_all, yhat, color='C0')
plt.plot(range(1, n + 1), ylog, label='Original Data (log scale)', color='C1')
plt.plot(range(n + 1, n + k + 1), predvalues_log, label='Forecasts', color='blue')
plt.axvline(x=n, color='black', linestyle='--', label='Forecast Start')
#plt.axhline(y=np.mean(y), color='gray', linestyle=':', label='Mean of Original Data')
plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Time Series + AR(p) Forecasts')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We now plot the predictions on the original data.

```python
#Plotting the series with forecasts:
time_all = np.arange(1, n + k + 1)
plt.plot(range(1, n + 1), y, label='Original Data', color='C1')
plt.plot(range(n + 1, n + k + 1), np.exp(predvalues_log), label='Forecasts (AR on log)', color='blue')
plt.plot(range(n + 1, n + k + 1), predvalues, label='Forecasts (AR original data)', color='green')
plt.axvline(x=n, color='black', linestyle='--', label='Forecast Start')
#plt.axhline(y=np.mean(y), color='gray', linestyle=':', label='Mean of Original Data')
plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Time Series + AR(p) Forecasts')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Dataset One: Liquor Sales Data from FRED](01-dataset-one-liquor-sales-data-from-fred.md) · [Up: contents](index.md) · [Sunspots Data →](03-sunspots-data.md)
