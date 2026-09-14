---
title: AR models (estimation, inference and prediction)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabNine153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabNine153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# AR models (estimation, inference and prediction)

**Source:** [`CodeLabNine153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabNine153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.ar_model import AutoReg
```

## GNP Dataset

The following dataset is from FRED: https://fred.stlouisfed.org/series/GNP. This is a quarterly dataset (there are four quarters in each year).

```python
gnp = pd.read_csv("GNP_02April2025.csv")
print(gnp.head())

y = gnp['GNP']
plt.figure(figsize = (12, 6))
plt.plot(y, color = 'black')
plt.show()
```

```
observation_date      GNP
0       1947-01-01  244.142
1       1947-04-01  247.063
2       1947-07-01  250.716
3       1947-10-01  260.981
4       1948-01-01  267.133
```

*(1 figure omitted — see the original notebook.)*

Let us reserve the last 16 observations (corresponding to the most recent 4 years) for testing purposes. We shall fit models to the rest of the data, and then evaluate prediction accuracy on the last 16 observations.

```python
n = len(y)
tme = range(1, n+1)

n_test = 16

n_train = n - n_test
y_train = y[:n_train]
tme_train = tme[:n_train]
y_test = y[n_train:]
tme_test = tme[n_train:]
```

## Model One: AR(p) directly on the training data

As seen in class, AR(p) can be fit in two ways. Either by using the AutoReg function (from the library statsmodels), or by manually creating $y$ and $X$ and then running OLS. Both methods give identical parameter estimates. But the standard errors will be slightly different (also AutoReg will use $z$-scores while OLS uses $t$-scores). Below we fit the AR(2) model for the GNP data using both these methods, and compare the results obtained.

```python
p = 2
armod_sm = AutoReg(y_train, lags = p, trend = 'c').fit()

---

[Up: contents](index.md) · [trend = 'c' will fit the model →](02-trend-c-will-fit-the-model.md)
