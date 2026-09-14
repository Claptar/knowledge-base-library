---
title: LSTM Neural Network Models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab14.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# LSTM Neural Network Models

**Source:** [`Lab14.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from statsmodels.tsa.ar_model import AutoReg
import statsmodels.api as sm
```

The following dataset is simulated according to the model:
\begin{equation*}
   y_t = 0.9 \sin (0.5\pi y_{t - p}) + \epsilon_t
\end{equation*}
for some fixed $p$. This equation is for $t \geq p+1$. For $t \leq p$, we take $y_t$ to be linear. We take $p$ to be a large value.

```python
n = 1500
truelag = 85
rng = np.random.default_rng(seed=0)
#sig_noise = 0.05
sig_noise = 0.01

eps = rng.normal(loc=0, scale=sig_noise, size=n)
y_sim = np.full(shape=n, fill_value=-999.0)
y_sim[0:truelag] = np.linspace(-1, 1, truelag)
for i in range(truelag, n):
    y_sim[i] = 0.9 * np.sin(0.5 * np.pi * y_sim[i - truelag]) + eps[i]
#y_sim = y_sim + eps

plt.figure(figsize = (12, 6))
plt.plot(y_sim)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us obtain predictions for future values using the actual function $g(y) = 0.9 \sin(0.5 \pi y)$ from which the data were generated. These predictions (which we can refer to as Oracle Predictions) will form the benchmark which we can use to compare the predictions of various methods (AR, LSTM, RNN, GRU).

```python

---

[Up: contents](index.md) · [Oracle Predictions →](02-oracle-predictions.md)
