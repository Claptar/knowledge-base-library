---
title: What about new data?
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# What about new data?

We have fit our data using the sinusoid pretty successfully here. What if we tried to use this as a predictive model to forecast new data? Let's try generating some new data in the future from the same underlying sinusoid, then use the coefficients that we fit above on our "training set" to fit the new "test set" data.

```python
# Generate some new data for some new time points in the future $t2$
duration2 = 1
t2 = np.arange(t[-1],t[-1]+duration2,step=1/fs)

y_test = B0 + R*np.cos(2*math.pi*f*t2 + phi) + np.sqrt(var_eps)*np.random.randn(len(t2))

plt.plot(t, y, label='original training')
plt.plot(t2, y_test, label='new test data')
plt.legend()
plt.xlabel('t')
plt.ylabel('value');
```

```python
# Make a new X matrix with the original best_f we estimated from the training data, and
# use t2 as our new time observations, then calculate our new estimate of y
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

### How does this look?

## More noise

Now try re-running the analysis above using a higher noise level (i.e. set `var_eps` to be much larger for the error variance). What do you notice? Fill in your edited code below, and first try doing a grid search over all frequencies from 0 to the Nyquist limit.

When do things break down?

```python
# REMAKE THE SINUSOID WITH NEW PARAMETERS AND PLOT IT
# FILL IN
```

```python
# TEST SOME FREQUENCIES from 0 to the Nyquist limit and choose the best one, and plot y and yhat again.
```

---

[← Estimating the original parameters of the sinusoid](03-estimating-the-original-parameters-of-the-sinusoid.md) · [Up: contents](index.md)
