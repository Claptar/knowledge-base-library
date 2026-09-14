---
title: use t2 as our new time observations, then calculate our new estimate of y
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# use t2 as our new time observations, then calculate our new estimate of y

**Source:** [`public/lectures/Lecture10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

cos_col = np.cos(2 * np.pi * f_hat * t2 )
sin_col = np.sin(2 * np.pi * f_hat * t2 )
X = np.column_stack([np.ones(len(t2)), cos_col, sin_col])

y_hat_test_orig = np.dot(X, model.params)
```

## Plot training and testing data

```python
plt.figure(figsize=(8,2))
plt.plot(t, y)
plt.plot(t, model.fittedvalues)

plt.plot(t2, y_test)
plt.plot(t2, y_hat_test_orig, color='k')

train_RMSE = np.sqrt(np.mean((model.resid)**2))
test_RMSE = np.sqrt(np.mean((y_test - y_hat_test_orig)**2))
print(f'root mean squared error on training data: {train_RMSE}')
print(f'root mean squared error on test data: {test_RMSE}')

plt.figure()
plt.plot(t2, y_test - y_hat_test_orig)
plt.plot(t, y - y_hat)
plt.xlabel('Time')
plt.ylabel('residual')
```

```
root mean squared error on training data: 0.44508702979915443
root mean squared error on test data: 0.4424284713076046
Text(0, 0.5, 'residual')
```

*(2 figures omitted — see the original notebook.)*

---

[← Make a new X matrix with the original fhat we estimated from the training data, and](10-make-a-new-x-matrix-with-the-original-fhat-we-estimated-from.md) · [Up: contents](index.md) · [Cross-validation on time series data →](12-cross-validation-on-time-series-data.md)
