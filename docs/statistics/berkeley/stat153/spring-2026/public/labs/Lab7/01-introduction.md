---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`public/labs/Lab7.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

# Lab 7 - Power Spectral Analysis

In this notebook, we'll build on our periodogram demos from Lecture 12 and explore:
1. The Discrete Fourier Transform (DFT) and its connection to the periodogram
2. Spectral density of common processes (white noise, MA, AR)
3. Linear filtering in the frequency domain

**Cells marked with `# TODO` or `#FILL IN` are for you to fill in!**

```python
import numpy as np
from matplotlib import pyplot as plt
import math
from scipy.signal import periodogram
plt.rcParams['figure.figsize'] = (5, 3)
```

---

[Up: contents](index.md) · [Part 1: The Discrete Fourier Transform (DFT) →](02-part-1-the-discrete-fourier-transform-dft.md)
