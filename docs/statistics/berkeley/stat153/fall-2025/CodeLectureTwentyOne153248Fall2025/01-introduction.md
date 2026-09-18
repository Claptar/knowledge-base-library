---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyOne153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyOne153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyOne153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

---
title: Moving Average Models
---

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

## Some simulations from the MA(1) model

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

---

[Up: contents](index.md) · [Sample ACF →](02-sample-acf.md)
