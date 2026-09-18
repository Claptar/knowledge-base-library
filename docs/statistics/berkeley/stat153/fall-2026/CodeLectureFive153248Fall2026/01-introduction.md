---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFive153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureFive153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureFive153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFive153248Fall2026.ipynb) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

---
title: Linear Regression and Uncertainty Quantification
---

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
```

## Squares Function Plotting

Given some data $y_1, \dots, y_n$ that are not all equal, consider the squares function:
\begin{align*}
   S(\theta) := \sum_{i=1}^n (y_i - \theta)^2.
\end{align*}
This function will be minimized at $\hat{\theta} = (y_1 + \dots + y_n)/n$. The code below plots this function for some data $y_1, \dots, y_n$.

```python
y = np.array([1, 0, 2, -2, 5])
theta_hat = np.mean(y)
#Below is the squares function S(theta) := sum_i (y_i - theta)^2
def S(theta):
    return np.sum((y - theta)**2)
```

```python
# Plot S(theta)
theta = np.linspace(-10, 12, 500)
S_values = np.array([S(t) for t in theta])

plt.figure(figsize=(7, 5))
plt.plot(theta, S_values)
plt.axvline(theta_hat, linestyle="--", label=rf"$\hat{{\theta}}={theta_hat}$")
plt.scatter(theta_hat, S(theta_hat), zorder=3)

plt.xlabel(r"$\theta$")
plt.ylabel(r"$S(\theta)$")
plt.title(r"Squares Function $S(\theta)=\sum_i (y_i-\theta)^2$")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Next we plot the function $S(\hat{\theta})/S(\theta)$ as a function of $\theta$.

```python
# Plot S(theta_hat) / S(theta)
theta = np.linspace(-10, 12, 500)
ratio = np.array([S(theta_hat) / S(t) for t in theta])

plt.figure(figsize=(7, 5))
plt.plot(theta, ratio)
plt.axvline(theta_hat, linestyle="--",
            label=rf"$\hat{{\theta}}={theta_hat}$")
plt.scatter(theta_hat, 1, zorder=3)

plt.xlabel(r"$\theta$")
plt.ylabel(r"$S(\hat{\theta})/S(\theta)$")
plt.title(r"$S(\hat{\theta})/S(\theta)$")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Below we plot $\left(S(\hat{\theta})/S(\theta) \right)^m$ for $m \geq 1$. When $m$ becomes large, this function becomes quite sharply concentrated around $\hat{\theta}$.

```python
theta = np.linspace(-10, 12, 5000)

m = 50

ratio_1 = np.array([S(theta_hat) / S(t) for t in theta])
ratio_m = ratio_1**m

plt.figure(figsize=(7, 5))

plt.plot(theta, ratio_1, label=r"$m=1$")
plt.plot(theta, ratio_m, label=rf"$m={m}$")

plt.axvline(theta_hat, linestyle="--",
            label=rf"$\hat{{\theta}}={theta_hat}$")

plt.scatter(theta_hat, 1, zorder=3)

plt.xlabel(r"$\theta$")
plt.ylabel(r"$\left(S(\hat{\theta})/S(\theta)\right)^m$")
plt.title(r"$\left(S(\hat{\theta})/S(\theta)\right)^m$")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[Up: contents](index.md) · [Dataset One: US Population →](02-dataset-one-us-population.md)
