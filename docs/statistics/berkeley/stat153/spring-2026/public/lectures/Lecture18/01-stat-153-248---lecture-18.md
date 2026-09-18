---
title: Stat 153/248 - Lecture 18
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Stat 153/248 - Lecture 18

In this notebook we'll work through three real datasets that motivate why we need AR, MA, and ARMA models. We'll use the following datasets:

1. **Sunspot numbers**
2. **US gas prices**
3. **Heart rate variability (HRV)**

By the end, you should have an intuition for when each model class is appropriate and why ARMA exists as a modeling framework.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import warnings
warnings.filterwarnings('ignore')

# statsmodels imports
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox

import warnings
from statsmodels.tools.sm_exceptions import ConvergenceWarning
warnings.filterwarnings('ignore', category=ConvergenceWarning)

plt.rcParams.update({
    'figure.figsize': (12, 4),
    'axes.spines.top': False,
    'axes.spines.right': False,
    'font.size': 16,
})
```

---
## The AR Model - Sunspot Numbers

We've already seen this dataset in several contexts, which records the monthly mean number of sunspots from 1749 to the present. This series has a well-known ~11-year cycle.

```python
# Sunspot data is in the statsmodels package (as well as astsa, but here we don't need it!)
import statsmodels.api as sm
sunspots = sm.datasets.sunspots.load_pandas().data
sunspots.columns = ['year', 'sunspots']
sunspots = sunspots.set_index('year')

fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(sunspots.index, sunspots['sunspots'], linewidth=0.8)
ax.set(xlabel='Year', ylabel='Sunspot number', title='Yearly Sunspot Numbers (1700–2008)')
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Predict (pair discussion, 2 min)

Before we look at the ACF and PACF:

1. **What kind of autocorrelation structure do you expect?** Slowly decaying? Oscillating? Sharp cutoff?
2. **If you had to guess: AR, MA, or ARMA?** Why?
3. **How many parameters do you think you'd need?**

Write down your predictions before running the next cell.

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 4))

plot_acf(sunspots['sunspots'].dropna(), lags=40, ax=axes[0], title='ACF — Sunspots')
plot_pacf(sunspots['sunspots'].dropna(), lags=40, ax=axes[1], title='PACF — Sunspots', method='ywm')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[Up: contents](index.md) · [What do we see? →](02-what-do-we-see.md)
