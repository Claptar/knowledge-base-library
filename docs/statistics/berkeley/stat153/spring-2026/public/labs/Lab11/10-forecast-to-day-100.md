---
title: Forecast to day 100
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Forecast to day 100

**Source:** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fc = res.get_forecast(steps=9)
fc_mean = fc.predicted_mean
fc_ci = fc.conf_int()

---

[← Extract smoothed states and standard errors](09-extract-smoothed-states-and-standard-errors.md) · [Up: contents](index.md) · [Plot function →](11-plot-function.md)
