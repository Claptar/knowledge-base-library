---
title: Only plot up to the Nyquist frequency (j = 0, ..., n/2)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Only plot up to the Nyquist frequency (j = 0, ..., n/2)

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

freqs_manual = np.arange(n // 2 + 1) / n  # frequencies j/n

---

[← TODO: Fill in the periodogram formula](10-todo-fill-in-the-periodogram-formula.md) · [Up: contents](index.md) · [Compare with scipy periodogram (fs=1 so frequencies are in cycles/sample) →](12-compare-with-scipy-periodogram-fs-1-so-frequencies-are-in-cy.md)
