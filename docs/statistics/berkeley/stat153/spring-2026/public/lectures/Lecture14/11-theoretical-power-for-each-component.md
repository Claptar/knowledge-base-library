---
title: Theoretical power for each component
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Theoretical power for each component

**Source:** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

for i, (freq, a, b) in enumerate(zip(f, [12,4,6], [13,5,7])):
    print(f'Component {i+1}: f = {freq} Hz, power = a² + b² = {a**2+b**2}')
```

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 3.5))

axes[0].plot(t, x_clean, lw=0.8, color='C0')
axes[0].set_title('Clean signal (no noise)')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Amplitude')

axes[1].plot(t, x_noisy, lw=0.8, color='C0')
axes[1].set_title(f'Noisy signal (σ_noise = {noise_std})')
axes[1].set_xlabel('Time (s)')

plt.tight_layout()
```

### Raw periodogram

First, let's look at the raw periodogram for this signal. We already saw something like this before. Notice that the peaks don't always line up with our Fourier frequencies, so there is spectral leakage into the nearby frequencies (for example, the 10.5 Hz peak is distributed across 10 Hz and 11 Hz).

```python
freqs_c, power_c = periodogram(x_clean, fs=fs)
freqs_n, power_n = periodogram(x_noisy, fs=fs)

fig, axes = plt.subplots(1, 2, figsize=(14, 4), sharey=True)

for ax, power, title in zip(axes, [power_c, power_n],
                            ['Clean signal', 'Noisy signal']):
    ax.stem(freqs_c, power)#, lw=0.8, color='C0')
    for freq in f:
        ax.axvline(freq, ls='--', color='red', alpha=0.5, lw=1)
    ax.set_xlabel('Frequency (Hz)')
    ax.set_title(f'Periodogram — {title}')
    ax.set_xlim(0, 50)

axes[0].set_ylabel('Power')

---

[← Signal + noise](10-signal-noise.md) · [Up: contents](index.md) · [Add frequency labels →](12-add-frequency-labels.md)
