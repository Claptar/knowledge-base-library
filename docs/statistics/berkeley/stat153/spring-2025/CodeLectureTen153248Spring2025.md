---
title: CodeLectureTen153248Spring2025
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# CodeLectureTen153248Spring2025

**Source:** [`CodeLectureTen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: High-dimensional Regression -- Ridge and LASSO
---

We illustrate regularization in high-dimensional regression in the context of a simple high-dimensional linear regression model that is applicable to the CA population dataset.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

Here is the CA population dataset from FRED.

```python
capop = pd.read_csv('CAPOP-Feb2025FRED.csv')
print(capop.head(10))
print(capop.tail(10))
tme = np.arange(1900, 2025)
plt.plot(tme, capop['CAPOP'])
plt.xlabel("Time (years)")
plt.ylabel('Population (thousands of persons)')
plt.title("Resident Population of California")
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

It is better to fit regression models to the logarithm of the population for better interpretability.

```python
y = np.log(capop['CAPOP'])
n = len(y)
plt.plot(tme, y)
plt.xlabel("Time (years)")
plt.ylabel('Log(Population in thousands)')
plt.title("Logarithms of Resident CA population")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The model we consider is:
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
Date:                Thu, 20 Feb 2025   Prob (F-statistic):                nan
Time:                        16:27:38   Log-Likelihood:                 3312.0
No. Observations:                 125   AIC:                            -6374.
Df Residuals:                       0   BIC:                            -6020.
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
Omnibus:                       16.182   Durbin-Watson:                   0.005
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               19.260
Skew:                           0.961   Prob(JB):                     6.57e-05
Kurtosis:                       3.028   Cond. No.                     1.78e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.78e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.11/site-packages/statsmodels/regression/linear_model.py:1795: RuntimeWarning: divide by zero encountered in divide
  return 1 - (np.divide(self.nobs - self.k_constant, self.df_resid)
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.11/site-packages/statsmodels/regression/linear_model.py:1795: RuntimeWarning: invalid value encountered in scalar multiply
  return 1 - (np.divide(self.nobs - self.k_constant, self.df_resid)
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.11/site-packages/statsmodels/regression/linear_model.py:1717: RuntimeWarning: divide by zero encountered in scalar divide
  return np.dot(wresid, wresid) / self.df_resid
```

As discussed in class, in this unregularized estimation, the estimate of $\beta_0$ equals $y_1$, the estimate of $\beta_1$ is $y_2 - y_1$, and the estimate of $\beta_j$ is $y_{j+1} - 2 y_j + y_{j-1}$ for $j = 2, \dots, n-1$. Let us check this.

```python
print(y[0])
print(y[1] - y[0])
print(y[2] - y[1] - y[1] + y[0])
```

```
7.306531398939505
0.03947881097378758
0.006542546627510859
```

We now compute the ridge and lasso regularized estimators using the optimization library cvxpy.

```python
import cvxpy as cp
```

Here is the function for solving the ridge optimization function.

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

Below is the code for computing the ridge estimator. Play around with different values of $\lambda$ and see how the estimator changes.

```python
b_ridge = solve_ridge(Xfull, y, lambda_val = 100000)
print(b_ridge)
```

```
[ 7.40992500e+00  4.00275320e-02 -1.03393598e-06 -3.10729516e-06
 -6.16012894e-06 -1.01173938e-05 -1.48639792e-05 -2.02516508e-05
 -2.62512136e-05 -3.28752427e-05 -4.00153757e-05 -4.75259297e-05
 -5.52764995e-05 -6.31470039e-05 -7.10198428e-05 -7.87699738e-05
 -8.63654917e-05 -9.39528806e-05 -1.01719569e-04 -1.09738889e-04
 -1.18120654e-04 -1.27023211e-04 -1.36213007e-04 -1.45423138e-04
 -1.54537869e-04 -1.63267866e-04 -1.71382635e-04 -1.78857604e-04
 -1.85662158e-04 -1.91743221e-04 -1.97103040e-04 -2.01773603e-04
 -2.05808616e-04 -2.09384087e-04 -2.12750427e-04 -2.16159037e-04
 -2.19814220e-04 -2.23891485e-04 -2.28486860e-04 -2.33668768e-04
 -2.39599808e-04 -2.46442465e-04 -2.54308514e-04 -2.63142884e-04
 -2.72627130e-04 -2.82155494e-04 -2.91566429e-04 -3.00762399e-04
 -3.09851859e-04 -3.18886155e-04 -3.27961902e-04 -3.37138098e-04
 -3.46414491e-04 -3.55691964e-04 -3.64846907e-04 -3.73676401e-04
 -3.82093673e-04 -3.90105211e-04 -3.97580623e-04 -4.04423834e-04
 -4.10505946e-04 -4.15729902e-04 -4.20124229e-04 -4.23583035e-04
 -4.26041094e-04 -4.27428402e-04 -4.27744145e-04 -4.27016646e-04
 -4.25360420e-04 -4.22864312e-04 -4.19667094e-04 -4.15854221e-04
 -4.11538004e-04 -4.06771708e-04 -4.01673406e-04 -3.96337483e-04
 -3.90845810e-04 -3.85251015e-04 -3.79589124e-04 -3.73887359e-04
 -3.68143201e-04 -3.62381775e-04 -3.56575992e-04 -3.50724535e-04
 -3.44806777e-04 -3.38800872e-04 -3.32707570e-04 -3.26485166e-04
 -3.20069926e-04 -3.13395840e-04 -3.06395322e-04 -2.98980587e-04
 -2.91074778e-04 -2.82691733e-04 -2.73845422e-04 -2.64610204e-04
 -2.55090757e-04 -2.45387384e-04 -2.35563178e-04 -2.25633058e-04
 -2.15602793e-04 -2.05478754e-04 -1.95154510e-04 -1.84629119e-04
 -1.73930098e-04 -1.63087521e-04 -1.52147718e-04 -1.41175179e-04
 -1.30250046e-04 -1.19441443e-04 -1.08783405e-04 -9.83089351e-05
 -8.80504949e-05 -7.80515235e-05 -6.83575323e-05 -5.90136572e-05
 -5.00588542e-05 -4.15361782e-05 -3.35074027e-05 -2.60485765e-05
 -1.92581650e-05 -1.32596431e-05 -8.15496520e-06 -4.16377748e-06
 -1.40922376e-06]
```

Below we plot the fitted values corresponding to the ridge estimator.

```python
plt.plot(y)
ridge_fitted = np.dot(Xfull, b_ridge)
plt.plot(ridge_fitted, color = 'red')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Here is the function for minimizing the LASSO objective function.

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

Below we compute the LASSO estimator. Play around with different values of $\lambda$ to see how the estimator changes.

```python
b_lasso = solve_lasso(Xfull, y, lambda_val = .01)
print(b_lasso)
```

```
[ 7.30269244e+00  4.59956784e-02  1.13278408e-08  1.92462120e-03
 -6.40268980e-08 -8.76035991e-08 -3.26952149e-04  2.39052977e-07
  3.15904351e-07  4.25073456e-03 -8.28996771e-07 -1.43863686e-06
 -1.38512978e-06 -7.25660808e-07 -1.18645663e-02 -1.28015230e-02
  2.50450783e-06  4.92198082e-06  5.37794880e-06  3.39542374e-06
  3.32017284e-02 -2.85923941e-06 -4.18132818e-06 -3.62826460e-06
 -1.78335862e-06 -1.72912123e-02 -8.43883921e-04 -4.69975439e-11
 -4.33949820e-03 -3.51071562e-03 -2.36868613e-03 -1.62391659e-02
 -7.05713503e-04  2.49825628e-11  4.86634719e-11  5.48622386e-03
  2.67797948e-03  4.60402492e-07  8.60595266e-07  8.60883578e-07
  4.60848871e-07  1.59946901e-02  3.65403551e-02  1.86624170e-11
 -1.57150031e-02 -1.93457918e-02 -1.43745192e-02  2.65602870e-09
  4.10959590e-09  2.66020735e-09  5.39348565e-03  1.19154305e-02
 -4.84872664e-12 -4.77326914e-12 -2.72354092e-03 -1.71136426e-03
 -2.64531238e-08 -4.09115505e-08 -2.65104251e-08 -1.67071216e-03
 -3.64020007e-03 -1.73333766e-08 -2.67839762e-08 -1.73251145e-08
 -6.10737429e-03 -4.40160149e-03 -8.63951229e-03 -1.34388452e-05
 -3.06913086e-05 -4.38085884e-05 -4.82612296e-05 -4.35525458e-05
 -3.23813391e-05 -1.89046354e-05 -7.09617760e-06  1.44915200e-03
  2.34048430e-03  8.38154364e-04  1.22310692e-03 -1.03101380e-05
  5.58349511e-04  5.77659149e-05  1.03355846e-04  1.00494541e-04
  5.27519904e-05  1.36670616e-03  1.76617276e-03  8.27241055e-07
  1.54282048e-06  1.54261199e-06  8.25823151e-07 -7.35378888e-03
 -3.39093469e-03 -5.74667286e-03  2.19044354e-09  3.39867679e-09
  2.20626934e-09  4.56438963e-03  3.71658355e-03  4.01577424e-04
 -3.25710647e-11 -4.04463837e-11 -3.26305587e-03 -3.21252006e-03
 -2.19308890e-03  1.92695815e-06  3.41184415e-06  2.91348012e-06
  5.94052415e-04 -5.30573306e-06 -1.36812511e-05 -2.40850769e-05
 -3.27590936e-05 -3.47276195e-05 -2.72549705e-05 -1.29144758e-05
 -1.79378810e-03 -1.74887499e-03 -2.63274301e-03 -3.13695391e-03
 -2.35150806e-08 -3.69481411e-08 -2.47371116e-08  1.21429028e-03
  4.75900086e-09]
```

The LASSO estimator is typically sparse. This can be checked by the code below where we only display the estimated coefficients which cross a threshold in absolute value.

```python
threshold = 1e-6
significant_idx = np.where(np.abs(b_lasso) > threshold)[0]
print(b_lasso[significant_idx])
# Or to see index-value pairs:
for idx in significant_idx:
    print(f"Index {idx}: {b_lasso[idx]}")
```

```
[ 7.30269244e+00  4.59956784e-02  1.92462120e-03 -3.26952149e-04
  4.25073456e-03 -1.43863686e-06 -1.38512978e-06 -1.18645663e-02
 -1.28015230e-02  2.50450783e-06  4.92198082e-06  5.37794880e-06
  3.39542374e-06  3.32017284e-02 -2.85923941e-06 -4.18132818e-06
 -3.62826460e-06 -1.78335862e-06 -1.72912123e-02 -8.43883921e-04
 -4.33949820e-03 -3.51071562e-03 -2.36868613e-03 -1.62391659e-02
 -7.05713503e-04  5.48622386e-03  2.67797948e-03  1.59946901e-02
  3.65403551e-02 -1.57150031e-02 -1.93457918e-02 -1.43745192e-02
  5.39348565e-03  1.19154305e-02 -2.72354092e-03 -1.71136426e-03
 -1.67071216e-03 -3.64020007e-03 -6.10737429e-03 -4.40160149e-03
 -8.63951229e-03 -1.34388452e-05 -3.06913086e-05 -4.38085884e-05
 -4.82612296e-05 -4.35525458e-05 -3.23813391e-05 -1.89046354e-05
 -7.09617760e-06  1.44915200e-03  2.34048430e-03  8.38154364e-04
  1.22310692e-03 -1.03101380e-05  5.58349511e-04  5.77659149e-05
  1.03355846e-04  1.00494541e-04  5.27519904e-05  1.36670616e-03
  1.76617276e-03  1.54282048e-06  1.54261199e-06 -7.35378888e-03
 -3.39093469e-03 -5.74667286e-03  4.56438963e-03  3.71658355e-03
  4.01577424e-04 -3.26305587e-03 -3.21252006e-03 -2.19308890e-03
  1.92695815e-06  3.41184415e-06  2.91348012e-06  5.94052415e-04
 -5.30573306e-06 -1.36812511e-05 -2.40850769e-05 -3.27590936e-05
 -3.47276195e-05 -2.72549705e-05 -1.29144758e-05 -1.79378810e-03
 -1.74887499e-03 -2.63274301e-03 -3.13695391e-03  1.21429028e-03]
Index 0: 7.3026924431482705
Index 1: 0.04599567836808963
Index 3: 0.001924621204141603
Index 6: -0.00032695214938934143
Index 9: 0.004250734557060632
Index 11: -1.4386368627679639e-06
Index 12: -1.3851297798412922e-06
Index 14: -0.011864566340370837
Index 15: -0.012801523037577886
Index 16: 2.5045078279208125e-06
Index 17: 4.921980819115612e-06
Index 18: 5.377948803675375e-06
Index 19: 3.3954237383557336e-06
Index 20: 0.03320172839965602
Index 21: -2.8592394114197065e-06
Index 22: -4.181328176815231e-06
Index 23: -3.6282646012395853e-06
Index 24: -1.7833586210799803e-06
Index 25: -0.017291212320518088
Index 26: -0.0008438839213785009
Index 28: -0.004339498200935062
Index 29: -0.003510715624334767
Index 30: -0.0023686861296357974
Index 31: -0.016239165914857894
Index 32: -0.0007057135028570661
Index 35: 0.005486223863096445
Index 36: 0.0026779794844688956
Index 41: 0.01599469012916109
Index 42: 0.03654035506139316
Index 44: -0.015715003090321894
Index 45: -0.019345791807218307
Index 46: -0.014374519230820651
Index 50: 0.005393485645496251
Index 51: 0.011915430498422428
Index 54: -0.0027235409187174563
Index 55: -0.0017113642603826245
Index 59: -0.0016707121608208974
Index 60: -0.003640200070043141
Index 64: -0.0061073742912775815
Index 65: -0.004401601485561286
Index 66: -0.008639512287568141
Index 67: -1.3438845192513127e-05
Index 68: -3.069130858951492e-05
Index 69: -4.380858835649143e-05
Index 70: -4.826122956626966e-05
Index 71: -4.355254584063083e-05
Index 72: -3.23813390726035e-05
Index 73: -1.890463543856427e-05
Index 74: -7.0961775967126024e-06
Index 75: 0.0014491520039281195
Index 76: 0.002340484298417104
Index 77: 0.0008381543643658823
Index 78: 0.0012231069197806777
Index 79: -1.0310137996785056e-05
Index 80: 0.0005583495113130934
Index 81: 5.776591486423462e-05
Index 82: 0.00010335584577512392
Index 83: 0.00010049454051912188
Index 84: 5.275199039689996e-05
Index 85: 0.0013667061577776983
Index 86: 0.0017661727605670133
Index 88: 1.5428204783865242e-06
Index 89: 1.5426119851903527e-06
Index 91: -0.007353788883304698
Index 92: -0.00339093468885236
Index 93: -0.005746672859874951
Index 97: 0.00456438962851299
Index 98: 0.0037165835536422157
Index 99: 0.00040157742359940823
Index 102: -0.003263055873844618
Index 103: -0.0032125200647176817
Index 104: -0.002193088901138311
Index 105: 1.926958149968248e-06
Index 106: 3.4118441536081185e-06
Index 107: 2.9134801193348907e-06
Index 108: 0.0005940524150163305
Index 109: -5.30573306460303e-06
Index 110: -1.3681251105176545e-05
Index 111: -2.4085076864502885e-05
Index 112: -3.275909364139106e-05
Index 113: -3.472761950563112e-05
Index 114: -2.7254970502129083e-05
Index 115: -1.291447575177195e-05
Index 116: -0.0017937880988986073
Index 117: -0.0017488749884387517
Index 118: -0.0026327430103439717
Index 119: -0.0031369539121646347
Index 123: 0.0012142902796427532
```

```python
plt.plot(y, color = 'None')
ridge_fitted = np.dot(Xfull, b_ridge)
plt.plot(ridge_fitted, color = 'None')
lasso_fitted = np.dot(Xfull, b_lasso)
plt.plot(lasso_fitted, color = 'black')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[Up: contents](index.md)
