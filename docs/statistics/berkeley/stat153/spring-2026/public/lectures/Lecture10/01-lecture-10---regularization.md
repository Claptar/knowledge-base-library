---
title: Lecture 10 - Regularization
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lecture 10 - Regularization

**Source:** [`public/lectures/Lecture10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

## The perfect model

```python
import numpy as np
import math
from matplotlib import pyplot as plt
import statsmodels.api as sm
```

We'll make some sinuosoidal data and add white noise, using the equation $y=\beta_0 + R \cos (2\pi ft + \phi) + \epsilon$

```python
fs = 500 # sampling rate
duration = 2
t = np.arange(0,duration,step=1/fs)
B0 = 2
phi = 0
f = 2.3
R =  2.5
var_eps = .2 # Variance of white noise

---

[Up: contents](index.md) · [Our true sinusoid →](02-our-true-sinusoid.md)
