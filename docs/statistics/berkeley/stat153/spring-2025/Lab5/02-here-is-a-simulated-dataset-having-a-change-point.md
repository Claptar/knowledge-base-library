---
title: Here is a simulated dataset having a change point
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Here is a simulated dataset having a change point

**Source:** [`Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

n = 10000
mu1 = 0
mu2 = 0.4
dt = np.concatenate([np.repeat(mu1, n/2), np.repeat(mu2, n/2)])
sig = 1

rng = np.random.default_rng(seed = 42)
errorsamples = rng.normal(loc = 0, scale = sig, size = n)

y = dt + errorsamples
```

```python
plt.figure(figsize = (15, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
def rss(c):
    x = np.arange(1, n + 1)
    xc = (x > c).astype(float)
    X = np.column_stack([np.ones(n), xc])

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    return rss
```

```python
allcvals = np.arange(1, n)
rssvals = np.array([rss(c) for c in allcvals])
```

```python
plt.plot(allcvals, rssvals)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
c_hat = allcvals[np.argmin(rssvals)]
print(c_hat)
```

```
5045
```

```python

---

[← Change-point model](01-change-point-model.md) · [Up: contents](index.md) · [Estimates of other parameters →](03-estimates-of-other-parameters.md)
