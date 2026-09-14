---
title: US Population Dataset
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThree153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureThree153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# US Population Dataset

**Source:** [`CodeLectureThree153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThree153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

This dataset is downloaded from FRED and gives monthly population of the United States in thousands.

```python
import pandas as pd
uspop = pd.read_csv('POPTHM-Jan2025FRED.csv')
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
(791, 2)
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
Method:                 Least Squares   F-statistic:                 2.422e+05
Date:                Tue, 28 Jan 2025   Prob (F-statistic):               0.00
Time:                        19:52:45   Log-Likelihood:                -7394.9
No. Observations:                 791   AIC:                         1.479e+04
Df Residuals:                     789   BIC:                         1.480e+04
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       1.746e+05    198.060    881.427      0.000    1.74e+05    1.75e+05
x1           213.2353      0.433    492.142      0.000     212.385     214.086
==============================================================================
Omnibus:                      409.683   Durbin-Watson:                   0.000
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               73.601
Skew:                          -0.479   Prob(JB):                     1.04e-16
Kurtosis:                       1.853   Cond. No.                         915.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
const    174575.148609
x1          213.235255
dtype: float64
```

The estimated slope parameter $\hat{\beta}_1$ is 213.2353. The interpretation of this is: the population grows by 213235.255 (note that unit of y is thousands) for every month.  The estimated slope parameter is $\hat{\beta}_0$ is $174575.148$.This is an estimate of the population at time 0 which corresponds to December 1958. The standard errors provide estimates of the uncertainty in $\hat{\beta}_0$ and $\hat{\beta}_1$.

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

The fitted regression line allows us to predict the US population at future time points. This is illustrated below. First note that the given dataset gives population numbers until November 2024:

```python
print(uspop.tail(15))
```

```
observation_date  POPTHM
776       2023-09-01  335612
777       2023-10-01  335773
778       2023-11-01  335925
779       2023-12-01  336070
780       2024-01-01  336194
781       2024-02-01  336306
782       2024-03-01  336423
783       2024-04-01  336550
784       2024-05-01  336687
785       2024-06-01  336839
786       2024-07-01  337005
787       2024-08-01  337185
788       2024-09-01  337362
789       2024-10-01  337521
790       2024-11-01  337669
```

The last (791th) observation corresponds to November 2024. Suppose we want to predict the population for January 2025. This corresponds to $x = 793$. The prediction is given by: $\hat{\beta}_0 + 793 \hat{\beta}_1$.

```python
predJan2025 = linmod.params.iloc[0] + 793*linmod.params.iloc[1]
print(predJan2025)
```

```
343670.70611584
```

The predicted US population for January 2025 is therefore 343670.7 million (note the units of $y$ are thousands).

linmod supports a function which gives the prediction automatically and also gives uncertainty quantification for the prediction.

```python
print(linmod.get_prediction([1, 793]).summary_frame())
#use linmod.get_prediction([[1, 793], [1, 795]]).summary_frame() to get multiple predictions at x = 793 and x = 795
```

```
mean     mean_se  mean_ci_lower  mean_ci_upper  obs_ci_lower  \
0  343670.706116  198.435157  343281.182823  344060.229409  338194.76474

    obs_ci_upper
0  349146.647492
```

The get_prediction function gives two uncertainty intervals. The first is for the **mean** of the prediction, and the second is for the prediction itself. We shall see how these predictions are obtained later. The commonly used uncertainty interval is the second one, which in this case, is $[338194.76474, 349146.647492]$.

---

[Up: contents](index.md) · [Google Trends Dataset for the query Amazon →](02-google-trends-dataset-for-the-query-amazon.md)
