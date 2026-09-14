---
title: Plot the forecast only (to zoom in)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot the forecast only (to zoom in)

**Source:** [`public/labs/Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure()
plt.plot(y_hrv[start_forecast:], label='true data')
plt.plot(all_forecast, label='forecast')
```

## To try yourself

Try doing this again with some of the worse models -- MA only, AR only, or various other combinations. What do you notice? How do the forecasts break down? What happens if you use a fixed sliding window for the training set? Does that help?

### Why is ARMA good for modeling HRV?

Think about what's generating heart rate variability:

**AR component (autonomic feedback):**
Your heart rate at beat $t$ depends on recent beats through something called the baroreceptor reflex and autonomic regulation. If your heart speeds up, the nervous system must push it back slowly over several beats. This is autoregressive feedback: $x_t$ depends on $x_{t-1}, x_{t-2}$.

**MA component (transient perturbations):**
Each breath modulates heart rate (respiratory sinus arrhythmia). A single breath is a *shock* that affects the current beat and the next beat or two, then vanishes. The current value depends on the current and recent shocks $w_t, w_{t-1}$.

**ARMA captures both**: slow autonomic feedback (AR) + fast respiratory/transient shocks (MA).

This decomposition into "feedback" vs "shock propagation" is broadly useful across multiple fields:
- **Economics**: monetary policy (slow AR feedback) + supply shocks (transient MA)
- **Neuroscience**: ongoing neural dynamics (AR) + stimulus-evoked responses (MA)
- **Climate**: ocean thermal inertia (AR) + weather perturbations (MA)

---

[← Plot the data and forecast](14-plot-the-data-and-forecast.md) · [Up: contents](index.md)
