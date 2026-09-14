---
title: statsmodels.tsa.stattools.acf computes the sample autocorrelation function.
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# statsmodels.tsa.stattools.acf computes the sample autocorrelation function.

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

max_lag_samples = sr  # 1 second of lags
lag_axis_ms = np.arange(max_lag_samples + 1) / sr * 1000  # in ms

fig, axes = plt.subplots(2, 2, figsize=(14, 8))

signals_all = [
    (y_solo,  'Solo / A cappella', '#e94560'),
    (y_rep,   'Repetitive',        '#533483'),
    (y_dance, 'Danceable',         '#0f3460'),
    (y_slow,  'Slow',              '#16c79a'),
]

for ax, (y, name, color) in zip(axes.flat, signals_all):
    acf_vals = acf(y, nlags=max_lag_samples, fft=True)
    ax.plot(lag_axis_ms, acf_vals, color=color, linewidth=0.6)
    ax.axhline(0, color='#aaa', linewidth=0.5)
    ax.set_title(name, fontsize=12, fontweight='bold')
    ax.set_xlabel('Lag (ms)')
    ax.set_ylabel('ACF')
    ax.set_ylim(-0.5, 1.05)

plt.suptitle('Demo 5a: Sample ACF (statsmodels.tsa.stattools.acf) — What patterns repeat?',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### What do we see in the ACF for these different songs?

What if we try other dance songs, slow songs, a cappella songs?

### Relationship between periodogram and autocovariance

Here we will show that the periodogram is the same as the FFT of the autocovariance function directly by plotting the power spectrum in two ways:
1. Using welch estimation `scipy.signal.welch`
2. Using `np.fft.rfft` on the sample autocovariance

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 8))

for ax, (y, name, color) in zip(axes.flat, signals_all):
    # Method 1: Welch PSD
    f_w, Pxx_w = welch(y, fs=sr, nperseg=4096)

    # Method 2: FFT of the ACF
    acf_vals = acf(y, nlags = len(y)-1, fft=True)
    psd_from_acov = np.abs(np.fft.rfft(acf_vals))
    f_acov = np.fft.rfftfreq(len(acf_vals), d=1/sr)

    # Plot both (scale the FFT version to match Welch for visual comparison)
    ax.semilogy(f_w, Pxx_w, color=color, linewidth=1.2, label='welch')
    scale = np.max(Pxx_w) / np.max(psd_from_acov)
    ax.semilogy(f_acov, psd_from_acov * scale,
                color='#aaa', linewidth=0.7, alpha=0.7, label='FFT of acf')
    ax.set_title(name, fontsize=12, fontweight='bold')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_xlim(0, 4000)
    if ax in [axes[0,0], axes[1,0]]:
        ax.set_ylabel('PSD')
    ax.legend(fontsize=8)

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Stationarity check

If the signal is stationary, the PSD should look similar no matter which chunk of the signal we compute it from. This is the same logic behind why Welch works — it assumes each segment is a sample from the same stationary process.

```python
def plot_stationarity_check(y, sr, name, color, n_segments=6):
    """Overlay Welch PSD from time segments to visually check stationarity."""
    seg_len = len(y) // n_segments

    fig, ax = plt.subplots(figsize=(10, 4))
    for i in range(n_segments):
        chunk = y[i*seg_len:(i+1)*seg_len]
        f, Pxx = welch(chunk, fs=sr, nperseg=min(2048, seg_len//2))
        alpha = 0.3 + 0.7 * i / n_segments
        ax.semilogy(f, Pxx, color=color, alpha=alpha, linewidth=1,
                     label=f'Segment {i+1}')

    ax.set_title(f'{name} — Do all segments have the same PSD?',
                  fontsize=12, fontweight='bold')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('PSD')
    ax.set_xlim(0, 4000)
    ax.legend(fontsize=8, ncol=3)
    plt.tight_layout()
    plt.show()


print('Stationarity check: if PSD is stable across time segments,')
print('the signal is approximately stationary and our spectral estimates are valid.\n')

for y, name, color in signals_all:
    plot_stationarity_check(y, sr, name, color)
```

```
Stationarity check: if PSD is stable across time segments,
the signal is approximately stationary and our spectral estimates are valid.
```

*(4 figures omitted — see the original notebook.)*

## Bonus: Build Your Own Spectrogram from `np.fft`

Since the spectrogram is really just the periodogram on a sliding window, let's build one from scratch.

```python

---

[← Apply to the slow track](29-apply-to-the-slow-track.md) · [Up: contents](index.md) · [Build a spectrogram from scratch →](31-build-a-spectrogram-from-scratch.md)
