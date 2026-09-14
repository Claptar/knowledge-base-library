---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLabEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
from statsmodels.tsa.ar_model import AutoReg
```

## AR model fitting: AutoReg vs ARIMA

There are two inbuilt functions in statsmodels for fitting AR models: (a) AutoReg (which we used previously), and (b) ARIMA. We compare and contrast these two ways below. We use the GNP dataset (from FRED) that we used previously.

```python
gnp = pd.read_csv("GNP_30Oct2025.csv")

---

[Up: contents](index.md) · [this is quarterly data →](02-this-is-quarterly-data.md)
