---
title: Fitting regression models
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab4_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab4_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Fitting regression models

Now we're going to fit some simple linear regression models with OLS. This is not necessarily the best choice for these data, but more on that later. For now, we're interested in whether the number of taps that someone makes can be modeled as a function of whether they used their dominant hand and which finger they used:

$\text{ntaps} = \beta_0 + \beta_1 (\text{dominant hand}) + \beta_2 (\text{pinky finger})$

As we saw in class, we could use dummy coded variables to assign Left/Right and Pinky/Index to new columns of zeros and ones, but we can also use the statsmodels formulas to make this a little more intuitive, as follows:

```python
import statsmodels.formula.api as smf
```

```python
model = smf.ols(formula="ntaps~ C(dominant_hand) + C(finger)", data=summary_df).fit()
print(model.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                  ntaps   R-squared:                       0.262
Model:                            OLS   Adj. R-squared:                  0.247
Method:                 Least Squares   F-statistic:                     17.38
Date:                Thu, 12 Feb 2026   Prob (F-statistic):           3.47e-07
Time:                        15:23:19   Log-Likelihood:                -531.87
No. Observations:                 101   AIC:                             1070.
Df Residuals:                      98   BIC:                             1078.
Df Model:                           2
Covariance Type:            nonrobust
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
Intercept                  323.5174      8.624     37.515      0.000     306.404     340.631
C(dominant_hand)[T.True]    46.7067      9.599      4.866      0.000      27.658      65.755
C(finger)[T.pinky]         -28.2498      9.549     -2.958      0.004     -47.200      -9.300
==============================================================================
Omnibus:                        6.839   Durbin-Watson:                   1.930
Prob(Omnibus):                  0.033   Jarque-Bera (JB):                7.578
Skew:                           0.395   Prob(JB):                       0.0226
Kurtosis:                       4.085   Cond. No.                         3.38
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
# What if we just wanted to fit whether taps depend only on using dominant hand? Note
# the difference in Adj. R-squared compared to the last example.

# FILL IN
```

## Plots to look at balance within our data

Are we sampling evenly across handedness? Around 10-12% of the world's population is left-handed, so we should expect that to be roughly the case for the data we get here. Let's see if that pans out.

```python
sns.countplot(x='handedness', data=summary_df)
```

```
<Axes: xlabel='handedness', ylabel='count'>
```

*(1 figure omitted — see the original notebook.)*

We do indeed have an imbalance in the data, with many more right-handed people than left-handed people. If we ran a regression just looking at whether using your right hand helps, it would show that there is a strong positive effect, but this is drive by the fact that we are mostly running this on right-handed people! So remember to think about how to interpret your coefficients in the context of your actual data.

Let's also just plot which hand the person used to do the task, and whether it was their dominant hand:

```python
sns.countplot(x='hand', data=summary_df, hue='dominant_hand')
```

```
<Axes: xlabel='hand', ylabel='count'>
```

*(1 figure omitted — see the original notebook.)*

---

← Using seaborn to explore our dataset · [Up: contents](index.md) · Google form data →
