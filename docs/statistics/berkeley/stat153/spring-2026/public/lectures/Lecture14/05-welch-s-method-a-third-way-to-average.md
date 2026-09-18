---
title: 'Welch''s method: a third way to average'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Welch's method: a third way to average

In practice, many fields instead use another method to calculate the periodogram - Welch's Method. It chops one long time series into overlapping segments, computes a periodogram for each segment, and averages them. It's like creating pseudo-independent "realizations" from a single dataset.

This is conceptually the same as (b) above, except the segments aren't truly independent (they overlap and come from the same series). But it works well in practice.

```python
welch?
```

By default, Welch's method uses a Hann window, which is defined as

$w(n)=0.5-0.5\cos\left(\frac{2\pi n}{M-1}\right) \quad 0 \leq n \leq M-1$

This window is applied to each time-domain segment before computing its periodogram, in the following sequence:

1. Chop the signal into overlapping segments of `nperseg`
2. Multiply each segment by the Hann window (in the time domain) - tapers the segment smoothly at the edges and results in a better behaved Fourier transform
3. Compute the periodogram of the windowed segment
4. Average the periodograms

```python
import scipy.signal
window = scipy.signal.windows.hann(51)
plt.figure(figsize=(5,3))
plt.plot(window)
plt.title("Hann window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
```

```python
np.random.seed(42)
n = 2048
wn = np.random.normal(0, np.sqrt(sigma2), n)

fig, axes = plt.subplots(1, 4, figsize=(16, 3.5), sharey=True)

# Raw periodogram
freqs_raw, power_raw = periodogram(wn, fs=1)
axes[0].plot(freqs_raw, power_raw, color='steelblue', lw=0.3, alpha=0.7)
axes[0].axhline(2 * sigma2, color='r', lw=2)
axes[0].set_title(f'Raw periodogram\n(1 segment of {n})', fontsize=10)
axes[0].set_ylabel('Power')
axes[0].set_xlabel('Frequency')
axes[0].set_ylim([0, 12])

# Welch with decreasing segment sizes
seg_sizes = [512, 256, 128]
for ax, nperseg in zip(axes[1:], seg_sizes):
    noverlap = nperseg // 2
    n_seg = (n - noverlap) // (nperseg - noverlap)

    # Calculate welch periodogram, hann window is the default
    freqs_w, power_w = welch(wn, fs=1, nperseg=nperseg, noverlap=noverlap,
                             window='hann')

    ax.plot(freqs_w, power_w, lw=1.2)
    ax.axhline(2 * sigma2, color='r', lw=2)
    ax.set_title(f'Welch (seg = {nperseg})\n(≈ {n_seg} segments averaged)', fontsize=10)
    ax.set_xlabel('Frequency')
    ax.set_ylim([0, 12])

fig.suptitle(f'Welch\'s method: splitting n = {n} into overlapping segments',
             y=1.03, fontsize=13)
plt.tight_layout()
```

---

← Comparing averaging methods · [Up: contents](index.md) · [Comparing methods on data with frequency peaks →](06-comparing-methods-on-data-with-frequency-peaks.md)
