---
title: Sunspots Data
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureSixteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureSixteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Sunspots Data

**Source:** [`CodeLectureSixteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureSixteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Autoregressive models were invented in the context of the sunspots data by Yule in 1927.

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header = None, sep = ';')
y = sunspots.iloc[:,1].values
n = len(y)
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The most basic model for this dataset is the single sinusoid model:
\begin{equation*}
    y_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin(2 \pi f t) + \epsilon_t
\end{equation*}
with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. We previously used this model. For estimating $f$, we calculate $RSS(f)$ for a bunch of $f$ values, and then minimize it over $f$.

```python
#rss function:
def rss(f):
    n = len(y)
    X = np.column_stack([np.ones(n)])
    x = np.arange(1, n+1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([X, xcos, xsin])
    md = sm.OLS(y, X).fit()
    ans = np.sum(md.resid ** 2)
    return ans
```

```python
ngrid = 10000
fvals = np.linspace(0, 0.5, ngrid)
rssvals = np.array([rss(f) for f in fvals])
plt.plot(fvals, rssvals) #plot rss and find f which minimizes rss
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
fhat = fvals[np.argmin(rssvals)]
print(fhat)
print(1/fhat)  #period corresponding to fhat
```

```
0.09090909090909091
11.0
```

The MLE of $f$ is basically $1/11$ (corresponding to the 11-year solar cycle). After estimating $f$, the other parameters $\beta_0, \beta_1, \beta_2, \sigma$ are estimated as in usual linear regression as follows.

```python
#Estimates of beta and sigma:
x = np.arange(1, n+1)
f = fhat
xcos = np.cos(2 * np.pi * f * x)
xsin = np.sin(2 * np.pi * f * x)
X = np.column_stack([np.ones(n), xcos, xsin])
md = sm.OLS(y, X).fit()
print(md.params) #this gives estimates of beta_0, beta_1, beta_2
rss_fhat = np.sum(md.resid ** 2)
#there are two estimates for sigma (which usually give similar values)
sigma_mle = np.sqrt(rss_fhat/n)
sigma_unbiased = np.sqrt((rss_fhat)/(n-3))
print(np.array([sigma_mle, sigma_unbiased]))
```

```
[ 78.87599158 -38.28231622 -29.2786631 ]
[51.62376442 51.86369026]
```

Yule did not like the simple single sinusoidal model for the sunspots data, mainly because if we simulate data from it, the data will look much more noisy and irregular as opposed to the sunspots data which have a smooth appearance. We can check this by simulating synthetic data from the single sinusoid model and comparing the synthetic data with the actual sunspots data. We will take the parameters $f, \beta, \sigma$ to be those estimated from the sunspots dataset to make the plots  comparable to the actual sunspots data.

```python
rng = np.random.default_rng(seed = 42)
errorsamples = rng.normal(loc = 0, scale = sigma_mle, size = n)
sim_data = md.fittedvalues + errorsamples
plt.figure(figsize = (10, 6))
plt.plot(sim_data)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

To facilitate comparison with the actual sunspots dataset, let us plot a bunch of these simulated datasets along with the real sunspots data (just to see if the sunspots dataset can be spotted as the “odd one out” from these plots).

```python
fig, axes = plt.subplots(3, 3, figsize = (12, 4))
axes = axes.flatten()
for i in range(5):
    errorsamples = rng.normal(loc = 0, scale = sigma_mle, size = n)
    sim_data = md.fittedvalues + errorsamples
    axes[i].plot(sim_data)
axes[5].plot(y)
for i, idx in enumerate(range(6, 9)):
    errorsamples = rng.normal(loc = 0, scale = sigma_mle, size = n)
    sim_data = md.fittedvalues + errorsamples
    axes[idx].plot(sim_data)
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is clear from the above plot-grid that the sunspots dataset sticks out as the odd one out. This shows that the simulated datasets (which are too wiggly and do not have well-defined peaks) are generated from a model that ignores many aspects of the sunspots dataset.

### Yule Model

Yule model is given by:
\begin{equation*}
   y_t = \phi_0 + \phi_1 y_{t-1} - y_{t-2} + \epsilon_t
\end{equation*}
Note that $\phi_2$ in the usual AR(2) model is set to -1 above. Also $\phi_1$ is given by $2 \cos(2 \pi f)$. The above model can be rewritten as
\begin{equation*}
  y_t + y_{t-2} = \phi_0 + \phi_1 y_{t-1} + \epsilon_t
\end{equation*}
so we can estimate $\phi_0$ and $\phi_1$ by regressing $y_t + y_{t-2}$ on $y_{t-1}$.

```python
p = 2
yreg = y[p:]
x1 = y[1:-1]
x2 = y[:-2]
Xmat = np.column_stack([np.ones(len(yreg)), x1])
print(Xmat.shape)
```

```
(323, 2)
```

```python
y_adjusted = yreg + x2
yulemod = sm.OLS(y_adjusted, Xmat).fit()
print(yulemod.summary())
print(yulemod.params)
slpe_est = yulemod.params[1]
```

```
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared:                       0.930
Model:                            OLS   Adj. R-squared:                  0.930
Method:                 Least Squares   F-statistic:                     4254.
Date:                Thu, 23 Oct 2025   Prob (F-statistic):          2.90e-187
Time:                        16:51:37   Log-Likelihood:                -1532.1
No. Observations:                 323   AIC:                             3068.
Df Residuals:                     321   BIC:                             3076.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         28.6834      2.511     11.421      0.000      23.742      33.624
x1             1.6365      0.025     65.224      0.000       1.587       1.686
==============================================================================
Omnibus:                       11.119   Durbin-Watson:                   2.493
Prob(Omnibus):                  0.004   Jarque-Bera (JB):               17.202
Skew:                           0.225   Prob(JB):                     0.000184
Kurtosis:                       4.037   Cond. No.                         162.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[28.6833743   1.63648935]
```

From the estimate for $\phi_1$, the frequency parameter can be estimated using the relation: $\phi_1 = 2 \cos (2 \pi f)$.

```python
yulefhat = np.arccos(slpe_est/2) / (2 * np.pi)
print(1/yulefhat)
```

```
10.259176143439632
```

The period corresponding to this frequency is $10.259$ which is smaller than the period of 11 that we get by fitting $y_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin(2 \pi f t) + \epsilon_t$.

```python
#Generate k-step ahead forecasts:
k = 100
yhat = np.concatenate([y, np.full(k, -9999)]) #extend data by k placeholder values
for i in range(1, k+1):
    ans = yulemod.params[0] - yhat[n+i-3]
    ans += yulemod.params[1] * yhat[n+i-2]
    yhat[n+i-1] = ans
predvalues = yhat[n:]
print(predvalues)
print(yhat)
```

```
[ 1.56348277e+02  1.29845664e+02  8.48261433e+01  3.76547907e+01
  5.47889486e+00 -5.26328291e-03  2.31958661e+01  6.66484255e+01
  1.14556947e+02  1.49506172e+02  1.58791685e+02  1.39038104e+02
  9.74260659e+01  4.90819890e+01  1.15794607e+01 -1.44895065e+00
  1.47327213e+01  5.42422665e+01  1.02717544e+02  1.42537275e+02
  1.59226562e+02  1.46718673e+02  1.09560357e+02  6.12590590e+01
  1.93728148e+01 -8.72279635e-01  7.88308317e+00  4.24562356e+01
  9.02794685e+01  1.33968527e+02  1.57641974e+02  1.52694258e+02
  1.20923928e+02  7.38798357e+01  2.86630109e+01  1.71025067e+00
  2.81917042e+00  3.15866660e+01  7.75554463e+01  1.24015370e+02
  1.54077760e+02  1.56814618e+02  1.31231066e+02  8.66269979e+01
  3.92164679e+01  6.23370836e+00 -3.31696240e-01  2.19068486e+01
  6.48653949e+01  1.12928054e+02  1.48623536e+02  1.58976155e+02
  1.40222622e+02  9.91800471e+01  5.07678428e+01  1.25843613e+01
 -1.49029536e+00  1.36601606e+01  5.25283769e+01  1.00985343e+02
  1.41416436e+02  1.59124522e+02  1.47672524e+02  1.11223365e+02
  6.30267024e+01  2.06025365e+01 -6.27496582e-01  7.05394632e+00
  4.08545789e+01  8.84875112e+01  1.32637665e+02  1.57255989e+02
  1.53393461e+02  1.22454150e+02  7.56848253e+01  3.00866351e+01
  2.23500697e+00  2.25430426e+00  3.01375122e+01  7.57487878e+01
  1.22507947e+02  1.53417536e+02  1.57241592e+02  1.32590028e+02
  8.84239513e+01  4.07982008e+01  7.02524409e+00 -6.18089412e-01
  2.06466335e+01  6.30894595e+01  1.11281969e+02  1.47705672e+02
  1.59120165e+02  1.41376156e+02  1.00923784e+02  5.24679154e+01
  1.36227750e+01 -1.49101484e+00  1.26205694e+01  5.08278165e+01]
[ 8.30000000e+00  1.83000000e+01  2.67000000e+01  3.83000000e+01
  6.00000000e+01  9.67000000e+01  4.83000000e+01  3.33000000e+01
  1.67000000e+01  1.33000000e+01  5.00000000e+00  0.00000000e+00
  0.00000000e+00  3.30000000e+00  1.83000000e+01  4.50000000e+01
  7.83000000e+01  1.05000000e+02  1.00000000e+02  6.50000000e+01
  4.67000000e+01  4.33000000e+01  3.67000000e+01  1.83000000e+01
  3.50000000e+01  6.67000000e+01  1.30000000e+02  2.03300000e+02
  1.71700000e+02  1.21700000e+02  7.83000000e+01  5.83000000e+01
  1.83000000e+01  8.30000000e+00  2.67000000e+01  5.67000000e+01
  1.16700000e+02  1.35000000e+02  1.85000000e+02  1.68300000e+02
  1.21700000e+02  6.67000000e+01  3.33000000e+01  2.67000000e+01
  8.30000000e+00  1.83000000e+01  3.67000000e+01  6.67000000e+01
  1.00000000e+02  1.34800000e+02  1.39000000e+02  7.95000000e+01
  7.97000000e+01  5.12000000e+01  2.03000000e+01  1.60000000e+01
  1.70000000e+01  5.40000000e+01  7.93000000e+01  9.00000000e+01
  1.04800000e+02  1.43200000e+02  1.02000000e+02  7.52000000e+01
  6.07000000e+01  3.48000000e+01  1.90000000e+01  6.30000000e+01
  1.16300000e+02  1.76800000e+02  1.68000000e+02  1.36000000e+02
  1.10800000e+02  5.80000000e+01  5.10000000e+01  1.17000000e+01
  3.30000000e+01  1.54200000e+02  2.57300000e+02  2.09800000e+02
  1.41300000e+02  1.13500000e+02  6.42000000e+01  3.80000000e+01
  1.70000000e+01  4.02000000e+01  1.38200000e+02  2.20000000e+02
  2.18200000e+02  1.96800000e+02  1.49800000e+02  1.11000000e+02
  1.00000000e+02  7.82000000e+01  6.83000000e+01  3.55000000e+01
  2.67000000e+01  1.07000000e+01  6.80000000e+00  1.13000000e+01
  2.42000000e+01  5.67000000e+01  7.50000000e+01  7.18000000e+01
  7.92000000e+01  7.03000000e+01  4.68000000e+01  1.68000000e+01
  1.35000000e+01  4.20000000e+00  0.00000000e+00  2.30000000e+00
  8.30000000e+00  2.03000000e+01  2.32000000e+01  5.90000000e+01
  7.63000000e+01  6.83000000e+01  5.29000000e+01  3.85000000e+01
  2.42000000e+01  9.20000000e+00  6.30000000e+00  2.20000000e+00
  1.14000000e+01  2.82000000e+01  5.99000000e+01  8.30000000e+01
  1.08500000e+02  1.15200000e+02  1.17400000e+02  8.08000000e+01
  4.43000000e+01  1.34000000e+01  1.95000000e+01  8.58000000e+01
  1.92700000e+02  2.27300000e+02  1.68700000e+02  1.43000000e+02
  1.05500000e+02  6.33000000e+01  4.03000000e+01  1.81000000e+01
  2.51000000e+01  6.58000000e+01  1.02700000e+02  1.66300000e+02
  2.08300000e+02  1.82500000e+02  1.26300000e+02  1.22000000e+02
  1.02700000e+02  7.41000000e+01  3.90000000e+01  1.27000000e+01
  8.20000000e+00  4.34000000e+01  1.04400000e+02  1.78300000e+02
  1.82200000e+02  1.46600000e+02  1.12100000e+02  8.35000000e+01
  8.92000000e+01  5.78000000e+01  3.07000000e+01  1.39000000e+01
  6.28000000e+01  1.23600000e+02  2.32000000e+02  1.85300000e+02
  1.69200000e+02  1.10100000e+02  7.45000000e+01  2.83000000e+01
  1.89000000e+01  2.07000000e+01  5.70000000e+00  1.00000000e+01
  5.37000000e+01  9.05000000e+01  9.90000000e+01  1.06100000e+02
  1.05800000e+02  8.63000000e+01  4.24000000e+01  2.18000000e+01
  1.12000000e+01  1.04000000e+01  1.18000000e+01  5.95000000e+01
  1.21700000e+02  1.42000000e+02  1.30000000e+02  1.06600000e+02
  6.94000000e+01  4.38000000e+01  4.44000000e+01  2.02000000e+01
  1.57000000e+01  4.60000000e+00  8.50000000e+00  4.08000000e+01
  7.01000000e+01  1.05500000e+02  9.01000000e+01  1.02800000e+02
  8.09000000e+01  7.32000000e+01  3.09000000e+01  9.50000000e+00
  6.00000000e+00  2.40000000e+00  1.61000000e+01  7.90000000e+01
  9.50000000e+01  1.73600000e+02  1.34600000e+02  1.05700000e+02
  6.27000000e+01  4.35000000e+01  2.37000000e+01  9.70000000e+00
  2.79000000e+01  7.40000000e+01  1.06500000e+02  1.14700000e+02
  1.29700000e+02  1.08200000e+02  5.94000000e+01  3.51000000e+01
  1.86000000e+01  9.20000000e+00  1.46000000e+01  6.02000000e+01
  1.32800000e+02  1.90600000e+02  1.82600000e+02  1.48000000e+02
  1.13000000e+02  7.92000000e+01  5.08000000e+01  2.71000000e+01
  1.61000000e+01  5.53000000e+01  1.54300000e+02  2.14700000e+02
  1.93000000e+02  1.90700000e+02  1.18900000e+02  9.83000000e+01
  4.50000000e+01  2.01000000e+01  6.60000000e+00  5.42000000e+01
  2.00700000e+02  2.69300000e+02  2.61700000e+02  2.25100000e+02
  1.59000000e+02  7.64000000e+01  5.34000000e+01  3.99000000e+01
  1.50000000e+01  2.20000000e+01  6.68000000e+01  1.32900000e+02
  1.50000000e+02  1.49400000e+02  1.48000000e+02  9.44000000e+01
  9.76000000e+01  5.41000000e+01  4.92000000e+01  2.25000000e+01
  1.84000000e+01  3.93000000e+01  1.31000000e+02  2.20100000e+02
  2.18900000e+02  1.98900000e+02  1.62400000e+02  9.10000000e+01
  6.05000000e+01  2.06000000e+01  1.48000000e+01  3.39000000e+01
  1.23000000e+02  2.11100000e+02  1.91800000e+02  2.03300000e+02
  1.33000000e+02  7.61000000e+01  4.49000000e+01  2.51000000e+01
  1.16000000e+01  2.89000000e+01  8.83000000e+01  1.36300000e+02
  1.73900000e+02  1.70400000e+02  1.63600000e+02  9.93000000e+01
  6.53000000e+01  4.58000000e+01  2.47000000e+01  1.26000000e+01
  4.20000000e+00  4.80000000e+00  2.49000000e+01  8.08000000e+01
  8.45000000e+01  9.40000000e+01  1.13300000e+02  6.98000000e+01
  3.98000000e+01  2.17000000e+01  7.00000000e+00  3.60000000e+00
  8.80000000e+00  2.96000000e+01  8.32000000e+01  1.25500000e+02
  1.54700000e+02  1.56348277e+02  1.29845664e+02  8.48261433e+01
  3.76547907e+01  5.47889486e+00 -5.26328291e-03  2.31958661e+01
  6.66484255e+01  1.14556947e+02  1.49506172e+02  1.58791685e+02
  1.39038104e+02  9.74260659e+01  4.90819890e+01  1.15794607e+01
 -1.44895065e+00  1.47327213e+01  5.42422665e+01  1.02717544e+02
  1.42537275e+02  1.59226562e+02  1.46718673e+02  1.09560357e+02
  6.12590590e+01  1.93728148e+01 -8.72279635e-01  7.88308317e+00
  4.24562356e+01  9.02794685e+01  1.33968527e+02  1.57641974e+02
  1.52694258e+02  1.20923928e+02  7.38798357e+01  2.86630109e+01
  1.71025067e+00  2.81917042e+00  3.15866660e+01  7.75554463e+01
  1.24015370e+02  1.54077760e+02  1.56814618e+02  1.31231066e+02
  8.66269979e+01  3.92164679e+01  6.23370836e+00 -3.31696240e-01
  2.19068486e+01  6.48653949e+01  1.12928054e+02  1.48623536e+02
  1.58976155e+02  1.40222622e+02  9.91800471e+01  5.07678428e+01
  1.25843613e+01 -1.49029536e+00  1.36601606e+01  5.25283769e+01
  1.00985343e+02  1.41416436e+02  1.59124522e+02  1.47672524e+02
  1.11223365e+02  6.30267024e+01  2.06025365e+01 -6.27496582e-01
  7.05394632e+00  4.08545789e+01  8.84875112e+01  1.32637665e+02
  1.57255989e+02  1.53393461e+02  1.22454150e+02  7.56848253e+01
  3.00866351e+01  2.23500697e+00  2.25430426e+00  3.01375122e+01
  7.57487878e+01  1.22507947e+02  1.53417536e+02  1.57241592e+02
  1.32590028e+02  8.84239513e+01  4.07982008e+01  7.02524409e+00
 -6.18089412e-01  2.06466335e+01  6.30894595e+01  1.11281969e+02
  1.47705672e+02  1.59120165e+02  1.41376156e+02  1.00923784e+02
  5.24679154e+01  1.36227750e+01 -1.49101484e+00  1.26205694e+01
  5.08278165e+01]
```

```python
#Plotting the series with forecasts:
plt.figure(figsize=(12, 6))
time_all = np.arange(1, n + k + 1)
plt.plot(time_all, yhat, label='Extended Series (yhat)', color='C0')
plt.plot(range(1, n + 1), y, label='Original Data', color='C1')
plt.plot(range(n + 1, n + k + 1), predvalues, label='Forecasts', color='blue')
plt.axvline(x=n, color='black', linestyle='--', label='Forecast Start')
#plt.axhline(y=np.mean(y), color='gray', linestyle=':', label='Mean of Original Data')
plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Time Series + AR(p) Forecasts')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions above are perfectly sinusoidal. Because the cycles for the sunspots data are irregular and can have different periods, there is a danger that these perfectly sinusoidal predictions can get out of phase sometimes leading to loss of prediction accuracy.

Below, we simulate datasets using the Yule model.

```python
#Simulating from the Yule Model:
rng = np.random.default_rng(seed = 42)
sighat = np.sqrt(np.mean(yulemod.resid ** 2))
print(sighat)
fig, axes = plt.subplots(3, 3, figsize = (12, 6))
axes = axes.flatten()
for j in range(1):
    ysim = y.copy()
    for i in range(2, n):
        err = rng.normal(loc = 0, scale = sighat, size = 1)
        ysim[i] = yulemod.params[0] + yulemod.params[1] * ysim[i-1] - ysim[i-2] + err[0]
    axes[j].plot(ysim)
axes[1].plot(y)
for j in range(2, 9):
    ysim = y.copy()
    for i in range(2, n):
        err = rng.normal(loc = 0, scale = sighat, size = 1)
        ysim[i] = yulemod.params[0] + yulemod.params[1] * ysim[i-1] - ysim[i-2] + err[0]
    axes[j].plot(ysim)
plt.show()
```

```
27.778317980024667
```

*(1 figure omitted — see the original notebook.)*

The sunspots dataset still probably sticks out compared to the synthetic datasets. However, all these synthetic datasets are quite smooth just like the actual sunspots data. This plots shows that the two "sinusoid + noise" models described in  lecture are fundamentally different.

---

[← Dataset Two: House Price Data from FRED](02-dataset-two-house-price-data-from-fred.md) · [Up: contents](index.md) · [AR(2) Model →](04-ar-2-model.md)
