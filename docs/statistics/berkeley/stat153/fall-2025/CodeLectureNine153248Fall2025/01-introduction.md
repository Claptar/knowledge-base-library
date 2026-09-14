---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureNine153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureNine153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureNine153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureNine153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: More on Sinusoidal Models
---

## Sunspots Dataset

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
```

To this sunspots dataset, we shall fit the sinusoidal model:
\begin{equation*}
  y_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin(2 \pi f t) + \epsilon_t
\end{equation*}
with $\epsilon_t$ being i.i.d $N(0, \sigma^2)$. We focus on estimation and uncertainty quantification for the important parameter in this model is $f$. We do this in two ways: (a) using Fourier frequencies, and (b) using a dense grid of frequencies, and we compare the results.

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header = None, sep = ';')
y = sunspots.iloc[:,1].values
n = len(y)
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

When restricting to Fourier frequencies, computation of $RSS(f)$ proceeds via the DFT and periodogram. Here is the code for computing the periodogram.

```python
def periodogram(y):
    fft_y = np.fft.fft(y) #this computation is very fast O(n log n)
    n = len(y)
    fourier_freqs = np.arange(1/n, 1/2, 1/n)
    m = len(fourier_freqs)
    pgram_y = (np.abs(fft_y[1:m+1]) ** 2)/n
    return fourier_freqs, pgram_y
```

Below we plot the periodogram.

```python
freqs, pgram = periodogram(y)
plt.plot(freqs, pgram)
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.title('Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Below is the code for computing the RSS using the periodogram.

```python
def rss_periodogram(y):
    fft_y = np.fft.fft(y)
    n = len(y)
    fourier_freqs = np.arange(1/n, 1/2, 1/n)
    m = len(fourier_freqs)
    pgram_y = (np.abs(fft_y[1:m+1]) ** 2)/n
    var_y = np.sum((y - np.mean(y)) ** 2)
    rssvals = var_y - 2*pgram_y
    return fourier_freqs, rssvals
```

The following is the plot for the RSS (restricted to Fourier frequencies in the range $(0, 0.5)$):

```python
freqs, rssvals = rss_periodogram(y)
plt.plot(freqs, rssvals)
plt.xlabel('Frequency')
plt.ylabel('Residual Sum of Squares')
plt.title('RSS Plot')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Below is the estimate of $f$ (along with the corresponding period) based on this RSS. It is simply the minimizer of RSS (or equivalently, maximizer of the periodogram):

```python
#Estimate of f and the corresponding period:
fhat = freqs[np.argmax(pgram)]
print(fhat)
period_hat = 1/fhat
print(period_hat)
```

```
0.09230769230769231
10.833333333333332
```

The estimate of the period is somewhat close to 11 but not very close. Let us now do uncertainty quantification (again with the restriction to Fourier frequencies) to see how wide the uncertainty interval for $f$ is. The following function calculates the posterior for $f$ on the log-scale. Recall that the posterior is given by:
\begin{align*}
  \text{posterior}(j/n) \propto \left(\frac{1}{RSS(j/n)} \right)^{(n-3)/2} I\{0 < j/n < 0.5\}.
\end{align*}
Note that there is no term $|X_f^T X_f|^{-1/2}$ as this term is a constant (not depending on $f$) when $f$ is restricted to Fourier frequencies. In the function below, we compute this posterior on the log-scale, and we use the connection between RSS and periodogram to compute the RSS.

```python
#Uncertainty quantification for f:
def logpost_periodogram(y):
    fft_y = np.fft.fft(y)
    n = len(y)
    fourier_freqs = np.arange(1/n, (1/2) + (1/n), 1/n)
    m = len(fourier_freqs)
    pgram_y = (np.abs(fft_y[1:m+1]) ** 2)/n
    var_y = np.sum((y - np.mean(y)) ** 2)
    rssvals = var_y - 2*pgram_y
    p = 3
    logpostvals = ((p-n)/2) * np.log(rssvals)
    return fourier_freqs, logpostvals
```

Below we plot the log posterior as a function of the fourier frequencies.

```python
freqs, logpostvals = logpost_periodogram(y)
plt.plot(freqs, logpostvals)
plt.xlabel('Frequency')
plt.ylabel('Logarithm of Unnormalized Posterior')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Below we exponentiate the log-posterior to compute the posterior (and subsequently normalize the posterior). We then compute the posterior mode, and the smallest symmetric region around the posterior mode for which the posterior probability exceeds 0.95. This will give our uncertainty interval for $f$. Note again that in this analysis, we are restricting $f$ to the set of Fourier frequencies.

```python
freqs, logpostvals = logpost_periodogram(y)
postvals_unnormalized = np.exp(logpostvals - np.max(logpostvals))
postvals = postvals_unnormalized/(np.sum(postvals_unnormalized))

def PostProbAroundMax(m):
    est_ind = np.argmax(postvals)
    ans = np.sum(postvals[(est_ind-m):(est_ind+m+1)])
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
[0.09230769 0.08923077 0.09538462]
[10.48387097 10.83333333 11.20689655]
```

For better interpretation of the uncertainty interval, let us convert the uncertainty range into days (as opposed to years). This gives:

```python
np.array([(period_est - ci_period_low)*365, (ci_period_high - period_est)*365])
```

```
array([127.55376344, 136.35057471])
```

Note that this interval for the period ($1/f$) is not symmetric because we took inverses (the interval for $f$ is symmetric).

The point estimate and the credible interval can be summarized as:
\begin{equation*}
   [10.83 \text{ years } - 127 \text{ days }, 10.83 \text{ years } + 136 \text{ days }]
\end{equation*}

Here we are losing something in doing the analysis through Fourier frequencies. If we instead use a much finer grid of frequencies, we will get a much narrower uncertainty for $f$ and the period. This is illustrated below.

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
    ans = np.sum(postvals[(est_ind-m):(est_ind+m+1)])
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
   [11 \text{ years } - 13 \text{ days}, 11 \text{ years } + 13 \text{ days}]
\end{equation*}
which is much narrower compared to the previous estimate of the period based only on Fourier frequencies.

## Fitting more sinusoids to the sunspots data

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

---

[Up: contents](index.md) · [mesh on the 3 axes; 'ij' preserves axis ordering →](02-mesh-on-the-3-axes-ij-preserves-axis-ordering.md)
