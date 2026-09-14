---
title: Lab7 solution Part 07 —
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab7 solution Part 07 —

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fft_numpy = np.fft.fft(x)
j_vals = np.arange(n)
d_numpy = 1/np.sqrt(n) * fft_numpy * np.exp(-1j * 2 * math.pi * j_vals / n)

---

[← Our convention uses t=1,...,n and 1/sqrt(n)](06-our-convention-uses-t-1-n-and-1-sqrt-n.md) · [Up: contents](index.md) · [Check they match →](08-check-they-match.md)
