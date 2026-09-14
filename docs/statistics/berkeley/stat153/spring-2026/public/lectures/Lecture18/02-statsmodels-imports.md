---
title: statsmodels imports
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# statsmodels imports

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

---

[← Stat 153/248 - Lecture 18](01-stat-153-248---lecture-18.md) · [Up: contents](index.md) · [Sunspot data is in the statsmodels package (as well as astsa, but here we don't need it!) →](03-sunspot-data-is-in-the-statsmodels-package-as-well-as-astsa.md)
