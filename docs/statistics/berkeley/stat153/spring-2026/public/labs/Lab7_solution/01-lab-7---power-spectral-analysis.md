---
title: Lab 7 - Power Spectral Analysis
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab 7 - Power Spectral Analysis

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

In this notebook, we'll build on our periodogram demos from Lecture 12 and explore:
1. The Discrete Fourier Transform (DFT) and its connection to the periodogram
2. Spectral density of common processes (white noise, MA, AR)
3. Linear filtering in the frequency domain

**Cells marked with `# TODO` are for you to fill in!**

```python
import numpy as np
from matplotlib import pyplot as plt
import math
from scipy.signal import periodogram
plt.rcParams['figure.figsize'] = (5, 3)
```

## Part 1: The Discrete Fourier Transform (DFT)

Recall from last lecture that the periodogram used coefficients:

$$a_j = \frac{2}{n}\sum_{t=1}^n x_t \cos(2\pi t j/n), \quad b_j = \frac{2}{n}\sum_{t=1}^n x_t \sin(2\pi t j/n)$$

The DFT wraps these together using Euler's formula $e^{-i\theta}=\cos\theta - i\sin\theta$:

$$d(j/n) = \frac{1}{\sqrt{n}}\sum_{t=1}^n x_t e^{-i 2\pi t j/n}$$

And the scaled periodogram is $P(j/n) = \frac{4}{n}|d(j/n)|^2$.

Let's implement the DFT by hand and compare it to `numpy.fft.fft`.

### Implement the DFT manually

Write a function that computes $d(j/n)$ for all $j = 0, 1, \dots, n-1$.

```python
def dft(x):
    '''Compute the Discrete Fourier Transform of signal x.

    Parameters
    ----------
    x : array of length n

    Returns
    -------
    d : complex array of length n, where d[j] = d(j/n)
    '''
    n = len(x)
    t = np.arange(1, n + 1)  # t = 1, ..., n
    d = np.zeros(n, dtype=complex)

    for j in range(n):
        # TODO: Compute d[j] using the DFT formula
        # Hint: d[j] = (1/sqrt(n)) * sum of x_t * exp(-i * 2pi * t * j / n)
        d[j] = 1/np.sqrt(n) * np.sum(x*np.exp(-1j*2*math.pi*t*j/n))  # FILL IN

    return d
```

### Compare your DFT to numpy's FFT

Note: `numpy.fft.fft` uses the convention $X[j] = \sum_{t=0}^{n-1} x_t e^{-i 2\pi t j/n}$ (no $1/\sqrt{n}$ scaling, and $t$ starts at 0). So to compare, we need to account for the different normalization and indexing.

```python

---

[Up: contents](index.md) · [Create a test signal: sum of two sinusoids + noise →](02-create-a-test-signal-sum-of-two-sinusoids-noise.md)
