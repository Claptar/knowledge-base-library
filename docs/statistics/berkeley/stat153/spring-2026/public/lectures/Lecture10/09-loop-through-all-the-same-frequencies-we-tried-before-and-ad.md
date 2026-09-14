---
title: Loop through all the same frequencies we tried before and add them to our model
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Loop through all the same frequencies we tried before and add them to our model

**Source:** [`public/lectures/Lecture10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

cols = [np.ones(len(t2))]  # intercept
for f2 in f_grid:
    cols.append(np.cos(2 * np.pi * f2 * t2))
    cols.append(np.sin(2 * np.pi * f2 * t2))

X_overfit_test = np.column_stack(cols)
y_hat_test = np.dot(X_overfit_test, model_overfit.params)

print(X_overfit_test.shape)
print(model_overfit.params.shape)
print(y_hat_test.shape)
```

```
(501, 1001)
(1001,)
(501,)
```

```python
plt.figure(figsize=(5,2))
plt.plot(t, y, label='train')
plt.plot(t, model_overfit.fittedvalues, label='est train data (overfit)')
plt.plot(t2, y_test, label='test data')
plt.plot(t2, y_hat_test, label='est. test data (overfit)')
#plt.legend()

train_RMSE_overfit = np.sqrt(np.mean((model_overfit.resid)**2))
test_RMSE_overfit = np.sqrt(np.mean((y_test - y_hat_test)**2))
print(f'root mean squared error on training data: {train_RMSE_overfit}')
print(f'root mean squared error on test data: {test_RMSE_overfit}')

plt.figure(figsize=(3,3))
plt.plot(y_test, y_hat_test,'.')
plt.xlabel('y_test')
plt.ylabel('yhat_test')
```

```
root mean squared error on training data: 0.1505931704635737
root mean squared error on test data: 4.4126726267868985
Text(0, 0.5, 'yhat_test')
```

*(2 figures omitted — see the original notebook.)*

## The results don't generalize to new data!

While we had many parameters to account for the noise in our training set, the result is that the forecasting performance is pretty terrible! We have massively overfit to noise in our training set. So what instead if we go back to our simpler 3 parameter model and look at training and test performance?

```python

---

[← and calculate predictions based on this seemingly "perfect" model.](08-and-calculate-predictions-based-on-this-seemingly-perfect-mo.md) · [Up: contents](index.md) · [Make a new X matrix with the original fhat we estimated from the training data, and →](10-make-a-new-x-matrix-with-the-original-fhat-we-estimated-from.md)
