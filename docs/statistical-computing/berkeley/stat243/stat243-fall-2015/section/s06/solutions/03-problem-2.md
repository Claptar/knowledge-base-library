---
title: problem 2
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/solutions.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2015/section/s06/solutions.ipynb
licence: unresolved
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# problem 2

**Source:** [`section/s06/solutions.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/solutions.ipynb) · **Licence:** unresolved · Converted 2026-09-14 from `.ipynb` (lossless)

```python
from math import exp, log
import numpy as np
from scipy.special import gammaln

def log_choose(n, k):
    return gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1)
```

## using a for loop

The solution is pretty much a copy of Chris's solution in python:

```python
def log_likelihood(k, n, p, phi):
    klogk = 0 if k == 0 else k * log(k)
    nmklognmk = 0 if n - k == 0 else (n - k)*log(n - k)

    return exp(log_choose(n, k) +
               (1 - phi)*(klogk + nmklognmk - n*log(n)) +
               (k*phi*log(p)) +
               (n-k)*phi*log(1-p))

def norm_const_slow(n, p, phi):
    total = 0.0
    for k in xrange(0, n+1):
        total += log_likelihood(k, n, p, phi)

    return total
```

---

[← problem 1](02-problem-1.md) · [Up: contents](index.md) · [using vectorization →](04-using-vectorization.md)
