---
title: Generate k-step ahead forecasts
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Generate k-step ahead forecasts

**Source:** [`Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

k = len(tme_test)
yhat = np.concatenate([y, np.full(k, -9999)]) # extend data by k placeholder values

for i in range(1, k+1):
    ans = armod.params[0]
    for j in range(1, p+1):
        ans += armod.params[j] * yhat[n+i-j-1]

    yhat[n+i-1] = ans

predvalues_ar_high = yhat[n:]
```

```python
pred_error_rms_ar_high = np.sqrt(np.mean((predvalues_ar_high - sunspots_test.iloc[:,1]) ** 2))
print(pred_error_rms_sinusoid, pred_error_rms_yulemod,
      pred_error_rms_ar, pred_error_rms_ar_high)
```

```
79.83531765284938 79.52702577862316 70.32365837557232 50.162969939451386
```

With $p = 12$, the prediction accuracy is much better compared to $p = 2$ (as well as models 1 and 2).

```python
plt.figure(figsize = (12, 6))
plt.xlabel('Time')
plt.ylabel('Count')
plt.plot(tme, sunspots.iloc[:,1], color = "None")
plt.plot(tme_train, y, color = 'black', label = 'Training data')
plt.plot(tme_test, sunspots_test.iloc[:,1], color = 'red', label = 'Test Data')
#plt.plot(tme_test, pred_test, color = 'blue', label = 'Predictions (Model One)')
#plt.plot(tme_test, predvalues_yulemod, color = 'green', label = 'Predictions (Model Two)')
plt.plot(tme_test, predvalues_ar, color = 'yellow', label = 'Predictions (AR(2))')
plt.plot(tme_test, predvalues_ar_high, color = 'pink', label = 'Predictions (AR(p) for high p)')
plt.legend()
plt.title('Sunspots Data')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Generate k-step ahead forecasts](04-generate-k-step-ahead-forecasts.md) · [Up: contents](index.md)
