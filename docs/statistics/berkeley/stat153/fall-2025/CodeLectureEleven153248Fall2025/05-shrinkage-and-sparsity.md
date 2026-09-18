---
title: Shrinkage and Sparsity
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEleven153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureEleven153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureEleven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureEleven153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Shrinkage and Sparsity

Let us compare the ridge regularized estimates of $\beta$ with the unregularized estimates (unregularized means $\lambda = 0$).

```python
y = y_jan
b_ridge_0 = solve_ridge(Xfull, y, lambda_val = 0)
b_ridge = solve_ridge(Xfull, y, lambda_val = 1000)
plt.scatter(b_ridge_0[2:], b_ridge[2:])
print(b_ridge_0[1], b_ridge[1])
print(b_ridge_0[0], b_ridge[0])
```

```
0.28999999999997206 0.003551957730090027
-0.4599999999999922 -0.18495721415398625
```

*(1 figure omitted — see the original notebook.)*

Note that the $y$-axis above has a much tighter range compared to the $x$-axis. This illustrates the **shrinkage** aspect of ridge regression. It shrinks the unregularized estimates towards zero.

```python
y = y_jan
b_lasso_0 = solve_lasso(Xfull, y, lambda_val = 0)
b_lasso = solve_lasso(Xfull, y, lambda_val = 10)
plt.scatter(b_lasso_0[2:], b_lasso[2:])
print(b_lasso_0[1], b_lasso[1])
print(b_lasso_0[0], b_lasso[0])
```

```
0.290000000008449 -0.00183578311693186
-0.46000000053282925 -0.14899519332692354
```

*(1 figure omitted — see the original notebook.)*

This plot clearly shows that the LASSO sets most coefficients exactly to zero. Compare this plot to the corresponding plot for the ridge estimator. This means that LASSO is setting most of the $\beta_j$'s to zero. This is referred to as **sparsity**.

Ridge estimation results in shrinkage and LASSO estimation results in sparsity.

---

← Cross-validation for picking $\lambda$ · [Up: contents](index.md) · [Simulated Data →](06-simulated-data.md)
