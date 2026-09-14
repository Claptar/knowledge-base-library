---
title: Extract smoothed states and standard errors
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Extract smoothed states and standard errors

**Source:** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

smoothed_state = res.smoother_results.smoothed_state.T
smoothed_cov = res.smoother_results.smoothed_state_cov
smoothed_se = np.sqrt(
    np.array([smoothed_cov[i, i, :] for i in range(3)]).T
)

---

[← Extract filtered states and standard errors](08-extract-filtered-states-and-standard-errors.md) · [Up: contents](index.md) · [Forecast to day 100 →](10-forecast-to-day-100.md)
