---
title: these are the forecasts for the differenced data
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# these are the forecasts for the differenced data

**Source:** [`CodeLabEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

last_observed_ylog = ylog[-1]
fcast_2 = np.zeros(k)
fcast_2[0] = last_observed_ylog + fcast_diff_2[0]
for i in range(1, k):
    fcast_2[i] = fcast_2[i-1] + fcast_diff_2[i]
```

```python
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_1, label = 'Model One', color = 'red')
plt.plot(tme_future, fcast_2, label = 'Model Two', color = 'green')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

So Model One and Model Two lead to basically the same predictions.

Next is Model Three which ARIMA(3, 1, 0).

```python

---

[← Model Two: MA(6) for the differenced log data](09-model-two-ma-6-for-the-differenced-log-data.md) · [Up: contents](index.md) · [Model Three: ARIMA(3, 1, 0) for the log data →](11-model-three-arima-3-1-0-for-the-log-data.md)
