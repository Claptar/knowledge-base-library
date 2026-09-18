---
title: Sample ACF
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Sample ACF

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

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Varve Dataset →](03-varve-dataset.md)
