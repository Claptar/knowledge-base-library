---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Linear Regression Models fit to the US population data
---

The first topic in this course is "Multiple Linear Regression" for time series. Linear regression can be used in many ways for time series analysis, with basic applications in trend estimation and prediction/forecasting. We shall illustrate this today through the US population data.

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
```

## US Population Dataset

This dataset is downloaded from FRED and gives monthly population of the United States in thousands.

```python
uspop = pd.read_csv('POPTHM_27Aug2026.csv')
print(uspop.head(10))
print(uspop.tail(10))
```

```
observation_date  POPTHM
0       1959-01-01  175818
1       1959-02-01  176044
2       1959-03-01  176274
3       1959-04-01  176503
4       1959-05-01  176723
5       1959-06-01  176954
6       1959-07-01  177208
7       1959-08-01  177479
8       1959-09-01  177755
9       1959-10-01  178026
    observation_date  POPTHM
801       2025-10-01  342366
802       2025-11-01  342439
803       2025-12-01  342495
804       2026-01-01  342540
805       2026-02-01  342581
806       2026-03-01  342627
807       2026-04-01  342680
808       2026-05-01  342746
809       2026-06-01  342822
810       2026-07-01  342909
```

Let us set the index of each row to be the corresponding month, so the plots are easier to interpret.

```python
uspop['observation_date'] = pd.to_datetime(uspop['observation_date'])
uspop.set_index('observation_date', inplace = True)
print(uspop)
```

```
POPTHM
observation_date
1959-01-01        175818
1959-02-01        176044
1959-03-01        176274
1959-04-01        176503
1959-05-01        176723
...                  ...
2026-03-01        342627
2026-04-01        342680
2026-05-01        342746
2026-06-01        342822
2026-07-01        342909

[811 rows x 1 columns]
```

Here is a plot of the dataset.

```python
plt.figure(figsize=(6, 4))
plt.plot(uspop['POPTHM'], label = "population")
plt.xlabel("Time (monthly)")
plt.ylabel("Population (thousands)")
plt.title("Population of the United States")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Based on this dataset, suppose we want to answer the following prediction (or forecasting) question: what would be the population of the United States in July 2040? The last month in the observed data is July 2026 (i.e., month $n$ corresponds to July 2026), so July 2040 would be month $n + 14*12 = n + 168$.

Let us attempt to answer this question by fitting simple models based on linear regression to the observed data. Before fitting models, let us first note some available answers to this question. There are population projections available from the Census Bureau, as well as from the United Nations. The Census Bureau projection for the US population in July 2040 is 355.309 million. The UN projection is 370.209 million.

Let $y_t$ denote the population of the United States for month $t$. The first model is simply: $y_t = \beta_0 + \beta_1 t + \epsilon_t$. This is just linear regression with time $t$ as the covariate.

### Model 1: $y_t = \beta_0 + \beta_1 t + \epsilon_t$

Parameter interpretation: $\beta_0$: population at time 0 (note that the data starts from January 1959 so time 0 refers to December 1958) and $\beta_1$: change in population for each additional month.

We fit this model to the data using the following code.

```python
#Model 1: y_t = beta_0 + beta_1 t + \epsilon_t
#y_t is the population at time t
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
Date:                Tue, 01 Sep 2026   Prob (F-statistic):               0.00
Time:                        19:06:34   Log-Likelihood:                -7554.3
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

The output above consists of many different things. We shall see how some of these numbers are calculated in the next couple of lectures. The main output is the estimates of $\beta_0$ and $\beta_1$ (these are given by the 'coef' column above).

```python
print(md1.params)
```

```
const    174585.548486
x1          213.215735
dtype: float64
```

After fitting a model, it is a good idea to look at the plot of the data along with the 'fitted values' and also the 'residuals'. Fitted values are defined by:
\begin{align*}
   \hat{\beta}_0 + \hat{\beta}_1 t
\end{align*}
for $t = 1, \dots, n$.

Residuals are defined by:
\begin{align*}
   y_t - \hat{\beta}_0 - \hat{\beta}_1 t.
\end{align*}
Residuals represent the part of the data that is not explained by the model equation.

```python
#Plotting data along with residuals
plt.figure(figsize=(6, 4))
plt.plot(y, label = "population")
plt.plot(md1.fittedvalues, label = "fitted values")
plt.xlabel("Time (monthly)")
plt.ylabel("Population (thousands)")
plt.title("Population of the United States with fitted values")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The fitted values plot suggests that the line is explaining the data well. Note though that the $y$-axis goes from 175K to 350K which covers a wide range, so even small changes in this plot can indicate big numerical departures.

```python
#Plotting residuals:
plt.figure(figsize=(6, 4))
plt.plot(md1.resid, label = "residuals")
plt.xlabel("Time (monthly)")
plt.ylabel("Residuals")
plt.title("Residuals of the OLS Model")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

All the recent residuals are negative which means that the fitted line takes higher values compared to the actual observations. From here, we can perhaps guess that future predictions will also be on the larger side.

There is a lot of structure in the residuals which indicates that more modeling on the residuals is necessary.

Here is how this fitted model can be used to predict the population in July 2040.

```python
#Prediction for time t = n + 168 (July 2040):
n = len(y)
i = n+168
prediction = md1.get_prediction([1, i])
print("Mean prediction for July 2040:", prediction.predicted_mean)
```

```
Mean prediction for July 2040: [383323.7529835]
```

We are getting a prediction of 383.323 million which is quite a bit higher than the Census Bureau as well as the UN predictions. Below we plot the predictions along with the original dataset.

```python

---

[Up: contents](index.md) · [Predict the next 168 monthly observations →](02-predict-the-next-168-monthly-observations.md)
