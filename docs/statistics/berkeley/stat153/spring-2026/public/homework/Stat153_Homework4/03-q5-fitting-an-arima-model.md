---
title: Q5. Fitting an ARIMA model
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_Homework4.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat153_Homework4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/homework/Stat153_Homework4.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_Homework4.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Q5. Fitting an ARIMA model

Q5a. Fit an ARIMA($p,d,q$) model to the global temperature data `gtemp_land`, loaded from `astsa` as below. Perform all the necessary diagnostics for the model, and decide on an appropriate model. Comment on why you decided on the model.

```python
gtemp_land = astsa.load_gtemp_land()

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Plot the data and diagnostics, decide on model
```

**Answer:** An ARIMA(0,1,1) should fit the data well. We know we need to do differencing because the original time series is not stationary (it has a trend / appears to be growing with time). After applying $d=1$ order differencing, we calculate the ACF and PACF and see a peak in the ACF and a slower tail off in the PACF, which suggests an MA term. The order of the MA term is found through the peak in the ACF (where it cuts off), which is 1.

Q5b. After deciding on the model, forecast (with 95% CI) the next 10 years, and comment on what you found. Hint: you should use `trend='t'` if using the ARIMA function from statsmodels. Also use the method `get_forecast` once you fit your model to perform the forecasting.

```python
model = ARIMA(## FILL IN...

fc = model.get_forecast(steps=10)

# Get mean and confidence intervals and print them
# FILL IN

# Plot the original data and the forecast including shaded confidence intervals.
```

---

[← Q2. ARMA model parameterization](02-q2-arma-model-parameterization.md) · [Up: contents](index.md) · [Q6. The covariance matrix $X^T X$ and time-lagged ridge regression →](04-q6-the-covariance-matrix-and-time-lagged-ridge-regression.md)
