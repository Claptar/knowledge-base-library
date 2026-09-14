---
title: Prediction 168 months ahead
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb
source_file: sources/berkeley-stat153/fall-2026/CodeLectureTwo153248Fall2026.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Prediction 168 months ahead

**Source:** [`CodeLectureTwo153248Fall2026.ipynb`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureTwo153248Fall2026.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print("Prediction 168 months ahead:", y_future[-1])
```

```
Prediction 168 months ahead: 412762.30604638177
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize=(6, 4))

plt.plot(x, y, label="Observed data")
plt.plot(x_future, y_future, label="Predictions")

plt.xlabel("Time (months)")
plt.ylabel("Population (thousands)")
plt.title("Observed U.S. Population and Model 2 Predictions")
plt.legend()

plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Model 3: $\log y_t = \beta_0 + \beta_1 t + \beta_2 t^2 + \epsilon_t$

$\log y_t = \beta_0 + \beta_1 t + \beta_2 t^2 + \epsilon_t$. The growth rate now is $d \log y_t/dt = \beta_1+ 2 \beta_2 t$. So this allows the growth rate to change with $t$ (we would expect $\beta_2$ to be negative which would explain the decaying growth rate).

```python

---

[← Plot observed data, fitted values, and future predictions](08-plot-observed-data-fitted-values-and-future-predictions.md) · [Up: contents](index.md) · [Model 3: $\log yt = \beta0 + \beta1 t + \beta2 t^2 + \epsilont$ →](10-model-3.md)
