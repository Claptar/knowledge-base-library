---
title: Print results
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Print results

**Source:** [`CodeLectureTwentyTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyTwo153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print(f"Best AR model by AIC: AR({best_ar_aic})")
print(f"Best AR model by BIC: AR({best_ar_bic})")

print(f"Best MA model by AIC: MA({best_ma_aic})")
print(f"Best MA model by BIC: MA({best_ma_bic})")

print(f"Best ARMA model by AIC: ARMA{best_arma_aic}")
print(f"Best ARMA model by BIC: ARMA{best_arma_bic}")
```

```
Best AR model by AIC: AR(5)
Best AR model by BIC: AR(3)
Best MA model by AIC: MA(5)
Best MA model by BIC: MA(3)
Best ARMA model by AIC: ARMA(1, 1)
Best ARMA model by BIC: ARMA(1, 1)
```

Best AR model: AR(3) (using BIC) and AR(5) (using AIC)

Best MA model: MA(3) (using BIC) and MA(5) (using AIC)

Best overall ARMA model: ARMA(1, 1)

Instead of fitting the best model to ylogdiff, we can find best models for ylog (in this case, we shall use ARIMA(p, d, q) and vary p, d, q).

```python
import warnings
warnings.filterwarnings("ignore") #this suppresses convergence warnings.


dt = ylog
pmax, dmax, qmax = 5, 2, 5

results = []

for p in range(pmax + 1):
    for d in range(dmax + 1):
        for q in range(qmax + 1):

            # Use linear trend only when d = 1
            #trend = 't' if d == 1 else None
            #trend = None

            try:
                model = ARIMA(dt, order=(p, d, q)).fit()

                results.append({
                    'p': p, 'd': d, 'q': q,
                    'AIC': model.aic,
                    'BIC': model.bic
                })
            except Exception as e:
                print(f"ARIMA({p},{d},{q}) failed: {e}")
                continue

---

[← Best ARMA model overall](10-best-arma-model-overall.md) · [Up: contents](index.md) · [Convert to DataFrame →](12-convert-to-dataframe.md)
