---
title: Least Squares Estimates
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab2.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Least Squares Estimates

**Source:** [`Lab2.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab2.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

The information on the estimates $\hat{\beta}_0, \hat{\beta}_1, \hat{\beta}_2, \hat{\beta}_3$ along with associated uncertainties (standard errors) are given in the table near the middle of the output. Specifically, the estimates from the above table are $\hat{\beta}_0 = 292.181$, $\hat{\beta}_1 = -2.5806$, $\hat{\beta}_2 = 0.0759$, and $\hat{\beta}_3 = 0.0007$. These numbers can also be obtained using model.params as follows:

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


These estimates are known as the Least Squares Estimates (also the same as Maximum Likelihood Estimates), and they are computed via the formula:
\begin{equation*}
   \hat{\beta} = \begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \\ \hat{\beta}_2 \\ \hat{\beta}_3 \end{pmatrix} = (X^T X)^{-1} X^T y.
\end{equation*}
Let us verify that this formula indeed gives the reported estimates.

```python
XTX = np.dot(X.T, X)
#XTX = np.matmul(X.T, X)
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

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Fitted Values →](03-fitted-values.md)
