---
title: Least Squares Estimates
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwo153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabTwo153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLabTwo153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabTwo153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Least Squares Estimates

The information on the estimates $\hat{\beta}_0, \hat{\beta}_1, \hat{\beta}_2, \hat{\beta}_3$ along with associated uncertainties (standard errors) are given in the table near the middle of the output. Specifically, the estimates from the above table are $\hat{\beta}_0 = 292.181$, $\hat{\beta}_1 = -2.5806$, $\hat{\beta}_2 = 0.0759$ and $\hat{\beta}_3 = 0.0007$. These numbers can also be obtained using model.params as follows:

```python
print(md.params)
```

```
const    292.184077
x1        -2.580592
x2         0.075924
x3         0.000665
dtype: float64
```

These estimates are known as the Least Squares Estimates (also the same as Maximum Likelihood Estimates) and they are computed via the formula:
\begin{equation*}
   \hat{\beta} = \begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \\ \hat{\beta}_2 \\ \hat{\beta}_3 \end{pmatrix} = (X^T X)^{-1} X^T y.
\end{equation*}
Let us verify that this formula indeed gives the reported estimates.

```python
XTX = np.dot(X.T, X)
XTX_inverse = np.linalg.inv(XTX)
XTX_inverse_XT = np.dot(XTX_inverse, X.T)
betahat = np.dot(XTX_inverse_XT, y)

print(np.column_stack([betahat, md.params]))
```

```
[[ 2.92184077e+02  2.92184077e+02]
 [-2.58059163e+00 -2.58059163e+00]
 [ 7.59236235e-02  7.59236235e-02]
 [ 6.64683542e-04  6.64683542e-04]]
```

In reality, sm.OLS does not use the above formula directly (even though the formula is the correct one), instead it uses some efficient linear algebra methods to solve the linear equations $X^T X \beta = X^T y$.

## Fitted Values

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

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Residuals →](03-residuals.md)
