---
title: Platelet forecast at day 100
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Platelet forecast at day 100

Let's actually do the forecast up to day 100. The last day of measurements is day 91, so we need to do 9 more steps (0-8):

```python
day_100_idx = 8  # 9 steps ahead, 0-indexed
plt_forecast = fc_mean[day_100_idx, 1]
plt_ci_lo = fc_ci[day_100_idx, 1]
plt_ci_hi = fc_ci[day_100_idx, 4]

print(f"Day 100 log(PLT) forecast: {plt_forecast:.3f}")
print(f"95% CI: [{plt_ci_lo:.3f}, {plt_ci_hi:.3f}]")

# We can also convert the log(PLT) back to actual platelet count,
# which we reference from the paper (Bolwell et al):
print(f"\nBack-transformed (PLT count):")
print(f"  Point estimate: {np.exp(plt_forecast):.0f}")
print(f"  95% CI: [{np.exp(plt_ci_lo):.0f}, {np.exp(plt_ci_hi):.0f}]")
```

## How do we connect these to the 2D tracking demo?

The blood marker model and the 2D tracking model are structurally identical. Both are linear Gaussian state-space models estimated by the Kalman filter/smoother. The key differences can be summarized in the table below:

| | Tracking demo | Blood markers |
|:---|:---|:---|
| $\Phi$ | Fixed by physics (kinematics) | Estimated from data (VAR(1)) |
| $A_t$ | Fixed as $I$ (always observe) | Time-varying: $I$ or $0$ (missing data) |
| $Q, R$ | Set by slider | Estimated via MLE |
| State meaning | Position + velocity | WBC + PLT + HCT |
| Estimation | Filter/smoother only | MLE for parameters, then filter/smoother for states |

In all of these cases, we use the same filter equations, and we also use the same prediction + update with Kalman gain. However, in the case of the first model, we have a physical model and its dynamics we can rely on, while in the second, we have to estimate these parameters.

---

[← Fit the model](03-fit-the-model.md) · [Up: contents](index.md)
