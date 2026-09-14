---
title: Build a spectrogram from scratch
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Build a spectrogram from scratch

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

def my_spectrogram(y, fs, nperseg=2048, noverlap=None):
    """Spectrogram from np.fft.rfft — no scipy needed."""
    if noverlap is None:
        noverlap = nperseg // 2

    hop = nperseg - noverlap
    n_windows = (len(y) - nperseg) // hop + 1

    freqs = np.fft.rfftfreq(nperseg, d=1/fs)
    times = (np.arange(n_windows) * hop + nperseg // 2) / fs
    window = np.hanning(nperseg)

    Sxx = np.zeros((len(freqs), n_windows))
    for i in range(n_windows):
        start = i * hop
        segment = y[start:start+nperseg] * window
        Y = np.fft.rfft(segment)
        Sxx[:, i] = np.abs(Y)**2 / (fs * np.sum(window**2))

    return freqs, times, Sxx

---

[← statsmodels.tsa.stattools.acf computes the sample autocorrelation function.](30-statsmodels-tsa-stattools-acf-computes-the-sample-autocorrel.md) · [Up: contents](index.md) · [Compare to scipy →](32-compare-to-scipy.md)
