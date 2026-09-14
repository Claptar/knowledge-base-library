---
title: 'Dataset One: Personal Consumption Expenditures from FRED'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEighteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureEighteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Dataset One: Personal Consumption Expenditures from FRED

**Source:** [`CodeLectureEighteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEighteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

The following data is on personal consumption expenditures from FRED (https://fred.stlouisfed.org/series/PCEC). It measures the total amount of money that U.S. households spend on goods and services. This is a time-series record of that spending reported quarterly in billions of dollars (with seasonal adjustment). This measure is compiled by the Bureau of Economic Analysis (BEA) and is a key indicator used to track consumer demand and overall economic activity in the United States.

```python
pcec = pd.read_csv("PCEC_30Oct2025.csv")
print(pcec.head())
y = pcec['PCEC'].to_numpy()
plt.plot(y, color = 'black')
plt.xlabel('Quarter')
plt.ylabel('Billions of Dollars')
plt.title('Personal Consumption Expenditure')
plt.show()
```

```
observation_date     PCEC
0       1947-01-01  156.161
1       1947-04-01  160.031
2       1947-07-01  163.543
3       1947-10-01  167.672
4       1948-01-01  170.372
```

*(1 figure omitted — see the original notebook.)*

We will fit AR(p) models to this dataset, and use the fitted models to predict future values. Let us leave the last 12 observations (corresponding to three years) as test values, and the remaining data form the training data. We will fit AR(p) models to the training data, predict the test values and then compare the predictions with the actual test values.

```python
n = len(y)
tme = range(1, n+1)
#n_test = 50
n_test = 19
n_train = n - n_test
y_train = y[:n_train]
tme_train = tme[:n_train]
y_test = y[n_train:]
tme_test = tme[n_train:]
```

Below, we fit AR(1) to the training data. There are two ways of doing this. Either manually create $y$ and $X$ and use OLS, or use the AutoReg function from statsmodels.

```python
p = 1
yreg = y_train[p:] #these are the response values in the autoregression
Xmat = np.ones((n_train-p, 1)) #this will be the design matrix (X) in the autoregression
for j in range(1, p+1):
    col = y_train[p-j : n_train-j].reshape(-1, 1)
    Xmat = np.column_stack([Xmat, col])

armod = sm.OLS(yreg, Xmat).fit()
print(armod.params)
print(armod.summary())
```

```
[16.73313785  1.00766445]
                            OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.999
Model:                            OLS   Adj. R-squared:                  0.999
Method:                 Least Squares   F-statistic:                 4.192e+05
Date:                Fri, 31 Oct 2025   Prob (F-statistic):               0.00
Time:                        01:46:54   Log-Likelihood:                -1813.7
No. Observations:                 294   AIC:                             3631.
Df Residuals:                     292   BIC:                             3639.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         16.7331      9.377      1.784      0.075      -1.722      35.189
x1             1.0077      0.002    647.467      0.000       1.005       1.011
==============================================================================
Omnibus:                      302.301   Durbin-Watson:                   2.181
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           160905.939
Skew:                          -3.206   Prob(JB):                         0.00
Kurtosis:                     117.429   Cond. No.                     8.35e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.35e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

```python
from statsmodels.tsa.ar_model import AutoReg
armod_sm = AutoReg(y_train, lags = p).fit()
print(armod_sm.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  295
Model:                     AutoReg(1)   Log Likelihood               -1813.666
Method:               Conditional MLE   S.D. of innovations            115.583
Date:                Fri, 31 Oct 2025   AIC                           3633.332
Time:                        01:46:55   BIC                           3644.382
Sample:                             1   HQIC                          3637.757
                                  295
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         16.7331      9.345      1.791      0.073      -1.583      35.050
y.L1           1.0077      0.002    649.681      0.000       1.005       1.011
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            0.9924           +0.0000j            0.9924            0.0000
-----------------------------------------------------------------------------
```

Here are some observations comparing the above two outputs:
1. The parameter estimates are exactly the same.
2. The regression summary gives t-scores corresponding to each parameter estimate while the AutoReg summary only gives z-scores
3. The standard errors are slightly different.

The standard errors given by the regression summary correspond to the square roots of the diagonal entries of:
\begin{equation*}
   \hat{\sigma}^2 (X^T X)^{-1} ~~~ \text{ where } \hat{\sigma}^2 = \sqrt{\frac{\|Y - X \hat{\beta}\|^2}{n-2p-1}}
\end{equation*}
while the standard errors reported by AutoReg summary correspond to the square roots of the diagonal entries of:
\begin{equation*}
   \hat{\sigma}_{\text{MLE}}^2 (X^T X)^{-1} ~~~ \text{ where } \hat{\sigma}_{\text{MLE}}^2 = \sqrt{\frac{\|Y - X \hat{\beta}\|^2}{n-p}}
\end{equation*}

Here is how the fitted model can be used to predict the test observations.

```python
k = n_test
fcast = armod_sm.get_prediction(start = n_train, end = n_train+k-1)
fcast_mean = fcast.predicted_mean #this gives point predictions for the future values of the time series
```

The method that the above function uses to calculate the predictions was detailed in class; and is captured in the code below.

```python
#Predictions
yhat = np.concatenate([y_train.astype(float), np.full(k, -9999)]) #extend data by k placeholder values
phi_vals = armod_sm.params
for i in range(1, k+1):
    ans = phi_vals[0]
    for j in range(1, p+1):
        ans += phi_vals[j] * yhat[n_train+i-j-1]
    yhat[n_train+i-1] = ans
predvalues = yhat[n_train:]

#Check that both predictions are identical:
print(np.column_stack([predvalues, fcast_mean]))
preds_nolog = fcast_mean
```

```
[[14606.9142231  14606.9142231 ]
 [14735.60125891 14735.60125891]
 [14865.2746095  14865.2746095 ]
 [14995.94183441 14995.94183441]
 [15127.61055115 15127.61055115]
 [15260.28843559 15260.28843559]
 [15393.98322245 15393.98322245]
 [15528.70270571 15528.70270571]
 [15664.45473911 15664.45473911]
 [15801.24723657 15801.24723657]
 [15939.08817267 15939.08817267]
 [16077.98558312 16077.98558312]
 [16217.94756519 16217.94756519]
 [16358.98227825 16358.98227825]
 [16501.09794419 16501.09794419]
 [16644.30284789 16644.30284789]
 [16788.60533778 16788.60533778]
 [16934.01382624 16934.01382624]
 [17080.53679013 17080.53679013]]
```

Below we plot the predictions along with the actual test observations.

```python
plt.plot(tme_train, y_train, label = 'Training Data')
plt.plot(tme_test, fcast_mean, label = 'Forecast', color = 'black')
plt.plot(tme_test, y_test, color = 'red',  label = 'Actual future values')
plt.axvline(x=n_train, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Next we discuss prediction uncertainty quantification. The prediction standard errors, and the associated uncertainty intervals, are calculated as follows.

```python
fcast_se = fcast.se_mean
alpha = 0.05
from scipy import stats
z_alpha_half = stats.norm.ppf(1 - alpha/2)
predlower = predvalues - z_alpha_half * fcast_se
predupper = predvalues + z_alpha_half * fcast_se
fcast_int = fcast.conf_int()
print(np.column_stack([predlower, predupper, fcast_int]))
```

```
[[14380.37479095 14833.45365525 14380.37479095 14833.45365525]
 [14413.99602915 15057.20648867 14413.99602915 15057.20648867]
 [14469.87407837 15260.67514062 14469.87407837 15260.67514062]
 [14537.61070798 15454.27296085 14537.61070798 15454.27296085]
 [14613.19828795 15642.02281435 14613.19828795 15642.02281435]
 [14694.59243385 15825.98443733 14694.59243385 15825.98443733]
 [14780.58587329 16007.3805716  14780.58587329 16007.3805716 ]
 [14870.39721667 16187.00819474 14870.39721667 16187.00819474]
 [14963.48775649 16365.42172173 14963.48775649 16365.42172173]
 [15059.4685554  16543.02591775 15059.4685554  16543.02591775]
 [15158.04876856 16720.12757678 15158.04876856 16720.12757678]
 [15259.00483287 16896.96633336 15259.00483287 16896.96633336]
 [15362.16107099 17073.7340594  15362.16107099 17073.7340594 ]
 [15467.37693502 17250.58762149 15467.37693502 17250.58762149]
 [15574.53830884 17427.65757953 15574.53830884 17427.65757953]
 [15683.5513957  17605.05430009 15683.5513957  17605.05430009]
 [15794.33831069 17782.87236487 15794.33831069 17782.87236487]
 [15906.83383123 17961.19382125 15906.83383123 17961.19382125]
 [16020.98295454 18140.09062572 16020.98295454 18140.09062572]]
```

Below we plot the predictions along with uncertainty intervals.

```python
#Plotting predictions along with uncertainty:
plt.plot(tme_train, y_train, label = 'Original Data')
plt.plot(tme_test, predvalues, label = 'Forecast', color = 'black')
plt.plot(tme_test, predlower, color = 'green', label = 'Prediction lower bound')
plt.plot(tme_test, predupper, color = 'green', label = 'Prediction upper bound')
plt.plot(tme_test, y_test, color = 'red', label = 'Actual Future Values')
plt.legend()
plt.axvline(x=n_train, color='gray', linestyle='--')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

In this example, the predicted values are somewhat below the actual test values.

Instead of applying AR models, directly to the raw data, it is common practice to apply them to the logarithms.

```python
ylog_train = np.log(y_train)
ylog_test = np.log(y_test)
```

```python
armod_sm = AutoReg(ylog_train, lags = p).fit()
print(armod_sm.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  295
Model:                     AutoReg(1)   Log Likelihood                 877.497
Method:               Conditional MLE   S.D. of innovations              0.012
Date:                Fri, 31 Oct 2025   AIC                          -1748.994
Time:                        01:47:02   BIC                          -1737.943
Sample:                             1   HQIC                         -1744.569
                                  295
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0273      0.004      7.271      0.000       0.020       0.035
y.L1           0.9984      0.000   2033.940      0.000       0.997       0.999
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.0016           +0.0000j            1.0016            0.0000
-----------------------------------------------------------------------------
```

Predictions are obtained as follows.

```python
fcast = armod_sm.get_prediction(start = n_train, end = n_train+k-1)
fcast_mean = fcast.predicted_mean #this gives the point predictions
```

Prediction uncertainty intervals are obtained as follows.

```python
fcast_se = fcast.se_mean
alpha = 0.05
z_alpha_half = stats.norm.ppf(1 - alpha/2)
predlower = fcast_mean - z_alpha_half * fcast_se
predupper = fcast_mean + z_alpha_half * fcast_se
fcast_int = fcast.conf_int()
print(np.column_stack([predlower, predupper, fcast_int]))
```

```
[[9.56863084 9.61658311 9.56863084 9.61658311]
 [9.57084537 9.63860634 9.57084537 9.63860634]
 [9.57536344 9.65828756 9.57536344 9.65828756]
 [9.58106762 9.67674429 9.58106762 9.67674429]
 [9.5875247  9.69440978 9.5875247  9.69440978]
 [9.59451235 9.71150643 9.59451235 9.71150643]
 [9.60189838 9.72816647 9.60189838 9.72816647]
 [9.60959661 9.74447617 9.60959661 9.74447617]
 [9.61754713 9.76049548 9.61754713 9.76049548]
 [9.6257063  9.7762681  9.6257063  9.7762681 ]
 [9.63404116 9.79182707 9.63404116 9.79182707]
 [9.64252607 9.80719807 9.64252607 9.80719807]
 [9.65114064 9.82240156 9.65114064 9.82240156]
 [9.65986833 9.83745414 9.65986833 9.83745414]
 [9.6686955  9.8523695  9.6686955  9.8523695 ]
 [9.67761074 9.86715912 9.67761074 9.86715912]
 [9.68660442 9.88183269 9.68660442 9.88183269]
 [9.69566826 9.89639854 9.69566826 9.89639854]
 [9.70479516 9.91086384 9.70479516 9.91086384]]
```

```python
plt.plot(tme_train, y_train, label = 'Training Data')
plt.plot(tme_test, np.exp(fcast_mean), label = 'Forecast', color = 'black') #Note the exponentiation
plt.plot(tme_test, y_test, color = 'red',  label = 'Actual future values')
plt.plot(tme_test, np.exp(predlower), color = 'green', label = 'Prediction lower bound')
plt.plot(tme_test, np.exp(predupper), color = 'green', label = 'Prediction upper bound')
plt.axvline(x=n_train, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Note that now the predictions are slightly closer to the actual observations.

```python
plt.plot(tme_train, y_train, label = 'Training Data')
plt.plot(tme_test, np.exp(fcast_mean), label = 'Predictions with logs', color = 'black') #Note the exponentiation
plt.plot(tme_test, y_test, color = 'red',  label = 'Actual future values')
plt.plot(tme_test, preds_nolog, color = 'darkgreen',  label = 'Predictions without logs')
plt.axvline(x=n_train, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[Up: contents](index.md) · [Dataset Two: House Price Data from FRED →](02-dataset-two-house-price-data-from-fred.md)
