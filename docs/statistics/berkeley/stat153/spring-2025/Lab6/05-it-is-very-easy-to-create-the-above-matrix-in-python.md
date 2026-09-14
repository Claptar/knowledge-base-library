---
title: It is very easy to create the above matrix in python
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab6.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab6.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# It is very easy to create the above matrix in python

**Source:** [`Lab6.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab6.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

X = np.tril(np.ones((n, n)), k = 0)
```

Derive that the unregularized estimate of $\beta$ is given by:
\begin{equation*}
   \hat{\beta}_0 = y_1 ~~~\text{ and }~~~ \hat{\beta}_t = y_{t+1} - y_t
\end{equation*}
for $t = 1, 2, \dots, n-1$. This can be verified as follows.

```python
unreg_md = sm.OLS(y, X).fit()
print(unreg_md.params)
print(np.diff(y))
print(y[0])
```

```
[ 1.5235854  -6.72350593  8.95217651 ...  1.92407071  8.27388838
 -0.81259816]
[-6.72350593  8.95217651  0.9505676  ...  1.92407071  8.27388838
 -0.81259816]
1.5235853987721568
```

Let us now see the performance of the regularized estimators. The ridge estimator minimizes:
\begin{equation*}
   \sum_{t=1}^n \left(y_t -  \beta_0 - \beta_1 I\{t \geq 2 \} - \beta_2 I\{t \geq 3 \} - \dots - \beta_{n-1} I\{t \ge n \}\right)^2 + \lambda \sum_{t=1}^{n-1} \beta_t^2
\end{equation*}
and the LASSO estimator minimizes
\begin{equation*}
   \sum_{t=1}^n \left(y_t -  \beta_0 - \beta_1 I\{t \geq 2 \} - \beta_2 I\{t \geq 3 \} - \dots - \beta_{n-1} I\{t \ge n \}\right)^2 + \lambda \sum_{t=1}^{n-1} |\beta_t|
\end{equation*}

We use the following functions (from class) to compute the ridge and lasso estimators.

```python

---

[← Create plot similar to R's plot with type="l" (line)](04-create-plot-similar-to-r-s-plot-with-type-l-line.md) · [Up: contents](index.md) · [note that penaltystart is now set to 1 (instead of 2 as in the model used in class) →](06-note-that-penaltystart-is-now-set-to-1-instead-of-2-as-in-th.md)
