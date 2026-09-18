---
title: Residuals
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLabTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwo153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Residuals

The residuals simply are the differences between the observed data and the fitted values. We use the notation $e$ for the vector of residuals:
\begin{equation*}
  e = y - \hat{y}
\end{equation*}
The $i^{th}$ residual is simply the $i^{th}$ entry of $e$.

```python
residuals = y - fvals
print(np.column_stack([md.resid[:10], residuals[:10]]))
```

```
[[-46.51607406 -46.51607406]
 [-41.36390609 -41.36390609]
 [-35.55856157 -35.55856157]
 [-23.3740286  -23.3740286 ]
 [-15.52029529 -15.52029528]
 [ -7.01034972  -7.01034972]
 [  1.12781999   1.12781999]
 [  3.62722574   3.62722574]
 [ -0.55912056  -0.55912056]
 [ -3.28420702  -3.28420702]]
```

A plot of the residuals against time is an important diagnostic tool which can tell us about the effectiveness of the fitted model.

```python
plt.plot(md.resid)
plt.xlabel("Time (quarterly)")
plt.ylabel("Billions of Dollars")
plt.title("Residuals")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

From this plot, we see that there are some very large residuals indicating the presence of time points where the model predictions are quite far off from the observed values. This could be because of outliers or some systematic features that the model is missing. Also the residual plot looks quite smooth which indicates that there is some correlation between nearby residuals. This can be better visualized via the **acf plot** (sometimes known as the correlogram) of the residuals.

```python
# For comparison
gamma = np.array([300.0, -3.0, 0.1, 0.001])
z = np.dot(X, gamma) + np.random.normal(0, 1, X.shape[0])

sim_model = sm.OLS(z, X).fit()
print(sim_model.params)

plt.plot(sim_model.resid)
plt.xlabel("Time (quarterly)")
plt.ylabel("Billions of Dollars")
plt.title("Residuals")
plt.show()
```

```
[ 2.99767066e+02 -2.99623705e+00  9.99834849e-02  1.00002346e-03]
```

*(1 figure omitted — see the original notebook.)*

---

[← Least Squares Estimates](02-least-squares-estimates.md) · [Up: contents](index.md) · [ACF Plot →](04-acf-plot.md)
