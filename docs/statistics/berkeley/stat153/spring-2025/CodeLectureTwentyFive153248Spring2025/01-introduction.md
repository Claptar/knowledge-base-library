---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyFive153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyFive153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureTwentyFive153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyFive153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import torch
import torch.nn as nn
import torch.optim as optim
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.ar_model import AutoReg
```

## Nonlinear AutoRegression

### Example One

We fit the NonLinear AR(1) model to a simulated dataset generated using the following equation:
\begin{equation*}
   y_t = \frac{2 y_{t-1}}{1 + 0.8 y_{t-1}^2} + \epsilon_t
\end{equation*}
where $\epsilon_t \overset{\text{i.i.d}}{\sim} \text{uniform}(-1, 1)$.

```python
n = 450
rng = np.random.default_rng(seed = 40)
eps = rng.uniform(low = -1.0, high = 1.0, size = n)

y_sim = np.full(n, 0, dtype = float)
for i in range(1, n):
    y_sim[i] = ((2*y_sim[i-1])/(1 + 0.8 * (y_sim[i-1] ** 2))) + eps[i]

plt.figure(figsize = (12, 6))
plt.plot(y_sim)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

This dataset is generated as $y_t = g(y_{t-1}) + \epsilon_t$ where $g(x) := 2x/(1 + 0.8 x^2)$. The function $g$ is plotted below.

```python
def g(x):
    return 2 * x / (1 + 0.8 * x**2)

x_vals = np.linspace(-2, 2, 400)
y_vals = g(x_vals)

---

[Up: contents](index.md) · [Plot the function →](02-plot-the-function.md)
