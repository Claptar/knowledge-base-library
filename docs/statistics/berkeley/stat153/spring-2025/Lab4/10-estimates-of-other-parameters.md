---
title: Estimates of other parameters
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Estimates of other parameters

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

x = np.arange(1, n + 1)
xc = (x > c_hat).astype(float)
X = np.column_stack([np.ones(n), xc])

md = sm.OLS(y, X).fit()
print(md.params)

---

[← we are ignoring a few points at the beginning and at the end](09-we-are-ignoring-a-few-points-at-the-beginning-and-at-the-end.md) · [Up: contents](index.md) · [Lab4 Part 11 — →](11-lab4-part-11.md)
