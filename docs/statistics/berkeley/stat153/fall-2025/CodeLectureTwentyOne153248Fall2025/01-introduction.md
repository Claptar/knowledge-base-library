---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Moving Average Models
---

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

### Some simulations from the MA(1) model

Below are some simulated data from the MA(1) model. Recall that the MA(1) model is:
\begin{align*}
   y_t = \mu + \epsilon_t + \theta \epsilon_{t-1}
\end{align*}
where $\epsilon_t$ is i.i.d $N(0, \sigma^2)$. Note that if $\theta = 0$, the model is just $\mu + \epsilon_t$ which is i.i.d $N(\mu, \sigma^2)$ so the standard i.i.d normal model is a special case of MA(1). Below is simulated data from i.i.d $N(\mu, \sigma^2)$ with $\mu = 0$ and $\sigma = 1$ (in other words, this is MA(1) with $\theta = 0, \mu = 0, \sigma = 1$). We call this the Gaussian White Noise.

```python
#Simulating from Gaussian white noise:
n = 600
seed = 43
rng = np.random.default_rng(seed)
sig = 1
y_wn = rng.normal(loc = 0, scale = sig, size = n)
plt.figure(figsize = (12, 6))
plt.plot(y_wn)
plt.xlabel('time')
plt.ylabel('Data')
plt.title('Simulated White Noise')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Next we shall simulate observations from the MA(1) model: $y_t = \mu + \epsilon_t + \theta \epsilon_{t-1}$ with non-zero $\theta$. These data will have some dependence between neighboring data points.

```python
#Simulating MA(1)
y_0 = np.concatenate(([0], y_wn))
theta = 0.8
y_ma = y_0[1:] + theta * y_0[:-1]
plt.figure(figsize = (12, 6))
plt.plot(y_ma)
plt.xlabel('time')
plt.ylabel('Data')
plt.title(f'Simulated MA(1) with theta = {theta: .2f}')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Here is a scatter plot of y_t vs y_{t-1} for the simulated MA(1) data
plt.scatter(y_ma[:-1], y_ma[1:], s = 10, color = 'black')
plt.xlabel('$y_{t-1}$')
plt.ylabel('$y_{t}$')
plt.title(f'Scatter plot of $y_t$ vs $y_{{t-1}}$ for Simulated MA(1) with theta = {theta: .2f}')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

This positive dependence between $y_t$ and $y_{t-1}$ will make the simulated dataset look smoother compared to white noise. On the other hand, if $\theta < 0$, then the simulated dataset will look more rough compared to white noise.

Below we plot the white noise observations, together with the simulated MA(1) observations for $\theta = 0.8$ and $\theta = -0.8$. When $\theta > 0$, the autocorrelation at lag one is positive making the data look smoother (compared to white noise). When $\theta < 0$, the autocorrelation at lag one is negative making the data look more wiggly (compared to white noise).

```python
fig, axes = plt.subplots(nrows = 3, ncols = 1, figsize = (12, 6))


axes[0].plot(y_wn)
axes[0].set_title('Simulated White Noise')

theta = 0.8
y_ma_1 = y_0[1:] + theta * y_0[:-1]
axes[1].plot(y_ma_1)
axes[1].set_title(f'Simulated MA(1) with theta = {theta: .2f}')

theta = -0.8
y_ma_2 = y_0[1:] + theta * y_0[:-1] #y_ma_2 is simulated data from MA(1) with negative theta
axes[2].plot(y_ma_2)
axes[2].set_title(f'Simulated MA(1) with theta = {theta: .2f}')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Sample ACF

We can distinguish between these datasets by computing the sample ACF which is defined as follows. Given a time series dataset $y_1, \dots, y_n$ and a **lag** h, define
\begin{equation}
   r_h := \frac{\sum_{t=1}^{n-h} (y_t - \bar{y})(y_{t+h} - \bar{y})}{\sum_{t=1}^n (y_t - \bar{y})^2}
\end{equation}
for $h = 0, 1, 2, \dots$. Here $\bar{y}$ is simply the mean of $z_1, \dots, z_n$. The acf plot graphs $h$ on the x-axis and $r_h$ on the y-axis. The quantity $r_h$ is known as the **sample autocorrelation** of the data at lag $h$ (acf stands for "Autocorrelation Function").

Below we compute the sample ACF.

```python
def sample_acf(y, h_max):
    n = len(y)
    y_mean = sum(y) / n
    denominator = sum((y_t - y_mean) ** 2 for y_t in y)
    autocorr = []

    for h in range(h_max + 1):
        numerator = sum((y[t] - y_mean) * (y[t + h] - y_mean) for t in range(n - h))
        r_h = numerator / denominator
        autocorr.append(r_h)

    return autocorr

h_max = 50
sample_acf_vals = sample_acf(y_wn, h_max)
print(sample_acf_vals[0]) #the sample_acf at lag = 0 always equals 1
plt.plot(range(0, h_max + 1), sample_acf_vals)
plt.show()
```

```
1.0
```

*(1 figure omitted — see the original notebook.)*

Visually, one gets nicer plots for the sample ACF by using the stem plot.

```python
h_max = 50
sample_acf_vals = sample_acf(y_wn, h_max)
plt.figure(figsize = (12, 6))
markerline, stemline, baseline = plt.stem(range(0, h_max + 1), sample_acf_vals)
markerline.set_marker("None")
plt.title('Sample AutoCorrelation')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Note that the sample ACF always takes the value 1 at $h = 0$ so the first spike is not giving us any information. We only look at the sample ACF for lages $h \geq 1$. From the above ACF plot, it appears that sample ACF values at all $h \geq 1$ are negligible.

Next we plot the sample ACF for MA(1) for positive as well as negative $\theta$.

```python
h_max = 50
sample_acf_vals = sample_acf(y_ma_1, h_max)
plt.figure(figsize = (12, 6))
markerline, stemline, baseline = plt.stem(range(0, h_max + 1), sample_acf_vals)
markerline.set_marker("None")
plt.title('Sample AutoCorrelation')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Observe the peak at lag one above. This is indicative of the MA(1) model.

```python
fig, axes = plt.subplots(nrows = 3, ncols = 1, figsize = (12, 6))

sample_acf_vals_wn = sample_acf(y_wn, h_max)
markerline, stemline, baseline = axes[0].stem(range(0, h_max + 1), sample_acf_vals_wn)
markerline.set_marker("None")
axes[0].set_title('Sample ACF of Simulated White Noise')

sample_acf_vals_ma_1 = sample_acf(y_ma_1, h_max)
markerline, stemline, baseline = axes[1].stem(range(0, h_max + 1), sample_acf_vals_ma_1)
markerline.set_marker("None")
theta = 0.8
axes[1].set_title(f'Simulated ACF of MA(1) with theta = {theta: .2f}')

sample_acf_vals_ma_2 = sample_acf(y_ma_2, h_max)
markerline, stemline, baseline = axes[2].stem(range(0, h_max + 1), sample_acf_vals_ma_2)
markerline.set_marker("None")
theta = -0.8
axes[2].set_title(f'Simulated ACF of MA(1) with theta = {theta: .2f}')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Clearly, there are spikes at lag one for the second and third datasets. The remaining ACF values are negligible.

There is an inbuilt function in statsmodels for plotting the sample_acf (and another inbuilt function for plotting the sample_acf). Its use is demonstrated below. Let us check that it gives identical answers to our computation.

```python
from statsmodels.tsa.stattools import acf

acf_values_wn = acf(y_wn, nlags=h_max)
print(np.column_stack([sample_acf_vals_wn, acf_values_wn]))
```

```
[[ 1.00000000e+00  1.00000000e+00]
 [-6.18986853e-02 -6.18986853e-02]
 [-3.16190776e-02 -3.16190776e-02]
 [ 3.37684035e-02  3.37684035e-02]
 [-5.08194511e-02 -5.08194511e-02]
 [ 3.25331941e-02  3.25331941e-02]
 [ 8.74858962e-03  8.74858962e-03]
 [-1.16498128e-02 -1.16498128e-02]
 [ 3.26472220e-02  3.26472220e-02]
 [ 8.33178480e-02  8.33178480e-02]
 [-3.27430872e-02 -3.27430872e-02]
 [ 1.14743957e-02  1.14743957e-02]
 [-6.46748355e-02 -6.46748355e-02]
 [-9.26355222e-03 -9.26355222e-03]
 [-1.48030902e-03 -1.48030902e-03]
 [ 5.98188096e-03  5.98188096e-03]
 [-4.20248527e-02 -4.20248527e-02]
 [ 5.47736551e-02  5.47736551e-02]
 [ 9.57612253e-03  9.57612253e-03]
 [-5.55307936e-02 -5.55307936e-02]
 [ 7.32655261e-02  7.32655261e-02]
 [ 8.66336997e-03  8.66336997e-03]
 [ 5.21590566e-02  5.21590566e-02]
 [-1.51121264e-02 -1.51121264e-02]
 [-2.06604710e-02 -2.06604710e-02]
 [-2.69178655e-02 -2.69178655e-02]
 [ 3.49261541e-02  3.49261541e-02]
 [ 3.86381603e-02  3.86381603e-02]
 [-2.07370593e-02 -2.07370593e-02]
 [ 3.56664414e-02  3.56664414e-02]
 [ 3.73042789e-02  3.73042789e-02]
 [-1.58643239e-03 -1.58643239e-03]
 [-2.62720921e-02 -2.62720921e-02]
 [-7.90709599e-03 -7.90709599e-03]
 [ 1.72123791e-02  1.72123791e-02]
 [ 1.64248945e-02  1.64248945e-02]
 [-4.29481074e-02 -4.29481074e-02]
 [-4.08484611e-02 -4.08484611e-02]
 [ 2.76715612e-02  2.76715612e-02]
 [-1.97488528e-02 -1.97488528e-02]
 [ 2.31475734e-03  2.31475734e-03]
 [-4.12288416e-02 -4.12288416e-02]
 [-1.05493982e-03 -1.05493982e-03]
 [-1.60649886e-02 -1.60649886e-02]
 [ 8.55000861e-06  8.55000861e-06]
 [-2.36297467e-02 -2.36297467e-02]
 [ 6.36622276e-02  6.36622276e-02]
 [ 3.89111470e-02  3.89111470e-02]
 [ 1.70688163e-02  1.70688163e-02]
 [ 5.94731208e-02  5.94731208e-02]
 [-1.23706214e-02 -1.23706214e-02]]
```

The following function plots the sample_acf values.

```python
from statsmodels.graphics.tsaplots import plot_acf
fig, axes = plt.subplots(nrows = 3, ncols = 1, figsize = (12, 6))

sample_acf_vals_wn = sample_acf(y_wn, h_max)
plot_acf(y_wn, lags = h_max, ax = axes[0])
axes[0].set_title('Sample ACF of Simulated White Noise')

sample_acf_vals_ma_1 = sample_acf(y_ma_1, h_max)
plot_acf(y_ma_1, lags = h_max, ax = axes[1])
theta = 0.8
axes[1].set_title(f'Simulated ACF of MA(1) with theta = {theta: .2f}')

sample_acf_vals_ma_2 = sample_acf(y_ma_2, h_max)
plot_acf(y_ma_2, lags = h_max, ax = axes[2])
theta = -0.8
axes[2].set_title(f'Simulated ACF of MA(1) with theta = {theta: .2f}')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

There are also real datasets whose sample ACF displays the above MA(1) behavior. Here is one example.

## Varve Dataset

This dataset is from the Shumway and Stoffer book. It records the thickness of yearly glacial varves—layers of sediment deposited by melting glaciers—collected from a single site in Massachusetts. Each varve represents one year of sedimentation, formed when meltwater streams carried sand and silt into a glacial lake during the spring and summer melt seasons at the end of the last Ice Age. The dataset contains 634 annual measurements, covering a continuous period that began about 11,834 years ago, when the glaciers in New England were retreating. Thicker varves indicate warmer years with more melting and heavier sediment flow, while thinner varves reflect colder years with less melting. Although these deposits stopped forming thousands of years ago when the glacial lake drained, the preserved layers now provide scientists with a high-resolution record of past climate variations, helping reconstruct temperature and melting patterns during the planet’s transition out of the Ice Age.

See Example 2.6 of the Shumway-Stoffer book, 4th edition, for more details on the dataset.

```python
varve_data = pd.read_csv("varve.csv")
yraw = varve_data['x']
plt.plot(yraw)
plt.xlabel('Time')
plt.ylabel('Thickness')
plt.title('Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We shall work with the logarithms of the raw data.

```python
#We shall work with the logarithms:
ylog = np.log(yraw)
plt.plot(ylog)
plt.xlabel('Time')
plt.ylabel('log(Thickness)')
plt.title('Logarithm of Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Fitting a stationary model such as MA($q$) is not appropriate for the logarithmed data. This is because the data does not seem to have constant mean. To deal with this, we difference the data as follows.

```python
ylogdiff = np.diff(ylog)
plt.plot(ylogdiff)
plt.xlabel('Time')
plt.ylabel('diff(log(Thickness))')
plt.title('Differenced Logarithm of Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now let us look at the sample acf of this dataset.

```python
h_max = 50
fig, ax = plt.subplots()
plot_acf(ylogdiff, lags = h_max, ax = ax)
ax.set_title("Sample ACF of log differenced varve series")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is clear that the sample ACF shows one negative nonnegligible spike at lag one.  The other spikes seem insignificant. This is MA(1) behaviour which suggests that the MA(1) should be appropriate for this data (which is differenced logarithms of the varve data).

## Fitting MA models using the ARIMA function

Fitting MA models to data is more complicated compared to AR models. We use an inbuilt function in statsmodels called ARIMA for this. ARIMA models (which we will define later) are determined by three orders $(p, d, q)$. $p$ denotes the AR order, $q$ denotes the MA order, and $d$ denotes differencing. To fit the MA(1) model, we take $p = 0, d = 0$ and $q = 1$.

```python
from statsmodels.tsa.arima.model import ARIMA
mamod = ARIMA(ylogdiff, order = (0, 0, 1)).fit()
print(mamod.summary())
print(mamod.params)
mu_hat = mamod.params[0]
theta_hat = mamod.params[1]
sigma_hat = np.sqrt(mamod.params[2])
print(f"mu_hat = {mu_hat: .4f}, theta_hat = {theta_hat: .4f}, sigma_hat = {sigma_hat: .4f}")
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  633
Model:                 ARIMA(0, 0, 1)   Log Likelihood                -440.678
Date:                Sat, 15 Nov 2025   AIC                            887.356
Time:                        22:14:29   BIC                            900.707
Sample:                             0   HQIC                           892.541
                                - 633
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.0013      0.004     -0.280      0.779      -0.010       0.008
ma.L1         -0.7710      0.023    -33.056      0.000      -0.817      -0.725
sigma2         0.2353      0.012     18.881      0.000       0.211       0.260
===================================================================================
Ljung-Box (L1) (Q):                   9.16   Jarque-Bera (JB):                 7.58
Prob(Q):                              0.00   Prob(JB):                         0.02
Heteroskedasticity (H):               0.95   Skew:                            -0.22
Prob(H) (two-sided):                  0.69   Kurtosis:                         3.30
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
[-0.00125667 -0.77099236  0.23528045]
mu_hat = -0.0013, theta_hat = -0.7710, sigma_hat =  0.4851
```

This ARIMA function can be applied on the log varve data also, instead of first differencing and then applying it on the differenced log data. If we are not using differencing data, we have to use d = 1 in the ARIMA function (i.e., $(p, d, q)
$  = $(0, 1, 1)$).

```python
mamod_ylog = ARIMA(ylog, order = (0, 1, 1)).fit()
print(mamod_ylog.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      x   No. Observations:                  634
Model:                 ARIMA(0, 1, 1)   Log Likelihood                -440.718
Date:                Sat, 15 Nov 2025   AIC                            885.435
Time:                        22:14:30   BIC                            894.336
Sample:                             0   HQIC                           888.892
                                - 634
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ma.L1         -0.7705      0.023    -32.948      0.000      -0.816      -0.725
sigma2         0.2353      0.012     19.124      0.000       0.211       0.259
===================================================================================
Ljung-Box (L1) (Q):                   9.10   Jarque-Bera (JB):                 7.59
Prob(Q):                              0.00   Prob(JB):                         0.02
Heteroskedasticity (H):               0.95   Skew:                            -0.22
Prob(H) (two-sided):                  0.69   Kurtosis:                         3.30
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Note now that there is no constant. This ARIMA function, by default, fits $y_t = \epsilon_t + \theta \epsilon_{t-1}$ (with no $\mu$ i.e., with $\mu = 0$) if the differencing order is strictly positive.

## MA(2) model


The MA(2) model is: $y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2}$. For this dataset, there are autocorrelations between $y_t$ and $y_{t-1}$ as well as between $y_t$ and $y_{t-2}$. To understand these autocorrelations, we can look at the theoretical ACF of MA(2).

```python
from statsmodels.tsa.arima_process import arma_acf
ar = [1]
ma = [1, 0.2, 0.2] #this is for MA(2) with theta_1 = 0.2 and theta_2 = 0.2
lag_max = 50
acf_vals = arma_acf(ar, ma, lags = lag_max)
print(acf_vals)
plt.stem(range(len(acf_vals)), acf_vals)
plt.xlabel("Lag")
plt.ylabel("ACF")
plt.title("Theoretical ACF of MA(2)")
plt.show()
```

```
[1.         0.22222222 0.18518519 0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.        ]
```

*(1 figure omitted — see the original notebook.)*

If we simulate data from this MA(2) model, the resulting data will have a sample ACF that looks like a noisy version of the above theoretical ACF.

```python
theta1 = 0.2
theta2 = 0.2
n = 500
#First generate \epsilon_t
np.random.seed(42)
eps = np.random.normal(0, 1, n+2)

y = np.zeros(n)
for t in range(2, n+2):
    y[t-2] = eps[t] + theta1 * eps[t-1] + theta2 * eps[t-2]

---

[Up: contents](index.md) · [Plot the simulated series →](02-plot-the-simulated-series.md)
