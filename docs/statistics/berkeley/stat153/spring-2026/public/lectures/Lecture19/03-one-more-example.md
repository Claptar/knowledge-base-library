---
title: One more example
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture19.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture19.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# One more example

Let's look at one more example from the Shumway and Stoffer book. This dataset gives the thickness of the yearly varves collected from one location in Massachusetts for 634 years (beginning 11,834 years ago!). Varves are sedimentary deposits of sand and silt that are deposited by melting glaciers during the spring melting seasons (see Example 2.8 of the Shumway-Stoffer book, 5th edition). These deposits can be used as proxies for paleoclimatic parameters, such as temperature, because, in a warm year, more sand and silt are deposited from the receding glacier.

```python
varve_data = pd.read_csv('varve.csv')

yraw = varve_data['x']
#plt.figure(figsize = (10, 8))
plt.plot(yraw)
plt.xlabel('Time')
plt.ylabel('Thickness')
plt.title('Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## More plot diagnostics

From just looking at the plot, it appears that the variance may be nonstationary. We can also look at the QQ-plot, which shows us whether the data come from an underlying distribution (default: normal), and whether they violate the assumption of homoscedasticity. Here, we'll see that the QQ plot deviates significantly from the line, so we probably do need a variance stabilizing transform (like the logarithm).

```python
from statsmodels.graphics.gofplots import qqplot

plt.figure()
qqplot(yraw, fit=True, line="45");
```

```
<Figure size 1200x400 with 0 Axes>
```

*(1 figure omitted — see the original notebook.)*

If we log-transform the data, this will be better behaved.

```python
#Log transform the data first
ylog = np.log(yraw)
#plt.figure(figsize = (12, 6))
plt.plot(ylog)
plt.xlabel('Time')
plt.ylabel('log(Thickness)')
plt.title('Logarithm of Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure()
qqplot(ylog, fit=True, line="45");
```

```
<Figure size 1200x400 with 0 Axes>
```

*(1 figure omitted — see the original notebook.)*

## ACF and PACF

In addition to the log transform, we're going to difference our data, then look at the ACF and PACF to see what to do next.

```python
ylogdiff = np.diff(ylog)
#plt.figure(figsize = (12, 6))
plt.plot(ylogdiff)
plt.xlabel('Time')
plt.ylabel('diff(log(Thickness))')
plt.title('Differenced Logarithm of Glacial Varve Thickness')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 4))

plot_acf(ylogdiff, lags=40, ax=axes[0], title='ACF - diff(log(thickness))')
plot_pacf(ylogdiff, lags=40, ax=axes[1], title='PACF - diff(log(thickness))', method='ywm')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Function |  AR(p)    | MA(q)                | ARMA(p,q)
---------|-----------|----------------------|----------
ACF      | tails off | cuts off after lag q | tails off
PACF     | cuts off after lag p | tails off | tails off

*What kind of model should we try?*

```python
h = 20
y_train = ylog[:-h]
y_test = ylog[-h:]

times = np.arange(len(ylog))
times_train = times[:-h]
times_test = times[-h:]

# ---- 3. Model grid ----
specs = [
    (1, 0, 0), (2, 0, 0), (3, 0, 0), # AR
    (0, 0, 1), (0, 0, 2), (0, 0, 3), # MA
    (0, 1, 1), (0, 1, 2), (0, 1, 3), #
    (1, 0, 1), (2, 0, 1), (3, 0, 1), # ARMA
    (1, 1, 0), (2, 1, 0), (3, 1, 0), # ARIMA
]

# ---- 4. Fit, forecast, score ----
results = []
fits = {}
for (p, d, q) in specs:
    try:
        if d == 0:
            trend = 'c'
        elif d == 1:
            trend = 'n'
        else:
            trend = 'n'
        fit = ARIMA(y_train, order=(p, d, q), trend=trend).fit()
        fcast = fit.get_forecast(steps=h)
        mean = np.asarray(fcast.predicted_mean)
        ci = np.asarray(fcast.conf_int(alpha=0.05))
        rmse = np.sqrt(np.mean((mean - y_test) ** 2))
        results.append({
            'spec': f'ARIMA({p},{d},{q})',
            'p': p, 'd': d, 'q': q,
            'n_params': p + q,
            'rmse': rmse,
        })
        fits[(p, d, q)] = (mean, ci)
    except Exception as e:
        print(f'ARIMA({p},{d},{q}) failed: {e}')

df = pd.DataFrame(results)

plt.figure()

# RMSE vs. complexity
colors = {0: 'C0', 1: 'C3', 2: 'C2'}

for d_val in sorted(df['d'].unique()):
    sub = df[df['d'] == d_val]
    plt.scatter(sub['n_params'], sub['rmse'],
               c=colors[d_val], s=80,
               label=f'd = {d_val}', edgecolor='k', linewidth=0.5)
    for _, row in sub.iterrows():
        plt.gca().annotate(row['spec'], (row['n_params'], row['rmse']),
                    xytext=(5, 5), textcoords='offset points')

plt.xlabel('# ARMA parameters (p + q)')
plt.gca().set_xticks(np.arange(1,5))
plt.ylabel(f'RMSE')
plt.title('Forecast accuracy vs. model complexity')
plt.legend(title='Differencing', loc='upper right')
plt.grid(alpha=0.3)

# Forecast

plt.figure()
context = 40 # Quarters to look back in the past (zooming in)
plt.plot(times_train[-context:], y_train[-context:],
        color='black', lw=1.2, label='Training (recent)')
plt.plot(times_test, y_test, color='black', lw=2, label='Held-out actual')

highlight = {
    (0, 0, 1): ('MA(2)', 'C0'),
    (0, 1, 1): ('ARIMA(0,1,1)', 'C3'),
    (1, 1, 1): ('ARIMA(1,1,1)', 'C2'),
}

for spec, (label, color) in highlight.items():
    if spec not in fits:
        continue
    mean, ci = fits[spec]
    plt.plot(times_test, mean, color=color, lw=1.8, label=label)
    plt.fill_between(times_test, ci[:, 0], ci[:, 1], color=color, alpha=0.15)

plt.axvline(times_test[0], color='gray', ls='--', lw=0.8)
plt.xlabel('Date')
plt.ylabel('log(GDP)')
plt.title(f'{h}-quarter forecasts with 95% intervals')
plt.legend(loc='upper left')
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

*(2 figures omitted — see the original notebook.)*

```python
p=0
d=1
q=1
fit = ARIMA(y_train, order=(p, d, q), trend=trend).fit()

fig = plt.figure(figsize=(10,6))
fit.plot_diagnostics(fig=fig);
plt.tight_layout()
```

*(1 figure omitted — see the original notebook.)*

---

[← Fitting the model](02-fitting-the-model.md) · [Up: contents](index.md) · [Ljung-Box p-values →](04-ljung-box-p-values.md)
