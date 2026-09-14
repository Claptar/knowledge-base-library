---
title: Generating Data using the above smooth function
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Generating Data using the above smooth function

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

tau_t = np.exp(alpha_true)
rng = np.random.default_rng(seed = 42)
y = rng.normal(loc = 0, scale = tau_t)

plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The goal is to get back the estimates of $\alpha_t$ from the above data.

We rescale $x$ below (but not $y$). Note that this model is not invariant to rescaling both $y$ and $x$.

```python

---

[← the following is the true alphat function](13-the-following-is-the-true-alphat-function.md) · [Up: contents](index.md) · [we rescale x but not y →](15-we-rescale-x-but-not-y.md)
