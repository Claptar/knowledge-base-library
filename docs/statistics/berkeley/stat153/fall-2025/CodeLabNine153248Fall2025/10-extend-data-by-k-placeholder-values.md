---
title: extend data by k placeholder values
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabNine153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabNine153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# extend data by k placeholder values

**Source:** [`CodeLabNine153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabNine153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

p = len(phi_vals)-1
for i in range(1, k+1):
    ans = phi_vals[0]
    for j in range(1, p+1):
        ans += phi_vals[j] * yhat[n_train+i-j-1]
    yhat[n_train+i-1] = ans
predvalues = yhat[n_train:]
print(predvalues)
```

```
[10.0401751  10.05858192 10.07752672 10.09423368 10.11061512 10.12647412
 10.14216459 10.15771507 10.17320371 10.18865159 10.20407884 10.21949372
 10.23490196 10.25030637 10.26570866 10.28110976]
```

These predictions coincide with the predictions obtained previously.

```python
plt.figure(figsize = (12, 7))
plt.plot(tme_train, y_train, label = 'Training Data')
plt.plot(tme_test, original_scale_forecast, label = 'Forecast', color = 'black')
plt.plot(tme_test, np.exp(predvalues), label = 'Forecast', color = 'green')
plt.plot(tme_test, y_test, color = 'red',  label = 'Actual future values')
plt.axvline(x=n_train, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The green and black predictions coincide above.

To conclude, predictions from the AR(3) model applied directly to the $\log \text{GNP}$ data are different from the predictions obtained by AR(2) fitted to the differences of $\log \text{GNP}$. It is quite common, while using AR models, to work with differenced data.

---

[← Check that both predictions are identical](09-check-that-both-predictions-are-identical.md) · [Up: contents](index.md)
