---
title: 'Part 4: Periodogram as a Noisy Estimator'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Part 4: Periodogram as a Noisy Estimator

**Source:** [`public/labs/Lab7.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

An important property of the periodogram: it is an **inconsistent** estimator of the spectral density. Even as $n \to \infty$, the periodogram does not converge to $f(\omega)$ — its variance doesn't shrink! Let's see this.

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

Why is the periodogram inconsistent? What could we do to get a better (smoother) estimate of the spectral density? (Hint: Think about averaging nearby frequencies — we'll cover this next lecture!)

---

[← Part 3: Linear Filtering in the Frequency Domain](04-part-3-linear-filtering-in-the-frequency-domain.md) · [Up: contents](index.md)
