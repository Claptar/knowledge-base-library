---
title: What about choosing the number of parameters?
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# What about choosing the number of parameters?

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

# Sort from lowest RSS to highest RSS (best to worst)
ranked_idx = np.argsort(rss_per_freq)
ranked_freqs = f_grid[ranked_idx]

print(ranked_freqs[:10])
```

```
[ 2.50501002  2.00400802 12.5250501   5.51102204  3.00601202  3.50701403
  1.50300601  4.00801603  5.01002004 93.68737475]
```

*(1 figure omitted — see the original notebook.)*

```python
# Now CV over how many top frequencies to include
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.linear_model import LinearRegression

cv = TimeSeriesSplit(n_splits=5)
mean_scores = []
n_freq_range = range(1, 30)

for n_freqs in n_freq_range:
    cols = [np.ones(len(t))]
    for f_k in ranked_freqs[:n_freqs]:
        cols.append(np.cos(2*np.pi*f_k*t))
        cols.append(np.sin(2*np.pi*f_k*t))
    X = np.column_stack(cols)
    scores = cross_val_score(LinearRegression(), X, y, cv=cv,
                            scoring='neg_mean_squared_error')
    mean_scores.append(-scores.mean())

plt.plot(list(n_freq_range), mean_scores)
plt.xlabel('Number of frequencies')
plt.ylabel('CV MSE')
```

---

[← Lecture 10 - Regularization](01-lecture-10---regularization.md) · [Up: contents](index.md)
