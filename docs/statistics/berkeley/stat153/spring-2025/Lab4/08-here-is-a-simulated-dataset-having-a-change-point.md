---
title: Here is a simulated dataset having a change point
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Here is a simulated dataset having a change point

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

n = 10000
mu1 = 0
mu2 = 0.4
dt = np.concatenate([np.repeat(mu1, n / 2), np.repeat(mu2, n / 2)])

sig = 1
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
allcvals = np.arange(5, n - 4)

---

[← note that the true value of f is 0.2035, b0 is 0, b1 is 3, b2 is 5 and sigma is 10](07-note-that-the-true-value-of-f-is-0-2035-b0-is-0-b1-is-3-b2-i.md) · [Up: contents](index.md) · [we are ignoring a few points at the beginning and at the end →](09-we-are-ignoring-a-few-points-at-the-beginning-and-at-the-end.md)
