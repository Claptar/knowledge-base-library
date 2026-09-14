---
title: Sunspots Dataset
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureEight153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureEight153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Sunspots Dataset

**Source:** [`CodeLectureEight153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureEight153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header = None, sep = ';')
y = sunspots.iloc[:,1].values
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
freqs, pgram = periodogram(y)
plt.plot(freqs, pgram)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Estimate of f and the corresponding period:
fhat = freqs[np.argmax(pgram)]
period_hat = 1/fhat
print(period_hat)
```

```
10.833333333333334
```

```python
freqs, logpostvals = logpost_periodogram(y)
postvals_unnormalized = np.exp(logpostvals - np.max(logpostvals))
postvals = postvals_unnormalized/(np.sum(postvals_unnormalized))

def PostProbAroundMax(m):
    est_ind = np.argmax(postvals)
    ans = np.sum(postvals[(est_ind-m):(est_ind+m)])
    return(ans)
m = 0
while PostProbAroundMax(m) <= 0.95:
    m = m+1
est_ind = np.argmax(postvals)
f_est = freqs[est_ind]
#95% credible interval for f:
ci_f_low = freqs[est_ind - m]
ci_f_high = freqs[est_ind + m]
print(np.array([f_est, ci_f_low, ci_f_high]))

period_est = 1/f_est
ci_period_low = 1/ci_f_high
ci_period_high = 1/ci_f_low
print(np.array([ci_period_low, period_est, ci_period_high]))
```

```
[0.09230769 0.08615385 0.09846154]
[10.15625    10.83333333 11.60714286]
```

```python
np.array([(period_est - ci_period_low)*365, (ci_period_high - period_est)*365])
```

```
array([247.13541667, 282.44047619])
```

The point estimate and the credible interval can be summarized as:
\begin{equation*}
   [10.83 \text{ years } - 247 \text{ days }, 10.83 \text{ years } + 282 \text{ days }]
\end{equation*}

Here we are losing something in doing the analysis through Fourier frequencies. If we instead use a much finer grid of frequencies, we will get a much narrower uncertainty for $f$ and the period.

```python
def logpost(f):
    n = len(y)
    x = np.arange(1, n+1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([np.ones(n), xcos, xsin])
    p = X.shape[1]
    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)
    sgn, log_det = np.linalg.slogdet(np.dot(X.T, X)) #sgn gives the sign of the determinant (in our case, this should 1)
    #log_det gives the logarithm of the absolute value of the determinant
    logval = ((p-n)/2) * np.log(rss) - (0.5)*log_det
    return logval

allfvals = np.arange(0.01, 0.5, .0001) #much finer grid
logpostvals = np.array([logpost(f) for f in allfvals])
postvals = np.exp(logpostvals - np.max(logpostvals))
postvals = postvals/(np.sum(postvals))
print(allfvals[np.argmax(postvals)])
print(1/allfvals[np.argmax(postvals)])
```

```
0.09089999999999951
11.00110011001106
```

```python
def PostProbAroundMax(m):
    est_ind = np.argmax(postvals)
    ans = np.sum(postvals[(est_ind-m):(est_ind+m)])
    return(ans)
m = 0
while PostProbAroundMax(m) <= 0.95:
    m = m+1
est_ind = np.argmax(postvals)
f_est = allfvals[est_ind]
#95% credible interval for f:
ci_f_low = allfvals[est_ind - m]
ci_f_high = allfvals[est_ind + m]
print(np.array([f_est, ci_f_low, ci_f_high]))

period_est = 1/f_est
ci_period_low = 1/ci_f_high
ci_period_high = 1/ci_f_low
print(np.array([ci_period_low, period_est, ci_period_high]))
```

```
[0.0909 0.0906 0.0912]
[10.96491228 11.00110011 11.03752759]
```

```python
np.array([(period_est - ci_period_low)*365, (ci_period_high - period_est)*365])
```

```
array([13.2085577 , 13.29603159])
```

So the uncertainty period can be summarized as:
\begin{equation*}
   [11 \text{ years } - 13.2 \text{ days}, 11 \text{ years } + 13.3 \text{ days}]
\end{equation*}
which is much narrower compared to the previous estimate of the period based only on Fourier frequencies.

### Fitting two sinusoids to the sunspots data

The periodogram can be used to suggest other models for the data. For the sunspots, the periodogram shows another frequency (which is much smaller than the 1/11 frequency) also has stronger power compared to its neighboring frequency. This might suggests the model:
\begin{equation*}
  y_t = \beta_0 + \beta_1 \cos(2 \pi f_1 t) + \beta_2 \sin(2 \pi f_1 t) + \beta_3 \cos(2 \pi f_2 t) + \beta_4 \sin(2 \pi f_2 t) + \epsilon_t
\end{equation*}
with both $f_1$ and $f_2$ denoting unknown parameters (along with $\beta_0, \beta_1, \beta_2, \beta_3, \beta_4$ and $\sigma$).

```python
freqs, pgram = periodogram(y)
plt.plot(freqs, pgram)
print(pgram)
```

```
[4.01088439e+03 1.26974867e+04 4.77297930e+04 8.70355431e+03
 1.12773110e+04 1.97012775e+04 1.99517379e+03 3.27980926e+03
 1.85999321e+03 2.05650593e+03 2.00187676e+03 3.35780063e+03
 2.70593790e+02 1.30319204e+03 7.06065964e+03 3.59682320e+02
 1.26206651e+03 4.71775939e+02 1.92275157e+03 1.79871306e+03
 1.89084747e+03 3.08964635e+03 4.42531690e+03 3.87102917e+02
 1.03191298e+04 4.23538290e+03 3.54415717e+04 1.08635660e+04
 6.23020333e+04 8.85252845e+04 8.84452519e+04 6.12489810e+04
 1.93441390e+04 4.21905730e+03 4.98195377e+03 3.85342684e+01
 7.89981650e+03 8.09772100e+03 5.20200317e+03 1.63452492e+04
 1.16651003e+03 2.95753013e+02 1.76392645e+03 2.59952918e+03
 2.12652083e+03 5.58100806e+02 9.14876776e+02 1.74020095e+02
 9.06805007e+02 2.11113310e+02 3.53243443e+01 3.48589976e+02
 1.57175530e+02 8.13281407e+02 1.88543436e+03 1.23676189e+03
 4.56802465e+03 6.78280638e+02 4.63319403e+03 1.59216745e+03
 4.50686809e+02 1.72894893e+03 7.59341336e+02 3.49550991e+02
 1.26903926e+03 2.79519394e+02 1.18966623e+03 1.48998334e+03
 6.61771486e+02 2.85746781e+02 7.17873708e+02 8.45294925e-01
 5.19890678e+02 3.98373906e+02 2.83005672e+02 1.99210455e+02
 7.62855531e+02 3.41710825e+02 2.43845875e+02 4.29775791e+02
 2.82099284e+01 8.44166448e+02 2.49406002e+01 2.39676657e+02
 1.86506986e+01 1.23597987e+01 3.74896219e+02 1.00338538e+02
 7.08119468e+02 1.75402561e+02 2.28395208e+02 1.20249110e+02
 2.07944689e+02 2.62763940e+02 2.21799503e+02 3.49803449e+00
 6.43784249e+01 2.54361793e+01 5.29661532e+01 4.05702574e+02
 2.79666173e+02 9.92553398e+02 3.10650859e+02 2.69630834e+02
 1.17191941e+02 1.08583577e+02 2.50519504e+01 3.76424772e+01
 2.60793028e+01 1.46241051e+02 1.41273213e+02 7.54162928e+01
 1.01043367e+02 8.31329324e+01 5.52401375e+01 5.46880788e+02
 7.40378233e+01 1.16012736e+02 4.63632828e+00 2.17629912e+02
 5.62837433e+01 1.31742816e+02 2.58148665e+01 8.38391575e+01
 5.97333453e+01 5.45167911e+01 5.53229242e-01 1.09375107e+02
 4.49951267e+01 2.58261199e+02 2.05794255e+02 6.97223568e+01
 9.36347039e+00 8.43348895e+01 5.23823824e+01 7.82297907e+01
 7.30425065e+01 9.53405890e+01 3.62747466e+02 3.80794296e+02
 6.08213753e+01 5.45772689e+01 8.98456611e+01 9.05460887e+00
 1.12274719e+02 3.63806714e+01 5.65311984e+01 2.07171247e+02
 2.45971879e+01 2.63687739e+02 3.61661096e+01 3.41586543e+02
 1.24920509e+02 9.05943774e+01 8.42935197e+00 2.53330115e+02
 3.74474309e+01 2.78470522e+02 6.08369905e+01 1.29312198e+02
 2.28090974e+02 2.05734310e+01]
```

*(1 figure omitted — see the original notebook.)*

We can try to fit two sinusoids (at $f_1 = 1/11$ and $f_2 = 3/n$ to the data) to see if we get an improved fit visually.

```python
n = len(y)
f1 = 1/11
x = np.arange(1, n+1)
xcos1 = np.cos(2 * np.pi * f1 * x)
xsin1 = np.sin(2 * np.pi * f1 * x)
X = np.column_stack([np.ones(n), xcos1, xsin1])
md1 = sm.OLS(y, X).fit()

f2 = 3/n
xcos2 = np.cos(2 * np.pi * f2 * x)
xsin2 = np.sin(2 * np.pi * f2 * x)
X = np.column_stack([np.ones(n), xcos1, xsin1, xcos2, xsin2])
md2 = sm.OLS(y, X).fit()
```

```python
plt.figure(figsize = (10, 6))
#plt.plot(y, linestyle = '', marker = '')
plt.plot(y)
plt.plot(md1.fittedvalues, color = 'red', marker = '', linestyle = '')
plt.plot(md2.fittedvalues, color = 'black')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The fit seems to have improved compared to the single sinusoid model. Let us now try to find the best $f_1$ and $f_2$ for the two sinusoid model using a grid search to minimize the RSS. The function for RSS is given below.

```python
def rss(f):
    n = len(y)
    x = np.arange(1, n+1)
    f1 = f[0]
    xcos1 = np.cos(2 * np.pi * f1 * x)
    xsin1 = np.sin(2 * np.pi * f1 * x)
    f2 = f[1]
    xcos2 = np.cos(2 * np.pi * f2 * x)
    xsin2 = np.sin(2 * np.pi * f2 * x)
    X = np.column_stack([np.ones(n), xcos1, xsin1, xcos2, xsin2])
    md = sm.OLS(y, X).fit()
    ans = np.sum(md.resid ** 2)
    return ans

#As examples, consider the following RSS values:
print(rss(np.array([1/11, 2/n])))
print(rss(np.array([1/11, 3/n])))
```

```
841338.0869793112
772463.5063723011
```

Now we do grid search to find the best $f_1$ and $f_2$ which fit the data. The intervals over which the grids need to be placed should be chosen carefully. Here I am using the intuition (based on the periodogram) that $f_1$ is the main frequency which should be around 1/11, and $f_2$ should be much smaller (the periodogram's first peak was at $3/n$).

```python
f1_gr = np.linspace(0.05, 0.15, 300)
f2_gr = np.linspace(1/n, 4/n, 300)
X, Y = np.meshgrid(f1_gr, f2_gr)
g = pd.DataFrame({'x': X.flatten(), 'y': Y.flatten()})

g['z'] = g.apply(lambda row: rss([row['x'], row['y']]), axis = 1)
```

The best $f_1$ and $f_2$ which minimize the RSS over the chosen grid can be obtained as follows.

```python
min_row = g.loc[g['z'].idxmin()]
print(min_row)
f_opt = np.array([min_row['x'], min_row['y']])
print(f_opt)
```

```
x         0.090803
y         0.009931
z    758772.699688
Name: 66722, dtype: float64
[0.09080268 0.00993054]
```

We can fit the two sinusoid model with these $f_1$ and $f_2$ and look at the fitted values.

```python
n = len(y)
f1 = f_opt[0]
x = np.arange(1, n+1)
xcos1 = np.cos(2 * np.pi * f1 * x)
xsin1 = np.sin(2 * np.pi * f1 * x)
X = np.column_stack([np.ones(n), xcos1, xsin1])
md1 = sm.OLS(y, X).fit()

f2 = f_opt[1]
xcos2 = np.cos(2 * np.pi * f2 * x)
xsin2 = np.sin(2 * np.pi * f2 * x)
X = np.column_stack([np.ones(n), xcos1, xsin1, xcos2, xsin2])
md2 = sm.OLS(y, X).fit()

plt.figure(figsize = (10, 6))
#plt.plot(y, linestyle = '', marker = '')
plt.plot(y)
plt.plot(md1.fittedvalues, color = 'red', marker = '', linestyle = '')
plt.plot(md2.fittedvalues, color = 'black')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Fitting three sinusoids to the sunspots data

We now fit three sinusoids to the sunspots data. The following is the function for computing the RSS. Here $f$ represents a possible array containing multiple frequencies.

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

We need to place three grids for the three frequency parameters. Again, the ranges for the three grids need to be carefully chosen.

```python
#Searching for the three best frequencies (will be computationally intensive):
f1_gr = np.linspace(1/12, 1/9, 50)
f2_gr = np.linspace(1/n, 4/n, 50)
f3_gr = np.linspace(0.09, 0.12, 50)
X, Y, Z = np.meshgrid(f1_gr, f2_gr, f3_gr)
g = pd.DataFrame({'x': X.flatten(), 'y': Y.flatten(), 'z': Z.flatten()})

g['rss'] = g.apply(lambda row: rss([row['x'], row['y'], row['z']]), axis = 1)
```

```python
min_row = g.loc[g['rss'].idxmin()]
print(min_row)
f_opt = np.array([min_row['x'], min_row['y'], min_row['z']])
print(f_opt)
```

```
x           0.090703
y           0.010047
z           0.099796
rss    595011.787595
Name: 93166, dtype: float64
[0.09070295 0.0100471  0.09979592]
```

Below, we fit the three sinusoid model with $f$ chosen as the grid-based minimizer above.

```python
rss(np.array([1/11, 0.009, 0.1]))
n = len(y)
f = f_opt #f_opt was obtained from the grid minimization
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

md = sm.OLS(y, X).fit()
print(md.summary())

plt.figure(figsize = (10, 6))
#plt.plot(y, linestyle = '', marker = '')
plt.plot(y)
plt.plot(md1.fittedvalues, color = 'red', marker = '', linestyle = '')
plt.plot(md2.fittedvalues, color = 'black', marker = '', linestyle = '')
plt.plot(md.fittedvalues, color = 'red')
plt.show()
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.522
Model:                            OLS   Adj. R-squared:                  0.513
Method:                 Least Squares   F-statistic:                     57.82
Date:                Thu, 13 Feb 2025   Prob (F-statistic):           4.13e-48
Time:                        23:30:21   Log-Likelihood:                -1681.9
No. Observations:                 325   AIC:                             3378.
Df Residuals:                     318   BIC:                             3404.
Df Model:                           6
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         80.8124      2.412     33.506      0.000      76.067      85.558
x1           -43.4458      3.395    -12.797      0.000     -50.125     -36.766
x2           -19.0327      3.393     -5.609      0.000     -25.708     -12.357
x3           -16.6335      3.417     -4.867      0.000     -23.357      -9.910
x4           -18.8847      3.394     -5.564      0.000     -25.562     -12.207
x5            30.3109      3.397      8.922      0.000      23.627      36.995
x6           -10.7739      3.391     -3.178      0.002     -17.445      -4.103
==============================================================================
Omnibus:                       40.259   Durbin-Watson:                   0.451
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               65.340
Skew:                           0.750   Prob(JB):                     6.48e-15
Kurtosis:                       4.604   Cond. No.                         1.46
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

*(1 figure omitted — see the original notebook.)*

---

[← Audio Data](02-audio-data.md) · [Up: contents](index.md)
