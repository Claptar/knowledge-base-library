---
title: Stat153/248 Lecture 12 - Power spectral analysis
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture12.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Stat153/248 Lecture 12 - Power spectral analysis

**Source:** [`public/lectures/Lecture12.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
import numpy as np
from matplotlib import pyplot as plt
import math
plt.rcParams['figure.figsize'] = (4, 3)
```

```python
fs = 1000 # sampling rate
t = np.arange(0, 0.5, 1/fs)

---

[Up: contents](index.md) · [Let's make three different sinusoids →](02-let-s-make-three-different-sinusoids.md)
