---
title: Summary of the posterior samples
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Summary of the posterior samples

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

pd.DataFrame(post_samples).describe()
```

```
0            1            2            3
count  1000.000000  1000.000000  1000.000000  1000.000000
mean   4990.655000    -0.007485     0.413230     1.002923
std      10.042451     0.014443     0.020551     0.007168
min    4931.000000    -0.053492     0.353096     0.978639
25%    4986.000000    -0.017177     0.399384     0.998240
50%    4989.000000    -0.007820     0.413441     1.002838
75%    4993.000000     0.002567     0.425842     1.007765
max    5104.000000     0.038280     0.483661     1.027721
```

## Change of Slope (or Broken Stick Regression)

Now consider the model:
\begin{equation*}
  y_t = \beta_0 + \beta_1 t + \beta_2 (t - c)_+ + \epsilon_t
\end{equation*}
Here $(t - c)_+ = \max(t-c, 0)$ denotes the positive part function (also known as the ReLU function). This model has parameters $\beta_, \beta_1, \beta_2$ **and** $c$ (as well as $\sigma$). This is a nonlinear regression model because of the presence of the parameter $c$. If a known value is plugged in for $c$, we would revert to a linear regression model.

This model states that, until the time point $c$, the slope parameter equals $\beta_1$. After $c$, the slope parameter becomes $\beta_1 + \beta_2$.

Let us fit this model to the US population dataset that we previously used in the class.

```python
uspop = pd.read_csv("POPTHM-Jan2025FRED.csv")
y = uspop['POPTHM']
n = len(y)

plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

For obtaining the MLEs, we proceed exactly as before. The RSS is now given by:
\begin{equation*}
    RSS(c) = \min_{\beta_0, \beta_1, \beta_2} \sum_{t=1}^n \left(y_t - \beta_0 - \beta_1 t - \beta_2 (t - c)_+ \right)^2
\end{equation*}

```python
def rss(c):
    x = np.arange(1, n + 1)
    xc = ((x > c).astype(float)) * (x - c)
    X = np.column_stack([np.ones(n), x, xc])

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    return rss
```

```python
allcvals = np.arange(5, n - 4) # we are ignoring a few points at the beginning and at the end
rssvals = np.array([rss(c) for c in allcvals])

plt.plot(allcvals, rssvals)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
c_hat = allcvals[np.argmin(rssvals)]
print(c_hat)
```

```
298
```

```python

---

[← this plot looks similar to the RSS plot](13-this-plot-looks-similar-to-the-rss-plot.md) · [Up: contents](index.md) · [Estimates of other parameters →](15-estimates-of-other-parameters.md)
