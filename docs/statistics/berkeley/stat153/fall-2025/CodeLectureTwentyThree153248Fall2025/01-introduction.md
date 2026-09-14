---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyThree153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureTwentyThree153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: ARIMA and SARIMA models
---

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_process import ArmaProcess, arma_acf, arma_pacf
from statsmodels.tsa.arima.model import ARIMA
```

## co2 dataset (Motivation for Multiplicative Seasonal ARMA models)

Next we study seasonal and multiplicative seasonal ARMA models. The following dataset provides some motivation for considering these models.

```python
co2 = pd.read_csv('co2_TSA.csv')
print(co2)
#This is a simple time series dataset from the R package TSA
#TSA is an R package that is written by the authors of the book "Time Series Analysis with Applications in R (second edition)"
#by Jonathan Cryer and Kung-Sik Chan
#This dataset gives the monthly co2 levels in Alert, Canada from January 1994 to December 2004 (132 observations in total for 11 years)
y = co2['x']
#plt.figure(figsize = (12, 7))
plt.plot(y)
plt.xlabel('Time (months)')
plt.ylabel('co2 level')
plt.title('Monthly co2 levels in Alert, Canada')
plt.show()
```

```
Unnamed: 0       x
0             1  363.05
1             2  364.18
2             3  364.87
3             4  364.47
4             5  364.32
..          ...     ...
127         128  368.69
128         129  368.55
129         130  373.39
130         131  378.49
131         132  381.62

[132 rows x 2 columns]
```

*(1 figure omitted — see the original notebook.)*

```python
ydiff = y.diff()
plt.plot(ydiff)
plt.xlabel('Time (months)')
plt.ylabel('Differenced co2 level')
plt.title('Differenced Monthly co2 levels in Alert, Canada')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Before fitting stationary ARMA models, we first preprocess the data by differencing. We first take the seasonal difference: $\nabla_s y_t = y_t - y_{t-s}$ where $s = 12$.

```python
#Seasonal differencing: y_t - y_{t-12}
ydiff12 = y.diff(periods = 12) #this works when y is a pandas series (it will not work when y is a np array for example)
#plt.figure(figsize = (12, 7))
plt.plot(ydiff12)
plt.xlabel('Time (months)')
plt.ylabel('value')
plt.title('Seasonal Differences of Monthly co2 levels in Alert, Canada')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Note that there will be NAs corresponding to the first 12 observations. The presence of these NAs might cause issues with subsequent functions (such as plot_acf and plot_pacf).

```python
#there will be NAs in the first twelve entries of ydiff12
print(ydiff12)
```

```
0       NaN
1       NaN
2       NaN
3       NaN
4       NaN
       ...
127    0.72
128    0.00
129    1.11
130    0.74
131    1.63
Name: x, Length: 132, dtype: float64
```

Below we use '.dropna()' to remove NAs before plotting ACF and PACF.

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))
plot_acf(ydiff12.dropna(), lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF")
axes[0].set_xticks([0, 1, 2, 3, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 36, 48])
plot_pacf(ydiff12.dropna(), lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF")
axes[1].set_xticks([0, 1, 2, 3, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 36, 48])
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Based on the plot of $\nabla_s y_t$, it appear that there are still some trends in the dataset. So we difference one more time before fitting stationary models.

```python
#We now take one more differencing; this time regular differencing
y2d = ydiff12.diff()
plt.figure(figsize = (12, 7))
plt.plot(y2d)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The sample ACF and PACF of this data is plotted using the code below.

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))
plot_acf(y2d.dropna(), lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF")
axes[0].set_xticks([0, 1, 2, 3, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 36, 48])
plot_pacf(y2d.dropna(), lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF")
axes[1].set_xticks([0, 1, 2, 3, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 36, 48])
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The ACF has a large negative autocorrelation at lag one, and then a bunch of small autocorrelations followed by nonnegligible ones at lags 11, 12, 13. If we want to use an MA(q) model here, then $q = 13$ would be reasonable. But that model will have quite a few parameters. It would be preferable to have a simpler MA model with fewer parameters that has an ACF similar to the above sample ACF. To get such a model, we need to learn about seasonal and multiplicative seasonal ARMA models.

## Seasonal ARMA models

Seasonal ARMA models are given by $\phi(B^s) (y_t - \mu) = \theta(B^s) \epsilon_t$. These are special cases of regular ARMA models with lots of zeros in the AR and MA coefficients. For example, the seasonal MA(1) model with period $s = 4$ is $y_t = \mu + \epsilon_t + \theta \epsilon_{t-4}$ which is also a regular MA(4) model with coefficients $\theta_1 = \theta_2 = \theta_3 = 0$ and $\theta_4 = \theta$. The following code is the same as that used previously to compute the ACF and PACF of ARMA processes. By inputting a bunch of zeros in ma_coeffs and ar_coeffs, we can obtain the ACF and PACF of seasonal ARMA models.

```python
#AR(1)
th = 0.8
#ma_coeffs = [1, 0, 0, 0, th] #this corresponds to seasonal MA with period = 4
ma_coeffs = [1]
#ma_coeffs = [1, th]
#ph = 0.8
#ar_coeffs = [1]
#ar_coeffs = [1, -ph]
ar_coeffs = [1, 0, 0, 0, -ph] #this corresponds to seasonal AR with period = 4
#th2 = 0.8
#ma_coeffs = [1, th, th2]
L = 20
corrs = arma_acf(ar = ar_coeffs, ma = ma_coeffs, lags = L)
par_corrs = arma_pacf(ar = ar_coeffs, ma = ma_coeffs, lags = L)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 5))
ax1.stem(range(L), corrs)
ax1.set(title = 'Theoretical ACF', xlabel = 'Lag h', ylabel = 'Autocorrelation')
ax1.axhline(0, lw = 0.5)
ax1.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

ax2.stem(range(L), par_corrs)
ax2.set(title = 'Theoretical PACF', xlabel = 'Lag h', ylabel = 'Partial Autocorrelation')
ax2.axhline(0, lw = 0.5)
ax2.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The ACF and PACF of a seasonal ARMA model is non-zero only at the seasonal lags $h = 0, s, 2s, 3s, 4s, \dots$. At these seasonal lags, the ACF and PACF exactly equal those of the non-seasonal ARMA.

```python

---

[Up: contents](index.md) · [Simulate data →](02-simulate-data.md)
