---
title: 'Model One: AR(3) for the differenced log data'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Model One: AR(3) for the differenced log data

**Source:** [`CodeLabEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

md1 = ARIMA(ylogdiff, order = (3, 0, 0)).fit()
fcast_diff_1 = (md1.get_prediction(start = n-1, end = n+k-2).predicted_mean)/100

---

[← AutoReg's estimate of phi1 is slightly more than 1](06-autoreg-s-estimate-of-phi1-is-slightly-more-than-1.md) · [Up: contents](index.md) · [these are the forecasts for the differenced data →](08-these-are-the-forecasts-for-the-differenced-data.md)
