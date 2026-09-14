---
title: use t2 as our new time observations, then calculate our new estimate of y
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# use t2 as our new time observations, then calculate our new estimate of y

**Source:** [`public/labs/Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

cos_col = # FILL IN
sin_col = # FILL IN
X = np.column_stack([np.ones(len(t2)), cos_col, sin_col])

y_hat_test_orig = np.dot(X, model.params)

plt.plot(t, y)
plt.plot(t, model.fittedvalues)

plt.plot(t2, y_test)
plt.plot(t2, y_hat_test_orig)

train_RMSE = np.sqrt(np.mean((model.resid)**2))
test_RMSE = np.sqrt(np.mean((y_test - y_hat_test_orig)**2))
print(f'root mean squared error on training data: {train_RMSE}')
print(f'root mean squared error on test data: {test_RMSE}')

plt.figure()
plt.plot(t2, y_test - y_hat_test_orig)
plt.xlabel('time')
plt.ylabel('Residual')
plt.title('Residuals')
```

## How does this look?

---

[← Make a new X matrix with the original bestf we estimated from the training data, and](13-make-a-new-x-matrix-with-the-original-bestf-we-estimated-fro.md) · [Up: contents](index.md) · [More noise →](15-more-noise.md)
