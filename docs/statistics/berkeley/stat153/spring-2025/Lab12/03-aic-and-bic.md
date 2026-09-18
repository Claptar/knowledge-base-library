---
title: AIC and BIC
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# AIC and BIC

In lectures this week, we used AIC and BIC to do model selection. The formulae for AIC and BIC are:
\begin{equation*}
   AIC \text{ for model} = (-2) \times \text{maximized log-likelihood for model} + 2 \times \text{number of parameters in the model}
\end{equation*}
and
\begin{equation*}
     BIC \text{ for model} = (-2) \times \text{maximized log-likelihood for model} + (\log \text{~sample size}) \times \text{number of parameters in the model}
\end{equation*}

Let us compute these for each of the models and check if the answer matches the one given by the model function.

```python
n = len(y)
mod1_aic_formula = -2 * mod1_arima.llf + 2 * len(mod1_arima.params)
mod1_bic_formula = -2 * mod1_arima.llf + (np.log(n - 1)) * len(mod1_arima.params)
print(mod1_aic_formula, mod1_arima.aic)
print(mod1_bic_formula, mod1_arima.bic)
# Note that we have used (n - 1) for sample size in the calculation for BIC
# because this model is really applied to the differenced data and there are n - 1 first differences
```

```
-2364.494873895399 -2364.494873895399
-2344.72865722396 -2344.72865722396
```

```python
n = len(y)
mod2_aic_formula = -2 * mod2.llf + 2 * len(mod2.params)
mod2_bic_formula = -2 * mod2.llf + (np.log(n - 1)) * len(mod2.params)
print(mod2_aic_formula, mod2.aic)
print(mod2_bic_formula, mod2.bic)
```

```
-2354.933614650533 -2354.933614650533
-2339.120641313382 -2339.120641313382
```

```python
n = len(y)
mod3_aic_formula = -2 * mod3.llf + 2 * len(mod3.params)
mod3_bic_formula = -2 * mod3.llf + (np.log(n - 2)) * len(mod3.params)
print(mod3_aic_formula, mod3.aic)
print(mod3_bic_formula, mod3.bic)
# Now we are using (n - 2) for sample size in the calculation of BIC
# because this model is applied to the twice-differenced data and there are n - 2 second order differences.
```

```
-2357.3214233532403 -2357.3214233532403
-2349.420138248065 -2349.420138248065
```

```python
n = len(y)
mod4_aic_formula = -2 * mod4.llf + 2 * len(mod4.params)
mod4_bic_formula = -2 * mod4.llf + (np.log(n - 2)) * len(mod4.params)
print(mod4_aic_formula, mod4.aic)
print(mod4_bic_formula, mod4.bic)
# Again we are using (n - 2) for sample size in the calculation of BIC
# because this model is applied to the twice-differenced data and there are n - 2 second order differences.
```

```
-2356.33062605351 -2356.33062605351
-2332.626770737984 -2332.626770737984
```

---

[← TTLCONS (Total Construction Spending Data)](02-ttlcons-total-construction-spending-data.md) · [Up: contents](index.md)
