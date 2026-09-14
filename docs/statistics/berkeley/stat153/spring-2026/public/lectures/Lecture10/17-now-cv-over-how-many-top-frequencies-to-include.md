---
title: Now CV over how many top frequencies to include
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Now CV over how many top frequencies to include

**Source:** [`public/lectures/Lecture10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

[← Sort from lowest RSS to highest RSS (best to worst)](16-sort-from-lowest-rss-to-highest-rss-best-to-worst.md) · [Up: contents](index.md)
