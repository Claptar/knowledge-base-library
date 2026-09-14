---
title: To show the confidence intervals on the data, we can use the getprediction
  method
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab3.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# To show the confidence intervals on the data, we can use the getprediction method

**Source:** [`public/labs/Lab3.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab3.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

#
pred = linreg_simple2.get_prediction(T)
pred_ci = pred.conf_int(alpha=0.05)
pred_summary = pred.summary_frame(alpha=0.05)

plt.plot(t,y)
plt.plot(t, pred_summary['mean'])
plt.fill_between(t, pred_summary['mean_ci_lower'], pred_summary['mean_ci_upper'], alpha=0.3, label="95% CI (mean)")
#plt.fill_between(t, pred_summary['obs_ci_lower'], pred_summary['obs_ci_upper'], alpha=0.3, label="95% CI (mean)")

plt.xlabel('t',fontsize=18)
plt.ylabel('y',fontsize=18)
```

```
Text(0, 0.5, 'y')
```

*(1 figure omitted — see the original notebook.)*

For time series, one thing we want to check is that our residuals (the difference between the predicted data and our actual value) are weakly stationary, which allows us to assume that our error $\epsilon_t$ is weakly stationary.

We can do that by plotting the residuals over time as well as the autocorrelation function of the residuals. How does this look?

```python
residuals = linreg_simple2.resid

plt.figure()
plt.plot(t,residuals)
plt.axhline(0, color='k', linewidth=0.5) # Horizontal line at 0
plt.xlabel('t')
plt.ylabel('Residual')

plt.figure(figsize=(10, 5))
plot_acf(residuals, lags=40, title='Autocorrelation Function of Residuals')
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
plt.show()
```

```
<Figure size 1000x500 with 0 Axes>
```

*(2 figures omitted — see the original notebook.)*

## The chicken example

Now let's load some data from `astsa`, for example, the price of chicken over time, from 2001 to 2016. As pointed out in your book, commodities (such as raw materials, basic resources, agricultural, or mining products) show specific fluctuations in their prices over time. For this example, we'll fit a regression model for chicken prices as our response $y$ and time as our predictor $x$.

```python
chicken_data = astsa.load_chicken()

---

[← Show the predictions and confidence intervals](08-show-the-predictions-and-confidence-intervals.md) · [Up: contents](index.md) · [Fix the time index →](10-fix-the-time-index.md)
