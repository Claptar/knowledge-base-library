---
title: Demean for stationarity
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Demean for stationarity

**Source:** [`public/labs/Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

y_hrv = hrv_data - np.mean(hrv_data)

fig, axes = plt.subplots(1, 2, figsize=(14, 4))

plot_acf(y_hrv, lags=40, ax=axes[0], title='ACF — HRV (RR intervals)')
plot_pacf(y_hrv, lags=40, ax=axes[1], title='PACF — HRV (RR intervals)', method='ywm')

plt.tight_layout()
plt.show()
```

### More predictions

Now having seen the ACF and the PACF, what is your best guess for the model? AR(p)? MA(q)? ARMA(p,q)? What orders?

## Results

The ACF decays but not as cleanly as pure AR would predict. The PACF doesn't cut off cleanly either, so this doesn't seem to be a pure AR *or* MA process.

This is what you might expect from ARMA. When you see gradual ACF decay *and* a messy PACF that doesn't cut off cleanly after a certain number of lags, the data likely has both autoregressive feedback and moving-average shock structure.

Let's try each of the models as before.

## AR vs MA vs ARMA

Here we will compare several AR, MA, and ARMA models of various orders. We will use the very naive split that we showed in class, where we will just try to predict the last `t` samples.

```python
t = 10 # Let's try and predict the last t samples

---

[← Also show a zoomed window](09-also-show-a-zoomed-window.md) · [Up: contents](index.md) · [Split our data into training and test data →](11-split-our-data-into-training-and-test-data.md)
