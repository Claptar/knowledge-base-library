---
title: Sample ACF
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwenty153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwenty153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Sample ACF

**Source:** [`CodeLectureTwenty153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwenty153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

There is an inbuilt function in statsmodels for plotting the sample_acf. Its use is demonstrated below. It gives identical answers to our computation.

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

To see that the inbuilt function gives answers identical to our calculation, we can do the following.

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

Given the data, we can fit the MA(1) using an inbuilt function. This inbuilt function more generally fits ARIMA models. $\text{order} = (0, 0, 1)$ in the code below refers to the MA(1) model. More generally, $\text{order} = (p, d, q)$ refers to the ARMA(p, q) model after d times differencing (we will explain this in detail later).

```python
from statsmodels.tsa.arima.model import ARIMA
mamod = ARIMA(y_ma_1, order = (0, 0, 1)).fit()
print(mamod.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  600
Model:                 ARIMA(0, 0, 1)   Log Likelihood                -843.763
Date:                Wed, 09 Apr 2025   AIC                           1693.526
Time:                        15:59:24   BIC                           1706.717
Sample:                             0   HQIC                          1698.661
                                - 600
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.0272      0.073     -0.371      0.711      -0.171       0.117
ma.L1          0.8212      0.022     36.511      0.000       0.777       0.865
sigma2         0.9732      0.056     17.274      0.000       0.863       1.084
===================================================================================
Ljung-Box (L1) (Q):                   3.80   Jarque-Bera (JB):                 0.37
Prob(Q):                              0.05   Prob(JB):                         0.83
Heteroskedasticity (H):               0.91   Skew:                            -0.06
Prob(H) (two-sided):                  0.51   Kurtosis:                         2.99
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

The estimate of $\theta$ is 0.8212 (which is close to the actual value of 0.8). The estimate of $\mu$ is $-0.0272$ (which is close to the actual value of 0), and the estimate of $\sigma$ is $0.9732$ which is also close to the actual value of 1. We shall later how these point estimates (as well as standard errors) are actually calculated.

MA models can be used for actual time series. To illustrate this, we give two examples of real data.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Varve Dataset →](03-varve-dataset.md)
