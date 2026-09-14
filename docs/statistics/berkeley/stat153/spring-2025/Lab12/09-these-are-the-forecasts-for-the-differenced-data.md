---
title: these are the forecasts for the differenced data
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# these are the forecasts for the differenced data

**Source:** [`Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

last_observed_y = y.iloc[-1]
fcast_1 = np.zeros(k)
fcast_1[0] = last_observed_y + fcast_diff_1[0]
for i in range(1, k):
    fcast_1[i] = fcast_1[i-1] + fcast_diff_1[i]
```

Next we obtain the forecasts using mod1 (which was fitted using ARIMA(3, 0, 0)).

```python
n = len(y)
k = 100
fcast_diff_1_arima = mod1.get_prediction(start=n-1, end=n+k-2).predicted_mean

---

[← but the remaining estimates are almost the same.](08-but-the-remaining-estimates-are-almost-the-same.md) · [Up: contents](index.md) · [these are the forecasts for the differenced data →](10-these-are-the-forecasts-for-the-differenced-data.md)
