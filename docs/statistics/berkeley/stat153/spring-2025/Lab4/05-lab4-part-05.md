---
title: Lab4 Part 05 —
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab4 Part 05 —

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

b0_est = md.params[0]
b1_est = md.params[1]
b2_est = md.params[2]
print(np.column_stack((np.array([b0_est, b1_est, b2_est]), np.array([b0, b1, b2]))))

rss_fhat = np.sum(md.resid ** 2)
sigma_mle = np.sqrt(rss_fhat / n)
sigma_unbiased = np.sqrt((rss_fhat)/(n - 3))
print(np.array([sigma_mle, sigma_unbiased, sig]))

---

[← Lab4 Part 04 —](04-lab4-part-04.md) · [Up: contents](index.md) · [sig is the true value of sigma which generated the data →](06-sig-is-the-true-value-of-sigma-which-generated-the-data.md)
