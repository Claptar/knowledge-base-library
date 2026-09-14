---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabFive153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabFive153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLabFive153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabFive153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: High-dimensional regression for change-points
---

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import cvxpy as cp
```

Consider the following function, and a simulated dataset obtained by adding noise to it.

```python
def blocks(x):
    """
    Convert the R arblocks function to Python using NumPy
    """
    # Create the step function using array operations
    ans = 4 * np.asarray(x > 0.1, dtype=float)
    ans -= 5 * np.asarray(x > 0.13, dtype=float)
    ans += 3 * np.asarray(x > 0.15, dtype=float)
    ans -= 4 * np.asarray(x > 0.23, dtype=float)
    ans += 5 * np.asarray(x > 0.25, dtype=float)
    ans -= 4.2 * np.asarray(x > 0.40, dtype=float)
    ans += 2.1 * np.asarray(x > 0.44, dtype=float)
    ans += 4.3 * np.asarray(x > 0.65, dtype=float)
    ans -= 3.1 * np.asarray(x > 0.76, dtype=float)
    ans += 2.1 * np.asarray(x > 0.78, dtype=float)
    ans -= 4.2 * np.asarray(x > 0.81, dtype=float)

    # Apply some arbitrary scaling
    ans = ans * 7 * 1.3 / np.sqrt(6.0695)

    return ans

---

[Up: contents](index.md) · [Create sequence similar to R's seq →](02-create-sequence-similar-to-r-s-seq.md)
