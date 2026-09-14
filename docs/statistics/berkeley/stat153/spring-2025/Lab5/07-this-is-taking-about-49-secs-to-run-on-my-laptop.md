---
title: this is taking about 49 secs to run on my laptop
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# this is taking about 49 secs to run on my laptop

**Source:** [`Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

```python
min_row = g.loc[g['rss'].idxmin()]
print(min_row)
c_opt = np.array(min_row[: -1])
```

```
x      100.000000
y      198.000000
z      300.000000
rss    432.679714
Name: 61123, dtype: float64
```

```python
plt.plot(y)
plt.axvline(c_opt[0], color = 'red')
plt.axvline(c_opt[1], color = 'red')
plt.axvline(c_opt[2], color = 'red')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The estimates are decent.

To obtain a faster algorithm for estimating $c_1, c_2, c_3$, we can try the following iterative algorithm. First we obtain $\hat{c}_1$ by solving single change-point RSS minimization:
\begin{equation*}
   \hat{c}_1 = \argmin_{c_1} \min_{\beta_0, \beta_1} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 I\{t > c_1\})^2.
\end{equation*}
Then we obtain $\hat{c}_2$ by two-change point RSS minimization with the first change-point fixed at $\hat{c}_1$:
\begin{equation*}
   \hat{c}_2 = \argmin_{c_2} \min_{\beta_0, \beta_1, \beta_2} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 I\{t > \hat{c}_1\} - \beta_2 I\{t > c_2\})^2.
\end{equation*}
Finally we determine $\hat{c}_3$ by three-change point RSS minimization with the first change-point fixed at $\hat{c}_1$ and the second change-point fixed at $\hat{c}_2$:
\begin{equation*}
   \hat{c}_3 = \argmin_{c_3} \min_{\beta_0, \beta_1, \beta_2, \beta_3} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 I\{t > \hat{c}_1\} - \beta_2 I\{t > \hat{c}_2\} - \beta_3 I\{t > c_3\})^2.
\end{equation*}
Here is the algorithm.

```python

---

[← Plotting only the change-point samples](06-plotting-only-the-change-point-samples.md) · [Up: contents](index.md) · [First estimate c1 as in the single change-point model →](08-first-estimate-c1-as-in-the-single-change-point-model.md)
