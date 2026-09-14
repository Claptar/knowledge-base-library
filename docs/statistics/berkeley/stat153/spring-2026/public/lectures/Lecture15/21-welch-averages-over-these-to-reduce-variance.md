---
title: Welch averages over these to reduce variance.
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Welch averages over these to reduce variance.

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

chunk_len = sr * 1  # 1-second chunks
n_chunks = min(30, len(y_dance) // chunk_len)

for i in range(n_chunks):
    chunk = y_dance[i*chunk_len:(i+1)*chunk_len]
    f_c, Pxx_c = periodogram(chunk, fs=sr)
    axes[0].plot(f_c, Pxx_c, linewidth=0.5, alpha=0.5)

axes[0].set_title(f'{n_chunks} raw periodograms from 1s chunks')
axes[0].set_xlabel('Frequency (Hz)')
axes[0].set_ylabel('Power')
axes[0].set_xlim(0, 3000)

---

[← even though the signal is approximately stationary.](20-even-though-the-signal-is-approximately-stationary.md) · [Up: contents](index.md) · [Welch does this averaging for us →](22-welch-does-this-averaging-for-us.md)
