---
title: which we reference from the paper (Bolwell et al)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# which we reference from the paper (Bolwell et al)

**Source:** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

[← We can also convert the log(PLT) back to actual platelet count,](14-we-can-also-convert-the-log-plt-back-to-actual-platelet-coun.md) · [Up: contents](index.md)
