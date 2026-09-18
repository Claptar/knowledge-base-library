---
title: ACF and PACF of ARMA processes
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureTwentyTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# ACF and PACF of ARMA processes

```python
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
from statsmodels.tsa.ar_model import AutoReg
```

Today we shall first look at the theoretical ACF and PACF functions of ARMA processes. The key observation is this: (a) For MA($q$), the ACF becomes zero for $h > q$. (b) For AR($p$), the PACF becomes zero for $h > p$. (c) For ARMA(p, q) with both $p, q \geq 1$, neither the ACF nor the PACF becomes zero after a finite lag. In this case, determining $p$ and $q$ by looking at the ACF and PACF alone is difficult.

In the code below, we are using the statsmodels functions arma_acf and arma_pacf below to compute the ACF and PACF. Different ARMA  processes are obtained by changing the ma_coeffs and ar_coeffs in the code below.

```python
from statsmodels.tsa.arima_process import ArmaProcess, arma_acf, arma_pacf
```

```python
#MA(1)
#th = 0.8
#ma_coeffs = [1]
#ma_coeffs = [1, 0, 0, 0, th]
ma_coeffs = [1, th]
#ma_coeffs = [1, 0.8, 0.6]
ph = 0.8
#ph = -0.8
ar_coeffs = [1]
ar_coeffs = [1, -ph] #these are the coefficients of the AR polynomial (note the sign changes)
#ar_coeffs = [1, -0.5, 0.25]
#ar_coeffs = [1, 0, 0, 0, -ph]
#th2 = 0.8
#ma_coeffs = [1, th, th2]
L = 20
corrs = arma_acf(ar = ar_coeffs, ma = ma_coeffs, lags = L)
par_corrs = arma_pacf(ar = ar_coeffs, ma = ma_coeffs, lags = L)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 5))
ax1.stem(range(L), corrs)
ax1.set(title = 'Theoretical ACF', xlabel = 'Lag h', ylabel = 'Autocorrelation')
ax1.axhline(0, lw = 0.5)
ax1.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

ax2.stem(range(L), par_corrs)
ax2.set(title = 'Theoretical PACF', xlabel = 'Lag h', ylabel = 'Partial Autocorrelation')
ax2.axhline(0, lw = 0.5)
ax2.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[Up: contents](index.md) · ARMA($p$, $q$) models for the GNP dataset →
