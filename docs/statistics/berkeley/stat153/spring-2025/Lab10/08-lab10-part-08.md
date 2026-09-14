---
title: Lab10 Part 08 —
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab10 Part 08 —

**Source:** [`Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

armod_nodiff = AutoReg(ylog_train, lags = 3).fit()
print(np.column_stack([phi_vals, armod_nodiff.params]))
```

```
[[ 0.00924128  0.02014238]
 [ 1.194775    1.17303216]
 [ 0.01035034  0.0029458 ]
 [-0.20512534 -0.17724759]]
```

It is interesting that the parameter estimates are somewhat similar but not exactly the same.

With this AR(3) model for $\log \text{GNP}_t$ that is derived from the AR(2) model for $y_t = \log \text{GNP}_t - \log \text{GNP}_{t-1}$, we can obtain predictions in the usual way as follows.

```python
yhat = np.concatenate([ylog_train.astype(float), np.full(k, -9999)]) # extend data by k placeholder values
p = len(phi_vals) - 1
for i in range(1, k + 1):
    ans = phi_vals[0]
    for j in range(1, p + 1):
        ans += phi_vals[j] * yhat[n_train + i - j - 1]
    yhat[n_train + i - 1] = ans
predvalues = yhat[n_train: ]

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

[← Check that both predictions are identical](07-check-that-both-predictions-are-identical.md) · [Up: contents](index.md)
