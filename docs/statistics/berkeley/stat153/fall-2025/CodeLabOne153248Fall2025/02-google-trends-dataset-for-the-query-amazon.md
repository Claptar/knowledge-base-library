---
title: Google Trends Dataset for the query Amazon
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Google Trends Dataset for the query Amazon

**Source:** [`CodeLabOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabOne153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

https://trends.google.com/trends/ is another (in addition to FRED) great source for time series datasets (see https://en.wikipedia.org/wiki/Google_Trends). The following is the trends monthly dataset for the query "amazon".

```python
amazon = pd.read_csv('AmazonTrends05Sept2025.csv', skiprows = 1)
#we are skipping the first row as it does not contain any data
print(amazon.head())
amazon.columns = ['Month', 'AmazonTrends']
print(amazon.tail(10))
```

```
Month  amazon: (Worldwide)
0  2004-01                   15
1  2004-02                   14
2  2004-03                   15
3  2004-04                   14
4  2004-05                   14
       Month  AmazonTrends
251  2024-12            69
252  2025-01            58
253  2025-02            53
254  2025-03            54
255  2025-04            53
256  2025-05            53
257  2025-06            55
258  2025-07            61
259  2025-08            61
260  2025-09            57
```

```python
#Here is a plot of the data
plt.plot(amazon['AmazonTrends'])
plt.xlabel('Time (months)')
plt.ylabel('Search popularity')
plt.title('Google Trends for the query "Amazon"')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Fitting a line:
y = amazon['AmazonTrends'] #should we be taking logs instead as in y = np.log(amazon['AmazonTrends'])
x = np.arange(1, len(y) + 1)
X = sm.add_constant(x)
linmod = sm.OLS(y, X).fit()
print(linmod.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:           AmazonTrends   R-squared:                       0.776
Model:                            OLS   Adj. R-squared:                  0.775
Method:                 Least Squares   F-statistic:                     897.9
Date:                Fri, 05 Sep 2025   Prob (F-statistic):           3.76e-86
Time:                        01:33:02   Log-Likelihood:                -970.39
No. Observations:                 261   AIC:                             1945.
Df Residuals:                     259   BIC:                             1952.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         15.4385      1.242     12.431      0.000      12.993      17.884
x1             0.2463      0.008     29.965      0.000       0.230       0.262
==============================================================================
Omnibus:                       25.112   Durbin-Watson:                   0.348
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               38.545
Skew:                           0.601   Prob(JB):                     4.27e-09
Kurtosis:                       4.450   Cond. No.                         303.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
plt.plot(y, label = 'Original Data')
plt.plot(linmod.fittedvalues, label = "Fitted values")
plt.xlabel('Time (months)')
plt.ylabel('Search popularity')
plt.title('Google search popularity for "Amazon"')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The line does not capture the trend in the data well. We can improve the model by adding a quadratic term.

```python
#Let us add a quadratic term:
x2 = x ** 2
X = np.column_stack([x, x2])
X = sm.add_constant(X)
quadmod = sm.OLS(y, X).fit()
print(quadmod.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:           AmazonTrends   R-squared:                       0.832
Model:                            OLS   Adj. R-squared:                  0.831
Method:                 Least Squares   F-statistic:                     638.9
Date:                Fri, 05 Sep 2025   Prob (F-statistic):          1.16e-100
Time:                        01:33:42   Log-Likelihood:                -932.92
No. Observations:                 261   AIC:                             1872.
Df Residuals:                     258   BIC:                             1883.
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          4.1785      1.625      2.572      0.011       0.979       7.378
x1             0.5031      0.029     17.571      0.000       0.447       0.560
x2            -0.0010      0.000     -9.263      0.000      -0.001      -0.001
==============================================================================
Omnibus:                       41.086   Durbin-Watson:                   0.463
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               58.290
Skew:                           0.983   Prob(JB):                     2.20e-13
Kurtosis:                       4.224   Cond. No.                     9.26e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 9.26e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
```

```python
plt.plot(y, label = 'Original Data', color = 'blue')
plt.plot(linmod.fittedvalues, label = "Fitted (linear)", color = 'red')
plt.plot(quadmod.fittedvalues, label = "Fitted (quadratic)", color = 'black')
plt.xlabel('Time (months)')
plt.ylabel('Search popularity')
plt.title('Google search popularity for "Amazon"')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The fit is still not good. Let us add a cubic term.

```python
#Cubic term:
x2 = x ** 2
x3 = x ** 3
X = np.column_stack([x, x2, x3])
X = sm.add_constant(X)
cubmod = sm.OLS(y, X).fit()
print(cubmod.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:           AmazonTrends   R-squared:                       0.889
Model:                            OLS   Adj. R-squared:                  0.888
Method:                 Least Squares   F-statistic:                     685.4
Date:                Fri, 05 Sep 2025   Prob (F-statistic):          2.87e-122
Time:                        01:33:59   Log-Likelihood:                -878.96
No. Observations:                 261   AIC:                             1766.
Df Residuals:                     257   BIC:                             1780.
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         17.7787      1.777     10.005      0.000      14.279      21.278
x1            -0.1139      0.059     -1.943      0.053      -0.229       0.002
x2             0.0049      0.001      9.426      0.000       0.004       0.006
x3         -1.495e-05    1.3e-06    -11.473      0.000   -1.75e-05   -1.24e-05
==============================================================================
Omnibus:                       62.446   Durbin-Watson:                   0.700
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              118.016
Skew:                           1.238   Prob(JB):                     2.36e-26
Kurtosis:                       5.173   Cond. No.                     2.75e+07
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.75e+07. This might indicate that there are
strong multicollinearity or other numerical problems.
```

```python
plt.figure(figsize = (10, 6))
plt.plot(y, label = 'Original Data', color = 'blue')
plt.plot(linmod.fittedvalues, label = "Fitted (linear)", color = 'red')
plt.plot(quadmod.fittedvalues, label = "Fitted (quadratic)", color = 'black')
plt.plot(cubmod.fittedvalues, label = "Fitted (cubic)", color = 'green')
plt.xlabel('Time (months)')
plt.ylabel('Search popularity')
plt.title('Google search popularity for "Amazon"')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now the fit is pretty good. This is a monthly dataset which also has a clear seasonal pattern. Some months in each year have a high $y$ value compared to other months. We can capture this seasonal pattern by adding cosines and sines to the regression model. The simplest seasonal functions with period $12$ are $\cos(2 \pi x/12)$ and $\sin(2 \pi x/12)$. Let us add these to the model.

```python
#Adding seasonal terms to the model:
x4 = np.cos(2 * np.pi * x * (1/12))
x5 = np.sin(2 * np.pi * x * (1/12))
X = np.column_stack([x, x2, x3, x4, x5])
X = sm.add_constant(X)
seasmod1 = sm.OLS(y, X).fit()
plt.figure(figsize = (10, 6))
plt.plot(y, label = 'Original Data', color = 'blue')
plt.plot(cubmod.fittedvalues, label = "Fitted (cubic)", color = 'red')
plt.plot(seasmod1.fittedvalues, label = "Fitted (with seasonal term)", color = 'black')
plt.xlabel('Time (months)')
plt.ylabel('Search popularity')
plt.title('Google search popularity for "Amazon"')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The fit is better but the seasonal term is not enough to capture the actual oscillation present in the data. We improve the fit by adding two more seasonal functions $\cos(2 \pi x (2/12))$ and $\sin(2 \pi x (2/12))$.

```python
#Adding seasonal terms to the model:
x4 = np.cos(2 * np.pi * x * (1/12))
x5 = np.sin(2 * np.pi * x * (1/12))
x6 = np.cos(2 * np.pi * x * (2/12))
x7 = np.sin(2 * np.pi * x * (2/12))
X = np.column_stack([x, x2, x3, x4, x5, x6, x7])
X = sm.add_constant(X)
seasmod = sm.OLS(y, X).fit()
plt.figure(figsize = (10, 6))
plt.plot(y, label = 'Original Data', color = 'blue')
plt.plot(cubmod.fittedvalues, label = "Fitted (cubic)", color = 'red')
plt.plot(seasmod.fittedvalues, label = "Fitted (with seasonal term)", color = 'black')
plt.xlabel('Time (months)')
plt.ylabel('Search popularity')
plt.title('Google search popularity for "Amazon"')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The fit is much improved (even though there is still some discrepancy between the seasonal oscillations in the data and the fitted function). We can use this model to predict the data for a bunch of future time points.

```python
#Computing future predictions:
nf = 100 #number of future points where we are calculating predictions
xf = np.arange(len(x) + 1, len(x) + 1 + nf) #these are the future time points
x2f = xf ** 2
x3f = xf ** 3
x4f = np.cos(2 * np.pi * xf * (1/12))
x5f = np.sin(2 * np.pi * xf * (1/12))
x6f = np.cos(2 * np.pi * xf * (2/12))
x7f = np.sin(2 * np.pi * xf * (2/12))
Xf = np.column_stack([xf, x2f, x3f, x4f, x5f, x6f, x7f])
Xf = sm.add_constant(Xf)
pred = Xf @ np.array(seasmod.params) #these are the predictions
print(pred)
```

```
[ 58.69757163  62.83107246  62.94640673  58.10579472  51.3433054
  46.94061484  46.63211642  48.40381473  48.94419146  47.17909445
  45.29588483  46.24607014  50.3068321   54.27037919  54.2146893
  49.20198269  42.26632834  37.68940231  37.205598    38.80091997
  39.16384994  37.22023573  35.15743848  35.92696573  39.8059992
  43.58674737  43.34718811  38.14954171  31.02787713  26.26387045
  25.59191504  26.9980155   27.17065351  25.03567691  22.78044685
  23.35647084  27.04093062  30.62603467  30.18976086  24.79432948
  17.47380948  12.50987695  11.63692526  12.840959    12.81045986
  10.47127569   8.0107676    8.38044315  11.85748405  15.23409879
  14.58826524   8.98220368   1.44998307  -3.7267205   -4.81351367
  -3.82439184  -4.07087331  -6.62711026  -9.30574155  -9.15525964
  -5.89848281  -2.74320258  -3.61144106  -9.44097799 -17.1977444
 -22.60006421 -23.91354404 -23.15217931 -23.62748832 -26.41362324
 -29.32322292 -29.40477984 -26.38111228 -23.46001174 -24.56350036
 -30.62935785 -38.62351525 -44.26429649 -45.81730818 -45.29654574
 -46.01352748 -49.04240555 -52.19581883 -52.52225977 -49.74454666
 -47.07047101 -48.42205495 -54.7370782  -62.98147178 -68.87355964
 -70.67894838 -70.41163343 -71.38313308 -74.66759951 -78.07767157
 -78.66184173 -76.14292827 -73.7287227  -75.34124715 -81.91828134]
```

```python
#Plotting the data, fitted values and predictions
xall = np.concatenate([x, xf])
fittedpred = np.concatenate([seasmod.fittedvalues, pred])
#plt.figure(figsize = (10, 6))
#print(x)
#print(xf)
plt.plot(xall, fittedpred, color = 'gray', label = 'Fitted values')
plt.plot(xf, pred, color = 'red', label = 'Predictions')
plt.plot(x, y, label = 'Original Data', color = 'blue')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Note that the future predictions become negative after a certain time. This is because the predictions follow the decreasing trend in the cubic function near the right end of the dataset. In this particular problem, negative predictions are meaningless. This issue can be fixed if we fit models to the logarithms of the original data. The model predictions will then have to be exponentiated if we want predictions for the original data. This exponentiation will ensure that all predictions are positive.

```python
#Prediction on log(data):
ylog = np.log(amazon['AmazonTrends'])
seasmodlog = sm.OLS(ylog, X).fit()
predlog = Xf @ np.array(seasmodlog.params)
print(predlog)

xall = np.concatenate([x, xf])
fittedpred_logmodel = np.concatenate([np.exp(seasmodlog.fittedvalues), np.exp(predlog)])
plt.figure(figsize = (10, 6))
#print(x)
#print(xf)
plt.plot(x, y, label = 'Original Data', color = 'blue')
plt.plot(xf, pred, color = 'red', label = 'Predictions (model on original data)')
#plt.plot(xall, fittedpred_logmodel, color = 'black')
plt.plot(xf, np.exp(predlog), color = 'green',  label = 'Predictions (model on log data)')
plt.legend()
plt.show()
```

```
[4.05879994 4.14334257 4.15285342 4.06392616 3.93021997 3.83524535
 3.81923837 3.85046614 3.8665653  3.84200082 3.81282069 3.83416063
 3.9147213  3.99652373 4.00328036 3.91158485 3.77509639 3.67732549
 3.65850819 3.68691162 3.70017242 3.67275556 3.64070903 3.65916855
 3.73683478 3.81572874 3.81956288 3.72493086 3.58549186 3.4847564
 3.46296053 3.48837136 3.49862554 3.46818804 3.43310684 3.44851767
 3.52312119 3.59893842 3.5996818  3.501945   3.35938721 3.25551893
 3.23057621 3.25282617 3.25990547 3.22627905 3.18799493 3.2001888
 3.27156135 3.34413358 3.34161794 3.2406081  3.09476324 2.98759388
 2.95933605 2.97825688 2.98199303 2.94500944 2.90335411 2.91216277
 2.98013607 3.04929504 3.04335212 2.93890098 2.78960079 2.67896207
 2.64722087 2.66264431 2.66286903 2.62236001 2.57716522 2.5824204
 2.64682619 2.71240363 2.70286516 2.59480444 2.44188066 2.32760433
 2.29221149 2.30396927 2.30051431 2.25631158 2.20740907 2.20894249
 2.26961252 2.33144017 2.31813788 2.20629933 2.04958369 1.93150147
 1.89228873 1.90021258 1.89290968 1.84484498 1.79206648 1.78970989
 1.84647588 1.90438547 1.8871511  1.77136645]
```

*(1 figure omitted — see the original notebook.)*

---

[← US Population Dataset](01-us-population-dataset.md) · [Up: contents](index.md) · [Derivation of the Least Squares Estimators in Simple Linear Regression →](03-derivation-of-the-least-squares-estimators-in-simple-linear.md)
