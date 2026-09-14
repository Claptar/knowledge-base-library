---
title: Simulate many periodograms from white noise and overlay them
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Simulate many periodograms from white noise and overlay them

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

*(1 figure omitted — see the original notebook.)*

Why is the periodogram inconsistent? What could we do to get a better (smoother) estimate of the spectral density? (Hint: Think about averaging nearby frequencies — we'll cover this next lecture!)

---

[← Plot frequency domain](31-plot-frequency-domain.md) · [Up: contents](index.md)
