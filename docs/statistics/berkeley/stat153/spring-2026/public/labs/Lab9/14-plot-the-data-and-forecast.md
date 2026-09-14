---
title: Plot the data and forecast
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot the data and forecast

**Source:** [`public/labs/Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure()
plt.plot(np.arange(len(y_hrv[:start_forecast]), len(y_hrv[:start_forecast])+len(y_hrv[start_forecast:])), y_hrv[start_forecast:], label='true data')
plt.plot(np.arange(len(y_hrv[:start_forecast]), len(y_hrv[:start_forecast])+len(all_forecast)), all_forecast, label='forecast')
plt.plot(y_hrv[:start_forecast])
plt.axvline(start_forecast, color='r', linestyle='--')
plt.legend()

---

[← Keep adding data to the forecast, starting our forecast at startforecast](13-keep-adding-data-to-the-forecast-starting-our-forecast-at-st.md) · [Up: contents](index.md) · [Plot the forecast only (to zoom in) →](15-plot-the-forecast-only-to-zoom-in.md)
