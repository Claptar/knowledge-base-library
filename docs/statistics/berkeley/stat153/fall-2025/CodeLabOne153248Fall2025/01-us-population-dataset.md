---
title: US Population Dataset
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# US Population Dataset

**Source:** [`CodeLabOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabOne153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

This dataset is downloaded from FRED and gives monthly population of the United States in thousands.

```python
import pandas as pd
uspop = pd.read_csv('POPTHM_01September2025.csv')
print(uspop.head(15))
print(uspop.shape)
```

```
observation_date  POPTHM
0        1959-01-01  175818
1        1959-02-01  176044
2        1959-03-01  176274
3        1959-04-01  176503
4        1959-05-01  176723
5        1959-06-01  176954
6        1959-07-01  177208
7        1959-08-01  177479
8        1959-09-01  177755
9        1959-10-01  178026
10       1959-11-01  178273
11       1959-12-01  178504
12       1960-01-01  178925
13       1960-02-01  179326
14       1960-03-01  179707
(799, 2)
```

We shall take the covariate variable as $x$ which takes the values $1, \dots, n$. Then we shall fit a linear function of $x$ to the observed time series $y$ using linear regression.

```python
y = uspop['POPTHM']
import numpy as np
x = np.arange(1, len(y)+1) #this is the covariate
import statsmodels.api as sm
X = sm.add_constant(x)
linmod = sm.OLS(y, X).fit()
print(linmod.summary())
print(linmod.params)
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                 POPTHM   R-squared:                       0.997
Model:                            OLS   Adj. R-squared:                  0.997
Method:                 Least Squares   F-statistic:                 2.740e+05
Date:                Fri, 05 Sep 2025   Prob (F-statistic):               0.00
Time:                        01:19:27   Log-Likelihood:                -7434.1
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
const    174459.566196
x1          213.684996
dtype: float64
```

The estimated slope parameter $\hat{\beta}_1$ is 213.684996. The interpretation of this is: the population grows by 213684.996 (note that unit of y is thousands) for every month.  The estimated intercept parameter $\hat{\beta}_0$ is $174459.566196$.This is an estimate of the population at time 0 which corresponds to December 1958. The standard errors provide estimates of the uncertainty in $\hat{\beta}_0$ and $\hat{\beta}_1$.

To see how well the regression line fits the data, we can plot the line over the original data, as follows.

```python
import matplotlib.pyplot as plt
plt.plot(y, label = "Observed Data")
plt.plot(linmod.fittedvalues, label = 'Fitted Values', color = 'red')
plt.xlabel('Time (months)')
plt.ylabel('Thousands')
plt.title('Population of the United States')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The fit is decent and the line gives a good idea of the overall population growth. However there are some time periods where the population growth diverges from the overall regression line.

The fitted regression line allows us to predict the US population at future time points. This is illustrated below. First note that the given dataset gives population numbers until July 2025:

```python
print(uspop.tail(15))
```

```
observation_date  POPTHM
784       2024-05-01  339927
785       2024-06-01  340213
786       2024-07-01  340448
787       2024-08-01  340637
788       2024-09-01  340825
789       2024-10-01  341002
790       2024-11-01  341169
791       2024-12-01  341320
792       2025-01-01  341454
793       2025-02-01  341588
794       2025-03-01  341729
795       2025-04-01  341874
796       2025-05-01  342032
797       2025-06-01  342197
798       2025-07-01  342370
```

The last (799th) observation corresponds to July 2025. Suppose we want to predict the population for August 2025. This corresponds to $x = 800$. The prediction is given by: $\hat{\beta}_0 + 800 \hat{\beta}_1$.

```python
predAug2025 = linmod.params.iloc[0] + 800*linmod.params.iloc[1]
print(predAug2025)
```

```
345407.5627146716
```

The predicted US population for January 2025 is therefore 345.40756 million (note the units of $y$ are thousands).

linmod supports a function which gives the prediction automatically and also gives uncertainty quantification for the prediction.

```python
print(linmod.get_prediction([1, 800]).summary_frame())
#use linmod.get_prediction([[1, 793], [1, 795]]).summary_frame() to get multiple predictions at x = 793 and x = 795
```

```
mean     mean_se  mean_ci_lower  mean_ci_upper   obs_ci_lower  \
0  345407.562715  188.487027   345037.57306  345777.552369  340170.212653

    obs_ci_upper
0  350644.912776
```

The get_prediction function gives two uncertainty intervals. The first is for the **mean** of the prediction, and the second is for the prediction itself. We shall see how these intervals are obtained in a later lecture/lab. The commonly used uncertainty interval is the second one, which in this case, is $[340170.212653, 350644.912776]$ thousands.

---

[Up: contents](index.md) · [Google Trends Dataset for the query Amazon →](02-google-trends-dataset-for-the-query-amazon.md)
