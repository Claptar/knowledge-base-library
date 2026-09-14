---
title: Stat 153/248 - Lecture 18
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture18.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Stat 153/248 - Lecture 18

**Source:** [`public/lectures/Lecture18.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture18.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

---

[Up: contents](index.md) · [statsmodels imports →](02-statsmodels-imports.md)
