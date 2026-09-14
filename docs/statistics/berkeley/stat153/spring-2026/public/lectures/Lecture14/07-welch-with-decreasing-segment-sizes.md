---
title: Welch with decreasing segment sizes
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Welch with decreasing segment sizes

**Source:** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Comparing methods on data with frequency peaks

Let's see an example of how these estimates compare for a signal with three sinusoidal components. This is very similar to the sinusoid we discussed in the Lecture 12 notebook.

```python
fs = 1000  # sampling rate
t = np.arange(0, 1, 1/fs)

---

[← Raw periodogram](06-raw-periodogram.md) · [Up: contents](index.md) · [Three sinusoidal components →](08-three-sinusoidal-components.md)
