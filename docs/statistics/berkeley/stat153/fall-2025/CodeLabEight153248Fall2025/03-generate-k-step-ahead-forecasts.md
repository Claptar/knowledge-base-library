---
title: Generate k-step ahead forecasts
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEight153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabEight153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Generate k-step ahead forecasts

**Source:** [`CodeLabEight153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabEight153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

k = len(tme_test)
yhat = np.concatenate([y, np.full(k, -9999)]) # extend data by k placeholder values
for i in range(1, k+1):
    ans = yulemod.params[0] - yhat[n+i-3]
    ans += yulemod.params[1] * yhat[n+i-2]
    yhat[n+i-1] = ans
predvalues_yulemod = yhat[n:]
print(predvalues_yulemod)
```

```
[146.06104972  75.38685636   4.49010921 -40.73521796 -43.77125261
  -3.50912861  65.34601702 137.64587487 186.98400606 195.34039803
 159.66300392  92.98245693  19.65282692 -33.5433384  -47.17693735
 -16.26850237  47.89312417 121.87387032 178.65337795 197.49378336
 171.513911   110.20251965  35.9526756  -24.11697905 -48.06690374
 -27.14974761  30.99481172 105.13034589 168.17996275 197.11573524
 181.36930636 126.69182313  53.05341637 -12.65059012 -46.42279325
 -35.92840227  14.99966389  87.76069276 155.77980967 194.21405216
 189.02588952 142.11022034  70.60228927   0.6192958  -42.27852115
 -42.42337723   0.23763408  70.12321812 141.70871333 188.84859105
 194.32571784 156.13965529  88.2372901   15.41894292 -35.71957693
 -46.50069192 -12.98676148  52.58175387 126.25693714 181.13003247
 197.15946465 168.49072395 105.59463801  31.44305903 -26.88126073
 -48.07623808 -24.4007254   35.49815135 109.74322567 171.21759752
 197.46867444 178.90864425 122.31627964  48.36109315 -15.94589238]
```

```python
plt.figure(figsize = (12, 6))
plt.xlabel('Time')
plt.ylabel('Count')
plt.plot(tme, sunspots.iloc[:,1], color = "None")
plt.plot(tme_train, y, color = 'black', label = 'Training data')
plt.plot(tme_test, sunspots_test.iloc[:,1], color = 'red', label = 'Test Data')
#plt.plot(tme_test, pred_test, color = 'blue', label = 'Predictions (Model One)')
plt.plot(tme_test, predvalues_yulemod, color = 'green', label = 'Predictions (Model Two)')
plt.legend()
plt.title('Sunspots Data')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
pred_error_rms_yulemod = np.sqrt(np.mean((predvalues_yulemod - sunspots_test.iloc[:,1]) ** 2))
print(pred_error_rms_sinusoid, pred_error_rms_yulemod)

---

[← Prediction error](02-prediction-error.md) · [Up: contents](index.md) · [CodeLabEight153248Fall2025 Part 04 — →](04-codelabeight153248fall2025-part-04.md)
