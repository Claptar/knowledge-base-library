---
title: (a) Single raw periodogram
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# (a) Single raw periodogram

**Source:** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

wn_single = np.random.normal(0, np.sqrt(sigma2), n)
freqs, power_single = periodogram(wn_single, fs=1)
axes[0].plot(freqs, power_single, color='steelblue', lw=0.6, alpha=0.8)
axes[0].axhline(2 * sigma2, color='r', lw=2)
axes[0].set_title('(a) One raw periodogram\n(1 estimate per frequency)')
axes[0].set_ylim([0, 10])
axes[0].set_xlabel('Frequency')
axes[0].set_ylabel('Power')

---

[← Simulate many periodograms from white noise and overlay them](02-simulate-many-periodograms-from-white-noise-and-overlay-them.md) · [Up: contents](index.md) · [(b) Average of K=21 periodograms from independent realizations →](04-b-average-of-k-21-periodograms-from-independent-realizations.md)
