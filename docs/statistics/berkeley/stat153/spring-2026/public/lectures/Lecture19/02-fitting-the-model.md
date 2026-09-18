---
title: Fitting the model
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture19.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture19.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Fitting the model

First we will fit up until the last 20 quarters (5 years) of data and forecast to the latest 5, using several different models that incorporate AR(), MA(), and differencing terms, and comparing them

```python
# ---- 2. Train/test split ----
h = 20 # 5 years of data

y_train = y_gdp[:-h] # take up to the last five years
y_test = y_gdp[-h:]  # predict last five years
dates_train = gdp.index[:-h]
dates_test = gdp.index[-h:]

# ---- 3. Model grid ----
specs = [
    (1, 0, 0), (2, 0, 0), (3, 0, 0), # p, d, q - AR models
    (1, 0, 1), (2, 0, 1), (3, 0, 1), # ARMA models
    (1, 1, 0), (2, 1, 0), (3, 1, 0), # ARI (differencing, no MA)
    (1, 1, 1), (2, 1, 1), (3, 1, 1), # ARIMA d=1
    (1, 2, 1), (2, 2, 1), (3, 2, 1), # ARIMA d=2
]

# ---- 4. Fit, forecast, score ----
results = []
fits = {}
for (p, d, q) in specs:
    try:
        if d == 0:
            trend = 'c'
        elif d == 1:
            trend = 't'   # was 'n'
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
plt.plot(dates_train[-context:], y_train[-context:],
        color='black', lw=1.2, label='Training (recent)')
plt.plot(dates_test, y_test, color='black', lw=2, label='Held-out actual')

highlight = {
    (2, 0, 0): ('AR(2)', 'C0'),
    (1, 1, 1): ('ARIMA(1,1,1)', 'C3'),
    (1, 2, 1): ('ARIMA(1,2,1)', 'C2'),
}

for spec, (label, color) in highlight.items():
    if spec not in fits:
        continue
    mean, ci = fits[spec]
    plt.plot(dates_test, mean, color=color, lw=1.8, label=label)
    plt.fill_between(dates_test, ci[:, 0], ci[:, 1], color=color, alpha=0.15)

plt.axvline(dates_test[0], color='gray', ls='--', lw=0.8)
plt.xlabel('Date')
plt.ylabel('log(GDP)')
plt.title(f'{h}-quarter forecasts with 95% intervals')
plt.legend(loc='upper left')
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

*(2 figures omitted — see the original notebook.)*

### Changes in linear trends

Here our data includes the COVID-19 pandemic years in the training set, where there were strong changes to the linear trend in GDP that can't be captured by first order differencing. What if we restrict our time points to pre-COVID?

```python
# ---- 2. Train/test split ----
# Truncate to pre-COVID
mask = gdp.index <= '2019-12-31'
y_pre = y_gdp[mask]
dates_pre = gdp.index[mask]

h = 20
y_train = y_pre[:-h]
y_test = y_pre[-h:]
dates_train = dates_pre[:-h]
dates_test = dates_pre[-h:]

# ---- 3. Model grid ----
specs = [
    (1, 0, 0), (2, 0, 0), (3, 0, 0),
    (1, 0, 1), (2, 0, 1), (3, 0, 1),
    (1, 1, 0), (2, 1, 0), (3, 1, 0),
    (1, 1, 1), (2, 1, 1), (3, 1, 1),
    (1, 2, 1), (2, 2, 1), (3, 2, 1),
]

# ---- 4. Fit, forecast, score ----
results = []
fits = {}
for (p, d, q) in specs:
    try:
        if d == 0:
            trend = 'c'
        elif d == 1:
            trend = 't'   # was 'n'
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
plt.plot(dates_train[-context:], y_train[-context:],
        color='black', lw=1.2, label='Training (recent)')
plt.plot(dates_test, y_test, color='black', lw=2, label='Held-out actual')

highlight = {
    (2, 0, 0): ('AR(2)', 'C0'),
    (1, 1, 1): ('ARIMA(1,1,1)', 'C3'),
    (1, 2, 1): ('ARIMA(1,2,1)', 'C2'),
}

for spec, (label, color) in highlight.items():
    if spec not in fits:
        continue
    mean, ci = fits[spec]
    plt.plot(dates_test, mean, color=color, lw=1.8, label=label)
    plt.fill_between(dates_test, ci[:, 0], ci[:, 1], color=color, alpha=0.15)

plt.axvline(dates_test[0], color='gray', ls='--', lw=0.8)
plt.xlabel('Date')
plt.ylabel('log(GDP)')
plt.title(f'{h}-quarter forecasts with 95% intervals')
plt.legend(loc='upper left')
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

*(2 figures omitted — see the original notebook.)*

### More problems...

Here we see a little less advantage from the $d=2$ model, but it's possible that economic shifts related to the 2008 financial crisis are at play here.. so what if we go even further back, to when the linear trend in GDP was more stable? (pre-2008)?

```python
# ---- 2. Train/test split ----
mask = gdp.index <= '2007-12-31'
y_pre = y_gdp[mask]
dates_pre = gdp.index[mask]

h = 20
y_train = y_pre[:-h]
y_test = y_pre[-h:]
dates_train = dates_pre[:-h]
dates_test = dates_pre[-h:]

# ---- 3. Model grid ----
specs = [
    (1, 0, 0), (2, 0, 0), (3, 0, 0),
    (1, 0, 1), (2, 0, 1), (3, 0, 1),
    (1, 1, 0), (2, 1, 0), (3, 1, 0),
    (1, 1, 1), (2, 1, 1), (3, 1, 1),
    (1, 2, 1), (2, 2, 1), (3, 2, 1),
]

# ---- 4. Fit, forecast, score ----
results = []
fits = {}
for (p, d, q) in specs:
    try:
        if d == 0:
            trend = 'c'
        elif d == 1:
            trend = 't'   # was 'n'
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
plt.plot(dates_train[-context:], y_train[-context:],
        color='black', lw=1.2, label='Training (recent)')
plt.plot(dates_test, y_test, color='black', lw=2, label='Held-out actual')

highlight = {
    (2, 0, 0): ('AR(2)', 'C0'),
    (1, 1, 1): ('ARIMA(1,1,1)', 'C3'),
    (1, 2, 1): ('ARIMA(1,2,1)', 'C2'),
}

for spec, (label, color) in highlight.items():
    if spec not in fits:
        continue
    mean, ci = fits[spec]
    plt.plot(dates_test, mean, color=color, lw=1.8, label=label)
    plt.fill_between(dates_test, ci[:, 0], ci[:, 1], color=color, alpha=0.15)

plt.axvline(dates_test[0], color='gray', ls='--', lw=0.8)
plt.xlabel('Date')
plt.ylabel('log(GDP)')
plt.title(f'{h}-quarter forecasts with 95% intervals')
plt.legend(loc='upper left')
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

*(2 figures omitted — see the original notebook.)*

## What does this mean?

So what does this mean about AR, ARMA, and ARIMA models and their use? In each case, it's very important to understand and plot the underlying data and to look for trends *before* fitting models. For time series data that have multiple underlying trends or more complex behavior, *state space* methods (which we will discuss later) may be more helpful. The steps for building any ARIMA models should be:

1. Plot the data
2. Possibly transform the data (log transform, differencing, etc)
3. Identify the dependence orders of the model (inspect ACF, PACF)
4. Parameter estimation
5. Diagnostics
6. Choosing a model

---

← Stat 153/248 - Lecture 19 · [Up: contents](index.md) · [One more example →](03-one-more-example.md)
