---
title: 'Part 1: The Discrete Fourier Transform (DFT)'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Part 1: The Discrete Fourier Transform (DFT)

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

Recall from last lecture that the periodogram used coefficients:

$$a_j = \frac{2}{n}\sum_{t=1}^n x_t \cos(2\pi t j/n), \quad b_j = \frac{2}{n}\sum_{t=1}^n x_t \sin(2\pi t j/n)$$

The DFT wraps these together using Euler's formula $e^{-i\theta}=\cos\theta - i\sin\theta$:

$$d(j/n) = \frac{1}{\sqrt{n}}\sum_{t=1}^n x_t e^{-i 2\pi t j/n}$$

And the scaled periodogram is $P(j/n) = \frac{4}{n}|d(j/n)|^2$.

Let's implement the DFT by hand and compare it to `numpy.fft.fft`.

## Implement the DFT manually

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

## Compare your DFT to numpy's FFT

Note: `numpy.fft.fft` uses the convention $X[j] = \sum_{t=0}^{n-1} x_t e^{-i 2\pi t j/n}$ (no $1/\sqrt{n}$ scaling, and $t$ starts at 0). So to compare, we need to account for the different normalization and indexing.

```python
# Create a test signal: sum of two sinusoids + noise
np.random.seed(42)
n = 100
t = np.arange(1, n+1)
x = 3*np.cos(2*math.pi*t*5/n) + 2*np.sin(2*math.pi*t*12/n) + np.random.normal(0, 0.5, n)

# Compute using your function
d_manual = dft(x)

# Compute using numpy (adjust for our convention)
# numpy uses t=0,...,n-1 and no 1/sqrt(n) normalization
# Our convention uses t=1,...,n and 1/sqrt(n)
# To match: multiply numpy result by exp(-i*2pi*j/n)/sqrt(n) to shift from 0-indexing to 1-indexing
fft_numpy = np.fft.fft(x)
j_vals = np.arange(n)
d_numpy = 1/np.sqrt(n) * fft_numpy * np.exp(-1j * 2 * math.pi * j_vals / n)

# Check they match
plt.figure()
plt.plot(d_manual)
plt.plot(d_numpy)

plt.figure()
plt.plot(fft_numpy)
print("Max difference between manual and numpy DFT:", np.max(np.abs(d_manual - d_numpy)))
```

```
Max difference between manual and numpy DFT: 1.5169458873047464e-13
/Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages/matplotlib/cbook.py:1719: ComplexWarning: Casting complex values to real discards the imaginary part
  return math.isfinite(val)
/Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages/matplotlib/cbook.py:1355: ComplexWarning: Casting complex values to real discards the imaginary part
  return np.asarray(x, float)
```

*(2 figures omitted — see the original notebook.)*

## From DFT to periodogram

The scaled periodogram is $P(j/n) = \frac{4}{n}|d(j/n)|^2$. Let's compute it from the DFT and compare to `scipy.signal.periodogram`.

```python
# Compute the scaled periodogram from our DFT
# TODO: Fill in the periodogram formula
P_manual = (4/n) * np.abs(d_manual)**2  # FILL IN: (4/n) * |d(j/n)|^2

# Only plot up to the Nyquist frequency (j = 0, ..., n/2)
freqs_manual = np.arange(n // 2 + 1) / n  # frequencies j/n

# Compare with scipy periodogram (fs=1 so frequencies are in cycles/sample)
freqs_scipy, power_scipy = periodogram(x, fs=1)

fig, axes = plt.subplots(1, 2, figsize=(10, 3))
axes[0].stem(freqs_manual, P_manual[:n // 2 + 1])
axes[0].set_title('Our periodogram (from DFT)')
axes[0].set_xlabel('Frequency (cycles/sample)')
axes[0].set_ylabel('Power')

axes[1].stem(freqs_scipy, power_scipy)
axes[1].set_title('scipy.signal.periodogram')
axes[1].set_xlabel('Frequency (cycles/sample)')
axes[1].set_ylabel('Power')
plt.tight_layout()

# Note: scipy uses a slightly different normalization. The shapes should match
# even if the scale differs. What normalization does scipy use?
```

*(1 figure omitted — see the original notebook.)*

## The symmetry property

We noted that $P(j/n) = P(1 - j/n)$, which is why we only need to look at frequencies up to 1/2. Let's verify this.

```python
# TODO: Verify that |d(j/n)|^2 = |d(1-j/n)|^2 for our test signal
# Hint: d(1 - j/n) corresponds to index (n - j) in the array

for j in range(1, 6):
    power_j = np.abs(d_manual[j])**2
    power_mirror = np.abs(d_manual[n-j])**2  # FILL IN: |d[n-j]|^2
    print(f"j={j}: |d(j/n)|^2 = {power_j:.4f}, |d(1-j/n)|^2 = {power_mirror:.4f}")
```

```
j=1: |d(j/n)|^2 = 0.3022, |d(1-j/n)|^2 = 0.3022
j=2: |d(j/n)|^2 = 0.0796, |d(1-j/n)|^2 = 0.0796
j=3: |d(j/n)|^2 = 0.2221, |d(1-j/n)|^2 = 0.2221
j=4: |d(j/n)|^2 = 0.1463, |d(1-j/n)|^2 = 0.1463
j=5: |d(j/n)|^2 = 214.0105, |d(1-j/n)|^2 = 214.0105
```

Why does this symmetry hold? What does it tell us about the information content of the DFT?

---

---

[Up: contents](index.md) · [Part 2: Spectral Density of Common Processes →](02-part-2-spectral-density-of-common-processes.md)
