---
title: More on Nonlinear Models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# More on Nonlinear Models

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

## Inference in Sinusoid Models

In the last lab, we studied the following problem. Consider the following dataset simulated using the model:
\begin{equation*}
    y_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin( 2 \pi f t) + \epsilon_t,
\end{equation*}
for $t = 1, \dots, n$ with some fixed values of $f, \beta_0, \beta_1, \beta_2$ and $\sigma$. The goal of this problem is to estimate $f$ along with associated uncertainty quantification.

Today we will start by addressing the problem of estimating the other parameters $\beta_0, \beta_1, \beta_2, \sigma$ also along with uncertainty quantification.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

```python
f = 0.2035
#f = 1.8
n = 400
b0 = 0
b1 = 3
b2 = 5
sig = 10

rng = np.random.default_rng(seed = 42)
errorsamples = rng.normal(loc = 0, scale = sig, size = n)
t = np.arange(1, n + 1)

y = b0 * np.ones(n) + b1 * np.cos(2 * np.pi * f * t) + b2 * np.sin(2 * np.pi * f * t) + errorsamples
```

```python
plt.figure(figsize = (10, 6))
plt.plot(y)
plt.xlabel('Time')
plt.ylabel('y')
plt.title('A simulated dataset')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

To obtain the MLEs of the parameters, we first obtain the MLE of $f$ (as before), then plug in $f = \hat{f}$, and run linear regression to estimate the other parameters.

```python
def rss(f):
    x = np.arange(1, n + 1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([np.ones(n), xcos, xsin])

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    return rss
```

```python

---

[Up: contents](index.md) · [We can minimize rss(f) over a fine grid of possible f values. →](02-we-can-minimize-rss-f-over-a-fine-grid-of-possible-f-values.md)
