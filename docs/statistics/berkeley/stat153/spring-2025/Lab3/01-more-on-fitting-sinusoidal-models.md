---
title: More on fitting sinusoidal models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab3.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab3.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# More on fitting sinusoidal models

**Source:** [`Lab3.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab3.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
```

## Estimating Frequency in a Simulated Dataset

Consider the following dataset simulated using the model:
\begin{equation*}
    y_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin( 2 \pi f t) + \epsilon_t,
\end{equation*}
for $t = 1, \dots, n$ with some fixed values of $f, \beta_0, \beta_1, \beta_2$ and $\sigma$. The goal of this problem is to estimate $f$ along with associated uncertainty quantification.

```python
f = 0.2
#f = 1.8
n = 400
b0 = 0
b1 = 3
b2 = 5
sig = 10

rng = np.random.default_rng()
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

The frequentist solution calculates the MLE. For computing the MLE, we first optimize the following criterion function over $f$ to obtain $\hat{f}$:
\begin{equation*}
   \text{crit}(f) := \min_{\beta_0, \beta_1, \beta_2} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 \cos(2 \pi f t) - \beta_2 \sin(2 \pi f t))^2 = RSS(f),
\end{equation*}
where $RSS(f)$ denotes the Residual Sum of Squares in the linear regression model obtaining by fixing $f$. After finding $\hat{f}$, the MLEs for the other parameters are obtained as in standard linear regression with $f$ fixed at $\hat{f}$.

```python
def crit(f):
    x = np.arange(1, n + 1)
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([np.ones(n), xcos, xsin])

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    return rss
```

Here is a plot of $\text{crit}(f)$ as a function of $f$ over a grid of values of $f$.

```python
ngrid = 100000
allfvals = np.linspace(0, 0.5, ngrid)
critvals = np.array([crit(f) for f in allfvals])
```

```python
plt.plot(allfvals, critvals)
plt.xlabel('Frequency')
plt.ylabel('Sum of Squares')
plt.title('Least Squares Criterion Function')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python

---

[Up: contents](index.md) · [the MLE of f is now calculated as →](02-the-mle-of-f-is-now-calculated-as.md)
