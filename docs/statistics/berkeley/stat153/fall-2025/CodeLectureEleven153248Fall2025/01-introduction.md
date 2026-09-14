---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEleven153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Ridge and LASSO Regularization
---

In the last lecture, we started discussing nonlinear regression models. As a motivating example, we considered the following dataset (from FRED) on Annual Estimates of the Resident Population of California (units are thousands of persons) from 1900 to 2024.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

```python
capop = pd.read_csv('CAPOP_11Sept2025.csv')
print(capop.head(10))
print(capop.tail(10))
tme = np.arange(1900, 2025)
plt.plot(tme, capop['CAPOP'], label='California Population')
plt.xlabel('Year')
plt.ylabel('Population (in thousands)')
plt.title('California Annual Resident Population (in thousands)')
plt.show()
```

```
observation_date   CAPOP
0       1900-01-01  1490.0
1       1901-01-01  1550.0
2       1902-01-01  1623.0
3       1903-01-01  1702.0
4       1904-01-01  1792.0
5       1905-01-01  1893.0
6       1906-01-01  1976.0
7       1907-01-01  2054.0
8       1908-01-01  2161.0
9       1909-01-01  2282.0
    observation_date      CAPOP
115       2015-01-01  38904.296
116       2016-01-01  39149.186
117       2017-01-01  39337.785
118       2018-01-01  39437.463
119       2019-01-01  39437.610
120       2020-01-01  39521.958
121       2021-01-01  39142.565
122       2022-01-01  39142.414
123       2023-01-01  39198.693
124       2024-01-01  39431.263
```

*(1 figure omitted — see the original notebook.)*

We work with the logarithms of the population data as this will lead to models with better interpretability.

```python
y = np.log(capop['CAPOP'])
n = len(y)
plt.plot(tme, y)
plt.xlabel('Year')
plt.ylabel('Log(Population in thousands)')
plt.title('Logarithm of California Annual Resident Population (in thousands)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We shall fit the following model to this dataset:
\begin{equation*}
  y_t = \beta_0 + \beta_1 (t - 1) + \beta_2 (t - 2)_+ + \beta_3 (t - 3)_+ + \dots + \beta_{n-1} (t - (n-1))_+ + \epsilon_t
\end{equation*}
We can write this as
\begin{equation*}
   y = X_{\text{full}} \beta + \epsilon
\end{equation*}
where $X_{\text{full}}$ is constructed as below.

```python
n = len(y)
x = np.arange(1, n+1)
Xfull = np.column_stack([np.ones(n), x-1])
for i in range(n-2):
    c = i+2
    xc = ((x > c).astype(float))*(x-c)
    Xfull = np.column_stack([Xfull, xc])
print(Xfull)
```

```
[[  1.   0.  -0. ...  -0.  -0.  -0.]
 [  1.   1.   0. ...  -0.  -0.  -0.]
 [  1.   2.   1. ...  -0.  -0.  -0.]
 ...
 [  1. 122. 121. ...   1.   0.  -0.]
 [  1. 123. 122. ...   2.   1.   0.]
 [  1. 124. 123. ...   3.   2.   1.]]
```

If we fit this model without any regularization, we get the following.

```python
mdfull = sm.OLS(y, Xfull).fit()
print(mdfull.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                  CAPOP   R-squared:                       1.000
Model:                            OLS   Adj. R-squared:                    nan
Method:                 Least Squares   F-statistic:                       nan
Date:                Thu, 02 Oct 2025   Prob (F-statistic):                nan
Time:                        16:09:30   Log-Likelihood:                 3409.6
No. Observations:                 125   AIC:                            -6569.
Df Residuals:                       0   BIC:                            -6216.
Df Model:                         124
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          7.3065        inf          0        nan         nan         nan
x1             0.0395        inf          0        nan         nan         nan
x2             0.0065        inf          0        nan         nan         nan
x3             0.0015        inf          0        nan         nan         nan
x4             0.0040        inf          0        nan         nan         nan
x5             0.0033        inf          0        nan         nan         nan
x6            -0.0119        inf         -0        nan         nan         nan
x7            -0.0042        inf         -0        nan         nan         nan
x8             0.0121        inf          0        nan         nan         nan
x9             0.0037        inf          0        nan         nan         nan
x10           -0.0016        inf         -0        nan         nan         nan
x11           -0.0011        inf         -0        nan         nan         nan
x12           -0.0003        inf         -0        nan         nan         nan
x13            0.0007        inf          0        nan         nan         nan
x14           -0.0094        inf         -0        nan         nan         nan
x15           -0.0179        inf         -0        nan         nan         nan
x16           -0.0042        inf         -0        nan         nan         nan
x17            0.0113        inf          0        nan         nan         nan
x18           -0.0038        inf         -0        nan         nan         nan
x19           -0.0050        inf         -0        nan         nan         nan
x20            0.0391        inf          0        nan         nan         nan
x21            0.0032        inf          0        nan         nan         nan
x22           -0.0153        inf         -0        nan         nan         nan
x23            0.0172        inf          0        nan         nan         nan
x24           -0.0060        inf         -0        nan         nan         nan
x25           -0.0208        inf         -0        nan         nan         nan
x26            0.0004        inf          0        nan         nan         nan
x27            0.0021        inf          0        nan         nan         nan
x28           -0.0057        inf         -0        nan         nan         nan
x29           -0.0032        inf         -0        nan         nan         nan
x30           -0.0024        inf         -0        nan         nan         nan
x31           -0.0124        inf         -0        nan         nan         nan
x32           -0.0076        inf         -0        nan         nan         nan
x33           -0.0003        inf         -0        nan         nan         nan
x34            0.0045        inf          0        nan         nan         nan
x35            0.0027        inf          0        nan         nan         nan
x36            0.0077        inf          0        nan         nan         nan
x37            0.0025        inf          0        nan         nan         nan
x38           -0.0096        inf         -0        nan         nan         nan
x39           -0.0002        inf         -0        nan         nan         nan
x40            0.0048        inf          0        nan         nan         nan
x41            0.0164        inf          0        nan         nan         nan
x42            0.0261        inf          0        nan         nan         nan
x43            0.0285        inf          0        nan         nan         nan
x44           -0.0447        inf         -0        nan         nan         nan
x45           -0.0067        inf         -0        nan         nan         nan
x46           -0.0209        inf         -0        nan         nan         nan
x47            0.0054        inf          0        nan         nan         nan
x48           -0.0048        inf         -0        nan         nan         nan
x49            0.0034        inf          0        nan         nan         nan
x50            0.0056        inf          0        nan         nan         nan
x51            0.0095        inf          0        nan         nan         nan
x52            0.0021        inf          0        nan         nan         nan
x53            0.0076        inf          0        nan         nan         nan
x54           -0.0120        inf         -0        nan         nan         nan
x55           -0.0097        inf         -0        nan         nan         nan
x56            0.0133        inf          0        nan         nan         nan
x57           -0.0038        inf         -0        nan         nan         nan
x58            0.0029        inf          0        nan         nan         nan
x59           -0.0036        inf         -0        nan         nan         nan
x60           -0.0130        inf         -0        nan         nan         nan
x61            0.0130        inf          0        nan         nan         nan
x62           -0.0045        inf         -0        nan         nan         nan
x63         5.425e-05        inf          0        nan         nan         nan
x64           -0.0073        inf         -0        nan         nan         nan
x65           -0.0033        inf         -0        nan         nan         nan
x66           -0.0090        inf         -0        nan         nan         nan
x67            0.0021        inf          0        nan         nan         nan
x68           -0.0054        inf         -0        nan         nan         nan
x69            0.0049        inf          0        nan         nan         nan
x70           -0.0031        inf         -0        nan         nan         nan
x71            0.0055        inf          0        nan         nan         nan
x72           -0.0069        inf         -0        nan         nan         nan
x73            0.0020        inf          0        nan         nan         nan
x74            0.0008        inf          0        nan         nan         nan
x75            0.0025        inf          0        nan         nan         nan
x76            0.0013        inf          0        nan         nan         nan
x77            0.0005        inf          0        nan         nan         nan
x78            0.0026        inf          0        nan         nan         nan
x79           -0.0031        inf         -0        nan         nan         nan
x80            0.0049        inf          0        nan         nan         nan
x81           -0.0029        inf         -0        nan         nan         nan
x82            0.0016        inf          0        nan         nan         nan
x83           -0.0002        inf         -0        nan         nan         nan
x84           -0.0026        inf         -0        nan         nan         nan
x85            0.0039        inf          0        nan         nan         nan
x86            0.0019        inf          0        nan         nan         nan
x87        -9.855e-05        inf         -0        nan         nan         nan
x88           -0.0002        inf         -0        nan         nan         nan
x89            0.0017        inf          0        nan         nan         nan
x90           -0.0014        inf         -0        nan         nan         nan
x91           -0.0094        inf         -0        nan         nan         nan
x92           -0.0003        inf         -0        nan         nan         nan
x93           -0.0063        inf         -0        nan         nan         nan
x94           -0.0033        inf         -0        nan         nan         nan
x95            0.0002        inf          0        nan         nan         nan
x96            0.0035        inf          0        nan         nan         nan
x97            0.0046        inf          0        nan         nan         nan
x98            0.0007        inf          0        nan         nan         nan
x99           -0.0003        inf         -0        nan         nan         nan
x100           0.0111        inf          0        nan         nan         nan
x101          -0.0108        inf         -0        nan         nan         nan
x102          -0.0030        inf         -0        nan         nan         nan
x103          -0.0004        inf         -0        nan         nan         nan
x104          -0.0018        inf         -0        nan         nan         nan
x105          -0.0020        inf         -0        nan         nan         nan
x106          -0.0017        inf         -0        nan         nan         nan
x107           0.0010        inf          0        nan         nan         nan
x108           0.0034        inf          0        nan         nan         nan
x109         -1.6e-05        inf         -0        nan         nan         nan
x110       -5.495e-05        inf         -0        nan         nan         nan
x111          -0.0012        inf         -0        nan         nan         nan
x112          -0.0003        inf         -0        nan         nan         nan
x113       -4.045e-05        inf         -0        nan         nan         nan
x114           0.0005        inf          0        nan         nan         nan
x115          -0.0005        inf         -0        nan         nan         nan
x116          -0.0019        inf         -0        nan         nan         nan
x117          -0.0015        inf         -0        nan         nan         nan
x118          -0.0023        inf         -0        nan         nan         nan
x119          -0.0025        inf         -0        nan         nan         nan
x120           0.0021        inf          0        nan         nan         nan
x121          -0.0118        inf         -0        nan         nan         nan
x122           0.0096        inf          0        nan         nan         nan
x123           0.0014        inf          0        nan         nan         nan
x124           0.0045        inf          0        nan         nan         nan
==============================================================================
Omnibus:                        2.109   Durbin-Watson:                   0.015
Prob(Omnibus):                  0.348   Jarque-Bera (JB):                1.923
Skew:                          -0.203   Prob(JB):                        0.382
Kurtosis:                       2.548   Cond. No.                     1.78e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.78e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
/Users/aditya/mambaforge/envs/stat153fall2025/lib/python3.11/site-packages/statsmodels/regression/linear_model.py:1795: RuntimeWarning: divide by zero encountered in divide
  return 1 - (np.divide(self.nobs - self.k_constant, self.df_resid)
/Users/aditya/mambaforge/envs/stat153fall2025/lib/python3.11/site-packages/statsmodels/regression/linear_model.py:1795: RuntimeWarning: invalid value encountered in scalar multiply
  return 1 - (np.divide(self.nobs - self.k_constant, self.df_resid)
/Users/aditya/mambaforge/envs/stat153fall2025/lib/python3.11/site-packages/statsmodels/regression/linear_model.py:1717: RuntimeWarning: divide by zero encountered in scalar divide
  return np.dot(wresid, wresid) / self.df_resid
```

In this unregularized estimation, the estimate of $\beta_0$ equals $y_1$, the estimate of $\beta_1$ is $y_2 - y_1$, and the estimate of $\beta_j$ is $y_{j+1} - 2 y_j + y_{j-1}$ for $j = 2, \dots, n-1$. Let us check this.

```python
print(y[0], mdfull.params.iloc[0])
print(y[1] - y[0], mdfull.params.iloc[1])
print(y[2] - y[1] - y[1] + y[0], mdfull.params.iloc[2])
print(y[3] - y[2] - y[2] + y[1], mdfull.params.iloc[3])
print(y[4] - y[3] - y[3] + y[2], mdfull.params.iloc[4])
```

```
7.306531398939505 7.3065313989395415
0.03947881097378758 0.03947881097376421
0.006542546627510859 0.00654254662755926
0.0015063840174303067 0.001506384017439581
0.004000542782827132 0.0040005427827803555
```

## Ridge and LASSO regularized estimation

We now compute the ridge and lasso regularized estimators using the optimization library `cvxpy`. `cvxpy` is a library for formulating and solving convex optimization problems. It is widely used in Machine Learning, Statistics, Engineering etc.

```python
import cvxpy as cp
```

Here is the function for solving the ridge optimization problem. Given $y_{n \times 1}$, $X_{n  \times m}$ and $\lambda$, this code solves the problem:
\begin{align*}
    \text{Minimize} ~ \left[\|y - X \beta\|^2 + \lambda (\beta_s^2 + \dots + \beta_m^2) \right]
\end{align*}
Here $s$ denotes `penalty_start` in the code (the penalty does not involve $\beta_j$ for $j < s$).

```python
def solve_ridge(X, y, lambda_val, penalty_start=2):
    n, p = X.shape

    # Define variable
    beta = cp.Variable(p)

    # Define objective
    loss = cp.sum_squares(X @ beta - y)
    reg = lambda_val * cp.sum_squares(beta[penalty_start:])
    objective = cp.Minimize(loss + reg)

    # Solve problem
    prob = cp.Problem(objective)
    prob.solve()

    return beta.value
```

Below is the code for computing the ridge estimator with a fixed value of $\lambda$. We also plot the fitted values (these are the values $\hat{\mu}^{\text{ridge}}(\lambda) = X \hat{\beta}^{\text{ridge}}(\lambda)$) corresponding to the Ridge estimate.

Play around with  different values of $\lambda$ and see how the estimator changes.

```python
b_ridge = solve_ridge(Xfull, y, lambda_val = 10000) #lambda = 10000 seems to work well
#print(b_ridge)
plt.plot(y)
ridge_fitted = np.dot(Xfull, b_ridge)
plt.plot(ridge_fitted, color = 'red')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Here is the function for minimizing the LASSO objective function. Given $y_{n \times 1}$, $X_{n  \times m}$ and $\lambda$, this code solves the problem:
\begin{align*}
    \text{Minimize} ~ \left[\|y - X \beta\|^2 + \lambda (|\beta_s| + \dots + |\beta_m|) \right]
\end{align*}
Here $s$ denotes `penalty_start` in the code (the penalty does not involve $\beta_j$ for $j < s$).

```python
def solve_lasso(X, y, lambda_val, penalty_start=2):
    n, p = X.shape

    # Define variable
    beta = cp.Variable(p)

    # Define objective
    loss = cp.sum_squares(X @ beta - y)
    reg = lambda_val * cp.norm1(beta[penalty_start:])
    objective = cp.Minimize(loss + reg)

    # Solve problem
    prob = cp.Problem(objective)
    prob.solve()

    return beta.value
```

Below is the code for computing the ridge estimator with a fixed value of $\lambda$. We also plot the fitted values (these are the values $\hat{\mu}^{\text{lasso}}(\lambda) = X \hat{\beta}^{\text{lasso}}(\lambda)$) corresponding to the Ridge estimate.

Play around with  different values of $\lambda$ and see how the estimator changes.

```python
b_lasso = solve_lasso(Xfull, y, lambda_val = 25) #10 seems to work well
#print(b_lasso)
plt.plot(y)
lasso_fitted = np.dot(Xfull, b_lasso)
plt.plot(lasso_fitted, color = 'red')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The LASSO estimator is typically sparse. This can be checked by the code below where we only display the estimated coefficients which cross a threshold in absolute value.

```python
threshold = 1e-6
significant_idx = np.where(np.abs(b_lasso) > threshold)[0]
print(b_lasso[significant_idx])

---

[Up: contents](index.md) · [Or to see index-value pairs →](02-or-to-see-index-value-pairs.md)
