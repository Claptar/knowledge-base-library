---
title: '---- 4. Fit, forecast, score ----'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture19.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ---- 4. Fit, forecast, score ----

**Source:** [`public/lectures/Lecture19.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

---

[← ---- 3. Model grid ----](24------3-model-grid.md) · [Up: contents](index.md) · [RMSE vs. complexity →](26-rmse-vs-complexity.md)
