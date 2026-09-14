---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwenty153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwenty153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureTwenty153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwenty153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Moving Average Models, ACF and PACF
---

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

Let us first simulate some data from the Gaussian white noise. After that, we will simulate data from the Moving Average models and compare them to the simulated white noise data.

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

Next we shall simulate observations from the MA(1) model: $y_t = \mu + \epsilon_t + \theta \epsilon_{t-1}$.

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

---

[Up: contents](index.md) · [Sample ACF →](02-sample-acf.md)
