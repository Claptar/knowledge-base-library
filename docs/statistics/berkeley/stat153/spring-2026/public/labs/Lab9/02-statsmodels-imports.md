---
title: statsmodels imports
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# statsmodels imports

**Source:** [`public/labs/Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

import statsmodels.api as sm
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

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

## Heart Rate Variability

Heart rate variability (HRV) — the beat-to-beat fluctuation in your heart's rhythm — is a widely studied biosignal. The RR interval series (time between consecutive heartbeats) reflects a mix of:

- **Autonomic feedback loops** (sympathetic/parasympathetic regulation, which could be modeled like an AR component)
- **Respiratory and other short-lived perturbations** (breathing, posture changes, which could cause MA-like shocks)

This mix makes HRV a natural ARMA process. Let's see it in action.

We'll use data from the **MIT-BIH Normal Sinus Rhythm Database** on PhysioNet. We can get this from the package [WFDB (Waveform Database)](https://www.physionet.org/content/wfdb/10.7.0/)

```python

---

[← Stat 153/248 - Lab 9](01-stat-153-248---lab-9.md) · [Up: contents](index.md) · [Heart Rate Variability - RR intervals →](03-heart-rate-variability---rr-intervals.md)
