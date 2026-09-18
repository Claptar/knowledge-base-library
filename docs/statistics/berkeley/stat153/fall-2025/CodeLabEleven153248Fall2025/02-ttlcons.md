---
title: TTLCONS
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLabEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEleven153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# TTLCONS

In Lecture 21, we fit ARIMA models to the following dataset.

```python
ttlcons = pd.read_csv('TTLCONS_13Nov2025.csv')
print(ttlcons.head())
y = ttlcons['TTLCONS'].to_numpy()
print(len(y))
plt.plot(y)
plt.title('Total Construction Spending')
plt.xlabel('Time (months)')
plt.show()
```

```
observation_date  TTLCONS
0       1993-01-01   458080
1       1993-02-01   462967
2       1993-03-01   458399
3       1993-04-01   469425
4       1993-05-01   468998
391
```

*(1 figure omitted — see the original notebook.)*

Let us revisit that analysis here again. We fit models to the logarithm of the data.

```python
ylog = np.log(y)
plt.plot(ylog, color = 'black')
plt.title('Log of Total Construction Spending')
plt.xlabel('Time (months)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We can obtain candidate models by differencing the data, and looking at acf and pacf.

```python
ylogdiff = 100 * np.diff(ylog)
plt.plot(ylogdiff, color = 'black')
plt.title('Percent change in Total Construction Spending')
plt.xlabel('Time (months)')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))
plot_acf(ylogdiff, lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF")
plot_pacf(ylogdiff, lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF")
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

These plots suggest:
1. AR(3) for the differenced log data
2. MA(6) for the differenced log data
3. ARIMA(3, 1, 0) for the log data (this is technically the same as Model 1 but the ARIMA function does not include intercepts while fitting this model so it can lead to different predictions)
4. ARIMA(0, 1, 6) for the log data

We can also take another difference of the data, and then look at acf and pacf.

```python
ylogdiff2 = np.diff(np.diff(ylog))
plt.plot(ylogdiff2)
plt.title("Double Differenced Data")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
h_max = 50
fig, axes = plt.subplots(nrows = 2, ncols = 1)
plot_acf(ylogdiff2, lags = h_max, ax = axes[0])
axes[0].set_title("Sample ACF")
plot_pacf(ylogdiff2, lags = h_max, ax = axes[1])
axes[1].set_title("Sample PACF")
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

This suggests the ARIMA(0, 2, 1) model for ylog.

Here is how to calculate the predictions for each of the five models.

```python
k = 100
n = len(ylog)
tme = range(1, n+1)
tme_future = range(n+1, n+k+1)
```

First is Model One: AR(3) for the differenced log data.

```python
# Model One: AR(3) for the differenced log data
md1 = ARIMA(ylogdiff, order = (3, 0, 0)).fit()
fcast_diff_1 = (md1.get_prediction(start = n-1, end = n+k-2).predicted_mean)/100
# these are the forecasts for the differenced data
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
# Model Two: MA(6) for the differenced log data
md2 = ARIMA(ylogdiff, order = (0, 0, 6)).fit()
fcast_diff_2 = (md2.get_prediction(start = n-1, end = n+k-2).predicted_mean)/100
# these are the forecasts for the differenced data
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
# Model Three: ARIMA(3, 1, 0) for the log data
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

[← AR model fitting: AutoReg vs ARIMA](01-ar-model-fitting-autoreg-vs-arima.md) · [Up: contents](index.md)
