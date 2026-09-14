---
title: Extract filtered states and standard errors
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Extract filtered states and standard errors

**Source:** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

filtered_state = res.filter_results.filtered_state.T
filtered_cov = res.filter_results.filtered_state_cov
filtered_se = np.sqrt(
    np.array([filtered_cov[i, i, :] for i in range(3)]).T
)

---

[← Helper to extract Q or R from Cholesky parameters](07-helper-to-extract-q-or-r-from-cholesky-parameters.md) · [Up: contents](index.md) · [Extract smoothed states and standard errors →](09-extract-smoothed-states-and-standard-errors.md)
