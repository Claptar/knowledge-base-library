---
title: Stat 153/248 - Lecture 16
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture16.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture16.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture16.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture16.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Stat 153/248 - Lecture 16

Here we will have some demos of autoregression.

```python
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf

plt.rcParams.update({
    'figure.figsize': (12, 4),
    'font.size': 14,
    'axes.titlesize': 16,
    'axes.labelsize': 14,
})

rng = np.random.default_rng(42)
```

Let's look at some example time series below. Which of these seems to have "memory" (i.e. where $x_t$ depends on its past values?)

```python
n = 300

# A
#series_a = rng.standard_normal(n)
series_a = np.zeros(n)
for t in range(1, n):
    series_a[t] = 0.5 * series_a[t-1] + rng.standard_normal()


# B: AR(1) with phi = 0.9
series_b = np.zeros(n)
for t in range(1, n):
    series_b[t] = 0.9 * series_b[t-1] + rng.standard_normal()

# C: random walk (unit root)
#series_c = np.cumsum(rng.standard_normal(n))
# D: AR(1) with phi = -0.8 (oscillatory)
series_c = np.zeros(n)
for t in range(1, n):
    series_c[t] = -0.3 * series_c[t-1] + rng.standard_normal()


# D: AR(1) with phi = -0.8 (oscillatory)
series_d = np.zeros(n)
for t in range(1, n):
    series_d[t] = -0.8 * series_d[t-1] + rng.standard_normal()

fig, axes = plt.subplots(2, 2, sharex=True)
for ax, series, label in zip(axes.flat,
                              [series_a, series_b, series_c, series_d],
                              ['Series A', 'Series B', 'Series C', 'Series D']):
    ax.plot(series, lw=0.8)
    ax.set_title(label)
    ax.set_ylabel('$X_t$')
axes[1, 0].set_xlabel('Time')
axes[1, 1].set_xlabel('Time')
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Simulating different AR(1) models

Let's simulate AR(1) processes with different values of $\phi$ and see what happens. If we increase $\phi$ from 0.5 to 0.95, what do you expect to change about the series?

```python
phi_values = [0.0, 0.5, 0.7, 0.99]
n = 500
w = rng.standard_normal(n)  # same shocks for all — isolate effect of phi

fig, axes = plt.subplots(len(phi_values), 1, figsize=(10, 6), sharex=True)

for ax, phi in zip(axes, phi_values):
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = phi * x[t-1] + w[t]
    ax.plot(x, lw=0.7)
    ax.set_title(f'AR(1), $\\phi = {phi}$', loc='left')
    ax.set_ylabel('$X_t$')

axes[-1].set_xlabel('Time')
plt.tight_layout()
plt.savefig('images/16_AR1_phi.png')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[Up: contents](index.md) · [Properties of the AR(1) model →](02-properties-of-the-ar-1-model.md)
