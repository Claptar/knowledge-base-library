---
title: (b) Average of K=21 periodograms from independent realizations
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# (b) Average of K=21 periodograms from independent realizations

**Source:** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

avg_power = np.zeros_like(power_single)
for rep in range(K):
    wn = np.random.normal(0, np.sqrt(sigma2), n)
    _, pw = periodogram(wn, fs=1)
    avg_power += pw
avg_power /= K
axes[1].plot(freqs, avg_power, color='steelblue', lw=1.2)
axes[1].axhline(2 * sigma2, color='r', lw=2)
axes[1].set_title(f'(b) Average of {K} independent\nperiodograms')
axes[1].set_ylim([0, 10])
axes[1].set_xlabel('Frequency')

---

[← (a) Single raw periodogram](03-a-single-raw-periodogram.md) · [Up: contents](index.md) · [(c) Daniell-smoothed periodogram from single realization →](05-c-daniell-smoothed-periodogram-from-single-realization.md)
