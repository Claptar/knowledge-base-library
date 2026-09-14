---
title: Lab4 Part 16 —
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab4 Part 16 —

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

rss_chat = np.sum(md.resid ** 2)
sigma_mle = np.sqrt(rss_chat / n)
sigma_unbiased = np.sqrt((rss_chat) / (n - 3))
print(np.array([sigma_mle, sigma_unbiased]))

---

[← Estimates of other parameters](15-estimates-of-other-parameters.md) · [Up: contents](index.md) · [sig is the true value of sigma which generated the data →](17-sig-is-the-true-value-of-sigma-which-generated-the-data.md)
