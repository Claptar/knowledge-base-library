---
title: Averaging across neighboring frequencies (Daniell smoother)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Averaging across neighboring frequencies (Daniell smoother)

Another way that we can smooth the periodogram is by averaging across neighboring frequencies, rather than realizations of a time series (which we often don't have). For a smooth spectral density, neighboring periodogram ordinates are approximately independent and have approximately the same expectation.
So averaging $2L+1$ neighbors is like averaging $2L+1$ independent estimates:

$$\hat{f}(\omega) = \frac{1}{2L+1}\sum_{k=-L}^{L} P\!\left(\omega + \frac{k}{n}\right)$$

This reduces variance by a factor of roughly $1/(2L+1)$, at the cost of some bias
(blurring in frequency).

```python
def daniell_smooth(power, L):
    """Smooth a periodogram by averaging 2L+1 neighbors."""
    kernel = np.ones(2 * L + 1) / (2 * L + 1)
    return np.convolve(power, kernel, mode='same')

np.random.seed(42)
n = 512
wn = np.random.normal(0, np.sqrt(sigma2), n)
freqs, power = periodogram(wn, fs=1)

L_values = [0, 3, 10, 30]

fig, axes = plt.subplots(1, 4, figsize=(16, 3.5), sharey=True)

for ax, L in zip(axes, L_values):
    if L == 0:
        smoothed = power
        label = 'Raw periodogram'
    else:
        smoothed = daniell_smooth(power, L)
        label = f'Smoothed (2L+1 = {2*L+1})'

    ax.plot(freqs, smoothed, color='steelblue', lw=0.8, label=label)
    ax.axhline(2 * sigma2, color='r', lw=2, label='$2\sigma^2$')
    ax.set_title(f'L = {L}  (window = {2*L+1})', fontsize=11)
    ax.set_xlabel('Frequency')
    ax.set_ylim([0, 8])
    ax.legend(fontsize=8)

axes[0].set_ylabel('Power')
fig.suptitle('Daniell smoother: averaging neighboring frequencies from ONE time series',
             y=1.02, fontsize=13)
plt.tight_layout()
```

This is the same idea as before, but now we're averaging across frequencies instead of across realizations or repetitions of our time series. With $L = 30$ (averaging 61 neighbors), the estimate is nearly flat.

For white noise, there's no bias from smoothing since the true spectrum is already constant. For a process with a peaked spectrum, smoothing would flatten the peak, so this can introduce bias in our estimates.

---

[← Averaging the periodogram](02-averaging-the-periodogram.md) · [Up: contents](index.md) · Comparing averaging methods →
