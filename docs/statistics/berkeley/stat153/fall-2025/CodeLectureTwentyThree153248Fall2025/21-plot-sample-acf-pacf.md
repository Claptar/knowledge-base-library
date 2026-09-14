---
title: Plot sample ACF/PACF
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyThree153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot sample ACF/PACF

**Source:** [`CodeLectureTwentyThree153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyThree153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 4))
plot_acf(ylog2d.dropna(), lags=L, ax=ax1, title='Sample ACF')
plot_pacf(ylog2d.dropna(), lags=L, ax=ax2, title='Sample PACF')
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It appears  hard to determine the orders for an appropriate SARIMA model directly from the above ACF and PACF plot. Below we use a brute force approach where we enumerate a whole bunch of $ARIMA(p, d, q) \times (P, D, Q)_{12}$ models, and then pick the best model via the AIC and BIC criteria.

```python
import warnings
warnings.filterwarnings("ignore") #this suppresses convergence warnings.


dt = ylog
pmax, dmax, qmax = 2, 1, 2
Pmax, D, Qmax = 2, 1, 2
seasonal_period = 12

results = []

for p in range(pmax + 1):
    for d in range(dmax + 1):
        for q in range(qmax + 1):
            for P in range(Pmax + 1):
                for Q in range(Qmax + 1):
                    try:
                        model = ARIMA(dt,
                                      order=(p, d, q),
                                      seasonal_order=(P, D, Q, seasonal_period)).fit()
                        results.append({
                            'p': p, 'd': d, 'q': q,
                            'P': P, 'D': D, 'Q': Q,
                            'AIC': model.aic,
                            'BIC': model.bic
                        })
                    # Progress message
                        print(f"Successfully fit ARIMA({p},{d},{q})x({P},{D},{Q})")
                    except Exception as e:
                        print(f"ARIMA({p},{d},{q})x({P},{D},{Q}) failed: {e}")
                        continue

---

[← Display results](20-display-results.md) · [Up: contents](index.md) · [Convert results to DataFrame →](22-convert-results-to-dataframe.md)
