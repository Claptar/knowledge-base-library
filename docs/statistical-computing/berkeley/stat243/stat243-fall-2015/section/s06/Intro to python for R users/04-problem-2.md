---
title: problem 2
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/Intro
  to python for R users.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2015/section/s06/Intro to python
  for R users.ipynb
licence: unresolved
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# problem 2

**Source:** [`section/s06/Intro to python for R users.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s06/Intro to python for R users.ipynb) · **Licence:** unresolved · Converted 2026-09-14 from `.ipynb` (lossless)

Refer back to problem set 3, problem 2. We can re-implement that solution using python. A few functions you might need are:

- `scipy.special.gammaln`
- `log_choose` (implemented below)

Implement 2 different versions:
1. Using a `for` loop
2. Using vectorization and numpy

```python
from scipy.special import gammaln

def log_choose(n, k):
    return gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1)
```

---

[← problem 1](03-problem-1.md) · [Up: contents](index.md)
