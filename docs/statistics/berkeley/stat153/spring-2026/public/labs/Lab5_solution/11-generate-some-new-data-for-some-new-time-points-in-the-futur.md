---
title: Generate some new data for some new time points in the future $t2$
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab5_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Generate some new data for some new time points in the future $t2$

**Source:** [`public/labs/Lab5_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

duration2 = 1
t2 = np.arange(t[-1],t[-1]+duration2,step=1/fs)

y_test = B0 + R*np.cos(2*math.pi*f*t2 + phi) + np.sqrt(var_eps)*np.random.randn(len(t2))

plt.plot(t, y, label='original training')
plt.plot(t2, y_test, label='new test data')
plt.legend()
plt.xlabel('t')
plt.ylabel('value');
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← What about new data?](10-what-about-new-data.md) · [Up: contents](index.md) · [Make a new X matrix with the original bestf we estimated from the training data, and →](12-make-a-new-x-matrix-with-the-original-bestf-we-estimated-fro.md)
