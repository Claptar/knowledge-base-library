---
title: Compare with scipy periodogram (fs=1 so frequencies are in cycles/sample)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Compare with scipy periodogram (fs=1 so frequencies are in cycles/sample)

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

freqs_scipy, power_scipy = periodogram(x, fs=1)

fig, axes = plt.subplots(1, 2, figsize=(10, 3))
axes[0].stem(freqs_manual, P_manual[:n // 2 + 1])
axes[0].set_title('Our periodogram (from DFT)')
axes[0].set_xlabel('Frequency (cycles/sample)')
axes[0].set_ylabel('Power')

axes[1].stem(freqs_scipy, power_scipy)
axes[1].set_title('scipy.signal.periodogram')
axes[1].set_xlabel('Frequency (cycles/sample)')
axes[1].set_ylabel('Power')
plt.tight_layout()

---

[← Only plot up to the Nyquist frequency (j = 0, ..., n/2)](11-only-plot-up-to-the-nyquist-frequency-j-0-n-2.md) · [Up: contents](index.md) · [Note: scipy uses a slightly different normalization. The shapes should match →](13-note-scipy-uses-a-slightly-different-normalization-the-shape.md)
