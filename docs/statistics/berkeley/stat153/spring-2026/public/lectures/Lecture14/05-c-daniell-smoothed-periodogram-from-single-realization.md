---
title: (c) Daniell-smoothed periodogram from single realization
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# (c) Daniell-smoothed periodogram from single realization

**Source:** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

smoothed = daniell_smooth(power_single, L)
axes[2].plot(freqs, smoothed, color='steelblue', lw=1.2)
axes[2].axhline(2 * sigma2, color='r', lw=2)
axes[2].set_title(f'(c) Daniell smooth (2L+1 = {2*L+1})\nfrom one realization')
axes[2].set_ylim([0, 10])
axes[2].set_xlabel('Frequency')

plt.tight_layout()
```

Notice that panels (b) and (c) look similar in terms of the variance reduction through averaging, though the Daniell smoother also introduces more spatially correlated structure (smoothness across frequencies).

## Welch's method: a third way to average

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

---

[← (b) Average of K=21 periodograms from independent realizations](04-b-average-of-k-21-periodograms-from-independent-realizations.md) · [Up: contents](index.md) · [Raw periodogram →](06-raw-periodogram.md)
