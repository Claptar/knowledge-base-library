---
title: What about choosing the number of parameters?
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# What about choosing the number of parameters?

**Source:** [`public/lectures/Lecture10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Here we had two straw man scenarios -- one where we have one frequency (which we know is our "true" model), and the other where we use many frequencies to perfectly approximate our training data. However, we may not always know how many frequencies we should actually choose, so we may need to search over many candidate frequencies and determine which to include in the model.

We'll try that here by testing each of the frequencies and ranking them by their individual RSS values:

```python
var_eps = 5
y2 = B0 + np.cos(2*math.pi*5.55*t + 0.12) + \
  R/2*np.cos(2*math.pi*12.5*t + 0.2) + R*np.cos(2*math.pi*f*t + phi) +\
   np.sqrt(var_eps)*np.random.randn(len(t))

plt.plot(t,y2)

rss_per_freq = []
for f_candidate in f_grid:
    X = np.column_stack([np.ones(len(t)),
                         np.cos(2*np.pi*f_candidate*t),
                         np.sin(2*np.pi*f_candidate*t)])
    model = sm.OLS(y2, X).fit()
    rss_per_freq.append(model.ssr)

---

[← This is cheating!](14-this-is-cheating.md) · [Up: contents](index.md) · [Sort from lowest RSS to highest RSS (best to worst) →](16-sort-from-lowest-rss-to-highest-rss-best-to-worst.md)
