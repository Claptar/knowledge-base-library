---
title: Stat 153/248 - Lecture 19
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture19.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Stat 153/248 - Lecture 19

**Source:** [`public/lectures/Lecture19.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Here we will extend the concepts from Lecture 18 to ARIMA.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import warnings
warnings.filterwarnings('ignore')

---

[Up: contents](index.md) · [statsmodels imports →](02-statsmodels-imports.md)
