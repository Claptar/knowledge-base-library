---
title: '── Row 3: Welch ──'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ── Row 3: Welch ──

**Source:** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

[← ── Row 2: Daniell smoother ──](14-row-2-daniell-smoother.md) · [Up: contents](index.md)
