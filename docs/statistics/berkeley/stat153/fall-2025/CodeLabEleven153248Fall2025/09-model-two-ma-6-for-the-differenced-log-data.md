---
title: 'Model Two: MA(6) for the differenced log data'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Model Two: MA(6) for the differenced log data

**Source:** [`CodeLabEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

md2 = ARIMA(ylogdiff, order = (0, 0, 6)).fit()
fcast_diff_2 = (md2.get_prediction(start = n-1, end = n+k-2).predicted_mean)/100

---

[← these are the forecasts for the differenced data](08-these-are-the-forecasts-for-the-differenced-data.md) · [Up: contents](index.md) · [these are the forecasts for the differenced data →](10-these-are-the-forecasts-for-the-differenced-data.md)
