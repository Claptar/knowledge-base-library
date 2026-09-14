---
title: 'Dataset One: US Population'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFour153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureFour153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Dataset One: US Population

**Source:** [`CodeLectureFour153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFour153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
uspop = pd.read_csv("POPTHM_01September2025.csv")
print(uspop)
y = uspop['POPTHM']
n = len(y)
plt.plot(y)
plt.xlabel('Month (starting from Jan 1959)')
plt.ylabel('US Population (in thousands)')
plt.title('US Population from Jan 1959 to July 2025')
plt.show()
```

```
observation_date  POPTHM
0         1959-01-01  175818
1         1959-02-01  176044
2         1959-03-01  176274
3         1959-04-01  176503
4         1959-05-01  176723
..               ...     ...
794       2025-03-01  341729
795       2025-04-01  341874
796       2025-05-01  342032
797       2025-06-01  342197
798       2025-07-01  342370

[799 rows x 2 columns]
```

*(1 figure omitted — see the original notebook.)*

Let us fit the simple linear regression model to this data (with time as covariate).

```python
X = np.column_stack([np.ones(n), np.arange(1, n+1)])
linmod = sm.OLS(y, X).fit()
print(linmod.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                 POPTHM   R-squared:                       0.997
Model:                            OLS   Adj. R-squared:                  0.997
Method:                 Least Squares   F-statistic:                 2.740e+05
Date:                Tue, 09 Sep 2025   Prob (F-statistic):               0.00
Time:                        16:51:18   Log-Likelihood:                -7434.1
No. Observations:                 799   AIC:                         1.487e+04
Df Residuals:                     797   BIC:                         1.488e+04
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       1.745e+05    188.487    925.579      0.000    1.74e+05    1.75e+05
x1           213.6850      0.408    523.463      0.000     212.884     214.486
==============================================================================
Omnibus:                      396.334   Durbin-Watson:                   0.000
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               68.971
Skew:                          -0.439   Prob(JB):                     1.05e-15
Kurtosis:                       1.859   Cond. No.                         924.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

The fitted regression line is plotted below along with the observed data.

```python
import matplotlib.pyplot as plt
plt.plot(y)
plt.plot(linmod.fittedvalues)
plt.xlabel('Month (starting from Jan 1959)')
plt.ylabel('US Population (in thousands)')
plt.title('US Population from Jan 1959 to July 2025')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We have seen that the posterior distribution of $\beta_0, \dots, \beta_m$ is given by:
\begin{align*}
   \beta_0, \dots, \beta_m \mid \text{data} \sim t_{m+1} \left(\hat{\beta}, \frac{S(\hat{\beta})}{n-m-1} (X^T X)^{-1}, n-m-1 \right)
\end{align*}
We can generate samples from this posterior distribution and plot the resulting lines on the observed data. This will give us an idea of the uncertainty in the parameters.

```python
#First we compute betahat:
betahat = linmod.params
print(betahat)
#Next we compute S(betahat):
S_betahat = np.sum(linmod.resid ** 2)
print(S_betahat)
#Next Sigma = S_betahat / (n - m - 1) * (X^T X)^{-1}:
m = X.shape[1] - 1 #in this case, m = 1
n = len(y)
Sigma = S_betahat / (n - m - 1) * np.linalg.inv(X.T @ X)
print(Sigma)
```

```
const    174459.566196
x1          213.684996
dtype: float64
5645370656.649733
[[ 3.55273594e+04 -6.66554585e+01]
 [-6.66554585e+01  1.66638646e-01]]
```

This matrix $\frac{S(\hat{\beta})}{n-m-1} (X^T X)^{-1}$ is actually calculated as part of the sm.OLS output, and can be obtained as follows:

```python
print(linmod.cov_params()) #this coincides with Sigma calculated above. Check out help(linmod.cov_params) for more details.
print(Sigma)
```

```
const         x1
const  35527.359360 -66.655458
x1       -66.655458   0.166639
[[ 3.55273594e+04 -6.66554585e+01]
 [-6.66554585e+01  1.66638646e-01]]
```

Now we need to generate observations from the $t$-distribution. For this, we shall use an inbuilt function from scipy:

```python
from scipy.stats import multivariate_t
N = 1000 #number of samples to generate
beta_samples = multivariate_t.rvs(loc=betahat, shape=Sigma, df=n - m - 1, size=N)
print(beta_samples)
```

```
[[174575.00246433    213.39051485]
 [174508.28682041    213.59172482]
 [174109.0428557     214.55694998]
 ...
 [174248.6028745     213.98321738]
 [174411.00997082    213.71640042]
 [174507.67966125    213.30575799]]
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
plt.xlabel('Month (starting from Jan 1959)')
plt.ylabel('US Population (in thousands)')
plt.title('Lines corresponding to posterior samples')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[Up: contents](index.md) · [Dataset Two: Lake Huron Levels →](02-dataset-two-lake-huron-levels.md)
