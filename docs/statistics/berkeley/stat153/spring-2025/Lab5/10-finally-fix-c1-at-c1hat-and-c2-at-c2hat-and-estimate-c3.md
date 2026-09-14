---
title: Finally fix c1 at c1hat, and c2 at c2hat and estimate c3
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Finally fix c1 at c1hat, and c2 at c2hat and estimate c3

**Source:** [`Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

def rss3(c):
    x = np.arange(1, n + 1)
    xc1hat = (x > c1_hat).astype(float)
    xc2hat = (x > c2_hat).astype(float)
    xc = (x > c).astype(float)
    X = np.column_stack([np.ones(n), xc1hat, xc2hat, xc])

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    return rss

allcvals = np.arange(1, n)
rss3vals = np.array([rss3(c) for c in allcvals])

c3_hat = allcvals[np.argmin(rss3vals)]
print(c3_hat)
```

```
300
```

In this example, this iterative scheme (which runs much much faster than joint grid minimization) gives the same estimates as the full grid search.

---

[← Next fix c1 at c1hat and estimate c2](09-next-fix-c1-at-c1hat-and-estimate-c2.md) · [Up: contents](index.md)
