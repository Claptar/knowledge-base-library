---
title: Averaging the periodogram
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Averaging the periodogram

If we could observe many independent copies of the same process, we could average
their periodograms. Since the periodogram is unbiased ($E[P(\omega)] \approx f(\omega)$),
the average converges to $f(\omega)$ by the law of large numbers.

Of course, in practice we usually only have *one* time series — but this exercise
shows the principle.

```python
np.random.seed(153)
n = 256
num_reps = [1, 5, 20, 100]

fig, axes = plt.subplots(1, 4, figsize=(16, 3.5), sharey=True)

for ax, K in zip(axes, num_reps):
    # Average K periodograms
    avg_power = None
    for rep in range(K):
        # Create a white noise signal with mean 0 and variance sigma^2
        # for n time points
        wn = np.random.normal(0, np.sqrt(sigma2), n)

        # Calculate the periodogram
        freqs, power = periodogram(wn, fs=1)

        # increment avg_power (later we'll divide by K)
        if avg_power is None:
            avg_power = power.copy()
        else:
            avg_power += power
        # Also plot individuals faintly for small K
        if K <= 5:
            ax.plot(freqs, power, alpha=0.15, color='steelblue', lw=0.5)
    avg_power /= K

    ax.plot(freqs, avg_power, lw=1.5, label=f'Avg of {K}')
    ax.axhline(2 * sigma2, color='r', lw=2, label='$2\sigma^2$')
    ax.set_title(f'K = {K} realization{"s" if K > 1 else ""}', fontsize=11)
    ax.set_xlabel('Frequency')
    ax.set_ylim([0, 8])

axes[0].set_ylabel('Power')
fig.suptitle('Averaging periodograms across independent realizations (n = 256 each)',
             y=1.02, fontsize=13)
plt.tight_layout()
```

With $K = 1$ our estimates are very noisy. By $K = 100$, the average is nearly flat at $2\sigma^2$.
By law of large numbers, we see this convergence when averaging independent, unbiased estimates.

**But we usually only have one time series.** So how do we get this averaging effect?

---

[← The periodogram stays noisy no matter how much data you have](01-the-periodogram-stays-noisy-no-matter-how-much-data-you-have.md) · [Up: contents](index.md) · [Averaging across neighboring frequencies (Daniell smoother) →](03-averaging-across-neighboring-frequencies-daniell-smoother.md)
