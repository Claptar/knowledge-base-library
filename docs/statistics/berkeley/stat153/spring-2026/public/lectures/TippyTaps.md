---
title: Stat153/248 - Lecture 7 and 8 Finger Tapping Exercise
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/TippyTaps.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/TippyTaps.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Stat153/248 - Lecture 7 and 8 Finger Tapping Exercise

**Source:** [`public/lectures/TippyTaps.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/TippyTaps.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

# Stat153/248 - Lecture 7 and 8 Finger Tapping Exercise

This is the (in progress) notebook from our exercise in class. We will continue with this during Lecture 8.

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib import pyplot as plt
import glob
import os
```

```python
data_dir = '/Users/liberty/Documents/Berkeley/Teaching/Stat153_data/Finger_Tap/'
csv_files = glob.glob(f'{data_dir}/*.csv')
```

```python
import seaborn as sns
```

```python
sns.lineplot(x='tap_index', y='t_seconds', hue='finger', data=df_all)
```

```
<Axes: xlabel='tap_index', ylabel='t_seconds'>
```

*(1 figure omitted — see the original notebook.)*

```python
sns.violinplot(data=df_all, x='dominant_hand', y='dt_seconds', hue='finger')
#plt.gca().set_ylim([0, 0.4])
```

```
<Axes: xlabel='dominant_hand', ylabel='dt_seconds'>
```

*(1 figure omitted — see the original notebook.)*

```python
summary_df
```

```
subj   hand finger handedness  dominant_hand  ntaps
0       0   left  index       left           True    330
1       1  right  pinky      right           True    371
2       2   left  pinky      right          False    296
3       3   left  index      right          False    308
4       4  right  index       left          False    301
..    ...    ...    ...        ...            ...    ...
96     96   left  pinky      right          False    314
97     97   left  index       left           True    355
98     98   left  index      right          False    305
99     99  right  index      right           True    387
100   100  right  index      right           True    347

[101 rows x 6 columns]
```

```python
import statsmodels.api as sm

df2 = pd.get_dummies(summary_df, columns = ['finger', 'hand'], drop_first=True)
```

```python
df2
```

```
subj handedness  dominant_hand  ntaps  finger_pinky  hand_right
0       0       left           True    330         False       False
1       1      right           True    371          True        True
2       2      right          False    296          True       False
3       3      right          False    308         False       False
4       4       left          False    301         False        True
..    ...        ...            ...    ...           ...         ...
96     96      right          False    314          True       False
97     97       left           True    355         False       False
98     98      right          False    305         False       False
99     99      right           True    387         False        True
100   100      right           True    347         False        True

[101 rows x 6 columns]
```

```python
y = df2['ntaps']
X = df2[['finger_pinky', 'dominant_hand']]
X = sm.add_constant(X)
X = X.astype(float)
print(X)
```

```
const  finger_pinky  dominant_hand
0      1.0           0.0            1.0
1      1.0           1.0            1.0
2      1.0           1.0            0.0
3      1.0           0.0            0.0
4      1.0           0.0            0.0
..     ...           ...            ...
96     1.0           1.0            0.0
97     1.0           0.0            1.0
98     1.0           0.0            0.0
99     1.0           0.0            1.0
100    1.0           0.0            1.0

[101 rows x 3 columns]
```

```python
print(y)
```

```
0      330
1      371
2      296
3      308
4      301
      ...
96     314
97     355
98     305
99     387
100    347
Name: ntaps, Length: 101, dtype: int64
```

```python
model = sm.OLS(y, X).fit()
print(model.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                  ntaps   R-squared:                       0.262
Model:                            OLS   Adj. R-squared:                  0.247
Method:                 Least Squares   F-statistic:                     17.38
Date:                Thu, 12 Feb 2026   Prob (F-statistic):           3.47e-07
Time:                        08:41:34   Log-Likelihood:                -531.87
No. Observations:                 101   AIC:                             1070.
Df Residuals:                      98   BIC:                             1078.
Df Model:                           2
Covariance Type:            nonrobust
=================================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------
const           323.5174      8.624     37.515      0.000     306.404     340.631
finger_pinky    -28.2498      9.549     -2.958      0.004     -47.200      -9.300
dominant_hand    46.7067      9.599      4.866      0.000      27.658      65.755
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
XTX_inv=np.linalg.inv(np.dot(X.T, X))
betas=np.dot(np.dot(XTX_inv, X.T), y)
print(betas)
```

```
[323.51735505 -28.24982225  46.70670933]
```

```python
X.shape
```

```
(101, 3)
```

```python
import statsmodels.formula.api as smf
```

```python
model = smf.ols(formula="ntaps~ C(dominant_hand) + C(finger)", data=summary_df).fit()
```

```python
print(model.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                  ntaps   R-squared:                       0.262
Model:                            OLS   Adj. R-squared:                  0.247
Method:                 Least Squares   F-statistic:                     17.38
Date:                Thu, 12 Feb 2026   Prob (F-statistic):           3.47e-07
Time:                        08:52:19   Log-Likelihood:                -531.87
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
model = smf.ols(formula = "ntaps ~ C(dominant_hand)", data=summary_df).fit()
print(model.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                  ntaps   R-squared:                       0.196
Model:                            OLS   Adj. R-squared:                  0.188
Method:                 Least Squares   F-statistic:                     24.12
Date:                Thu, 12 Feb 2026   Prob (F-statistic):           3.58e-06
Time:                        08:55:18   Log-Likelihood:                -536.19
No. Observations:                 101   AIC:                             1076.
Df Residuals:                      99   BIC:                             1082.
Df Model:                           1
Covariance Type:            nonrobust
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
Intercept                  309.7209      7.533     41.118      0.000     294.775     324.667
C(dominant_hand)[T.True]    48.8136      9.940      4.911      0.000      29.090      68.537
==============================================================================
Omnibus:                        3.904   Durbin-Watson:                   1.960
Prob(Omnibus):                  0.142   Jarque-Bera (JB):                4.421
Skew:                           0.114   Prob(JB):                        0.110
Kurtosis:                       3.999   Cond. No.                         2.83
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
model = smf.ols(formula = "ntaps ~ C(hand)+C(finger)", data=summary_df).fit()
print(model.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                  ntaps   R-squared:                       0.306
Model:                            OLS   Adj. R-squared:                  0.292
Method:                 Least Squares   F-statistic:                     21.58
Date:                Thu, 12 Feb 2026   Prob (F-statistic):           1.71e-08
Time:                        08:56:55   Log-Likelihood:                -528.77
No. Observations:                 101   AIC:                             1064.
Df Residuals:                      98   BIC:                             1071.
Df Model:                           2
Covariance Type:            nonrobust
======================================================================================
                         coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------
Intercept            322.2382      8.123     39.669      0.000     306.118     338.358
C(hand)[T.right]      51.8645      9.258      5.602      0.000      33.492      70.237
C(finger)[T.pinky]   -30.8740      9.236     -3.343      0.001     -49.203     -12.545
==============================================================================
Omnibus:                        5.051   Durbin-Watson:                   1.844
Prob(Omnibus):                  0.080   Jarque-Bera (JB):                6.712
Skew:                           0.133   Prob(JB):                       0.0349
Kurtosis:                       4.234   Cond. No.                         3.27
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
sns.countplot(x='hand', data=summary_df, hue='dominant_hand')
```

```
<Axes: xlabel='hand', ylabel='count'>
```

*(1 figure omitted — see the original notebook.)*

```python
google_form = pd.read_csv('/Users/liberty/Documents/Berkeley/Teaching/Stat153_data/fingertaps_summary.csv')
```

```python
google_form['How many finger taps did you complete in 60 seconds?']
```

```
0     338
1     398
2     364
3     409
4     304
     ...
60    360
61    271
62    425
63    328
64    424
Name: How many finger taps did you complete in 60 seconds?, Length: 65, dtype: int64
```

```python
google_form = google_form.rename(columns=lambda c: "ntaps" if "How many finger taps" in c else c)
google_form = google_form.rename(columns=lambda c: "sleep_hrs" if "How much sleep" in c else c)
google_form = google_form.rename(columns=lambda c: "handedness" if "Are you left handed" in c else c)
google_form = google_form.rename(columns=lambda c: "finger" if "Which finger" in c else c)
google_form = google_form.rename(columns=lambda c: "hand" if "Which hand" in c else c)
google_form = google_form.rename(columns=lambda c: "gamer" if "play video games" in c else c)
google_form = google_form.rename(columns=lambda c: "sport" if "sport" in c else c)

google_form['dominant_hand'] = google_form['handedness'] == google_form['hand']

google_form
```

```
Timestamp  ntaps handedness finger   hand gamer  sleep_hrs  sport  \
0   2/10/26 9:04    338      Right  Pinky   Left    No       7.00      0
1   2/10/26 9:04    398      Right  Index  Right    No       6.00      8
2   2/10/26 9:04    364      Right  Index  Right    No       5.00      0
3   2/10/26 9:04    409      Right  Pinky  Right   Yes       4.00      7
4   2/10/26 9:04    304      Right  Index   Left    No       5.83      2
..           ...    ...        ...    ...    ...   ...        ...    ...
60  2/10/26 9:05    360      Right  Index  Right    No       6.00      5
61  2/10/26 9:05    271       Left  Pinky  Right    No       6.00      4
62  2/10/26 9:05    425      Right  Index  Right    No       8.00      4
63  2/10/26 9:06    328      Right  Index   Left    No       8.50      7
64  2/10/26 9:06    424      Right  Pinky  Right    No       8.00      4

    dominant_hand
0           False
1            True
2            True
3            True
4           False
..            ...
60           True
61          False
62           True
63          False
64           True

[65 rows x 9 columns]
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                  ntaps   R-squared:                       0.326
Model:                            OLS   Adj. R-squared:                  0.293
Method:                 Least Squares   F-statistic:                     9.826
Date:                Thu, 12 Feb 2026   Prob (F-statistic):           2.23e-05
Time:                        09:06:11   Log-Likelihood:                -348.16
No. Observations:                  65   AIC:                             704.3
Df Residuals:                      61   BIC:                             713.0
Df Model:                           3
Covariance Type:            nonrobust
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
Intercept                  394.3168     43.678      9.028      0.000     306.977     481.657
C(finger)[T.Pinky]         -38.0001     13.444     -2.826      0.006     -64.884     -11.117
C(dominant_hand)[T.True]    51.1944     13.676      3.743      0.000      23.848      78.541
sleep_hrs                   -9.4037      6.196     -1.518      0.134     -21.794       2.987
==============================================================================
Omnibus:                        3.462   Durbin-Watson:                   1.776
Prob(Omnibus):                  0.177   Jarque-Bera (JB):                2.638
Skew:                           0.462   Prob(JB):                        0.267
Kurtosis:                       3.349   Cond. No.                         45.8
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

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
Time:                        09:07:59   Log-Likelihood:                -348.99
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
Time:                        09:10:22   Log-Likelihood:                -345.21
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
df_all
```

```
tap_index  t_seconds  dt_seconds  subj finger   hand handedness  \
0              1      0.000       0.000     0  index   left       left
1              2      0.149       0.149     0  index   left       left
2              3      0.316       0.167     0  index   left       left
3              4      0.483       0.167     0  index   left       left
4              5      0.634       0.151     0  index   left       left
...          ...        ...         ...   ...    ...    ...        ...
34108        343     58.878       0.188   100  index  right      right
34109        344     59.058       0.180   100  index  right      right
34110        345     59.229       0.171   100  index  right      right
34111        346     59.411       0.182   100  index  right      right
34112        347     59.591       0.180   100  index  right      right

       dominant_hand
0               True
1               True
2               True
3               True
4               True
...              ...
34108           True
34109           True
34110           True
34111           True
34112           True

[34113 rows x 8 columns]
```

```python
bin_size = 10 # in seconds
df_all['time_bin'] = (df_all['t_seconds'] // bin_size).astype(int)
df_all

df_bins = ( df_all.groupby(['subj', 'handedness', 'finger','hand','dominant_hand', 'time_bin'])
            .size()
            .reset_index(name='taps_bin')
          )
df_bins
```

```
subj handedness finger   hand  dominant_hand  time_bin  taps_bin
0       0       left  index   left           True         0        66
1       0       left  index   left           True         1        54
2       0       left  index   left           True         2        52
3       0       left  index   left           True         3        55
4       0       left  index   left           True         4        50
..    ...        ...    ...    ...            ...       ...       ...
598   100      right  index  right           True         1        60
599   100      right  index  right           True         2        57
600   100      right  index  right           True         3        57
601   100      right  index  right           True         4        56
602   100      right  index  right           True         5        55

[603 rows x 7 columns]
```

```python
df_bins.to_csv('/Users/liberty/Documents/Berkeley/Teaching/Stat153_data/df_bins.csv')
```

```python
sns.lineplot(x='time_bin', y='taps_bin', data=df_bins)
```

```
<Axes: xlabel='time_bin', ylabel='taps_bin'>
```

*(1 figure omitted — see the original notebook.)*

```python
sns.lineplot(x='time_bin', y='taps_bin', hue='hand', data=df_bins)
```

```
<Axes: xlabel='time_bin', ylabel='taps_bin'>
```

*(1 figure omitted — see the original notebook.)*

```python
sns.lineplot(x='time_bin', y='taps_bin', hue='finger', data=df_bins)
```

```
<Axes: xlabel='time_bin', ylabel='taps_bin'>
```

*(1 figure omitted — see the original notebook.)*

```python
model=smf.ols('taps_bin ~ time_bin', data=df_bins).fit()
print(model.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:               taps_bin   R-squared:                       0.062
Model:                            OLS   Adj. R-squared:                  0.061
Method:                 Least Squares   F-statistic:                     39.96
Date:                Thu, 12 Feb 2026   Prob (F-statistic):           5.06e-10
Time:                        09:27:53   Log-Likelihood:                -2264.1
No. Observations:                 603   AIC:                             4532.
Df Residuals:                     601   BIC:                             4541.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     60.4624      0.746     81.047      0.000      58.997      61.927
time_bin      -1.5608      0.247     -6.321      0.000      -2.046      -1.076
==============================================================================
Omnibus:                       38.053   Durbin-Watson:                   0.665
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               51.912
Skew:                           0.520   Prob(JB):                     5.34e-12
Kurtosis:                       3.991   Cond. No.                         5.76
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

```python
model = smf.ols('taps_bin ~ time_bin*C(finger) + C(dominant_hand)', data=df_bins).fit()
print(model.summary())
```

```
OLS Regression Results
==============================================================================
Dep. Variable:               taps_bin   R-squared:                       0.282
Model:                            OLS   Adj. R-squared:                  0.278
Method:                 Least Squares   F-statistic:                     58.82
Date:                Thu, 12 Feb 2026   Prob (F-statistic):           7.05e-42
Time:                        09:30:12   Log-Likelihood:                -2183.5
No. Observations:                 603   AIC:                             4377.
Df Residuals:                     598   BIC:                             4399.
Df Model:                           4
Covariance Type:            nonrobust
===============================================================================================
                                  coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------------------
Intercept                      58.5275      0.990     59.112      0.000      56.583      60.472
C(finger)[T.pinky]             -6.3238      1.317     -4.800      0.000      -8.911      -3.736
C(dominant_hand)[T.True]        8.2628      0.749     11.027      0.000       6.791       9.734
time_bin                       -1.7458      0.291     -5.991      0.000      -2.318      -1.173
time_bin:C(finger)[T.pinky]     0.4467      0.435      1.026      0.305      -0.409       1.302
==============================================================================
Omnibus:                       65.282   Durbin-Watson:                   0.739
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              144.550
Skew:                           0.608   Prob(JB):                     4.09e-32
Kurtosis:                       5.067   Cond. No.                         14.9
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

---

[Up: contents](../../index.md)
