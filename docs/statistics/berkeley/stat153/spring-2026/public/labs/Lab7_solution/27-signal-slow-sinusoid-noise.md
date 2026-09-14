---
title: 'Signal: slow sinusoid + noise'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Signal: slow sinusoid + noise

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

signal = 4*np.cos(2*math.pi*t*5/n)  # 5 cycles over n points
noise = np.random.normal(0, 6, n)
x = signal + noise

---

[← effectively doubling the values.](26-effectively-doubling-the-values.md) · [Up: contents](index.md) · [Apply a moving average filter of order m →](28-apply-a-moving-average-filter-of-order-m.md)
