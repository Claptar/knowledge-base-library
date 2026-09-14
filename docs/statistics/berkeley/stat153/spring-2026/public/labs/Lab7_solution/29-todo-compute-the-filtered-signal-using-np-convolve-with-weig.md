---
title: 'TODO: Compute the filtered signal using np.convolve with weights 1/m'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# TODO: Compute the filtered signal using np.convolve with weights 1/m

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

weights = np.ones(m) / m
y = np.convolve(x, weights, mode='valid')  # FILL IN: use np.convolve(x, weights, mode='valid')

---

[← Apply a moving average filter of order m](28-apply-a-moving-average-filter-of-order-m.md) · [Up: contents](index.md) · [Plot time domain →](30-plot-time-domain.md)
