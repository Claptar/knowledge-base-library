---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab14.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`Lab14.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab14.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

## LSTM Neural Network Models

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
# Oracle Predictions
n_future = 1000
y_extended = np.concatenate([y_sim, np.empty(n_future, dtype=float)])
for t in range(n, n+n_future):
    y_extended[t] = 0.9 * np.sin(0.5 * np.pi * y_extended[t - truelag])
oracle_preds = y_extended[n:]

n = len(y_sim)
tme = range(1, n+1)
tme_future = range(n+1, n+n_future+1)

plt.figure(figsize = (12, 6))
plt.plot(tme, y_sim, label = 'Data')
plt.plot(tme_future, oracle_preds, label = 'Forecast (Oracle)', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us now fit AR(p) to this data. Even if $p$ is taken to be the correct value, this model will not work well (because the actual function which generated the data is nonlinear).

```python
# Let us fit AR(p)
p = truelag
#p = 50
ar = AutoReg(y_sim, lags=p).fit()

n = len(y_sim)
tme = range(1, n+1)
tme_future = range(n+1, n+n_future+1)
fcast = ar.get_prediction(start=n, end=n+n_future-1).predicted_mean

plt.figure(figsize = (12, 7))
plt.plot(tme, y_sim, label = 'Data')
plt.plot(tme_future, oracle_preds, label = 'Forecast (Oracle)', color = 'lightgreen')
plt.plot(tme_future, fcast, label = 'Forecast (AR(p))', color = 'black')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The AR predictions seem to be "expanding" compared to the Oracle predictions.

```python
rmse_ar = np.sqrt(np.mean((fcast - oracle_preds)**2))
median_abs_error_ar = np.median(np.abs(fcast - oracle_preds))
print(rmse_ar)
print(median_abs_error_ar)
```

```
0.18216756914528526
0.1433347216860818
```

```python
mu, sig = y_sim.mean(), y_sim.std()
y_std = (y_sim - mu) / sig

X = torch.tensor(y_std[:-1], dtype=torch.float32)
Y = torch.tensor(y_std[1: ], dtype=torch.float32)

X = X.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)
Y = Y.unsqueeze(0).unsqueeze(-1)   # shape (1, seq_len, 1)

seq_len = X.size(1)
print(seq_len)
```

```
1499
```

---

[Up: contents](index.md) · [LSTM →](02-lstm.md)
