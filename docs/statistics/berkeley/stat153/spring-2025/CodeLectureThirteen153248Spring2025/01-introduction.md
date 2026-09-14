---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureThirteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureThirteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Sunspots and the Spectrum Model
---

We will revisit some sinusoidal models in the context of the sunspots data. We will then do some simulations illustrating the spectrum model.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import cvxpy as cp
```

```
(CVXPY) Mar 05 11:46:52 PM: Encountered unexpected exception importing solver SCS:
ImportError("dlopen(/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/_scs_direct.cpython-310-darwin.so, 0x0002): Library not loaded: @rpath/libmkl_rt.2.dylib\n  Referenced from: <D8729A1C-CFE9-3397-89EC-E45F5ADDD8F2> /Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/_scs_direct.cpython-310-darwin.so\n  Reason: tried: '/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/../../libmkl_rt.2.dylib' (no such file), '/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.10/site-packages/../../libmkl_rt.2.dylib' (no such file), '/Users/aditya/mambaforge/envs/stat153spring2025/bin/../lib/libmkl_rt.2.dylib' (no such file), '/Users/aditya/mambaforge/envs/stat153spring2025/bin/../lib/libmkl_rt.2.dylib' (no such file), '/usr/local/lib/libmkl_rt.2.dylib' (no such file), '/usr/lib/libmkl_rt.2.dylib' (no such file, not in dyld cache)")
```

## Sunspots Dataset

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header = None, sep = ';')
y = sunspots.iloc[:,1].values
n = len(y)
plt.figure(figsize = (10, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

One aspect of the sunspots dataset (that we ignored previously) is the following. The data shows clear peaks (as well as troughs). Further the distance between successive peaks varies from cycle to cycle. The following is an illustration of this.

```python
#peaks of a time series dataset can be found by using the following function from the signal processing module of scipy
from scipy.signal import find_peaks

---

[Up: contents](index.md) · [Find peaks →](02-find-peaks.md)
