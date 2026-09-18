---
title: The periodogram stays noisy no matter how much data you have
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# The periodogram stays noisy no matter how much data you have

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

White noise has a flat spectral density: $f(\omega) = \sigma^2$ for all $\omega$.
With the default scaling in `scipy.signal.periodogram` (which uses `scaling='density'`),
the theoretical level is $2\sigma^2$ (because the two-sided spectrum is folded onto $[0, 1/2]$).

Let's simulate 20 white noise series at each of three sample sizes and overlay their periodograms.

```python
# Simulate many periodograms from white noise and overlay them
np.random.seed(42)
sigma2 = 1.0
fig, axes = plt.subplots(1, 3, figsize=(12, 3))
for idx, n in enumerate([64, 256, 1024]):
    for rep in range(20):
        wn = np.random.normal(0, np.sqrt(sigma2), n)
        freqs, power = periodogram(wn, fs=1)
        axes[idx].plot(freqs, power, alpha=0.2, color='steelblue')

    axes[idx].axhline(2 * sigma2, color='r', linewidth=2, label='$2\sigma^2$')
    axes[idx].set_title(f'n = {n}')
    axes[idx].set_xlabel('Frequency')
    axes[idx].set_ylim([0, 15])
    if idx == 0:
        axes[idx].set_ylabel('Power')
    axes[idx].legend(fontsize=8)
plt.suptitle('Periodogram variability does NOT decrease with n', y=1.02)
plt.tight_layout()
```

Each blue line is one periodogram. The red line is the true spectral density.

Notice that as $n$ grows from 64 to 1024, the periodogram gets *denser*
(more Fourier frequencies), but the scatter around the red line doesn't shrink at all.
Every individual periodogram ordinate has roughly the same wild variability regardless of $n$.

---

[Up: contents](index.md) · [Averaging the periodogram →](02-averaging-the-periodogram.md)
