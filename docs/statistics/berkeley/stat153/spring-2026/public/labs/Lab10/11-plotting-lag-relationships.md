---
title: Plotting lag relationships
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plotting lag relationships

**Source:** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Now we will plot the average cross-correlation function across features to determine how we want to structure our lags for the regression.

```python
lags_s = lags / fs

---

[← How do we choose the lags?](10-how-do-we-choose-the-lags.md) · [Up: contents](index.md) · [Average |CCF| across features, then show per-electrode traces + mean →](12-average-ccf-across-features-then-show-per-electrode-traces-m.md)
