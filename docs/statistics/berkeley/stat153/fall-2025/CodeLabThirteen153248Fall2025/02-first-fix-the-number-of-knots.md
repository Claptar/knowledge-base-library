---
title: First fix the number of knots
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# First fix the number of knots

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

k = 4

quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
knots_init = np.quantile(x_raw, quantile_levels)

n = len(y_raw)
X = np.column_stack([np.ones(n), x_raw])
for j in range(k):
    xc = ((x_raw > knots_init[j]).astype(float)) * (x_raw - knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(y_raw, X).fit()
beta_init = md_init.params.values

print(knots_init)
print(beta_init)
```

```
[ 56.4 111.8 167.2 222.6]
[52167.91700846   628.19139706 -1505.22955093  1506.51113458
  -264.69041849   565.3087544 ]
```

Once the initial values are determined, we construct our model.

```python

---

[← More on model fitting using PyTorch](01-more-on-model-fitting-using-pytorch.md) · [Up: contents](index.md) · [Define a model →](03-define-a-model.md)
