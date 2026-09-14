---
title: Next fix c1 at c1hat and estimate c2
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Next fix c1 at c1hat and estimate c2

**Source:** [`Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

def rss2(c):
    x = np.arange(1, n + 1)
    xc1hat = (x > c1_hat).astype(float)
    xc = (x > c).astype(float)
    X = np.column_stack([np.ones(n), xc1hat, xc])

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    return rss

allcvals = np.arange(1, n)
rss2vals = np.array([rss2(c) for c in allcvals])

c2_hat = allcvals[np.argmin(rss2vals)]
print(c2_hat)
```

```
100
```

```python

---

[← First estimate c1 as in the single change-point model](08-first-estimate-c1-as-in-the-single-change-point-model.md) · [Up: contents](index.md) · [Finally fix c1 at c1hat, and c2 at c2hat and estimate c3 →](10-finally-fix-c1-at-c1hat-and-c2-at-c2hat-and-estimate-c3.md)
