---
title: Comparing methods on data with frequency peaks
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Comparing methods on data with frequency peaks

Let's see an example of how these estimates compare for a signal with three sinusoidal components. This is very similar to the sinusoid we discussed in the Lecture 12 notebook.

```python
fs = 1000  # sampling rate
t = np.arange(0, 1, 1/fs)

# Three sinusoidal components
f = [6, 10.5, 39.2]  # Frequencies of the sinusoids
x1 = 12*np.cos(2*math.pi*f[0]*t) + 13*np.sin(2*math.pi*f[0]*t)
x2 =  4*np.cos(2*math.pi*f[1]*t) +  5*np.sin(2*math.pi*f[1]*t)
x3 =  6*np.cos(2*math.pi*f[2]*t) +  7*np.sin(2*math.pi*f[2]*t)

# Clean signal
x_clean = x1 + x2 + x3

# Signal + noise
np.random.seed(42)
noise_std = 20.0
x_noisy = x_clean + noise_std * np.random.randn(len(t))

# Theoretical power for each component
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

# Add frequency labels
for ax in axes:
    for freq in f:
        ax.text(freq + 0.5, ax.get_ylim()[1] * 0.3, f'{freq} Hz',
                fontsize=8, color='red')

plt.tight_layout()
```

### Smoothing

Now let's use the noisy data (which is a more realistic case) and the smoothing methods to see what we recover.

```python
fig, axes = plt.subplots(2, 3, figsize=(15, 11))

# Column labels
col_labels = ['Light smoothing', 'Medium smoothing', 'Heavy smoothing']

# ── Row 2: Daniell smoother ──
daniell_Ls = [1, 2, 15]
for col, L in enumerate(daniell_Ls):
    smoothed = daniell_smooth(power_n, L)
    axes[0, col].semilogy(freqs_n, smoothed, lw=1.2, color='C1',
                          label=f'Daniell (2L+1 = {2*L+1})')
    axes[0, col].semilogy(freqs_n, power_n, lw=0.3, color='C0')
    for freq in f:
        axes[1, col].axvline(freq, ls='--', color='red', alpha=0.4, lw=1)
    axes[0, col].set_xlim(0, 50)
    axes[0, col].set_ylim(1e-2, 1e4)
    axes[0, col].legend(fontsize=9, loc='upper right')
    if col == 0:
        axes[1, col].set_ylabel('Daniell smoother\n\nPower (log)')

# ── Row 3: Welch ──
welch_segs = [800, 500, 150]
for col, nperseg in enumerate(welch_segs):
    freqs_w, power_w = welch(x_noisy, fs=fs, nperseg=nperseg, noverlap=nperseg//2)
    n_segs = int(2 * len(x_noisy) / nperseg - 1)
    axes[1, col].semilogy(freqs_w, power_w, lw=1.2, color='C2',
                          label=f'Welch (seg={nperseg}, ~{n_segs} avg)')
    axes[1, col].semilogy(freqs_n, power_n, lw=0.3, color='C0')
    for freq in f:
        axes[1, col].axvline(freq, ls='--', color='red', alpha=0.4, lw=1)
    axes[1, col].set_xlim(0, 50)
    axes[1, col].set_ylim(1e-2, 1e4)
    axes[1, col].set_xlabel('Frequency (Hz)')
    axes[1, col].legend(fontsize=9, loc='upper right')
    if col == 0:
        axes[1, col].set_ylabel('Welch\'s method\n\nPower (log)')

fig.suptitle('Three estimators × three smoothing levels — red dashed lines mark true frequencies',
             fontsize=13, y=1.01)
plt.tight_layout()
```

### How to choose the number of segments?

Welch can only resolve two peaks that are at least $\Delta f = f_s / N_{seg}$ apart, where $N_{seg}$ is the segment length in samples. If you need resolved peaks separated by $\delta f$ Hz, you need segments of at least:

$$N_{seg}\geq \frac{f_s}{\Delta f}$$

So for the 6 and the 10.5 Hz peak, these are 4.5 Hz apart, and with a sampling rate of $f_s=1000$ we'd need:

$$N_{seg}\geq \frac{1000}{\Delta 4.5} = 222$$

However, this in practice is the absolute floor, so we'd probably want segments at least 2-3 times longer than that, so 400 to 600 samples may work better here.

For the Daniell smoother, if you want to resolve two peaks separated by $\Delta f$, you need the smoothed bandwidth to be less than this:

$$\Delta f_{\text{smooth}} < \Delta f \implies L < \frac{N \cdot \Delta f}{2f_s} - \frac{1}{2}$$

For the 6 and 10.5 Hz peak, we'd have:

$$L < \frac{1000(4.5)}{2(1000)} - \frac{1}{2} = 2.25 - 0.5 = 1.75$$

So here $L=1$ would be fine and not obscure the peaks, but $L=2$ is already borderline for these frequencies.

## When is the periodogram not enough?

Can you think of some signals where knowing the periodogram obscures information that you might care about?

[Interactive Spectrogram](https://musiclab.chromeexperiments.com/Spectrogram/)

---

[← Welch's method: a third way to average](05-welch-s-method-a-third-way-to-average.md) · [Up: contents](index.md)
