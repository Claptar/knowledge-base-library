---
title: Investigate other model effects
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab4_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Investigate other model effects

**Source:** [`public/labs/Lab4_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Effect of playing sports and being a gamer are shown below:

```python
model = smf.ols(formula = "ntaps ~ C(finger) + C(dominant_hand) + sport", data=google_form).fit()
print(model.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                  ntaps   R-squared:                       0.308
Model:                            OLS   Adj. R-squared:                  0.274
Method:                 Least Squares   F-statistic:                     9.064
Date:                Thu, 12 Feb 2026   Prob (F-statistic):           4.75e-05
Time:                        15:23:19   Log-Likelihood:                -348.99
No. Observations:                  65   AIC:                             706.0
Df Residuals:                      61   BIC:                             714.7
Df Model:                           3
Covariance Type:            nonrobust
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
Intercept                  325.4028     14.726     22.098      0.000     295.957     354.849
C(finger)[T.Pinky]         -35.4348     13.660     -2.594      0.012     -62.749      -8.120
C(dominant_hand)[T.True]    51.0389     13.933      3.663      0.001      23.179      78.899
sport                        1.1967      1.428      0.838      0.405      -1.660       4.053
==============================================================================
Omnibus:                        2.871   Durbin-Watson:                   1.779
Prob(Omnibus):                  0.238   Jarque-Bera (JB):                2.078
Skew:                           0.283   Prob(JB):                        0.354
Kurtosis:                       3.669   Cond. No.                         20.4
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
model = smf.ols(formula = "ntaps ~ C(finger) + C(dominant_hand) + C(gamer)", data=google_form).fit()
print(model.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                  ntaps   R-squared:                       0.384
Model:                            OLS   Adj. R-squared:                  0.354
Method:                 Least Squares   F-statistic:                     12.69
Date:                Thu, 12 Feb 2026   Prob (F-statistic):           1.51e-06
Time:                        15:23:19   Log-Likelihood:                -345.21
No. Observations:                  65   AIC:                             698.4
Df Residuals:                      61   BIC:                             707.1
Df Model:                           3
Covariance Type:            nonrobust
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
Intercept                  326.3398     12.480     26.148      0.000     301.384     351.296
C(finger)[T.Pinky]         -36.3306     12.819     -2.834      0.006     -61.964     -10.697
C(dominant_hand)[T.True]    49.5358     13.084      3.786      0.000      23.372      75.699
C(gamer)[T.Yes]             58.5620     20.311      2.883      0.005      17.949      99.175
==============================================================================
Omnibus:                        1.340   Durbin-Watson:                   1.818
Prob(Omnibus):                  0.512   Jarque-Bera (JB):                0.691
Skew:                           0.163   Prob(JB):                        0.708
Kurtosis:                       3.386   Cond. No.                         4.20
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
sns.boxplot(x='dominant_hand', y='ntaps', hue='gamer', data=google_form)
```

```
<Axes: xlabel='dominant_hand', ylabel='ntaps'>
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← Google form data](24-google-form-data.md) · [Up: contents](index.md) · [can you make a boxplot showing whether using your pinky vs your index finger →](26-can-you-make-a-boxplot-showing-whether-using-your-pinky-vs-y.md)
