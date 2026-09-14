---
title: Generate some new data for some new time points in the future $t2$
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Generate some new data for some new time points in the future $t2$

**Source:** [`public/lectures/Lecture10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

duration2 = 1
t2 = np.arange(t[-1],t[-1]+duration2,step=1/fs)

y_test = B0 + R*np.cos(2*math.pi*f*t2 + phi) + np.sqrt(var_eps)*np.random.randn(len(t2))

plt.figure(figsize=(5,1))
plt.plot(t, y, label='original training')
plt.plot(t2, y_test, label='new test data')
plt.legend()
plt.xlabel('t')
plt.ylabel('value')

print(len(y_test))
```

```
501
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← Make a new grid of frequencies from 1 to the Nyquist limit](05-make-a-new-grid-of-frequencies-from-1-to-the-nyquist-limit.md) · [Up: contents](index.md) · [Now let's make a new X matrix for our test data of the correct dimensions →](07-now-let-s-make-a-new-x-matrix-for-our-test-data-of-the-corre.md)
