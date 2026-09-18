---
title: MA(2) model
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# MA(2) model

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

# Plot the simulated series
plt.plot(y, color='black')
plt.title("Manually Simulated MA(2) Process (θ₁=0.2, θ₂=0.2)")
plt.xlabel("Time")
plt.ylabel("y_t")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
h_max = 50
fig, ax = plt.subplots()
plot_acf(y, lags = h_max, ax = ax)
ax.set_title("Sample ACF of log differenced varve series")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Fitting MA models using the ARIMA function](04-fitting-ma-models-using-the-arima-function.md) · [Up: contents](index.md) · [GDP Growth Rate Data →](06-gdp-growth-rate-data.md)
