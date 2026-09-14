---
title: Fitted Values
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab2.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Fitted Values

**Source:** [`Lab2.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab2.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

The next quantity to understand are the fitted values. These are given by model.fittedvalues and they are obtained via the simple formula:
\begin{equation*}
   \hat{y} = X \hat{\beta}
\end{equation*}
The entries $\hat{y}_1, \dots, \hat{y}_n$ of the vector $\hat{y}$ are known as the fitted values. Let us check the correctness of this formula.

```python
fvals = np.dot(X, betahat)

print(np.column_stack([fvals[:10], md.fittedvalues[:10]]))
```

```
[[289.68007406 289.68007406]
 [287.33190609 287.33190609]
 [285.14356157 285.14356157]
 [283.1190286  283.1190286 ]
 [281.26229528 281.26229529]
 [279.57734972 279.57734972]
 [278.06818001 278.06818001]
 [276.73877426 276.73877426]
 [275.59312056 275.59312056]
 [274.63520702 274.63520702]]
```

To assess how well the regression model fits the data, we plot the fitted values along with the original data.

```python
plt.plot(y, label = "Data")
plt.plot(md.fittedvalues, label = "Fitted values")
plt.legend()
plt.xlabel("Time (quarterly)")
plt.ylabel("Billions of Dollars")
plt.title("Gross Domestic Product (GDP) of the United States")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Least Squares Estimates](02-least-squares-estimates.md) · [Up: contents](index.md) · [Residuals →](04-residuals.md)
