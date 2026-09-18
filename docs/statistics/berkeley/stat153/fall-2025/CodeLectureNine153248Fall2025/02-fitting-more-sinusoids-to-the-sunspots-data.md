---
title: Fitting more sinusoids to the sunspots data
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureNine153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureNine153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureNine153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureNine153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Fitting more sinusoids to the sunspots data

We now consider the model with two sinusoids:
\begin{equation*}
  y_t = \beta_0 + \beta_1 \cos(2 \pi f_1 t) + \beta_2 \sin(2 \pi f_1 t) + \beta_3 \cos(2 \pi f_2 t) + \beta_4 \sin(2 \pi f_2 t) + \epsilon_t
\end{equation*}
with both $f_1$ and $f_2$ denoting unknown parameters (along with $\beta_0, \beta_1, \beta_2, \beta_3, \beta_4$ and $\sigma$).

Before fitting this model to the data, let us first compute the fitted values for the best single sinusoidal model (that we fit above).

```python
n = len(y)
f = f_est
x = np.arange(1, n+1)
X = np.column_stack([np.ones(n)])
x = np.arange(1, n+1)
if np.isscalar(f):
    f = [f]
for j in range(len(f)):
    f1 = f[j]
    xcos = np.cos(2 * np.pi * f1 * x)
    xsin = np.sin(2 * np.pi * f1 * x)
    X = np.column_stack([X, xcos, xsin])

md_1 = sm.OLS(y, X).fit()
print(md_1.summary())
best_rss_1 = np.sum(md_1.resid ** 2)
print(best_rss_1)

plt.figure(figsize = (10, 6))
#plt.plot(y, linestyle = '', marker = '')
plt.plot(y)
#plt.plot(md1.fittedvalues, color = 'red', marker = '', linestyle = '')
#plt.plot(md2.fittedvalues, color = 'black', marker = '', linestyle = '')
plt.plot(md_1.fittedvalues, color = 'red')
plt.show()
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.304
Model:                            OLS   Adj. R-squared:                  0.300
Method:                 Least Squares   F-statistic:                     70.27
Date:                Thu, 25 Sep 2025   Prob (F-statistic):           4.74e-26
Time:                        16:22:56   Log-Likelihood:                -1742.9
No. Observations:                 325   AIC:                             3492.
Df Residuals:                     322   BIC:                             3503.
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         78.8755      2.877     27.414      0.000      73.215      84.536
x1           -38.5951      4.066     -9.491      0.000     -46.595     -30.595
x2           -28.8721      4.071     -7.092      0.000     -36.881     -20.863
==============================================================================
Omnibus:                       55.801   Durbin-Watson:                   0.383
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               91.576
Skew:                           0.999   Prob(JB):                     1.30e-20
Kurtosis:                       4.664   Cond. No.                         1.42
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
866098.0246370969
```

*(1 figure omitted — see the original notebook.)*

Below we write a function for calculating RSS with multiple frequencies.

```python
def rss(f):
    n = len(y)
    X = np.column_stack([np.ones(n)])
    x = np.arange(1, n+1)
    if np.isscalar(f):
        f = [f]
    for j in range(len(f)):
        f1 = f[j]
        xcos = np.cos(2 * np.pi * f1 * x)
        xsin = np.sin(2 * np.pi * f1 * x)
        X = np.column_stack([X, xcos, xsin])
    md = sm.OLS(y, X).fit()
    ans = np.sum(md.resid ** 2)
    return ans
```

In the code below, we search over two frequencies $f_1$ and $f_2$ which best fit to the data. For the range of frequencies, we restrict to the range $(0, 0.15)$. This is because it seems unlikely that sinusoids with frequencies larger than 0.15 will fit well to the data.

```python
f1_gr = np.linspace(0, 0.15, 1000)
f2_gr = np.linspace(0, 0.15, 1000)
# mesh on the 3 axes; 'ij' preserves axis ordering
X, Y = np.meshgrid(f1_gr, f2_gr, indexing='ij')
# keep only nondecreasing triples to kill permutations:
mask = (X <= Y)
xf, yf = X[mask], Y[mask]
def _rss3(x, y):
    return rss([float(x), float(y)])
rss_vec = np.vectorize(_rss3)
rss_vals = rss_vec(xf, yf)
g = pd.DataFrame({'x': xf, 'y': yf, 'rss': rss_vals})
```

```python
min_row = g.loc[g['rss'].idxmin()]
print(min_row)
f_opt_2 = np.array([min_row['x'], min_row['y']])
print(f_opt_2)
print(1/f_opt_2)
```

```
x           0.090691
y           0.099850
rss    702139.356644
Name: 421955, dtype: float64
[0.09069069 0.09984985]
[11.02649007 10.01503759]
```

Below we plot the fitted function with the two best frequencies obtained as above.

```python
n = len(y)
f = f_opt_2 #f_opt was obtained from the grid minimization
x = np.arange(1, n+1)
X = np.column_stack([np.ones(n)])
x = np.arange(1, n+1)
if np.isscalar(f):
    f = [f]
for j in range(len(f)):
    f1 = f[j]
    xcos = np.cos(2 * np.pi * f1 * x)
    xsin = np.sin(2 * np.pi * f1 * x)
    X = np.column_stack([X, xcos, xsin])

md_2 = sm.OLS(y, X).fit()
print(md_2.summary())
best_rss_2 = np.sum(md_2.resid ** 2)
print(best_rss_2)


plt.figure(figsize = (10, 6))
#plt.plot(y, linestyle = '', marker = '')
plt.plot(y)
#plt.plot(md_1.fittedvalues, color = 'black')
#plt.plot(md2.fittedvalues, color = 'black', marker = '', linestyle = '')
plt.plot(md_2.fittedvalues, color = 'red')
plt.show()
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.436
Model:                            OLS   Adj. R-squared:                  0.429
Method:                 Least Squares   F-statistic:                     61.75
Date:                Thu, 25 Sep 2025   Prob (F-statistic):           1.26e-38
Time:                        16:28:55   Log-Likelihood:                -1708.8
No. Observations:                 325   AIC:                             3428.
Df Residuals:                     320   BIC:                             3447.
Df Model:                           4
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         79.0015      2.599     30.398      0.000      73.888      84.115
x1           -43.8394      3.676    -11.925      0.000     -51.072     -36.607
x2           -18.6771      3.674     -5.084      0.000     -25.905     -11.450
x3            30.9542      3.678      8.417      0.000      23.719      38.189
x4            -9.3010      3.672     -2.533      0.012     -16.526      -2.076
==============================================================================
Omnibus:                       32.983   Durbin-Watson:                   0.383
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               45.724
Skew:                           0.699   Prob(JB):                     1.18e-10
Kurtosis:                       4.192   Cond. No.                         1.42
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
702139.3566439697
```

*(1 figure omitted — see the original notebook.)*

Next we try to find the three best frequencies, again using a grid minimization strategy.

```python
f1_gr = np.linspace(0, 0.15, 200)
f2_gr = np.linspace(0, 0.15, 200)
f3_gr = np.linspace(0, 0.15, 200)
# mesh on the 3 axes; 'ij' preserves axis ordering
X, Y, Z = np.meshgrid(f1_gr, f2_gr, f3_gr, indexing='ij')
# keep only nondecreasing triples to kill permutations:
mask = (X <= Y) & (Y <= Z)
xf, yf, zf = X[mask], Y[mask], Z[mask]
def _rss3(x, y, z):
    return rss([float(x), float(y), float(z)])
rss_vec = np.vectorize(_rss3)
rss_vals = rss_vec(xf, yf, zf)
g = pd.DataFrame({'x': xf, 'y': yf, 'z': zf, 'rss': rss_vals})
```

```python
min_row = g.loc[g['rss'].idxmin()]
print(min_row)
f_opt_3 = np.array([min_row['x'], min_row['y'], min_row['z']])
print(f_opt_3)
print(1/f_opt_3)
```

```
x           0.091206
y           0.093467
z           0.100251
rss    580238.083040
Name: 1268323, dtype: float64
[0.09120603 0.09346734 0.10025126]
[10.96418733 10.69892473  9.97493734]
```

Next we plot the fitted function using the three best frequencies.

```python
n = len(y)
f = f_opt_3 #f_opt was obtained from the grid minimization
x = np.arange(1, n+1)
X = np.column_stack([np.ones(n)])
x = np.arange(1, n+1)
if np.isscalar(f):
    f = [f]
for j in range(len(f)):
    f1 = f[j]
    xcos = np.cos(2 * np.pi * f1 * x)
    xsin = np.sin(2 * np.pi * f1 * x)
    X = np.column_stack([X, xcos, xsin])

md_3 = sm.OLS(y, X).fit()
print(md_3.summary())
best_rss_3 = np.sum(md_3.resid ** 2)
print(best_rss_3)


plt.figure(figsize = (10, 6))
#plt.plot(y, linestyle = '', marker = '')
plt.plot(y)
#plt.plot(md_1.fittedvalues, color = 'red', label = 'One frequency')
#plt.plot(md_2.fittedvalues, color = 'black', label = 'Two frequencies')
plt.plot(md_3.fittedvalues, color = 'red', label = 'Three frequencies')
plt.legend()
plt.show()
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.534
Model:                            OLS   Adj. R-squared:                  0.525
Method:                 Least Squares   F-statistic:                     60.64
Date:                Thu, 25 Sep 2025   Prob (F-statistic):           7.93e-50
Time:                        16:35:57   Log-Likelihood:                -1677.9
No. Observations:                 325   AIC:                             3370.
Df Residuals:                     318   BIC:                             3396.
Df Model:                           6
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         78.7632      2.370     33.229      0.000      74.100      83.427
x1           -35.3139      3.537     -9.984      0.000     -42.273     -28.355
x2           -40.2022      3.539    -11.360      0.000     -47.165     -33.240
x3           -23.2887      3.557     -6.548      0.000     -30.286     -16.291
x4            23.6220      3.544      6.665      0.000      16.649      30.595
x5            31.9130      3.362      9.492      0.000      25.299      38.527
x6             1.7416      3.366      0.517      0.605      -4.880       8.363
==============================================================================
Omnibus:                       29.948   Durbin-Watson:                   0.393
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               39.822
Skew:                           0.665   Prob(JB):                     2.25e-09
Kurtosis:                       4.082   Cond. No.                         1.73
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
580238.0830404736
```

*(1 figure omitted — see the original notebook.)*

Below we look at the smallest RSS achieved with one frequency, two frequencies and three frequencies respectively.

```python
print(np.array([best_rss_1, best_rss_2, best_rss_3]))
```

```
[866098.0246371  702139.35664397 580238.08304047]
```

If, instead of trying to find the best frequencies, we only look at the Fourier frequencies, the RSS will be much higher.

```python
print(rss([30/n, 31/n, 29/n]))
```

```
765576.0204283749
```

The best Fourier frequencies can be found as follows (these are the maximizers of the periodogram):

```python
print(n * freqs[np.argsort(pgram)[::-1]])
```

```
[ 30.  31.  29.  32.   3.  27.   6.  33.  40.   2.   5.  28.  25.   4.
  38.  37.  15.  39.  35.  59.  57.  23.  26.  34.   1.  12.   8.  22.
  44.  45.  10.  11.   7.  19.  21.  55.   9.  20.  43.  62.  60.  68.
  14.  65.  17.  56.  67.  41. 102.  47.  49.  82.  54.  77.  63.  71.
  89.  58.  69.  46. 116.  73.  18.  61.  80. 100.  74.  24. 140.  87.
 139.  16.  64.  52.  78. 152. 103.  42.  70.  75. 101.  66. 158.  13.
 104. 150.  94. 130. 156.  79.  84.  91. 161.  95. 120.  50.  93. 148.
 131.  76.  90.  48.  53. 110. 111. 122. 160. 153.  92. 105. 118. 145.
 128. 106. 113.  88. 138. 154. 143. 134. 124. 114. 136. 112. 117. 137.
 132.  97. 159. 141. 125. 147. 121. 115. 142. 126.  99. 135. 129.  36.
 108. 157. 146. 151.  51.  81. 109. 123.  98. 107.  83. 149. 162.  85.
  86. 133. 144. 155. 119.  96.  72. 127.]
```

```python
print(rss([30/n, 31/n, 29/n, 32/n]))
print([30/n, 31/n, 29/n, 32/n])
print(f_opt_3)
```

Below we plot the best fitted function with the top 5 Fourier frequencies.

```python
n = len(y)
f = [30/n, 31/n, 29/n, 32/n, 3/n] #f_opt was obtained from the grid minimization
x = np.arange(1, n+1)
X = np.column_stack([np.ones(n)])
x = np.arange(1, n+1)
if np.isscalar(f):
    f = [f]
for j in range(len(f)):
    f1 = f[j]
    xcos = np.cos(2 * np.pi * f1 * x)
    xsin = np.sin(2 * np.pi * f1 * x)
    X = np.column_stack([X, xcos, xsin])

md_5 = sm.OLS(y, X).fit()
print(md_5.summary())
best_rss_5 = np.sum(md_3.resid ** 2)
print(best_rss_5) #computed with Fourier frequencies


plt.figure(figsize = (10, 6))
#plt.plot(y, linestyle = '', marker = '')
plt.plot(y)
#plt.plot(md_1.fittedvalues, color = 'red', label = 'One frequency')
plt.plot(md_3.fittedvalues, color = 'black', label = 'Three frequencies')
plt.plot(md_5.fittedvalues, color = 'red', label = 'Five frequencies')
plt.legend()
plt.show()
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.560
Model:                            OLS   Adj. R-squared:                  0.546
Method:                 Least Squares   F-statistic:                     39.94
Date:                Thu, 25 Sep 2025   Prob (F-statistic):           3.02e-50
Time:                        16:42:39   Log-Likelihood:                -1668.5
No. Observations:                 325   AIC:                             3359.
Df Residuals:                     314   BIC:                             3401.
Df Model:                          10
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         78.7600      2.317     34.000      0.000      74.202      83.318
x1            26.2644      3.276      8.017      0.000      19.819      32.710
x2           -19.9931      3.276     -6.103      0.000     -26.439     -13.547
x3            -3.2889      3.276     -1.004      0.316      -9.735       3.157
x4           -32.8289      3.276    -10.021      0.000     -39.275     -26.383
x5           -10.6690      3.276     -3.257      0.001     -17.115      -4.223
x6            25.5532      3.276      7.800      0.000      19.107      31.999
x7            -2.7915      3.276     -0.852      0.395      -9.237       3.654
x8           -27.3138      3.276     -8.337      0.000     -33.759     -20.868
x9           -24.2296      3.276     -7.396      0.000     -30.675     -17.784
x10           -0.6090      3.276     -0.186      0.853      -7.055       5.837
==============================================================================
Omnibus:                       57.146   Durbin-Watson:                   0.468
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              108.550
Skew:                           0.948   Prob(JB):                     2.68e-24
Kurtosis:                       5.103   Cond. No.                         1.41
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
580238.0830404736
```

*(1 figure omitted — see the original notebook.)*

Below we compare the prediction accuracy for the best models based on Fourier frequencies (compared to the frequencies chosen over grids). We use the first 275 observations for training the model, and check the prediction accuracy on the test dataset (last 50 observations).

```python
n = len(y)
f = np.array([30/n, 31/n, 29/n, 32/n], dtype=float) #these are the 5 best fourier frequencies
#f = f_opt_3 #this gives the best prediction accuracy
#f = np.array([30/n, 31/n, 29/n], dtype=float) #these are best three Fourier frequencies

# time index 1..n
x = np.arange(1, n+1, dtype=float)

# Build design matrix for ALL times (intercept + cos/sin for each f), vectorized
cos_cols = np.cos(2*np.pi*np.outer(x, f))   # shape (n, k)
sin_cols = np.sin(2*np.pi*np.outer(x, f))   # shape (n, k)
X_all = np.column_stack([np.ones(n), cos_cols, sin_cols])

# Hold out the last 25 observations for testing
n_test = 50
X_train, X_test = X_all[:-n_test], X_all[-n_test:]
y_train, y_test = y[:-n_test], y[-n_test:]

# Fit on train only
model = sm.OLS(y_train, X_train).fit()

# Predict the last 25 and compute test MSE
y_pred_test = model.predict(X_test)
test_mse = np.mean((y_test - y_pred_test)**2)

#print(model.summary())
print(f"Test MSE (last {n_test} observations): {test_mse:.6g}")
```

```
Test MSE (last 50 observations): 2253.98
```

```python
y_fit_train = model.predict(X_train)
plt.figure(figsize=(10, 6))
plt.plot(y, label='Observed')
plt.plot(np.arange(len(y_fit_train)), y_fit_train, color='black', label='Train fit')
plt.plot(np.arange(n - n_test, n), y_pred_test, color='red', label='Test predictions')
plt.axvspan(n - n_test, n - 1, alpha=0.1, label='Test window')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Discrete Fourier Transform

For a dataset $y_0, \dots, y_{n-1}$, its DFT is $b_0, b_1, \dots, b_{n-1}$ where
\begin{equation*}
   b_j = \sum_{t=0}^{n-1} y_t \exp \left(-\frac{2 \pi i j t}{n} \right).
\end{equation*}
for $j = 0, 1, \dots, n-1$. In other words, $b_j$ is a complex number with real part $\sum_t y_t \cos(2 \pi (j/n) t)$ and imaginary part $-\sum_t y_t \sin(2 \pi (j/n) t)$.

```python
y = np.array([1, -5, 3, 10, -5, 1, 6])
dft_y = np.fft.fft(y)
print(dft_y)
b0 = np.sum(y)
print(b0)
n = len(y)
#Here is the formula for calculating the real and imaginary parts of b2:
f = 3/n
cosvec = np.cos(2 * np.pi * f * np.arange(n))
sinvec = np.sin(2 * np.pi * f * np.arange(n))
b_cos = np.sum(y * cosvec)
b_sin = np.sum(y * sinvec)
print(b_cos, b_sin) #the real part of DFT is b_cos and the imaginary part is -b_sin (note the negative sign for the imaginary part)
```

---

[← Sunspots Dataset](01-sunspots-dataset.md) · [Up: contents](index.md) · Orthogonality of Sinusoids at Fourier Frequencies →
