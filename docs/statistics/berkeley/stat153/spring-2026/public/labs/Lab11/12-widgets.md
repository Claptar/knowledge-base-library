---
title: Widgets
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Widgets

**Source:** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

obs_w = Checkbox(value=True, description='Observed')
filt_w = Checkbox(value=True, description='Filtered')
smooth_w = Checkbox(value=True, description='Smoothed')
fc_w = Checkbox(value=True, description='Forecast')
ci_w = Checkbox(value=True, description='95% CI bands')

out = interactive_output(plot_blood, {
    'show_observed': obs_w,
    'show_filtered': filt_w,
    'show_smoothed': smooth_w,
    'show_forecast': fc_w,
    'show_ci': ci_w,
})

display(VBox([HBox([obs_w, filt_w, smooth_w, fc_w, ci_w]), out]))
```

### What do we see in these plots?

1. **Confidence intervals widen in missing-data regions** (gray bands) because no update step occurs. We can only use the dynamics, and $P_t$ grows via the $+Q$ term at each predict step. When the next observation arrives, $P_t$ snaps back down.

2. **WBC and PLT** are smoothly estimated with tight CIs even when there is missing data. Their small $Q$ entries mean the model treats them as slowly varying.

3. **HCT** has much wider CIs, consistent with its large $Q_{33}$ and $R_{33}$. Biologically, hematocrit is more variable and harder to measure precisely.

4. **Forecasts** (dashed lines past day 91) converge toward the long-run mean with widening CIs. The platelet forecast at day 100 is a clinically relevant quantity that is correlated with long term survival. In particular, research has shown a good prognosis for a total platelet count > 50 (log platelet count > 3.91) ([Bolwell et al. 2004](https://www.nature.com/articles/1704330).)

---

[← Plot function](11-plot-function.md) · [Up: contents](index.md) · [Platelet forecast at day 100 →](13-platelet-forecast-at-day-100.md)
