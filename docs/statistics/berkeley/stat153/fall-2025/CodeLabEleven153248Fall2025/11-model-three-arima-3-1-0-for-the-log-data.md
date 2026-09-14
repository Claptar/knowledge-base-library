---
title: 'Model Three: ARIMA(3, 1, 0) for the log data'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Model Three: ARIMA(3, 1, 0) for the log data

**Source:** [`CodeLabEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

md3 = ARIMA(ylog, order = (3, 1, 0)).fit()
fcast_3 = md3.get_prediction(start = n, end = n+k-1).predicted_mean
```

```python
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_1, label = 'Model One', color = 'red')
plt.plot(tme_future, fcast_2, label = 'Model Two', color = 'green')
plt.plot(tme_future, fcast_3, label = 'Model Three', color = 'black')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The lack of intercept is leading to flat predictions.

```python
#Model Four: ARIMA(0, 1, 6) for the log data
md4 = ARIMA(ylog, order = (0, 1, 6)).fit()
fcast_4 = md4.get_prediction(start = n, end = n+k-1).predicted_mean
```

```python
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_1, label = 'Model One', color = 'red')
plt.plot(tme_future, fcast_2, label = 'Model Two', color = 'green')
plt.plot(tme_future, fcast_3, label = 'Model Three', color = 'black')
plt.plot(tme_future, fcast_4, label = 'Model Four', color = 'orange')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The forecasts for models 3 and 4 are largely similar.

Finally below are the predictions for model 5.

```python
#Model Four: ARIMA(0, 2, 1) for the log data
md5 = ARIMA(ylog, order = (0, 2, 1)).fit()
fcast_5 = md5.get_prediction(start = n, end = n+k-1).predicted_mean
```

```python
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_1, label = 'Model One', color = 'red')
plt.plot(tme_future, fcast_2, label = 'Model Two', color = 'green')
plt.plot(tme_future, fcast_3, label = 'Model Three', color = 'black')
plt.plot(tme_future, fcast_4, label = 'Model Four', color = 'orange')
plt.plot(tme_future, fcast_5, label = 'Model Five', color = 'darkgreen')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us try to manually fit the AR(1) model to the double differenced data (so the model will involve an intercept), and then manually convert the predictions on the double differenced data to predictions on the original data.

```python
md6 = ARIMA(ylogdiff2, order = (0, 0, 1)).fit()
fcast_diff_6 = md6.get_prediction(start = n-2, end = n+k-3).predicted_mean
```

```python
tmp1 = ylog[-1] - ylog[-2]
fcast_d1 = np.zeros(k)
fcast_d1[0] = tmp1 + fcast_diff_6[0]
for i in range(1, k):
    fcast_d1[i] = fcast_d1[i-1] + fcast_diff_6[i]
```

```python
tmp2 = ylog[-1]
fcast_6 = np.zeros(k)
fcast_6[0] = tmp2 + fcast_d1[0]
for i in range(1, k):
    fcast_6[i] = fcast_6[i-1] + fcast_d1[i]
```

```python
plt.plot(tme, ylog, label = 'Data')
plt.plot(tme_future, fcast_1, label = 'Model One', color = 'red')
plt.plot(tme_future, fcast_2, label = 'Model Two', color = 'green')
plt.plot(tme_future, fcast_3, label = 'Model Three', color = 'black')
plt.plot(tme_future, fcast_4, label = 'Model Four', color = 'orange')
plt.plot(tme_future, fcast_5, label = 'Model Five', color = 'darkgreen')
plt.plot(tme_future, fcast_6, label = 'Model Six', color = 'darkblue')
plt.axvline(x=n, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

All these models seem to give quite different predictions. Which prediction do you like?

---

[← these are the forecasts for the differenced data](10-these-are-the-forecasts-for-the-differenced-data.md) · [Up: contents](index.md)
