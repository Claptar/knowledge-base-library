---
title: 'Dataset One: US Population'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFive153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureFive153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureFive153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFive153248Fall2026.ipynb) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Dataset One: US Population

```python
uspop = pd.read_csv("POPTHM_27Aug2026.csv")
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
806       2026-03-01  342627
807       2026-04-01  342680
808       2026-05-01  342746
809       2026-06-01  342822
810       2026-07-01  342909

[811 rows x 2 columns]
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
Method:                 Least Squares   F-statistic:                 2.794e+05
Date:                Thu, 10 Sep 2026   Prob (F-statistic):               0.00
Time:                        19:35:53   Log-Likelihood:                -7554.3
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
const    174585.548486
x1          213.215735
dtype: float64
5851610121.093412
[[ 3.57412307e+04 -6.60651215e+01]
 [-6.60651215e+01  1.62721974e-01]]
```

This matrix $\frac{S(\hat{\beta})}{n-m-1} (X^T X)^{-1}$ is actually calculated as part of the sm.OLS output, and can be obtained as follows:

```python
print(linmod.cov_params()) #this coincides with Sigma calculated above. Check out help(linmod.cov_params) for more details.
print(Sigma)
```

```
const         x1
const  35741.230736 -66.065122
x1       -66.065122   0.162722
[[ 3.57412307e+04 -6.60651215e+01]
 [-6.60651215e+01  1.62721974e-01]]
```

Now we need to generate observations from the $t$-distribution. For this, we shall use an inbuilt function from scipy:

```python
from scipy.stats import multivariate_t
N = 1000 #number of samples to generate
beta_samples = multivariate_t.rvs(loc=betahat, shape=Sigma, df=n - m - 1, size=N)
print(beta_samples)
```

```
[[174721.3080949     213.12657353]
 [174305.73941779    213.6399766 ]
 [174822.94796507    212.62380814]
 ...
 [174662.70781635    213.3719372 ]
 [174460.98218758    213.5398607 ]
 [174747.83235296    212.89862161]]
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

[← Introduction](01-introduction.md) · [Up: contents](index.md) · Dataset Two: Lake Huron Levels →
