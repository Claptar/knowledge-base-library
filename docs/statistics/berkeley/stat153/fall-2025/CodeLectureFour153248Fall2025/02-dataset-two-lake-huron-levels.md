---
title: 'Dataset Two: Lake Huron Levels'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFour153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureFour153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Dataset Two: Lake Huron Levels

**Source:** [`CodeLectureFour153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFour153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
#Lake Huron dataset which gives annual measurements of the level (in feet) of Lake Huron from 1875 to 1972
huron = pd.read_csv("LakeHuron.csv")
print(huron)
plt.plot(huron['x'])
plt.xlabel('Time (yearly)')
plt.ylabel('Feet')
plt.title('Lake Huron level from 1875 to 1972')
plt.show()
```

```
Unnamed: 0       x
0            1  580.38
1            2  581.86
2            3  580.97
3            4  580.80
4            5  579.79
..         ...     ...
93          94  578.52
94          95  579.74
95          96  579.31
96          97  579.89
97          98  579.96

[98 rows x 2 columns]
```

*(1 figure omitted — see the original notebook.)*

```python
y = huron['x']
n = len(y)
x = np.arange(1, n+1)
X = np.column_stack([np.ones(n), x])
print(X)
```

```
[[ 1.  1.]
 [ 1.  2.]
 [ 1.  3.]
 [ 1.  4.]
 [ 1.  5.]
 [ 1.  6.]
 [ 1.  7.]
 [ 1.  8.]
 [ 1.  9.]
 [ 1. 10.]
 [ 1. 11.]
 [ 1. 12.]
 [ 1. 13.]
 [ 1. 14.]
 [ 1. 15.]
 [ 1. 16.]
 [ 1. 17.]
 [ 1. 18.]
 [ 1. 19.]
 [ 1. 20.]
 [ 1. 21.]
 [ 1. 22.]
 [ 1. 23.]
 [ 1. 24.]
 [ 1. 25.]
 [ 1. 26.]
 [ 1. 27.]
 [ 1. 28.]
 [ 1. 29.]
 [ 1. 30.]
 [ 1. 31.]
 [ 1. 32.]
 [ 1. 33.]
 [ 1. 34.]
 [ 1. 35.]
 [ 1. 36.]
 [ 1. 37.]
 [ 1. 38.]
 [ 1. 39.]
 [ 1. 40.]
 [ 1. 41.]
 [ 1. 42.]
 [ 1. 43.]
 [ 1. 44.]
 [ 1. 45.]
 [ 1. 46.]
 [ 1. 47.]
 [ 1. 48.]
 [ 1. 49.]
 [ 1. 50.]
 [ 1. 51.]
 [ 1. 52.]
 [ 1. 53.]
 [ 1. 54.]
 [ 1. 55.]
 [ 1. 56.]
 [ 1. 57.]
 [ 1. 58.]
 [ 1. 59.]
 [ 1. 60.]
 [ 1. 61.]
 [ 1. 62.]
 [ 1. 63.]
 [ 1. 64.]
 [ 1. 65.]
 [ 1. 66.]
 [ 1. 67.]
 [ 1. 68.]
 [ 1. 69.]
 [ 1. 70.]
 [ 1. 71.]
 [ 1. 72.]
 [ 1. 73.]
 [ 1. 74.]
 [ 1. 75.]
 [ 1. 76.]
 [ 1. 77.]
 [ 1. 78.]
 [ 1. 79.]
 [ 1. 80.]
 [ 1. 81.]
 [ 1. 82.]
 [ 1. 83.]
 [ 1. 84.]
 [ 1. 85.]
 [ 1. 86.]
 [ 1. 87.]
 [ 1. 88.]
 [ 1. 89.]
 [ 1. 90.]
 [ 1. 91.]
 [ 1. 92.]
 [ 1. 93.]
 [ 1. 94.]
 [ 1. 95.]
 [ 1. 96.]
 [ 1. 97.]
 [ 1. 98.]]
```

```python
linmod = sm.OLS(y, X).fit()
print(linmod.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      x   R-squared:                       0.272
Model:                            OLS   Adj. R-squared:                  0.265
Method:                 Least Squares   F-statistic:                     35.95
Date:                Tue, 09 Sep 2025   Prob (F-statistic):           3.55e-08
Time:                        16:55:48   Log-Likelihood:                -150.05
No. Observations:                  98   AIC:                             304.1
Df Residuals:                      96   BIC:                             309.3
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        580.2020      0.230   2521.398      0.000     579.745     580.659
x1            -0.0242      0.004     -5.996      0.000      -0.032      -0.016
==============================================================================
Omnibus:                        1.626   Durbin-Watson:                   0.439
Prob(Omnibus):                  0.444   Jarque-Bera (JB):                1.274
Skew:                          -0.039   Prob(JB):                        0.529
Kurtosis:                       2.447   Cond. No.                         115.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
N = 1000 #number of samples to generate
n = X.shape[0]
m = X.shape[1] - 1
beta_samples = multivariate_t.rvs(loc=linmod.params, shape=linmod.cov_params(), df=n - m - 1, size=N)
print(beta_samples)
```

```
[[ 5.80499273e+02 -2.78497563e-02]
 [ 5.80376544e+02 -2.50568409e-02]
 [ 5.80254458e+02 -2.53452978e-02]
 ...
 [ 5.80128367e+02 -2.27296382e-02]
 [ 5.80430828e+02 -2.74647190e-02]
 [ 5.80262300e+02 -2.75464709e-02]]
```

```python
import matplotlib.pyplot as plt
plt.scatter(beta_samples[:,0], beta_samples[:,1], marker = '.')
plt.xlabel('Intercept')
plt.ylabel('Slope')
plt.title('Posterior Samples (drawn from t-distribution)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.plot(y)
for r in range(N):
    fvalsnew = np.dot(X, beta_samples[r])
    plt.plot(fvalsnew,  color = 'red')
plt.plot(y, color = 'blue')
plt.xlabel('Time (yearly)')
plt.ylabel('Feet')
plt.title('Lake Huron level from 1875 to 1972')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Dataset One: US Population](01-dataset-one-us-population.md) · [Up: contents](index.md) · [Dataset Three: A Simulated Dataset →](03-dataset-three-a-simulated-dataset.md)
