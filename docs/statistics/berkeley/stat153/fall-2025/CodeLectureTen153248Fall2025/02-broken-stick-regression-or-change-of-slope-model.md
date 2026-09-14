---
title: Broken-stick Regression or Change of Slope Model
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Broken-stick Regression or Change of Slope Model

**Source:** [`CodeLectureTen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

The simple linear regression model obviously does not provide a good fit to the data. For an improved model, let us consider:
\begin{equation*}
    y_t = \beta_0 + \beta_1 t + \beta_2 (t - c)_+ + \epsilon_t
\end{equation*}
This model uses $\beta_1$ for the slope before $c$, and $\beta_1 + \beta_2$ for the slope after $c$. We estimated $c$ by the following:

1. For each fixed value of $c$, calculate RSS
2. Use the value of $c$ with the smallest RSS as the estimate

```python
def rss(c):
    x = np.arange(1, n+1)
    x_c = np.maximum(0, x - c)
    X = np.column_stack((np.ones(n), x, x_c))
    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)
    return rss
```

We compute $RSS(c)$ for each $c$ in a grid of values of $c$ as follows.

```python
num_c_vals = 1000 #this is the number of different values of c we will try
allcvals = np.linspace(1, n, num_c_vals)
rssvals = np.array([rss(c) for c in allcvals])
plt.plot(allcvals, rssvals)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The estimate $\hat{c}$ is obtained by minimizing $RSS(c)$ as follows.

```python
c_hat = allcvals[np.argmin(rssvals)]
print(c_hat)
print(c_hat - 1 + tme[0]) #this is the estimated year when the slope changes
rss_smallest = np.min(rssvals)
print(rss_smallest)
```

```
66.28928928928929
1965.2892892892892
0.3490460776066189
```

The fitted values will now look much better than before.

```python
c = c_hat
x = np.arange(1, n+1)
x_c = np.maximum(0, x - c)
X = np.column_stack((np.ones(n), x, x_c))
md = sm.OLS(y, X).fit()
plt.plot(tme, y)
plt.plot(tme, md.fittedvalues, color = 'red')
plt.axvline(c_hat - 1 + tme[0], color='green', linestyle='--')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Point estimates of the other parameters $\beta_0, \beta_1, \beta_2$ are obtained as follows.

```python
#Estimates of other parameters:
c = c_hat
x = np.arange(1, n+1)
x_c = np.maximum(0, x - c)
X = np.column_stack((np.ones(n), x, x_c))
md = sm.OLS(y, X).fit()
print(md.params) #this gives estimates of beta_0, beta_1, beta_2
```

```
const    7.369373
x1       0.037996
x2      -0.024062
dtype: float64
```

The estimate of $\hat{\beta}_1$ is 0.038 and the estimate of $\hat{\beta}_2$ is $-0.024$. This means that the growth rate before 1965 was 3.8\% while the growth rate after 1965 is $3.8 - 2.4 = 1.4$\%.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Models with more changes of Slope →](03-models-with-more-changes-of-slope.md)
