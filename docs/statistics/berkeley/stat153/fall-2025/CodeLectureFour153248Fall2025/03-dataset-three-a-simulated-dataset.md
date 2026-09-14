---
title: 'Dataset Three: A Simulated Dataset'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFour153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureFour153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Dataset Three: A Simulated Dataset

**Source:** [`CodeLectureFour153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFour153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
#A simulated dataset
n = 400
x = np.arange(1, n+1)
sig = 1000
rng = np.random.default_rng(12345)
#quadratic data with noise
y = 5 + 0.8 * ((x - (n/2)) ** 2) + rng.normal(loc = 0, scale = sig, size = n)
plt.plot(y)
plt.xlabel("Time")
plt.ylabel("Data")
plt.title("A simulated dataset")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us fit a line (not a quadratic) to this dataset.

```python
X = np.column_stack([np.ones(n), x])
linmod = sm.OLS(y, X).fit()
plt.plot(y)
plt.plot(linmod.fittedvalues, color = "red")
plt.xlabel("Time")
plt.ylabel("Data")
plt.title("A simulated dataset")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
N = 1000 #number of samples to generate
n = X.shape[0]
m = X.shape[1] - 1
beta_samples = multivariate_t.rvs(loc=linmod.params, shape=linmod.cov_params(), df=n - m - 1, size=N)
print(beta_samples)
plt.plot(y)
for r in range(N):
    fvalsnew = np.dot(X, beta_samples[r])
    plt.plot(fvalsnew,  color = 'red')
plt.plot(y, color = 'blue')
plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Simulated Dataset')
plt.show()
```

```
[[ 9.66930939e+03  6.35948185e-01]
 [ 9.82173879e+03  4.95083835e+00]
 [ 1.07166131e+04 -2.58237495e+00]
 ...
 [ 1.11091843e+04 -2.96914690e+00]
 [ 1.17110546e+04 -2.56353648e+00]
 [ 1.08299014e+04  1.92028758e+00]]
```

*(1 figure omitted — see the original notebook.)*

The correct thing here is to fit a quadratic. This is done by multiple linear regression as shown below.

```python
X  = np.column_stack([np.ones(n), x, x ** 2])
quadmod = sm.OLS(y, X).fit()
print(quadmod.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.989
Model:                            OLS   Adj. R-squared:                  0.989
Method:                 Least Squares   F-statistic:                 1.849e+04
Date:                Tue, 09 Sep 2025   Prob (F-statistic):               0.00
Time:                        16:58:01   Log-Likelihood:                -3325.9
No. Observations:                 400   AIC:                             6658.
Df Residuals:                     397   BIC:                             6670.
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         3.2e+04    149.517    214.033      0.000    3.17e+04    3.23e+04
x1          -319.9986      1.722   -185.840      0.000    -323.384    -316.613
x2             0.7997      0.004    192.309      0.000       0.792       0.808
==============================================================================
Omnibus:                        0.637   Durbin-Watson:                   1.911
Prob(Omnibus):                  0.727   Jarque-Bera (JB):                0.732
Skew:                          -0.004   Prob(JB):                        0.693
Kurtosis:                       2.791   Cond. No.                     2.16e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.16e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
```

```python
N = 1000 #number of samples to generate
n = X.shape[0]
m = X.shape[1] - 1
beta_samples = multivariate_t.rvs(loc=quadmod.params, shape=quadmod.cov_params(), df=n - m - 1, size=N)
print(beta_samples)
plt.plot(y)
for r in range(N):
    fvalsnew = np.dot(X, beta_samples[r])
    plt.plot(fvalsnew,  color = 'red')
#plt.plot(y, color = 'blue')
plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Simulated Dataset')
plt.show()
```

```
[[ 3.21069430e+04 -3.22423230e+02  8.05609683e-01]
 [ 3.16930896e+04 -3.16670879e+02  7.94291883e-01]
 [ 3.19318577e+04 -3.19033173e+02  7.96698822e-01]
 ...
 [ 3.20219463e+04 -3.19719476e+02  7.98186797e-01]
 [ 3.15799399e+04 -3.15402767e+02  7.89790348e-01]
 [ 3.19058432e+04 -3.19227293e+02  7.98035112e-01]]
```

*(1 figure omitted — see the original notebook.)*

---

[← Dataset Two: Lake Huron Levels](02-dataset-two-lake-huron-levels.md) · [Up: contents](index.md)
