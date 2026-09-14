---
title: Lecture 14
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lecture 14

**Source:** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Here we will include some more demos of the periodogram and methods for averaging that can improve the behavior of the periodogram.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram, welch
import math

plt.rcParams['figure.figsize'] = (12, 4)
plt.rcParams['font.size'] = 14
plt.rcParams['mathtext.fontset'] = 'cm'
```

## The periodogram stays noisy no matter how much data you have

White noise has a flat spectral density: $f(\omega) = \sigma^2$ for all $\omega$.
With the default scaling in `scipy.signal.periodogram` (which uses `scaling='density'`),
the theoretical level is $2\sigma^2$ (because the two-sided spectrum is folded onto $[0, 1/2]$).

Let's simulate 20 white noise series at each of three sample sizes and overlay their periodograms.

```python

---

[Up: contents](index.md) · [Simulate many periodograms from white noise and overlay them →](02-simulate-many-periodograms-from-white-noise-and-overlay-them.md)
