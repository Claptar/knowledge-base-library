---
title: 'Dataset Three: A Simulated Dataset'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFive153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureFive153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureFive153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFive153248Fall2026.ipynb) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Dataset Three: A Simulated Dataset

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
[[ 1.24847900e+04 -7.45209402e+00]
 [ 9.66084443e+03  5.88415623e+00]
 [ 1.14314746e+04 -4.28814832e+00]
 ...
 [ 1.10088743e+04 -1.72996011e+00]
 [ 1.04394835e+04  1.05566039e+00]
 [ 1.13698106e+04  1.56511066e+00]]
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
Date:                Thu, 10 Sep 2026   Prob (F-statistic):               0.00
Time:                        19:45:58   Log-Likelihood:                -3325.9
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
[[ 3.18471308e+04 -3.17976656e+02  7.94430399e-01]
 [ 3.19486063e+04 -3.20504111e+02  8.01512967e-01]
 [ 3.20846821e+04 -3.20623326e+02  8.01345909e-01]
 ...
 [ 3.22390951e+04 -3.21993886e+02  8.03728479e-01]
 [ 3.18593038e+04 -3.18269400e+02  7.95333099e-01]
 [ 3.18704431e+04 -3.19046782e+02  7.98341252e-01]]
```

*(1 figure omitted — see the original notebook.)*

## Standard Errors and Intervals in Regression

Consider the simple linear regression model:
\begin{align*}
   y_t = \beta_0 + \beta_1 t + \epsilon_t
\end{align*}
that we used in Lecture 2 for the US population dataset.

```python
uspop = pd.read_csv('POPTHM_27Aug2026.csv')
y = uspop['POPTHM']
n = len(y)
x = np.arange(1, n + 1)
X = np.column_stack([np.ones(n),x])

md1 = sm.OLS(y, X).fit()
print(md1.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                 POPTHM   R-squared:                       0.997
Model:                            OLS   Adj. R-squared:                  0.997
Method:                 Least Squares   F-statistic:                 2.794e+05
Date:                Thu, 10 Sep 2026   Prob (F-statistic):               0.00
Time:                        19:46:45   Log-Likelihood:                -7554.3
No. Observations:                 811   AIC:                         1.511e+04
Df Residuals:                     809   BIC:                         1.512e+04
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       1.746e+05    189.054    923.472      0.000    1.74e+05    1.75e+05
x1           213.2157      0.403    528.562      0.000     212.424     214.008
==============================================================================
Omnibus:                      562.602   Durbin-Watson:                   0.000
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               69.512
Skew:                          -0.398   Prob(JB):                     8.05e-16
Kurtosis:                       1.807   Cond. No.                         938.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

The output above reports that the standard error corresponding to the estimate for $\beta_1$ is 0.403 and the 95% interval for $\beta_1$ is $[212.424, 214.008]$. These quantities can also be obtained from the regression output as follows.

```python
print(md1.params) #these are the betahats (least squares estimates)
print(md1.bse) #these are the standard errors of the betahats
print(md1.conf_int(alpha=0.05)) #these are the 95% confidence intervals
```

```
const    174585.548486
x1          213.215735
dtype: float64
const    189.053513
x1         0.403388
dtype: float64
                   0              1
const  174214.455222  174956.641750
x1        212.423924     214.007546
```

We can obtain these manually using the formulae that we derived and check if we are getting exactly the same answers.

```python
#For betahat:
betahat = np.linalg.inv(X.T @ X) @ X.T @ y
print(betahat)
print(md1.params) #these are the betahats (least squares estimates)
```

```
[174585.54848609    213.21573493]
const    174585.548486
x1          213.215735
dtype: float64
```

```python
#For standard errors:
residuals = y - X @ betahat
sigma2hat = (residuals.T @ residuals) / (n - X.shape[1])
var_betahat = sigma2hat * np.linalg.inv(X.T @ X)
se_betahat = np.sqrt(np.diag(var_betahat))
print(se_betahat)
print(md1.bse) #these are the standard errors of the betahats
```

```
[189.05351289   0.40338812]
const    189.053513
x1         0.403388
dtype: float64
```

```python
#For confidence intervals:
from scipy.stats import t
alpha = 0.05
t_critical = t.ppf(1 - alpha/2, df=n - X.shape[1]) #this computes t_{df, 1-alpha/2}
conf_int_lower = betahat - t_critical * se_betahat
conf_int_upper = betahat + t_critical * se_betahat
conf_int = np.column_stack((conf_int_lower, conf_int_upper))
print(conf_int)
print(md1.conf_int(alpha=0.05)) #these are the 95% confidence intervals
```

```
[[174214.45522237 174956.64174982]
 [   212.42392413    214.00754573]]
                   0              1
const  174214.455222  174956.641750
x1        212.423924     214.007546
```

---

← Dataset Two: Lake Huron Levels · [Up: contents](index.md)
