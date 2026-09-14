---
title: First estimate c1 as in the single change-point model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# First estimate c1 as in the single change-point model

**Source:** [`Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

def rss(c):
    x = np.arange(1, n + 1)
    xc = (x > c).astype(float)
    X = np.column_stack([np.ones(n), xc])

    md = sm.OLS(y, X).fit()
    rss = np.sum(md.resid ** 2)

    return rss

allcvals = np.arange(1, n)
rssvals = np.array([rss(c) for c in allcvals])

c1_hat = allcvals[np.argmin(rssvals)]
print(c1_hat)
```

```
198
```

```python

---

[← this is taking about 49 secs to run on my laptop](07-this-is-taking-about-49-secs-to-run-on-my-laptop.md) · [Up: contents](index.md) · [Next fix c1 at c1hat and estimate c2 →](09-next-fix-c1-at-c1hat-and-estimate-c2.md)
