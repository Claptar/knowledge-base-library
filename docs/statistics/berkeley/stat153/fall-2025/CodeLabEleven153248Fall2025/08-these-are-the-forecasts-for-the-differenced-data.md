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
fcast_1 = np.zeros(k)
fcast_1[0] = last_observed_ylog + fcast_diff_1[0]
for i in range(1, k):
    fcast_1[i] = fcast_1[i-1] + fcast_diff_1[i]
```

```python
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_1, label = 'Model One', color = 'red')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Next is Model Two: MA(6) on differenced log data.

```python

---

[← Model One: AR(3) for the differenced log data](07-model-one-ar-3-for-the-differenced-log-data.md) · [Up: contents](index.md) · [Model Two: MA(6) for the differenced log data →](09-model-two-ma-6-for-the-differenced-log-data.md)
