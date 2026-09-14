---
title: Platelet forecast at day 100
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Platelet forecast at day 100

**Source:** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Let's actually do the forecast up to day 100. The last day of measurements is day 91, so we need to do 9 more steps (0-8):

```python
day_100_idx = 8  # 9 steps ahead, 0-indexed
plt_forecast = fc_mean[day_100_idx, 1]
plt_ci_lo = fc_ci[day_100_idx, 1]
plt_ci_hi = fc_ci[day_100_idx, 4]

print(f"Day 100 log(PLT) forecast: {plt_forecast:.3f}")
print(f"95% CI: [{plt_ci_lo:.3f}, {plt_ci_hi:.3f}]")

---

[← Widgets](12-widgets.md) · [Up: contents](index.md) · [We can also convert the log(PLT) back to actual platelet count, →](14-we-can-also-convert-the-log-plt-back-to-actual-platelet-coun.md)
